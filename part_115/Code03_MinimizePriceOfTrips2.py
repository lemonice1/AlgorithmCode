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

# 最小化旅行的价格总和(tarjan方法求lca)
# 有n个节点形成一棵树，每个节点上有点权，再给定很多路径
# 每条路径有开始点和结束点，路径代价就是从开始点到结束点的点权和
# 所有路径的代价总和就是旅行的价格总和
# 你可以选择把某些点的点权减少一半，来降低旅行的价格总和
# 但是要求选择的点不能相邻
# 返回旅行的价格总和最少能是多少
# 测试链接 : https://leetcode.cn/problems/minimize-the-total-price-of-the-trips/
class Code03_MinimizePriceOfTrips2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'price': 'price', 'num': 'num', 'headEdge': 'headEdge', 'edgeNext': 'edgeNext', 'edgeTo': 'edgeTo', 'tcnt': 'tcnt', 'headQuery': 'headQuery', 'queryNext': 'queryNext', 'queryTo': 'queryTo', 'queryIndex': 'queryIndex', 'qcnt': 'qcnt', 'visited': 'visited', 'unionfind': 'unionfind', 'father': 'father', 'ans': 'ans', 'no': 'no', 'yes': 'yes'}
    # 题目给定点的编号从0号点开始，代码中调整成从1号点开始
    @staticmethod
    def minimumTotalPrice(n, es, ps, ts):
        n = jcast('int', n)
        Code03_MinimizePriceOfTrips2.build(n)
        i = jcast('int', 0)
        j = jcast('int', 1)
        while (i < n):
            Code03_MinimizePriceOfTrips2.price[j] = jcast('int', ps[i])
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        for edge in es:
            Code03_MinimizePriceOfTrips2.addEdge(jcast('int', jadd(edge[0], 1)), jcast('int', jadd(edge[1], 1)))
            Code03_MinimizePriceOfTrips2.addEdge(jcast('int', jadd(edge[1], 1)), jcast('int', jadd(edge[0], 1)))
        m = jcast('int', jget(ts, 'length'))
        i = jcast('int', 0)
        j = jcast('int', 1)
        while (i < m):
            Code03_MinimizePriceOfTrips2.addQuery(jcast('int', jadd(ts[i][0], 1)), jcast('int', jadd(ts[i][1], 1)), j)
            Code03_MinimizePriceOfTrips2.addQuery(jcast('int', jadd(ts[i][1], 1)), jcast('int', jadd(ts[i][0], 1)), j)
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        Code03_MinimizePriceOfTrips2.tarjan(1, 0)
        i = jcast('int', 0)
        j = jcast('int', 1)
        u = 0
        v = 0
        lca = 0
        lcafather = 0
        while (i < m):
            u = jcast('int', jcast('int', jadd(ts[i][0], 1)))
            v = jcast('int', jcast('int', jadd(ts[i][1], 1)))
            lca = jcast('int', Code03_MinimizePriceOfTrips2.ans[j])
            lcafather = jcast('int', Code03_MinimizePriceOfTrips2.father[lca])
            Code03_MinimizePriceOfTrips2.num[u] = jcast('int', (Code03_MinimizePriceOfTrips2.num[u] + 1))
            Code03_MinimizePriceOfTrips2.num[v] = jcast('int', (Code03_MinimizePriceOfTrips2.num[v] + 1))
            Code03_MinimizePriceOfTrips2.num[lca] = jcast('int', (Code03_MinimizePriceOfTrips2.num[lca] - 1))
            Code03_MinimizePriceOfTrips2.num[lcafather] = jcast('int', (Code03_MinimizePriceOfTrips2.num[lcafather] - 1))
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        Code03_MinimizePriceOfTrips2.dfs(1, 0)
        Code03_MinimizePriceOfTrips2.dp(1, 0)
        return jcast('int', jstatic('Math', 'min', Code03_MinimizePriceOfTrips2.no, Code03_MinimizePriceOfTrips2.yes))

    MAXN = 0
    MAXM = 0
    price = None
    num = None
    headEdge = None
    edgeNext = None
    edgeTo = None
    tcnt = 0
    headQuery = None
    queryNext = None
    queryTo = None
    queryIndex = None
    qcnt = 0
    visited = None
    unionfind = None
    father = None
    ans = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        jstatic('Arrays', 'fill', Code03_MinimizePriceOfTrips2.num, 1, jcast('int', jadd(n, 1)), 0)
        Code03_MinimizePriceOfTrips2.tcnt = jcast('int', jset(Code03_MinimizePriceOfTrips2, 'qcnt', 1))
        jstatic('Arrays', 'fill', Code03_MinimizePriceOfTrips2.headEdge, 1, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code03_MinimizePriceOfTrips2.headQuery, 1, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code03_MinimizePriceOfTrips2.visited, 1, jcast('int', jadd(n, 1)), False)
        i = jcast('int', 1)
        while (i <= n):
            Code03_MinimizePriceOfTrips2.unionfind[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code03_MinimizePriceOfTrips2.edgeNext[Code03_MinimizePriceOfTrips2.tcnt] = jcast('int', Code03_MinimizePriceOfTrips2.headEdge[u])
        Code03_MinimizePriceOfTrips2.edgeTo[Code03_MinimizePriceOfTrips2.tcnt] = jcast('int', v)
        jset(Code03_MinimizePriceOfTrips2.headEdge, u, ((_java_obj_1 := Code03_MinimizePriceOfTrips2), (_java_key_2 := 'tcnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def addQuery(u, v, i):
        u = jcast('int', u)
        v = jcast('int', v)
        i = jcast('int', i)
        Code03_MinimizePriceOfTrips2.queryNext[Code03_MinimizePriceOfTrips2.qcnt] = jcast('int', Code03_MinimizePriceOfTrips2.headQuery[u])
        Code03_MinimizePriceOfTrips2.queryTo[Code03_MinimizePriceOfTrips2.qcnt] = jcast('int', v)
        Code03_MinimizePriceOfTrips2.queryIndex[Code03_MinimizePriceOfTrips2.qcnt] = jcast('int', i)
        jset(Code03_MinimizePriceOfTrips2.headQuery, u, ((_java_obj_4 := Code03_MinimizePriceOfTrips2), (_java_key_5 := 'qcnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4])

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code03_MinimizePriceOfTrips2.unionfind[i]):
            jset(Code03_MinimizePriceOfTrips2.unionfind, i, Code03_MinimizePriceOfTrips2.find(Code03_MinimizePriceOfTrips2.unionfind[i]))
        return jcast('int', Code03_MinimizePriceOfTrips2.unionfind[i])

    @staticmethod
    def tarjan(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code03_MinimizePriceOfTrips2.visited[u] = jcast('boolean', True)
        e = jcast('int', Code03_MinimizePriceOfTrips2.headEdge[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_MinimizePriceOfTrips2.edgeTo[e])
            if (v != f):
                Code03_MinimizePriceOfTrips2.tarjan(v, u)
            e = jcast('int', Code03_MinimizePriceOfTrips2.edgeNext[e])
        e = jcast('int', Code03_MinimizePriceOfTrips2.headQuery[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_MinimizePriceOfTrips2.queryTo[e])
            if Code03_MinimizePriceOfTrips2.visited[v]:
                jset(Code03_MinimizePriceOfTrips2.ans, Code03_MinimizePriceOfTrips2.queryIndex[e], Code03_MinimizePriceOfTrips2.find(v))
            e = jcast('int', Code03_MinimizePriceOfTrips2.queryNext[e])
        Code03_MinimizePriceOfTrips2.unionfind[u] = jcast('int', f)
        Code03_MinimizePriceOfTrips2.father[u] = jcast('int', f)

    @staticmethod
    def dfs(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code03_MinimizePriceOfTrips2.headEdge[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_MinimizePriceOfTrips2.edgeTo[e])
            if (v != f):
                Code03_MinimizePriceOfTrips2.dfs(v, u)
            e = jcast('int', Code03_MinimizePriceOfTrips2.edgeNext[e])
        e = jcast('int', Code03_MinimizePriceOfTrips2.headEdge[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_MinimizePriceOfTrips2.edgeTo[e])
            if (v != f):
                Code03_MinimizePriceOfTrips2.num[u] = jcast('int', jcast('int', jadd(Code03_MinimizePriceOfTrips2.num[u], Code03_MinimizePriceOfTrips2.num[v])))
            e = jcast('int', Code03_MinimizePriceOfTrips2.edgeNext[e])

    no = 0
    yes = 0
    @staticmethod
    def dp(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        n = jcast('int', jcast('int', (Code03_MinimizePriceOfTrips2.price[u] * Code03_MinimizePriceOfTrips2.num[u])))
        y = jcast('int', jcast('int', (jcast('int', jdiv(Code03_MinimizePriceOfTrips2.price[u], 2)) * Code03_MinimizePriceOfTrips2.num[u])))
        e = jcast('int', Code03_MinimizePriceOfTrips2.headEdge[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_MinimizePriceOfTrips2.edgeTo[e])
            if (v != f):
                Code03_MinimizePriceOfTrips2.dp(v, u)
                n = jcast('int', jcast('int', jadd(n, jstatic('Math', 'min', Code03_MinimizePriceOfTrips2.no, Code03_MinimizePriceOfTrips2.yes))))
                y = jcast('int', jcast('int', jadd(y, Code03_MinimizePriceOfTrips2.no)))
            e = jcast('int', Code03_MinimizePriceOfTrips2.edgeNext[e])
        Code03_MinimizePriceOfTrips2.no = jcast('int', n)
        Code03_MinimizePriceOfTrips2.yes = jcast('int', y)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_MinimizePriceOfTrips2.MAXN = jcast('int', 51)
Code03_MinimizePriceOfTrips2.MAXM = jcast('int', 101)
Code03_MinimizePriceOfTrips2.price = jarray('int', [Code03_MinimizePriceOfTrips2.MAXN])
Code03_MinimizePriceOfTrips2.num = jarray('int', [Code03_MinimizePriceOfTrips2.MAXN])
Code03_MinimizePriceOfTrips2.headEdge = jarray('int', [Code03_MinimizePriceOfTrips2.MAXN])
Code03_MinimizePriceOfTrips2.edgeNext = jarray('int', [jcast('int', (Code03_MinimizePriceOfTrips2.MAXN << (1 & 31)))])
Code03_MinimizePriceOfTrips2.edgeTo = jarray('int', [jcast('int', (Code03_MinimizePriceOfTrips2.MAXN << (1 & 31)))])
Code03_MinimizePriceOfTrips2.tcnt = jcast('int', 0)
Code03_MinimizePriceOfTrips2.headQuery = jarray('int', [Code03_MinimizePriceOfTrips2.MAXN])
Code03_MinimizePriceOfTrips2.queryNext = jarray('int', [jcast('int', (Code03_MinimizePriceOfTrips2.MAXM << (1 & 31)))])
Code03_MinimizePriceOfTrips2.queryTo = jarray('int', [jcast('int', (Code03_MinimizePriceOfTrips2.MAXM << (1 & 31)))])
Code03_MinimizePriceOfTrips2.queryIndex = jarray('int', [jcast('int', (Code03_MinimizePriceOfTrips2.MAXM << (1 & 31)))])
Code03_MinimizePriceOfTrips2.qcnt = jcast('int', 0)
Code03_MinimizePriceOfTrips2.visited = jarray('boolean', [Code03_MinimizePriceOfTrips2.MAXN])
Code03_MinimizePriceOfTrips2.unionfind = jarray('int', [Code03_MinimizePriceOfTrips2.MAXN])
Code03_MinimizePriceOfTrips2.father = jarray('int', [Code03_MinimizePriceOfTrips2.MAXN])
Code03_MinimizePriceOfTrips2.ans = jarray('int', [Code03_MinimizePriceOfTrips2.MAXM])
Code03_MinimizePriceOfTrips2.no = jcast('int', 0)
Code03_MinimizePriceOfTrips2.yes = jcast('int', 0)
