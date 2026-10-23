# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 数组中只有1种数出现次数少于m次，其他数都出现了m次
# 返回出现次数小于m次的那种数
# 测试链接 : https://leetcode.cn/problems/single-number-ii/
# 注意 : 测试题目只是通用方法的一个特例，课上讲了更通用的情况
class Code06_OneKindNumberLessMtimes:
    __java_fields__ = {}
    @staticmethod
    def singleNumber(nums):
        return jcast('int', Code06_OneKindNumberLessMtimes.find(nums, 3))

    # 更通用的方法
    # 已知数组中只有1种数出现次数少于m次，其他数都出现了m次
    # 返回出现次数小于m次的那种数
    @staticmethod
    def find(arr, m):
        m = jcast('int', m)
        # cnts[0] : 0位上有多少个1
        # cnts[i] : i位上有多少个1
        # cnts[31] : 31位上有多少个1
        cnts = jarray('int', [32])
        for num in arr:
            i = jcast('int', 0)
            while (i < 32):
                cnts[i] = jcast('int', jcast('int', jadd(cnts[i], jcast('int', (jcast('int', (num >> (i & 31))) & 1)))))
                i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < 32):
            if (jcast('int', jmod(cnts[i], m)) != 0):
                ans = jcast('int', jcast('int', (ans | jcast('int', (1 << (i & 31))))))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


