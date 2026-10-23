# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最强祝福力场
# 小扣在探索丛林的过程中，无意间发现了传说中"落寞的黄金之都"
# 而在这片建筑废墟的地带中，小扣使用探测仪监测到了存在某种带有「祝福」效果的力场
# 经过不断的勘测记录，小扣将所有力场的分布都记录了下来
# forceField[i] = [x,y,side]
# 表示第 i 片力场将覆盖以坐标 (x,y) 为中心，边长为 side 的正方形区域。
# 若任意一点的 力场强度 等于覆盖该点的力场数量
# 请求出在这片地带中 力场强度 最强处的 力场强度
# 注意：力场范围的边缘同样被力场覆盖。
# 测试链接 : https://leetcode.cn/problems/xepqZ5/
class Code05_StrongestForceField:
    __java_fields__ = {}
    # 时间复杂度O(n^2)，额外空间复杂度O(n^2)，n是力场的个数
    @staticmethod
    def fieldOfGreatestBlessing(fields):
        n = jcast('int', jget(fields, 'length'))
        # n : 矩形的个数，x 2*n个坐标
        xs = jarray('long', [jcast('int', (n << (1 & 31)))])
        ys = jarray('long', [jcast('int', (n << (1 & 31)))])
        i = jcast('int', 0)
        k = jcast('int', 0)
        p = jcast('int', 0)
        while (i < n):
            x = jcast('long', fields[i][0])
            y = jcast('long', fields[i][1])
            r = jcast('long', fields[i][2])
            jset(xs, ((_java_old_1 := k), (k := jcast('int', (k + (1)))), _java_old_1)[2], jcast('long', (jcast('long', (x << (1 & 63))) - r)))
            jset(xs, ((_java_old_2 := k), (k := jcast('int', (k + (1)))), _java_old_2)[2], jcast('long', jadd(jcast('long', (x << (1 & 63))), r)))
            jset(ys, ((_java_old_3 := p), (p := jcast('int', (p + (1)))), _java_old_3)[2], jcast('long', (jcast('long', (y << (1 & 63))) - r)))
            jset(ys, ((_java_old_4 := p), (p := jcast('int', (p + (1)))), _java_old_4)[2], jcast('long', jadd(jcast('long', (y << (1 & 63))), r)))
            i = jcast('int', (i + 1))
        # xs数组中，排序了且相同值只留一份，返回有效长度
        sizex = jcast('int', Code05_StrongestForceField.sort(xs))
        # ys数组中，排序了且相同值只留一份，返回有效长度
        sizey = jcast('int', Code05_StrongestForceField.sort(ys))
        # n个力场，sizex : 2 * n, sizey : 2 * n
        diff = jarray('int', [jcast('int', jadd(sizex, 2)), jcast('int', jadd(sizey, 2))])
        i = jcast('int', 0)
        a = 0
        b = 0
        c = 0
        d = 0
        while (i < n):
            x = jcast('long', fields[i][0])
            y = jcast('long', fields[i][1])
            r = jcast('long', fields[i][2])
            a = jcast('int', Code05_StrongestForceField.rank(xs, jcast('long', (jcast('long', (x << (1 & 63))) - r)), sizex))
            b = jcast('int', Code05_StrongestForceField.rank(ys, jcast('long', (jcast('long', (y << (1 & 63))) - r)), sizey))
            c = jcast('int', Code05_StrongestForceField.rank(xs, jcast('long', jadd(jcast('long', (x << (1 & 63))), r)), sizex))
            d = jcast('int', Code05_StrongestForceField.rank(ys, jcast('long', jadd(jcast('long', (y << (1 & 63))), r)), sizey))
            Code05_StrongestForceField.add(diff, a, b, c, d)
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        # O(n^2)
        i = jcast('int', 1)
        while (i < jget(diff, 'length')):
            j = jcast('int', 1)
            while (j < jget(diff[0], 'length')):
                ((_java_obj_5 := diff[i]), (_java_key_6 := j), jset(_java_obj_5, _java_key_6, jcast('int', jadd(jget(_java_obj_5, _java_key_6), jcast('int', (jcast('int', jadd(diff[jcast('int', (i - 1))][j], diff[i][jcast('int', (j - 1))])) - diff[jcast('int', (i - 1))][jcast('int', (j - 1))]))))))[2]
                ans = jcast('int', jstatic('Math', 'max', ans, diff[i][j]))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # [50,70,30,70,30,60] 长度6
    # [30,30,50,60,70,70]
    # [30,50,60,70] 60 -> 3
    # 1  2  3  4
    # 长度4，
    @staticmethod
    def sort(nums):
        jstatic('Arrays', 'sort', nums)
        size = jcast('int', 1)
        i = jcast('int', 1)
        while (i < jget(nums, 'length')):
            if (nums[i] != nums[jcast('int', (size - 1))]):
                jset(nums, ((_java_old_7 := size), (size := jcast('int', (size + (1)))), _java_old_7)[2], nums[i])
            i = jcast('int', (i + 1))
        return jcast('int', size)

    # nums 有序数组，有效长度是size，0~size-1范围上无重复值
    # 已知v一定在nums[0~size-1]，返回v所对应的编号
    @staticmethod
    def rank(nums, v, size):
        v = jcast('long', v)
        size = jcast('int', size)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (size - 1)))
        m = 0
        ans = jcast('int', 0)
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (nums[m] >= v):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', jcast('int', jadd(ans, 1)))

    # 二维差分
    @staticmethod
    def add(diff, a, b, c, d):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        ((_java_obj_8 := diff[a]), (_java_key_9 := b), jset(_java_obj_8, _java_key_9, jcast('int', jadd(jget(_java_obj_8, _java_key_9), 1))))[2]
        ((_java_obj_10 := diff[jcast('int', jadd(c, 1))]), (_java_key_11 := jcast('int', jadd(d, 1))), jset(_java_obj_10, _java_key_11, jcast('int', jadd(jget(_java_obj_10, _java_key_11), 1))))[2]
        ((_java_obj_12 := diff[jcast('int', jadd(c, 1))]), (_java_key_13 := b), jset(_java_obj_12, _java_key_13, jcast('int', (jget(_java_obj_12, _java_key_13) - 1))))[2]
        ((_java_obj_14 := diff[a]), (_java_key_15 := jcast('int', jadd(d, 1))), jset(_java_obj_14, _java_key_15, jcast('int', (jget(_java_obj_14, _java_key_15) - 1))))[2]

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


