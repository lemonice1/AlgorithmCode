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

# 找出第K小的数对距离
# 数对 (a,b) 由整数 a 和 b 组成，其数对距离定义为 a 和 b 的绝对差值。
# 给你一个整数数组 nums 和一个整数 k
# 数对由 nums[i] 和 nums[j] 组成且满足 0 <= i < j < nums.length
# 返回 所有数对距离中 第 k 小的数对距离。
# 测试链接 : https://leetcode.cn/problems/find-k-th-smallest-pair-distance/
class Code04_FindKthSmallestPairDistance:
    __java_fields__ = {}
    # 时间复杂度O(n * log(n) + log(max-min) * n)，额外空间复杂度O(1)
    @staticmethod
    def smallestDistancePair(nums, k):
        k = jcast('int', k)
        n = jcast('int', jget(nums, 'length'))
        jstatic('Arrays', 'sort', nums)
        ans = jcast('int', 0)
        # [0, 最大-最小]，不停二分
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (nums[jcast('int', (n - 1))] - nums[0])))
        m = 0
        cnt = 0
        while (l <= r):
            # m中点，arr中任意两数的差值 <= m
            m = jcast('int', jcast('int', jadd(l, jcast('int', (jcast('int', (r - l)) >> (1 & 31))))))
            # 返回数字对的数量
            cnt = jcast('int', Code04_FindKthSmallestPairDistance.f(nums, m))
            if (cnt >= k):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    # arr中任意两数的差值 <= limit
    # 这样的数字配对，有几对？
    @staticmethod
    def f(arr, limit):
        limit = jcast('int', limit)
        ans = jcast('int', 0)
        # O(n)
        l = jcast('int', 0)
        r = jcast('int', 0)
        while (l < jget(arr, 'length')):
            # l......r r+1
            while ((jcast('int', jadd(r, 1)) < jget(arr, 'length')) and (jcast('int', (arr[jcast('int', jadd(r, 1))] - arr[l])) <= limit)):
                r = jcast('int', (r + 1))
            # arr[l...r]范围上的数差值的绝对值都不超过limit
            # arr[0...3]
            # 0,1
            # 0,2
            # 0,3
            ans = jcast('int', jcast('int', jadd(ans, jcast('int', (r - l)))))
            l = jcast('int', (l + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


