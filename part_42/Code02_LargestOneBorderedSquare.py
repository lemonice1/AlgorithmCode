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

# 边框为1的最大正方形
# 给你一个由若干 0 和 1 组成的二维网格 grid
# 请你找出边界全部由 1 组成的最大 正方形 子网格
# 并返回该子网格中的元素数量。如果不存在，则返回 0。
# 测试链接 : https://leetcode.cn/problems/largest-1-bordered-square/
class Code02_LargestOneBorderedSquare:
    __java_fields__ = {}
    # 打败比例不高，但完全是常数时间的问题
    # 时间复杂度O(n * m * min(n,m))，额外空间复杂度O(1)
    # 复杂度指标上绝对是最优解
    @staticmethod
    def largest1BorderedSquare(g):
        n = jcast('int', jget(g, 'length'))
        m = jcast('int', jget(g[0], 'length'))
        Code02_LargestOneBorderedSquare.build(n, m, g)
        if (Code02_LargestOneBorderedSquare.sum(g, 0, 0, jcast('int', (n - 1)), jcast('int', (m - 1))) == 0):
            return jcast('int', 0)
        # 找到的最大合法正方形的边长
        ans = jcast('int', 1)
        a = jcast('int', 0)
        while (a < n):
            b = jcast('int', 0)
            while (b < m):
                # (a,b)所有左上角点
                # (c,d)更大边长的右下角点，k是当前尝试的边长
                c = jcast('int', jcast('int', jadd(a, ans)))
                d = jcast('int', jcast('int', jadd(b, ans)))
                k = jcast('int', jcast('int', jadd(ans, 1)))
                while ((c < n) and (d < m)):
                    if (jcast('int', (Code02_LargestOneBorderedSquare.sum(g, a, b, c, d) - Code02_LargestOneBorderedSquare.sum(g, jcast('int', jadd(a, 1)), jcast('int', jadd(b, 1)), jcast('int', (c - 1)), jcast('int', (d - 1))))) == jcast('int', (jcast('int', (k - 1)) << (2 & 31)))):
                        ans = jcast('int', k)
                    c = jcast('int', (c + 1))
                    d = jcast('int', (d + 1))
                    k = jcast('int', (k + 1))
                b = jcast('int', (b + 1))
            a = jcast('int', (a + 1))
        return jcast('int', jcast('int', (ans * ans)))

    # g : 原始二维数组
    # 把g变成原始二维数组的前缀和数组sum，复用自己
    # 不能补0行，0列，都是0
    @staticmethod
    def build(n, m, g):
        n = jcast('int', n)
        m = jcast('int', m)
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                ((_java_obj_1 := g[i]), (_java_key_2 := j), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), jcast('int', (jcast('int', jadd(Code02_LargestOneBorderedSquare.get(g, i, jcast('int', (j - 1))), Code02_LargestOneBorderedSquare.get(g, jcast('int', (i - 1)), j))) - Code02_LargestOneBorderedSquare.get(g, jcast('int', (i - 1)), jcast('int', (j - 1)))))))))[2]
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def sum(g, a, b, c, d):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        return jcast('int', (0 if (a > c) else jcast('int', jadd(jcast('int', (jcast('int', (g[c][d] - Code02_LargestOneBorderedSquare.get(g, c, jcast('int', (b - 1))))) - Code02_LargestOneBorderedSquare.get(g, jcast('int', (a - 1)), d))), Code02_LargestOneBorderedSquare.get(g, jcast('int', (a - 1)), jcast('int', (b - 1)))))))

    @staticmethod
    def get(g, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        return jcast('int', (0 if ((i < 0) or (j < 0)) else g[i][j]))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


