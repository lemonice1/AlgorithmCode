# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 使网格图至少有一条有效路径的最小代价
# 给你一个 m * n 的网格图 grid 。 grid 中每个格子都有一个数字
# 对应着从该格子出发下一步走的方向。 grid[i][j] 中的数字可能为以下几种情况：
# 1 ，下一步往右走，也就是你会从 grid[i][j] 走到 grid[i][j + 1]
# 2 ，下一步往左走，也就是你会从 grid[i][j] 走到 grid[i][j - 1]
# 3 ，下一步往下走，也就是你会从 grid[i][j] 走到 grid[i + 1][j]
# 4 ，下一步往上走，也就是你会从 grid[i][j] 走到 grid[i - 1][j]
# 注意网格图中可能会有 无效数字 ，因为它们可能指向 grid 以外的区域
# 一开始，你会从最左上角的格子 (0,0) 出发
# 我们定义一条 有效路径 为从格子 (0,0) 出发，每一步都顺着数字对应方向走
# 最终在最右下角的格子 (m - 1, n - 1) 结束的路径
# 有效路径 不需要是最短路径
# 你可以花费1的代价修改一个格子中的数字，但每个格子中的数字 只能修改一次
# 请你返回让网格图至少有一条有效路径的最小代价
# 测试链接 : https://leetcode.cn/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
class Code04_MinimumCostToMakeAtLeastOneValidPath:
    __java_fields__ = {}
    @staticmethod
    def minCost(grid):
        # 格子的数值 :
        # 1 右
        # 2 左
        # 3 下
        # 4 上
        # 0      1         2          3         4
        move = jarray('int', [None, None], [[], [0, 1], [0, jcast('int', (-1))], [1, 0], [jcast('int', (-1)), 0]])
        m = jcast('int', jget(grid, 'length'))
        n = jcast('int', jget(grid[0], 'length'))
        distance = jarray('int', [m, n])
        i = jcast('int', 0)
        while (i < m):
            j = jcast('int', 0)
            while (j < n):
                jset(distance[i], j, jget(Integer, 'MAX_VALUE'))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        q = jnew('ArrayDeque')
        jcall(q, 'addFirst', jarray('int', [None], [0, 0]))
        jset(distance[0], 0, 0)
        while (not jcall(q, 'isEmpty')):
            record = jcall(q, 'pollFirst')
            x = jcast('int', record[0])
            y = jcast('int', record[1])
            if ((x == jcast('int', (m - 1))) and (y == jcast('int', (n - 1)))):
                return jcast('int', distance[x][y])
            i = jcast('int', 1)
            while (i <= 4):
                nx = jcast('int', jcast('int', jadd(x, move[i][0])))
                ny = jcast('int', jcast('int', jadd(y, move[i][1])))
                weight = jcast('int', (1 if (grid[x][y] != i) else 0))
                if (((((nx >= 0) and (nx < m)) and (ny >= 0)) and (ny < n)) and (jcast('int', jadd(distance[x][y], weight)) < distance[nx][ny])):
                    jset(distance[nx], ny, jcast('int', jadd(distance[x][y], weight)))
                    if (weight == 0):
                        jcall(q, 'offerFirst', jarray('int', [None], [nx, ny]))
                    else:
                        jcall(q, 'offerLast', jarray('int', [None], [nx, ny]))
                i = jcast('int', (i + 1))
        return jcast('int', jcast('int', (-1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


