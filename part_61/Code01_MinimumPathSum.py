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

# 最小路径和
# 给定一个包含非负整数的 m x n 网格 grid
# 请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。
# 测试链接 : https://leetcode.cn/problems/minimum-path-sum/
class Code01_MinimumPathSum:
    __java_fields__ = {}
    # 暴力递归
    @staticmethod
    def minPathSum1(grid):
        return jcast('int', Code01_MinimumPathSum.f1(grid, jcast('int', (jget(grid, 'length') - 1)), jcast('int', (jget(grid[0], 'length') - 1))))

    # 从(0,0)到(i,j)最小路径和
    # 一定每次只能向右或者向下
    @staticmethod
    def f1(grid, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if ((i == 0) and (j == 0)):
            return jcast('int', grid[0][0])
        up = jcast('int', jget(Integer, 'MAX_VALUE'))
        left = jcast('int', jget(Integer, 'MAX_VALUE'))
        if (jcast('int', (i - 1)) >= 0):
            up = jcast('int', Code01_MinimumPathSum.f1(grid, jcast('int', (i - 1)), j))
        if (jcast('int', (j - 1)) >= 0):
            left = jcast('int', Code01_MinimumPathSum.f1(grid, i, jcast('int', (j - 1))))
        return jcast('int', jcast('int', jadd(grid[i][j], jstatic('Math', 'min', up, left))))

    # 记忆化搜索
    @staticmethod
    def minPathSum2(grid):
        n = jcast('int', jget(grid, 'length'))
        m = jcast('int', jget(grid[0], 'length'))
        dp = jarray('int', [n, m])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                jset(dp[i], j, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code01_MinimumPathSum.f2(grid, jcast('int', (jget(grid, 'length') - 1)), jcast('int', (jget(grid[0], 'length') - 1)), dp))

    @staticmethod
    def f2(grid, i, j, dp):
        i = jcast('int', i)
        j = jcast('int', j)
        if (dp[i][j] != jcast('int', (-1))):
            return jcast('int', dp[i][j])
        ans = 0
        if ((i == 0) and (j == 0)):
            ans = jcast('int', grid[0][0])
        else:
            up = jcast('int', jget(Integer, 'MAX_VALUE'))
            left = jcast('int', jget(Integer, 'MAX_VALUE'))
            if (jcast('int', (i - 1)) >= 0):
                up = jcast('int', Code01_MinimumPathSum.f2(grid, jcast('int', (i - 1)), j, dp))
            if (jcast('int', (j - 1)) >= 0):
                left = jcast('int', Code01_MinimumPathSum.f2(grid, i, jcast('int', (j - 1)), dp))
            ans = jcast('int', jcast('int', jadd(grid[i][j], jstatic('Math', 'min', up, left))))
        jset(dp[i], j, ans)
        return jcast('int', ans)

    # 严格位置依赖的动态规划
    @staticmethod
    def minPathSum3(grid):
        n = jcast('int', jget(grid, 'length'))
        m = jcast('int', jget(grid[0], 'length'))
        dp = jarray('int', [n, m])
        jset(dp[0], 0, grid[0][0])
        i = jcast('int', 1)
        while (i < n):
            jset(dp[i], 0, jcast('int', jadd(dp[jcast('int', (i - 1))][0], grid[i][0])))
            i = jcast('int', (i + 1))
        j = jcast('int', 1)
        while (j < m):
            jset(dp[0], j, jcast('int', jadd(dp[0][jcast('int', (j - 1))], grid[0][j])))
            j = jcast('int', (j + 1))
        i = jcast('int', 1)
        while (i < n):
            j = jcast('int', 1)
            while (j < m):
                jset(dp[i], j, jcast('int', jadd(jstatic('Math', 'min', dp[jcast('int', (i - 1))][j], dp[i][jcast('int', (j - 1))]), grid[i][j])))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[jcast('int', (n - 1))][jcast('int', (m - 1))])

    # 严格位置依赖的动态规划 + 空间压缩技巧
    @staticmethod
    def minPathSum4(grid):
        n = jcast('int', jget(grid, 'length'))
        m = jcast('int', jget(grid[0], 'length'))
        # 先让dp表，变成想象中的表的第0行的数据
        dp = jarray('int', [m])
        dp[0] = jcast('int', grid[0][0])
        j = jcast('int', 1)
        while (j < m):
            dp[j] = jcast('int', jcast('int', jadd(dp[jcast('int', (j - 1))], grid[0][j])))
            j = jcast('int', (j + 1))
        i = jcast('int', 1)
        while (i < n):
            # i = 1，dp表变成想象中二维表的第1行的数据
            # i = 2，dp表变成想象中二维表的第2行的数据
            # i = 3，dp表变成想象中二维表的第3行的数据
            # ...
            # i = n-1，dp表变成想象中二维表的第n-1行的数据
            dp[0] = jcast('int', jcast('int', jadd(dp[0], grid[i][0])))
            j = jcast('int', 1)
            while (j < m):
                jset(dp, j, jcast('int', jadd(jstatic('Math', 'min', dp[jcast('int', (j - 1))], dp[j]), grid[i][j])))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[jcast('int', (m - 1))])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


