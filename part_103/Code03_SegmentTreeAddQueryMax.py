# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 线段树支持范围增加、范围查询
# 维护最大值
# 对数器验证
# 当你写线段树出错了，就需要用对数器的方式来排查
# 所以本题选择对数器验证，来展示一下怎么写测试
class Code03_SegmentTreeAddQueryMax:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'max': 'max', 'add': 'add_data'}
    MAXN = 0
    arr = None
    max = None
    add_data = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        jset(Code03_SegmentTreeAddQueryMax.max, i, jstatic('Math', 'max', Code03_SegmentTreeAddQueryMax.max[jcast('int', (i << (1 & 31)))], Code03_SegmentTreeAddQueryMax.max[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if (Code03_SegmentTreeAddQueryMax.add_data[i] != 0):
            Code03_SegmentTreeAddQueryMax.lazy(jcast('int', (i << (1 & 31))), Code03_SegmentTreeAddQueryMax.add_data[i])
            Code03_SegmentTreeAddQueryMax.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code03_SegmentTreeAddQueryMax.add_data[i])
            Code03_SegmentTreeAddQueryMax.add_data[i] = jcast('long', 0)

    @staticmethod
    def lazy(i, v):
        i = jcast('int', i)
        v = jcast('long', v)
        Code03_SegmentTreeAddQueryMax.max[i] = jcast('long', jcast('long', jadd(Code03_SegmentTreeAddQueryMax.max[i], v)))
        Code03_SegmentTreeAddQueryMax.add_data[i] = jcast('long', jcast('long', jadd(Code03_SegmentTreeAddQueryMax.add_data[i], v)))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code03_SegmentTreeAddQueryMax.max[i] = jcast('long', Code03_SegmentTreeAddQueryMax.arr[l])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code03_SegmentTreeAddQueryMax.build(l, mid, jcast('int', (i << (1 & 31))))
            Code03_SegmentTreeAddQueryMax.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code03_SegmentTreeAddQueryMax.up(i)
        Code03_SegmentTreeAddQueryMax.add_data[i] = jcast('long', 0)

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code03_SegmentTreeAddQueryMax.lazy(i, jobv)
        else:
            Code03_SegmentTreeAddQueryMax.down(i)
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code03_SegmentTreeAddQueryMax.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code03_SegmentTreeAddQueryMax.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code03_SegmentTreeAddQueryMax.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code03_SegmentTreeAddQueryMax.max[i])
        Code03_SegmentTreeAddQueryMax.down(i)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('long', jget(Long, 'MIN_VALUE'))
        if (jobl <= mid):
            ans = jcast('long', jstatic('Math', 'max', ans, Code03_SegmentTreeAddQueryMax.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('long', jstatic('Math', 'max', ans, Code03_SegmentTreeAddQueryMax.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('long', ans)

    # 对数器逻辑
    # 展示了线段树的建立和使用
    # 使用验证结构来检查线段树是否正常工作
    @staticmethod
    def main(args):
        jprint('测试开始', newline=True)
        n = jcast('int', 1000)
        v = jcast('int', 2000)
        t = jcast('int', 5000000)
        # 生成随机值填入arr数组
        Code03_SegmentTreeAddQueryMax.randomArray(n, v)
        # 建立线段树
        Code03_SegmentTreeAddQueryMax.build(1, n, 1)
        # 生成验证的结构
        check = jarray('long', [jcast('int', jadd(n, 1))])
        i = jcast('int', 1)
        while (i <= n):
            check[i] = jcast('long', Code03_SegmentTreeAddQueryMax.arr[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= t):
            # 生成操作类型
            # op = 0 增加操作
            # op = 1 查询操作
            op = jcast('int', jcast('int', (jstatic('Math', 'random') * 2)))
            # 下标从1开始，不从0开始，生成两个随机下标
            a = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            b = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            # 确保jobl <= jobr
            jobl = jcast('int', jstatic('Math', 'min', a, b))
            jobr = jcast('int', jstatic('Math', 'max', a, b))
            if (op == 0):
                # 增加操作
                # 线段树、验证结构同步增加
                jobv = jcast('int', jcast('int', (jcast('int', ((jstatic('Math', 'random') * v) * 2)) - v)))
                Code03_SegmentTreeAddQueryMax.add(jobl, jobr, jobv, 1, n, 1)
                Code03_SegmentTreeAddQueryMax.checkAdd(check, jobl, jobr, jobv)
            else:
                # 查询操作
                # 线段树、验证结构同步查询
                # 比对答案
                ans1 = jcast('long', Code03_SegmentTreeAddQueryMax.query(jobl, jobr, 1, n, 1))
                ans2 = jcast('long', Code03_SegmentTreeAddQueryMax.checkQuery(check, jobl, jobr))
                if (ans1 != ans2):
                    jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    # 生成随机值填入arr数组
    # 为了验证
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        i = jcast('int', 1)
        while (i <= n):
            jset(Code03_SegmentTreeAddQueryMax.arr, i, jcast('long', (jstatic('Math', 'random') * v)))
            i = jcast('int', (i + 1))

    # 验证结构的增加
    # 暴力增加
    # 为了验证
    @staticmethod
    def checkAdd(check, jobl, jobr, jobv):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        i = jcast('int', jobl)
        while (i <= jobr):
            check[i] = jcast('long', jcast('long', jadd(check[i], jobv)))
            i = jcast('int', (i + 1))

    # 验证结构的查询
    # 暴力查询
    # 为了验证
    @staticmethod
    def checkQuery(check, jobl, jobr):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        ans = jcast('long', jget(Long, 'MIN_VALUE'))
        i = jcast('int', jobl)
        while (i <= jobr):
            ans = jcast('long', jstatic('Math', 'max', ans, check[i]))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_SegmentTreeAddQueryMax.MAXN = jcast('int', 100001)
Code03_SegmentTreeAddQueryMax.arr = jarray('long', [Code03_SegmentTreeAddQueryMax.MAXN])
Code03_SegmentTreeAddQueryMax.max = jarray('long', [jcast('int', (Code03_SegmentTreeAddQueryMax.MAXN << (2 & 31)))])
Code03_SegmentTreeAddQueryMax.add_data = jarray('long', [jcast('int', (Code03_SegmentTreeAddQueryMax.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code03_SegmentTreeAddQueryMax.main([])
