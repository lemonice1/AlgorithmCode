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

# 用三种不同颜色为网格涂色
# 给你两个整数m和n，表示m*n的网格，其中每个单元格最开始是白色
# 请你用红、绿、蓝三种颜色为每个单元格涂色，所有单元格都需要被涂色
# 要求相邻单元格的颜色一定要不同
# 返回网格涂色的方法数，答案对 1000000007 取模
# 1 <= m <= 5
# 1 <= n <= 1000
# 测试链接 : https://leetcode.cn/problems/painting-a-grid-with-three-different-colors/
# 有兴趣的同学可以自己改一下空间压缩的版本
class Code02_GridPainting:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXS': 'MAXS', 'MOD': 'MOD', 'n': 'n', 'm': 'm', 'maxs': 'maxs', 'dp': 'dp', 'first': 'first', 'size': 'size'}
    MAXN = 0
    MAXM = 0
    MAXS = 0
    MOD = 0
    n = 0
    m = 0
    maxs = 0
    dp = None
    first = None
    size = 0
    @staticmethod
    def colorTheGrid(rows, cols):
        rows = jcast('int', rows)
        cols = jcast('int', cols)
        Code02_GridPainting.build(rows, cols)
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < Code02_GridPainting.size):
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_GridPainting.f(1, 0, Code02_GridPainting.first[i], 1))), Code02_GridPainting.MOD)))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def build(rows, cols):
        rows = jcast('int', rows)
        cols = jcast('int', cols)
        Code02_GridPainting.n = jcast('int', jstatic('Math', 'max', rows, cols))
        Code02_GridPainting.m = jcast('int', jstatic('Math', 'min', rows, cols))
        Code02_GridPainting.maxs = jcast('int', jcast('int', jstatic('Math', 'pow', 3, Code02_GridPainting.m)))
        i = jcast('int', 0)
        while (i < Code02_GridPainting.n):
            j = jcast('int', 0)
            while (j < Code02_GridPainting.m):
                s = jcast('int', 0)
                while (s < Code02_GridPainting.maxs):
                    jset(Code02_GridPainting.dp[i][j], s, jcast('int', (-1)))
                    s = jcast('int', (s + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        Code02_GridPainting.size = jcast('int', 0)
        Code02_GridPainting.dfs(0, 0, 1)

    # 取得所有第一行的有效状态
    @staticmethod
    def dfs(j, s, bit):
        j = jcast('int', j)
        s = jcast('int', s)
        bit = jcast('int', bit)
        if (j == Code02_GridPainting.m):
            jset(Code02_GridPainting.first, ((_java_obj_1 := Code02_GridPainting), (_java_key_2 := 'size'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], s)
        else:
            left = jcast('int', (jcast('int', (-1)) if (j == 0) else Code02_GridPainting.get(s, jcast('int', jdiv(bit, 3)))))
            if (left != 0):
                Code02_GridPainting.dfs(jcast('int', jadd(j, 1)), Code02_GridPainting.set(s, bit, 0), jcast('int', (bit * 3)))
            if (left != 1):
                Code02_GridPainting.dfs(jcast('int', jadd(j, 1)), Code02_GridPainting.set(s, bit, 1), jcast('int', (bit * 3)))
            if (left != 2):
                Code02_GridPainting.dfs(jcast('int', jadd(j, 1)), Code02_GridPainting.set(s, bit, 2), jcast('int', (bit * 3)))

    @staticmethod
    def f(i, j, s, bit):
        i = jcast('int', i)
        j = jcast('int', j)
        s = jcast('int', s)
        bit = jcast('int', bit)
        if (i == Code02_GridPainting.n):
            return jcast('int', 1)
        if (j == Code02_GridPainting.m):
            return jcast('int', Code02_GridPainting.f(jcast('int', jadd(i, 1)), 0, s, 1))
        if (Code02_GridPainting.dp[i][j][s] != jcast('int', (-1))):
            return jcast('int', Code02_GridPainting.dp[i][j][s])
        # 上方的颜色
        up = jcast('int', Code02_GridPainting.get(s, bit))
        # 左侧的颜色，-1代表左侧没有格子
        left = jcast('int', (jcast('int', (-1)) if (j == 0) else Code02_GridPainting.get(s, jcast('int', jdiv(bit, 3)))))
        ans = jcast('int', 0)
        if ((up != 0) and (left != 0)):
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_GridPainting.f(i, jcast('int', jadd(j, 1)), Code02_GridPainting.set(s, bit, 0), jcast('int', (bit * 3))))), Code02_GridPainting.MOD)))
        if ((up != 1) and (left != 1)):
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_GridPainting.f(i, jcast('int', jadd(j, 1)), Code02_GridPainting.set(s, bit, 1), jcast('int', (bit * 3))))), Code02_GridPainting.MOD)))
        if ((up != 2) and (left != 2)):
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_GridPainting.f(i, jcast('int', jadd(j, 1)), Code02_GridPainting.set(s, bit, 2), jcast('int', (bit * 3))))), Code02_GridPainting.MOD)))
        jset(Code02_GridPainting.dp[i][j], s, ans)
        return jcast('int', ans)

    @staticmethod
    def get(s, bit):
        s = jcast('int', s)
        bit = jcast('int', bit)
        return jcast('int', jcast('int', jmod(jcast('int', jdiv(s, bit)), 3)))

    @staticmethod
    def set(s, bit, v):
        s = jcast('int', s)
        bit = jcast('int', bit)
        v = jcast('int', v)
        return jcast('int', jcast('int', jadd(jcast('int', (s - jcast('int', (Code02_GridPainting.get(s, bit) * bit)))), jcast('int', (v * bit)))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_GridPainting.MAXN = jcast('int', 1001)
Code02_GridPainting.MAXM = jcast('int', 5)
Code02_GridPainting.MAXS = jcast('int', jcast('int', jstatic('Math', 'pow', 3, Code02_GridPainting.MAXM)))
Code02_GridPainting.MOD = jcast('int', 1000000007)
Code02_GridPainting.n = jcast('int', 0)
Code02_GridPainting.m = jcast('int', 0)
Code02_GridPainting.maxs = jcast('int', 0)
Code02_GridPainting.dp = jarray('int', [Code02_GridPainting.MAXN, Code02_GridPainting.MAXM, Code02_GridPainting.MAXS])
Code02_GridPainting.first = jarray('int', [Code02_GridPainting.MAXS])
Code02_GridPainting.size = jcast('int', 0)
