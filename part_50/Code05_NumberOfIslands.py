# -*- coding: utf-8 -*-
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
class Code05_NumberOfIslands:
    __java_fields__ = {'MAXSIZE': 'MAXSIZE', 'father': 'father', 'cols': 'cols', 'sets': 'sets'}
    # 并查集的做法
    @staticmethod
    def numIslands(board):
        n = jcast('int', jget(board, 'length'))
        m = jcast('int', jget(board[0], 'length'))
        Code05_NumberOfIslands.build(n, m, board)
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                if (board[i][j] == jchar('1')):
                    if ((j > 0) and (board[i][jcast('int', (j - 1))] == jchar('1'))):
                        Code05_NumberOfIslands.union(i, j, i, jcast('int', (j - 1)))
                    if ((i > 0) and (board[jcast('int', (i - 1))][j] == jchar('1'))):
                        Code05_NumberOfIslands.union(i, j, jcast('int', (i - 1)), j)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code05_NumberOfIslands.sets)

    MAXSIZE = 0
    father = None
    cols = 0
    sets = 0
    @staticmethod
    def build(n, m, board):
        n = jcast('int', n)
        m = jcast('int', m)
        Code05_NumberOfIslands.cols = jcast('int', m)
        Code05_NumberOfIslands.sets = jcast('int', 0)
        a = jcast('int', 0)
        while (a < n):
            b = jcast('int', 0)
            index = 0
            while (b < m):
                if (board[a][b] == jchar('1')):
                    index = jcast('int', Code05_NumberOfIslands.index(a, b))
                    Code05_NumberOfIslands.father[index] = jcast('int', index)
                    Code05_NumberOfIslands.sets = jcast('int', (Code05_NumberOfIslands.sets + 1))
                b = jcast('int', (b + 1))
            a = jcast('int', (a + 1))

    @staticmethod
    def index(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        return jcast('int', jcast('int', jadd(jcast('int', (a * Code05_NumberOfIslands.cols)), b)))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code05_NumberOfIslands.father[i]):
            jset(Code05_NumberOfIslands.father, i, Code05_NumberOfIslands.find(Code05_NumberOfIslands.father[i]))
        return jcast('int', Code05_NumberOfIslands.father[i])

    @staticmethod
    def union(a, b, c, d):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        fx = jcast('int', Code05_NumberOfIslands.find(Code05_NumberOfIslands.index(a, b)))
        fy = jcast('int', Code05_NumberOfIslands.find(Code05_NumberOfIslands.index(c, d)))
        if (fx != fy):
            Code05_NumberOfIslands.father[fx] = jcast('int', fy)
            Code05_NumberOfIslands.sets = jcast('int', (Code05_NumberOfIslands.sets - 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_NumberOfIslands.MAXSIZE = jcast('int', 100001)
Code05_NumberOfIslands.father = jarray('int', [Code05_NumberOfIslands.MAXSIZE])
Code05_NumberOfIslands.cols = jcast('int', 0)
Code05_NumberOfIslands.sets = jcast('int', 0)
