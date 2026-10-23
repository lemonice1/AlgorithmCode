# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 缺失的第一个正数
# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
# 测试链接 : https://leetcode.cn/problems/first-missing-positive/
class Code07_FirstMissingPositive:
    __java_fields__ = {}
    # 时间复杂度O(n)，额外空间复杂度O(1)
    @staticmethod
    def firstMissingPositive(arr):
        # l的左边，都是做到i位置上放着i+1的区域
        # 永远盯着l位置的数字看，看能不能扩充(l++)
        l = jcast('int', 0)
        # [r....]垃圾区
        # 最好的状况下，认为1~r是可以收集全的，每个数字收集1个，不能有垃圾
        # 有垃圾呢？预期就会变差(r--)
        r = jcast('int', jget(arr, 'length'))
        while (l < r):
            if (arr[l] == jcast('int', jadd(l, 1))):
                l = jcast('int', (l + 1))
            else:
                if (((arr[l] <= l) or (arr[l] > r)) or (arr[jcast('int', (arr[l] - 1))] == arr[l])):
                    Code07_FirstMissingPositive.swap(arr, l, (r := jcast('int', (r + (-1)))))
                else:
                    Code07_FirstMissingPositive.swap(arr, l, jcast('int', (arr[l] - 1)))
        return jcast('int', jcast('int', jadd(l, 1)))

    @staticmethod
    def swap(arr, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', arr[i])
        arr[i] = jcast('int', arr[j])
        arr[j] = jcast('int', tmp)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


