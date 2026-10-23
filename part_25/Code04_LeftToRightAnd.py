# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 给你两个整数 left 和 right ，表示区间 [left, right]
# 返回此区间内所有数字 & 的结果
# 包含 left 、right 端点
# 测试链接 : https://leetcode.cn/problems/bitwise-and-of-numbers-range/
class Code04_LeftToRightAnd:
    __java_fields__ = {}
    @staticmethod
    def rangeBitwiseAnd(left, right):
        left = jcast('int', left)
        right = jcast('int', right)
        while (left < right):
            right = jcast('int', jcast('int', (right - jcast('int', (right & jcast('int', (-right)))))))
        return jcast('int', right)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


