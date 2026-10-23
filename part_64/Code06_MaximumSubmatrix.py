# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 子矩阵最大累加和问题
# 给定一个二维数组grid，找到其中子矩阵的最大累加和
# 返回拥有最大累加和的子矩阵左上角和右下角坐标
# 如果有多个子矩阵都有最大累加和，返回哪一个都可以
# 测试链接 : https://leetcode.cn/problems/max-submatrix-lcci/
class Code06_MaximumSubmatrix:
    __java_fields__ = {}
    # 如果行和列的规模都是n，时间复杂度O(n^3)，最优解了
    @staticmethod
    def getMaxMatrix(grid):
        n = jcast('int', jget(grid, 'length'))
        m = jcast('int', jget(grid[0], 'length'))
        max = jcast('int', jget(Integer, 'MIN_VALUE'))
        a = jcast('int', 0)
        b = jcast('int', 0)
        c = jcast('int', 0)
        d = jcast('int', 0)
        nums = jarray('int', [m])
        up = jcast('int', 0)
        while (up < n):
            jstatic('Arrays', 'fill', nums, 0)
            down = jcast('int', up)
            while (down < n):
                # 如下代码就是题目1的附加问题 :
                # 子数组中找到拥有最大累加和的子数组
                l = jcast('int', 0)
                r = jcast('int', 0)
                pre = jcast('int', jget(Integer, 'MIN_VALUE'))
                while (r < m):
                    nums[r] = jcast('int', jcast('int', jadd(nums[r], grid[down][r])))
                    if (pre >= 0):
                        pre = jcast('int', jcast('int', jadd(pre, nums[r])))
                    else:
                        pre = jcast('int', nums[r])
                        l = jcast('int', r)
                    if (pre > max):
                        max = jcast('int', pre)
                        a = jcast('int', up)
                        b = jcast('int', l)
                        c = jcast('int', down)
                        d = jcast('int', r)
                    r = jcast('int', (r + 1))
                down = jcast('int', (down + 1))
            up = jcast('int', (up + 1))
        return jarray('int', [None], [a, b, c, d])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


