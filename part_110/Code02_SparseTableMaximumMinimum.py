# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# ST表查询最大值和最小值
# 给定一个长度为n的数组arr，一共有m次查询
# 每次查询arr[l~r]上的最大值和最小值
# 每次查询只需要打印最大值-最小值的结果
# 测试链接 : https://www.luogu.com.cn/problem/P2880
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_SparseTableMaximumMinimum:
    __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'arr': 'arr', 'log2': 'log2', 'stmax': 'stmax', 'stmin': 'stmin'}
    MAXN = 0
    # 2的15次方是<=50001且最接近的
    # 所以次方可能是0~15
    # 于是准备16长度够用了
    LIMIT = 0
    arr = None
    # log2[i] : 查询<=i情况下，最大的2的幂，是2的几次方
    log2 = None
    stmax = None
    stmin = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code02_SparseTableMaximumMinimum.log2[0] = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= n):
            Code02_SparseTableMaximumMinimum.log2[i] = jcast('int', jcast('int', jadd(Code02_SparseTableMaximumMinimum.log2[jcast('int', (i >> (1 & 31)))], 1)))
            jset(Code02_SparseTableMaximumMinimum.stmax[i], 0, Code02_SparseTableMaximumMinimum.arr[i])
            jset(Code02_SparseTableMaximumMinimum.stmin[i], 0, Code02_SparseTableMaximumMinimum.arr[i])
            i = jcast('int', (i + 1))
        p = jcast('int', 1)
        while (p <= Code02_SparseTableMaximumMinimum.log2[n]):
            i = jcast('int', 1)
            while (jcast('int', (jcast('int', jadd(i, jcast('int', (1 << (p & 31))))) - 1)) <= n):
                jset(Code02_SparseTableMaximumMinimum.stmax[i], p, jstatic('Math', 'max', Code02_SparseTableMaximumMinimum.stmax[i][jcast('int', (p - 1))], Code02_SparseTableMaximumMinimum.stmax[jcast('int', jadd(i, jcast('int', (1 << (jcast('int', (p - 1)) & 31)))))][jcast('int', (p - 1))]))
                jset(Code02_SparseTableMaximumMinimum.stmin[i], p, jstatic('Math', 'min', Code02_SparseTableMaximumMinimum.stmin[i][jcast('int', (p - 1))], Code02_SparseTableMaximumMinimum.stmin[jcast('int', jadd(i, jcast('int', (1 << (jcast('int', (p - 1)) & 31)))))][jcast('int', (p - 1))]))
                i = jcast('int', (i + 1))
            p = jcast('int', (p + 1))

    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        p = jcast('int', Code02_SparseTableMaximumMinimum.log2[jcast('int', jadd(jcast('int', (r - l)), 1))])
        a = jcast('int', jstatic('Math', 'max', Code02_SparseTableMaximumMinimum.stmax[l][p], Code02_SparseTableMaximumMinimum.stmax[jcast('int', jadd(jcast('int', (r - jcast('int', (1 << (p & 31))))), 1))][p]))
        b = jcast('int', jstatic('Math', 'min', Code02_SparseTableMaximumMinimum.stmin[l][p], Code02_SparseTableMaximumMinimum.stmin[jcast('int', jadd(jcast('int', (r - jcast('int', (1 << (p & 31))))), 1))][p]))
        return jcast('int', jcast('int', (a - b)))

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
            Code02_SparseTableMaximumMinimum.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code02_SparseTableMaximumMinimum.build(n)
        i = jcast('int', 1)
        l = 0
        r = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            l = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            r = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'println', Code02_SparseTableMaximumMinimum.query(l, r))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_SparseTableMaximumMinimum.MAXN = jcast('int', 50001)
Code02_SparseTableMaximumMinimum.LIMIT = jcast('int', 16)
Code02_SparseTableMaximumMinimum.arr = jarray('int', [Code02_SparseTableMaximumMinimum.MAXN])
Code02_SparseTableMaximumMinimum.log2 = jarray('int', [Code02_SparseTableMaximumMinimum.MAXN])
Code02_SparseTableMaximumMinimum.stmax = jarray('int', [Code02_SparseTableMaximumMinimum.MAXN, Code02_SparseTableMaximumMinimum.LIMIT])
Code02_SparseTableMaximumMinimum.stmin = jarray('int', [Code02_SparseTableMaximumMinimum.MAXN, Code02_SparseTableMaximumMinimum.LIMIT])

if __name__ == '__main__':
    Code02_SparseTableMaximumMinimum.main([])
