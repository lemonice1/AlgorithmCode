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

# 柱状图中最大的矩形
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度
# 每个柱子彼此相邻，且宽度为 1 。求在该柱状图中，能够勾勒出来的矩形的最大面积
# 测试链接：https://leetcode.cn/problems/largest-rectangle-in-histogram
class Code04_LargestRectangleInHistogram:
    __java_fields__ = {'MAXN': 'MAXN', 'stack': 'stack', 'r': 'r'}
    MAXN = 0
    stack = None
    r = 0
    @staticmethod
    def largestRectangleArea(height):
        n = jcast('int', jget(height, 'length'))
        Code04_LargestRectangleInHistogram.r = jcast('int', 0)
        ans = jcast('int', 0)
        cur = 0
        left = 0
        i = jcast('int', 0)
        while (i < n):
            # i -> arr[i]
            while ((Code04_LargestRectangleInHistogram.r > 0) and (height[Code04_LargestRectangleInHistogram.stack[jcast('int', (Code04_LargestRectangleInHistogram.r - 1))]] >= height[i])):
                cur = jcast('int', Code04_LargestRectangleInHistogram.stack[((_java_obj_1 := Code04_LargestRectangleInHistogram), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))))[3]])
                left = jcast('int', (jcast('int', (-1)) if (Code04_LargestRectangleInHistogram.r == 0) else Code04_LargestRectangleInHistogram.stack[jcast('int', (Code04_LargestRectangleInHistogram.r - 1))]))
                ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', (height[cur] * jcast('int', (jcast('int', (i - left)) - 1))))))
            jset(Code04_LargestRectangleInHistogram.stack, ((_java_obj_4 := Code04_LargestRectangleInHistogram), (_java_key_5 := 'r'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], i)
            i = jcast('int', (i + 1))
        while (Code04_LargestRectangleInHistogram.r > 0):
            cur = jcast('int', Code04_LargestRectangleInHistogram.stack[((_java_obj_7 := Code04_LargestRectangleInHistogram), (_java_key_8 := 'r'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))))[3]])
            left = jcast('int', (jcast('int', (-1)) if (Code04_LargestRectangleInHistogram.r == 0) else Code04_LargestRectangleInHistogram.stack[jcast('int', (Code04_LargestRectangleInHistogram.r - 1))]))
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', (height[cur] * jcast('int', (jcast('int', (n - left)) - 1))))))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_LargestRectangleInHistogram.MAXN = jcast('int', 100001)
Code04_LargestRectangleInHistogram.stack = jarray('int', [Code04_LargestRectangleInHistogram.MAXN])
Code04_LargestRectangleInHistogram.r = jcast('int', 0)
