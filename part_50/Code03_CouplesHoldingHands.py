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

# 情侣牵手
# n对情侣坐在连续排列的 2n 个座位上，想要牵到对方的手
# 人和座位由一个整数数组 row 表示，其中 row[i] 是坐在第 i 个座位上的人的ID
# 情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2n-2, 2n-1)
# 返回 最少交换座位的次数，以便每对情侣可以并肩坐在一起
# 每次交换可选择任意两人，让他们站起来交换座位
# 测试链接 : https://leetcode.cn/problems/couples-holding-hands/
class Code03_CouplesHoldingHands:
    __java_fields__ = {'MAXN': 'MAXN', 'father': 'father', 'sets': 'sets'}
    @staticmethod
    def minSwapsCouples(row):
        n = jcast('int', jget(row, 'length'))
        Code03_CouplesHoldingHands.build(jcast('int', jdiv(n, 2)))
        i = jcast('int', 0)
        while (i < n):
            Code03_CouplesHoldingHands.union(jcast('int', jdiv(row[i], 2)), jcast('int', jdiv(row[jcast('int', jadd(i, 1))], 2)))
            i = jcast('int', jcast('int', jadd(i, 2)))
        return jcast('int', jcast('int', (jcast('int', jdiv(n, 2)) - Code03_CouplesHoldingHands.sets)))

    MAXN = 0
    father = None
    sets = 0
    @staticmethod
    def build(m):
        m = jcast('int', m)
        i = jcast('int', 0)
        while (i < m):
            Code03_CouplesHoldingHands.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        Code03_CouplesHoldingHands.sets = jcast('int', m)

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code03_CouplesHoldingHands.father[i]):
            jset(Code03_CouplesHoldingHands.father, i, Code03_CouplesHoldingHands.find(Code03_CouplesHoldingHands.father[i]))
        return jcast('int', Code03_CouplesHoldingHands.father[i])

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code03_CouplesHoldingHands.find(x))
        fy = jcast('int', Code03_CouplesHoldingHands.find(y))
        if (fx != fy):
            Code03_CouplesHoldingHands.father[fx] = jcast('int', fy)
            Code03_CouplesHoldingHands.sets = jcast('int', (Code03_CouplesHoldingHands.sets - 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_CouplesHoldingHands.MAXN = jcast('int', 31)
Code03_CouplesHoldingHands.father = jarray('int', [Code03_CouplesHoldingHands.MAXN])
Code03_CouplesHoldingHands.sets = jcast('int', 0)
