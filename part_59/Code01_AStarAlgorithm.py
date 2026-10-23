# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# A*算法模版（对数器验证）
class Code01_AStarAlgorithm:
    __java_fields__ = {'move': 'move'}
    # 0:上，1:右，2:下，3:左
    move = None
    # Dijkstra算法
    # grid[i][j] == 0 代表障碍
    # grid[i][j] == 1 代表道路
    # 只能走上、下、左、右，不包括斜线方向
    # 返回从(startX, startY)到(targetX, targetY)的最短距离
    @staticmethod
    def minDistance1(grid, startX, startY, targetX, targetY):
        startX = jcast('int', startX)
        startY = jcast('int', startY)
        targetX = jcast('int', targetX)
        targetY = jcast('int', targetY)
        if ((grid[startX][startY] == 0) or (grid[targetX][targetY] == 0)):
            return jcast('int', jcast('int', (-1)))
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
        jset(distance[startX], startY, 1)
        visited = jarray('boolean', [n, m])
        heap = jnew('PriorityQueue', (lambda a, b: (a[2] - b[2])))
        # 0 : 行
        # 1 : 列
        # 2 : 从源点出发到达当前点的距离
        jcall(heap, 'add', jarray('int', [None], [startX, startY, 1]))
        while (not jcall(heap, 'isEmpty')):
            try:
                cur = jcall(heap, 'poll')
                x = jcast('int', cur[0])
                y = jcast('int', cur[1])
                if visited[x][y]:
                    raise JContinue(None)
                jset(visited[x], y, True)
                if ((x == targetX) and (y == targetY)):
                    return jcast('int', distance[x][y])
                i = jcast('int', 0)
                nx = 0
                ny = 0
                while (i < 4):
                    nx = jcast('int', jcast('int', jadd(x, Code01_AStarAlgorithm.move[i])))
                    ny = jcast('int', jcast('int', jadd(y, Code01_AStarAlgorithm.move[jcast('int', jadd(i, 1))])))
                    if (((((((nx >= 0) and (nx < n)) and (ny >= 0)) and (ny < m)) and (grid[nx][ny] == 1)) and (not visited[nx][ny])) and (jcast('int', jadd(distance[x][y], 1)) < distance[nx][ny])):
                        jset(distance[nx], ny, jcast('int', jadd(distance[x][y], 1)))
                        jcall(heap, 'add', jarray('int', [None], [nx, ny, jcast('int', jadd(distance[x][y], 1))]))
                    i = jcast('int', (i + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        return jcast('int', jcast('int', (-1)))

    # A*算法
    # grid[i][j] == 0 代表障碍
    # grid[i][j] == 1 代表道路
    # 只能走上、下、左、右，不包括斜线方向
    # 返回从(startX, startY)到(targetX, targetY)的最短距离
    @staticmethod
    def minDistance2(grid, startX, startY, targetX, targetY):
        startX = jcast('int', startX)
        startY = jcast('int', startY)
        targetX = jcast('int', targetX)
        targetY = jcast('int', targetY)
        if ((grid[startX][startY] == 0) or (grid[targetX][targetY] == 0)):
            return jcast('int', jcast('int', (-1)))
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
        jset(distance[startX], startY, 1)
        visited = jarray('boolean', [n, m])
        # 0 : 行
        # 1 : 列
        # 2 : 从源点出发到达当前点的距离 + 当前点到终点的预估距离
        heap = jnew('PriorityQueue', (lambda a, b: (a[2] - b[2])))
        jcall(heap, 'add', jarray('int', [None], [startX, startY, jcast('int', jadd(1, Code01_AStarAlgorithm.f1(startX, startY, targetX, targetY)))]))
        while (not jcall(heap, 'isEmpty')):
            try:
                cur = jcall(heap, 'poll')
                x = jcast('int', cur[0])
                y = jcast('int', cur[1])
                if visited[x][y]:
                    raise JContinue(None)
                jset(visited[x], y, True)
                if ((x == targetX) and (y == targetY)):
                    return jcast('int', distance[x][y])
                i = jcast('int', 0)
                nx = 0
                ny = 0
                while (i < 4):
                    nx = jcast('int', jcast('int', jadd(x, Code01_AStarAlgorithm.move[i])))
                    ny = jcast('int', jcast('int', jadd(y, Code01_AStarAlgorithm.move[jcast('int', jadd(i, 1))])))
                    if (((((((nx >= 0) and (nx < n)) and (ny >= 0)) and (ny < m)) and (grid[nx][ny] == 1)) and (not visited[nx][ny])) and (jcast('int', jadd(distance[x][y], 1)) < distance[nx][ny])):
                        jset(distance[nx], ny, jcast('int', jadd(distance[x][y], 1)))
                        jcall(heap, 'add', jarray('int', [None], [nx, ny, jcast('int', jadd(jcast('int', jadd(distance[x][y], 1)), Code01_AStarAlgorithm.f1(nx, ny, targetX, targetY)))]))
                    i = jcast('int', (i + 1))
            except JContinue as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
            except JBreak as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
                break
        return jcast('int', jcast('int', (-1)))

    # 曼哈顿距离
    @staticmethod
    def f1(x, y, targetX, targetY):
        x = jcast('int', x)
        y = jcast('int', y)
        targetX = jcast('int', targetX)
        targetY = jcast('int', targetY)
        return jcast('int', jcast('int', jadd(jstatic('Math', 'abs', jcast('int', (targetX - x))), jstatic('Math', 'abs', jcast('int', (targetY - y))))))

    # 对角线距离
    @staticmethod
    def f2(x, y, targetX, targetY):
        x = jcast('int', x)
        y = jcast('int', y)
        targetX = jcast('int', targetX)
        targetY = jcast('int', targetY)
        return jcast('int', jstatic('Math', 'max', jstatic('Math', 'abs', jcast('int', (targetX - x))), jstatic('Math', 'abs', jcast('int', (targetY - y)))))

    # 欧式距离
    @staticmethod
    def f3(x, y, targetX, targetY):
        x = jcast('int', x)
        y = jcast('int', y)
        targetX = jcast('int', targetX)
        targetY = jcast('int', targetY)
        return jcast('double', jstatic('Math', 'sqrt', jadd(jstatic('Math', 'pow', jcast('int', (targetX - x)), 2), jstatic('Math', 'pow', jcast('int', (targetY - y)), 2))))

    # 为了测试
    @staticmethod
    def randomGrid(n):
        n = jcast('int', n)
        grid = jarray('int', [n, n])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < n):
                if (jstatic('Math', 'random') < 0.3):
                    # 每个格子有30%概率是0
                    jset(grid[i], j, 0)
                else:
                    # 每个格子有70%概率是1
                    jset(grid[i], j, 1)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return grid

    # 为了测试
    @staticmethod
    def main(args):
        len = jcast('int', 100)
        testTime = jcast('int', 10000)
        jprint('功能测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTime):
            n = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * len)), 2)))
            grid = Code01_AStarAlgorithm.randomGrid(n)
            startX = jcast('int', jcast('int', (jstatic('Math', 'random') * n)))
            startY = jcast('int', jcast('int', (jstatic('Math', 'random') * n)))
            targetX = jcast('int', jcast('int', (jstatic('Math', 'random') * n)))
            targetY = jcast('int', jcast('int', (jstatic('Math', 'random') * n)))
            ans1 = jcast('int', Code01_AStarAlgorithm.minDistance1(grid, startX, startY, targetX, targetY))
            ans2 = jcast('int', Code01_AStarAlgorithm.minDistance2(grid, startX, startY, targetX, targetY))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('功能测试结束', newline=True)
        jprint('性能测试开始', newline=True)
        grid = Code01_AStarAlgorithm.randomGrid(4000)
        startX = jcast('int', 0)
        startY = jcast('int', 0)
        targetX = jcast('int', 3900)
        targetY = jcast('int', 3900)
        start = 0
        end = 0
        start = jcast('long', jstatic('System', 'currentTimeMillis'))
        ans1 = jcast('int', Code01_AStarAlgorithm.minDistance1(grid, startX, startY, targetX, targetY))
        end = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd(jadd(jadd('运行dijskra算法结果: ', ans1), ', 运行时间(毫秒) : '), jcast('long', (end - start))), newline=True)
        start = jcast('long', jstatic('System', 'currentTimeMillis'))
        ans2 = jcast('int', Code01_AStarAlgorithm.minDistance2(grid, startX, startY, targetX, targetY))
        end = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd(jadd(jadd('运行A*算法结果: ', ans2), ', 运行时间(毫秒) : '), jcast('long', (end - start))), newline=True)
        jprint('性能测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_AStarAlgorithm.move = jarray('int', [None], [jcast('int', (-1)), 0, 1, 0, jcast('int', (-1))])

if __name__ == '__main__':
    Code01_AStarAlgorithm.main([])
