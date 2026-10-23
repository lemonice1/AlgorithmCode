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

# 寻找重复数
# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n）
# 可知至少存在一个重复的整数。
# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
# 测试链接 : https://leetcode.cn/problems/find-the-duplicate-number/
class Code02_FindTheDuplicateNumber:
    __java_fields__ = {}
    # 时间复杂度O(n)，额外空间复杂度O(1)
    @staticmethod
    def findDuplicate(nums):
        if ((nums == None) or (jget(nums, 'length') < 2)):
            return jcast('int', jcast('int', (-1)))
        slow = jcast('int', nums[0])
        fast = jcast('int', nums[nums[0]])
        while (slow != fast):
            slow = jcast('int', nums[slow])
            fast = jcast('int', nums[nums[fast]])
        # 相遇了，快指针回开头
        fast = jcast('int', 0)
        while (slow != fast):
            fast = jcast('int', nums[fast])
            slow = jcast('int', nums[slow])
        return jcast('int', slow)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


