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

# 最大人工岛
# 给你一个大小为 n * n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。
# 返回执行此操作后，grid 中最大的岛屿面积是多少？
# 岛屿 由一组上、下、左、右四个方向相连的 1 形成
# 测试链接 : https://leetcode.cn/problems/making-a-large-island/
class Code03_MakingLargeIsland:
    __java_fields__ = {}
    @staticmethod
    def largestIsland(grid):
        n = jcast('int', jget(grid, 'length'))
        m = jcast('int', jget(grid[0], 'length'))
        id = jcast('int', 2)
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                if (grid[i][j] == 1):
                    Code03_MakingLargeIsland.dfs(grid, n, m, i, j, ((_java_old_1 := id), (id := jcast('int', (id + (1)))), _java_old_1)[2])
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        sizes = jarray('int', [id])
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                if (grid[i][j] > 1):
                    ans = jcast('int', jstatic('Math', 'max', ans, ((_java_obj_2 := sizes), (_java_key_3 := grid[i][j]), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))))[3]))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        # 讨论所有的0，变成1，能带来的最大岛的大小
        visited = jarray('boolean', [id])
        up = 0
        down = 0
        left = 0
        right = 0
        merge = 0
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                if (grid[i][j] == 0):
                    up = jcast('int', (grid[jcast('int', (i - 1))][j] if (i > 0) else 0))
                    down = jcast('int', (grid[jcast('int', jadd(i, 1))][j] if (jcast('int', jadd(i, 1)) < n) else 0))
                    left = jcast('int', (grid[i][jcast('int', (j - 1))] if (j > 0) else 0))
                    right = jcast('int', (grid[i][jcast('int', jadd(j, 1))] if (jcast('int', jadd(j, 1)) < m) else 0))
                    visited[up] = jcast('boolean', True)
                    merge = jcast('int', jcast('int', jadd(1, sizes[up])))
                    if (not visited[down]):
                        merge = jcast('int', jcast('int', jadd(merge, sizes[down])))
                        visited[down] = jcast('boolean', True)
                    if (not visited[left]):
                        merge = jcast('int', jcast('int', jadd(merge, sizes[left])))
                        visited[left] = jcast('boolean', True)
                    if (not visited[right]):
                        merge = jcast('int', jcast('int', jadd(merge, sizes[right])))
                        visited[right] = jcast('boolean', True)
                    ans = jcast('int', jstatic('Math', 'max', ans, merge))
                    visited[up] = jcast('boolean', False)
                    visited[down] = jcast('boolean', False)
                    visited[left] = jcast('boolean', False)
                    visited[right] = jcast('boolean', False)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def dfs(grid, n, m, i, j, id):
        n = jcast('int', n)
        m = jcast('int', m)
        i = jcast('int', i)
        j = jcast('int', j)
        id = jcast('int', id)
        if (((((i < 0) or (i == n)) or (j < 0)) or (j == m)) or (grid[i][j] != 1)):
            return
        # grid[i][j] == 1
        jset(grid[i], j, id)
        Code03_MakingLargeIsland.dfs(grid, n, m, jcast('int', (i - 1)), j, id)
        Code03_MakingLargeIsland.dfs(grid, n, m, jcast('int', jadd(i, 1)), j, id)
        Code03_MakingLargeIsland.dfs(grid, n, m, i, jcast('int', (j - 1)), id)
        Code03_MakingLargeIsland.dfs(grid, n, m, i, jcast('int', jadd(j, 1)), id)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


