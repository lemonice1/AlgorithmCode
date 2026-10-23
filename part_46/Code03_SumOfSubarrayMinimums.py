# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 子数组的最小值之和
# 给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
# 由于答案可能很大，答案对 1000000007 取模
# 测试链接 : https://leetcode.cn/problems/sum-of-subarray-minimums/
class Code03_SumOfSubarrayMinimums:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'stack': 'stack', 'r': 'r'}
    MOD = 0
    MAXN = 0
    stack = None
    r = 0
    @staticmethod
    def sumSubarrayMins(arr):
        ans = jcast('long', 0)
        Code03_SumOfSubarrayMinimums.r = jcast('int', 0)
        # 注意课上讲的相等情况的修正
        i = jcast('int', 0)
        while (i < jget(arr, 'length')):
            while ((Code03_SumOfSubarrayMinimums.r > 0) and (arr[Code03_SumOfSubarrayMinimums.stack[jcast('int', (Code03_SumOfSubarrayMinimums.r - 1))]] >= arr[i])):
                cur = jcast('int', Code03_SumOfSubarrayMinimums.stack[((_java_obj_1 := Code03_SumOfSubarrayMinimums), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))))[3]])
                left = jcast('int', (jcast('int', (-1)) if (Code03_SumOfSubarrayMinimums.r == 0) else Code03_SumOfSubarrayMinimums.stack[jcast('int', (Code03_SumOfSubarrayMinimums.r - 1))]))
                ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, jcast('long', (jcast('long', (jcast('long', jcast('int', (cur - left))) * jcast('int', (i - cur)))) * arr[cur])))), Code03_SumOfSubarrayMinimums.MOD)))
            jset(Code03_SumOfSubarrayMinimums.stack, ((_java_obj_4 := Code03_SumOfSubarrayMinimums), (_java_key_5 := 'r'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], i)
            i = jcast('int', (i + 1))
        while (Code03_SumOfSubarrayMinimums.r > 0):
            cur = jcast('int', Code03_SumOfSubarrayMinimums.stack[((_java_obj_7 := Code03_SumOfSubarrayMinimums), (_java_key_8 := 'r'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))))[3]])
            left = jcast('int', (jcast('int', (-1)) if (Code03_SumOfSubarrayMinimums.r == 0) else Code03_SumOfSubarrayMinimums.stack[jcast('int', (Code03_SumOfSubarrayMinimums.r - 1))]))
            ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, jcast('long', (jcast('long', (jcast('long', jcast('int', (cur - left))) * jcast('int', (jget(arr, 'length') - cur)))) * arr[cur])))), Code03_SumOfSubarrayMinimums.MOD)))
        return jcast('int', jcast('int', ans))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_SumOfSubarrayMinimums.MOD = jcast('int', 1000000007)
Code03_SumOfSubarrayMinimums.MAXN = jcast('int', 30001)
Code03_SumOfSubarrayMinimums.stack = jarray('int', [Code03_SumOfSubarrayMinimums.MAXN])
Code03_SumOfSubarrayMinimums.r = jcast('int', 0)
