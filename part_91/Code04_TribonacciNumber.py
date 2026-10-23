# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 第n个泰波那契数
# t(0) = 0, t(1) = 1, t(2) = 1
# t(i) = t(i-1) + t(i-2) + t(i-3)
# 求t(n)
# 测试链接 : https://leetcode.cn/problems/n-th-tribonacci-number/
# 这个测试的数据量太小，并且不牵扯取模的事情
# 所以矩阵快速幂看不出优势
class Code04_TribonacciNumber:
    __java_fields__ = {}
    @staticmethod
    def tribonacci(n):
        n = jcast('int', n)
        if (n == 0):
            return jcast('int', 0)
        if (n == 1):
            return jcast('int', 1)
        if (n == 2):
            return jcast('int', 1)
        start = jarray('int', [None, None], [[1, 1, 0]])
        base = jarray('int', [None, None], [[1, 1, 0], [1, 0, 1], [1, 0, 0]])
        ans = Code04_TribonacciNumber.multiply(start, Code04_TribonacciNumber.power(base, jcast('int', (n - 2))))
        return jcast('int', ans[0][0])

    # 矩阵相乘
    # a的列数一定要等于b的行数
    @staticmethod
    def multiply(a, b):
        n = jcast('int', jget(a, 'length'))
        m = jcast('int', jget(b[0], 'length'))
        k = jcast('int', jget(a[0], 'length'))
        ans = jarray('int', [n, m])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                c = jcast('int', 0)
                while (c < k):
                    ((_java_obj_1 := ans[i]), (_java_key_2 := j), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), jcast('int', (a[i][c] * b[c][j]))))))[2]
                    c = jcast('int', (c + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return ans

    # 矩阵快速幂
    @staticmethod
    def power(m, p):
        p = jcast('int', p)
        n = jcast('int', jget(m, 'length'))
        ans = jarray('int', [n, n])
        i = jcast('int', 0)
        while (i < n):
            jset(ans[i], i, 1)
            i = jcast('int', (i + 1))
        while (p != 0):
            if (jcast('int', (p & 1)) != 0):
                ans = Code04_TribonacciNumber.multiply(ans, m)
            m = Code04_TribonacciNumber.multiply(m, m)
            p = jcast('int', jcast('int', (p >> (1 & 31))))
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


