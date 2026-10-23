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

# 至少有1位重复的数字个数
# 给定正整数n，返回在[1, n]范围内至少有1位重复数字的正整数个数
# 测试链接 : https://leetcode.cn/problems/numbers-with-repeated-digits/
class Code04_NumbersWithRepeatedDigits:
    __java_fields__ = {}
    @staticmethod
    def numDupDigitsAtMostN(n):
        n = jcast('int', n)
        return jcast('int', jcast('int', (n - Code04_NumbersWithRepeatedDigits.countSpecialNumbers(n))))

    @staticmethod
    def countSpecialNumbers(n):
        n = jcast('int', n)
        len = jcast('int', 1)
        offset = jcast('int', 1)
        tmp = jcast('int', jcast('int', jdiv(n, 10)))
        while (tmp > 0):
            len = jcast('int', (len + 1))
            offset = jcast('int', jcast('int', (offset * 10)))
            tmp = jcast('int', jcast('int', jdiv(tmp, 10)))
        cnt = jarray('int', [len])
        cnt[0] = jcast('int', 1)
        i = jcast('int', 1)
        k = jcast('int', jcast('int', jadd(jcast('int', (10 - len)), 1)))
        while (i < len):
            cnt[i] = jcast('int', jcast('int', (cnt[jcast('int', (i - 1))] * k)))
            i = jcast('int', (i + 1))
            k = jcast('int', (k + 1))
        ans = jcast('int', 0)
        if (len >= 2):
            ans = jcast('int', 9)
            i = jcast('int', 2)
            a = jcast('int', 9)
            b = jcast('int', 9)
            while (i < len):
                a = jcast('int', jcast('int', (a * b)))
                ans = jcast('int', jcast('int', jadd(ans, a)))
                i = jcast('int', (i + 1))
                b = jcast('int', (b - 1))
        first = jcast('int', jcast('int', jdiv(n, offset)))
        ans = jcast('int', jcast('int', jadd(ans, jcast('int', (jcast('int', (first - 1)) * cnt[jcast('int', (len - 1))])))))
        ans = jcast('int', jcast('int', jadd(ans, Code04_NumbersWithRepeatedDigits.f(cnt, n, jcast('int', (len - 1)), jcast('int', jdiv(offset, 10)), jcast('int', (1 << (first & 31)))))))
        return jcast('int', ans)

    @staticmethod
    def f(cnt, num, len, offset, status):
        num = jcast('int', num)
        len = jcast('int', len)
        offset = jcast('int', offset)
        status = jcast('int', status)
        if (len == 0):
            return jcast('int', 1)
        ans = jcast('int', 0)
        first = jcast('int', jcast('int', jmod(jcast('int', jdiv(num, offset)), 10)))
        cur = jcast('int', 0)
        while (cur < first):
            if (jcast('int', (status & jcast('int', (1 << (cur & 31))))) == 0):
                ans = jcast('int', jcast('int', jadd(ans, cnt[jcast('int', (len - 1))])))
            cur = jcast('int', (cur + 1))
        if (jcast('int', (status & jcast('int', (1 << (first & 31))))) == 0):
            ans = jcast('int', jcast('int', jadd(ans, Code04_NumbersWithRepeatedDigits.f(cnt, num, jcast('int', (len - 1)), jcast('int', jdiv(offset, 10)), jcast('int', (status | jcast('int', (1 << (first & 31)))))))))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


