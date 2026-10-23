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

# 将数组分成几个递增序列
# 给你一个有序的正数数组 nums 和整数 K
# 判断该数组是否可以被分成一个或几个 长度至少 为 K 的 不相交的递增子序列
# 数组中的所有数字，都要被，若干不相交的递增子序列包含
# 测试链接 : https://leetcode.cn/problems/divide-array-into-increasing-sequences/
class Code05_DivideArrayIncreasingSequences:
    __java_fields__ = {}
    @staticmethod
    def canDivideIntoSubsequences(nums, k):
        k = jcast('int', k)
        cnt = jcast('int', 1)
        # maxCnt : 最大词频
        maxCnt = jcast('int', 1)
        # 在有序数组中，求某个数的最大词频
        i = jcast('int', 1)
        while (i < jget(nums, 'length')):
            if (nums[jcast('int', (i - 1))] != nums[i]):
                maxCnt = jcast('int', jstatic('Math', 'max', maxCnt, cnt))
                cnt = jcast('int', 1)
            else:
                cnt = jcast('int', (cnt + 1))
            i = jcast('int', (i + 1))
        maxCnt = jcast('int', jstatic('Math', 'max', maxCnt, cnt))
        # 向下取整如果满足 >= k
        # 那么所有的递增子序列长度一定 >= k
        return jcast('boolean', (jcast('int', jdiv(jget(nums, 'length'), maxCnt)) >= k))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


