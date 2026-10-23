# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 求斐波那契数列第n项
# 测试链接 : https://leetcode.cn/problems/fibonacci-number/
# 这个测试的数据量太小，并且不牵扯取模的事情
# 所以矩阵快速幂看不出优势
class Code02_FibonacciNumber:
    __java_fields__ = {}
    # 时间复杂度O(n)，普通解法，讲解066，题目1
    @staticmethod
    def fib1(n):
        n = jcast('int', n)
        if (n == 0):
            return jcast('int', 0)
        if (n == 1):
            return jcast('int', 1)
        lastLast = jcast('int', 0)
        last = jcast('int', 1)
        i = jcast('int', 2)
        cur = 0
        while (i <= n):
            cur = jcast('int', jcast('int', jadd(lastLast, last)))
            lastLast = jcast('int', last)
            last = jcast('int', cur)
            i = jcast('int', (i + 1))
        return jcast('int', last)

    # 时间复杂度O(logn)，矩阵快速幂的解法
    @staticmethod
    def fib2(n):
        n = jcast('int', n)
        if (n == 0):
            return jcast('int', 0)
        if (n == 1):
            return jcast('int', 1)
        start = jarray('int', [None, None], [[1, 0]])
        base = jarray('int', [None, None], [[1, 1], [1, 0]])
        ans = Code02_FibonacciNumber.multiply(start, Code02_FibonacciNumber.power(base, jcast('int', (n - 1))))
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
                ans = Code02_FibonacciNumber.multiply(ans, m)
            m = Code02_FibonacciNumber.multiply(m, m)
            p = jcast('int', jcast('int', (p >> (1 & 31))))
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


