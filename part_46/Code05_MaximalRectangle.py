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

# 最大矩形
# 给定一个仅包含 0 和 1 、大小为 rows * cols 的二维二进制矩阵
# 找出只包含 1 的最大矩形，并返回其面积
# 测试链接：https://leetcode.cn/problems/maximal-rectangle/
class Code05_MaximalRectangle:
    __java_fields__ = {'MAXN': 'MAXN', 'height': 'height', 'stack': 'stack', 'r': 'r'}
    MAXN = 0
    height = None
    stack = None
    r = 0
    @staticmethod
    def maximalRectangle(grid):
        n = jcast('int', jget(grid, 'length'))
        m = jcast('int', jget(grid[0], 'length'))
        jstatic('Arrays', 'fill', Code05_MaximalRectangle.height, 0, m, 0)
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            # 来到i行，长方形一定要以i行做底！
            # 加工高度数组(压缩数组)
            j = jcast('int', 0)
            while (j < m):
                Code05_MaximalRectangle.height[j] = jcast('int', (0 if (grid[i][j] == jchar('0')) else jcast('int', jadd(Code05_MaximalRectangle.height[j], 1))))
                j = jcast('int', (j + 1))
            ans = jcast('int', jstatic('Math', 'max', Code05_MaximalRectangle.largestRectangleArea(m), ans))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def largestRectangleArea(m):
        m = jcast('int', m)
        Code05_MaximalRectangle.r = jcast('int', 0)
        ans = jcast('int', 0)
        cur = 0
        left = 0
        i = jcast('int', 0)
        while (i < m):
            # i -> arr[i]
            while ((Code05_MaximalRectangle.r > 0) and (Code05_MaximalRectangle.height[Code05_MaximalRectangle.stack[jcast('int', (Code05_MaximalRectangle.r - 1))]] >= Code05_MaximalRectangle.height[i])):
                cur = jcast('int', Code05_MaximalRectangle.stack[((_java_obj_1 := Code05_MaximalRectangle), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))))[3]])
                left = jcast('int', (jcast('int', (-1)) if (Code05_MaximalRectangle.r == 0) else Code05_MaximalRectangle.stack[jcast('int', (Code05_MaximalRectangle.r - 1))]))
                ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', (Code05_MaximalRectangle.height[cur] * jcast('int', (jcast('int', (i - left)) - 1))))))
            jset(Code05_MaximalRectangle.stack, ((_java_obj_4 := Code05_MaximalRectangle), (_java_key_5 := 'r'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], i)
            i = jcast('int', (i + 1))
        while (Code05_MaximalRectangle.r > 0):
            cur = jcast('int', Code05_MaximalRectangle.stack[((_java_obj_7 := Code05_MaximalRectangle), (_java_key_8 := 'r'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))))[3]])
            left = jcast('int', (jcast('int', (-1)) if (Code05_MaximalRectangle.r == 0) else Code05_MaximalRectangle.stack[jcast('int', (Code05_MaximalRectangle.r - 1))]))
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', (Code05_MaximalRectangle.height[cur] * jcast('int', (jcast('int', (m - left)) - 1))))))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_MaximalRectangle.MAXN = jcast('int', 201)
Code05_MaximalRectangle.height = jarray('int', [Code05_MaximalRectangle.MAXN])
Code05_MaximalRectangle.stack = jarray('int', [Code05_MaximalRectangle.MAXN])
Code05_MaximalRectangle.r = jcast('int', 0)
