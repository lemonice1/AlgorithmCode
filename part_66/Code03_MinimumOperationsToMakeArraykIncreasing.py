# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 使数组K递增的最少操作次数
# 给你一个下标从0开始包含n个正整数的数组arr，和一个正整数k
# 如果对于每个满足 k <= i <= n-1 的下标 i
# 都有 arr[i-k] <= arr[i] ，那么称 arr 是K递增的
# 每一次操作中，你可以选择一个下标i并将arr[i]改成任意正整数
# 请你返回对于给定的 k ，使数组变成K递增的最少操作次数
# 测试链接 : https://leetcode.cn/problems/minimum-operations-to-make-the-array-k-increasing/
class Code03_MinimumOperationsToMakeArraykIncreasing:
    __java_fields__ = {'MAXN': 'MAXN', 'nums': 'nums', 'ends': 'ends'}
    MAXN = 0
    nums = None
    ends = None
    @staticmethod
    def kIncreasing(arr, k):
        k = jcast('int', k)
        n = jcast('int', jget(arr, 'length'))
        ans = jcast('int', 0)
        i = jcast('int', 0)
        size = 0
        while (i < k):
            size = jcast('int', 0)
            # 把每一组的数字放入容器
            j = jcast('int', i)
            while (j < n):
                jset(Code03_MinimumOperationsToMakeArraykIncreasing.nums, ((_java_old_1 := size), (size := jcast('int', (size + (1)))), _java_old_1)[2], arr[j])
                j = jcast('int', jcast('int', jadd(j, k)))
            # 当前组长度 - 当前组最长不下降子序列长度 = 当前组至少需要修改的数字个数
            ans = jcast('int', jcast('int', jadd(ans, jcast('int', (size - Code03_MinimumOperationsToMakeArraykIncreasing.lengthOfNoDecreasing(size))))))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # nums[0...size-1]中的最长不下降子序列长度
    @staticmethod
    def lengthOfNoDecreasing(size):
        size = jcast('int', size)
        len = jcast('int', 0)
        i = jcast('int', 0)
        find = 0
        while (i < size):
            find = jcast('int', Code03_MinimumOperationsToMakeArraykIncreasing.bs(len, Code03_MinimumOperationsToMakeArraykIncreasing.nums[i]))
            if (find == jcast('int', (-1))):
                jset(Code03_MinimumOperationsToMakeArraykIncreasing.ends, ((_java_old_2 := len), (len := jcast('int', (len + (1)))), _java_old_2)[2], Code03_MinimumOperationsToMakeArraykIncreasing.nums[i])
            else:
                Code03_MinimumOperationsToMakeArraykIncreasing.ends[find] = jcast('int', Code03_MinimumOperationsToMakeArraykIncreasing.nums[i])
            i = jcast('int', (i + 1))
        return jcast('int', len)

    @staticmethod
    def bs(len, num):
        len = jcast('int', len)
        num = jcast('int', num)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (len - 1)))
        m = 0
        ans = jcast('int', jcast('int', (-1)))
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (num < Code03_MinimumOperationsToMakeArraykIncreasing.ends[m]):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_MinimumOperationsToMakeArraykIncreasing.MAXN = jcast('int', 100001)
Code03_MinimumOperationsToMakeArraykIncreasing.nums = jarray('int', [Code03_MinimumOperationsToMakeArraykIncreasing.MAXN])
Code03_MinimumOperationsToMakeArraykIncreasing.ends = jarray('int', [Code03_MinimumOperationsToMakeArraykIncreasing.MAXN])
