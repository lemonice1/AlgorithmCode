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

# 被围绕的区域
# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域
# 并将这些区域里所有的 'O' 用 'X' 填充。
# 测试链接 : https://leetcode.cn/problems/surrounded-regions/
class Code02_SurroundedRegions:
    __java_fields__ = {}
    @staticmethod
    def solve(board):
        n = jcast('int', jget(board, 'length'))
        m = jcast('int', jget(board[0], 'length'))
        j = jcast('int', 0)
        while (j < m):
            if (board[0][j] == jchar('O')):
                Code02_SurroundedRegions.dfs(board, n, m, 0, j)
            if (board[jcast('int', (n - 1))][j] == jchar('O')):
                Code02_SurroundedRegions.dfs(board, n, m, jcast('int', (n - 1)), j)
            j = jcast('int', (j + 1))
        i = jcast('int', 1)
        while (i < jcast('int', (n - 1))):
            if (board[i][0] == jchar('O')):
                Code02_SurroundedRegions.dfs(board, n, m, i, 0)
            if (board[i][jcast('int', (m - 1))] == jchar('O')):
                Code02_SurroundedRegions.dfs(board, n, m, i, jcast('int', (m - 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                if (board[i][j] == jchar('O')):
                    jset(board[i], j, jchar('X'))
                if (board[i][j] == jchar('F')):
                    jset(board[i], j, jchar('O'))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def dfs(board, n, m, i, j):
        n = jcast('int', n)
        m = jcast('int', m)
        i = jcast('int', i)
        j = jcast('int', j)
        if (((((i < 0) or (i == n)) or (j < 0)) or (j == m)) or (board[i][j] != jchar('O'))):
            return
        jset(board[i], j, jchar('F'))
        Code02_SurroundedRegions.dfs(board, n, m, jcast('int', jadd(i, 1)), j)
        Code02_SurroundedRegions.dfs(board, n, m, jcast('int', (i - 1)), j)
        Code02_SurroundedRegions.dfs(board, n, m, i, jcast('int', jadd(j, 1)))
        Code02_SurroundedRegions.dfs(board, n, m, i, jcast('int', (j - 1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


