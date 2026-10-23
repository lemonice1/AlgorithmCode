# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 数字1的个数
# 给定一个整数n
# 计算所有小于等于n的非负整数中数字1出现的个数
# 测试链接 : https://leetcode.cn/problems/number-of-digit-one/
class Code04_DigitCount3:
    __java_fields__ = {}
    @staticmethod
    def countDigitOne(n):
        n = jcast('int', n)
        return jcast('int', Code04_DigitCount3.count(n, 1))

    @staticmethod
    def count(num, d):
        num = jcast('int', num)
        d = jcast('int', d)
        ans = jcast('int', 0)
        right = jcast('int', 1)
        tmp = jcast('int', num)
        left = 0
        cur = 0
        while (tmp != 0):
            left = jcast('int', jcast('int', jdiv(tmp, 10)))
            cur = jcast('int', jcast('int', jmod(tmp, 10)))
            if (d == 0):
                left = jcast('int', (left - 1))
            ans = jcast('int', jcast('int', jadd(ans, jcast('int', (left * right)))))
            if (cur > d):
                ans = jcast('int', jcast('int', jadd(ans, right)))
            else:
                if (cur == d):
                    ans = jcast('int', jcast('int', jadd(ans, jcast('int', jadd(jcast('int', jmod(num, right)), 1)))))
            right = jcast('int', jcast('int', (right * 10)))
            tmp = jcast('int', jcast('int', jdiv(tmp, 10)))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


