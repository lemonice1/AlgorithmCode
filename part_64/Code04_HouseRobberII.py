# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 环形数组中不能选相邻元素的最大累加和
# 给定一个数组nums，长度为n
# nums是一个环形数组，下标0和下标n-1是连在一起的
# 可以随意选择数字，但是不能选择相邻的数字
# 返回能得到的最大累加和
# 测试链接 : https://leetcode.cn/problems/house-robber-ii/
class Code04_HouseRobberII:
    __java_fields__ = {}
    @staticmethod
    def rob(nums):
        n = jcast('int', jget(nums, 'length'))
        if (n == 1):
            return jcast('int', nums[0])
        return jcast('int', jstatic('Math', 'max', Code04_HouseRobberII.best(nums, 1, jcast('int', (n - 1))), jcast('int', jadd(nums[0], Code04_HouseRobberII.best(nums, 2, jcast('int', (n - 2)))))))

    # nums[l....r]范围上，没有环形的概念
    # 返回 : 可以随意选择数字，但不能选择相邻数字的情况下，最大累加和
    @staticmethod
    def best(nums, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l > r):
            return jcast('int', 0)
        if (l == r):
            return jcast('int', nums[l])
        if (jcast('int', jadd(l, 1)) == r):
            return jcast('int', jstatic('Math', 'max', nums[l], nums[r]))
        prepre = jcast('int', nums[l])
        pre = jcast('int', jstatic('Math', 'max', nums[l], nums[jcast('int', jadd(l, 1))]))
        i = jcast('int', jcast('int', jadd(l, 2)))
        cur = 0
        while (i <= r):
            cur = jcast('int', jstatic('Math', 'max', pre, jcast('int', jadd(nums[i], jstatic('Math', 'max', 0, prepre)))))
            prepre = jcast('int', pre)
            pre = jcast('int', cur)
            i = jcast('int', (i + 1))
        return jcast('int', pre)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


