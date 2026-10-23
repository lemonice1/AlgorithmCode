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

# 斐波那契数
# 斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列
# 该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。
# 也就是：F(0) = 0，F(1) = 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1
# 给定 n ，请计算 F(n)
# 测试链接 : https://leetcode.cn/problems/fibonacci-number/
# 注意：最优解来自矩阵快速幂，时间复杂度可以做到O(log n)
# 后续课程一定会讲述！本节课不涉及！
class Code01_FibonacciNumber:
    __java_fields__ = {}
    @staticmethod
    def fib1(n):
        n = jcast('int', n)
        return jcast('int', Code01_FibonacciNumber.f1(n))

    @staticmethod
    def f1(i):
        i = jcast('int', i)
        if (i == 0):
            return jcast('int', 0)
        if (i == 1):
            return jcast('int', 1)
        return jcast('int', jcast('int', jadd(Code01_FibonacciNumber.f1(jcast('int', (i - 1))), Code01_FibonacciNumber.f1(jcast('int', (i - 2))))))

    @staticmethod
    def fib2(n):
        n = jcast('int', n)
        dp = jarray('int', [jcast('int', jadd(n, 1))])
        jstatic('Arrays', 'fill', dp, jcast('int', (-1)))
        return jcast('int', Code01_FibonacciNumber.f2(n, dp))

    @staticmethod
    def f2(i, dp):
        i = jcast('int', i)
        if (i == 0):
            return jcast('int', 0)
        if (i == 1):
            return jcast('int', 1)
        if (dp[i] != jcast('int', (-1))):
            return jcast('int', dp[i])
        ans = jcast('int', jcast('int', jadd(Code01_FibonacciNumber.f2(jcast('int', (i - 1)), dp), Code01_FibonacciNumber.f2(jcast('int', (i - 2)), dp))))
        dp[i] = jcast('int', ans)
        return jcast('int', ans)

    @staticmethod
    def fib3(n):
        n = jcast('int', n)
        if (n == 0):
            return jcast('int', 0)
        if (n == 1):
            return jcast('int', 1)
        dp = jarray('int', [jcast('int', jadd(n, 1))])
        dp[1] = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= n):
            dp[i] = jcast('int', jcast('int', jadd(dp[jcast('int', (i - 1))], dp[jcast('int', (i - 2))])))
            i = jcast('int', (i + 1))
        return jcast('int', dp[n])

    @staticmethod
    def fib4(n):
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

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


