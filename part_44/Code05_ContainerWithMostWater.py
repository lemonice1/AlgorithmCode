# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 盛最多水的容器
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水
# 返回容器可以储存的最大水量
# 说明：你不能倾斜容器
# 测试链接 : https://leetcode.cn/problems/container-with-most-water/
class Code05_ContainerWithMostWater:
    __java_fields__ = {}
    # 时间复杂度O(n)，额外空间复杂度O(1)
    @staticmethod
    def maxArea(height):
        ans = jcast('int', 0)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (jget(height, 'length') - 1)))
        while (l < r):
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', (jstatic('Math', 'min', height[l], height[r]) * jcast('int', (r - l))))))
            if (height[l] <= height[r]):
                l = jcast('int', (l + 1))
            else:
                r = jcast('int', (r - 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


