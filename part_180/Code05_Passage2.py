# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 通道，Python版
# 三棵树t1、t2、t3都有n个节点，各自给定n-1条边以及每条边的边权，边权没有负数
# 点对(x, y)，要求两点必须不同，两点在树上的距离就是简单路径上边权的累加和
# 点对(x, y)，在t1、t2、t3的距离，分别记为dis1(x, y)、dis2(x, y)、dis3(x, y)
# 打印最大的dis1(x, y) + dis2(x, y) + dis3(x, y)
# 2 <= n <= 10^5
# 0 <= 边权 <= 10^12
# 测试链接 : https://www.luogu.com.cn/problem/P4220
# 测试链接 : https://loj.ac/p/2339
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Passage2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 'MAXT': 'MAXT', 'INF': 'INF', 'n': 'n', 'cntn': 'cntn', 'head0': 'head0', 'next0': 'next0', 'to0': 'to0', 'weight0': 'weight0', 'cnt0': 'cnt0', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'weight1': 'weight1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'weight2': 'weight2', 'cnt2': 'cnt2', 'head3': 'head3', 'next3': 'next3', 'to3': 'to3', 'weight3': 'weight3', 'cnt3': 'cnt3', 'dep2': 'dep2', 'dist3': 'dist3', 'vis': 'vis', 'siz': 'siz', 'dfn': 'dfn', 'lg2': 'lg2', 'rmq': 'rmq', 'cntd': 'cntd', 'up': 'up', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'lx': 'lx', 'ly': 'ly', 'lxv': 'lxv', 'lyv': 'lyv', 'rx': 'rx', 'ry': 'ry', 'rxv': 'rxv', 'ryv': 'ryv', 'cntt': 'cntt', 'ans': 'ans', 'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'av': 'av', 'bv': 'bv', 'cv': 'cv', 'dv': 'dv', 'x': 'x', 'y': 'y', 'xv': 'xv', 'yv': 'yv', 'bestDist': 'bestDist'}
    MAXN = 0
    MAXM = 0
    MAXP = 0
    MAXT = 0
    INF = 0
    n = 0
    cntn = 0
    head0 = None
    next0 = None
    to0 = None
    weight0 = None
    cnt0 = 0
    head1 = None
    next1 = None
    to1 = None
    weight1 = None
    cnt1 = 0
    head2 = None
    next2 = None
    to2 = None
    weight2 = None
    cnt2 = 0
    head3 = None
    next3 = None
    to3 = None
    weight3 = None
    cnt3 = 0
    dep2 = None
    dist3 = None
    vis = None
    siz = None
    dfn = None
    lg2 = None
    rmq = None
    cntd = 0
    up = None
    root = None
    ls = None
    rs = None
    lx = None
    ly = None
    lxv = None
    lyv = None
    rx = None
    ry = None
    rxv = None
    ryv = None
    cntt = 0
    ans = 0
    @staticmethod
    def addEdge0(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('long', w)
        jset(Code05_Passage2.next0, ((_java_obj_1 := Code05_Passage2), (_java_key_2 := 'cnt0'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_Passage2.head0[u])
        Code05_Passage2.to0[Code05_Passage2.cnt0] = jcast('int', v)
        Code05_Passage2.weight0[Code05_Passage2.cnt0] = jcast('long', w)
        Code05_Passage2.head0[u] = jcast('int', Code05_Passage2.cnt0)

    @staticmethod
    def addEdge1(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('long', w)
        jset(Code05_Passage2.next1, ((_java_obj_4 := Code05_Passage2), (_java_key_5 := 'cnt1'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code05_Passage2.head1[u])
        Code05_Passage2.to1[Code05_Passage2.cnt1] = jcast('int', v)
        Code05_Passage2.weight1[Code05_Passage2.cnt1] = jcast('long', w)
        Code05_Passage2.head1[u] = jcast('int', Code05_Passage2.cnt1)

    @staticmethod
    def addEdge2(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('long', w)
        jset(Code05_Passage2.next2, ((_java_obj_7 := Code05_Passage2), (_java_key_8 := 'cnt2'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], Code05_Passage2.head2[u])
        Code05_Passage2.to2[Code05_Passage2.cnt2] = jcast('int', v)
        Code05_Passage2.weight2[Code05_Passage2.cnt2] = jcast('long', w)
        Code05_Passage2.head2[u] = jcast('int', Code05_Passage2.cnt2)

    @staticmethod
    def addEdge3(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('long', w)
        jset(Code05_Passage2.next3, ((_java_obj_10 := Code05_Passage2), (_java_key_11 := 'cnt3'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], Code05_Passage2.head3[u])
        Code05_Passage2.to3[Code05_Passage2.cnt3] = jcast('int', v)
        Code05_Passage2.weight3[Code05_Passage2.cnt3] = jcast('long', w)
        Code05_Passage2.head3[u] = jcast('int', Code05_Passage2.cnt3)

    @staticmethod
    def dfsTree2(u, fa, dep):
        u = jcast('int', u)
        fa = jcast('int', fa)
        dep = jcast('long', dep)
        Code05_Passage2.dep2[u] = jcast('long', dep)
        e = jcast('int', Code05_Passage2.head2[u])
        while (e > 0):
            v = jcast('int', Code05_Passage2.to2[e])
            if (v != fa):
                Code05_Passage2.dfsTree2(v, u, jcast('long', jadd(dep, Code05_Passage2.weight2[e])))
            e = jcast('int', Code05_Passage2.next2[e])

    @staticmethod
    def rebuildTree1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        last = jcast('int', 0)
        e = jcast('int', Code05_Passage2.head0[u])
        while (e > 0):
            v = jcast('int', Code05_Passage2.to0[e])
            w = jcast('long', Code05_Passage2.weight0[e])
            if (v != fa):
                if (last == 0):
                    last = jcast('int', u)
                    Code05_Passage2.addEdge1(u, v, w)
                    Code05_Passage2.addEdge1(v, u, w)
                else:
                    add = jcast('int', ((_java_obj_13 := Code05_Passage2), (_java_key_14 := 'cntn'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
                    Code05_Passage2.addEdge1(last, add, 0)
                    Code05_Passage2.addEdge1(add, last, 0)
                    Code05_Passage2.addEdge1(add, v, w)
                    Code05_Passage2.addEdge1(v, add, w)
                    last = jcast('int', add)
                Code05_Passage2.rebuildTree1(v, u)
            e = jcast('int', Code05_Passage2.next0[e])

    @staticmethod
    def getSize(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code05_Passage2.siz[u] = jcast('int', 1)
        e = jcast('int', Code05_Passage2.head1[u])
        while (e > 0):
            v = jcast('int', Code05_Passage2.to1[e])
            if ((v != fa) and (not Code05_Passage2.vis[jcast('int', (e >> (1 & 31)))])):
                Code05_Passage2.getSize(v, u)
                Code05_Passage2.siz[u] = jcast('int', jcast('int', jadd(Code05_Passage2.siz[u], Code05_Passage2.siz[v])))
            e = jcast('int', Code05_Passage2.next1[e])

    @staticmethod
    def getCentroidEdge(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code05_Passage2.getSize(u, fa)
        total = jcast('int', Code05_Passage2.siz[u])
        half = jcast('int', jcast('int', (total >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code05_Passage2.head1[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code05_Passage2.to1[e])
                        if (((v != fa) and (not Code05_Passage2.vis[jcast('int', (e >> (1 & 31)))])) and (Code05_Passage2.siz[v] > half)):
                            fa = jcast('int', u)
                            u = jcast('int', v)
                            find = jcast('boolean', False)
                            raise JBreak(None)
                    except JContinue as _java_control_17:
                        if _java_control_17.label not in (None,):
                            raise
                    except JBreak as _java_control_17:
                        if _java_control_17.label not in (None,):
                            raise
                        break
                    e = jcast('int', Code05_Passage2.next1[e])
            except JContinue as _java_control_16:
                if _java_control_16.label not in (None,):
                    raise
            except JBreak as _java_control_16:
                if _java_control_16.label not in (None,):
                    raise
                break
        best = jcast('int', 0)
        edge = jcast('int', 0)
        e = jcast('int', Code05_Passage2.head1[u])
        while (e > 0):
            if (not Code05_Passage2.vis[jcast('int', (e >> (1 & 31)))]):
                v = jcast('int', Code05_Passage2.to1[e])
                sub = jcast('int', (jcast('int', (total - Code05_Passage2.siz[u])) if (v == fa) else Code05_Passage2.siz[v]))
                if (sub > best):
                    best = jcast('int', sub)
                    edge = jcast('int', e)
            e = jcast('int', Code05_Passage2.next1[e])
        return jcast('int', edge)

    @staticmethod
    def dfsTree1(u, fa, path, op):
        u = jcast('int', u)
        fa = jcast('int', fa)
        path = jcast('long', path)
        op = jcast('int', op)
        if (u <= Code05_Passage2.n):
            if (Code05_Passage2.up[u] == 0):
                jset(Code05_Passage2.up, u, ((_java_obj_18 := Code05_Passage2), (_java_key_19 := 'cntt'), (_java_old_20 := jget(_java_obj_18, _java_key_19)), jset(_java_obj_18, _java_key_19, jcast('int', (_java_old_20 + (1)))))[3])
                Code05_Passage2.root[u] = jcast('int', Code05_Passage2.cntt)
            cur = jcast('int', Code05_Passage2.up[u])
            nxt = jcast('int', ((_java_obj_21 := Code05_Passage2), (_java_key_22 := 'cntt'), (_java_old_23 := jget(_java_obj_21, _java_key_22)), jset(_java_obj_21, _java_key_22, jcast('int', (_java_old_23 + (1)))))[3])
            val = jcast('long', jcast('long', jadd(path, Code05_Passage2.dep2[u])))
            if (op == 0):
                Code05_Passage2.ls[cur] = jcast('int', nxt)
                jset(Code05_Passage2.lx, cur, jset(Code05_Passage2.ly, cur, u))
                jset(Code05_Passage2.lxv, cur, jset(Code05_Passage2.lyv, cur, val))
            else:
                Code05_Passage2.rs[cur] = jcast('int', nxt)
                jset(Code05_Passage2.rx, cur, jset(Code05_Passage2.ry, cur, u))
                jset(Code05_Passage2.rxv, cur, jset(Code05_Passage2.ryv, cur, val))
            Code05_Passage2.up[u] = jcast('int', nxt)
        e = jcast('int', Code05_Passage2.head1[u])
        while (e > 0):
            v = jcast('int', Code05_Passage2.to1[e])
            if ((v != fa) and (not Code05_Passage2.vis[jcast('int', (e >> (1 & 31)))])):
                Code05_Passage2.dfsTree1(v, u, jcast('long', jadd(path, Code05_Passage2.weight1[e])), op)
            e = jcast('int', Code05_Passage2.next1[e])

    @staticmethod
    def solveTree1(u):
        u = jcast('int', u)
        edge = jcast('int', Code05_Passage2.getCentroidEdge(u, 0))
        if (edge > 0):
            Code05_Passage2.vis[jcast('int', (edge >> (1 & 31)))] = jcast('boolean', True)
            v1 = jcast('int', Code05_Passage2.to1[edge])
            v2 = jcast('int', Code05_Passage2.to1[jcast('int', (edge ^ 1))])
            Code05_Passage2.dfsTree1(v1, 0, 0, 0)
            Code05_Passage2.dfsTree1(v2, 0, Code05_Passage2.weight1[edge], 1)
            Code05_Passage2.solveTree1(v1)
            Code05_Passage2.solveTree1(v2)

    @staticmethod
    def getUp(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('int', (x if (Code05_Passage2.dfn[x] < Code05_Passage2.dfn[y]) else y))

    @staticmethod
    def dfsTree3(u, fa, dist):
        u = jcast('int', u)
        fa = jcast('int', fa)
        dist = jcast('long', dist)
        jset(Code05_Passage2.dfn, u, ((_java_obj_24 := Code05_Passage2), (_java_key_25 := 'cntd'), (_java_old_26 := jget(_java_obj_24, _java_key_25)), jset(_java_obj_24, _java_key_25, jcast('int', (_java_old_26 + (1)))))[3])
        jset(Code05_Passage2.rmq[Code05_Passage2.dfn[u]], 0, fa)
        Code05_Passage2.dist3[u] = jcast('long', dist)
        e = jcast('int', Code05_Passage2.head3[u])
        while (e > 0):
            v = jcast('int', Code05_Passage2.to3[e])
            if (v != fa):
                Code05_Passage2.dfsTree3(v, u, jcast('long', jadd(dist, Code05_Passage2.weight3[e])))
            e = jcast('int', Code05_Passage2.next3[e])

    @staticmethod
    def rmqTree3():
        Code05_Passage2.dfsTree3(1, 0, 0)
        i = jcast('int', 2)
        while (i <= Code05_Passage2.n):
            Code05_Passage2.lg2[i] = jcast('int', jcast('int', jadd(Code05_Passage2.lg2[jcast('int', (i >> (1 & 31)))], 1)))
            i = jcast('int', (i + 1))
        pre = jcast('int', 0)
        cur = jcast('int', 1)
        while (cur <= Code05_Passage2.lg2[Code05_Passage2.n]):
            i = jcast('int', 1)
            while (jcast('int', (jcast('int', jadd(i, jcast('int', (1 << (cur & 31))))) - 1)) <= Code05_Passage2.n):
                jset(Code05_Passage2.rmq[i], cur, Code05_Passage2.getUp(Code05_Passage2.rmq[i][pre], Code05_Passage2.rmq[jcast('int', jadd(i, jcast('int', (1 << (pre & 31)))))][pre]))
                i = jcast('int', (i + 1))
            pre = jcast('int', (pre + 1))
            cur = jcast('int', (cur + 1))

    @staticmethod
    def lcaTree3(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        if (x == y):
            return jcast('int', x)
        x = jcast('int', Code05_Passage2.dfn[x])
        y = jcast('int', Code05_Passage2.dfn[y])
        if (x > y):
            tmp = jcast('int', x)
            x = jcast('int', y)
            y = jcast('int', tmp)
        x = jcast('int', (x + 1))
        k = jcast('int', Code05_Passage2.lg2[jcast('int', jadd(jcast('int', (y - x)), 1))])
        return jcast('int', Code05_Passage2.getUp(Code05_Passage2.rmq[x][k], Code05_Passage2.rmq[jcast('int', jadd(jcast('int', (y - jcast('int', (1 << (k & 31))))), 1))][k]))

    @staticmethod
    def getDist3(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('long', jcast('long', (jcast('long', jadd(Code05_Passage2.dist3[x], Code05_Passage2.dist3[y])) - jcast('long', (Code05_Passage2.dist3[Code05_Passage2.lcaTree3(x, y)] * 2)))))

    @staticmethod
    def getDist(x, y, xv, yv):
        x = jcast('int', x)
        y = jcast('int', y)
        xv = jcast('long', xv)
        yv = jcast('long', yv)
        if (x == y):
            return jcast('long', 0)
        return jcast('long', jcast('long', jadd(jcast('long', jadd(Code05_Passage2.getDist3(x, y), xv)), yv)))

    a = 0
    b = 0
    c = 0
    d = 0
    av = 0
    bv = 0
    cv = 0
    dv = 0
    @staticmethod
    def getInfo(i, j, iop, jop):
        i = jcast('int', i)
        j = jcast('int', j)
        iop = jcast('int', iop)
        jop = jcast('int', jop)
        if (iop == 0):
            Code05_Passage2.a = jcast('int', Code05_Passage2.lx[i])
            Code05_Passage2.b = jcast('int', Code05_Passage2.ly[i])
            Code05_Passage2.av = jcast('long', Code05_Passage2.lxv[i])
            Code05_Passage2.bv = jcast('long', Code05_Passage2.lyv[i])
        else:
            Code05_Passage2.a = jcast('int', Code05_Passage2.rx[i])
            Code05_Passage2.b = jcast('int', Code05_Passage2.ry[i])
            Code05_Passage2.av = jcast('long', Code05_Passage2.rxv[i])
            Code05_Passage2.bv = jcast('long', Code05_Passage2.ryv[i])
        if (jop == 0):
            Code05_Passage2.c = jcast('int', Code05_Passage2.lx[j])
            Code05_Passage2.d = jcast('int', Code05_Passage2.ly[j])
            Code05_Passage2.cv = jcast('long', Code05_Passage2.lxv[j])
            Code05_Passage2.dv = jcast('long', Code05_Passage2.lyv[j])
        else:
            Code05_Passage2.c = jcast('int', Code05_Passage2.rx[j])
            Code05_Passage2.d = jcast('int', Code05_Passage2.ry[j])
            Code05_Passage2.cv = jcast('long', Code05_Passage2.rxv[j])
            Code05_Passage2.dv = jcast('long', Code05_Passage2.ryv[j])

    @staticmethod
    def bestCross(i, j, iop, jop):
        i = jcast('int', i)
        j = jcast('int', j)
        iop = jcast('int', iop)
        jop = jcast('int', jop)
        Code05_Passage2.getInfo(i, j, iop, jop)
        p1 = jcast('long', Code05_Passage2.getDist(Code05_Passage2.a, Code05_Passage2.c, Code05_Passage2.av, Code05_Passage2.cv))
        p2 = jcast('long', Code05_Passage2.getDist(Code05_Passage2.a, Code05_Passage2.d, Code05_Passage2.av, Code05_Passage2.dv))
        p3 = jcast('long', Code05_Passage2.getDist(Code05_Passage2.b, Code05_Passage2.c, Code05_Passage2.bv, Code05_Passage2.cv))
        p4 = jcast('long', Code05_Passage2.getDist(Code05_Passage2.b, Code05_Passage2.d, Code05_Passage2.bv, Code05_Passage2.dv))
        return jcast('long', jstatic('Math', 'max', jstatic('Math', 'max', p1, p2), jstatic('Math', 'max', p3, p4)))

    x = 0
    y = 0
    xv = 0
    yv = 0
    bestDist = 0
    @staticmethod
    def better(curx, cury, curxv, curyv):
        curx = jcast('int', curx)
        cury = jcast('int', cury)
        curxv = jcast('long', curxv)
        curyv = jcast('long', curyv)
        if ((curx == 0) or (cury == 0)):
            return
        curDist = jcast('long', Code05_Passage2.getDist(curx, cury, curxv, curyv))
        if (curDist > Code05_Passage2.bestDist):
            Code05_Passage2.x = jcast('int', curx)
            Code05_Passage2.y = jcast('int', cury)
            Code05_Passage2.xv = jcast('long', curxv)
            Code05_Passage2.yv = jcast('long', curyv)
            Code05_Passage2.bestDist = jcast('long', curDist)

    @staticmethod
    def mergeInfo(i, j, op):
        i = jcast('int', i)
        j = jcast('int', j)
        op = jcast('int', op)
        Code05_Passage2.getInfo(i, j, op, op)
        Code05_Passage2.x = jcast('int', jset(Code05_Passage2, 'y', 0))
        Code05_Passage2.xv = jcast('long', jset(Code05_Passage2, 'yv', 0))
        Code05_Passage2.bestDist = jcast('long', jcast('long', (-Code05_Passage2.INF)))
        Code05_Passage2.better(Code05_Passage2.a, Code05_Passage2.b, Code05_Passage2.av, Code05_Passage2.bv)
        Code05_Passage2.better(Code05_Passage2.c, Code05_Passage2.d, Code05_Passage2.cv, Code05_Passage2.dv)
        Code05_Passage2.better(Code05_Passage2.a, Code05_Passage2.c, Code05_Passage2.av, Code05_Passage2.cv)
        Code05_Passage2.better(Code05_Passage2.a, Code05_Passage2.d, Code05_Passage2.av, Code05_Passage2.dv)
        Code05_Passage2.better(Code05_Passage2.b, Code05_Passage2.c, Code05_Passage2.bv, Code05_Passage2.cv)
        Code05_Passage2.better(Code05_Passage2.b, Code05_Passage2.d, Code05_Passage2.bv, Code05_Passage2.dv)
        if (op == 0):
            Code05_Passage2.lx[i] = jcast('int', Code05_Passage2.x)
            Code05_Passage2.ly[i] = jcast('int', Code05_Passage2.y)
            Code05_Passage2.lxv[i] = jcast('long', Code05_Passage2.xv)
            Code05_Passage2.lyv[i] = jcast('long', Code05_Passage2.yv)
        else:
            Code05_Passage2.rx[i] = jcast('int', Code05_Passage2.x)
            Code05_Passage2.ry[i] = jcast('int', Code05_Passage2.y)
            Code05_Passage2.rxv[i] = jcast('long', Code05_Passage2.xv)
            Code05_Passage2.ryv[i] = jcast('long', Code05_Passage2.yv)

    @staticmethod
    def mergeTree(i, j, add):
        i = jcast('int', i)
        j = jcast('int', j)
        add = jcast('long', add)
        if ((i == 0) or (j == 0)):
            return jcast('int', jcast('int', jadd(i, j)))
        if ((Code05_Passage2.ls[i] > 0) and (Code05_Passage2.rs[j] > 0)):
            Code05_Passage2.ans = jcast('long', jstatic('Math', 'max', Code05_Passage2.ans, jcast('long', jadd(Code05_Passage2.bestCross(i, j, 0, 1), add))))
        if ((Code05_Passage2.rs[i] > 0) and (Code05_Passage2.ls[j] > 0)):
            Code05_Passage2.ans = jcast('long', jstatic('Math', 'max', Code05_Passage2.ans, jcast('long', jadd(Code05_Passage2.bestCross(i, j, 1, 0), add))))
        Code05_Passage2.mergeInfo(i, j, 0)
        Code05_Passage2.mergeInfo(i, j, 1)
        jset(Code05_Passage2.ls, i, Code05_Passage2.mergeTree(Code05_Passage2.ls[i], Code05_Passage2.ls[j], add))
        jset(Code05_Passage2.rs, i, Code05_Passage2.mergeTree(Code05_Passage2.rs[i], Code05_Passage2.rs[j], add))
        return jcast('int', i)

    @staticmethod
    def compute(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        e = jcast('int', Code05_Passage2.head2[u])
        while (e > 0):
            v = jcast('int', Code05_Passage2.to2[e])
            if (v != fa):
                Code05_Passage2.compute(v, u)
                jset(Code05_Passage2.root, u, Code05_Passage2.mergeTree(Code05_Passage2.root[u], Code05_Passage2.root[v], jcast('long', (jcast('long', (-Code05_Passage2.dep2[u])) * 2))))
            e = jcast('int', Code05_Passage2.next2[e])

    @staticmethod
    def main(args):
        in_ = Code05_Passage2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_Passage2.n = jcast('int', jcall(in_, 'nextInt'))
        u = 0
        v = 0
        w = 0
        i = jcast('int', 1)
        while (i < Code05_Passage2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('long', jcall(in_, 'nextLong'))
            Code05_Passage2.addEdge0(u, v, w)
            Code05_Passage2.addEdge0(v, u, w)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < Code05_Passage2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('long', jcall(in_, 'nextLong'))
            Code05_Passage2.addEdge2(u, v, w)
            Code05_Passage2.addEdge2(v, u, w)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < Code05_Passage2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('long', jcall(in_, 'nextLong'))
            Code05_Passage2.addEdge3(u, v, w)
            Code05_Passage2.addEdge3(v, u, w)
            i = jcast('int', (i + 1))
        Code05_Passage2.cntn = jcast('int', Code05_Passage2.n)
        Code05_Passage2.cnt1 = jcast('int', 1)
        Code05_Passage2.ans = jcast('long', jcast('long', (-Code05_Passage2.INF)))
        Code05_Passage2.dfsTree2(1, 0, 0)
        Code05_Passage2.rebuildTree1(1, 0)
        Code05_Passage2.solveTree1(1)
        Code05_Passage2.rmqTree3()
        Code05_Passage2.compute(1, 0)
        jcall(out, 'println', Code05_Passage2.ans)
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len', 'in': 'in_'}
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        def _java_init_0(self, in_):
            self.in_ = in_

        def readByte(self):
            if (self.ptr >= self.len):
                self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
                self.ptr = jcast('int', 0)
                if (self.len <= 0):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', self.buffer[((_java_obj_27 := self), (_java_key_28 := 'ptr'), (_java_old_29 := jget(_java_obj_27, _java_key_28)), jset(_java_obj_27, _java_key_28, jcast('int', (_java_old_29 + (1)))), _java_old_29)[4]])

        def nextInt(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('int', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('int', (jcast('int', (-val)) if neg else val))

        def nextLong(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('long', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('long', jcast('long', jadd(jcast('long', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('long', (jcast('long', (-val)) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_Passage2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Passage2.MAXN = jcast('int', 100001)
Code05_Passage2.MAXM = jcast('int', jcast('int', (Code05_Passage2.MAXN << (1 & 31))))
Code05_Passage2.MAXP = jcast('int', 20)
Code05_Passage2.MAXT = jcast('int', jcast('int', (Code05_Passage2.MAXN * 20)))
Code05_Passage2.INF = jcast('long', jcast('long', (1 << (60 & 63))))
Code05_Passage2.n = jcast('int', 0)
Code05_Passage2.cntn = jcast('int', 0)
Code05_Passage2.head0 = jarray('int', [Code05_Passage2.MAXN])
Code05_Passage2.next0 = jarray('int', [jcast('int', (Code05_Passage2.MAXN << (1 & 31)))])
Code05_Passage2.to0 = jarray('int', [jcast('int', (Code05_Passage2.MAXN << (1 & 31)))])
Code05_Passage2.weight0 = jarray('long', [jcast('int', (Code05_Passage2.MAXN << (1 & 31)))])
Code05_Passage2.cnt0 = jcast('int', 0)
Code05_Passage2.head1 = jarray('int', [Code05_Passage2.MAXM])
Code05_Passage2.next1 = jarray('int', [jcast('int', (Code05_Passage2.MAXM << (1 & 31)))])
Code05_Passage2.to1 = jarray('int', [jcast('int', (Code05_Passage2.MAXM << (1 & 31)))])
Code05_Passage2.weight1 = jarray('long', [jcast('int', (Code05_Passage2.MAXM << (1 & 31)))])
Code05_Passage2.cnt1 = jcast('int', 0)
Code05_Passage2.head2 = jarray('int', [Code05_Passage2.MAXN])
Code05_Passage2.next2 = jarray('int', [jcast('int', (Code05_Passage2.MAXN << (1 & 31)))])
Code05_Passage2.to2 = jarray('int', [jcast('int', (Code05_Passage2.MAXN << (1 & 31)))])
Code05_Passage2.weight2 = jarray('long', [jcast('int', (Code05_Passage2.MAXN << (1 & 31)))])
Code05_Passage2.cnt2 = jcast('int', 0)
Code05_Passage2.head3 = jarray('int', [Code05_Passage2.MAXN])
Code05_Passage2.next3 = jarray('int', [jcast('int', (Code05_Passage2.MAXN << (1 & 31)))])
Code05_Passage2.to3 = jarray('int', [jcast('int', (Code05_Passage2.MAXN << (1 & 31)))])
Code05_Passage2.weight3 = jarray('long', [jcast('int', (Code05_Passage2.MAXN << (1 & 31)))])
Code05_Passage2.cnt3 = jcast('int', 0)
Code05_Passage2.dep2 = jarray('long', [Code05_Passage2.MAXN])
Code05_Passage2.dist3 = jarray('long', [Code05_Passage2.MAXN])
Code05_Passage2.vis = jarray('boolean', [Code05_Passage2.MAXM])
Code05_Passage2.siz = jarray('int', [Code05_Passage2.MAXM])
Code05_Passage2.dfn = jarray('int', [Code05_Passage2.MAXN])
Code05_Passage2.lg2 = jarray('int', [Code05_Passage2.MAXN])
Code05_Passage2.rmq = jarray('int', [Code05_Passage2.MAXN, Code05_Passage2.MAXP])
Code05_Passage2.cntd = jcast('int', 0)
Code05_Passage2.up = jarray('int', [Code05_Passage2.MAXN])
Code05_Passage2.root = jarray('int', [Code05_Passage2.MAXN])
Code05_Passage2.ls = jarray('int', [Code05_Passage2.MAXT])
Code05_Passage2.rs = jarray('int', [Code05_Passage2.MAXT])
Code05_Passage2.lx = jarray('int', [Code05_Passage2.MAXT])
Code05_Passage2.ly = jarray('int', [Code05_Passage2.MAXT])
Code05_Passage2.lxv = jarray('long', [Code05_Passage2.MAXT])
Code05_Passage2.lyv = jarray('long', [Code05_Passage2.MAXT])
Code05_Passage2.rx = jarray('int', [Code05_Passage2.MAXT])
Code05_Passage2.ry = jarray('int', [Code05_Passage2.MAXT])
Code05_Passage2.rxv = jarray('long', [Code05_Passage2.MAXT])
Code05_Passage2.ryv = jarray('long', [Code05_Passage2.MAXT])
Code05_Passage2.cntt = jcast('int', 0)
Code05_Passage2.ans = jcast('long', 0)
Code05_Passage2.a = jcast('int', 0)
Code05_Passage2.b = jcast('int', 0)
Code05_Passage2.c = jcast('int', 0)
Code05_Passage2.d = jcast('int', 0)
Code05_Passage2.av = jcast('long', 0)
Code05_Passage2.bv = jcast('long', 0)
Code05_Passage2.cv = jcast('long', 0)
Code05_Passage2.dv = jcast('long', 0)
Code05_Passage2.x = jcast('int', 0)
Code05_Passage2.y = jcast('int', 0)
Code05_Passage2.xv = jcast('long', 0)
Code05_Passage2.yv = jcast('long', 0)
Code05_Passage2.bestDist = jcast('long', 0)

if __name__ == '__main__':
    Code05_Passage2.main([])
