# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 包含取模操作的线段树
# 给定一个长度为n的数组arr，实现如下三种操作，一共调用m次
# 操作 1 l r : 查询arr[l..r]的累加和
# 操作 2 l r x : 把arr[l..r]上每个数字对x取模
# 操作 3 k x : 把arr[k]上的数字设置为x
# 1 <= n, m <= 10^5，操作1得到的结果，有可能超过int范围
# 测试链接 : https://www.luogu.com.cn/problem/CF438D
# 测试链接 : https://codeforces.com/problemset/problem/438/D
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_QueryModUpdate:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'sum': 'sum', 'max': 'max'}
    MAXN = 0
    arr = None
    sum = None
    max = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code04_QueryModUpdate.sum[i] = jcast('long', jcast('long', jadd(Code04_QueryModUpdate.sum[jcast('int', (i << (1 & 31)))], Code04_QueryModUpdate.sum[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
        jset(Code04_QueryModUpdate.max, i, jstatic('Math', 'max', Code04_QueryModUpdate.max[jcast('int', (i << (1 & 31)))], Code04_QueryModUpdate.max[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            jset(Code04_QueryModUpdate.sum, i, jset(Code04_QueryModUpdate.max, i, Code04_QueryModUpdate.arr[l]))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code04_QueryModUpdate.build(l, mid, jcast('int', (i << (1 & 31))))
            Code04_QueryModUpdate.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code04_QueryModUpdate.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code04_QueryModUpdate.sum[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('long', 0)
        if (jobl <= mid):
            ans = jcast('long', jcast('long', jadd(ans, Code04_QueryModUpdate.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            ans = jcast('long', jcast('long', jadd(ans, Code04_QueryModUpdate.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('long', ans)

    @staticmethod
    def mod(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (jobv > Code04_QueryModUpdate.max[i]):
            return
        if (l == r):
            Code04_QueryModUpdate.sum[i] = jcast('long', jcast('long', jmod(Code04_QueryModUpdate.sum[i], jobv)))
            Code04_QueryModUpdate.max[i] = jcast('int', jcast('int', jmod(Code04_QueryModUpdate.max[i], jobv)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code04_QueryModUpdate.mod(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code04_QueryModUpdate.mod(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code04_QueryModUpdate.up(i)

    @staticmethod
    def update(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            jset(Code04_QueryModUpdate.sum, i, jset(Code04_QueryModUpdate.max, i, jobv))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                Code04_QueryModUpdate.update(jobi, jobv, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code04_QueryModUpdate.update(jobi, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code04_QueryModUpdate.up(i)

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
            Code04_QueryModUpdate.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code04_QueryModUpdate.build(1, n, 1)
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
                jcall(out, 'println', Code04_QueryModUpdate.query(jobl, jobr, 1, n, 1))
            else:
                if (op == 2):
                    jcall(in_, 'nextToken')
                    jobl = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    jobr = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    jobv = jcast('int', jcast('int', jget(in_, 'nval')))
                    Code04_QueryModUpdate.mod(jobl, jobr, jobv, 1, n, 1)
                else:
                    jcall(in_, 'nextToken')
                    jobi = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    jobv = jcast('int', jcast('int', jget(in_, 'nval')))
                    Code04_QueryModUpdate.update(jobi, jobv, 1, n, 1)
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_QueryModUpdate.MAXN = jcast('int', 100001)
Code04_QueryModUpdate.arr = jarray('int', [Code04_QueryModUpdate.MAXN])
Code04_QueryModUpdate.sum = jarray('long', [jcast('int', (Code04_QueryModUpdate.MAXN << (2 & 31)))])
Code04_QueryModUpdate.max = jarray('int', [jcast('int', (Code04_QueryModUpdate.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code04_QueryModUpdate.main([])
