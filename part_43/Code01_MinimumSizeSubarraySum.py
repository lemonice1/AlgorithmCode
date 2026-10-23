# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 累加和大于等于target的最短子数组长度
# 给定一个含有 n 个正整数的数组和一个正整数 target
# 找到累加和 >= target 的长度最小的子数组并返回其长度
# 如果不存在符合条件的子数组返回0
# 测试链接 : https://leetcode.cn/problems/minimum-size-subarray-sum/
class Code01_MinimumSizeSubarraySum:
    __java_fields__ = {}
    @staticmethod
    def minSubArrayLen(target, nums):
        target = jcast('int', target)
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        l = jcast('int', 0)
        r = jcast('int', 0)
        sum = jcast('int', 0)
        while (r < jget(nums, 'length')):
            sum = jcast('int', jcast('int', jadd(sum, nums[r])))
            while (jcast('int', (sum - nums[l])) >= target):
                # sum : nums[l....r]
                # 如果l位置的数从窗口出去，还能继续达标，那就出去
                sum = jcast('int', jcast('int', (sum - nums[((_java_old_1 := l), (l := jcast('int', (l + (1)))), _java_old_1)[2]])))
            if (sum >= target):
                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(jcast('int', (r - l)), 1))))
            r = jcast('int', (r + 1))
        return jcast('int', (0 if (ans == jget(Integer, 'MAX_VALUE')) else ans))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


