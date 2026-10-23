# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 矩阵中的最长递增路径
# 给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度
# 对于每个单元格，你可以往上，下，左，右四个方向移动
# 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）
# 测试链接 : https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/
class Code06_LongestIncreasingPath:
    __java_fields__ = {}
    @staticmethod
    def longestIncreasingPath1(grid):
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < jget(grid, 'length')):
            j = jcast('int', 0)
            while (j < jget(grid[0], 'length')):
                ans = jcast('int', jstatic('Math', 'max', ans, Code06_LongestIncreasingPath.f1(grid, i, j)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 从(i,j)出发，能走出来多长的递增路径，返回最长长度
    @staticmethod
    def f1(grid, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        next = jcast('int', 0)
        if ((i > 0) and (grid[i][j] < grid[jcast('int', (i - 1))][j])):
            next = jcast('int', jstatic('Math', 'max', next, Code06_LongestIncreasingPath.f1(grid, jcast('int', (i - 1)), j)))
        if ((jcast('int', jadd(i, 1)) < jget(grid, 'length')) and (grid[i][j] < grid[jcast('int', jadd(i, 1))][j])):
            next = jcast('int', jstatic('Math', 'max', next, Code06_LongestIncreasingPath.f1(grid, jcast('int', jadd(i, 1)), j)))
        if ((j > 0) and (grid[i][j] < grid[i][jcast('int', (j - 1))])):
            next = jcast('int', jstatic('Math', 'max', next, Code06_LongestIncreasingPath.f1(grid, i, jcast('int', (j - 1)))))
        if ((jcast('int', jadd(j, 1)) < jget(grid[0], 'length')) and (grid[i][j] < grid[i][jcast('int', jadd(j, 1))])):
            next = jcast('int', jstatic('Math', 'max', next, Code06_LongestIncreasingPath.f1(grid, i, jcast('int', jadd(j, 1)))))
        return jcast('int', jcast('int', jadd(next, 1)))

    @staticmethod
    def longestIncreasingPath2(grid):
        n = jcast('int', jget(grid, 'length'))
        m = jcast('int', jget(grid[0], 'length'))
        dp = jarray('int', [n, m])
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                ans = jcast('int', jstatic('Math', 'max', ans, Code06_LongestIncreasingPath.f2(grid, i, j, dp)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def f2(grid, i, j, dp):
        i = jcast('int', i)
        j = jcast('int', j)
        if (dp[i][j] != 0):
            return jcast('int', dp[i][j])
        next = jcast('int', 0)
        if ((i > 0) and (grid[i][j] < grid[jcast('int', (i - 1))][j])):
            next = jcast('int', jstatic('Math', 'max', next, Code06_LongestIncreasingPath.f2(grid, jcast('int', (i - 1)), j, dp)))
        if ((jcast('int', jadd(i, 1)) < jget(grid, 'length')) and (grid[i][j] < grid[jcast('int', jadd(i, 1))][j])):
            next = jcast('int', jstatic('Math', 'max', next, Code06_LongestIncreasingPath.f2(grid, jcast('int', jadd(i, 1)), j, dp)))
        if ((j > 0) and (grid[i][j] < grid[i][jcast('int', (j - 1))])):
            next = jcast('int', jstatic('Math', 'max', next, Code06_LongestIncreasingPath.f2(grid, i, jcast('int', (j - 1)), dp)))
        if ((jcast('int', jadd(j, 1)) < jget(grid[0], 'length')) and (grid[i][j] < grid[i][jcast('int', jadd(j, 1))])):
            next = jcast('int', jstatic('Math', 'max', next, Code06_LongestIncreasingPath.f2(grid, i, jcast('int', jadd(j, 1)), dp)))
        jset(dp[i], j, jcast('int', jadd(next, 1)))
        return jcast('int', jcast('int', jadd(next, 1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


