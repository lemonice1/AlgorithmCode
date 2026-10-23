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

# 最小体力消耗路径
# 你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights
# 其中 heights[row][col] 表示格子 (row, col) 的高度
# 一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1)
# （注意下标从 0 开始编号）。你每次可以往 上，下，左，右 四个方向之一移动
# 你想要找到耗费 体力 最小的一条路径
# 一条路径耗费的体力值是路径上，相邻格子之间高度差绝对值的最大值
# 请你返回从左上角走到右下角的最小 体力消耗值
# 测试链接 ：https://leetcode.cn/problems/path-with-minimum-effort/
class Code02_PathWithMinimumEffort:
    __java_fields__ = {'move': 'move'}
    # 0:上，1:右，2:下，3:左
    move = None
    def minimumEffortPath(self, heights):
        # (0,0)源点
        # -> (x,y)
        n = jcast('int', jget(heights, 'length'))
        m = jcast('int', jget(heights[0], 'length'))
        distance = jarray('int', [n, m])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                jset(distance[i], j, jget(Integer, 'MAX_VALUE'))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        jset(distance[0], 0, 0)
        visited = jarray('boolean', [n, m])
        # 0 : 格子的行
        # 1 : 格子的列
        # 2 : 源点到当前格子的代价
        heap = jnew('PriorityQueue', (lambda a, b: (a[2] - b[2])))
        jcall(heap, 'add', jarray('int', [None], [0, 0, 0]))
        while (not jcall(heap, 'isEmpty')):
            try:
                record = jcall(heap, 'poll')
                x = jcast('int', record[0])
                y = jcast('int', record[1])
                c = jcast('int', record[2])
                if visited[x][y]:
                    raise JContinue(None)
                if ((x == jcast('int', (n - 1))) and (y == jcast('int', (m - 1)))):
                    # 常见剪枝
                    # 发现终点直接返回
                    # 不用等都结束
                    return jcast('int', c)
                jset(visited[x], y, True)
                i = jcast('int', 0)
                while (i < 4):
                    nx = jcast('int', jcast('int', jadd(x, Code02_PathWithMinimumEffort.move[i])))
                    ny = jcast('int', jcast('int', jadd(y, Code02_PathWithMinimumEffort.move[jcast('int', jadd(i, 1))])))
                    if (((((nx >= 0) and (nx < n)) and (ny >= 0)) and (ny < m)) and (not visited[nx][ny])):
                        nc = jcast('int', jstatic('Math', 'max', c, jstatic('Math', 'abs', jcast('int', (heights[x][y] - heights[nx][ny])))))
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


Code02_PathWithMinimumEffort.move = jarray('int', [None], [jcast('int', (-1)), 0, 1, 0, jcast('int', (-1))])
