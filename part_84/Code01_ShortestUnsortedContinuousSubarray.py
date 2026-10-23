# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最短无序连续子数组
# 给你一个整数数组nums，你需要找出一个 连续子数组
# 如果对这个子数组进行升序排序，那么整个数组都会变为升序排序
# 请你找出符合题意的最短子数组，并输出它的长度
# 测试链接 : https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/
class Code01_ShortestUnsortedContinuousSubarray:
    __java_fields__ = {}
    @staticmethod
    def findUnsortedSubarray(nums):
        n = jcast('int', jget(nums, 'length'))
        # max > 当前数，认为不达标
        # 从左往右遍历，记录最右不达标的位置
        right = jcast('int', jcast('int', (-1)))
        max = jcast('int', jget(Integer, 'MIN_VALUE'))
        i = jcast('int', 0)
        while (i < n):
            if (max > nums[i]):
                right = jcast('int', i)
            max = jcast('int', jstatic('Math', 'max', max, nums[i]))
            i = jcast('int', (i + 1))
        min = jcast('int', jget(Integer, 'MAX_VALUE'))
        # min < 当前数，认为不达标
        # 从右往左遍历，记录最左不达标的位置
        left = jcast('int', n)
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            if (min < nums[i]):
                left = jcast('int', i)
            min = jcast('int', jstatic('Math', 'min', min, nums[i]))
            i = jcast('int', (i - 1))
        return jcast('int', jstatic('Math', 'max', 0, jcast('int', jadd(jcast('int', (right - left)), 1))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


