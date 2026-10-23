# -*- coding: utf-8 -*-
# Python 3 算法实现；中文题意、算法说明与原课程顺序对应。
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 线段树同时支持范围重置、范围增加、范围查询
# 维护累加和
# 对数器验证
# 当你写线段树出错了，就需要用对数器的方式来排查
# 所以本题选择对数器验证，来展示一下怎么写测试
class Code05_SegmentTreeUpdateAddQuerySum:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'sum': 'sum', 'add': 'add_data', 'change': 'change', 'update': 'update_data'}
    MAXN = 0
    arr = None
    sum = None
    add_data = None
    change = None
    update_data = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code05_SegmentTreeUpdateAddQuerySum.sum[i] = jcast('long', jcast('long', jadd(Code05_SegmentTreeUpdateAddQuerySum.sum[jcast('int', (i << (1 & 31)))], Code05_SegmentTreeUpdateAddQuerySum.sum[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))

    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        if Code05_SegmentTreeUpdateAddQuerySum.update_data[i]:
            Code05_SegmentTreeUpdateAddQuerySum.updateLazy(jcast('int', (i << (1 & 31))), Code05_SegmentTreeUpdateAddQuerySum.change[i], ln)
            Code05_SegmentTreeUpdateAddQuerySum.updateLazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code05_SegmentTreeUpdateAddQuerySum.change[i], rn)
            Code05_SegmentTreeUpdateAddQuerySum.update_data[i] = jcast('boolean', False)
        if (Code05_SegmentTreeUpdateAddQuerySum.add_data[i] != 0):
            Code05_SegmentTreeUpdateAddQuerySum.addLazy(jcast('int', (i << (1 & 31))), Code05_SegmentTreeUpdateAddQuerySum.add_data[i], ln)
            Code05_SegmentTreeUpdateAddQuerySum.addLazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code05_SegmentTreeUpdateAddQuerySum.add_data[i], rn)
            Code05_SegmentTreeUpdateAddQuerySum.add_data[i] = jcast('long', 0)

    @staticmethod
    def updateLazy(i, v, n):
        i = jcast('int', i)
        v = jcast('long', v)
        n = jcast('int', n)
        Code05_SegmentTreeUpdateAddQuerySum.sum[i] = jcast('long', jcast('long', (v * n)))
        Code05_SegmentTreeUpdateAddQuerySum.add_data[i] = jcast('long', 0)
        Code05_SegmentTreeUpdateAddQuerySum.change[i] = jcast('long', v)
        Code05_SegmentTreeUpdateAddQuerySum.update_data[i] = jcast('boolean', True)

    @staticmethod
    def addLazy(i, v, n):
        i = jcast('int', i)
        v = jcast('long', v)
        n = jcast('int', n)
        Code05_SegmentTreeUpdateAddQuerySum.sum[i] = jcast('long', jcast('long', jadd(Code05_SegmentTreeUpdateAddQuerySum.sum[i], jcast('long', (v * n)))))
        Code05_SegmentTreeUpdateAddQuerySum.add_data[i] = jcast('long', jcast('long', jadd(Code05_SegmentTreeUpdateAddQuerySum.add_data[i], v)))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code05_SegmentTreeUpdateAddQuerySum.sum[i] = jcast('long', Code05_SegmentTreeUpdateAddQuerySum.arr[l])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code05_SegmentTreeUpdateAddQuerySum.build(l, mid, jcast('int', (i << (1 & 31))))
            Code05_SegmentTreeUpdateAddQuerySum.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code05_SegmentTreeUpdateAddQuerySum.up(i)
        Code05_SegmentTreeUpdateAddQuerySum.add_data[i] = jcast('long', 0)
        Code05_SegmentTreeUpdateAddQuerySum.change[i] = jcast('long', 0)
        Code05_SegmentTreeUpdateAddQuerySum.update_data[i] = jcast('boolean', False)

    @staticmethod
    def update(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code05_SegmentTreeUpdateAddQuerySum.updateLazy(i, jobv, jcast('int', jadd(jcast('int', (r - l)), 1)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code05_SegmentTreeUpdateAddQuerySum.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code05_SegmentTreeUpdateAddQuerySum.update(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code05_SegmentTreeUpdateAddQuerySum.update(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code05_SegmentTreeUpdateAddQuerySum.up(i)

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code05_SegmentTreeUpdateAddQuerySum.addLazy(i, jobv, jcast('int', jadd(jcast('int', (r - l)), 1)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code05_SegmentTreeUpdateAddQuerySum.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code05_SegmentTreeUpdateAddQuerySum.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code05_SegmentTreeUpdateAddQuerySum.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code05_SegmentTreeUpdateAddQuerySum.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code05_SegmentTreeUpdateAddQuerySum.sum[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        Code05_SegmentTreeUpdateAddQuerySum.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
        ans = jcast('long', 0)
        if (jobl <= mid):
            ans = jcast('long', jcast('long', jadd(ans, Code05_SegmentTreeUpdateAddQuerySum.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            ans = jcast('long', jcast('long', jadd(ans, Code05_SegmentTreeUpdateAddQuerySum.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        jprint('测试开始', newline=True)
        n = jcast('int', 1000)
        v = jcast('int', 2000)
        t = jcast('int', 5000000)
        # 生成随机值填入arr数组
        Code05_SegmentTreeUpdateAddQuerySum.randomArray(n, v)
        # 建立线段树
        Code05_SegmentTreeUpdateAddQuerySum.build(1, n, 1)
        # 生成验证的结构
        check = jarray('long', [jcast('int', jadd(n, 1))])
        i = jcast('int', 1)
        while (i <= n):
            check[i] = jcast('long', Code05_SegmentTreeUpdateAddQuerySum.arr[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= t):
            # 生成操作类型
            # op = 0 增加操作
            # op = 1 更新操作
            # op = 2 查询操作
            op = jcast('int', jcast('int', (jstatic('Math', 'random') * 3)))
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
                Code05_SegmentTreeUpdateAddQuerySum.add(jobl, jobr, jobv, 1, n, 1)
                Code05_SegmentTreeUpdateAddQuerySum.checkAdd(check, jobl, jobr, jobv)
            else:
                if (op == 1):
                    # 更新操作
                    # 线段树、验证结构同步更新
                    jobv = jcast('int', jcast('int', (jcast('int', ((jstatic('Math', 'random') * v) * 2)) - v)))
                    Code05_SegmentTreeUpdateAddQuerySum.update(jobl, jobr, jobv, 1, n, 1)
                    Code05_SegmentTreeUpdateAddQuerySum.checkUpdate(check, jobl, jobr, jobv)
                else:
                    # 查询操作
                    # 线段树、验证结构同步查询
                    # 比对答案
                    ans1 = jcast('long', Code05_SegmentTreeUpdateAddQuerySum.query(jobl, jobr, 1, n, 1))
                    ans2 = jcast('long', Code05_SegmentTreeUpdateAddQuerySum.checkQuery(check, jobl, jobr))
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
            jset(Code05_SegmentTreeUpdateAddQuerySum.arr, i, jcast('long', (jstatic('Math', 'random') * v)))
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

    # 验证结构的更新
    # 暴力更新
    # 为了验证
    @staticmethod
    def checkUpdate(check, jobl, jobr, jobv):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        i = jcast('int', jobl)
        while (i <= jobr):
            check[i] = jcast('long', jobv)
            i = jcast('int', (i + 1))

    # 验证结构的查询
    # 暴力查询
    # 为了验证
    @staticmethod
    def checkQuery(check, jobl, jobr):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        ans = jcast('long', 0)
        i = jcast('int', jobl)
        while (i <= jobr):
            ans = jcast('long', jcast('long', jadd(ans, check[i])))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_SegmentTreeUpdateAddQuerySum.MAXN = jcast('int', 1000001)
Code05_SegmentTreeUpdateAddQuerySum.arr = jarray('long', [Code05_SegmentTreeUpdateAddQuerySum.MAXN])
Code05_SegmentTreeUpdateAddQuerySum.sum = jarray('long', [jcast('int', (Code05_SegmentTreeUpdateAddQuerySum.MAXN << (2 & 31)))])
Code05_SegmentTreeUpdateAddQuerySum.add_data = jarray('long', [jcast('int', (Code05_SegmentTreeUpdateAddQuerySum.MAXN << (2 & 31)))])
Code05_SegmentTreeUpdateAddQuerySum.change = jarray('long', [jcast('int', (Code05_SegmentTreeUpdateAddQuerySum.MAXN << (2 & 31)))])
Code05_SegmentTreeUpdateAddQuerySum.update_data = jarray('boolean', [jcast('int', (Code05_SegmentTreeUpdateAddQuerySum.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code05_SegmentTreeUpdateAddQuerySum.main([])
