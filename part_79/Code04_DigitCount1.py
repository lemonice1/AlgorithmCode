# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 范围内的数字计数
# 给定两个正整数a和b，求在[a,b]范围上的所有整数中
# 1 <= a, b
# 某个数码d出现了多少次
# 测试链接 : https://leetcode.cn/problems/digit-count-in-range/
class Code04_DigitCount1:
    __java_fields__ = {}
    @staticmethod
    def digitsCount(d, a, b):
        d = jcast('int', d)
        a = jcast('int', a)
        b = jcast('int', b)
        return jcast('int', jcast('int', (Code04_DigitCount1.count(b, d) - Code04_DigitCount1.count(jcast('int', (a - 1)), d))))

    # 统计1~num范围上所有的数中，数码d出现了多少次
    # 注意是1~num范围，不是0~num范围
    @staticmethod
    def count(num, d):
        num = jcast('int', num)
        d = jcast('int', d)
        ans = jcast('int', 0)
        # left : 当前位左边的情况数
        # right : 当前位右边的情况数
        # 当前位的数字是cur
        right = jcast('int', 1)
        tmp = jcast('int', num)
        left = 0
        cur = 0
        while (tmp != 0):
            # 情况1：
            # d != 0
            # 1 ~ 30583 , d = 5
            # cur < d的情况
            # 个位cur=3 : 0000~3057 5
            # 个位上没有额外加
            #
            # cur > d的情况
            # 十位cur=8 : 000~304 5 0~9
            # 十位上额外加 : 305 5 0~9
            #
            # cur == d的情况
            # 百位cur=5 : 00~29 5 00~99
            # 百位上额外加 : 30 5 00~83
            # ...
            # 情况2：
            # d == 0
            # 1 ~ 30583 d = 0
            # cur > d的情况
            # 个位cur=3 : 0001~3057 0
            # 个位上额外加 : 3058 0
            #
            # cur > d的情况
            # 十位cur=8 : 001~304 0 0~9
            # 十位上额外加 : 305 0 0~9
            #
            # cur > d的情况
            # 百位cur=5 : 01~29 0 00~99
            # 百位上额外加 : 30 0 00~99
            #
            # cur == d的情况
            # 千位cur=0 : 1~2 0 000~099
            # 千位上额外加 : 3 0 000~583
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


