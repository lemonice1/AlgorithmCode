# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最后一块石头的重量 II
# 有一堆石头，用整数数组 stones 表示
# 其中 stones[i] 表示第 i 块石头的重量。
# 每一回合，从中选出任意两块石头，然后将它们一起粉碎
# 假设石头的重量分别为 x 和 y，且 x <= y
# 那么粉碎的可能结果如下：
# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x
# 最后，最多只会剩下一块 石头，返回此石头 最小的可能重量
# 如果没有石头剩下，就返回 0
# 测试链接 : https://leetcode.cn/problems/last-stone-weight-ii/
class Code04_LastStoneWeightII:
    __java_fields__ = {}
    @staticmethod
    def lastStoneWeightII(nums):
        sum = jcast('int', 0)
        for num in nums:
            sum = jcast('int', jcast('int', jadd(sum, num)))
        # nums中随意选择数字
        # 累加和一定要 <= sum / 2
        # 又尽量接近
        near = jcast('int', Code04_LastStoneWeightII.near(nums, jcast('int', jdiv(sum, 2))))
        return jcast('int', jcast('int', (jcast('int', (sum - near)) - near)))

    # 非负数组nums中，子序列累加和不超过t，但是最接近t的累加和是多少
    # 01背包问题(子集累加和尽量接近t) + 空间压缩
    @staticmethod
    def near(nums, t):
        t = jcast('int', t)
        dp = jarray('int', [jcast('int', jadd(t, 1))])
        for num in nums:
            j = jcast('int', t)
            while (j >= num):
                # dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-nums[i]]+nums[i])
                jset(dp, j, jstatic('Math', 'max', dp[j], jcast('int', jadd(dp[jcast('int', (j - num))], num))))
                j = jcast('int', (j - 1))
        return jcast('int', dp[t])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


