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

# 数组中1种数出现了奇数次，其他的数都出现了偶数次
# 返回出现了奇数次的数
# 测试链接 : https://leetcode.cn/problems/single-number/
class Code04_SingleNumber:
    __java_fields__ = {}
    @staticmethod
    def singleNumber(nums):
        eor = jcast('int', 0)
        for num in nums:
            eor = jcast('int', jcast('int', (eor ^ num)))
        return jcast('int', eor)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


