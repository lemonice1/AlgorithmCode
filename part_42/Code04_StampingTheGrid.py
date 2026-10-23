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

# 用邮票贴满网格图
# 给你一个 m * n 的二进制矩阵 grid
# 每个格子要么为 0 （空）要么为 1 （被占据）
# 给你邮票的尺寸为 stampHeight * stampWidth
# 我们想将邮票贴进二进制矩阵中，且满足以下 限制 和 要求 ：
# 覆盖所有空格子，不覆盖任何被占据的格子
# 可以放入任意数目的邮票，邮票可以相互有重叠部分
# 邮票不允许旋转，邮票必须完全在矩阵内
# 如果在满足上述要求的前提下，可以放入邮票，请返回 true ，否则返回 false
# 测试链接 : https://leetcode.cn/problems/stamping-the-grid/
class Code04_StampingTheGrid:
    __java_fields__ = {}
    # 时间复杂度O(n*m)，额外空间复杂度O(n*m)
    @staticmethod
    def possibleToStamp(grid, h, w):
        h = jcast('int', h)
        w = jcast('int', w)
        n = jcast('int', jget(grid, 'length'))
        m = jcast('int', jget(grid[0], 'length'))
        # sum是前缀和数组
        # 查询原始矩阵中的某个范围的累加和很快速
        sum = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(m, 1))])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                jset(sum[jcast('int', jadd(i, 1))], jcast('int', jadd(j, 1)), grid[i][j])
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        Code04_StampingTheGrid.build(sum)
        # 差分矩阵
        # 当贴邮票的时候，不再原始矩阵里贴，在差分矩阵里贴
        # 原始矩阵就用来判断能不能贴邮票，不进行修改
        # 每贴一张邮票都在差分矩阵里修改
        diff = jarray('int', [jcast('int', jadd(n, 2)), jcast('int', jadd(m, 2))])
        a = jcast('int', 1)
        c = jcast('int', jcast('int', (jcast('int', jadd(a, h)) - 1)))
        while (c <= n):
            b = jcast('int', 1)
            d = jcast('int', jcast('int', (jcast('int', jadd(b, w)) - 1)))
            while (d <= m):
                # 原始矩阵中 (a,b)左上角点
                # 根据邮票规格，h、w，算出右下角点(c,d)
                # 这个区域彻底都是0，那么:
                # sumRegion(sum, a, b, c, d) == 0
                # 那么此时这个区域可以贴邮票
                if (Code04_StampingTheGrid.sumRegion(sum, a, b, c, d) == 0):
                    Code04_StampingTheGrid.add(diff, a, b, c, d)
                b = jcast('int', (b + 1))
                d = jcast('int', (d + 1))
            a = jcast('int', (a + 1))
            c = jcast('int', (c + 1))
        Code04_StampingTheGrid.build(diff)
        # 检查所有的格子！
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                # 原始矩阵里：grid[i][j] == 0，说明是个洞
                # 差分矩阵里：diff[i + 1][j + 1] == 0，说明洞上并没有邮票
                # 此时返回false
                if ((grid[i][j] == 0) and (diff[jcast('int', jadd(i, 1))][jcast('int', jadd(j, 1))] == 0)):
                    return jcast('boolean', False)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('boolean', True)

    @staticmethod
    def build(m):
        i = jcast('int', 1)
        while (i < jget(m, 'length')):
            j = jcast('int', 1)
            while (j < jget(m[0], 'length')):
                ((_java_obj_1 := m[i]), (_java_key_2 := j), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), jcast('int', (jcast('int', jadd(m[jcast('int', (i - 1))][j], m[i][jcast('int', (j - 1))])) - m[jcast('int', (i - 1))][jcast('int', (j - 1))]))))))[2]
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def sumRegion(sum, a, b, c, d):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        return jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (sum[c][d] - sum[c][jcast('int', (b - 1))])) - sum[jcast('int', (a - 1))][d])), sum[jcast('int', (a - 1))][jcast('int', (b - 1))])))

    @staticmethod
    def add(diff, a, b, c, d):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        ((_java_obj_3 := diff[a]), (_java_key_4 := b), jset(_java_obj_3, _java_key_4, jcast('int', jadd(jget(_java_obj_3, _java_key_4), 1))))[2]
        ((_java_obj_5 := diff[jcast('int', jadd(c, 1))]), (_java_key_6 := jcast('int', jadd(d, 1))), jset(_java_obj_5, _java_key_6, jcast('int', jadd(jget(_java_obj_5, _java_key_6), 1))))[2]
        ((_java_obj_7 := diff[jcast('int', jadd(c, 1))]), (_java_key_8 := b), jset(_java_obj_7, _java_key_8, jcast('int', (jget(_java_obj_7, _java_key_8) - 1))))[2]
        ((_java_obj_9 := diff[a]), (_java_key_10 := jcast('int', jadd(d, 1))), jset(_java_obj_9, _java_key_10, jcast('int', (jget(_java_obj_9, _java_key_10) - 1))))[2]

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


