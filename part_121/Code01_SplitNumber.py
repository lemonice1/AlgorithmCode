# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 数的划分方法
# 将整数m分成n份，且每份不能为空，任意两个方案不相同(不考虑顺序)
# 比如，m=7、n=3，那么(1, 1, 5) (1, 5, 1) (5, 1, 1)认为是同一种方法
# 返回有多少种不同的划分方法
# 测试链接 : https://www.luogu.com.cn/problem/P1025
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_SplitNumber:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 'dp': 'dp'}
    MAXN = 0
    MAXK = 0
    dp = None
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(out, 'println', Code01_SplitNumber.compute(m, n))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute(m, n):
        m = jcast('int', m)
        n = jcast('int', n)
        if (m < n):
            return jcast('int', 0)
        if (m == n):
            return jcast('int', 1)
        m = jcast('int', jcast('int', (m - n)))
        i = jcast('int', 0)
        while (i <= m):
            j = jcast('int', 0)
            while (j <= n):
                jset(Code01_SplitNumber.dp[i], j, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code01_SplitNumber.f(m, n))

    @staticmethod
    def f(m, n):
        m = jcast('int', m)
        n = jcast('int', n)
        if (m == 0):
            return jcast('int', 1)
        if (n == 0):
            return jcast('int', 0)
        if (Code01_SplitNumber.dp[m][n] != jcast('int', (-1))):
            return jcast('int', Code01_SplitNumber.dp[m][n])
        ans = 0
        if (n > m):
            ans = jcast('int', Code01_SplitNumber.f(m, m))
        else:
            ans = jcast('int', jcast('int', jadd(Code01_SplitNumber.f(m, jcast('int', (n - 1))), Code01_SplitNumber.f(jcast('int', (m - n)), n))))
        jset(Code01_SplitNumber.dp[m], n, ans)
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_SplitNumber.MAXN = jcast('int', 201)
Code01_SplitNumber.MAXK = jcast('int', 7)
Code01_SplitNumber.dp = jarray('int', [Code01_SplitNumber.MAXN, Code01_SplitNumber.MAXK])

if __name__ == '__main__':
    Code01_SplitNumber.main([])
