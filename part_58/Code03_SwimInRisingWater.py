# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 水位上升的泳池中游泳
# 在一个 n x n 的整数矩阵 grid 中
# 每一个方格的值 grid[i][j] 表示位置 (i, j) 的平台高度
# 当开始下雨时，在时间为 t 时，水池中的水位为 t
# 你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台
# 假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的
# 当然，在你游泳的时候你必须待在坐标方格里面。
# 你从坐标方格的左上平台 (0，0) 出发
# 返回 你到达坐标方格的右下平台 (n-1, n-1) 所需的最少时间
# 测试链接 : https://leetcode.cn/problems/swim-in-rising-water/
class Code03_SwimInRisingWater:
    __java_fields__ = {'move': 'move'}
    # 0:上，1:右，2:下，3:左
    move = None
    @staticmethod
    def swimInWater(grid):
        n = jcast('int', jget(grid, 'length'))
        m = jcast('int', jget(grid[0], 'length'))
        distance = jarray('int', [n, m])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                jset(distance[i], j, jget(Integer, 'MAX_VALUE'))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        jset(distance[0], 0, grid[0][0])
        visited = jarray('boolean', [n, m])
        # 0 : 格子的行
        # 1 : 格子的列
        # 2 : 源点到当前格子的代价
        heap = jnew('PriorityQueue', (lambda a, b: (a[2] - b[2])))
        jcall(heap, 'add', jarray('int', [None], [0, 0, grid[0][0]]))
        while (not jcall(heap, 'isEmpty')):
            try:
                x = jcast('int', jcall(heap, 'peek')[0])
                y = jcast('int', jcall(heap, 'peek')[1])
                c = jcast('int', jcall(heap, 'peek')[2])
                jcall(heap, 'poll')
                if visited[x][y]:
                    raise JContinue(None)
                jset(visited[x], y, True)
                if ((x == jcast('int', (n - 1))) and (y == jcast('int', (m - 1)))):
                    # 常见剪枝
                    # 发现终点直接返回
                    # 不用等都结束
                    return jcast('int', c)
                i = jcast('int', 0)
                nx = 0
                ny = 0
                nc = 0
                while (i < 4):
                    nx = jcast('int', jcast('int', jadd(x, Code03_SwimInRisingWater.move[i])))
                    ny = jcast('int', jcast('int', jadd(y, Code03_SwimInRisingWater.move[jcast('int', jadd(i, 1))])))
                    if (((((nx >= 0) and (nx < n)) and (ny >= 0)) and (ny < m)) and (not visited[nx][ny])):
                        nc = jcast('int', jstatic('Math', 'max', c, grid[nx][ny]))
                        if (nc < distance[nx][ny]):
                            jset(distance[nx], ny, nc)
                            jcall(heap, 'add', jarray('int', [None], [nx, ny, nc]))
                    i = jcast('int', (i + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        return jcast('int', jcast('int', (-1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_SwimInRisingWater.move = jarray('int', [None], [jcast('int', (-1)), 0, 1, 0, jcast('int', (-1))])
