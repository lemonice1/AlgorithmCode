# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 二维接雨水
# 给你一个 m * n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度
# 请计算图中形状最多能接多少体积的雨水。
# 测试链接 : https://leetcode.cn/problems/trapping-rain-water-ii/
class Code05_TrappingRainWaterII:
    __java_fields__ = {}
    @staticmethod
    def trapRainWater(height):
        move = jarray('int', [None], [jcast('int', (-1)), 0, 1, 0, jcast('int', (-1))])
        n = jcast('int', jget(height, 'length'))
        m = jcast('int', jget(height[0], 'length'))
        # 0 : 行
        # 1 : 列
        # 2 : 水线
        heap = jnew('PriorityQueue', (lambda a, b: (a[2] - b[2])))
        visited = jarray('boolean', [n, m])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                if ((((i == 0) or (i == jcast('int', (n - 1)))) or (j == 0)) or (j == jcast('int', (m - 1)))):
                    # 边界
                    jcall(heap, 'add', jarray('int', [None], [i, j, height[i][j]]))
                    jset(visited[i], j, True)
                else:
                    jset(visited[i], j, False)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        while (not jcall(heap, 'isEmpty')):
            record = jcall(heap, 'poll')
            r = jcast('int', record[0])
            c = jcast('int', record[1])
            w = jcast('int', record[2])
            ans = jcast('int', jcast('int', jadd(ans, jcast('int', (w - height[r][c])))))
            i = jcast('int', 0)
            nr = 0
            nc = 0
            while (i < 4):
                nr = jcast('int', jcast('int', jadd(r, move[i])))
                nc = jcast('int', jcast('int', jadd(c, move[jcast('int', jadd(i, 1))])))
                if (((((nr >= 0) and (nr < n)) and (nc >= 0)) and (nc < m)) and (not visited[nr][nc])):
                    jcall(heap, 'add', jarray('int', [None], [nr, nc, jstatic('Math', 'max', height[nr][nc], w)]))
                    jset(visited[nr], nc, True)
                i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


