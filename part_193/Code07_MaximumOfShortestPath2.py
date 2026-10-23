# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最短路最大值，Python版
# 给定n个点、m条边的仙人掌图，每条边有边权，没有自环，可能有重边
# 一共q条查询，格式 k a1 a2 .. ak 含义如下
# 给定的k个点中，任意选两个点，可以选择相同点
# 打印它们之间最短路的最大值是多少
# 1 <= n、查询中k的总和 <= 3 * 10^5
# 测试链接 : https://uoj.ac/problem/87
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_MaximumOfShortestPath2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'q': 'q', 'k': 'k', 'cntn': 'cntn', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'weight1': 'weight1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'weight2': 'weight2', 'cnt2': 'cnt2', 'head3': 'head3', 'next3': 'next3', 'to3': 'to3', 'cnt3': 'cnt3', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'stasiz': 'stasiz', 'fromWeight': 'fromWeight', 'cycleLen': 'cycleLen', 'cycleSum': 'cycleSum', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'len': 'len', 'son': 'son', 'top': 'top', 'arr': 'arr', 'tmp': 'tmp', 'dist': 'dist', 'diameter': 'diameter', 'idx': 'idx', 'pre': 'pre', 'val': 'val', 'que': 'que'}
    MAXN = 0
    n = 0
    m = 0
    q = 0
    k = 0
    cntn = 0
    # 原图
    head1 = None
    next1 = None
    to1 = None
    weight1 = None
    cnt1 = 0
    # 圆方树
    head2 = None
    next2 = None
    to2 = None
    weight2 = None
    cnt2 = 0
    # 虚树
    head3 = None
    next3 = None
    to3 = None
    cnt3 = 0
    # dfn数组，tarjan和树剖都要使用
    dfn = None
    low = None
    cntd = 0
    sta = None
    stasiz = 0
    # 环的信息
    fromWeight = None
    cycleLen = None
    cycleSum = None
    # 树链剖分
    fa = None
    dep = None
    siz = None
    len = None
    son = None
    top = None
    # 批量节点
    arr = None
    tmp = None
    # dist[u] : 以u为头的树，u到任意点的最短路距离的最大值
    dist = None
    diameter = 0
    # 单调队列
    idx = None
    pre = None
    val = None
    que = None
    @staticmethod
    def addEdge1(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code07_MaximumOfShortestPath2.next1, ((_java_obj_1 := Code07_MaximumOfShortestPath2), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_MaximumOfShortestPath2.head1[u])
        Code07_MaximumOfShortestPath2.to1[Code07_MaximumOfShortestPath2.cnt1] = jcast('int', v)
        Code07_MaximumOfShortestPath2.weight1[Code07_MaximumOfShortestPath2.cnt1] = jcast('int', w)
        Code07_MaximumOfShortestPath2.head1[u] = jcast('int', Code07_MaximumOfShortestPath2.cnt1)

    @staticmethod
    def addEdge2(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('long', w)
        jset(Code07_MaximumOfShortestPath2.next2, ((_java_obj_4 := Code07_MaximumOfShortestPath2), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code07_MaximumOfShortestPath2.head2[u])
        Code07_MaximumOfShortestPath2.to2[Code07_MaximumOfShortestPath2.cnt2] = jcast('int', v)
        Code07_MaximumOfShortestPath2.weight2[Code07_MaximumOfShortestPath2.cnt2] = jcast('long', w)
        Code07_MaximumOfShortestPath2.head2[u] = jcast('int', Code07_MaximumOfShortestPath2.cnt2)

    @staticmethod
    def addEdge3(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_MaximumOfShortestPath2.next3, ((_java_obj_7 := Code07_MaximumOfShortestPath2), (_java_key_8 := 'cnt3'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], Code07_MaximumOfShortestPath2.head3[u])
        Code07_MaximumOfShortestPath2.to3[Code07_MaximumOfShortestPath2.cnt3] = jcast('int', v)
        Code07_MaximumOfShortestPath2.head3[u] = jcast('int', Code07_MaximumOfShortestPath2.cnt3)

    @staticmethod
    def sortByDfn(nums, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', nums[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        while (i <= j):
            while (Code07_MaximumOfShortestPath2.dfn[nums[i]] < Code07_MaximumOfShortestPath2.dfn[pivot]):
                i = jcast('int', (i + 1))
            while (Code07_MaximumOfShortestPath2.dfn[nums[j]] > Code07_MaximumOfShortestPath2.dfn[pivot]):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', nums[i])
                nums[i] = jcast('int', nums[j])
                nums[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code07_MaximumOfShortestPath2.sortByDfn(nums, l, j)
        Code07_MaximumOfShortestPath2.sortByDfn(nums, i, r)

    @staticmethod
    def sortByLen(nums, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', nums[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        while (i <= j):
            while (Code07_MaximumOfShortestPath2.cycleLen[nums[i]] < Code07_MaximumOfShortestPath2.cycleLen[pivot]):
                i = jcast('int', (i + 1))
            while (Code07_MaximumOfShortestPath2.cycleLen[nums[j]] > Code07_MaximumOfShortestPath2.cycleLen[pivot]):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', nums[i])
                nums[i] = jcast('int', nums[j])
                nums[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code07_MaximumOfShortestPath2.sortByLen(nums, l, j)
        Code07_MaximumOfShortestPath2.sortByLen(nums, i, r)

    @staticmethod
    def cycleLink(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code07_MaximumOfShortestPath2.cntn = jcast('int', (Code07_MaximumOfShortestPath2.cntn + 1))
        Code07_MaximumOfShortestPath2.cycleSum[Code07_MaximumOfShortestPath2.cntn] = jcast('long', Code07_MaximumOfShortestPath2.fromWeight[u])
        Code07_MaximumOfShortestPath2.addEdge2(u, Code07_MaximumOfShortestPath2.cntn, 0)
        tmp = jcast('int', Code07_MaximumOfShortestPath2.stasiz)
        pop = 0
        while True:
            pop = jcast('int', Code07_MaximumOfShortestPath2.sta[((_java_old_10 := tmp), (tmp := jcast('int', (tmp + (-1)))), _java_old_10)[2]])
            Code07_MaximumOfShortestPath2.cycleLen[pop] = jcast('long', Code07_MaximumOfShortestPath2.cycleSum[Code07_MaximumOfShortestPath2.cntn])
            Code07_MaximumOfShortestPath2.cycleSum[Code07_MaximumOfShortestPath2.cntn] = jcast('long', jcast('long', jadd(Code07_MaximumOfShortestPath2.cycleSum[Code07_MaximumOfShortestPath2.cntn], Code07_MaximumOfShortestPath2.fromWeight[pop])))
            if not ((pop != v)):
                break
        while True:
            pop = jcast('int', Code07_MaximumOfShortestPath2.sta[((_java_obj_11 := Code07_MaximumOfShortestPath2), (_java_key_12 := 'stasiz'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (-1)))), _java_old_13)[4]])
            Code07_MaximumOfShortestPath2.addEdge2(Code07_MaximumOfShortestPath2.cntn, pop, jstatic('Math', 'min', Code07_MaximumOfShortestPath2.cycleLen[pop], jcast('long', (Code07_MaximumOfShortestPath2.cycleSum[Code07_MaximumOfShortestPath2.cntn] - Code07_MaximumOfShortestPath2.cycleLen[pop]))))
            if not ((pop != v)):
                break

    @staticmethod
    def tarjan(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code07_MaximumOfShortestPath2.dfn, u, jset(Code07_MaximumOfShortestPath2.low, u, ((_java_obj_14 := Code07_MaximumOfShortestPath2), (_java_key_15 := 'cntd'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))))[3]))
        jset(Code07_MaximumOfShortestPath2.sta, ((_java_obj_17 := Code07_MaximumOfShortestPath2), (_java_key_18 := 'stasiz'), (_java_old_19 := jget(_java_obj_17, _java_key_18)), jset(_java_obj_17, _java_key_18, jcast('int', (_java_old_19 + (1)))))[3], u)
        e = jcast('int', Code07_MaximumOfShortestPath2.head1[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code07_MaximumOfShortestPath2.to1[e])
                w = jcast('long', Code07_MaximumOfShortestPath2.weight1[e])
                if (Code07_MaximumOfShortestPath2.dfn[v] == 0):
                    Code07_MaximumOfShortestPath2.tarjan(v, e)
                    Code07_MaximumOfShortestPath2.fromWeight[v] = jcast('long', w)
                    if (Code07_MaximumOfShortestPath2.low[v] < Code07_MaximumOfShortestPath2.dfn[u]):
                        jset(Code07_MaximumOfShortestPath2.low, u, jstatic('Math', 'min', Code07_MaximumOfShortestPath2.low[u], Code07_MaximumOfShortestPath2.low[v]))
                    else:
                        if (Code07_MaximumOfShortestPath2.low[v] > Code07_MaximumOfShortestPath2.dfn[u]):
                            Code07_MaximumOfShortestPath2.stasiz = jcast('int', (Code07_MaximumOfShortestPath2.stasiz - 1))
                            Code07_MaximumOfShortestPath2.addEdge2(u, v, w)
                        else:
                            Code07_MaximumOfShortestPath2.cycleLink(u, v)
                else:
                    if (Code07_MaximumOfShortestPath2.dfn[v] < Code07_MaximumOfShortestPath2.dfn[u]):
                        Code07_MaximumOfShortestPath2.fromWeight[v] = jcast('long', w)
                        jset(Code07_MaximumOfShortestPath2.low, u, jstatic('Math', 'min', Code07_MaximumOfShortestPath2.low[u], Code07_MaximumOfShortestPath2.dfn[v]))
            except JContinue as _java_control_20:
                if _java_control_20.label not in (None,):
                    raise
            except JBreak as _java_control_20:
                if _java_control_20.label not in (None,):
                    raise
                break
            e = jcast('int', Code07_MaximumOfShortestPath2.next1[e])

    @staticmethod
    def dfs1(u, f, l):
        u = jcast('int', u)
        f = jcast('int', f)
        l = jcast('long', l)
        Code07_MaximumOfShortestPath2.fa[u] = jcast('int', f)
        Code07_MaximumOfShortestPath2.dep[u] = jcast('int', jcast('int', jadd(Code07_MaximumOfShortestPath2.dep[f], 1)))
        Code07_MaximumOfShortestPath2.siz[u] = jcast('int', 1)
        Code07_MaximumOfShortestPath2.len[u] = jcast('long', l)
        e = jcast('int', Code07_MaximumOfShortestPath2.head2[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code07_MaximumOfShortestPath2.to2[e])
            if (v != f):
                Code07_MaximumOfShortestPath2.dfs1(v, u, jcast('long', jadd(Code07_MaximumOfShortestPath2.len[u], Code07_MaximumOfShortestPath2.weight2[e])))
                Code07_MaximumOfShortestPath2.siz[u] = jcast('int', jcast('int', jadd(Code07_MaximumOfShortestPath2.siz[u], Code07_MaximumOfShortestPath2.siz[v])))
                if ((Code07_MaximumOfShortestPath2.son[u] == 0) or (Code07_MaximumOfShortestPath2.siz[Code07_MaximumOfShortestPath2.son[u]] < Code07_MaximumOfShortestPath2.siz[v])):
                    Code07_MaximumOfShortestPath2.son[u] = jcast('int', v)
            e = jcast('int', Code07_MaximumOfShortestPath2.next2[e])

    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code07_MaximumOfShortestPath2.top[u] = jcast('int', t)
        jset(Code07_MaximumOfShortestPath2.dfn, u, ((_java_obj_21 := Code07_MaximumOfShortestPath2), (_java_key_22 := 'cntd'), (_java_old_23 := jget(_java_obj_21, _java_key_22)), jset(_java_obj_21, _java_key_22, jcast('int', (_java_old_23 + (1)))))[3])
        if (Code07_MaximumOfShortestPath2.son[u] != 0):
            Code07_MaximumOfShortestPath2.dfs2(Code07_MaximumOfShortestPath2.son[u], t)
        e = jcast('int', Code07_MaximumOfShortestPath2.head2[u])
        while (e > 0):
            v = jcast('int', Code07_MaximumOfShortestPath2.to2[e])
            if ((v != Code07_MaximumOfShortestPath2.fa[u]) and (v != Code07_MaximumOfShortestPath2.son[u])):
                Code07_MaximumOfShortestPath2.dfs2(v, v)
            e = jcast('int', Code07_MaximumOfShortestPath2.next2[e])

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        while (Code07_MaximumOfShortestPath2.top[a] != Code07_MaximumOfShortestPath2.top[b]):
            if (Code07_MaximumOfShortestPath2.dep[Code07_MaximumOfShortestPath2.top[a]] <= Code07_MaximumOfShortestPath2.dep[Code07_MaximumOfShortestPath2.top[b]]):
                b = jcast('int', Code07_MaximumOfShortestPath2.fa[Code07_MaximumOfShortestPath2.top[b]])
            else:
                a = jcast('int', Code07_MaximumOfShortestPath2.fa[Code07_MaximumOfShortestPath2.top[a]])
        return jcast('int', (a if (Code07_MaximumOfShortestPath2.dep[a] <= Code07_MaximumOfShortestPath2.dep[b]) else b))

    @staticmethod
    def find(x, square):
        x = jcast('int', x)
        square = jcast('int', square)
        pre = jcast('int', 0)
        while (Code07_MaximumOfShortestPath2.top[x] != Code07_MaximumOfShortestPath2.top[square]):
            pre = jcast('int', Code07_MaximumOfShortestPath2.top[x])
            x = jcast('int', Code07_MaximumOfShortestPath2.fa[pre])
        return jcast('int', (pre if (x == square) else Code07_MaximumOfShortestPath2.son[square]))

    # 虚树的建立方式，二次排序 + 相邻LCA连边
    @staticmethod
    def buildVirtualTree():
        Code07_MaximumOfShortestPath2.sortByDfn(Code07_MaximumOfShortestPath2.arr, 1, Code07_MaximumOfShortestPath2.k)
        len = jcast('int', 0)
        i = jcast('int', 1)
        while (i < Code07_MaximumOfShortestPath2.k):
            jset(Code07_MaximumOfShortestPath2.tmp, (len := jcast('int', (len + (1)))), Code07_MaximumOfShortestPath2.arr[i])
            jset(Code07_MaximumOfShortestPath2.tmp, (len := jcast('int', (len + (1)))), Code07_MaximumOfShortestPath2.lca(Code07_MaximumOfShortestPath2.arr[i], Code07_MaximumOfShortestPath2.arr[jcast('int', jadd(i, 1))]))
            i = jcast('int', (i + 1))
        jset(Code07_MaximumOfShortestPath2.tmp, (len := jcast('int', (len + (1)))), Code07_MaximumOfShortestPath2.arr[Code07_MaximumOfShortestPath2.k])
        Code07_MaximumOfShortestPath2.sortByDfn(Code07_MaximumOfShortestPath2.tmp, 1, len)
        unique = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= len):
            if (Code07_MaximumOfShortestPath2.tmp[unique] != Code07_MaximumOfShortestPath2.tmp[i]):
                jset(Code07_MaximumOfShortestPath2.tmp, (unique := jcast('int', (unique + (1)))), Code07_MaximumOfShortestPath2.tmp[i])
            i = jcast('int', (i + 1))
        Code07_MaximumOfShortestPath2.cnt3 = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= unique):
            jset(Code07_MaximumOfShortestPath2.head3, Code07_MaximumOfShortestPath2.tmp[i], 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < unique):
            Code07_MaximumOfShortestPath2.addEdge3(Code07_MaximumOfShortestPath2.lca(Code07_MaximumOfShortestPath2.tmp[i], Code07_MaximumOfShortestPath2.tmp[jcast('int', jadd(i, 1))]), Code07_MaximumOfShortestPath2.tmp[jcast('int', jadd(i, 1))])
            i = jcast('int', (i + 1))
        return jcast('int', Code07_MaximumOfShortestPath2.tmp[1])

    @staticmethod
    def computeOnCycle(u, siz):
        u = jcast('int', u)
        siz = jcast('int', siz)
        Code07_MaximumOfShortestPath2.sortByLen(Code07_MaximumOfShortestPath2.idx, 1, siz)
        i = jcast('int', 1)
        while (i <= siz):
            Code07_MaximumOfShortestPath2.pre[i] = jcast('long', Code07_MaximumOfShortestPath2.cycleLen[Code07_MaximumOfShortestPath2.idx[i]])
            Code07_MaximumOfShortestPath2.pre[jcast('int', jadd(i, siz))] = jcast('long', jcast('long', jadd(Code07_MaximumOfShortestPath2.pre[i], Code07_MaximumOfShortestPath2.cycleSum[u])))
            Code07_MaximumOfShortestPath2.val[i] = jcast('long', Code07_MaximumOfShortestPath2.dist[Code07_MaximumOfShortestPath2.idx[i]])
            Code07_MaximumOfShortestPath2.val[jcast('int', jadd(i, siz))] = jcast('long', Code07_MaximumOfShortestPath2.val[i])
            i = jcast('int', (i + 1))
        l = jcast('int', 1)
        r = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= jcast('int', (siz * 2))):
            while ((l <= r) and (jcast('long', (jcast('long', (Code07_MaximumOfShortestPath2.pre[i] - Code07_MaximumOfShortestPath2.pre[Code07_MaximumOfShortestPath2.que[l]])) * 2)) > Code07_MaximumOfShortestPath2.cycleSum[u])):
                l = jcast('int', (l + 1))
            if (l <= r):
                Code07_MaximumOfShortestPath2.diameter = jcast('long', jstatic('Math', 'max', Code07_MaximumOfShortestPath2.diameter, jcast('long', jadd(jcast('long', jadd(jcast('long', (Code07_MaximumOfShortestPath2.val[Code07_MaximumOfShortestPath2.que[l]] - Code07_MaximumOfShortestPath2.pre[Code07_MaximumOfShortestPath2.que[l]])), Code07_MaximumOfShortestPath2.val[i])), Code07_MaximumOfShortestPath2.pre[i]))))
            while ((l <= r) and (jcast('long', (Code07_MaximumOfShortestPath2.val[Code07_MaximumOfShortestPath2.que[r]] - Code07_MaximumOfShortestPath2.pre[Code07_MaximumOfShortestPath2.que[r]])) <= jcast('long', (Code07_MaximumOfShortestPath2.val[i] - Code07_MaximumOfShortestPath2.pre[i])))):
                r = jcast('int', (r - 1))
            jset(Code07_MaximumOfShortestPath2.que, (r := jcast('int', (r + (1)))), i)
            i = jcast('int', (i + 1))

    @staticmethod
    def dpOnTree(u):
        u = jcast('int', u)
        Code07_MaximumOfShortestPath2.dist[u] = jcast('long', 0)
        if (u <= Code07_MaximumOfShortestPath2.n):
            e = jcast('int', Code07_MaximumOfShortestPath2.head3[u])
            while (e > 0):
                v = jcast('int', Code07_MaximumOfShortestPath2.to3[e])
                Code07_MaximumOfShortestPath2.dpOnTree(v)
                Code07_MaximumOfShortestPath2.diameter = jcast('long', jstatic('Math', 'max', Code07_MaximumOfShortestPath2.diameter, jcast('long', (jcast('long', jadd(jcast('long', jadd(Code07_MaximumOfShortestPath2.dist[u], Code07_MaximumOfShortestPath2.dist[v])), Code07_MaximumOfShortestPath2.len[v])) - Code07_MaximumOfShortestPath2.len[u]))))
                jset(Code07_MaximumOfShortestPath2.dist, u, jstatic('Math', 'max', Code07_MaximumOfShortestPath2.dist[u], jcast('long', (jcast('long', jadd(Code07_MaximumOfShortestPath2.dist[v], Code07_MaximumOfShortestPath2.len[v])) - Code07_MaximumOfShortestPath2.len[u]))))
                e = jcast('int', Code07_MaximumOfShortestPath2.next3[e])
        else:
            e = jcast('int', Code07_MaximumOfShortestPath2.head3[u])
            while (e > 0):
                v = jcast('int', Code07_MaximumOfShortestPath2.to3[e])
                Code07_MaximumOfShortestPath2.dpOnTree(v)
                e = jcast('int', Code07_MaximumOfShortestPath2.next3[e])
            # 注意，下面的for循环，不能和上面的for循环合并处理
            # 因为idx是全局数组，此时u是方点，会收集环上的相关节点
            # 如果边递归边收集idx，那么当前已经写入的idx[1..siz]
            # 可能会被孩子的递归过程覆盖掉，导致idx收集脏数据
            # 所以先执行所有孩子的递归，再收集环上节点
            siz = jcast('int', 0)
            e = jcast('int', Code07_MaximumOfShortestPath2.head3[u])
            while (e > 0):
                v = jcast('int', Code07_MaximumOfShortestPath2.to3[e])
                f = jcast('int', Code07_MaximumOfShortestPath2.find(v, u))
                Code07_MaximumOfShortestPath2.dist[f] = jcast('long', jcast('long', (jcast('long', jadd(Code07_MaximumOfShortestPath2.dist[v], Code07_MaximumOfShortestPath2.len[v])) - Code07_MaximumOfShortestPath2.len[f])))
                jset(Code07_MaximumOfShortestPath2.idx, (siz := jcast('int', (siz + (1)))), f)
                jset(Code07_MaximumOfShortestPath2.dist, u, jstatic('Math', 'max', Code07_MaximumOfShortestPath2.dist[u], jcast('long', (jcast('long', jadd(Code07_MaximumOfShortestPath2.dist[v], Code07_MaximumOfShortestPath2.len[v])) - Code07_MaximumOfShortestPath2.len[u]))))
                e = jcast('int', Code07_MaximumOfShortestPath2.next3[e])
            Code07_MaximumOfShortestPath2.computeOnCycle(u, siz)

    @staticmethod
    def main(args):
        in_ = Code07_MaximumOfShortestPath2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_MaximumOfShortestPath2.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_MaximumOfShortestPath2.m = jcast('int', jcall(in_, 'nextInt'))
        Code07_MaximumOfShortestPath2.cntn = jcast('int', Code07_MaximumOfShortestPath2.n)
        Code07_MaximumOfShortestPath2.cnt1 = jcast('int', 1)
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i <= Code07_MaximumOfShortestPath2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code07_MaximumOfShortestPath2.addEdge1(u, v, w)
            Code07_MaximumOfShortestPath2.addEdge1(v, u, w)
            i = jcast('int', (i + 1))
        Code07_MaximumOfShortestPath2.tarjan(1, 0)
        Code07_MaximumOfShortestPath2.cntd = jcast('int', 0)
        Code07_MaximumOfShortestPath2.dfs1(1, 0, 0)
        Code07_MaximumOfShortestPath2.dfs2(1, 1)
        Code07_MaximumOfShortestPath2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_MaximumOfShortestPath2.q):
            Code07_MaximumOfShortestPath2.k = jcast('int', jcall(in_, 'nextInt'))
            j = jcast('int', 1)
            while (j <= Code07_MaximumOfShortestPath2.k):
                jset(Code07_MaximumOfShortestPath2.arr, j, jcall(in_, 'nextInt'))
                j = jcast('int', (j + 1))
            Code07_MaximumOfShortestPath2.diameter = jcast('long', 0)
            tree = jcast('int', Code07_MaximumOfShortestPath2.buildVirtualTree())
            Code07_MaximumOfShortestPath2.dpOnTree(tree)
            jcall(out, 'println', Code07_MaximumOfShortestPath2.diameter)
            i = jcast('int', (i + 1))
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
            return jcast('int', self.buffer[((_java_obj_24 := self), (_java_key_25 := 'ptr'), (_java_old_26 := jget(_java_obj_24, _java_key_25)), jset(_java_obj_24, _java_key_25, jcast('int', (_java_old_26 + (1)))), _java_old_26)[4]])

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

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code07_MaximumOfShortestPath2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_MaximumOfShortestPath2.MAXN = jcast('int', 600001)
Code07_MaximumOfShortestPath2.n = jcast('int', 0)
Code07_MaximumOfShortestPath2.m = jcast('int', 0)
Code07_MaximumOfShortestPath2.q = jcast('int', 0)
Code07_MaximumOfShortestPath2.k = jcast('int', 0)
Code07_MaximumOfShortestPath2.cntn = jcast('int', 0)
Code07_MaximumOfShortestPath2.head1 = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.next1 = jarray('int', [jcast('int', (Code07_MaximumOfShortestPath2.MAXN << (1 & 31)))])
Code07_MaximumOfShortestPath2.to1 = jarray('int', [jcast('int', (Code07_MaximumOfShortestPath2.MAXN << (1 & 31)))])
Code07_MaximumOfShortestPath2.weight1 = jarray('int', [jcast('int', (Code07_MaximumOfShortestPath2.MAXN << (1 & 31)))])
Code07_MaximumOfShortestPath2.cnt1 = jcast('int', 0)
Code07_MaximumOfShortestPath2.head2 = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.next2 = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.to2 = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.weight2 = jarray('long', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.cnt2 = jcast('int', 0)
Code07_MaximumOfShortestPath2.head3 = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.next3 = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.to3 = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.cnt3 = jcast('int', 0)
Code07_MaximumOfShortestPath2.dfn = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.low = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.cntd = jcast('int', 0)
Code07_MaximumOfShortestPath2.sta = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.stasiz = jcast('int', 0)
Code07_MaximumOfShortestPath2.fromWeight = jarray('long', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.cycleLen = jarray('long', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.cycleSum = jarray('long', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.fa = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.dep = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.siz = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.len = jarray('long', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.son = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.top = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.arr = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.tmp = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.dist = jarray('long', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.diameter = jcast('long', 0)
Code07_MaximumOfShortestPath2.idx = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.pre = jarray('long', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.val = jarray('long', [Code07_MaximumOfShortestPath2.MAXN])
Code07_MaximumOfShortestPath2.que = jarray('int', [Code07_MaximumOfShortestPath2.MAXN])

if __name__ == '__main__':
    Code07_MaximumOfShortestPath2.main([])
