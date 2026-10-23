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

# 获取所有钥匙的最短路径
# 给定一个二维网格 grid ，其中：
# '.' 代表一个空房间、'#' 代表一堵、'@' 是起点
# 小写字母代表钥匙、大写字母代表锁
# 从起点开始出发，一次移动是指向四个基本方向之一行走一个单位空间
# 不能在网格外面行走，也无法穿过一堵墙
# 如果途经一个钥匙，我们就把它捡起来。除非我们手里有对应的钥匙，否则无法通过锁。
# 假设 k 为 钥匙/锁 的个数，且满足 1 <= k <= 6，
# 字母表中的前 k 个字母在网格中都有自己对应的一个小写和一个大写字母
# 换言之，每个锁有唯一对应的钥匙，每个钥匙也有唯一对应的锁
# 另外，代表钥匙和锁的字母互为大小写并按字母顺序排列
# 返回获取所有钥匙所需要的移动的最少次数。如果无法获取所有钥匙，返回 -1 。
# 测试链接：https://leetcode.cn/problems/shortest-path-to-get-all-keys
class Code04_ShortestPathToGetAllKeys:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXK': 'MAXK', 'move': 'move', 'grid': 'grid', 'visited': 'visited', 'queue': 'queue', 'l': 'l', 'r': 'r', 'n': 'n', 'm': 'm', 'key': 'key'}
    MAXN = 0
    MAXM = 0
    MAXK = 0
    # 0:上，1:右，2:下，3:左
    move = None
    grid = None
    visited = None
    # 0 : 行
    # 1 : 列
    # 2 : 收集钥匙的状态
    queue = None
    l = 0
    r = 0
    n = 0
    m = 0
    key = 0
    @staticmethod
    def build(g):
        Code04_ShortestPathToGetAllKeys.l = jcast('int', jset(Code04_ShortestPathToGetAllKeys, 'r', jset(Code04_ShortestPathToGetAllKeys, 'key', 0)))
        Code04_ShortestPathToGetAllKeys.n = jcast('int', jget(g, 'length'))
        Code04_ShortestPathToGetAllKeys.m = jcast('int', jcall(g[0], 'length'))
        i = jcast('int', 0)
        while (i < Code04_ShortestPathToGetAllKeys.n):
            jset(Code04_ShortestPathToGetAllKeys.grid, i, jcall(g[i], 'toCharArray'))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < Code04_ShortestPathToGetAllKeys.n):
            j = jcast('int', 0)
            while (j < Code04_ShortestPathToGetAllKeys.m):
                if (Code04_ShortestPathToGetAllKeys.grid[i][j] == jchar('@')):
                    jset(Code04_ShortestPathToGetAllKeys.queue[Code04_ShortestPathToGetAllKeys.r], 0, i)
                    jset(Code04_ShortestPathToGetAllKeys.queue[Code04_ShortestPathToGetAllKeys.r], 1, j)
                    # 0 : 000000
                    jset(Code04_ShortestPathToGetAllKeys.queue[((_java_obj_1 := Code04_ShortestPathToGetAllKeys), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]], 2, 0)
                if ((Code04_ShortestPathToGetAllKeys.grid[i][j] >= jchar('a')) and (Code04_ShortestPathToGetAllKeys.grid[i][j] <= jchar('f'))):
                    Code04_ShortestPathToGetAllKeys.key = jcast('int', jcast('int', (Code04_ShortestPathToGetAllKeys.key | jcast('int', (1 << (jcast('int', (Code04_ShortestPathToGetAllKeys.grid[i][j] - jchar('a'))) & 31))))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < Code04_ShortestPathToGetAllKeys.n):
            j = jcast('int', 0)
            while (j < Code04_ShortestPathToGetAllKeys.m):
                s = jcast('int', 0)
                while (s <= Code04_ShortestPathToGetAllKeys.key):
                    jset(Code04_ShortestPathToGetAllKeys.visited[i][j], s, False)
                    s = jcast('int', (s + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def shortestPathAllKeys(g):
        Code04_ShortestPathToGetAllKeys.build(g)
        level = jcast('int', 1)
        while (Code04_ShortestPathToGetAllKeys.l < Code04_ShortestPathToGetAllKeys.r):
            try:
                k = jcast('int', 0)
                size = jcast('int', jcast('int', (Code04_ShortestPathToGetAllKeys.r - Code04_ShortestPathToGetAllKeys.l)))
                x = 0
                y = 0
                s = 0
                while (k < size):
                    try:
                        x = jcast('int', Code04_ShortestPathToGetAllKeys.queue[Code04_ShortestPathToGetAllKeys.l][0])
                        y = jcast('int', Code04_ShortestPathToGetAllKeys.queue[Code04_ShortestPathToGetAllKeys.l][1])
                        s = jcast('int', Code04_ShortestPathToGetAllKeys.queue[((_java_obj_6 := Code04_ShortestPathToGetAllKeys), (_java_key_7 := 'l'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))), _java_old_8)[4]][2])
                        i = jcast('int', 0)
                        nx = 0
                        ny = 0
                        ns = 0
                        while (i < 4):
                            try:
                                nx = jcast('int', jcast('int', jadd(x, Code04_ShortestPathToGetAllKeys.move[i])))
                                ny = jcast('int', jcast('int', jadd(y, Code04_ShortestPathToGetAllKeys.move[jcast('int', jadd(i, 1))])))
                                ns = jcast('int', s)
                                if (((((nx < 0) or (nx == Code04_ShortestPathToGetAllKeys.n)) or (ny < 0)) or (ny == Code04_ShortestPathToGetAllKeys.m)) or (Code04_ShortestPathToGetAllKeys.grid[nx][ny] == jchar('#'))):
                                    # 越界或者障碍
                                    raise JContinue(None)
                                if (((Code04_ShortestPathToGetAllKeys.grid[nx][ny] >= jchar('A')) and (Code04_ShortestPathToGetAllKeys.grid[nx][ny] <= jchar('F'))) and (jcast('int', (ns & jcast('int', (1 << (jcast('int', (Code04_ShortestPathToGetAllKeys.grid[nx][ny] - jchar('A'))) & 31))))) == 0)):
                                    # 是锁，又没有对应的钥匙
                                    raise JContinue(None)
                                if ((Code04_ShortestPathToGetAllKeys.grid[nx][ny] >= jchar('a')) and (Code04_ShortestPathToGetAllKeys.grid[nx][ny] <= jchar('f'))):
                                    # 是某一把钥匙
                                    ns = jcast('int', jcast('int', (ns | jcast('int', (1 << (jcast('int', (Code04_ShortestPathToGetAllKeys.grid[nx][ny] - jchar('a'))) & 31))))))
                                if (ns == Code04_ShortestPathToGetAllKeys.key):
                                    # 常见剪枝
                                    # 发现终点直接返回
                                    # 不用等都结束
                                    return jcast('int', level)
                                if (not Code04_ShortestPathToGetAllKeys.visited[nx][ny][ns]):
                                    jset(Code04_ShortestPathToGetAllKeys.visited[nx][ny], ns, True)
                                    jset(Code04_ShortestPathToGetAllKeys.queue[Code04_ShortestPathToGetAllKeys.r], 0, nx)
                                    jset(Code04_ShortestPathToGetAllKeys.queue[Code04_ShortestPathToGetAllKeys.r], 1, ny)
                                    jset(Code04_ShortestPathToGetAllKeys.queue[((_java_obj_10 := Code04_ShortestPathToGetAllKeys), (_java_key_11 := 'r'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]], 2, ns)
                            except JContinue as _java_control_9:
                                if _java_control_9.label not in (None,):
                                    raise
                            except JBreak as _java_control_9:
                                if _java_control_9.label not in (None,):
                                    raise
                                break
                            i = jcast('int', (i + 1))
                    except JContinue as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                    except JBreak as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                        break
                    k = jcast('int', (k + 1))
                level = jcast('int', (level + 1))
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
        return jcast('int', jcast('int', (-1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_ShortestPathToGetAllKeys.MAXN = jcast('int', 31)
Code04_ShortestPathToGetAllKeys.MAXM = jcast('int', 31)
Code04_ShortestPathToGetAllKeys.MAXK = jcast('int', 6)
Code04_ShortestPathToGetAllKeys.move = jarray('int', [None], [jcast('int', (-1)), 0, 1, 0, jcast('int', (-1))])
Code04_ShortestPathToGetAllKeys.grid = jarray('char', [Code04_ShortestPathToGetAllKeys.MAXN, None])
Code04_ShortestPathToGetAllKeys.visited = jarray('boolean', [Code04_ShortestPathToGetAllKeys.MAXN, Code04_ShortestPathToGetAllKeys.MAXM, jcast('int', (1 << (Code04_ShortestPathToGetAllKeys.MAXK & 31)))])
Code04_ShortestPathToGetAllKeys.queue = jarray('int', [jcast('int', (jcast('int', (Code04_ShortestPathToGetAllKeys.MAXN * Code04_ShortestPathToGetAllKeys.MAXM)) * jcast('int', (1 << (Code04_ShortestPathToGetAllKeys.MAXK & 31))))), 3])
Code04_ShortestPathToGetAllKeys.l = jcast('int', 0)
Code04_ShortestPathToGetAllKeys.r = jcast('int', 0)
Code04_ShortestPathToGetAllKeys.n = jcast('int', 0)
Code04_ShortestPathToGetAllKeys.m = jcast('int', 0)
Code04_ShortestPathToGetAllKeys.key = jcast('int', 0)
