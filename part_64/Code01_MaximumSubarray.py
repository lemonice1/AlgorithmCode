# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 子数组最大累加和
# 给你一个整数数组 nums
# 返回非空子数组的最大累加和
# 测试链接 : https://leetcode.cn/problems/maximum-subarray/
class Code01_MaximumSubarray:
    __java_fields__ = {'left': 'left', 'right': 'right', 'sum': 'sum'}
    # 动态规划
    @staticmethod
    def maxSubArray1(nums):
        n = jcast('int', jget(nums, 'length'))
        # dp[i] : 子数组必须以i位置的数做结尾，往左能延伸出来的最大累加和
        dp = jarray('int', [n])
        dp[0] = jcast('int', nums[0])
        ans = jcast('int', nums[0])
        i = jcast('int', 1)
        while (i < n):
            jset(dp, i, jstatic('Math', 'max', nums[i], jcast('int', jadd(dp[jcast('int', (i - 1))], nums[i]))))
            ans = jcast('int', jstatic('Math', 'max', ans, dp[i]))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 空间压缩
    @staticmethod
    def maxSubArray2(nums):
        n = jcast('int', jget(nums, 'length'))
        ans = jcast('int', nums[0])
        i = jcast('int', 1)
        pre = jcast('int', nums[0])
        while (i < n):
            pre = jcast('int', jstatic('Math', 'max', nums[i], jcast('int', jadd(pre, nums[i]))))
            ans = jcast('int', jstatic('Math', 'max', ans, pre))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 如下代码为附加问题的实现
    # 子数组中找到拥有最大累加和的子数组
    # 并返回如下三个信息:
    # 1) 最大累加和子数组的开头left
    # 2) 最大累加和子数组的结尾right
    # 3) 最大累加和子数组的累加和sum
    # 如果不止一个子数组拥有最大累加和，那么找到哪一个都可以
    left = 0
    right = 0
    sum = 0
    # 找到拥有最大累加和的子数组
    # 更新好全局变量left、right、sum
    # 上游调用函数可以直接使用这三个变量
    # 相当于返回了三个值
    @staticmethod
    def extra(nums):
        Code01_MaximumSubarray.sum = jcast('int', jget(Integer, 'MIN_VALUE'))
        l = jcast('int', 0)
        r = jcast('int', 0)
        pre = jcast('int', jget(Integer, 'MIN_VALUE'))
        while (r < jget(nums, 'length')):
            if (pre >= 0):
                # 吸收前面的累加和有利可图
                # 那就不换开头
                pre = jcast('int', jcast('int', jadd(pre, nums[r])))
            else:
                # 吸收前面的累加和已经无利可图
                # 那就换开头
                pre = jcast('int', nums[r])
                l = jcast('int', r)
            if (pre > Code01_MaximumSubarray.sum):
                Code01_MaximumSubarray.sum = jcast('int', pre)
                Code01_MaximumSubarray.left = jcast('int', l)
                Code01_MaximumSubarray.right = jcast('int', r)
            r = jcast('int', (r + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_MaximumSubarray.left = jcast('int', 0)
Code01_MaximumSubarray.right = jcast('int', 0)
Code01_MaximumSubarray.sum = jcast('int', 0)
