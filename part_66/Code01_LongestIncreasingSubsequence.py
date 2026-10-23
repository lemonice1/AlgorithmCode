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

# 最长递增子序列和最长不下降子序列
# 给定一个整数数组nums
# 找到其中最长严格递增子序列长度、最长不下降子序列长度
# 测试链接 : https://leetcode.cn/problems/longest-increasing-subsequence/
class Code01_LongestIncreasingSubsequence:
    __java_fields__ = {}
    # 普通解法的动态规划
    # 时间复杂度O(n^2)，数组稍大就会超时
    @staticmethod
    def lengthOfLIS1(nums):
        n = jcast('int', jget(nums, 'length'))
        dp = jarray('int', [n])
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            dp[i] = jcast('int', 1)
            j = jcast('int', 0)
            while (j < i):
                if (nums[j] < nums[i]):
                    jset(dp, i, jstatic('Math', 'max', dp[i], jcast('int', jadd(dp[j], 1))))
                j = jcast('int', (j + 1))
            ans = jcast('int', jstatic('Math', 'max', ans, dp[i]))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 最优解
    # 时间复杂度O(n * logn)
    @staticmethod
    def lengthOfLIS2(nums):
        n = jcast('int', jget(nums, 'length'))
        ends = jarray('int', [n])
        # len表示ends数组目前的有效区长度
        # ends[0...len-1]是有效区，有效区内的数字一定严格升序
        len = jcast('int', 0)
        i = jcast('int', 0)
        find = 0
        while (i < n):
            find = jcast('int', Code01_LongestIncreasingSubsequence.bs1(ends, len, nums[i]))
            if (find == jcast('int', (-1))):
                jset(ends, ((_java_old_1 := len), (len := jcast('int', (len + (1)))), _java_old_1)[2], nums[i])
            else:
                ends[find] = jcast('int', nums[i])
            i = jcast('int', (i + 1))
        return jcast('int', len)

    # "最长递增子序列"使用如下二分搜索 :
    # ends[0...len-1]是严格升序的，找到>=num的最左位置
    # 如果不存在返回-1
    @staticmethod
    def bs1(ends, len, num):
        len = jcast('int', len)
        num = jcast('int', num)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (len - 1)))
        m = 0
        ans = jcast('int', jcast('int', (-1)))
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (ends[m] >= num):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    # 如果求最长不下降子序列，那么使用如下的二分搜索 :
    # ends[0...len-1]是不降序的
    # 在其中找到>num的最左位置，如果不存在返回-1
    # 如果求最长不下降子序列，就在lengthOfLIS中把bs1方法换成bs2方法
    # 已经用对数器验证了，是正确的
    @staticmethod
    def bs2(ends, len, num):
        len = jcast('int', len)
        num = jcast('int', num)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (len - 1)))
        m = 0
        ans = jcast('int', jcast('int', (-1)))
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (ends[m] > num):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


