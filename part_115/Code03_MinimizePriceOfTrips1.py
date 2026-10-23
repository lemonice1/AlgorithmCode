# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最小化旅行的价格总和(倍增方法求lca)
# 有n个节点形成一棵树，每个节点上有点权，再给定很多路径
# 每条路径有开始点和结束点，路径代价就是从开始点到结束点的点权和
# 所有路径的代价总和就是旅行的价格总和
# 你可以选择把某些点的点权减少一半，来降低旅行的价格总和
# 但是要求选择的点不能相邻
# 返回旅行的价格总和最少能是多少
# 测试链接 : https://leetcode.cn/problems/minimize-the-total-price-of-the-trips/
class Code03_MinimizePriceOfTrips1:
    __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'power': 'power', 'price': 'price', 'num': 'num', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'deep': 'deep', 'stjump': 'stjump', 'no': 'no', 'yes': 'yes'}
    # 题目给定点的编号从0号点开始，代码中调整成从1号点开始
    @staticmethod
    def minimumTotalPrice(n, es, ps, ts):
        n = jcast('int', n)
        Code03_MinimizePriceOfTrips1.build(n)
        i = jcast('int', 0)
        j = jcast('int', 1)
        while (i < n):
            Code03_MinimizePriceOfTrips1.price[j] = jcast('int', ps[i])
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        for edge in es:
            Code03_MinimizePriceOfTrips1.addEdge(jcast('int', jadd(edge[0], 1)), jcast('int', jadd(edge[1], 1)))
            Code03_MinimizePriceOfTrips1.addEdge(jcast('int', jadd(edge[1], 1)), jcast('int', jadd(edge[0], 1)))
        Code03_MinimizePriceOfTrips1.dfs1(1, 0)
        u = 0
        v = 0
        lca = 0
        lcafather = 0
        for trip in ts:
            u = jcast('int', jcast('int', jadd(trip[0], 1)))
            v = jcast('int', jcast('int', jadd(trip[1], 1)))
            lca = jcast('int', Code03_MinimizePriceOfTrips1.lca(u, v))
            lcafather = jcast('int', Code03_MinimizePriceOfTrips1.stjump[lca][0])
            Code03_MinimizePriceOfTrips1.num[u] = jcast('int', (Code03_MinimizePriceOfTrips1.num[u] + 1))
            Code03_MinimizePriceOfTrips1.num[v] = jcast('int', (Code03_MinimizePriceOfTrips1.num[v] + 1))
            Code03_MinimizePriceOfTrips1.num[lca] = jcast('int', (Code03_MinimizePriceOfTrips1.num[lca] - 1))
            Code03_MinimizePriceOfTrips1.num[lcafather] = jcast('int', (Code03_MinimizePriceOfTrips1.num[lcafather] - 1))
        Code03_MinimizePriceOfTrips1.dfs2(1, 0)
        Code03_MinimizePriceOfTrips1.dp(1, 0)
        return jcast('int', jstatic('Math', 'min', Code03_MinimizePriceOfTrips1.no, Code03_MinimizePriceOfTrips1.yes))

    MAXN = 0
    LIMIT = 0
    power = 0
    @staticmethod
    def log2(n):
        n = jcast('int', n)
        ans = jcast('int', 0)
        while (jcast('int', (1 << (ans & 31))) <= jcast('int', (n >> (1 & 31)))):
            ans = jcast('int', (ans + 1))
        return jcast('int', ans)

    price = None
    num = None
    head = None
    next = None
    to = None
    cnt = 0
    deep = None
    stjump = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code03_MinimizePriceOfTrips1.power = jcast('int', Code03_MinimizePriceOfTrips1.log2(n))
        jstatic('Arrays', 'fill', Code03_MinimizePriceOfTrips1.num, 1, jcast('int', jadd(n, 1)), 0)
        Code03_MinimizePriceOfTrips1.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code03_MinimizePriceOfTrips1.head, 1, jcast('int', jadd(n, 1)), 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code03_MinimizePriceOfTrips1.next[Code03_MinimizePriceOfTrips1.cnt] = jcast('int', Code03_MinimizePriceOfTrips1.head[u])
        Code03_MinimizePriceOfTrips1.to[Code03_MinimizePriceOfTrips1.cnt] = jcast('int', v)
        jset(Code03_MinimizePriceOfTrips1.head, u, ((_java_obj_1 := Code03_MinimizePriceOfTrips1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code03_MinimizePriceOfTrips1.deep[u] = jcast('int', jcast('int', jadd(Code03_MinimizePriceOfTrips1.deep[f], 1)))
        jset(Code03_MinimizePriceOfTrips1.stjump[u], 0, f)
        p = jcast('int', 1)
        while (p <= Code03_MinimizePriceOfTrips1.power):
            jset(Code03_MinimizePriceOfTrips1.stjump[u], p, Code03_MinimizePriceOfTrips1.stjump[Code03_MinimizePriceOfTrips1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code03_MinimizePriceOfTrips1.head[u])
        while (e != 0):
            if (Code03_MinimizePriceOfTrips1.to[e] != f):
                Code03_MinimizePriceOfTrips1.dfs1(Code03_MinimizePriceOfTrips1.to[e], u)
            e = jcast('int', Code03_MinimizePriceOfTrips1.next[e])

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code03_MinimizePriceOfTrips1.deep[a] < Code03_MinimizePriceOfTrips1.deep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', Code03_MinimizePriceOfTrips1.power)
        while (p >= 0):
            if (Code03_MinimizePriceOfTrips1.deep[Code03_MinimizePriceOfTrips1.stjump[a][p]] >= Code03_MinimizePriceOfTrips1.deep[b]):
                a = jcast('int', Code03_MinimizePriceOfTrips1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', Code03_MinimizePriceOfTrips1.power)
        while (p >= 0):
            if (Code03_MinimizePriceOfTrips1.stjump[a][p] != Code03_MinimizePriceOfTrips1.stjump[b][p]):
                a = jcast('int', Code03_MinimizePriceOfTrips1.stjump[a][p])
                b = jcast('int', Code03_MinimizePriceOfTrips1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code03_MinimizePriceOfTrips1.stjump[a][0])

    @staticmethod
    def dfs2(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code03_MinimizePriceOfTrips1.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_MinimizePriceOfTrips1.to[e])
            if (v != f):
                Code03_MinimizePriceOfTrips1.dfs2(v, u)
            e = jcast('int', Code03_MinimizePriceOfTrips1.next[e])
        e = jcast('int', Code03_MinimizePriceOfTrips1.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_MinimizePriceOfTrips1.to[e])
            if (v != f):
                Code03_MinimizePriceOfTrips1.num[u] = jcast('int', jcast('int', jadd(Code03_MinimizePriceOfTrips1.num[u], Code03_MinimizePriceOfTrips1.num[v])))
            e = jcast('int', Code03_MinimizePriceOfTrips1.next[e])

    no = 0
    yes = 0
    @staticmethod
    def dp(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        n = jcast('int', jcast('int', (Code03_MinimizePriceOfTrips1.price[u] * Code03_MinimizePriceOfTrips1.num[u])))
        y = jcast('int', jcast('int', (jcast('int', jdiv(Code03_MinimizePriceOfTrips1.price[u], 2)) * Code03_MinimizePriceOfTrips1.num[u])))
        e = jcast('int', Code03_MinimizePriceOfTrips1.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_MinimizePriceOfTrips1.to[e])
            if (v != f):
                Code03_MinimizePriceOfTrips1.dp(v, u)
                n = jcast('int', jcast('int', jadd(n, jstatic('Math', 'min', Code03_MinimizePriceOfTrips1.no, Code03_MinimizePriceOfTrips1.yes))))
                y = jcast('int', jcast('int', jadd(y, Code03_MinimizePriceOfTrips1.no)))
            e = jcast('int', Code03_MinimizePriceOfTrips1.next[e])
        Code03_MinimizePriceOfTrips1.no = jcast('int', n)
        Code03_MinimizePriceOfTrips1.yes = jcast('int', y)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_MinimizePriceOfTrips1.MAXN = jcast('int', 51)
Code03_MinimizePriceOfTrips1.LIMIT = jcast('int', 6)
Code03_MinimizePriceOfTrips1.power = jcast('int', 0)
Code03_MinimizePriceOfTrips1.price = jarray('int', [Code03_MinimizePriceOfTrips1.MAXN])
Code03_MinimizePriceOfTrips1.num = jarray('int', [Code03_MinimizePriceOfTrips1.MAXN])
Code03_MinimizePriceOfTrips1.head = jarray('int', [Code03_MinimizePriceOfTrips1.MAXN])
Code03_MinimizePriceOfTrips1.next = jarray('int', [jcast('int', (Code03_MinimizePriceOfTrips1.MAXN << (1 & 31)))])
Code03_MinimizePriceOfTrips1.to = jarray('int', [jcast('int', (Code03_MinimizePriceOfTrips1.MAXN << (1 & 31)))])
Code03_MinimizePriceOfTrips1.cnt = jcast('int', 0)
Code03_MinimizePriceOfTrips1.deep = jarray('int', [Code03_MinimizePriceOfTrips1.MAXN])
Code03_MinimizePriceOfTrips1.stjump = jarray('int', [Code03_MinimizePriceOfTrips1.MAXN, Code03_MinimizePriceOfTrips1.LIMIT])
Code03_MinimizePriceOfTrips1.no = jcast('int', 0)
Code03_MinimizePriceOfTrips1.yes = jcast('int', 0)
