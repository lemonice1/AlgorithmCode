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

# 丑数 II
# 给你一个整数 n ，请你找出并返回第 n 个 丑数
# 丑数 就是只包含质因数 2、3 或 5 的正整数
# 测试链接 : https://leetcode.cn/problems/ugly-number-ii/
class Code05_UglyNumberII:
    __java_fields__ = {}
    # 时间复杂度O(n)，n代表第n个丑数
    @staticmethod
    def nthUglyNumber(n):
        n = jcast('int', n)
        # dp 0 1 2 ...  n
        # 1 2 ...  ?
        dp = jarray('int', [jcast('int', jadd(n, 1))])
        dp[1] = jcast('int', 1)
        i = jcast('int', 2)
        i2 = jcast('int', 1)
        i3 = jcast('int', 1)
        i5 = jcast('int', 1)
        a = 0
        b = 0
        c = 0
        cur = 0
        while (i <= n):
            a = jcast('int', jcast('int', (dp[i2] * 2)))
            b = jcast('int', jcast('int', (dp[i3] * 3)))
            c = jcast('int', jcast('int', (dp[i5] * 5)))
            cur = jcast('int', jstatic('Math', 'min', jstatic('Math', 'min', a, b), c))
            if (cur == a):
                i2 = jcast('int', (i2 + 1))
            if (cur == b):
                i3 = jcast('int', (i3 + 1))
            if (cur == c):
                i5 = jcast('int', (i5 + 1))
            dp[i] = jcast('int', cur)
            i = jcast('int', (i + 1))
        return jcast('int', dp[n])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


