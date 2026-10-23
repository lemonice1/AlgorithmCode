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

# 水资源分配优化
# 村里面一共有 n 栋房子。我们希望通过建造水井和铺设管道来为所有房子供水。
# 对于每个房子 i，我们有两种可选的供水方案：一种是直接在房子内建造水井
# 成本为 wells[i - 1] （注意 -1 ，因为 索引从0开始 ）
# 另一种是从另一口井铺设管道引水，数组 pipes 给出了在房子间铺设管道的成本，
# 其中每个 pipes[j] = [house1j, house2j, costj]
# 代表用管道将 house1j 和 house2j连接在一起的成本。连接是双向的。
# 请返回 为所有房子都供水的最低总成本
# 测试链接 : https://leetcode.cn/problems/optimize-water-distribution-in-a-village/
class Code03_OptimizeWaterDistribution:
    __java_fields__ = {'MAXN': 'MAXN', 'edges': 'edges', 'cnt': 'cnt', 'father': 'father'}
    @staticmethod
    def minCostToSupplyWater(n, wells, pipes):
        n = jcast('int', n)
        Code03_OptimizeWaterDistribution.build(n)
        i = jcast('int', 0)
        while (i < n):
            # wells : 100   30
            # 0(1)  1(2)
            jset(Code03_OptimizeWaterDistribution.edges[Code03_OptimizeWaterDistribution.cnt], 0, 0)
            jset(Code03_OptimizeWaterDistribution.edges[Code03_OptimizeWaterDistribution.cnt], 1, jcast('int', jadd(i, 1)))
            jset(Code03_OptimizeWaterDistribution.edges[Code03_OptimizeWaterDistribution.cnt], 2, wells[i])
            i = jcast('int', (i + 1))
            Code03_OptimizeWaterDistribution.cnt = jcast('int', (Code03_OptimizeWaterDistribution.cnt + 1))
        i = jcast('int', 0)
        while (i < jget(pipes, 'length')):
            jset(Code03_OptimizeWaterDistribution.edges[Code03_OptimizeWaterDistribution.cnt], 0, pipes[i][0])
            jset(Code03_OptimizeWaterDistribution.edges[Code03_OptimizeWaterDistribution.cnt], 1, pipes[i][1])
            jset(Code03_OptimizeWaterDistribution.edges[Code03_OptimizeWaterDistribution.cnt], 2, pipes[i][2])
            i = jcast('int', (i + 1))
            Code03_OptimizeWaterDistribution.cnt = jcast('int', (Code03_OptimizeWaterDistribution.cnt + 1))
        jstatic('Arrays', 'sort', Code03_OptimizeWaterDistribution.edges, 0, Code03_OptimizeWaterDistribution.cnt, (lambda a, b: (a[2] - b[2])))
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < Code03_OptimizeWaterDistribution.cnt):
            if Code03_OptimizeWaterDistribution.union(Code03_OptimizeWaterDistribution.edges[i][0], Code03_OptimizeWaterDistribution.edges[i][1]):
                ans = jcast('int', jcast('int', jadd(ans, Code03_OptimizeWaterDistribution.edges[i][2])))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    MAXN = 0
    edges = None
    cnt = 0
    father = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code03_OptimizeWaterDistribution.cnt = jcast('int', 0)
        i = jcast('int', 0)
        while (i <= n):
            Code03_OptimizeWaterDistribution.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code03_OptimizeWaterDistribution.father[i]):
            jset(Code03_OptimizeWaterDistribution.father, i, Code03_OptimizeWaterDistribution.find(Code03_OptimizeWaterDistribution.father[i]))
        return jcast('int', Code03_OptimizeWaterDistribution.father[i])

    # 如果x和y，原本是一个集合，返回false
    # 如果x和y，不是一个集合，合并之后后返回true
    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code03_OptimizeWaterDistribution.find(x))
        fy = jcast('int', Code03_OptimizeWaterDistribution.find(y))
        if (fx != fy):
            Code03_OptimizeWaterDistribution.father[fx] = jcast('int', fy)
            return jcast('boolean', True)
        else:
            return jcast('boolean', False)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_OptimizeWaterDistribution.MAXN = jcast('int', 10010)
Code03_OptimizeWaterDistribution.edges = jarray('int', [jcast('int', (Code03_OptimizeWaterDistribution.MAXN << (1 & 31))), 3])
Code03_OptimizeWaterDistribution.cnt = jcast('int', 0)
Code03_OptimizeWaterDistribution.father = jarray('int', [Code03_OptimizeWaterDistribution.MAXN])
