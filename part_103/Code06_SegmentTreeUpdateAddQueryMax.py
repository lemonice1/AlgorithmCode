# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 线段树同时支持范围重置、范围增加、范围查询
# 维护最大值
# 测试链接 : https://www.luogu.com.cn/problem/P1253
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_SegmentTreeUpdateAddQueryMax:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'max': 'max', 'add': 'add_data', 'change': 'change', 'update': 'update_data'}
    MAXN = 0
    arr = None
    max = None
    add_data = None
    change = None
    update_data = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        jset(Code06_SegmentTreeUpdateAddQueryMax.max, i, jstatic('Math', 'max', Code06_SegmentTreeUpdateAddQueryMax.max[jcast('int', (i << (1 & 31)))], Code06_SegmentTreeUpdateAddQueryMax.max[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if Code06_SegmentTreeUpdateAddQueryMax.update_data[i]:
            Code06_SegmentTreeUpdateAddQueryMax.updateLazy(jcast('int', (i << (1 & 31))), Code06_SegmentTreeUpdateAddQueryMax.change[i])
            Code06_SegmentTreeUpdateAddQueryMax.updateLazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code06_SegmentTreeUpdateAddQueryMax.change[i])
            Code06_SegmentTreeUpdateAddQueryMax.update_data[i] = jcast('boolean', False)
        if (Code06_SegmentTreeUpdateAddQueryMax.add_data[i] != 0):
            Code06_SegmentTreeUpdateAddQueryMax.addLazy(jcast('int', (i << (1 & 31))), Code06_SegmentTreeUpdateAddQueryMax.add_data[i])
            Code06_SegmentTreeUpdateAddQueryMax.addLazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code06_SegmentTreeUpdateAddQueryMax.add_data[i])
            Code06_SegmentTreeUpdateAddQueryMax.add_data[i] = jcast('long', 0)

    @staticmethod
    def updateLazy(i, v):
        i = jcast('int', i)
        v = jcast('long', v)
        Code06_SegmentTreeUpdateAddQueryMax.max[i] = jcast('long', v)
        Code06_SegmentTreeUpdateAddQueryMax.add_data[i] = jcast('long', 0)
        Code06_SegmentTreeUpdateAddQueryMax.change[i] = jcast('long', v)
        Code06_SegmentTreeUpdateAddQueryMax.update_data[i] = jcast('boolean', True)

    @staticmethod
    def addLazy(i, v):
        i = jcast('int', i)
        v = jcast('long', v)
        Code06_SegmentTreeUpdateAddQueryMax.max[i] = jcast('long', jcast('long', jadd(Code06_SegmentTreeUpdateAddQueryMax.max[i], v)))
        Code06_SegmentTreeUpdateAddQueryMax.add_data[i] = jcast('long', jcast('long', jadd(Code06_SegmentTreeUpdateAddQueryMax.add_data[i], v)))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code06_SegmentTreeUpdateAddQueryMax.max[i] = jcast('long', Code06_SegmentTreeUpdateAddQueryMax.arr[l])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code06_SegmentTreeUpdateAddQueryMax.build(l, mid, jcast('int', (i << (1 & 31))))
            Code06_SegmentTreeUpdateAddQueryMax.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code06_SegmentTreeUpdateAddQueryMax.up(i)
        Code06_SegmentTreeUpdateAddQueryMax.add_data[i] = jcast('long', 0)
        Code06_SegmentTreeUpdateAddQueryMax.change[i] = jcast('long', 0)
        Code06_SegmentTreeUpdateAddQueryMax.update_data[i] = jcast('boolean', False)

    @staticmethod
    def update(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code06_SegmentTreeUpdateAddQueryMax.updateLazy(i, jobv)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code06_SegmentTreeUpdateAddQueryMax.down(i)
            if (jobl <= mid):
                Code06_SegmentTreeUpdateAddQueryMax.update(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code06_SegmentTreeUpdateAddQueryMax.update(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code06_SegmentTreeUpdateAddQueryMax.up(i)

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code06_SegmentTreeUpdateAddQueryMax.addLazy(i, jobv)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code06_SegmentTreeUpdateAddQueryMax.down(i)
            if (jobl <= mid):
                Code06_SegmentTreeUpdateAddQueryMax.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code06_SegmentTreeUpdateAddQueryMax.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code06_SegmentTreeUpdateAddQueryMax.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code06_SegmentTreeUpdateAddQueryMax.max[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        Code06_SegmentTreeUpdateAddQueryMax.down(i)
        ans = jcast('long', jget(Long, 'MIN_VALUE'))
        if (jobl <= mid):
            ans = jcast('long', jstatic('Math', 'max', ans, Code06_SegmentTreeUpdateAddQueryMax.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('long', jstatic('Math', 'max', ans, Code06_SegmentTreeUpdateAddQueryMax.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= n):
            jcall(in_, 'nextToken')
            Code06_SegmentTreeUpdateAddQueryMax.arr[i] = jcast('long', jcast('long', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code06_SegmentTreeUpdateAddQueryMax.build(1, n, 1)
        jobv = 0
        i = jcast('int', 1)
        op = 0
        jobl = 0
        jobr = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            if (op == 1):
                jcall(in_, 'nextToken')
                jobl = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jobr = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jobv = jcast('long', jcast('long', jget(in_, 'nval')))
                Code06_SegmentTreeUpdateAddQueryMax.update(jobl, jobr, jobv, 1, n, 1)
            else:
                if (op == 2):
                    jcall(in_, 'nextToken')
                    jobl = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    jobr = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    jobv = jcast('long', jcast('long', jget(in_, 'nval')))
                    Code06_SegmentTreeUpdateAddQueryMax.add(jobl, jobr, jobv, 1, n, 1)
                else:
                    jcall(in_, 'nextToken')
                    jobl = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    jobr = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(out, 'println', Code06_SegmentTreeUpdateAddQueryMax.query(jobl, jobr, 1, n, 1))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_SegmentTreeUpdateAddQueryMax.MAXN = jcast('int', 1000001)
Code06_SegmentTreeUpdateAddQueryMax.arr = jarray('long', [Code06_SegmentTreeUpdateAddQueryMax.MAXN])
Code06_SegmentTreeUpdateAddQueryMax.max = jarray('long', [jcast('int', (Code06_SegmentTreeUpdateAddQueryMax.MAXN << (2 & 31)))])
Code06_SegmentTreeUpdateAddQueryMax.add_data = jarray('long', [jcast('int', (Code06_SegmentTreeUpdateAddQueryMax.MAXN << (2 & 31)))])
Code06_SegmentTreeUpdateAddQueryMax.change = jarray('long', [jcast('int', (Code06_SegmentTreeUpdateAddQueryMax.MAXN << (2 & 31)))])
Code06_SegmentTreeUpdateAddQueryMax.update_data = jarray('boolean', [jcast('int', (Code06_SegmentTreeUpdateAddQueryMax.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code06_SegmentTreeUpdateAddQueryMax.main([])
