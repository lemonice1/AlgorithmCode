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

# 出现次数大于n/2的数
# 给定一个大小为n的数组nums
# 水王数是指在数组中出现次数大于n/2的数
# 返回其中的水王数，如果数组不存在水王数返回-1
# 测试链接 : https://leetcode.cn/problems/majority-element/
class Code01_WaterKing:
    __java_fields__ = {}
    @staticmethod
    def majorityElement(nums):
        cand = jcast('int', 0)
        hp = jcast('int', 0)
        for num in nums:
            if (hp == 0):
                cand = jcast('int', num)
                hp = jcast('int', 1)
            else:
                if (num != cand):
                    hp = jcast('int', (hp - 1))
                else:
                    hp = jcast('int', (hp + 1))
        if (hp == 0):
            return jcast('int', jcast('int', (-1)))
        # 复用hp，统计真实出现的次数
        hp = jcast('int', 0)
        for num in nums:
            if (num == cand):
                hp = jcast('int', (hp + 1))
        return jcast('int', (cand if (hp > jcast('int', jdiv(jget(nums, 'length'), 2))) else jcast('int', (-1))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


