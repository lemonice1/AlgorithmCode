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

# 岛屿数量
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成
# 此外，你可以假设该网格的四条边均被水包围
# 测试链接 : https://leetcode.cn/problems/number-of-islands/
class Code01_NumberOfIslands:
    __java_fields__ = {}
    # 洪水填充的做法
    # board : n * m
    # O(n*m)最优解！
    @staticmethod
    def numIslands(board):
        n = jcast('int', jget(board, 'length'))
        m = jcast('int', jget(board[0], 'length'))
        islands = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                if (board[i][j] == jchar('1')):
                    islands = jcast('int', (islands + 1))
                    Code01_NumberOfIslands.dfs(board, n, m, i, j)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', islands)

    @staticmethod
    def dfs(board, n, m, i, j):
        n = jcast('int', n)
        m = jcast('int', m)
        i = jcast('int', i)
        j = jcast('int', j)
        if (((((i < 0) or (i == n)) or (j < 0)) or (j == m)) or (board[i][j] != jchar('1'))):
            return
        # board[i][j] = '1'
        jset(board[i], j, 0)
        Code01_NumberOfIslands.dfs(board, n, m, jcast('int', (i - 1)), j)
        Code01_NumberOfIslands.dfs(board, n, m, jcast('int', jadd(i, 1)), j)
        Code01_NumberOfIslands.dfs(board, n, m, i, jcast('int', (j - 1)))
        Code01_NumberOfIslands.dfs(board, n, m, i, jcast('int', jadd(j, 1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


