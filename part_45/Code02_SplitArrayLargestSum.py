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

# 分割数组的最大值(画匠问题)
# 给定一个非负整数数组 nums 和一个整数 m
# 你需要将这个数组分成 m 个非空的连续子数组。
# 设计一个算法使得这 m 个子数组各自和的最大值最小。
# 测试链接 : https://leetcode.cn/problems/split-array-largest-sum/
class Code02_SplitArrayLargestSum:
    __java_fields__ = {}
    # 时间复杂度O(n * log(sum))，额外空间复杂度O(1)
    @staticmethod
    def splitArray(nums, k):
        k = jcast('int', k)
        sum = jcast('long', 0)
        for num in nums:
            sum = jcast('long', jcast('long', jadd(sum, num)))
        ans = jcast('long', 0)
        # [0,sum]二分
        l = jcast('long', 0)
        r = jcast('long', sum)
        m = 0
        need = 0
        while (l <= r):
            # 中点m
            m = jcast('long', jcast('long', jadd(l, jcast('long', (jcast('long', (r - l)) >> (1 & 63))))))
            # 必须让数组每一部分的累加和 <= m，请问划分成几个部分才够!
            need = jcast('long', Code02_SplitArrayLargestSum.f(nums, m))
            if (need <= k):
                # 达标
                ans = jcast('long', m)
                r = jcast('long', jcast('long', (m - 1)))
            else:
                l = jcast('long', jcast('long', jadd(m, 1)))
        return jcast('int', jcast('int', ans))

    # 必须让数组arr每一部分的累加和 <= limit，请问划分成几个部分才够!
    # 返回需要的部分数量
    @staticmethod
    def f(arr, limit):
        limit = jcast('long', limit)
        parts = jcast('int', 1)
        sum = jcast('int', 0)
        for num in arr:
            if (num > limit):
                return jcast('int', jget(Integer, 'MAX_VALUE'))
            if (jcast('int', jadd(sum, num)) > limit):
                parts = jcast('int', (parts + 1))
                sum = jcast('int', num)
            else:
                sum = jcast('int', jcast('int', jadd(sum, num)))
        return jcast('int', parts)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


