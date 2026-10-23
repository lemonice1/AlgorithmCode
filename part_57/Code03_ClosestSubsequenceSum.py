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

# 最接近目标值的子序列和
# 给你一个整数数组 nums 和一个目标值 goal
# 你需要从 nums 中选出一个子序列，使子序列元素总和最接近 goal
# 也就是说，如果子序列元素和为 sum ，你需要 最小化绝对差 abs(sum - goal)
# 返回 abs(sum - goal) 可能的 最小值
# 注意，数组的子序列是通过移除原始数组中的某些元素（可能全部或无）而形成的数组。
# 数据量描述:
# 1 <= nums.length <= 40
# -10^7 <= nums[i] <= 10^7
# -10^9 <= goal <= 10^9
# 测试链接 : https://leetcode.cn/problems/closest-subsequence-sum/
class Code03_ClosestSubsequenceSum:
    __java_fields__ = {'MAXN': 'MAXN', 'lsum': 'lsum', 'rsum': 'rsum', 'fill': 'fill'}
    MAXN = 0
    lsum = None
    rsum = None
    fill = 0
    @staticmethod
    def minAbsDifference(nums, goal):
        goal = jcast('int', goal)
        n = jcast('int', jget(nums, 'length'))
        min = jcast('long', 0)
        max = jcast('long', 0)
        i = jcast('int', 0)
        while (i < n):
            if (nums[i] >= 0):
                max = jcast('long', jcast('long', jadd(max, nums[i])))
            else:
                min = jcast('long', jcast('long', jadd(min, nums[i])))
            i = jcast('int', (i + 1))
        if (max < goal):
            return jcast('int', jcast('int', jstatic('Math', 'abs', jcast('long', (max - goal)))))
        if (min > goal):
            return jcast('int', jcast('int', jstatic('Math', 'abs', jcast('long', (min - goal)))))
        # 原始数组排序，为了后面递归的时候，还能剪枝
        # 常数优化
        jstatic('Arrays', 'sort', nums)
        Code03_ClosestSubsequenceSum.fill = jcast('int', 0)
        Code03_ClosestSubsequenceSum.collect(nums, 0, jcast('int', (n >> (1 & 31))), 0, Code03_ClosestSubsequenceSum.lsum)
        lsize = jcast('int', Code03_ClosestSubsequenceSum.fill)
        Code03_ClosestSubsequenceSum.fill = jcast('int', 0)
        Code03_ClosestSubsequenceSum.collect(nums, jcast('int', (n >> (1 & 31))), n, 0, Code03_ClosestSubsequenceSum.rsum)
        rsize = jcast('int', Code03_ClosestSubsequenceSum.fill)
        jstatic('Arrays', 'sort', Code03_ClosestSubsequenceSum.lsum, 0, lsize)
        jstatic('Arrays', 'sort', Code03_ClosestSubsequenceSum.rsum, 0, rsize)
        ans = jcast('int', jstatic('Math', 'abs', goal))
        i = jcast('int', 0)
        j = jcast('int', jcast('int', (rsize - 1)))
        while (i < lsize):
            while ((j > 0) and (jstatic('Math', 'abs', jcast('int', (jcast('int', (goal - Code03_ClosestSubsequenceSum.lsum[i])) - Code03_ClosestSubsequenceSum.rsum[jcast('int', (j - 1))]))) <= jstatic('Math', 'abs', jcast('int', (jcast('int', (goal - Code03_ClosestSubsequenceSum.lsum[i])) - Code03_ClosestSubsequenceSum.rsum[j]))))):
                j = jcast('int', (j - 1))
            ans = jcast('int', jstatic('Math', 'min', ans, jstatic('Math', 'abs', jcast('int', (jcast('int', (goal - Code03_ClosestSubsequenceSum.lsum[i])) - Code03_ClosestSubsequenceSum.rsum[j])))))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def collect(nums, i, e, s, sum):
        i = jcast('int', i)
        e = jcast('int', e)
        s = jcast('int', s)
        if (i == e):
            jset(sum, ((_java_obj_1 := Code03_ClosestSubsequenceSum), (_java_key_2 := 'fill'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], s)
        else:
            # nums[i.....]这一组，相同的数字有几个
            j = jcast('int', jcast('int', jadd(i, 1)))
            while ((j < e) and (nums[j] == nums[i])):
                j = jcast('int', (j + 1))
            # nums[ 1 1 1 1 1 2....
            # i         j
            k = jcast('int', 0)
            while (k <= jcast('int', (j - i))):
                # k = 0个
                # k = 1个
                # k = 2个
                Code03_ClosestSubsequenceSum.collect(nums, j, e, jcast('int', jadd(s, jcast('int', (k * nums[i])))), sum)
                k = jcast('int', (k + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_ClosestSubsequenceSum.MAXN = jcast('int', jcast('int', (1 << (20 & 31))))
Code03_ClosestSubsequenceSum.lsum = jarray('int', [Code03_ClosestSubsequenceSum.MAXN])
Code03_ClosestSubsequenceSum.rsum = jarray('int', [Code03_ClosestSubsequenceSum.MAXN])
Code03_ClosestSubsequenceSum.fill = jcast('int', 0)
