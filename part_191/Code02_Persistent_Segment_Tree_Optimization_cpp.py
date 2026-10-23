# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 主席树优化建图，Python版
# 点的编号范围1~n，点权范围1~v，初始时袋子为空，没有任何边，实现如下方法
# add(x, xv)，编号为x、点权为xv的点进入袋子，该编号已经入袋则忽略
# rangeToX(l, r, x, w)，袋中点权范围l~r的每个点，向点x连边权为w的边
# xToRange(x, l, r, w)，点x向袋中点权范围l~r的每个点，连边权为w的边
# rangeToRange(l1, r1, l2, r2, w)，范围向范围连边，具体含义如下
# 袋中点权l1~r1的每个点，向袋中点权l2~r2的每个点，连边权为w的边
# 建好图之后可以测试图的任何算法，比如dijkstra算法求最短路
# 如下 Python 实现保留对数器验证逻辑，可比较不同方法的计算结果
# 对应实现保留相同的算法逻辑
class Code02_Persistent_Segment_Tree_Optimization_cpp:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'n': 'n', 'v': 'v', 'cntt': 'cntt', 'inBag': 'inBag', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'rootOut': 'rootOut', 'rootIn': 'rootIn', 'ls': 'ls', 'rs': 'rs', 'curVersion': 'curVersion', 'MAX_2': 'MAX_2', 'in_bag_2': 'in_bag_2', 'bag_id': 'bag_id', 'bag_val': 'bag_val', 'bag_siz': 'bag_siz', 'head_2': 'head_2', 'nxt_2': 'nxt_2', 'to_2': 'to_2', 'weight_2': 'weight_2', 'cnt_2': 'cnt_2', 'INF': 'INF', 'dist': 'dist', 'vis': 'vis', 'heap': 'heap'}
    MAXN = 0
    MAXV = 0
    MAXT = 0
    MAXE = 0
    n = 0
    v = 0
    cntt = 0
    inBag = None
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    rootOut = None
    rootIn = None
    ls = None
    rs = None
    curVersion = 0
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code02_Persistent_Segment_Tree_Optimization_cpp.nxt, ((_java_obj_1 := Code02_Persistent_Segment_Tree_Optimization_cpp), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_Persistent_Segment_Tree_Optimization_cpp.head[u])
        Code02_Persistent_Segment_Tree_Optimization_cpp.to[Code02_Persistent_Segment_Tree_Optimization_cpp.cntg] = jcast('int', v)
        Code02_Persistent_Segment_Tree_Optimization_cpp.weight[Code02_Persistent_Segment_Tree_Optimization_cpp.cntg] = jcast('int', w)
        Code02_Persistent_Segment_Tree_Optimization_cpp.head[u] = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.cntg)

    @staticmethod
    def buildOut(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_4 := Code02_Persistent_Segment_Tree_Optimization_cpp), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code02_Persistent_Segment_Tree_Optimization_cpp.ls, rt, Code02_Persistent_Segment_Tree_Optimization_cpp.buildOut(l, mid))
            jset(Code02_Persistent_Segment_Tree_Optimization_cpp.rs, rt, Code02_Persistent_Segment_Tree_Optimization_cpp.buildOut(jcast('int', jadd(mid, 1)), r))
            Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge(Code02_Persistent_Segment_Tree_Optimization_cpp.ls[rt], rt, 0)
            Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge(Code02_Persistent_Segment_Tree_Optimization_cpp.rs[rt], rt, 0)
        return jcast('int', rt)

    @staticmethod
    def buildIn(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_7 := Code02_Persistent_Segment_Tree_Optimization_cpp), (_java_key_8 := 'cntt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code02_Persistent_Segment_Tree_Optimization_cpp.ls, rt, Code02_Persistent_Segment_Tree_Optimization_cpp.buildIn(l, mid))
            jset(Code02_Persistent_Segment_Tree_Optimization_cpp.rs, rt, Code02_Persistent_Segment_Tree_Optimization_cpp.buildIn(jcast('int', jadd(mid, 1)), r))
            Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge(rt, Code02_Persistent_Segment_Tree_Optimization_cpp.ls[rt], 0)
            Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge(rt, Code02_Persistent_Segment_Tree_Optimization_cpp.rs[rt], 0)
        return jcast('int', rt)

    @staticmethod
    def addOut(jobx, jobv, l, r, i):
        jobx = jcast('int', jobx)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_10 := Code02_Persistent_Segment_Tree_Optimization_cpp), (_java_key_11 := 'cntt'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
        Code02_Persistent_Segment_Tree_Optimization_cpp.ls[rt] = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.ls[i])
        Code02_Persistent_Segment_Tree_Optimization_cpp.rs[rt] = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.rs[i])
        Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge(i, rt, 0)
        if (l == r):
            Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge(jobx, rt, 0)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobv <= mid):
                jset(Code02_Persistent_Segment_Tree_Optimization_cpp.ls, rt, Code02_Persistent_Segment_Tree_Optimization_cpp.addOut(jobx, jobv, l, mid, Code02_Persistent_Segment_Tree_Optimization_cpp.ls[rt]))
                Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge(Code02_Persistent_Segment_Tree_Optimization_cpp.ls[rt], rt, 0)
            else:
                jset(Code02_Persistent_Segment_Tree_Optimization_cpp.rs, rt, Code02_Persistent_Segment_Tree_Optimization_cpp.addOut(jobx, jobv, jcast('int', jadd(mid, 1)), r, Code02_Persistent_Segment_Tree_Optimization_cpp.rs[rt]))
                Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge(Code02_Persistent_Segment_Tree_Optimization_cpp.rs[rt], rt, 0)
        return jcast('int', rt)

    @staticmethod
    def addIn(jobx, jobv, l, r, i):
        jobx = jcast('int', jobx)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_13 := Code02_Persistent_Segment_Tree_Optimization_cpp), (_java_key_14 := 'cntt'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
        Code02_Persistent_Segment_Tree_Optimization_cpp.ls[rt] = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.ls[i])
        Code02_Persistent_Segment_Tree_Optimization_cpp.rs[rt] = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.rs[i])
        Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge(rt, i, 0)
        if (l == r):
            Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge(rt, jobx, 0)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobv <= mid):
                jset(Code02_Persistent_Segment_Tree_Optimization_cpp.ls, rt, Code02_Persistent_Segment_Tree_Optimization_cpp.addIn(jobx, jobv, l, mid, Code02_Persistent_Segment_Tree_Optimization_cpp.ls[rt]))
                Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge(rt, Code02_Persistent_Segment_Tree_Optimization_cpp.ls[rt], 0)
            else:
                jset(Code02_Persistent_Segment_Tree_Optimization_cpp.rs, rt, Code02_Persistent_Segment_Tree_Optimization_cpp.addIn(jobx, jobv, jcast('int', jadd(mid, 1)), r, Code02_Persistent_Segment_Tree_Optimization_cpp.rs[rt]))
                Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge(rt, Code02_Persistent_Segment_Tree_Optimization_cpp.rs[rt], 0)
        return jcast('int', rt)

    @staticmethod
    def add(x, xv):
        x = jcast('int', x)
        xv = jcast('int', xv)
        if (not Code02_Persistent_Segment_Tree_Optimization_cpp.inBag[x]):
            Code02_Persistent_Segment_Tree_Optimization_cpp.inBag[x] = jcast('boolean', True)
            Code02_Persistent_Segment_Tree_Optimization_cpp.curVersion = jcast('int', (Code02_Persistent_Segment_Tree_Optimization_cpp.curVersion + 1))
            jset(Code02_Persistent_Segment_Tree_Optimization_cpp.rootOut, Code02_Persistent_Segment_Tree_Optimization_cpp.curVersion, Code02_Persistent_Segment_Tree_Optimization_cpp.addOut(x, xv, 1, Code02_Persistent_Segment_Tree_Optimization_cpp.v, Code02_Persistent_Segment_Tree_Optimization_cpp.rootOut[jcast('int', (Code02_Persistent_Segment_Tree_Optimization_cpp.curVersion - 1))]))
            jset(Code02_Persistent_Segment_Tree_Optimization_cpp.rootIn, Code02_Persistent_Segment_Tree_Optimization_cpp.curVersion, Code02_Persistent_Segment_Tree_Optimization_cpp.addIn(x, xv, 1, Code02_Persistent_Segment_Tree_Optimization_cpp.v, Code02_Persistent_Segment_Tree_Optimization_cpp.rootIn[jcast('int', (Code02_Persistent_Segment_Tree_Optimization_cpp.curVersion - 1))]))

    @staticmethod
    def _java_rangeToX_0(jobl, jobr, jobx, jobw, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobx = jcast('int', jobx)
        jobw = jcast('int', jobw)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge(i, jobx, jobw)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code02_Persistent_Segment_Tree_Optimization_cpp._java_rangeToX_0(jobl, jobr, jobx, jobw, l, mid, Code02_Persistent_Segment_Tree_Optimization_cpp.ls[i])
            if (jobr > mid):
                Code02_Persistent_Segment_Tree_Optimization_cpp._java_rangeToX_0(jobl, jobr, jobx, jobw, jcast('int', jadd(mid, 1)), r, Code02_Persistent_Segment_Tree_Optimization_cpp.rs[i])

    @staticmethod
    def _java_rangeToX_1(l, r, x, w):
        l = jcast('int', l)
        r = jcast('int', r)
        x = jcast('int', x)
        w = jcast('int', w)
        Code02_Persistent_Segment_Tree_Optimization_cpp._java_rangeToX_0(l, r, x, w, 1, Code02_Persistent_Segment_Tree_Optimization_cpp.v, Code02_Persistent_Segment_Tree_Optimization_cpp.rootOut[Code02_Persistent_Segment_Tree_Optimization_cpp.curVersion])

    @staticmethod
    def _java_xToRange_0(jobx, jobl, jobr, jobw, l, r, i):
        jobx = jcast('int', jobx)
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobw = jcast('int', jobw)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge(jobx, i, jobw)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code02_Persistent_Segment_Tree_Optimization_cpp._java_xToRange_0(jobx, jobl, jobr, jobw, l, mid, Code02_Persistent_Segment_Tree_Optimization_cpp.ls[i])
            if (jobr > mid):
                Code02_Persistent_Segment_Tree_Optimization_cpp._java_xToRange_0(jobx, jobl, jobr, jobw, jcast('int', jadd(mid, 1)), r, Code02_Persistent_Segment_Tree_Optimization_cpp.rs[i])

    @staticmethod
    def _java_xToRange_1(x, l, r, w):
        x = jcast('int', x)
        l = jcast('int', l)
        r = jcast('int', r)
        w = jcast('int', w)
        Code02_Persistent_Segment_Tree_Optimization_cpp._java_xToRange_0(x, l, r, w, 1, Code02_Persistent_Segment_Tree_Optimization_cpp.v, Code02_Persistent_Segment_Tree_Optimization_cpp.rootIn[Code02_Persistent_Segment_Tree_Optimization_cpp.curVersion])

    @staticmethod
    def rangeToRange(l1, r1, l2, r2, w):
        l1 = jcast('int', l1)
        r1 = jcast('int', r1)
        l2 = jcast('int', l2)
        r2 = jcast('int', r2)
        w = jcast('int', w)
        x = jcast('int', ((_java_obj_16 := Code02_Persistent_Segment_Tree_Optimization_cpp), (_java_key_17 := 'cntt'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3])
        y = jcast('int', ((_java_obj_19 := Code02_Persistent_Segment_Tree_Optimization_cpp), (_java_key_20 := 'cntt'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3])
        Code02_Persistent_Segment_Tree_Optimization_cpp._java_rangeToX_1(l1, r1, x, 0)
        Code02_Persistent_Segment_Tree_Optimization_cpp._java_xToRange_1(y, l2, r2, 0)
        Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge(x, y, w)

    MAX_2 = 0
    in_bag_2 = None
    bag_id = None
    bag_val = None
    bag_siz = 0
    head_2 = None
    nxt_2 = None
    to_2 = None
    weight_2 = None
    cnt_2 = 0
    @staticmethod
    def addEdge_2(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code02_Persistent_Segment_Tree_Optimization_cpp.nxt_2, ((_java_obj_22 := Code02_Persistent_Segment_Tree_Optimization_cpp), (_java_key_23 := 'cnt_2'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))))[3], Code02_Persistent_Segment_Tree_Optimization_cpp.head_2[u])
        Code02_Persistent_Segment_Tree_Optimization_cpp.to_2[Code02_Persistent_Segment_Tree_Optimization_cpp.cnt_2] = jcast('int', v)
        Code02_Persistent_Segment_Tree_Optimization_cpp.weight_2[Code02_Persistent_Segment_Tree_Optimization_cpp.cnt_2] = jcast('int', w)
        Code02_Persistent_Segment_Tree_Optimization_cpp.head_2[u] = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.cnt_2)

    @staticmethod
    def add_2(x, xv):
        x = jcast('int', x)
        xv = jcast('int', xv)
        if (not Code02_Persistent_Segment_Tree_Optimization_cpp.in_bag_2[x]):
            Code02_Persistent_Segment_Tree_Optimization_cpp.in_bag_2[x] = jcast('boolean', True)
            jset(Code02_Persistent_Segment_Tree_Optimization_cpp.bag_id, ((_java_obj_25 := Code02_Persistent_Segment_Tree_Optimization_cpp), (_java_key_26 := 'bag_siz'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3], x)
            Code02_Persistent_Segment_Tree_Optimization_cpp.bag_val[Code02_Persistent_Segment_Tree_Optimization_cpp.bag_siz] = jcast('int', xv)

    @staticmethod
    def rangeToX_2(l, r, x, w):
        l = jcast('int', l)
        r = jcast('int', r)
        x = jcast('int', x)
        w = jcast('int', w)
        i = jcast('int', 1)
        while (i <= Code02_Persistent_Segment_Tree_Optimization_cpp.bag_siz):
            if ((Code02_Persistent_Segment_Tree_Optimization_cpp.bag_val[i] >= l) and (Code02_Persistent_Segment_Tree_Optimization_cpp.bag_val[i] <= r)):
                Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge_2(Code02_Persistent_Segment_Tree_Optimization_cpp.bag_id[i], x, w)
            i = jcast('int', (i + 1))

    @staticmethod
    def xToRange_2(x, l, r, w):
        x = jcast('int', x)
        l = jcast('int', l)
        r = jcast('int', r)
        w = jcast('int', w)
        i = jcast('int', 1)
        while (i <= Code02_Persistent_Segment_Tree_Optimization_cpp.bag_siz):
            if ((Code02_Persistent_Segment_Tree_Optimization_cpp.bag_val[i] >= l) and (Code02_Persistent_Segment_Tree_Optimization_cpp.bag_val[i] <= r)):
                Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge_2(x, Code02_Persistent_Segment_Tree_Optimization_cpp.bag_id[i], w)
            i = jcast('int', (i + 1))

    @staticmethod
    def rangeToRange_2(l1, r1, l2, r2, w):
        l1 = jcast('int', l1)
        r1 = jcast('int', r1)
        l2 = jcast('int', l2)
        r2 = jcast('int', r2)
        w = jcast('int', w)
        i = jcast('int', 1)
        while (i <= Code02_Persistent_Segment_Tree_Optimization_cpp.bag_siz):
            if ((Code02_Persistent_Segment_Tree_Optimization_cpp.bag_val[i] >= l1) and (Code02_Persistent_Segment_Tree_Optimization_cpp.bag_val[i] <= r1)):
                j = jcast('int', 1)
                while (j <= Code02_Persistent_Segment_Tree_Optimization_cpp.bag_siz):
                    if ((Code02_Persistent_Segment_Tree_Optimization_cpp.bag_val[j] >= l2) and (Code02_Persistent_Segment_Tree_Optimization_cpp.bag_val[j] <= r2)):
                        Code02_Persistent_Segment_Tree_Optimization_cpp.addEdge_2(Code02_Persistent_Segment_Tree_Optimization_cpp.bag_id[i], Code02_Persistent_Segment_Tree_Optimization_cpp.bag_id[j], w)
                    j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    INF = 0
    dist = None
    vis = None
    heap = None
    @staticmethod
    def dijkstra(s, t):
        s = jcast('int', s)
        t = jcast('int', t)
        i = jcast('int', 1)
        while (i <= Code02_Persistent_Segment_Tree_Optimization_cpp.cntt):
            Code02_Persistent_Segment_Tree_Optimization_cpp.dist[i] = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.INF)
            Code02_Persistent_Segment_Tree_Optimization_cpp.vis[i] = jcast('boolean', False)
            i = jcast('int', (i + 1))
        jcall(Code02_Persistent_Segment_Tree_Optimization_cpp.heap, 'clear')
        Code02_Persistent_Segment_Tree_Optimization_cpp.dist[s] = jcast('int', 0)
        jcall(Code02_Persistent_Segment_Tree_Optimization_cpp.heap, 'add', jarray('int', [None], [s, 0]))
        while (not jcall(Code02_Persistent_Segment_Tree_Optimization_cpp.heap, 'isEmpty')):
            cur = jcall(Code02_Persistent_Segment_Tree_Optimization_cpp.heap, 'poll')
            u = jcast('int', cur[0])
            d = jcast('int', cur[1])
            if (u == t):
                return jcast('int', d)
            if (not Code02_Persistent_Segment_Tree_Optimization_cpp.vis[u]):
                Code02_Persistent_Segment_Tree_Optimization_cpp.vis[u] = jcast('boolean', True)
                e = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.head[u])
                while (e > 0):
                    v = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.to[e])
                    w = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.weight[e])
                    if ((not Code02_Persistent_Segment_Tree_Optimization_cpp.vis[v]) and (Code02_Persistent_Segment_Tree_Optimization_cpp.dist[v] > jcast('int', jadd(d, w)))):
                        Code02_Persistent_Segment_Tree_Optimization_cpp.dist[v] = jcast('int', jcast('int', jadd(d, w)))
                        jcall(Code02_Persistent_Segment_Tree_Optimization_cpp.heap, 'add', jarray('int', [None], [v, Code02_Persistent_Segment_Tree_Optimization_cpp.dist[v]]))
                    e = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.nxt[e])
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def dijkstra2(s, t):
        s = jcast('int', s)
        t = jcast('int', t)
        i = jcast('int', 1)
        while (i <= Code02_Persistent_Segment_Tree_Optimization_cpp.n):
            Code02_Persistent_Segment_Tree_Optimization_cpp.dist[i] = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.INF)
            Code02_Persistent_Segment_Tree_Optimization_cpp.vis[i] = jcast('boolean', False)
            i = jcast('int', (i + 1))
        jcall(Code02_Persistent_Segment_Tree_Optimization_cpp.heap, 'clear')
        Code02_Persistent_Segment_Tree_Optimization_cpp.dist[s] = jcast('int', 0)
        jcall(Code02_Persistent_Segment_Tree_Optimization_cpp.heap, 'add', jarray('int', [None], [s, 0]))
        while (not jcall(Code02_Persistent_Segment_Tree_Optimization_cpp.heap, 'isEmpty')):
            cur = jcall(Code02_Persistent_Segment_Tree_Optimization_cpp.heap, 'poll')
            u = jcast('int', cur[0])
            d = jcast('int', cur[1])
            if (u == t):
                return jcast('int', d)
            if (not Code02_Persistent_Segment_Tree_Optimization_cpp.vis[u]):
                Code02_Persistent_Segment_Tree_Optimization_cpp.vis[u] = jcast('boolean', True)
                e = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.head_2[u])
                while (e > 0):
                    v = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.to_2[e])
                    w = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.weight_2[e])
                    if ((not Code02_Persistent_Segment_Tree_Optimization_cpp.vis[v]) and (Code02_Persistent_Segment_Tree_Optimization_cpp.dist[v] > jcast('int', jadd(d, w)))):
                        Code02_Persistent_Segment_Tree_Optimization_cpp.dist[v] = jcast('int', jcast('int', jadd(d, w)))
                        jcall(Code02_Persistent_Segment_Tree_Optimization_cpp.heap, 'add', jarray('int', [None], [v, Code02_Persistent_Segment_Tree_Optimization_cpp.dist[v]]))
                    e = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.nxt_2[e])
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def random(maxv):
        maxv = jcast('int', maxv)
        return jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * maxv)), 1)))

    @staticmethod
    def clear():
        i = jcast('int', 1)
        while (i <= Code02_Persistent_Segment_Tree_Optimization_cpp.cntt):
            Code02_Persistent_Segment_Tree_Optimization_cpp.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        Code02_Persistent_Segment_Tree_Optimization_cpp.cntg = jcast('int', 0)
        Code02_Persistent_Segment_Tree_Optimization_cpp.cntt = jcast('int', 0)
        Code02_Persistent_Segment_Tree_Optimization_cpp.curVersion = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code02_Persistent_Segment_Tree_Optimization_cpp.n):
            Code02_Persistent_Segment_Tree_Optimization_cpp.inBag[i] = jcast('boolean', False)
            Code02_Persistent_Segment_Tree_Optimization_cpp.in_bag_2[i] = jcast('boolean', False)
            Code02_Persistent_Segment_Tree_Optimization_cpp.head_2[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        Code02_Persistent_Segment_Tree_Optimization_cpp.bag_siz = jcast('int', 0)
        Code02_Persistent_Segment_Tree_Optimization_cpp.cnt_2 = jcast('int', 0)

    @staticmethod
    def main(args):
        jprint('主席树优化建图', newline=True)
        jprint('============', newline=True)
        Code02_Persistent_Segment_Tree_Optimization_cpp.n = jcast('int', 100)
        Code02_Persistent_Segment_Tree_Optimization_cpp.v = jcast('int', 200)
        weightMax = jcast('int', 1000)
        round = jcast('int', 20)
        t = jcast('int', 1)
        while (t <= round):
            jprint(jadd(jadd('第', t), '轮'), newline=True)
            jprint('测试开始', newline=True)
            Code02_Persistent_Segment_Tree_Optimization_cpp.cntt = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.n)
            jset(Code02_Persistent_Segment_Tree_Optimization_cpp.rootOut, 0, Code02_Persistent_Segment_Tree_Optimization_cpp.buildOut(1, Code02_Persistent_Segment_Tree_Optimization_cpp.v))
            jset(Code02_Persistent_Segment_Tree_Optimization_cpp.rootIn, 0, Code02_Persistent_Segment_Tree_Optimization_cpp.buildIn(1, Code02_Persistent_Segment_Tree_Optimization_cpp.v))
            opCnt = jcast('int', 200)
            i = jcast('int', 1)
            while (i <= opCnt):
                op = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.random(4))
                if (op == 1):
                    x = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.random(Code02_Persistent_Segment_Tree_Optimization_cpp.n))
                    xv = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.random(Code02_Persistent_Segment_Tree_Optimization_cpp.v))
                    Code02_Persistent_Segment_Tree_Optimization_cpp.add(x, xv)
                    Code02_Persistent_Segment_Tree_Optimization_cpp.add_2(x, xv)
                else:
                    a = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.random(Code02_Persistent_Segment_Tree_Optimization_cpp.v))
                    b = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.random(Code02_Persistent_Segment_Tree_Optimization_cpp.v))
                    l = jcast('int', jstatic('Math', 'min', a, b))
                    r = jcast('int', jstatic('Math', 'max', a, b))
                    a = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.random(Code02_Persistent_Segment_Tree_Optimization_cpp.v))
                    b = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.random(Code02_Persistent_Segment_Tree_Optimization_cpp.v))
                    l2 = jcast('int', jstatic('Math', 'min', a, b))
                    r2 = jcast('int', jstatic('Math', 'max', a, b))
                    x = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.random(Code02_Persistent_Segment_Tree_Optimization_cpp.n))
                    w = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.random(weightMax))
                    if (op == 2):
                        Code02_Persistent_Segment_Tree_Optimization_cpp._java_rangeToX_1(l, r, x, w)
                        Code02_Persistent_Segment_Tree_Optimization_cpp.rangeToX_2(l, r, x, w)
                    else:
                        if (op == 3):
                            Code02_Persistent_Segment_Tree_Optimization_cpp._java_xToRange_1(x, l, r, w)
                            Code02_Persistent_Segment_Tree_Optimization_cpp.xToRange_2(x, l, r, w)
                        else:
                            Code02_Persistent_Segment_Tree_Optimization_cpp.rangeToRange(l, r, l2, r2, w)
                            Code02_Persistent_Segment_Tree_Optimization_cpp.rangeToRange_2(l, r, l2, r2, w)
                i = jcast('int', (i + 1))
            x = jcast('int', 1)
            while (x <= Code02_Persistent_Segment_Tree_Optimization_cpp.n):
                y = jcast('int', 1)
                while (y <= Code02_Persistent_Segment_Tree_Optimization_cpp.n):
                    ans1 = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.dijkstra(x, y))
                    ans2 = jcast('int', Code02_Persistent_Segment_Tree_Optimization_cpp.dijkstra2(x, y))
                    if (ans1 != ans2):
                        jprint('出错了!', newline=True)
                    y = jcast('int', (y + 1))
                x = jcast('int', (x + 1))
            Code02_Persistent_Segment_Tree_Optimization_cpp.clear()
            jprint('测试结束', newline=True)
            jprint('=======', newline=True)
            t = jcast('int', (t + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def rangeToX(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int', 'int', 'int'], ['int', 'int', 'int', 'int']], [False, False])
        if _java_choice == 0:
            return Code02_Persistent_Segment_Tree_Optimization_cpp._java_rangeToX_0(*args)
        if _java_choice == 1:
            return Code02_Persistent_Segment_Tree_Optimization_cpp._java_rangeToX_1(*args)
        raise TypeError("No matching overload for Code02_Persistent_Segment_Tree_Optimization_cpp.rangeToX")

    @staticmethod
    def xToRange(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int', 'int', 'int'], ['int', 'int', 'int', 'int']], [False, False])
        if _java_choice == 0:
            return Code02_Persistent_Segment_Tree_Optimization_cpp._java_xToRange_0(*args)
        if _java_choice == 1:
            return Code02_Persistent_Segment_Tree_Optimization_cpp._java_xToRange_1(*args)
        raise TypeError("No matching overload for Code02_Persistent_Segment_Tree_Optimization_cpp.xToRange")


Code02_Persistent_Segment_Tree_Optimization_cpp.MAXN = jcast('int', 1001)
Code02_Persistent_Segment_Tree_Optimization_cpp.MAXV = jcast('int', 1001)
Code02_Persistent_Segment_Tree_Optimization_cpp.MAXT = jcast('int', 10001)
Code02_Persistent_Segment_Tree_Optimization_cpp.MAXE = jcast('int', 10001)
Code02_Persistent_Segment_Tree_Optimization_cpp.n = jcast('int', 0)
Code02_Persistent_Segment_Tree_Optimization_cpp.v = jcast('int', 0)
Code02_Persistent_Segment_Tree_Optimization_cpp.cntt = jcast('int', 0)
Code02_Persistent_Segment_Tree_Optimization_cpp.inBag = jarray('boolean', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAXN])
Code02_Persistent_Segment_Tree_Optimization_cpp.head = jarray('int', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAXT])
Code02_Persistent_Segment_Tree_Optimization_cpp.nxt = jarray('int', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAXE])
Code02_Persistent_Segment_Tree_Optimization_cpp.to = jarray('int', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAXE])
Code02_Persistent_Segment_Tree_Optimization_cpp.weight = jarray('int', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAXE])
Code02_Persistent_Segment_Tree_Optimization_cpp.cntg = jcast('int', 0)
Code02_Persistent_Segment_Tree_Optimization_cpp.rootOut = jarray('int', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAXN])
Code02_Persistent_Segment_Tree_Optimization_cpp.rootIn = jarray('int', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAXN])
Code02_Persistent_Segment_Tree_Optimization_cpp.ls = jarray('int', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAXT])
Code02_Persistent_Segment_Tree_Optimization_cpp.rs = jarray('int', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAXT])
Code02_Persistent_Segment_Tree_Optimization_cpp.curVersion = jcast('int', 0)
Code02_Persistent_Segment_Tree_Optimization_cpp.MAX_2 = jcast('int', 100001)
Code02_Persistent_Segment_Tree_Optimization_cpp.in_bag_2 = jarray('boolean', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAX_2])
Code02_Persistent_Segment_Tree_Optimization_cpp.bag_id = jarray('int', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAX_2])
Code02_Persistent_Segment_Tree_Optimization_cpp.bag_val = jarray('int', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAX_2])
Code02_Persistent_Segment_Tree_Optimization_cpp.bag_siz = jcast('int', 0)
Code02_Persistent_Segment_Tree_Optimization_cpp.head_2 = jarray('int', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAX_2])
Code02_Persistent_Segment_Tree_Optimization_cpp.nxt_2 = jarray('int', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAX_2])
Code02_Persistent_Segment_Tree_Optimization_cpp.to_2 = jarray('int', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAX_2])
Code02_Persistent_Segment_Tree_Optimization_cpp.weight_2 = jarray('int', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAX_2])
Code02_Persistent_Segment_Tree_Optimization_cpp.cnt_2 = jcast('int', 0)
Code02_Persistent_Segment_Tree_Optimization_cpp.INF = jcast('int', 1000000001)
Code02_Persistent_Segment_Tree_Optimization_cpp.dist = jarray('int', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAXT])
Code02_Persistent_Segment_Tree_Optimization_cpp.vis = jarray('boolean', [Code02_Persistent_Segment_Tree_Optimization_cpp.MAXT])
Code02_Persistent_Segment_Tree_Optimization_cpp.heap = jnew('PriorityQueue', (lambda x, y: (x[1] - y[1])))

if __name__ == '__main__':
    Code02_Persistent_Segment_Tree_Optimization_cpp.main([])
