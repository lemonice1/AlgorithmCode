# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 运输计划，Python递归版
# 有n个节点，给定n-1条边使其连接成一棵树，每条边有正数边权
# 给定很多运输计划，每个运输计划(a,b)表示从a去往b
# 每个运输计划的代价就是沿途边权和，运输计划之间完全互不干扰
# 你只能选择一条边，将其边权变成0
# 你的目的是让所有运输计划代价的最大值尽量小
# 返回所有运输计划代价的最大值最小能是多少
# 测试链接 : https://www.luogu.com.cn/problem/P2680
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
# 对应实现可参考 Code05_TransportPlan3.py
class Code05_TransportPlan1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'num': 'num', 'headEdge': 'headEdge', 'edgeNext': 'edgeNext', 'edgeTo': 'edgeTo', 'edgeWeight': 'edgeWeight', 'tcnt': 'tcnt', 'headQuery': 'headQuery', 'queryNext': 'queryNext', 'queryTo': 'queryTo', 'queryIndex': 'queryIndex', 'qcnt': 'qcnt', 'visited': 'visited', 'unionfind': 'unionfind', 'quesu': 'quesu', 'quesv': 'quesv', 'distance': 'distance', 'lca': 'lca', 'cost': 'cost', 'maxCost': 'maxCost', 'atLeast': 'atLeast', 'beyond': 'beyond'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    # num[i] : i节点和其父节点的边，有多少代价>=limit的运输计划用到
    num = None
    # 链式前向星建图需要
    headEdge = None
    edgeNext = None
    edgeTo = None
    edgeWeight = None
    tcnt = 0
    # tarjan算法需要
    headQuery = None
    queryNext = None
    queryTo = None
    queryIndex = None
    qcnt = 0
    visited = None
    unionfind = None
    quesu = None
    quesv = None
    # distance[i] : 头节点到i号点的距离，tarjan算法过程中更新
    distance = None
    # lca[i] : 第i号运输计划的两端点lca，tarjan算法过程中更新
    lca = None
    # cost[i] : 第i号运输计划代价是多少，tarjan算法过程中更新
    cost = None
    # 所有运输计划的最大代价，tarjan算法过程中更新
    maxCost = 0
    @staticmethod
    def build():
        Code05_TransportPlan1.tcnt = jcast('int', jset(Code05_TransportPlan1, 'qcnt', 1))
        jstatic('Arrays', 'fill', Code05_TransportPlan1.headEdge, 1, jcast('int', jadd(Code05_TransportPlan1.n, 1)), 0)
        jstatic('Arrays', 'fill', Code05_TransportPlan1.headQuery, 1, jcast('int', jadd(Code05_TransportPlan1.n, 1)), 0)
        jstatic('Arrays', 'fill', Code05_TransportPlan1.visited, 1, jcast('int', jadd(Code05_TransportPlan1.n, 1)), False)
        i = jcast('int', 1)
        while (i <= Code05_TransportPlan1.n):
            Code05_TransportPlan1.unionfind[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        Code05_TransportPlan1.maxCost = jcast('int', 0)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code05_TransportPlan1.edgeNext[Code05_TransportPlan1.tcnt] = jcast('int', Code05_TransportPlan1.headEdge[u])
        Code05_TransportPlan1.edgeTo[Code05_TransportPlan1.tcnt] = jcast('int', v)
        Code05_TransportPlan1.edgeWeight[Code05_TransportPlan1.tcnt] = jcast('int', w)
        jset(Code05_TransportPlan1.headEdge, u, ((_java_obj_1 := Code05_TransportPlan1), (_java_key_2 := 'tcnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def addQuery(u, v, i):
        u = jcast('int', u)
        v = jcast('int', v)
        i = jcast('int', i)
        Code05_TransportPlan1.queryNext[Code05_TransportPlan1.qcnt] = jcast('int', Code05_TransportPlan1.headQuery[u])
        Code05_TransportPlan1.queryTo[Code05_TransportPlan1.qcnt] = jcast('int', v)
        Code05_TransportPlan1.queryIndex[Code05_TransportPlan1.qcnt] = jcast('int', i)
        jset(Code05_TransportPlan1.headQuery, u, ((_java_obj_4 := Code05_TransportPlan1), (_java_key_5 := 'qcnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4])

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code05_TransportPlan1.unionfind[i]):
            jset(Code05_TransportPlan1.unionfind, i, Code05_TransportPlan1.find(Code05_TransportPlan1.unionfind[i]))
        return jcast('int', Code05_TransportPlan1.unionfind[i])

    @staticmethod
    def tarjan(u, f, w):
        u = jcast('int', u)
        f = jcast('int', f)
        w = jcast('int', w)
        Code05_TransportPlan1.visited[u] = jcast('boolean', True)
        Code05_TransportPlan1.distance[u] = jcast('int', jcast('int', jadd(Code05_TransportPlan1.distance[f], w)))
        e = jcast('int', Code05_TransportPlan1.headEdge[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code05_TransportPlan1.edgeTo[e])
            if (v != f):
                Code05_TransportPlan1.tarjan(v, u, Code05_TransportPlan1.edgeWeight[e])
            e = jcast('int', Code05_TransportPlan1.edgeNext[e])
        e = jcast('int', Code05_TransportPlan1.headQuery[u])
        v = 0
        i = 0
        while (e != 0):
            v = jcast('int', Code05_TransportPlan1.queryTo[e])
            if Code05_TransportPlan1.visited[v]:
                i = jcast('int', Code05_TransportPlan1.queryIndex[e])
                jset(Code05_TransportPlan1.lca, i, Code05_TransportPlan1.find(v))
                Code05_TransportPlan1.cost[i] = jcast('int', jcast('int', (jcast('int', jadd(Code05_TransportPlan1.distance[u], Code05_TransportPlan1.distance[v])) - jcast('int', (2 * Code05_TransportPlan1.distance[Code05_TransportPlan1.lca[i]])))))
                Code05_TransportPlan1.maxCost = jcast('int', jstatic('Math', 'max', Code05_TransportPlan1.maxCost, Code05_TransportPlan1.cost[i]))
            e = jcast('int', Code05_TransportPlan1.queryNext[e])
        Code05_TransportPlan1.unionfind[u] = jcast('int', f)

    # 只能把一条边的权值变成0
    # 还要求每个运输计划的代价都要<=limit
    # 返回能不能做到
    @staticmethod
    def f(limit):
        limit = jcast('int', limit)
        Code05_TransportPlan1.atLeast = jcast('int', jcast('int', (Code05_TransportPlan1.maxCost - limit)))
        jstatic('Arrays', 'fill', Code05_TransportPlan1.num, 1, jcast('int', jadd(Code05_TransportPlan1.n, 1)), 0)
        Code05_TransportPlan1.beyond = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code05_TransportPlan1.m):
            if (Code05_TransportPlan1.cost[i] > limit):
                ((_java_obj_7 := Code05_TransportPlan1.num), (_java_key_8 := Code05_TransportPlan1.quesu[i]), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]
                ((_java_obj_10 := Code05_TransportPlan1.num), (_java_key_11 := Code05_TransportPlan1.quesv[i]), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]
                ((_java_obj_13 := Code05_TransportPlan1.num), (_java_key_14 := Code05_TransportPlan1.lca[i]), jset(_java_obj_13, _java_key_14, jcast('int', (jget(_java_obj_13, _java_key_14) - 2))))[2]
                Code05_TransportPlan1.beyond = jcast('int', (Code05_TransportPlan1.beyond + 1))
            i = jcast('int', (i + 1))
        return jcast('boolean', ((Code05_TransportPlan1.beyond == 0) or Code05_TransportPlan1.dfs(1, 0, 0)))

    # 至少要减少多少边权
    atLeast = 0
    # 超过要求的运输计划有几个
    beyond = 0
    @staticmethod
    def dfs(u, f, w):
        u = jcast('int', u)
        f = jcast('int', f)
        w = jcast('int', w)
        e = jcast('int', Code05_TransportPlan1.headEdge[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code05_TransportPlan1.edgeTo[e])
            if (v != f):
                if Code05_TransportPlan1.dfs(v, u, Code05_TransportPlan1.edgeWeight[e]):
                    return jcast('boolean', True)
            e = jcast('int', Code05_TransportPlan1.edgeNext[e])
        e = jcast('int', Code05_TransportPlan1.headEdge[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code05_TransportPlan1.edgeTo[e])
            if (v != f):
                Code05_TransportPlan1.num[u] = jcast('int', jcast('int', jadd(Code05_TransportPlan1.num[u], Code05_TransportPlan1.num[v])))
            e = jcast('int', Code05_TransportPlan1.edgeNext[e])
        return jcast('boolean', ((Code05_TransportPlan1.num[u] == Code05_TransportPlan1.beyond) and (w >= Code05_TransportPlan1.atLeast)))

    @staticmethod
    def compute():
        Code05_TransportPlan1.tarjan(1, 0, 0)
        l = jcast('int', 0)
        r = jcast('int', Code05_TransportPlan1.maxCost)
        mid = 0
        ans = jcast('int', 0)
        while (l <= r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if Code05_TransportPlan1.f(mid):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_TransportPlan1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code05_TransportPlan1.build()
        jcall(in_, 'nextToken')
        Code05_TransportPlan1.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code05_TransportPlan1.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            w = jcast('int', jcast('int', jget(in_, 'nval')))
            Code05_TransportPlan1.addEdge(u, v, w)
            Code05_TransportPlan1.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code05_TransportPlan1.m):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code05_TransportPlan1.quesu[i] = jcast('int', u)
            Code05_TransportPlan1.quesv[i] = jcast('int', v)
            Code05_TransportPlan1.addQuery(u, v, i)
            Code05_TransportPlan1.addQuery(v, u, i)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code05_TransportPlan1.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_TransportPlan1.MAXN = jcast('int', 300001)
Code05_TransportPlan1.MAXM = jcast('int', 300001)
Code05_TransportPlan1.n = jcast('int', 0)
Code05_TransportPlan1.m = jcast('int', 0)
Code05_TransportPlan1.num = jarray('int', [Code05_TransportPlan1.MAXN])
Code05_TransportPlan1.headEdge = jarray('int', [Code05_TransportPlan1.MAXN])
Code05_TransportPlan1.edgeNext = jarray('int', [jcast('int', (Code05_TransportPlan1.MAXN << (1 & 31)))])
Code05_TransportPlan1.edgeTo = jarray('int', [jcast('int', (Code05_TransportPlan1.MAXN << (1 & 31)))])
Code05_TransportPlan1.edgeWeight = jarray('int', [jcast('int', (Code05_TransportPlan1.MAXN << (1 & 31)))])
Code05_TransportPlan1.tcnt = jcast('int', 0)
Code05_TransportPlan1.headQuery = jarray('int', [Code05_TransportPlan1.MAXN])
Code05_TransportPlan1.queryNext = jarray('int', [jcast('int', (Code05_TransportPlan1.MAXM << (1 & 31)))])
Code05_TransportPlan1.queryTo = jarray('int', [jcast('int', (Code05_TransportPlan1.MAXM << (1 & 31)))])
Code05_TransportPlan1.queryIndex = jarray('int', [jcast('int', (Code05_TransportPlan1.MAXM << (1 & 31)))])
Code05_TransportPlan1.qcnt = jcast('int', 0)
Code05_TransportPlan1.visited = jarray('boolean', [Code05_TransportPlan1.MAXN])
Code05_TransportPlan1.unionfind = jarray('int', [Code05_TransportPlan1.MAXN])
Code05_TransportPlan1.quesu = jarray('int', [Code05_TransportPlan1.MAXM])
Code05_TransportPlan1.quesv = jarray('int', [Code05_TransportPlan1.MAXM])
Code05_TransportPlan1.distance = jarray('int', [Code05_TransportPlan1.MAXN])
Code05_TransportPlan1.lca = jarray('int', [Code05_TransportPlan1.MAXM])
Code05_TransportPlan1.cost = jarray('int', [Code05_TransportPlan1.MAXM])
Code05_TransportPlan1.maxCost = jcast('int', 0)
Code05_TransportPlan1.atLeast = jcast('int', 0)
Code05_TransportPlan1.beyond = jcast('int', 0)

if __name__ == '__main__':
    Code05_TransportPlan1.main([])
