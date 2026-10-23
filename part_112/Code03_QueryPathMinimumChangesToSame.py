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

# 边权相等的最小修改次数
# 一棵树有n个节点，编号0 ~ n-1，每条边(u,v,w)表示从u到v有一条权重为w的边
# 一共有m条查询，每条查询(a,b)表示，a到b的最短路径中把所有边变成一种值需要修改几条边
# 返回每条查询的查询结果
# 1 <= n <= 10^4
# 1 <= m <= 2 * 10^4
# 0 <= u、v、a、b < n
# 1 <= w <= 26
# 测试链接 : https://leetcode.cn/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/
class Code03_QueryPathMinimumChangesToSame:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXW': 'MAXW', 'headEdge': 'headEdge', 'edgeNext': 'edgeNext', 'edgeTo': 'edgeTo', 'edgeValue': 'edgeValue', 'tcnt': 'tcnt', 'weightCnt': 'weightCnt', 'headQuery': 'headQuery', 'queryNext': 'queryNext', 'queryTo': 'queryTo', 'queryIndex': 'queryIndex', 'qcnt': 'qcnt', 'visited': 'visited', 'father': 'father', 'lca': 'lca'}
    MAXN = 0
    MAXM = 0
    MAXW = 0
    # 链式前向星建图
    headEdge = None
    edgeNext = None
    edgeTo = None
    edgeValue = None
    tcnt = 0
    # weightCnt[i][w] : 从头节点到i的路径中，权值为w的边有几条
    weightCnt = None
    # 以下所有的结构都是为了tarjan算法做准备
    headQuery = None
    queryNext = None
    queryTo = None
    queryIndex = None
    qcnt = 0
    visited = None
    father = None
    lca = None
    @staticmethod
    def minOperationsQueries(n, edges, queries):
        n = jcast('int', n)
        Code03_QueryPathMinimumChangesToSame.build(n)
        for edge in edges:
            Code03_QueryPathMinimumChangesToSame.addEdge(edge[0], edge[1], edge[2])
            Code03_QueryPathMinimumChangesToSame.addEdge(edge[1], edge[0], edge[2])
        # 从头节点到每个节点的边权值词频统计
        Code03_QueryPathMinimumChangesToSame.dfs(0, 0, jcast('int', (-1)))
        m = jcast('int', jget(queries, 'length'))
        i = jcast('int', 0)
        while (i < m):
            Code03_QueryPathMinimumChangesToSame.addQuery(queries[i][0], queries[i][1], i)
            Code03_QueryPathMinimumChangesToSame.addQuery(queries[i][1], queries[i][0], i)
            i = jcast('int', (i + 1))
        # 得到每个查询的最低公共祖先
        Code03_QueryPathMinimumChangesToSame.tarjan(0, jcast('int', (-1)))
        ans = jarray('int', [m])
        i = jcast('int', 0)
        a = 0
        b = 0
        c = 0
        while (i < m):
            a = jcast('int', queries[i][0])
            b = jcast('int', queries[i][1])
            c = jcast('int', Code03_QueryPathMinimumChangesToSame.lca[i])
            # 从a到b的路，所有权值的边一共多少条
            allCnt = jcast('int', 0)
            # 从a到b的路，权值重复最多的次数
            maxCnt = jcast('int', 0)
            # 所有权值枚举一遍
            w = jcast('int', 1)
            wcnt = 0
            while (w <= Code03_QueryPathMinimumChangesToSame.MAXW):
                wcnt = jcast('int', jcast('int', (jcast('int', jadd(Code03_QueryPathMinimumChangesToSame.weightCnt[a][w], Code03_QueryPathMinimumChangesToSame.weightCnt[b][w])) - jcast('int', (2 * Code03_QueryPathMinimumChangesToSame.weightCnt[c][w])))))
                maxCnt = jcast('int', jstatic('Math', 'max', maxCnt, wcnt))
                allCnt = jcast('int', jcast('int', jadd(allCnt, wcnt)))
                w = jcast('int', (w + 1))
            ans[i] = jcast('int', jcast('int', (allCnt - maxCnt)))
            i = jcast('int', (i + 1))
        return ans

    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code03_QueryPathMinimumChangesToSame.tcnt = jcast('int', jset(Code03_QueryPathMinimumChangesToSame, 'qcnt', 1))
        jstatic('Arrays', 'fill', Code03_QueryPathMinimumChangesToSame.headEdge, 0, n, 0)
        jstatic('Arrays', 'fill', Code03_QueryPathMinimumChangesToSame.headQuery, 0, n, 0)
        jstatic('Arrays', 'fill', Code03_QueryPathMinimumChangesToSame.visited, 0, n, False)
        i = jcast('int', 0)
        while (i < n):
            Code03_QueryPathMinimumChangesToSame.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code03_QueryPathMinimumChangesToSame.edgeNext[Code03_QueryPathMinimumChangesToSame.tcnt] = jcast('int', Code03_QueryPathMinimumChangesToSame.headEdge[u])
        Code03_QueryPathMinimumChangesToSame.edgeTo[Code03_QueryPathMinimumChangesToSame.tcnt] = jcast('int', v)
        Code03_QueryPathMinimumChangesToSame.edgeValue[Code03_QueryPathMinimumChangesToSame.tcnt] = jcast('int', w)
        jset(Code03_QueryPathMinimumChangesToSame.headEdge, u, ((_java_obj_1 := Code03_QueryPathMinimumChangesToSame), (_java_key_2 := 'tcnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # 当前来到u节点，父亲节点f，从f到u权重为w
    # 统计从头节点到u节点，每种权值的边有多少条
    # 信息存放在weightCnt[u][1..26]里
    @staticmethod
    def dfs(u, w, f):
        u = jcast('int', u)
        w = jcast('int', w)
        f = jcast('int', f)
        if (u == 0):
            jstatic('Arrays', 'fill', Code03_QueryPathMinimumChangesToSame.weightCnt[u], 0)
        else:
            i = jcast('int', 1)
            while (i <= Code03_QueryPathMinimumChangesToSame.MAXW):
                jset(Code03_QueryPathMinimumChangesToSame.weightCnt[u], i, Code03_QueryPathMinimumChangesToSame.weightCnt[f][i])
                i = jcast('int', (i + 1))
            ((_java_obj_4 := Code03_QueryPathMinimumChangesToSame.weightCnt[u]), (_java_key_5 := w), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]
        e = jcast('int', Code03_QueryPathMinimumChangesToSame.headEdge[u])
        while (e != 0):
            if (Code03_QueryPathMinimumChangesToSame.edgeTo[e] != f):
                Code03_QueryPathMinimumChangesToSame.dfs(Code03_QueryPathMinimumChangesToSame.edgeTo[e], Code03_QueryPathMinimumChangesToSame.edgeValue[e], u)
            e = jcast('int', Code03_QueryPathMinimumChangesToSame.edgeNext[e])

    @staticmethod
    def addQuery(u, v, i):
        u = jcast('int', u)
        v = jcast('int', v)
        i = jcast('int', i)
        Code03_QueryPathMinimumChangesToSame.queryNext[Code03_QueryPathMinimumChangesToSame.qcnt] = jcast('int', Code03_QueryPathMinimumChangesToSame.headQuery[u])
        Code03_QueryPathMinimumChangesToSame.queryTo[Code03_QueryPathMinimumChangesToSame.qcnt] = jcast('int', v)
        Code03_QueryPathMinimumChangesToSame.queryIndex[Code03_QueryPathMinimumChangesToSame.qcnt] = jcast('int', i)
        jset(Code03_QueryPathMinimumChangesToSame.headQuery, u, ((_java_obj_7 := Code03_QueryPathMinimumChangesToSame), (_java_key_8 := 'qcnt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4])

    # tarjan算法批量查询两点的最低公共祖先
    @staticmethod
    def tarjan(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code03_QueryPathMinimumChangesToSame.visited[u] = jcast('boolean', True)
        e = jcast('int', Code03_QueryPathMinimumChangesToSame.headEdge[u])
        while (e != 0):
            if (Code03_QueryPathMinimumChangesToSame.edgeTo[e] != f):
                Code03_QueryPathMinimumChangesToSame.tarjan(Code03_QueryPathMinimumChangesToSame.edgeTo[e], u)
            e = jcast('int', Code03_QueryPathMinimumChangesToSame.edgeNext[e])
        e = jcast('int', Code03_QueryPathMinimumChangesToSame.headQuery[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_QueryPathMinimumChangesToSame.queryTo[e])
            if Code03_QueryPathMinimumChangesToSame.visited[v]:
                jset(Code03_QueryPathMinimumChangesToSame.lca, Code03_QueryPathMinimumChangesToSame.queryIndex[e], Code03_QueryPathMinimumChangesToSame.find(v))
            e = jcast('int', Code03_QueryPathMinimumChangesToSame.queryNext[e])
        Code03_QueryPathMinimumChangesToSame.father[u] = jcast('int', f)

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code03_QueryPathMinimumChangesToSame.father[i]):
            jset(Code03_QueryPathMinimumChangesToSame.father, i, Code03_QueryPathMinimumChangesToSame.find(Code03_QueryPathMinimumChangesToSame.father[i]))
        return jcast('int', Code03_QueryPathMinimumChangesToSame.father[i])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_QueryPathMinimumChangesToSame.MAXN = jcast('int', 10001)
Code03_QueryPathMinimumChangesToSame.MAXM = jcast('int', 20001)
Code03_QueryPathMinimumChangesToSame.MAXW = jcast('int', 26)
Code03_QueryPathMinimumChangesToSame.headEdge = jarray('int', [Code03_QueryPathMinimumChangesToSame.MAXN])
Code03_QueryPathMinimumChangesToSame.edgeNext = jarray('int', [jcast('int', (Code03_QueryPathMinimumChangesToSame.MAXN << (1 & 31)))])
Code03_QueryPathMinimumChangesToSame.edgeTo = jarray('int', [jcast('int', (Code03_QueryPathMinimumChangesToSame.MAXN << (1 & 31)))])
Code03_QueryPathMinimumChangesToSame.edgeValue = jarray('int', [jcast('int', (Code03_QueryPathMinimumChangesToSame.MAXN << (1 & 31)))])
Code03_QueryPathMinimumChangesToSame.tcnt = jcast('int', 0)
Code03_QueryPathMinimumChangesToSame.weightCnt = jarray('int', [Code03_QueryPathMinimumChangesToSame.MAXN, jcast('int', jadd(Code03_QueryPathMinimumChangesToSame.MAXW, 1))])
Code03_QueryPathMinimumChangesToSame.headQuery = jarray('int', [Code03_QueryPathMinimumChangesToSame.MAXN])
Code03_QueryPathMinimumChangesToSame.queryNext = jarray('int', [jcast('int', (Code03_QueryPathMinimumChangesToSame.MAXM << (1 & 31)))])
Code03_QueryPathMinimumChangesToSame.queryTo = jarray('int', [jcast('int', (Code03_QueryPathMinimumChangesToSame.MAXM << (1 & 31)))])
Code03_QueryPathMinimumChangesToSame.queryIndex = jarray('int', [jcast('int', (Code03_QueryPathMinimumChangesToSame.MAXM << (1 & 31)))])
Code03_QueryPathMinimumChangesToSame.qcnt = jcast('int', 0)
Code03_QueryPathMinimumChangesToSame.visited = jarray('boolean', [Code03_QueryPathMinimumChangesToSame.MAXN])
Code03_QueryPathMinimumChangesToSame.father = jarray('int', [Code03_QueryPathMinimumChangesToSame.MAXN])
Code03_QueryPathMinimumChangesToSame.lca = jarray('int', [Code03_QueryPathMinimumChangesToSame.MAXM])
