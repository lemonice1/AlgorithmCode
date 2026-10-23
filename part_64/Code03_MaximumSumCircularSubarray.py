# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 环形数组的子数组最大累加和
# 给定一个数组nums，长度为n
# nums是一个环形数组，下标0和下标n-1是连在一起的
# 返回环形数组中，子数组最大累加和
# 测试链接 : https://leetcode.cn/problems/maximum-sum-circular-subarray/
class Code03_MaximumSumCircularSubarray:
    __java_fields__ = {}
    @staticmethod
    def maxSubarraySumCircular(nums):
        n = jcast('int', jget(nums, 'length'))
        all = jcast('int', nums[0])
        maxsum = jcast('int', nums[0])
        minsum = jcast('int', nums[0])
        i = jcast('int', 1)
        maxpre = jcast('int', nums[0])
        minpre = jcast('int', nums[0])
        while (i < n):
            all = jcast('int', jcast('int', jadd(all, nums[i])))
            maxpre = jcast('int', jstatic('Math', 'max', nums[i], jcast('int', jadd(nums[i], maxpre))))
            maxsum = jcast('int', jstatic('Math', 'max', maxsum, maxpre))
            minpre = jcast('int', jstatic('Math', 'min', nums[i], jcast('int', jadd(nums[i], minpre))))
            minsum = jcast('int', jstatic('Math', 'min', minsum, minpre))
            i = jcast('int', (i + 1))
        # 1) maxsum
        # 2) all - minsum
        return jcast('int', (maxsum if (all == minsum) else jstatic('Math', 'max', maxsum, jcast('int', (all - minsum)))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


