# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 矩阵中和能被 K 整除的路径
# 给一个下标从0开始的 n * m 整数矩阵 grid 和一个整数 k
# 从起点(0,0)出发，每步只能往下或者往右，你想要到达终点(m-1, n-1)
# 请你返回路径和能被 k 整除的路径数目
# 答案对 1000000007 取模
# 测试链接 : https://leetcode.cn/problems/paths-in-matrix-whose-sum-is-divisible-by-k/
class Code04_PathsDivisibleByK:
    __java_fields__ = {'mod': 'mod'}
    mod = 0
    @staticmethod
    def numberOfPaths1(grid, k):
        k = jcast('int', k)
        n = jcast('int', jget(grid, 'length'))
        m = jcast('int', jget(grid[0], 'length'))
        return jcast('int', Code04_PathsDivisibleByK.f1(grid, n, m, k, 0, 0, 0))

    # 当前来到(i,j)位置，最终一定要走到右下角(n-1,m-1)
    # 从(i,j)出发，最终一定要走到右下角(n-1,m-1)，有多少条路径，累加和%k的余数是r
    @staticmethod
    def f1(grid, n, m, k, i, j, r):
        n = jcast('int', n)
        m = jcast('int', m)
        k = jcast('int', k)
        i = jcast('int', i)
        j = jcast('int', j)
        r = jcast('int', r)
        if ((i == jcast('int', (n - 1))) and (j == jcast('int', (m - 1)))):
            return jcast('int', (1 if (jcast('int', jmod(grid[i][j], k)) == r) else 0))
        # 后续需要凑出来的余数need
        need = jcast('int', jcast('int', jmod(jcast('int', (jcast('int', jadd(k, r)) - jcast('int', jmod(grid[i][j], k)))), k)))
        ans = jcast('int', 0)
        if (jcast('int', jadd(i, 1)) < n):
            ans = jcast('int', Code04_PathsDivisibleByK.f1(grid, n, m, k, jcast('int', jadd(i, 1)), j, need))
        if (jcast('int', jadd(j, 1)) < m):
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code04_PathsDivisibleByK.f1(grid, n, m, k, i, jcast('int', jadd(j, 1)), need))), Code04_PathsDivisibleByK.mod)))
        return jcast('int', ans)

    @staticmethod
    def numberOfPaths2(grid, k):
        k = jcast('int', k)
        n = jcast('int', jget(grid, 'length'))
        m = jcast('int', jget(grid[0], 'length'))
        dp = jarray('int', [n, m, k])
        a = jcast('int', 0)
        while (a < n):
            b = jcast('int', 0)
            while (b < m):
                c = jcast('int', 0)
                while (c < k):
                    jset(dp[a][b], c, jcast('int', (-1)))
                    c = jcast('int', (c + 1))
                b = jcast('int', (b + 1))
            a = jcast('int', (a + 1))
        return jcast('int', Code04_PathsDivisibleByK.f2(grid, n, m, k, 0, 0, 0, dp))

    @staticmethod
    def f2(grid, n, m, k, i, j, r, dp):
        n = jcast('int', n)
        m = jcast('int', m)
        k = jcast('int', k)
        i = jcast('int', i)
        j = jcast('int', j)
        r = jcast('int', r)
        if ((i == jcast('int', (n - 1))) and (j == jcast('int', (m - 1)))):
            return jcast('int', (1 if (jcast('int', jmod(grid[i][j], k)) == r) else 0))
        if (dp[i][j][r] != jcast('int', (-1))):
            return jcast('int', dp[i][j][r])
        need = jcast('int', jcast('int', jmod(jcast('int', (jcast('int', jadd(k, r)) - jcast('int', jmod(grid[i][j], k)))), k)))
        ans = jcast('int', 0)
        if (jcast('int', jadd(i, 1)) < n):
            ans = jcast('int', Code04_PathsDivisibleByK.f2(grid, n, m, k, jcast('int', jadd(i, 1)), j, need, dp))
        if (jcast('int', jadd(j, 1)) < m):
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code04_PathsDivisibleByK.f2(grid, n, m, k, i, jcast('int', jadd(j, 1)), need, dp))), Code04_PathsDivisibleByK.mod)))
        jset(dp[i][j], r, ans)
        return jcast('int', ans)

    @staticmethod
    def numberOfPaths3(grid, k):
        k = jcast('int', k)
        n = jcast('int', jget(grid, 'length'))
        m = jcast('int', jget(grid[0], 'length'))
        dp = jarray('int', [n, m, k])
        jset(dp[jcast('int', (n - 1))][jcast('int', (m - 1))], jcast('int', jmod(grid[jcast('int', (n - 1))][jcast('int', (m - 1))], k)), 1)
        i = jcast('int', jcast('int', (n - 2)))
        while (i >= 0):
            r = jcast('int', 0)
            while (r < k):
                jset(dp[i][jcast('int', (m - 1))], r, dp[jcast('int', jadd(i, 1))][jcast('int', (m - 1))][jcast('int', jmod(jcast('int', (jcast('int', jadd(k, r)) - jcast('int', jmod(grid[i][jcast('int', (m - 1))], k)))), k))])
                r = jcast('int', (r + 1))
            i = jcast('int', (i - 1))
        j = jcast('int', jcast('int', (m - 2)))
        while (j >= 0):
            r = jcast('int', 0)
            while (r < k):
                jset(dp[jcast('int', (n - 1))][j], r, dp[jcast('int', (n - 1))][jcast('int', jadd(j, 1))][jcast('int', jmod(jcast('int', (jcast('int', jadd(k, r)) - jcast('int', jmod(grid[jcast('int', (n - 1))][j], k)))), k))])
                r = jcast('int', (r + 1))
            j = jcast('int', (j - 1))
        i = jcast('int', jcast('int', (n - 2)))
        need = 0
        while (i >= 0):
            j = jcast('int', jcast('int', (m - 2)))
            while (j >= 0):
                r = jcast('int', 0)
                while (r < k):
                    need = jcast('int', jcast('int', jmod(jcast('int', (jcast('int', jadd(k, r)) - jcast('int', jmod(grid[i][j], k)))), k)))
                    jset(dp[i][j], r, dp[jcast('int', jadd(i, 1))][j][need])
                    jset(dp[i][j], r, jcast('int', jmod(jcast('int', jadd(dp[i][j][r], dp[i][jcast('int', jadd(j, 1))][need])), Code04_PathsDivisibleByK.mod)))
                    r = jcast('int', (r + 1))
                j = jcast('int', (j - 1))
            i = jcast('int', (i - 1))
        return jcast('int', dp[0][0][0])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_PathsDivisibleByK.mod = jcast('int', 1000000007)
