# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# ST表查询最大公约数
# 给定一个长度为n的数组arr，一共有m次查询
# 每次查询arr[l~r]上所有数的最大公约数
# 测试链接 : https://www.luogu.com.cn/problem/P1890
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_SparseTableGCD:
    __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'arr': 'arr', 'log2': 'log2', 'stgcd': 'stgcd'}
    MAXN = 0
    LIMIT = 0
    arr = None
    log2 = None
    stgcd = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code03_SparseTableGCD.log2[0] = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= n):
            Code03_SparseTableGCD.log2[i] = jcast('int', jcast('int', jadd(Code03_SparseTableGCD.log2[jcast('int', (i >> (1 & 31)))], 1)))
            jset(Code03_SparseTableGCD.stgcd[i], 0, Code03_SparseTableGCD.arr[i])
            i = jcast('int', (i + 1))
        p = jcast('int', 1)
        while (p <= Code03_SparseTableGCD.log2[n]):
            i = jcast('int', 1)
            while (jcast('int', (jcast('int', jadd(i, jcast('int', (1 << (p & 31))))) - 1)) <= n):
                jset(Code03_SparseTableGCD.stgcd[i], p, Code03_SparseTableGCD.gcd(Code03_SparseTableGCD.stgcd[i][jcast('int', (p - 1))], Code03_SparseTableGCD.stgcd[jcast('int', jadd(i, jcast('int', (1 << (jcast('int', (p - 1)) & 31)))))][jcast('int', (p - 1))]))
                i = jcast('int', (i + 1))
            p = jcast('int', (p + 1))

    # 算法讲解041 - 辗转相除法求最大公约数
    @staticmethod
    def gcd(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        return jcast('int', (a if (b == 0) else Code03_SparseTableGCD.gcd(b, jcast('int', jmod(a, b)))))

    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        p = jcast('int', Code03_SparseTableGCD.log2[jcast('int', jadd(jcast('int', (r - l)), 1))])
        return jcast('int', Code03_SparseTableGCD.gcd(Code03_SparseTableGCD.stgcd[l][p], Code03_SparseTableGCD.stgcd[jcast('int', jadd(jcast('int', (r - jcast('int', (1 << (p & 31))))), 1))][p]))

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
            Code03_SparseTableGCD.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code03_SparseTableGCD.build(n)
        i = jcast('int', 1)
        l = 0
        r = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            l = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            r = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'println', Code03_SparseTableGCD.query(l, r))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_SparseTableGCD.MAXN = jcast('int', 1001)
Code03_SparseTableGCD.LIMIT = jcast('int', 10)
Code03_SparseTableGCD.arr = jarray('int', [Code03_SparseTableGCD.MAXN])
Code03_SparseTableGCD.log2 = jarray('int', [Code03_SparseTableGCD.MAXN])
Code03_SparseTableGCD.stgcd = jarray('int', [Code03_SparseTableGCD.MAXN, Code03_SparseTableGCD.LIMIT])

if __name__ == '__main__':
    Code03_SparseTableGCD.main([])
