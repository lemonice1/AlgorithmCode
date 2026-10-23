# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 地图分析
# 你现在手里有一份大小为 n x n 的 网格 grid
# 上面的每个 单元格 都用 0 和 1 标记好了其中 0 代表海洋，1 代表陆地。
# 请你找出一个海洋单元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的
# 并返回该距离。如果网格上只有陆地或者海洋，请返回 -1。
# 我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：
# (x0, y0) 和 (x1, y1) 这两个单元格之间的距离是 |x0 - x1| + |y0 - y1| 。
# 测试链接 : https://leetcode.cn/problems/as-far-from-land-as-possible/
class Code01_AsFarFromLandAsPossible:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'queue': 'queue', 'l': 'l', 'r': 'r', 'visited': 'visited', 'move': 'move'}
    MAXN = 0
    MAXM = 0
    queue = None
    l = 0
    r = 0
    visited = None
    # 0:上，1:右，2:下，3:左
    move = None
    # 0  1  2  3   4
    # i
    # (x,y)  i来到0位置 : x + move[i], y + move[i+1] -> x - 1, y
    # (x,y)  i来到1位置 : x + move[i], y + move[i+1] -> x, y + 1
    # (x,y)  i来到2位置 : x + move[i], y + move[i+1] -> x + 1, y
    # (x,y)  i来到3位置 : x + move[i], y + move[i+1] -> x, y - 1
    @staticmethod
    def maxDistance(grid):
        Code01_AsFarFromLandAsPossible.l = jcast('int', jset(Code01_AsFarFromLandAsPossible, 'r', 0))
        n = jcast('int', jget(grid, 'length'))
        m = jcast('int', jget(grid[0], 'length'))
        seas = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                if (grid[i][j] == 1):
                    jset(Code01_AsFarFromLandAsPossible.visited[i], j, True)
                    jset(Code01_AsFarFromLandAsPossible.queue[Code01_AsFarFromLandAsPossible.r], 0, i)
                    jset(Code01_AsFarFromLandAsPossible.queue[((_java_obj_1 := Code01_AsFarFromLandAsPossible), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]], 1, j)
                else:
                    jset(Code01_AsFarFromLandAsPossible.visited[i], j, False)
                    seas = jcast('int', (seas + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        if ((seas == 0) or (seas == jcast('int', (n * m)))):
            return jcast('int', jcast('int', (-1)))
        level = jcast('int', 0)
        while (Code01_AsFarFromLandAsPossible.l < Code01_AsFarFromLandAsPossible.r):
            level = jcast('int', (level + 1))
            size = jcast('int', jcast('int', (Code01_AsFarFromLandAsPossible.r - Code01_AsFarFromLandAsPossible.l)))
            k = jcast('int', 0)
            x = 0
            y = 0
            nx = 0
            ny = 0
            while (k < size):
                x = jcast('int', Code01_AsFarFromLandAsPossible.queue[Code01_AsFarFromLandAsPossible.l][0])
                y = jcast('int', Code01_AsFarFromLandAsPossible.queue[((_java_obj_4 := Code01_AsFarFromLandAsPossible), (_java_key_5 := 'l'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]][1])
                i = jcast('int', 0)
                while (i < 4):
                    # 上、右、下、左
                    nx = jcast('int', jcast('int', jadd(x, Code01_AsFarFromLandAsPossible.move[i])))
                    ny = jcast('int', jcast('int', jadd(y, Code01_AsFarFromLandAsPossible.move[jcast('int', jadd(i, 1))])))
                    if (((((nx >= 0) and (nx < n)) and (ny >= 0)) and (ny < m)) and (not Code01_AsFarFromLandAsPossible.visited[nx][ny])):
                        jset(Code01_AsFarFromLandAsPossible.visited[nx], ny, True)
                        jset(Code01_AsFarFromLandAsPossible.queue[Code01_AsFarFromLandAsPossible.r], 0, nx)
                        jset(Code01_AsFarFromLandAsPossible.queue[((_java_obj_7 := Code01_AsFarFromLandAsPossible), (_java_key_8 := 'r'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]], 1, ny)
                    i = jcast('int', (i + 1))
                k = jcast('int', (k + 1))
        return jcast('int', jcast('int', (level - 1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_AsFarFromLandAsPossible.MAXN = jcast('int', 101)
Code01_AsFarFromLandAsPossible.MAXM = jcast('int', 101)
Code01_AsFarFromLandAsPossible.queue = jarray('int', [jcast('int', (Code01_AsFarFromLandAsPossible.MAXN * Code01_AsFarFromLandAsPossible.MAXM)), 2])
Code01_AsFarFromLandAsPossible.l = jcast('int', 0)
Code01_AsFarFromLandAsPossible.r = jcast('int', 0)
Code01_AsFarFromLandAsPossible.visited = jarray('boolean', [Code01_AsFarFromLandAsPossible.MAXN, Code01_AsFarFromLandAsPossible.MAXM])
Code01_AsFarFromLandAsPossible.move = jarray('int', [None], [jcast('int', (-1)), 0, 1, 0, jcast('int', (-1))])
