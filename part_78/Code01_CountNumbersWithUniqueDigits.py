# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 统计各位数字都不同的数字个数
# 给你一个整数n，代表十进制数字最多有n位
# 如果某个数字，每一位都不同，那么这个数字叫做有效数字
# 返回有效数字的个数，不统计负数范围
# 测试链接 : https://leetcode.cn/problems/count-numbers-with-unique-digits/
class Code01_CountNumbersWithUniqueDigits:
    __java_fields__ = {}
    @staticmethod
    def countNumbersWithUniqueDigits(n):
        n = jcast('int', n)
        if (n == 0):
            return jcast('int', 1)
        ans = jcast('int', 10)
        # 1 : 10
        # 2 : 9 * 9
        # 3 : 9 * 9 * 8
        # 4 : 9 * 9 * 8 * 7
        # ...都累加起来...
        s = jcast('int', 9)
        i = jcast('int', 9)
        k = jcast('int', 2)
        while (k <= n):
            s = jcast('int', jcast('int', (s * i)))
            ans = jcast('int', jcast('int', jadd(ans, s)))
            i = jcast('int', (i - 1))
            k = jcast('int', (k + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


