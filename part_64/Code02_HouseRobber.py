# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 数组中不能选相邻元素的最大累加和
# 给定一个数组，可以随意选择数字
# 但是不能选择相邻的数字，返回能得到的最大累加和
# 测试链接 : https://leetcode.cn/problems/house-robber/
class Code02_HouseRobber:
    __java_fields__ = {}
    # 动态规划
    @staticmethod
    def rob1(nums):
        n = jcast('int', jget(nums, 'length'))
        if (n == 1):
            return jcast('int', nums[0])
        if (n == 2):
            return jcast('int', jstatic('Math', 'max', nums[0], nums[1]))
        # dp[i] : nums[0...i]范围上可以随意选择数字，但是不能选相邻数，能得到的最大累加和
        dp = jarray('int', [n])
        dp[0] = jcast('int', nums[0])
        jset(dp, 1, jstatic('Math', 'max', nums[0], nums[1]))
        i = jcast('int', 2)
        while (i < n):
            jset(dp, i, jstatic('Math', 'max', dp[jcast('int', (i - 1))], jstatic('Math', 'max', nums[i], jcast('int', jadd(dp[jcast('int', (i - 2))], nums[i])))))
            i = jcast('int', (i + 1))
        return jcast('int', dp[jcast('int', (n - 1))])

    # 空间压缩
    @staticmethod
    def rob2(nums):
        n = jcast('int', jget(nums, 'length'))
        if (n == 1):
            return jcast('int', nums[0])
        if (n == 2):
            return jcast('int', jstatic('Math', 'max', nums[0], nums[1]))
        prepre = jcast('int', nums[0])
        pre = jcast('int', jstatic('Math', 'max', nums[0], nums[1]))
        i = jcast('int', 2)
        cur = 0
        while (i < n):
            cur = jcast('int', jstatic('Math', 'max', pre, jstatic('Math', 'max', nums[i], jcast('int', jadd(prepre, nums[i])))))
            prepre = jcast('int', pre)
            pre = jcast('int', cur)
            i = jcast('int', (i + 1))
        return jcast('int', pre)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


