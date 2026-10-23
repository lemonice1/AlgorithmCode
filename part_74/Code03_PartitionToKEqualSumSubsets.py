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

# 划分为k个相等的子集
# 给定一个整数数组  nums 和一个正整数 k，
# 找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
# 测试链接 : https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/
class Code03_PartitionToKEqualSumSubsets:
    __java_fields__ = {}
    # 状压dp的解法
    # 这是最正式的解
    @staticmethod
    def canPartitionKSubsets1(nums, k):
        k = jcast('int', k)
        sum = jcast('int', 0)
        for num in nums:
            sum = jcast('int', jcast('int', jadd(sum, num)))
        if (jcast('int', jmod(sum, k)) != 0):
            return jcast('boolean', False)
        n = jcast('int', jget(nums, 'length'))
        dp = jarray('int', [jcast('int', (1 << (n & 31)))])
        return jcast('boolean', Code03_PartitionToKEqualSumSubsets.f1(nums, jcast('int', jdiv(sum, k)), jcast('int', (jcast('int', (1 << (n & 31))) - 1)), 0, k, dp))

    # 就是题目2的递归函数
    @staticmethod
    def f1(nums, limit, status, cur, rest, dp):
        limit = jcast('int', limit)
        status = jcast('int', status)
        cur = jcast('int', cur)
        rest = jcast('int', rest)
        if (rest == 0):
            return jcast('boolean', (status == 0))
        if (dp[status] != 0):
            return jcast('boolean', (dp[status] == 1))
        ans = jcast('boolean', False)
        i = jcast('int', 0)
        while (i < jget(nums, 'length')):
            try:
                if ((jcast('int', (status & jcast('int', (1 << (i & 31))))) != 0) and (jcast('int', jadd(cur, nums[i])) <= limit)):
                    if (jcast('int', jadd(cur, nums[i])) == limit):
                        ans = jcast('boolean', Code03_PartitionToKEqualSumSubsets.f1(nums, limit, jcast('int', (status ^ jcast('int', (1 << (i & 31))))), 0, jcast('int', (rest - 1)), dp))
                    else:
                        ans = jcast('boolean', Code03_PartitionToKEqualSumSubsets.f1(nums, limit, jcast('int', (status ^ jcast('int', (1 << (i & 31))))), jcast('int', jadd(cur, nums[i])), rest, dp))
                    if ans:
                        raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        dp[status] = jcast('int', (1 if ans else jcast('int', (-1))))
        return jcast('boolean', ans)

    # 纯暴力的递归（不做任何动态规划），利用良好的剪枝策略，可以做到非常好的效率
    # 但这并不是正式的解，如果数据设计的很苛刻，是通过不了的
    @staticmethod
    def canPartitionKSubsets2(nums, k):
        k = jcast('int', k)
        sum = jcast('int', 0)
        for num in nums:
            sum = jcast('int', jcast('int', jadd(sum, num)))
        if (jcast('int', jmod(sum, k)) != 0):
            return jcast('boolean', False)
        n = jcast('int', jget(nums, 'length'))
        jstatic('Arrays', 'sort', nums)
        return jcast('boolean', Code03_PartitionToKEqualSumSubsets.f2(jarray('int', [k]), jcast('int', jdiv(sum, k)), nums, jcast('int', (n - 1))))

    # group里面是各个集合已经有的累加和
    # 随着递归的展开，group里的累加和会变化
    # 所以这是一个带路径的递归，而且路径信息比较复杂(group数组)
    # 本版本采用剪枝搜索，不展开完整的动态规划状态
    # group[0....index]这些数字，填入每个集合，一定要都使用
    # 每个集合的累加和一定都要是target，返回能不能做到
    @staticmethod
    def f2(group, target, nums, index):
        target = jcast('int', target)
        index = jcast('int', index)
        if (index < 0):
            return jcast('boolean', True)
        num = jcast('int', nums[index])
        len = jcast('int', jget(group, 'length'))
        i = jcast('int', 0)
        while (i < len):
            if (jcast('int', jadd(group[i], num)) <= target):
                # 当前数字num放进i号集合
                group[i] = jcast('int', jcast('int', jadd(group[i], num)))
                if Code03_PartitionToKEqualSumSubsets.f2(group, target, nums, jcast('int', (index - 1))):
                    return jcast('boolean', True)
                # 递归完成后将路径还原
                group[i] = jcast('int', jcast('int', (group[i] - num)))
                while ((jcast('int', jadd(i, 1)) < jget(group, 'length')) and (group[i] == group[jcast('int', jadd(i, 1))])):
                    i = jcast('int', (i + 1))
            i = jcast('int', (i + 1))
        return jcast('boolean', False)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


