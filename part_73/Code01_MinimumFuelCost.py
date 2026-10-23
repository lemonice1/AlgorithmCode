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

# 到达首都的最少油耗
# 给你一棵 n 个节点的树（一个无向、连通、无环图）
# 每个节点表示一个城市，编号从 0 到 n - 1 ，且恰好有 n - 1 条路
# 0 是首都。给你一个二维整数数组 roads
# 其中 roads[i] = [ai, bi] ，表示城市 ai 和 bi 之间有一条 双向路
# 每个城市里有一个代表，他们都要去首都参加一个会议
# 每座城市里有一辆车。给你一个整数 seats 表示每辆车里面座位的数目
# 城市里的代表可以选择乘坐所在城市的车，或者乘坐其他城市的车
# 相邻城市之间一辆车的油耗是一升汽油
# 请你返回到达首都最少需要多少升汽油
# 测试链接 : https://leetcode.cn/problems/minimum-fuel-cost-to-report-to-the-capital/
class Code01_MinimumFuelCost:
    __java_fields__ = {}
    @staticmethod
    def minimumFuelCost(roads, seats):
        seats = jcast('int', seats)
        n = jcast('int', jcast('int', jadd(jget(roads, 'length'), 1)))
        graph = jnew('ArrayList')
        i = jcast('int', 0)
        while (i < n):
            jcall(graph, 'add', jnew('ArrayList'))
            i = jcast('int', (i + 1))
        for r in roads:
            jcall(jcall(graph, 'get', r[0]), 'add', r[1])
            jcall(jcall(graph, 'get', r[1]), 'add', r[0])
        size = jarray('int', [n])
        cost = jarray('long', [n])
        Code01_MinimumFuelCost.f(graph, seats, 0, jcast('int', (-1)), size, cost)
        return jcast('long', cost[0])

    # 根据图，当前来到u，u的父节点是p
    # 遍历完成后，请填好size[u]、cost[u]
    @staticmethod
    def f(graph, seats, u, p, size, cost):
        seats = jcast('int', seats)
        u = jcast('int', u)
        p = jcast('int', p)
        size[u] = jcast('int', 1)
        for v in jcall(graph, 'get', u):
            if (v != p):
                Code01_MinimumFuelCost.f(graph, seats, v, u, size, cost)
                size[u] = jcast('int', jcast('int', jadd(size[u], size[v])))
                cost[u] = jcast('long', jcast('long', jadd(cost[u], cost[v])))
                # a/b向上取整，可以写成(a+b-1)/b
                # (size[v]+seats-1) / seats = size[v] / seats 向上取整
                cost[u] = jcast('long', jcast('long', jadd(cost[u], jcast('int', jdiv(jcast('int', (jcast('int', jadd(size[v], seats)) - 1)), seats)))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


