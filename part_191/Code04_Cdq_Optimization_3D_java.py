# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# cdq优化建图三维偏序，Python版
# 一共n个点，每个点给定三个点权，a[i]、b[i]、c[i]，初始时没有边
# 一共m条操作，格式 x w，每个满足如下要求的点，都向x连权值为w的边
# 三种点权 <= x对应的点权，这样的点就算满足要求，注意x自己也是达标的
# 建好图之后可以测试图的任何算法，比如dijkstra算法求最短路
# 对数器验证
class Code04_Cdq_Optimization_3D_java:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXV': 'MAXV', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'n': 'n', 'm': 'm', 'maxc': 'maxc', 'cntt': 'cntt', 'a': 'a', 'b': 'b', 'c': 'c', 'arr': 'arr', 'cnta': 'cnta', 'headg': 'headg', 'nextg': 'nextg', 'tog': 'tog', 'weightg': 'weightg', 'cntg': 'cntg', 'headp': 'headp', 'nextp': 'nextp', 'top': 'top', 'weightp': 'weightp', 'cntp': 'cntp', 'tree': 'tree', 'MAX_2': 'MAX_2', 'head_2': 'head_2', 'nxt_2': 'nxt_2', 'to_2': 'to_2', 'weight_2': 'weight_2', 'cnt_2': 'cnt_2', 'INF': 'INF', 'dist': 'dist', 'vis': 'vis', 'heap': 'heap'}
    MAXN = 0
    MAXM = 0
    MAXV = 0
    MAXT = 0
    MAXE = 0
    n = 0
    m = 0
    maxc = 0
    cntt = 0
    a = None
    b = None
    c = None
    # i、a、b、c
    arr = None
    cnta = 0
    # 建图
    headg = None
    nextg = None
    tog = None
    weightg = None
    cntg = 0
    # 每个小组的操作列表
    headp = None
    nextp = None
    top = None
    weightp = None
    cntp = 0
    # 树状数组
    tree = None
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code04_Cdq_Optimization_3D_java.nextg, ((_java_obj_1 := Code04_Cdq_Optimization_3D_java), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_Cdq_Optimization_3D_java.headg[u])
        Code04_Cdq_Optimization_3D_java.tog[Code04_Cdq_Optimization_3D_java.cntg] = jcast('int', v)
        Code04_Cdq_Optimization_3D_java.weightg[Code04_Cdq_Optimization_3D_java.cntg] = jcast('int', w)
        Code04_Cdq_Optimization_3D_java.headg[u] = jcast('int', Code04_Cdq_Optimization_3D_java.cntg)

    @staticmethod
    def addOp(x, u, w):
        x = jcast('int', x)
        u = jcast('int', u)
        w = jcast('int', w)
        jset(Code04_Cdq_Optimization_3D_java.nextp, ((_java_obj_4 := Code04_Cdq_Optimization_3D_java), (_java_key_5 := 'cntp'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code04_Cdq_Optimization_3D_java.headp[x])
        Code04_Cdq_Optimization_3D_java.top[Code04_Cdq_Optimization_3D_java.cntp] = jcast('int', u)
        Code04_Cdq_Optimization_3D_java.weightp[Code04_Cdq_Optimization_3D_java.cntp] = jcast('int', w)
        Code04_Cdq_Optimization_3D_java.headp[x] = jcast('int', Code04_Cdq_Optimization_3D_java.cntp)

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        while (i <= Code04_Cdq_Optimization_3D_java.maxc):
            pre = jcast('int', Code04_Cdq_Optimization_3D_java.tree[i])
            cur = jcast('int', ((_java_obj_7 := Code04_Cdq_Optimization_3D_java), (_java_key_8 := 'cntt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
            if (pre != 0):
                Code04_Cdq_Optimization_3D_java.addEdge(pre, cur, 0)
            Code04_Cdq_Optimization_3D_java.addEdge(x, cur, 0)
            Code04_Cdq_Optimization_3D_java.tree[i] = jcast('int', cur)
            i = jcast('int', jcast('int', jadd(i, Code04_Cdq_Optimization_3D_java.lowbit(i))))

    @staticmethod
    def rangeToX(i, x, w):
        i = jcast('int', i)
        x = jcast('int', x)
        w = jcast('int', w)
        while (i > 0):
            if (Code04_Cdq_Optimization_3D_java.tree[i] > 0):
                Code04_Cdq_Optimization_3D_java.addEdge(Code04_Cdq_Optimization_3D_java.tree[i], x, w)
            i = jcast('int', jcast('int', (i - Code04_Cdq_Optimization_3D_java.lowbit(i))))

    @staticmethod
    def _java_clear_0(val):
        val = jcast('int', val)
        while (val <= Code04_Cdq_Optimization_3D_java.maxc):
            Code04_Cdq_Optimization_3D_java.tree[val] = jcast('int', 0)
            val = jcast('int', jcast('int', jadd(val, Code04_Cdq_Optimization_3D_java.lowbit(val))))

    @staticmethod
    def merge(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        p1 = 0
        p2 = 0
        p1 = jcast('int', jcast('int', (l - 1)))
        p2 = jcast('int', jcast('int', jadd(m, 1)))
        while (p2 <= r):
            while ((jcast('int', jadd(p1, 1)) <= m) and (Code04_Cdq_Optimization_3D_java.arr[jcast('int', jadd(p1, 1))][2] <= Code04_Cdq_Optimization_3D_java.arr[p2][2])):
                p1 = jcast('int', (p1 + 1))
                Code04_Cdq_Optimization_3D_java.add(Code04_Cdq_Optimization_3D_java.arr[p1][3], Code04_Cdq_Optimization_3D_java.arr[p1][0])
            e = jcast('int', Code04_Cdq_Optimization_3D_java.headp[Code04_Cdq_Optimization_3D_java.arr[p2][0]])
            while (e > 0):
                u = jcast('int', Code04_Cdq_Optimization_3D_java.top[e])
                w = jcast('int', Code04_Cdq_Optimization_3D_java.weightp[e])
                Code04_Cdq_Optimization_3D_java.rangeToX(Code04_Cdq_Optimization_3D_java.arr[p2][3], u, w)
                e = jcast('int', Code04_Cdq_Optimization_3D_java.nextp[e])
            p2 = jcast('int', (p2 + 1))
        i = jcast('int', l)
        while (i <= p1):
            Code04_Cdq_Optimization_3D_java._java_clear_0(Code04_Cdq_Optimization_3D_java.arr[i][3])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_Cdq_Optimization_3D_java.arr, l, jcast('int', jadd(r, 1)), (lambda x, y: (x[2] - y[2])))

    @staticmethod
    def cdq(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code04_Cdq_Optimization_3D_java.cdq(l, mid)
        Code04_Cdq_Optimization_3D_java.cdq(jcast('int', jadd(mid, 1)), r)
        Code04_Cdq_Optimization_3D_java.merge(l, mid, r)

    @staticmethod
    def buildGraph():
        i = jcast('int', 1)
        while (i <= Code04_Cdq_Optimization_3D_java.n):
            jset(Code04_Cdq_Optimization_3D_java.arr[i], 0, i)
            jset(Code04_Cdq_Optimization_3D_java.arr[i], 1, Code04_Cdq_Optimization_3D_java.a[i])
            jset(Code04_Cdq_Optimization_3D_java.arr[i], 2, Code04_Cdq_Optimization_3D_java.b[i])
            jset(Code04_Cdq_Optimization_3D_java.arr[i], 3, Code04_Cdq_Optimization_3D_java.c[i])
            Code04_Cdq_Optimization_3D_java.maxc = jcast('int', jstatic('Math', 'max', Code04_Cdq_Optimization_3D_java.maxc, Code04_Cdq_Optimization_3D_java.c[i]))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_Cdq_Optimization_3D_java.arr, 1, jcast('int', jadd(Code04_Cdq_Optimization_3D_java.n, 1)), (lambda x, y: ((x[1] - y[1]) if (x[1] != y[1]) else ((x[2] - y[2]) if (x[2] != y[2]) else (x[3] - y[3])))))
        Code04_Cdq_Optimization_3D_java.cntt = jcast('int', Code04_Cdq_Optimization_3D_java.n)
        l = jcast('int', 1)
        r = jcast('int', 1)
        while (l <= Code04_Cdq_Optimization_3D_java.n):
            a = jcast('int', Code04_Cdq_Optimization_3D_java.arr[l][1])
            b = jcast('int', Code04_Cdq_Optimization_3D_java.arr[l][2])
            c = jcast('int', Code04_Cdq_Optimization_3D_java.arr[l][3])
            while ((((jcast('int', jadd(r, 1)) <= Code04_Cdq_Optimization_3D_java.n) and (a == Code04_Cdq_Optimization_3D_java.arr[jcast('int', jadd(r, 1))][1])) and (b == Code04_Cdq_Optimization_3D_java.arr[jcast('int', jadd(r, 1))][2])) and (c == Code04_Cdq_Optimization_3D_java.arr[jcast('int', jadd(r, 1))][3])):
                r = jcast('int', (r + 1))
            x = jcast('int', ((_java_obj_10 := Code04_Cdq_Optimization_3D_java), (_java_key_11 := 'cntt'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
            i = jcast('int', l)
            while (i <= r):
                u = jcast('int', Code04_Cdq_Optimization_3D_java.arr[i][0])
                Code04_Cdq_Optimization_3D_java.addEdge(u, x, 0)
                e = jcast('int', Code04_Cdq_Optimization_3D_java.headp[u])
                while (e > 0):
                    Code04_Cdq_Optimization_3D_java.addEdge(x, u, Code04_Cdq_Optimization_3D_java.weightp[e])
                    Code04_Cdq_Optimization_3D_java.addOp(x, u, Code04_Cdq_Optimization_3D_java.weightp[e])
                    e = jcast('int', Code04_Cdq_Optimization_3D_java.nextp[e])
                i = jcast('int', (i + 1))
            jset(Code04_Cdq_Optimization_3D_java.arr[((_java_obj_13 := Code04_Cdq_Optimization_3D_java), (_java_key_14 := 'cnta'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]], 0, x)
            jset(Code04_Cdq_Optimization_3D_java.arr[Code04_Cdq_Optimization_3D_java.cnta], 1, a)
            jset(Code04_Cdq_Optimization_3D_java.arr[Code04_Cdq_Optimization_3D_java.cnta], 2, b)
            jset(Code04_Cdq_Optimization_3D_java.arr[Code04_Cdq_Optimization_3D_java.cnta], 3, c)
            l = jcast('int', (r := jcast('int', (r + (1)))))
        Code04_Cdq_Optimization_3D_java.cdq(1, Code04_Cdq_Optimization_3D_java.cnta)

    MAX_2 = 0
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
        jset(Code04_Cdq_Optimization_3D_java.nxt_2, ((_java_obj_16 := Code04_Cdq_Optimization_3D_java), (_java_key_17 := 'cnt_2'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code04_Cdq_Optimization_3D_java.head_2[u])
        Code04_Cdq_Optimization_3D_java.to_2[Code04_Cdq_Optimization_3D_java.cnt_2] = jcast('int', v)
        Code04_Cdq_Optimization_3D_java.weight_2[Code04_Cdq_Optimization_3D_java.cnt_2] = jcast('int', w)
        Code04_Cdq_Optimization_3D_java.head_2[u] = jcast('int', Code04_Cdq_Optimization_3D_java.cnt_2)

    @staticmethod
    def link(x, w):
        x = jcast('int', x)
        w = jcast('int', w)
        i = jcast('int', 1)
        while (i <= Code04_Cdq_Optimization_3D_java.n):
            if (((Code04_Cdq_Optimization_3D_java.a[i] <= Code04_Cdq_Optimization_3D_java.a[x]) and (Code04_Cdq_Optimization_3D_java.b[i] <= Code04_Cdq_Optimization_3D_java.b[x])) and (Code04_Cdq_Optimization_3D_java.c[i] <= Code04_Cdq_Optimization_3D_java.c[x])):
                Code04_Cdq_Optimization_3D_java.addEdge_2(i, x, w)
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
        while (i <= Code04_Cdq_Optimization_3D_java.cntt):
            Code04_Cdq_Optimization_3D_java.dist[i] = jcast('int', Code04_Cdq_Optimization_3D_java.INF)
            Code04_Cdq_Optimization_3D_java.vis[i] = jcast('boolean', False)
            i = jcast('int', (i + 1))
        jcall(Code04_Cdq_Optimization_3D_java.heap, 'clear')
        Code04_Cdq_Optimization_3D_java.dist[s] = jcast('int', 0)
        jcall(Code04_Cdq_Optimization_3D_java.heap, 'add', jarray('int', [None], [s, 0]))
        while (not jcall(Code04_Cdq_Optimization_3D_java.heap, 'isEmpty')):
            cur = jcall(Code04_Cdq_Optimization_3D_java.heap, 'poll')
            u = jcast('int', cur[0])
            d = jcast('int', cur[1])
            if (u == t):
                return jcast('int', d)
            if (not Code04_Cdq_Optimization_3D_java.vis[u]):
                Code04_Cdq_Optimization_3D_java.vis[u] = jcast('boolean', True)
                e = jcast('int', Code04_Cdq_Optimization_3D_java.headg[u])
                while (e > 0):
                    v = jcast('int', Code04_Cdq_Optimization_3D_java.tog[e])
                    w = jcast('int', Code04_Cdq_Optimization_3D_java.weightg[e])
                    if ((not Code04_Cdq_Optimization_3D_java.vis[v]) and (Code04_Cdq_Optimization_3D_java.dist[v] > jcast('int', jadd(d, w)))):
                        Code04_Cdq_Optimization_3D_java.dist[v] = jcast('int', jcast('int', jadd(d, w)))
                        jcall(Code04_Cdq_Optimization_3D_java.heap, 'add', jarray('int', [None], [v, Code04_Cdq_Optimization_3D_java.dist[v]]))
                    e = jcast('int', Code04_Cdq_Optimization_3D_java.nextg[e])
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def dijkstra2(s, t):
        s = jcast('int', s)
        t = jcast('int', t)
        i = jcast('int', 1)
        while (i <= Code04_Cdq_Optimization_3D_java.n):
            Code04_Cdq_Optimization_3D_java.dist[i] = jcast('int', Code04_Cdq_Optimization_3D_java.INF)
            Code04_Cdq_Optimization_3D_java.vis[i] = jcast('boolean', False)
            i = jcast('int', (i + 1))
        jcall(Code04_Cdq_Optimization_3D_java.heap, 'clear')
        Code04_Cdq_Optimization_3D_java.dist[s] = jcast('int', 0)
        jcall(Code04_Cdq_Optimization_3D_java.heap, 'add', jarray('int', [None], [s, 0]))
        while (not jcall(Code04_Cdq_Optimization_3D_java.heap, 'isEmpty')):
            cur = jcall(Code04_Cdq_Optimization_3D_java.heap, 'poll')
            u = jcast('int', cur[0])
            d = jcast('int', cur[1])
            if (u == t):
                return jcast('int', d)
            if (not Code04_Cdq_Optimization_3D_java.vis[u]):
                Code04_Cdq_Optimization_3D_java.vis[u] = jcast('boolean', True)
                e = jcast('int', Code04_Cdq_Optimization_3D_java.head_2[u])
                while (e > 0):
                    v = jcast('int', Code04_Cdq_Optimization_3D_java.to_2[e])
                    w = jcast('int', Code04_Cdq_Optimization_3D_java.weight_2[e])
                    if ((not Code04_Cdq_Optimization_3D_java.vis[v]) and (Code04_Cdq_Optimization_3D_java.dist[v] > jcast('int', jadd(d, w)))):
                        Code04_Cdq_Optimization_3D_java.dist[v] = jcast('int', jcast('int', jadd(d, w)))
                        jcall(Code04_Cdq_Optimization_3D_java.heap, 'add', jarray('int', [None], [v, Code04_Cdq_Optimization_3D_java.dist[v]]))
                    e = jcast('int', Code04_Cdq_Optimization_3D_java.nxt_2[e])
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def random(v):
        v = jcast('int', v)
        return jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * v)), 1)))

    @staticmethod
    def _java_clear_1():
        i = jcast('int', 1)
        while (i <= Code04_Cdq_Optimization_3D_java.cntt):
            jset(Code04_Cdq_Optimization_3D_java.headg, i, jset(Code04_Cdq_Optimization_3D_java.headp, i, 0))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_Cdq_Optimization_3D_java.n):
            Code04_Cdq_Optimization_3D_java.head_2[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        Code04_Cdq_Optimization_3D_java.maxc = jcast('int', jset(Code04_Cdq_Optimization_3D_java, 'cnta', jset(Code04_Cdq_Optimization_3D_java, 'cntg', jset(Code04_Cdq_Optimization_3D_java, 'cntp', jset(Code04_Cdq_Optimization_3D_java, 'cntt', jset(Code04_Cdq_Optimization_3D_java, 'cnt_2', 0))))))

    @staticmethod
    def main(args):
        jprint('cdq优化建图，三维偏序', newline=True)
        jprint('=============', newline=True)
        Code04_Cdq_Optimization_3D_java.n = jcast('int', 100)
        Code04_Cdq_Optimization_3D_java.m = jcast('int', 1000)
        valMax = jcast('int', 10)
        weightMax = jcast('int', 10000)
        round = jcast('int', 20)
        t = jcast('int', 1)
        while (t <= round):
            jprint(jadd(jadd('第', t), '轮'), newline=True)
            jprint('测试开始', newline=True)
            i = jcast('int', 1)
            while (i <= Code04_Cdq_Optimization_3D_java.n):
                jset(Code04_Cdq_Optimization_3D_java.a, i, Code04_Cdq_Optimization_3D_java.random(valMax))
                jset(Code04_Cdq_Optimization_3D_java.b, i, Code04_Cdq_Optimization_3D_java.random(valMax))
                jset(Code04_Cdq_Optimization_3D_java.c, i, Code04_Cdq_Optimization_3D_java.random(valMax))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code04_Cdq_Optimization_3D_java.m):
                x = jcast('int', Code04_Cdq_Optimization_3D_java.random(Code04_Cdq_Optimization_3D_java.n))
                w = jcast('int', Code04_Cdq_Optimization_3D_java.random(weightMax))
                Code04_Cdq_Optimization_3D_java.addOp(x, x, w)
                Code04_Cdq_Optimization_3D_java.link(x, w)
                i = jcast('int', (i + 1))
            Code04_Cdq_Optimization_3D_java.buildGraph()
            x = jcast('int', 1)
            while (x <= Code04_Cdq_Optimization_3D_java.n):
                y = jcast('int', 1)
                while (y <= Code04_Cdq_Optimization_3D_java.n):
                    ans1 = jcast('int', Code04_Cdq_Optimization_3D_java.dijkstra(x, y))
                    ans2 = jcast('int', Code04_Cdq_Optimization_3D_java.dijkstra2(x, y))
                    if (ans1 != ans2):
                        jprint('出错了!', newline=True)
                    y = jcast('int', (y + 1))
                x = jcast('int', (x + 1))
            Code04_Cdq_Optimization_3D_java._java_clear_1()
            jprint('测试结束', newline=True)
            jprint('=======', newline=True)
            t = jcast('int', (t + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def clear(*args):
        _java_choice = jselect(args, [['int'], []], [False, False])
        if _java_choice == 0:
            return Code04_Cdq_Optimization_3D_java._java_clear_0(*args)
        if _java_choice == 1:
            return Code04_Cdq_Optimization_3D_java._java_clear_1(*args)
        raise TypeError("No matching overload for Code04_Cdq_Optimization_3D_java.clear")


Code04_Cdq_Optimization_3D_java.MAXN = jcast('int', 101)
Code04_Cdq_Optimization_3D_java.MAXM = jcast('int', 1001)
Code04_Cdq_Optimization_3D_java.MAXV = jcast('int', 10001)
Code04_Cdq_Optimization_3D_java.MAXT = jcast('int', 100001)
Code04_Cdq_Optimization_3D_java.MAXE = jcast('int', 100001)
Code04_Cdq_Optimization_3D_java.n = jcast('int', 0)
Code04_Cdq_Optimization_3D_java.m = jcast('int', 0)
Code04_Cdq_Optimization_3D_java.maxc = jcast('int', 0)
Code04_Cdq_Optimization_3D_java.cntt = jcast('int', 0)
Code04_Cdq_Optimization_3D_java.a = jarray('int', [Code04_Cdq_Optimization_3D_java.MAXN])
Code04_Cdq_Optimization_3D_java.b = jarray('int', [Code04_Cdq_Optimization_3D_java.MAXN])
Code04_Cdq_Optimization_3D_java.c = jarray('int', [Code04_Cdq_Optimization_3D_java.MAXN])
Code04_Cdq_Optimization_3D_java.arr = jarray('int', [Code04_Cdq_Optimization_3D_java.MAXN, 4])
Code04_Cdq_Optimization_3D_java.cnta = jcast('int', 0)
Code04_Cdq_Optimization_3D_java.headg = jarray('int', [Code04_Cdq_Optimization_3D_java.MAXT])
Code04_Cdq_Optimization_3D_java.nextg = jarray('int', [Code04_Cdq_Optimization_3D_java.MAXE])
Code04_Cdq_Optimization_3D_java.tog = jarray('int', [Code04_Cdq_Optimization_3D_java.MAXE])
Code04_Cdq_Optimization_3D_java.weightg = jarray('int', [Code04_Cdq_Optimization_3D_java.MAXE])
Code04_Cdq_Optimization_3D_java.cntg = jcast('int', 0)
Code04_Cdq_Optimization_3D_java.headp = jarray('int', [Code04_Cdq_Optimization_3D_java.MAXT])
Code04_Cdq_Optimization_3D_java.nextp = jarray('int', [jcast('int', (Code04_Cdq_Optimization_3D_java.MAXM << (1 & 31)))])
Code04_Cdq_Optimization_3D_java.top = jarray('int', [jcast('int', (Code04_Cdq_Optimization_3D_java.MAXM << (1 & 31)))])
Code04_Cdq_Optimization_3D_java.weightp = jarray('int', [jcast('int', (Code04_Cdq_Optimization_3D_java.MAXM << (1 & 31)))])
Code04_Cdq_Optimization_3D_java.cntp = jcast('int', 0)
Code04_Cdq_Optimization_3D_java.tree = jarray('int', [Code04_Cdq_Optimization_3D_java.MAXV])
Code04_Cdq_Optimization_3D_java.MAX_2 = jcast('int', 100001)
Code04_Cdq_Optimization_3D_java.head_2 = jarray('int', [Code04_Cdq_Optimization_3D_java.MAX_2])
Code04_Cdq_Optimization_3D_java.nxt_2 = jarray('int', [Code04_Cdq_Optimization_3D_java.MAX_2])
Code04_Cdq_Optimization_3D_java.to_2 = jarray('int', [Code04_Cdq_Optimization_3D_java.MAX_2])
Code04_Cdq_Optimization_3D_java.weight_2 = jarray('int', [Code04_Cdq_Optimization_3D_java.MAX_2])
Code04_Cdq_Optimization_3D_java.cnt_2 = jcast('int', 0)
Code04_Cdq_Optimization_3D_java.INF = jcast('int', 1000000001)
Code04_Cdq_Optimization_3D_java.dist = jarray('int', [Code04_Cdq_Optimization_3D_java.MAXT])
Code04_Cdq_Optimization_3D_java.vis = jarray('boolean', [Code04_Cdq_Optimization_3D_java.MAXT])
Code04_Cdq_Optimization_3D_java.heap = jnew('PriorityQueue', (lambda x, y: (x[1] - y[1])))

if __name__ == '__main__':
    Code04_Cdq_Optimization_3D_java.main([])
