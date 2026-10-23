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

# 接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水
# 测试链接 : https://leetcode.cn/problems/trapping-rain-water/
class Code03_TrappingRainWater:
    __java_fields__ = {}
    # 辅助数组的解法（不是最优解）
    # 时间复杂度O(n)，额外空间复杂度O(n)
    # 提交时改名为trap
    @staticmethod
    def trap1(nums):
        n = jcast('int', jget(nums, 'length'))
        lmax = jarray('int', [n])
        rmax = jarray('int', [n])
        lmax[0] = jcast('int', nums[0])
        # 0~i范围上的最大值，记录在lmax[i]
        i = jcast('int', 1)
        while (i < n):
            jset(lmax, i, jstatic('Math', 'max', lmax[jcast('int', (i - 1))], nums[i]))
            i = jcast('int', (i + 1))
        rmax[jcast('int', (n - 1))] = jcast('int', nums[jcast('int', (n - 1))])
        # i~n-1范围上的最大值，记录在rmax[i]
        i = jcast('int', jcast('int', (n - 2)))
        while (i >= 0):
            jset(rmax, i, jstatic('Math', 'max', rmax[jcast('int', jadd(i, 1))], nums[i]))
            i = jcast('int', (i - 1))
        ans = jcast('int', 0)
        # x              x
        # 0 1 2 3...n-2 n-1
        i = jcast('int', 1)
        while (i < jcast('int', (n - 1))):
            ans = jcast('int', jcast('int', jadd(ans, jstatic('Math', 'max', 0, jcast('int', (jstatic('Math', 'min', lmax[jcast('int', (i - 1))], rmax[jcast('int', jadd(i, 1))]) - nums[i]))))))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 双指针的解法（最优解）
    # 时间复杂度O(n)，额外空间复杂度O(1)
    # 提交时改名为trap
    @staticmethod
    def trap2(nums):
        l = jcast('int', 1)
        r = jcast('int', jcast('int', (jget(nums, 'length') - 2)))
        lmax = jcast('int', nums[0])
        rmax = jcast('int', nums[jcast('int', (jget(nums, 'length') - 1))])
        ans = jcast('int', 0)
        while (l <= r):
            if (lmax <= rmax):
                ans = jcast('int', jcast('int', jadd(ans, jstatic('Math', 'max', 0, jcast('int', (lmax - nums[l]))))))
                lmax = jcast('int', jstatic('Math', 'max', lmax, nums[((_java_old_1 := l), (l := jcast('int', (l + (1)))), _java_old_1)[2]]))
            else:
                ans = jcast('int', jcast('int', jadd(ans, jstatic('Math', 'max', 0, jcast('int', (rmax - nums[r]))))))
                rmax = jcast('int', jstatic('Math', 'max', rmax, nums[((_java_old_2 := r), (r := jcast('int', (r + (-1)))), _java_old_2)[2]]))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


