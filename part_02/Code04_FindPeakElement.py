# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 峰值元素是指其值严格大于左右相邻值的元素
# 给你一个整数数组 nums，已知任何两个相邻的值都不相等
# 找到峰值元素并返回其索引
# 数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
# 你可以假设 nums[-1] = nums[n] = 无穷小
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
class Code04_FindPeakElement:
    __java_fields__ = {}
    # 测试链接 : https://leetcode.cn/problems/find-peak-element/
    class Solution:
        __java_fields__ = {}
        @staticmethod
        def findPeakElement(arr):
            n = jcast('int', jget(arr, 'length'))
            if (jget(arr, 'length') == 1):
                return jcast('int', 0)
            if (arr[0] > arr[1]):
                return jcast('int', 0)
            if (arr[jcast('int', (n - 1))] > arr[jcast('int', (n - 2))]):
                return jcast('int', jcast('int', (n - 1)))
            l = jcast('int', 1)
            r = jcast('int', jcast('int', (n - 2)))
            m = jcast('int', 0)
            ans = jcast('int', jcast('int', (-1)))
            while (l <= r):
                try:
                    m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
                    if (arr[jcast('int', (m - 1))] > arr[m]):
                        r = jcast('int', jcast('int', (m - 1)))
                    else:
                        if (arr[m] < arr[jcast('int', jadd(m, 1))]):
                            l = jcast('int', jcast('int', jadd(m, 1)))
                        else:
                            ans = jcast('int', m)
                            raise JBreak(None)
                except JContinue as _java_control_1:
                    if _java_control_1.label not in (None,):
                        raise
                except JBreak as _java_control_1:
                    if _java_control_1.label not in (None,):
                        raise
                    break
            return jcast('int', ans)

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


