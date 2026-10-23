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

# 和至少为K的最短子数组
# 给定一个数组arr，其中的值有可能正、负、0
# 给定一个正数k
# 返回累加和>=k的所有子数组中，最短的子数组长度
# 测试链接 : https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/
class Code01_ShortestSubarrayWithSumAtLeastK:
    __java_fields__ = {'MAXN': 'MAXN', 'sum': 'sum', 'deque': 'deque', 'h': 'h', 't': 't'}
    MAXN = 0
    # sum[0] : 前0个数的前缀和
    # sum[i] : 前i个数的前缀和
    sum = None
    deque = None
    h = 0
    t = 0
    @staticmethod
    def shortestSubarray(arr, K):
        K = jcast('int', K)
        n = jcast('int', jget(arr, 'length'))
        i = jcast('int', 0)
        while (i < n):
            # [3,4,5]
            # 0 1 2
            # sum[0] = 0
            # sum[1] = 3
            # sum[2] = 7
            # sum[3] = 12
            Code01_ShortestSubarrayWithSumAtLeastK.sum[jcast('int', jadd(i, 1))] = jcast('long', jcast('long', jadd(Code01_ShortestSubarrayWithSumAtLeastK.sum[i], arr[i])))
            i = jcast('int', (i + 1))
        Code01_ShortestSubarrayWithSumAtLeastK.h = jcast('int', jset(Code01_ShortestSubarrayWithSumAtLeastK, 't', 0))
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        i = jcast('int', 0)
        while (i <= n):
            # 前0个数前缀和
            # 前1个数前缀和
            # 前2个数前缀和
            # ...
            # 前n个数前缀和
            while ((Code01_ShortestSubarrayWithSumAtLeastK.h != Code01_ShortestSubarrayWithSumAtLeastK.t) and (jcast('long', (Code01_ShortestSubarrayWithSumAtLeastK.sum[i] - Code01_ShortestSubarrayWithSumAtLeastK.sum[Code01_ShortestSubarrayWithSumAtLeastK.deque[Code01_ShortestSubarrayWithSumAtLeastK.h]])) >= K)):
                # 如果当前的前缀和 - 头前缀和，达标！
                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', (i - Code01_ShortestSubarrayWithSumAtLeastK.deque[((_java_obj_1 := Code01_ShortestSubarrayWithSumAtLeastK), (_java_key_2 := 'h'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]]))))
            # 前i个数前缀和，从尾部加入
            # 小 大
            while ((Code01_ShortestSubarrayWithSumAtLeastK.h != Code01_ShortestSubarrayWithSumAtLeastK.t) and (Code01_ShortestSubarrayWithSumAtLeastK.sum[Code01_ShortestSubarrayWithSumAtLeastK.deque[jcast('int', (Code01_ShortestSubarrayWithSumAtLeastK.t - 1))]] >= Code01_ShortestSubarrayWithSumAtLeastK.sum[i])):
                Code01_ShortestSubarrayWithSumAtLeastK.t = jcast('int', (Code01_ShortestSubarrayWithSumAtLeastK.t - 1))
            jset(Code01_ShortestSubarrayWithSumAtLeastK.deque, ((_java_obj_4 := Code01_ShortestSubarrayWithSumAtLeastK), (_java_key_5 := 't'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], i)
            i = jcast('int', (i + 1))
        return jcast('int', (ans if (ans != jget(Integer, 'MAX_VALUE')) else jcast('int', (-1))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_ShortestSubarrayWithSumAtLeastK.MAXN = jcast('int', 100001)
Code01_ShortestSubarrayWithSumAtLeastK.sum = jarray('long', [Code01_ShortestSubarrayWithSumAtLeastK.MAXN])
Code01_ShortestSubarrayWithSumAtLeastK.deque = jarray('int', [Code01_ShortestSubarrayWithSumAtLeastK.MAXN])
Code01_ShortestSubarrayWithSumAtLeastK.h = jcast('int', 0)
Code01_ShortestSubarrayWithSumAtLeastK.t = jcast('int', 0)
