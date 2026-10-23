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

# 骑士在棋盘上的概率
# n * n的国际象棋棋盘上，一个骑士从单元格(row, col)开始，并尝试进行 k 次移动
# 行和列从0开始，所以左上单元格是 (0,0)，右下单元格是 (n-1, n-1)
# 象棋骑士有8种可能的走法。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格
# 每次骑士要移动时，它都会随机从8种可能的移动中选择一种，然后移动到那里
# 骑士继续移动，直到它走了 k 步或离开了棋盘
# 返回 骑士在棋盘停止移动后仍留在棋盘上的概率
# 测试链接 : https://leetcode.cn/problems/knight-probability-in-chessboard/
class Code03_KnightProbabilityInChessboard:
    __java_fields__ = {}
    @staticmethod
    def knightProbability(n, k, row, col):
        n = jcast('int', n)
        k = jcast('int', k)
        row = jcast('int', row)
        col = jcast('int', col)
        dp = jarray('double', [n, n, jcast('int', jadd(k, 1))])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < n):
                t = jcast('int', 0)
                while (t <= k):
                    jset(dp[i][j], t, jcast('int', (-1)))
                    t = jcast('int', (t + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('double', Code03_KnightProbabilityInChessboard.f(n, row, col, k, dp))

    # 从(i,j)出发还有k步要走，返回最后在棋盘上的概率
    @staticmethod
    def f(n, i, j, k, dp):
        n = jcast('int', n)
        i = jcast('int', i)
        j = jcast('int', j)
        k = jcast('int', k)
        if ((((i < 0) or (i >= n)) or (j < 0)) or (j >= n)):
            return jcast('double', 0)
        if (dp[i][j][k] != jcast('int', (-1))):
            return jcast('double', dp[i][j][k])
        ans = jcast('double', 0)
        if (k == 0):
            ans = jcast('double', 1)
        else:
            ans = jcast('double', jadd(ans, jdiv(Code03_KnightProbabilityInChessboard.f(n, jcast('int', (i - 2)), jcast('int', jadd(j, 1)), jcast('int', (k - 1)), dp), 8)))
            ans = jcast('double', jadd(ans, jdiv(Code03_KnightProbabilityInChessboard.f(n, jcast('int', (i - 1)), jcast('int', jadd(j, 2)), jcast('int', (k - 1)), dp), 8)))
            ans = jcast('double', jadd(ans, jdiv(Code03_KnightProbabilityInChessboard.f(n, jcast('int', jadd(i, 1)), jcast('int', jadd(j, 2)), jcast('int', (k - 1)), dp), 8)))
            ans = jcast('double', jadd(ans, jdiv(Code03_KnightProbabilityInChessboard.f(n, jcast('int', jadd(i, 2)), jcast('int', jadd(j, 1)), jcast('int', (k - 1)), dp), 8)))
            ans = jcast('double', jadd(ans, jdiv(Code03_KnightProbabilityInChessboard.f(n, jcast('int', jadd(i, 2)), jcast('int', (j - 1)), jcast('int', (k - 1)), dp), 8)))
            ans = jcast('double', jadd(ans, jdiv(Code03_KnightProbabilityInChessboard.f(n, jcast('int', jadd(i, 1)), jcast('int', (j - 2)), jcast('int', (k - 1)), dp), 8)))
            ans = jcast('double', jadd(ans, jdiv(Code03_KnightProbabilityInChessboard.f(n, jcast('int', (i - 1)), jcast('int', (j - 2)), jcast('int', (k - 1)), dp), 8)))
            ans = jcast('double', jadd(ans, jdiv(Code03_KnightProbabilityInChessboard.f(n, jcast('int', (i - 2)), jcast('int', (j - 1)), jcast('int', (k - 1)), dp), 8)))
        jset(dp[i][j], k, ans)
        return jcast('double', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


