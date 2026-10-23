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

# 一个正整数如果能被 a 或 b 整除，那么它是神奇的。
# 给定三个整数 n , a , b ，返回第 n 个神奇的数字。
# 因为答案可能很大，所以返回答案 对 1000000007 取模
# 测试链接 : https://leetcode.cn/problems/nth-magical-number/
class Code02_NthMagicalNumber:
    __java_fields__ = {}
    @staticmethod
    def nthMagicalNumber(n, a, b):
        n = jcast('int', n)
        a = jcast('int', a)
        b = jcast('int', b)
        lcm = jcast('long', Code02_NthMagicalNumber.lcm(a, b))
        ans = jcast('long', 0)
        # l = 0
        # r = (long) n * Math.min(a, b)
        # l......r
        l = jcast('long', 0)
        r = jcast('long', jcast('long', (jcast('long', n) * jstatic('Math', 'min', a, b))))
        m = jcast('long', 0)
        while (l <= r):
            m = jcast('long', jcast('long', jdiv(jcast('long', jadd(l, r)), 2)))
            # 1....m
            if (jcast('long', (jcast('long', jadd(jcast('long', jdiv(m, a)), jcast('long', jdiv(m, b)))) - jcast('long', jdiv(m, lcm)))) >= n):
                ans = jcast('long', m)
                r = jcast('long', jcast('long', (m - 1)))
            else:
                l = jcast('long', jcast('long', jadd(m, 1)))
        return jcast('int', jcast('int', jcast('long', jmod(ans, 1000000007))))

    @staticmethod
    def gcd(a, b):
        a = jcast('long', a)
        b = jcast('long', b)
        return jcast('long', (a if (b == 0) else Code02_NthMagicalNumber.gcd(b, jcast('long', jmod(a, b)))))

    @staticmethod
    def lcm(a, b):
        a = jcast('long', a)
        b = jcast('long', b)
        return jcast('long', jcast('long', (jcast('long', jdiv(jcast('long', a), Code02_NthMagicalNumber.gcd(a, b))) * b)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


