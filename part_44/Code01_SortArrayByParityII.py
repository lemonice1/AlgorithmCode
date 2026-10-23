# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 按奇偶排序数组II
# 给定一个非负整数数组 nums。nums 中一半整数是奇数 ，一半整数是偶数
# 对数组进行排序，以便当 nums[i] 为奇数时，i也是奇数
# 当 nums[i] 为偶数时， i 也是 偶数
# 你可以返回 任何满足上述条件的数组作为答案
# 测试链接 : https://leetcode.cn/problems/sort-array-by-parity-ii/
class Code01_SortArrayByParityII:
    __java_fields__ = {}
    # 时间复杂度O(n)，额外空间复杂度O(1)
    @staticmethod
    def sortArrayByParityII(nums):
        n = jcast('int', jget(nums, 'length'))
        odd = jcast('int', 1)
        even = jcast('int', 0)
        while ((odd < n) and (even < n)):
            if (jcast('int', (nums[jcast('int', (n - 1))] & 1)) == 1):
                Code01_SortArrayByParityII.swap(nums, odd, jcast('int', (n - 1)))
                odd = jcast('int', jcast('int', jadd(odd, 2)))
            else:
                Code01_SortArrayByParityII.swap(nums, even, jcast('int', (n - 1)))
                even = jcast('int', jcast('int', jadd(even, 2)))
        return nums

    @staticmethod
    def swap(nums, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', nums[i])
        nums[i] = jcast('int', nums[j])
        nums[j] = jcast('int', tmp)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


