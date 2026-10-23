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

# 乘积最大子数组
# 给你一个整数数组 nums
# 请你找出数组中乘积最大的非空连续子数组
# 并返回该子数组所对应的乘积
# 测试链接 : https://leetcode.cn/problems/maximum-product-subarray/
class Code01_MaximumProductSubarray:
    __java_fields__ = {}
    # 这节课讲完之后，测试数据又增加了
    # 用int类型的变量会让中间结果溢出
    # 所以改成用double类型的变量
    # 思路是不变的
    @staticmethod
    def maxProduct(nums):
        ans = jcast('double', nums[0])
        min = jcast('double', nums[0])
        max = jcast('double', nums[0])
        curmin = 0.0
        curmax = 0.0
        i = jcast('int', 1)
        while (i < jget(nums, 'length')):
            curmin = jcast('double', jstatic('Math', 'min', nums[i], jstatic('Math', 'min', (min * nums[i]), (max * nums[i]))))
            curmax = jcast('double', jstatic('Math', 'max', nums[i], jstatic('Math', 'max', (min * nums[i]), (max * nums[i]))))
            min = jcast('double', curmin)
            max = jcast('double', curmax)
            ans = jcast('double', jstatic('Math', 'max', ans, max))
            i = jcast('int', (i + 1))
        return jcast('int', jcast('int', ans))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


