# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 找到缺失的数字
# 测试链接 : https://leetcode.cn/problems/missing-number/
class Code03_MissingNumber:
    __java_fields__ = {}
    @staticmethod
    def missingNumber(nums):
        eorAll = jcast('int', 0)
        eorHas = jcast('int', 0)
        i = jcast('int', 0)
        while (i < jget(nums, 'length')):
            eorAll = jcast('int', jcast('int', (eorAll ^ i)))
            eorHas = jcast('int', jcast('int', (eorHas ^ nums[i])))
            i = jcast('int', (i + 1))
        eorAll = jcast('int', jcast('int', (eorAll ^ jget(nums, 'length'))))
        return jcast('int', jcast('int', (eorAll ^ eorHas)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


