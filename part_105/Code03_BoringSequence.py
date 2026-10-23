# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 无聊的数列
# 给定一个长度为n的数组arr，实现如下两种操作
# 操作 1 l r k d : arr[l..r]范围上的数依次加上等差数列，首项k，公差d
# 操作 2 p       : 查询arr[p]的值
# 测试链接 : https://www.luogu.com.cn/problem/P1438
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_BoringSequence:
    __java_fields__ = {'MAXN': 'MAXN', 'diff': 'diff', 'sum': 'sum', 'add': 'add_data'}
    MAXN = 0
    diff = None
    sum = None
    add_data = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code03_BoringSequence.sum[i] = jcast('long', jcast('long', jadd(Code03_BoringSequence.sum[jcast('int', (i << (1 & 31)))], Code03_BoringSequence.sum[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))

    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        if (Code03_BoringSequence.add_data[i] != 0):
            Code03_BoringSequence.lazy(jcast('int', (i << (1 & 31))), Code03_BoringSequence.add_data[i], ln)
            Code03_BoringSequence.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code03_BoringSequence.add_data[i], rn)
            Code03_BoringSequence.add_data[i] = jcast('long', 0)

    @staticmethod
    def lazy(i, v, n):
        i = jcast('int', i)
        v = jcast('long', v)
        n = jcast('int', n)
        Code03_BoringSequence.add_data[i] = jcast('long', jcast('long', jadd(Code03_BoringSequence.add_data[i], v)))
        Code03_BoringSequence.sum[i] = jcast('long', jcast('long', jadd(Code03_BoringSequence.sum[i], jcast('long', (v * n)))))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code03_BoringSequence.sum[i] = jcast('long', Code03_BoringSequence.diff[l])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code03_BoringSequence.build(l, mid, jcast('int', (i << (1 & 31))))
            Code03_BoringSequence.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code03_BoringSequence.up(i)
        Code03_BoringSequence.add_data[i] = jcast('long', 0)

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code03_BoringSequence.lazy(i, jobv, jcast('int', jadd(jcast('int', (r - l)), 1)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code03_BoringSequence.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code03_BoringSequence.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code03_BoringSequence.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code03_BoringSequence.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code03_BoringSequence.sum[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        Code03_BoringSequence.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
        ans = jcast('long', 0)
        if (jobl <= mid):
            ans = jcast('long', jcast('long', jadd(ans, Code03_BoringSequence.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            ans = jcast('long', jcast('long', jadd(ans, Code03_BoringSequence.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
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
        pre = jcast('int', 0)
        cur = 0
        while (i <= n):
            jcall(in_, 'nextToken')
            cur = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_BoringSequence.diff[i] = jcast('int', jcast('int', (cur - pre)))
            pre = jcast('int', cur)
            i = jcast('int', (i + 1))
        Code03_BoringSequence.build(1, n, 1)
        i = jcast('int', 1)
        op = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            if (op == 1):
                jcall(in_, 'nextToken')
                jobl = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jobr = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                k = jcast('long', jcast('long', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                d = jcast('long', jcast('long', jget(in_, 'nval')))
                e = jcast('long', jcast('long', jadd(k, jcast('long', (d * jcast('int', (jobr - jobl)))))))
                Code03_BoringSequence.add(jobl, jobl, k, 1, n, 1)
                if (jcast('int', jadd(jobl, 1)) <= jobr):
                    Code03_BoringSequence.add(jcast('int', jadd(jobl, 1)), jobr, d, 1, n, 1)
                if (jobr < n):
                    Code03_BoringSequence.add(jcast('int', jadd(jobr, 1)), jcast('int', jadd(jobr, 1)), jcast('long', (-e)), 1, n, 1)
            else:
                jcall(in_, 'nextToken')
                p = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(out, 'println', Code03_BoringSequence.query(1, p, 1, n, 1))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_BoringSequence.MAXN = jcast('int', 100001)
Code03_BoringSequence.diff = jarray('int', [Code03_BoringSequence.MAXN])
Code03_BoringSequence.sum = jarray('long', [jcast('int', (Code03_BoringSequence.MAXN << (2 & 31)))])
Code03_BoringSequence.add_data = jarray('long', [jcast('int', (Code03_BoringSequence.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code03_BoringSequence.main([])
