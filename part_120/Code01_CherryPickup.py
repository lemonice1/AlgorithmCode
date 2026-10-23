# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 摘樱桃
# 给定一个n*n的正方形矩阵grid，每个格子值只有三种-1、0、1
# -1表示格子不能走、0表示格子可以走但是没有樱桃、1表示格子可以走且有一颗樱桃
# 你的目标是从左上角走到右下角，每一步只能 向下 或者 向右
# 然后从右下角走回左上角，每一步只能 向上 或者 向左
# 这个过程中，想尽量多的获得樱桃，但是有樱桃的格子，只能捡一次
# 返回最多能获得多少樱桃，如果不存在通路返回0
# 测试链接 : https://leetcode.cn/problems/cherry-pickup/
# 这里只讲述核心思路
# 有兴趣同学自己改出严格位置依赖的动态规划
# 有兴趣同学自己改出空间压缩版本的动态规划
# 之前的课大量涉及，这里不再赘述
class Code01_CherryPickup:
    __java_fields__ = {}
    @staticmethod
    def cherryPickup(grid):
        n = jcast('int', jget(grid, 'length'))
        dp = jarray('int', [n, n, n])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < n):
                k = jcast('int', 0)
                while (k < n):
                    jset(dp[i][j], k, jcast('int', (-2)))
                    k = jcast('int', (k + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', Code01_CherryPickup.f(grid, n, 0, 0, 0, dp))
        return jcast('int', (0 if (ans == jcast('int', (-1))) else ans))

    @staticmethod
    def f(grid, n, a, b, c, dp):
        n = jcast('int', n)
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', jcast('int', (jcast('int', jadd(a, b)) - c)))
        if ((((((a == n) or (b == n)) or (c == n)) or (d == n)) or (grid[a][b] == jcast('int', (-1)))) or (grid[c][d] == jcast('int', (-1)))):
            return jcast('int', jcast('int', (-1)))
        if ((a == jcast('int', (n - 1))) and (b == jcast('int', (n - 1)))):
            return jcast('int', grid[a][b])
        if (dp[a][b][c] != jcast('int', (-2))):
            return jcast('int', dp[a][b][c])
        get = jcast('int', (grid[a][b] if ((a == c) and (b == d)) else jcast('int', jadd(grid[a][b], grid[c][d]))))
        next = jcast('int', Code01_CherryPickup.f(grid, n, jcast('int', jadd(a, 1)), b, jcast('int', jadd(c, 1)), dp))
        next = jcast('int', jstatic('Math', 'max', next, Code01_CherryPickup.f(grid, n, jcast('int', jadd(a, 1)), b, c, dp)))
        next = jcast('int', jstatic('Math', 'max', next, Code01_CherryPickup.f(grid, n, a, jcast('int', jadd(b, 1)), jcast('int', jadd(c, 1)), dp)))
        next = jcast('int', jstatic('Math', 'max', next, Code01_CherryPickup.f(grid, n, a, jcast('int', jadd(b, 1)), c, dp)))
        ans = jcast('int', jcast('int', (-1)))
        if (next != jcast('int', (-1))):
            ans = jcast('int', jcast('int', jadd(get, next)))
        jset(dp[a][b], c, ans)
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


