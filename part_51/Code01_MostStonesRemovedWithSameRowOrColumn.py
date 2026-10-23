# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 移除最多的同行或同列石头
# n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头
# 如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头
# 给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置
# 返回 可以移除的石子 的最大数量。
# 测试链接 : https://leetcode.cn/problems/most-stones-removed-with-same-row-or-column/
class Code01_MostStonesRemovedWithSameRowOrColumn:
    __java_fields__ = {'rowFirst': 'rowFirst', 'colFirst': 'colFirst', 'MAXN': 'MAXN', 'father': 'father', 'sets': 'sets'}
    # key : 某行
    # value : 第一次遇到的石头编号
    rowFirst = None
    colFirst = None
    MAXN = 0
    father = None
    sets = 0
    @staticmethod
    def build(n):
        n = jcast('int', n)
        jcall(Code01_MostStonesRemovedWithSameRowOrColumn.rowFirst, 'clear')
        jcall(Code01_MostStonesRemovedWithSameRowOrColumn.colFirst, 'clear')
        i = jcast('int', 0)
        while (i < n):
            Code01_MostStonesRemovedWithSameRowOrColumn.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        Code01_MostStonesRemovedWithSameRowOrColumn.sets = jcast('int', n)

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code01_MostStonesRemovedWithSameRowOrColumn.father[i]):
            jset(Code01_MostStonesRemovedWithSameRowOrColumn.father, i, Code01_MostStonesRemovedWithSameRowOrColumn.find(Code01_MostStonesRemovedWithSameRowOrColumn.father[i]))
        return jcast('int', Code01_MostStonesRemovedWithSameRowOrColumn.father[i])

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code01_MostStonesRemovedWithSameRowOrColumn.find(x))
        fy = jcast('int', Code01_MostStonesRemovedWithSameRowOrColumn.find(y))
        if (fx != fy):
            Code01_MostStonesRemovedWithSameRowOrColumn.father[fx] = jcast('int', fy)
            Code01_MostStonesRemovedWithSameRowOrColumn.sets = jcast('int', (Code01_MostStonesRemovedWithSameRowOrColumn.sets - 1))

    @staticmethod
    def removeStones(stones):
        n = jcast('int', jget(stones, 'length'))
        Code01_MostStonesRemovedWithSameRowOrColumn.build(n)
        i = jcast('int', 0)
        while (i < n):
            row = jcast('int', stones[i][0])
            col = jcast('int', stones[i][1])
            if (not jcall(Code01_MostStonesRemovedWithSameRowOrColumn.rowFirst, 'containsKey', row)):
                jcall(Code01_MostStonesRemovedWithSameRowOrColumn.rowFirst, 'put', row, i)
            else:
                Code01_MostStonesRemovedWithSameRowOrColumn.union(i, jcall(Code01_MostStonesRemovedWithSameRowOrColumn.rowFirst, 'get', row))
            if (not jcall(Code01_MostStonesRemovedWithSameRowOrColumn.colFirst, 'containsKey', col)):
                jcall(Code01_MostStonesRemovedWithSameRowOrColumn.colFirst, 'put', col, i)
            else:
                Code01_MostStonesRemovedWithSameRowOrColumn.union(i, jcall(Code01_MostStonesRemovedWithSameRowOrColumn.colFirst, 'get', col))
            i = jcast('int', (i + 1))
        return jcast('int', jcast('int', (n - Code01_MostStonesRemovedWithSameRowOrColumn.sets)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_MostStonesRemovedWithSameRowOrColumn.rowFirst = jnew('HashMap')
Code01_MostStonesRemovedWithSameRowOrColumn.colFirst = jnew('HashMap')
Code01_MostStonesRemovedWithSameRowOrColumn.MAXN = jcast('int', 1001)
Code01_MostStonesRemovedWithSameRowOrColumn.father = jarray('int', [Code01_MostStonesRemovedWithSameRowOrColumn.MAXN])
Code01_MostStonesRemovedWithSameRowOrColumn.sets = jcast('int', 0)
