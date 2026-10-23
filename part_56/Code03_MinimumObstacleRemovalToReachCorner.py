# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 到达角落需要移除障碍物的最小数目
# 给你一个下标从 0 开始的二维整数数组 grid ，数组大小为 m x n
# 每个单元格都是两个值之一：
# 0 表示一个 空 单元格，
# 1 表示一个可以移除的 障碍物
# 你可以向上、下、左、右移动，从一个空单元格移动到另一个空单元格。
# 现在你需要从左上角 (0, 0) 移动到右下角 (m - 1, n - 1)
# 返回需要移除的障碍物的最小数目
# 测试链接 : https://leetcode.cn/problems/minimum-obstacle-removal-to-reach-corner/
class Code03_MinimumObstacleRemovalToReachCorner:
    __java_fields__ = {}
    @staticmethod
    def minimumObstacles(grid):
        move = jarray('int', [None], [jcast('int', (-1)), 0, 1, 0, jcast('int', (-1))])
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
        deque = jnew('ArrayDeque')
        jcall(deque, 'addFirst', jarray('int', [None], [0, 0]))
        jset(distance[0], 0, 0)
        while (not jcall(deque, 'isEmpty')):
            record = jcall(deque, 'pollFirst')
            x = jcast('int', record[0])
            y = jcast('int', record[1])
            if ((x == jcast('int', (m - 1))) and (y == jcast('int', (n - 1)))):
                return jcast('int', distance[x][y])
            i = jcast('int', 0)
            while (i < 4):
                nx = jcast('int', jcast('int', jadd(x, move[i])))
                ny = jcast('int', jcast('int', jadd(y, move[jcast('int', jadd(i, 1))])))
                if (((((nx >= 0) and (nx < m)) and (ny >= 0)) and (ny < n)) and (jcast('int', jadd(distance[x][y], grid[nx][ny])) < distance[nx][ny])):
                    jset(distance[nx], ny, jcast('int', jadd(distance[x][y], grid[nx][ny])))
                    if (grid[nx][ny] == 0):
                        jcall(deque, 'addFirst', jarray('int', [None], [nx, ny]))
                    else:
                        jcall(deque, 'addLast', jarray('int', [None], [nx, ny]))
                i = jcast('int', (i + 1))
        return jcast('int', jcast('int', (-1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


