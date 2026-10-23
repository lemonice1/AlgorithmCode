# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 使数组相似的最少操作次数
# 给你两个正整数数组 nums 和 target ，两个数组长度相等
# 在一次操作中，你可以选择两个 不同 的下标 i 和 j
# 其中 0 <= i, j < nums.length ，并且：
# 令 nums[i] = nums[i] + 2 且
# 令 nums[j] = nums[j] - 2
# 如果两个数组中每个元素出现的频率相等，我们称两个数组是 相似 的
# 请你返回将 nums 变得与 target 相似的最少操作次数
# 测试数据保证nums一定能变得与target相似
# 测试链接 : https://leetcode.cn/problems/minimum-number-of-operations-to-make-arrays-similar/
class Code03_MinimumOperationsMakeSimilar:
    __java_fields__ = {}
    @staticmethod
    def makeSimilar(nums, target):
        n = jcast('int', jget(nums, 'length'))
        oddSize = jcast('int', Code03_MinimumOperationsMakeSimilar.split(nums, n))
        Code03_MinimumOperationsMakeSimilar.split(target, n)
        jstatic('Arrays', 'sort', nums, 0, oddSize)
        jstatic('Arrays', 'sort', nums, oddSize, n)
        jstatic('Arrays', 'sort', target, 0, oddSize)
        jstatic('Arrays', 'sort', target, oddSize, n)
        ans = jcast('long', 0)
        i = jcast('int', 0)
        while (i < n):
            ans = jcast('long', jcast('long', jadd(ans, jstatic('Math', 'abs', jcast('long', (jcast('long', nums[i]) - target[i]))))))
            i = jcast('int', (i + 1))
        return jcast('long', jcast('long', jdiv(ans, 4)))

    # 把数组分割成左部分全是奇数，右部分全是偶数
    # 返回左部分的长度
    @staticmethod
    def split(arr, n):
        n = jcast('int', n)
        oddSize = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            if (jcast('int', (arr[i] & 1)) == 1):
                Code03_MinimumOperationsMakeSimilar.swap(arr, i, ((_java_old_1 := oddSize), (oddSize := jcast('int', (oddSize + (1)))), _java_old_1)[2])
            i = jcast('int', (i + 1))
        return jcast('int', oddSize)

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


