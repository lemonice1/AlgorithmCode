# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 利用前缀和快速得到区域累加和
# 测试链接 : https://leetcode.cn/problems/range-sum-query-immutable/
class Code01_PrefixSumArray:
    __java_fields__ = {}
    class NumArray:
        __java_fields__ = {'sum': 'sum'}
        # sum：实例字段，在构造函数中初始化。
        def _java_init_0(self, nums):
            self.sum = jarray('int', [jcast('int', jadd(jget(nums, 'length'), 1))])
            i = jcast('int', 1)
            while (i <= jget(nums, 'length')):
                self.sum[i] = jcast('int', jcast('int', jadd(self.sum[jcast('int', (i - 1))], nums[jcast('int', (i - 1))])))
                i = jcast('int', (i + 1))

        def sumRange(self, left, right):
            left = jcast('int', left)
            right = jcast('int', right)
            return jcast('int', jcast('int', (self.sum[jcast('int', jadd(right, 1))] - self.sum[left])))

        def __init__(self, *args, _java_ctor=None):
            self.sum = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int[]']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_PrefixSumArray.NumArray.NumArray")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


