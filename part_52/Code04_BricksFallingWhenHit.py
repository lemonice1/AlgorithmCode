# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 打砖块
# 有一个 m * n 的二元网格 grid ，其中 1 表示砖块，0 表示空白
# 砖块 稳定（不会掉落）的前提是：
# 一块砖直接连接到网格的顶部，或者
# 至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时
# 给你一个数组 hits ，这是需要依次消除砖块的位置
# 每当消除 hits[i] = (rowi, coli) 位置上的砖块时，对应位置的砖块（若存在）会消失
# 然后其他的砖块可能因为这一消除操作而 掉落
# 一旦砖块掉落，它会 立即 从网格 grid 中消失（即，它不会落在其他稳定的砖块上）
# 返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。
# 注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。
# 测试链接 : https://leetcode.cn/problems/bricks-falling-when-hit/
class Code04_BricksFallingWhenHit:
    __java_fields__ = {'n': 'n', 'm': 'm', 'grid': 'grid'}
    n = 0
    m = 0
    grid = None
    @staticmethod
    def hitBricks(g, h):
        Code04_BricksFallingWhenHit.grid = g
        Code04_BricksFallingWhenHit.n = jcast('int', jget(g, 'length'))
        Code04_BricksFallingWhenHit.m = jcast('int', jget(g[0], 'length'))
        ans = jarray('int', [jget(h, 'length')])
        if (Code04_BricksFallingWhenHit.n == 1):
            return ans
        for hit in h:
            ((_java_obj_1 := Code04_BricksFallingWhenHit.grid[hit[0]]), (_java_key_2 := hit[1]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))), _java_old_3)[4]
        i = jcast('int', 0)
        while (i < Code04_BricksFallingWhenHit.m):
            Code04_BricksFallingWhenHit.dfs(0, i)
            i = jcast('int', (i + 1))
        i = jcast('int', jcast('int', (jget(h, 'length') - 1)))
        row = 0
        col = 0
        while (i >= 0):
            row = jcast('int', h[i][0])
            col = jcast('int', h[i][1])
            ((_java_obj_4 := Code04_BricksFallingWhenHit.grid[row]), (_java_key_5 := col), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]
            if Code04_BricksFallingWhenHit.worth(row, col):
                jset(ans, i, jcast('int', (Code04_BricksFallingWhenHit.dfs(row, col) - 1)))
            i = jcast('int', (i - 1))
        return ans

    # 从(i,j)格子出发，遇到1就感染成2
    # 统计新增了几个2！
    @staticmethod
    def dfs(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if (((((i < 0) or (i == Code04_BricksFallingWhenHit.n)) or (j < 0)) or (j == Code04_BricksFallingWhenHit.m)) or (Code04_BricksFallingWhenHit.grid[i][j] != 1)):
            return jcast('int', 0)
        jset(Code04_BricksFallingWhenHit.grid[i], j, 2)
        return jcast('int', jcast('int', jadd(jcast('int', jadd(jcast('int', jadd(jcast('int', jadd(1, Code04_BricksFallingWhenHit.dfs(jcast('int', jadd(i, 1)), j))), Code04_BricksFallingWhenHit.dfs(i, jcast('int', jadd(j, 1))))), Code04_BricksFallingWhenHit.dfs(jcast('int', (i - 1)), j))), Code04_BricksFallingWhenHit.dfs(i, jcast('int', (j - 1))))))

    @staticmethod
    def worth(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        return jcast('boolean', ((Code04_BricksFallingWhenHit.grid[i][j] == 1) and (((((i == 0) or ((i > 0) and (Code04_BricksFallingWhenHit.grid[jcast('int', (i - 1))][j] == 2))) or ((i < jcast('int', (Code04_BricksFallingWhenHit.n - 1))) and (Code04_BricksFallingWhenHit.grid[jcast('int', jadd(i, 1))][j] == 2))) or ((j > 0) and (Code04_BricksFallingWhenHit.grid[i][jcast('int', (j - 1))] == 2))) or ((j < jcast('int', (Code04_BricksFallingWhenHit.m - 1))) and (Code04_BricksFallingWhenHit.grid[i][jcast('int', jadd(j, 1))] == 2)))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_BricksFallingWhenHit.n = jcast('int', 0)
Code04_BricksFallingWhenHit.m = jcast('int', 0)
Code04_BricksFallingWhenHit.grid = None
