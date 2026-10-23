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

# 返回无序数组中累加和为给定值的子数组个数
# 测试链接 : https://leetcode.cn/problems/subarray-sum-equals-k/
class Code03_NumberOfSubarraySumEqualsAim:
    __java_fields__ = {}
    @staticmethod
    def subarraySum(nums, aim):
        aim = jcast('int', aim)
        map = jnew('HashMap')
        # 0这个前缀和，在没有任何数字的时候，已经有1次了
        jcall(map, 'put', 0, 1)
        ans = jcast('int', 0)
        i = jcast('int', 0)
        sum = jcast('int', 0)
        while (i < jget(nums, 'length')):
            # sum : 0...i前缀和
            sum = jcast('int', jcast('int', jadd(sum, nums[i])))
            ans = jcast('int', jadd(ans, jcall(map, 'getOrDefault', jcast('int', (sum - aim)), 0)))
            jcall(map, 'put', sum, jadd(jcall(map, 'getOrDefault', sum, 0), 1))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


