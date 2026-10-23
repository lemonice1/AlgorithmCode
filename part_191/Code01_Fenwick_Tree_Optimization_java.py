# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 树状数组优化建图，Python版
# 点的编号范围1~n，点权范围1~v，初始时袋子为空，没有任何边，实现如下方法
# add(x, xv)，编号为x、点权为xv的点进入袋子，该编号已经入袋则忽略
# rangeToX(p, x, w)，袋中点权范围1~p的每个点，向点x连边权为w的边
# xToRange(x, p, w)，点x向袋中点权范围1~p的每个点，连边权为w的边
# rangeToRange(p1, p2, w)，范围向范围连边，具体含义如下
# 袋中点权1~p1的每个点，向袋中点权1~p2的每个点，连边权为w的边
# 建好图之后可以测试图的任何算法，比如dijkstra算法求最短路
# 对数器验证
class Code01_Fenwick_Tree_Optimization_java:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'n': 'n', 'v': 'v', 'cntt': 'cntt', 'inBag': 'inBag', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'outTree': 'outTree', 'inTree': 'inTree', 'MAX_2': 'MAX_2', 'in_bag_2': 'in_bag_2', 'bag_id': 'bag_id', 'bag_val': 'bag_val', 'bag_siz': 'bag_siz', 'head_2': 'head_2', 'nxt_2': 'nxt_2', 'to_2': 'to_2', 'weight_2': 'weight_2', 'cnt_2': 'cnt_2', 'INF': 'INF', 'dist': 'dist', 'vis': 'vis', 'heap': 'heap'}
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
    outTree = None
    inTree = None
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code01_Fenwick_Tree_Optimization_java.nxt, ((_java_obj_1 := Code01_Fenwick_Tree_Optimization_java), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_Fenwick_Tree_Optimization_java.head[u])
        Code01_Fenwick_Tree_Optimization_java.to[Code01_Fenwick_Tree_Optimization_java.cntg] = jcast('int', v)
        Code01_Fenwick_Tree_Optimization_java.weight[Code01_Fenwick_Tree_Optimization_java.cntg] = jcast('int', w)
        Code01_Fenwick_Tree_Optimization_java.head[u] = jcast('int', Code01_Fenwick_Tree_Optimization_java.cntg)

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def addOut(x, xv):
        x = jcast('int', x)
        xv = jcast('int', xv)
        while (xv <= Code01_Fenwick_Tree_Optimization_java.v):
            preo = jcast('int', Code01_Fenwick_Tree_Optimization_java.outTree[xv])
            curo = jcast('int', ((_java_obj_4 := Code01_Fenwick_Tree_Optimization_java), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
            if (preo > 0):
                Code01_Fenwick_Tree_Optimization_java.addEdge(preo, curo, 0)
            Code01_Fenwick_Tree_Optimization_java.addEdge(x, curo, 0)
            Code01_Fenwick_Tree_Optimization_java.outTree[xv] = jcast('int', curo)
            xv = jcast('int', jcast('int', jadd(xv, Code01_Fenwick_Tree_Optimization_java.lowbit(xv))))

    @staticmethod
    def addIn(x, xv):
        x = jcast('int', x)
        xv = jcast('int', xv)
        while (xv <= Code01_Fenwick_Tree_Optimization_java.v):
            prei = jcast('int', Code01_Fenwick_Tree_Optimization_java.inTree[xv])
            curi = jcast('int', ((_java_obj_7 := Code01_Fenwick_Tree_Optimization_java), (_java_key_8 := 'cntt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
            if (prei > 0):
                Code01_Fenwick_Tree_Optimization_java.addEdge(curi, prei, 0)
            Code01_Fenwick_Tree_Optimization_java.addEdge(curi, x, 0)
            Code01_Fenwick_Tree_Optimization_java.inTree[xv] = jcast('int', curi)
            xv = jcast('int', jcast('int', jadd(xv, Code01_Fenwick_Tree_Optimization_java.lowbit(xv))))

    @staticmethod
    def add(x, xv):
        x = jcast('int', x)
        xv = jcast('int', xv)
        if (not Code01_Fenwick_Tree_Optimization_java.inBag[x]):
            Code01_Fenwick_Tree_Optimization_java.inBag[x] = jcast('boolean', True)
            Code01_Fenwick_Tree_Optimization_java.addOut(x, xv)
            Code01_Fenwick_Tree_Optimization_java.addIn(x, xv)

    @staticmethod
    def rangeToX(p, x, w):
        p = jcast('int', p)
        x = jcast('int', x)
        w = jcast('int', w)
        while (p > 0):
            if (Code01_Fenwick_Tree_Optimization_java.outTree[p] > 0):
                Code01_Fenwick_Tree_Optimization_java.addEdge(Code01_Fenwick_Tree_Optimization_java.outTree[p], x, w)
            p = jcast('int', jcast('int', (p - Code01_Fenwick_Tree_Optimization_java.lowbit(p))))

    @staticmethod
    def xToRange(x, p, w):
        x = jcast('int', x)
        p = jcast('int', p)
        w = jcast('int', w)
        while (p > 0):
            if (Code01_Fenwick_Tree_Optimization_java.inTree[p] > 0):
                Code01_Fenwick_Tree_Optimization_java.addEdge(x, Code01_Fenwick_Tree_Optimization_java.inTree[p], w)
            p = jcast('int', jcast('int', (p - Code01_Fenwick_Tree_Optimization_java.lowbit(p))))

    @staticmethod
    def rangeToRange(p1, p2, w):
        p1 = jcast('int', p1)
        p2 = jcast('int', p2)
        w = jcast('int', w)
        x = jcast('int', ((_java_obj_10 := Code01_Fenwick_Tree_Optimization_java), (_java_key_11 := 'cntt'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
        y = jcast('int', ((_java_obj_13 := Code01_Fenwick_Tree_Optimization_java), (_java_key_14 := 'cntt'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
        Code01_Fenwick_Tree_Optimization_java.rangeToX(p1, x, 0)
        Code01_Fenwick_Tree_Optimization_java.xToRange(y, p2, 0)
        Code01_Fenwick_Tree_Optimization_java.addEdge(x, y, w)

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
        jset(Code01_Fenwick_Tree_Optimization_java.nxt_2, ((_java_obj_16 := Code01_Fenwick_Tree_Optimization_java), (_java_key_17 := 'cnt_2'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code01_Fenwick_Tree_Optimization_java.head_2[u])
        Code01_Fenwick_Tree_Optimization_java.to_2[Code01_Fenwick_Tree_Optimization_java.cnt_2] = jcast('int', v)
        Code01_Fenwick_Tree_Optimization_java.weight_2[Code01_Fenwick_Tree_Optimization_java.cnt_2] = jcast('int', w)
        Code01_Fenwick_Tree_Optimization_java.head_2[u] = jcast('int', Code01_Fenwick_Tree_Optimization_java.cnt_2)

    @staticmethod
    def add_2(x, xv):
        x = jcast('int', x)
        xv = jcast('int', xv)
        if (not Code01_Fenwick_Tree_Optimization_java.in_bag_2[x]):
            Code01_Fenwick_Tree_Optimization_java.in_bag_2[x] = jcast('boolean', True)
            jset(Code01_Fenwick_Tree_Optimization_java.bag_id, ((_java_obj_19 := Code01_Fenwick_Tree_Optimization_java), (_java_key_20 := 'bag_siz'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], x)
            Code01_Fenwick_Tree_Optimization_java.bag_val[Code01_Fenwick_Tree_Optimization_java.bag_siz] = jcast('int', xv)

    @staticmethod
    def rangeToX_2(p, x, w):
        p = jcast('int', p)
        x = jcast('int', x)
        w = jcast('int', w)
        i = jcast('int', 1)
        while (i <= Code01_Fenwick_Tree_Optimization_java.bag_siz):
            if (Code01_Fenwick_Tree_Optimization_java.bag_val[i] <= p):
                Code01_Fenwick_Tree_Optimization_java.addEdge_2(Code01_Fenwick_Tree_Optimization_java.bag_id[i], x, w)
            i = jcast('int', (i + 1))

    @staticmethod
    def xToRange_2(x, p, w):
        x = jcast('int', x)
        p = jcast('int', p)
        w = jcast('int', w)
        i = jcast('int', 1)
        while (i <= Code01_Fenwick_Tree_Optimization_java.bag_siz):
            if (Code01_Fenwick_Tree_Optimization_java.bag_val[i] <= p):
                Code01_Fenwick_Tree_Optimization_java.addEdge_2(x, Code01_Fenwick_Tree_Optimization_java.bag_id[i], w)
            i = jcast('int', (i + 1))

    @staticmethod
    def rangeToRange_2(p1, p2, w):
        p1 = jcast('int', p1)
        p2 = jcast('int', p2)
        w = jcast('int', w)
        i = jcast('int', 1)
        while (i <= Code01_Fenwick_Tree_Optimization_java.bag_siz):
            if (Code01_Fenwick_Tree_Optimization_java.bag_val[i] <= p1):
                j = jcast('int', 1)
                while (j <= Code01_Fenwick_Tree_Optimization_java.bag_siz):
                    if (Code01_Fenwick_Tree_Optimization_java.bag_val[j] <= p2):
                        Code01_Fenwick_Tree_Optimization_java.addEdge_2(Code01_Fenwick_Tree_Optimization_java.bag_id[i], Code01_Fenwick_Tree_Optimization_java.bag_id[j], w)
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
        while (i <= Code01_Fenwick_Tree_Optimization_java.cntt):
            Code01_Fenwick_Tree_Optimization_java.dist[i] = jcast('int', Code01_Fenwick_Tree_Optimization_java.INF)
            Code01_Fenwick_Tree_Optimization_java.vis[i] = jcast('boolean', False)
            i = jcast('int', (i + 1))
        jcall(Code01_Fenwick_Tree_Optimization_java.heap, 'clear')
        Code01_Fenwick_Tree_Optimization_java.dist[s] = jcast('int', 0)
        jcall(Code01_Fenwick_Tree_Optimization_java.heap, 'add', jarray('int', [None], [s, 0]))
        while (not jcall(Code01_Fenwick_Tree_Optimization_java.heap, 'isEmpty')):
            cur = jcall(Code01_Fenwick_Tree_Optimization_java.heap, 'poll')
            u = jcast('int', cur[0])
            d = jcast('int', cur[1])
            if (u == t):
                return jcast('int', d)
            if (not Code01_Fenwick_Tree_Optimization_java.vis[u]):
                Code01_Fenwick_Tree_Optimization_java.vis[u] = jcast('boolean', True)
                e = jcast('int', Code01_Fenwick_Tree_Optimization_java.head[u])
                while (e > 0):
                    v = jcast('int', Code01_Fenwick_Tree_Optimization_java.to[e])
                    w = jcast('int', Code01_Fenwick_Tree_Optimization_java.weight[e])
                    if ((not Code01_Fenwick_Tree_Optimization_java.vis[v]) and (Code01_Fenwick_Tree_Optimization_java.dist[v] > jcast('int', jadd(d, w)))):
                        Code01_Fenwick_Tree_Optimization_java.dist[v] = jcast('int', jcast('int', jadd(d, w)))
                        jcall(Code01_Fenwick_Tree_Optimization_java.heap, 'add', jarray('int', [None], [v, Code01_Fenwick_Tree_Optimization_java.dist[v]]))
                    e = jcast('int', Code01_Fenwick_Tree_Optimization_java.nxt[e])
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def dijkstra2(s, t):
        s = jcast('int', s)
        t = jcast('int', t)
        i = jcast('int', 1)
        while (i <= Code01_Fenwick_Tree_Optimization_java.n):
            Code01_Fenwick_Tree_Optimization_java.dist[i] = jcast('int', Code01_Fenwick_Tree_Optimization_java.INF)
            Code01_Fenwick_Tree_Optimization_java.vis[i] = jcast('boolean', False)
            i = jcast('int', (i + 1))
        jcall(Code01_Fenwick_Tree_Optimization_java.heap, 'clear')
        Code01_Fenwick_Tree_Optimization_java.dist[s] = jcast('int', 0)
        jcall(Code01_Fenwick_Tree_Optimization_java.heap, 'add', jarray('int', [None], [s, 0]))
        while (not jcall(Code01_Fenwick_Tree_Optimization_java.heap, 'isEmpty')):
            cur = jcall(Code01_Fenwick_Tree_Optimization_java.heap, 'poll')
            u = jcast('int', cur[0])
            d = jcast('int', cur[1])
            if (u == t):
                return jcast('int', d)
            if (not Code01_Fenwick_Tree_Optimization_java.vis[u]):
                Code01_Fenwick_Tree_Optimization_java.vis[u] = jcast('boolean', True)
                e = jcast('int', Code01_Fenwick_Tree_Optimization_java.head_2[u])
                while (e > 0):
                    v = jcast('int', Code01_Fenwick_Tree_Optimization_java.to_2[e])
                    w = jcast('int', Code01_Fenwick_Tree_Optimization_java.weight_2[e])
                    if ((not Code01_Fenwick_Tree_Optimization_java.vis[v]) and (Code01_Fenwick_Tree_Optimization_java.dist[v] > jcast('int', jadd(d, w)))):
                        Code01_Fenwick_Tree_Optimization_java.dist[v] = jcast('int', jcast('int', jadd(d, w)))
                        jcall(Code01_Fenwick_Tree_Optimization_java.heap, 'add', jarray('int', [None], [v, Code01_Fenwick_Tree_Optimization_java.dist[v]]))
                    e = jcast('int', Code01_Fenwick_Tree_Optimization_java.nxt_2[e])
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def random(maxv):
        maxv = jcast('int', maxv)
        return jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * maxv)), 1)))

    @staticmethod
    def clear():
        i = jcast('int', 1)
        while (i <= Code01_Fenwick_Tree_Optimization_java.cntt):
            Code01_Fenwick_Tree_Optimization_java.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        Code01_Fenwick_Tree_Optimization_java.cntg = jcast('int', 0)
        Code01_Fenwick_Tree_Optimization_java.cntt = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code01_Fenwick_Tree_Optimization_java.v):
            Code01_Fenwick_Tree_Optimization_java.inTree[i] = jcast('int', 0)
            Code01_Fenwick_Tree_Optimization_java.outTree[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_Fenwick_Tree_Optimization_java.n):
            Code01_Fenwick_Tree_Optimization_java.inBag[i] = jcast('boolean', False)
            Code01_Fenwick_Tree_Optimization_java.in_bag_2[i] = jcast('boolean', False)
            Code01_Fenwick_Tree_Optimization_java.head_2[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        Code01_Fenwick_Tree_Optimization_java.bag_siz = jcast('int', 0)
        Code01_Fenwick_Tree_Optimization_java.cnt_2 = jcast('int', 0)

    @staticmethod
    def main(args):
        jprint('树状数组优化建图', newline=True)
        jprint('============', newline=True)
        Code01_Fenwick_Tree_Optimization_java.n = jcast('int', 100)
        Code01_Fenwick_Tree_Optimization_java.v = jcast('int', 200)
        weightMax = jcast('int', 1000)
        round = jcast('int', 20)
        t = jcast('int', 1)
        while (t <= round):
            jprint(jadd(jadd('第', t), '轮'), newline=True)
            jprint('测试开始', newline=True)
            Code01_Fenwick_Tree_Optimization_java.cntt = jcast('int', Code01_Fenwick_Tree_Optimization_java.n)
            opCnt = jcast('int', 200)
            i = jcast('int', 1)
            while (i <= opCnt):
                op = jcast('int', Code01_Fenwick_Tree_Optimization_java.random(4))
                if (op == 1):
                    x = jcast('int', Code01_Fenwick_Tree_Optimization_java.random(Code01_Fenwick_Tree_Optimization_java.n))
                    xv = jcast('int', Code01_Fenwick_Tree_Optimization_java.random(Code01_Fenwick_Tree_Optimization_java.v))
                    Code01_Fenwick_Tree_Optimization_java.add(x, xv)
                    Code01_Fenwick_Tree_Optimization_java.add_2(x, xv)
                else:
                    p = jcast('int', Code01_Fenwick_Tree_Optimization_java.random(Code01_Fenwick_Tree_Optimization_java.v))
                    p2 = jcast('int', Code01_Fenwick_Tree_Optimization_java.random(Code01_Fenwick_Tree_Optimization_java.v))
                    x = jcast('int', Code01_Fenwick_Tree_Optimization_java.random(Code01_Fenwick_Tree_Optimization_java.n))
                    w = jcast('int', Code01_Fenwick_Tree_Optimization_java.random(weightMax))
                    if (op == 2):
                        Code01_Fenwick_Tree_Optimization_java.rangeToX(p, x, w)
                        Code01_Fenwick_Tree_Optimization_java.rangeToX_2(p, x, w)
                    else:
                        if (op == 3):
                            Code01_Fenwick_Tree_Optimization_java.xToRange(x, p, w)
                            Code01_Fenwick_Tree_Optimization_java.xToRange_2(x, p, w)
                        else:
                            Code01_Fenwick_Tree_Optimization_java.rangeToRange(p, p2, w)
                            Code01_Fenwick_Tree_Optimization_java.rangeToRange_2(p, p2, w)
                i = jcast('int', (i + 1))
            x = jcast('int', 1)
            while (x <= Code01_Fenwick_Tree_Optimization_java.n):
                y = jcast('int', 1)
                while (y <= Code01_Fenwick_Tree_Optimization_java.n):
                    ans1 = jcast('int', Code01_Fenwick_Tree_Optimization_java.dijkstra(x, y))
                    ans2 = jcast('int', Code01_Fenwick_Tree_Optimization_java.dijkstra2(x, y))
                    if (ans1 != ans2):
                        jprint('出错了!', newline=True)
                    y = jcast('int', (y + 1))
                x = jcast('int', (x + 1))
            Code01_Fenwick_Tree_Optimization_java.clear()
            jprint('测试结束', newline=True)
            jprint('=======', newline=True)
            t = jcast('int', (t + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_Fenwick_Tree_Optimization_java.MAXN = jcast('int', 1001)
Code01_Fenwick_Tree_Optimization_java.MAXV = jcast('int', 1001)
Code01_Fenwick_Tree_Optimization_java.MAXT = jcast('int', 10001)
Code01_Fenwick_Tree_Optimization_java.MAXE = jcast('int', 10001)
Code01_Fenwick_Tree_Optimization_java.n = jcast('int', 0)
Code01_Fenwick_Tree_Optimization_java.v = jcast('int', 0)
Code01_Fenwick_Tree_Optimization_java.cntt = jcast('int', 0)
Code01_Fenwick_Tree_Optimization_java.inBag = jarray('boolean', [Code01_Fenwick_Tree_Optimization_java.MAXN])
Code01_Fenwick_Tree_Optimization_java.head = jarray('int', [Code01_Fenwick_Tree_Optimization_java.MAXT])
Code01_Fenwick_Tree_Optimization_java.nxt = jarray('int', [Code01_Fenwick_Tree_Optimization_java.MAXE])
Code01_Fenwick_Tree_Optimization_java.to = jarray('int', [Code01_Fenwick_Tree_Optimization_java.MAXE])
Code01_Fenwick_Tree_Optimization_java.weight = jarray('int', [Code01_Fenwick_Tree_Optimization_java.MAXE])
Code01_Fenwick_Tree_Optimization_java.cntg = jcast('int', 0)
Code01_Fenwick_Tree_Optimization_java.outTree = jarray('int', [Code01_Fenwick_Tree_Optimization_java.MAXV])
Code01_Fenwick_Tree_Optimization_java.inTree = jarray('int', [Code01_Fenwick_Tree_Optimization_java.MAXV])
Code01_Fenwick_Tree_Optimization_java.MAX_2 = jcast('int', 100001)
Code01_Fenwick_Tree_Optimization_java.in_bag_2 = jarray('boolean', [Code01_Fenwick_Tree_Optimization_java.MAX_2])
Code01_Fenwick_Tree_Optimization_java.bag_id = jarray('int', [Code01_Fenwick_Tree_Optimization_java.MAX_2])
Code01_Fenwick_Tree_Optimization_java.bag_val = jarray('int', [Code01_Fenwick_Tree_Optimization_java.MAX_2])
Code01_Fenwick_Tree_Optimization_java.bag_siz = jcast('int', 0)
Code01_Fenwick_Tree_Optimization_java.head_2 = jarray('int', [Code01_Fenwick_Tree_Optimization_java.MAX_2])
Code01_Fenwick_Tree_Optimization_java.nxt_2 = jarray('int', [Code01_Fenwick_Tree_Optimization_java.MAX_2])
Code01_Fenwick_Tree_Optimization_java.to_2 = jarray('int', [Code01_Fenwick_Tree_Optimization_java.MAX_2])
Code01_Fenwick_Tree_Optimization_java.weight_2 = jarray('int', [Code01_Fenwick_Tree_Optimization_java.MAX_2])
Code01_Fenwick_Tree_Optimization_java.cnt_2 = jcast('int', 0)
Code01_Fenwick_Tree_Optimization_java.INF = jcast('int', 1000000001)
Code01_Fenwick_Tree_Optimization_java.dist = jarray('int', [Code01_Fenwick_Tree_Optimization_java.MAXT])
Code01_Fenwick_Tree_Optimization_java.vis = jarray('boolean', [Code01_Fenwick_Tree_Optimization_java.MAXT])
Code01_Fenwick_Tree_Optimization_java.heap = jnew('PriorityQueue', (lambda x, y: (x[1] - y[1])))

if __name__ == '__main__':
    Code01_Fenwick_Tree_Optimization_java.main([])
