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

# 大工程，Python版
# 一共有n个节点，给定n-1条无向边，所有节点组成一棵树
# 如果在节点a和节点b之间建立新通道，那么代价是两个节点在树上的距离
# 一共有q条查询，每条查询格式如下
# 查询 k a1 a2 ... ak : 给出了k个不同的节点，任意两个节点之间都会建立新通道
# 打印新通道的代价和、新通道中代价最小的值、新通道中代价最大的值
# 1 <= n <= 10^6
# 1 <= q <= 5 * 10^4
# 1 <= 所有查询给出的点的总数 <= 2 * n
# 测试链接 : https://www.luogu.com.cn/problem/P4103
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_BigProject1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'INF': 'INF', 'n': 'n', 'q': 'q', 'k': 'k', 'headg': 'headg', 'nextg': 'nextg', 'tog': 'tog', 'cntg': 'cntg', 'headv': 'headv', 'nextv': 'nextv', 'tov': 'tov', 'cntv': 'cntv', 'dep': 'dep', 'dfn': 'dfn', 'stjump': 'stjump', 'cntd': 'cntd', 'arr': 'arr', 'isKey': 'isKey', 'tmp': 'tmp', 'stk': 'stk', 'siz': 'siz', 'sum': 'sum', 'near': 'near', 'far': 'far', 'costSum': 'costSum', 'costMin': 'costMin', 'costMax': 'costMax', 'ufe': 'ufe', 'stacksize': 'stacksize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    MAXP = 0
    INF = 0
    n = 0
    q = 0
    k = 0
    headg = None
    nextg = None
    tog = None
    cntg = 0
    headv = None
    nextv = None
    tov = None
    cntv = 0
    dep = None
    dfn = None
    stjump = None
    cntd = 0
    arr = None
    isKey = None
    tmp = None
    stk = None
    # siz[u]表示子树u上，关键点的数量
    # sum[u]表示子树u上，所有关键点到u的总距离
    # near[u]表示子树u上，到u最近关键点的距离
    # far[u]表示子树u上，到u最远关键点的距离
    siz = None
    sum = None
    near = None
    far = None
    # 新通道的代价和、新通道中代价最小的值、新通道中代价最大的值
    costSum = 0
    costMin = 0
    costMax = 0
    # dfs过程和dp过程：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    # 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    # 不会改迭代版，去看讲解118，详解了从递归版改迭代版
    # ufe不仅用于dfs改迭代，也用于dp改迭代
    ufe = None
    stacksize = 0
    u = 0
    f = 0
    e = 0
    @staticmethod
    def push(u, f, e):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', e)
        jset(Code02_BigProject1.ufe[Code02_BigProject1.stacksize], 0, u)
        jset(Code02_BigProject1.ufe[Code02_BigProject1.stacksize], 1, f)
        jset(Code02_BigProject1.ufe[Code02_BigProject1.stacksize], 2, e)
        Code02_BigProject1.stacksize = jcast('int', (Code02_BigProject1.stacksize + 1))

    @staticmethod
    def pop():
        Code02_BigProject1.stacksize = jcast('int', (Code02_BigProject1.stacksize - 1))
        Code02_BigProject1.u = jcast('int', Code02_BigProject1.ufe[Code02_BigProject1.stacksize][0])
        Code02_BigProject1.f = jcast('int', Code02_BigProject1.ufe[Code02_BigProject1.stacksize][1])
        Code02_BigProject1.e = jcast('int', Code02_BigProject1.ufe[Code02_BigProject1.stacksize][2])

    @staticmethod
    def addEdgeG(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_BigProject1.nextg, ((_java_obj_1 := Code02_BigProject1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_BigProject1.headg[u])
        Code02_BigProject1.tog[Code02_BigProject1.cntg] = jcast('int', v)
        Code02_BigProject1.headg[u] = jcast('int', Code02_BigProject1.cntg)

    @staticmethod
    def addEdgeV(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_BigProject1.nextv, ((_java_obj_4 := Code02_BigProject1), (_java_key_5 := 'cntv'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code02_BigProject1.headv[u])
        Code02_BigProject1.tov[Code02_BigProject1.cntv] = jcast('int', v)
        Code02_BigProject1.headv[u] = jcast('int', Code02_BigProject1.cntv)

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
            while (Code02_BigProject1.dfn[nums[i]] < Code02_BigProject1.dfn[pivot]):
                i = jcast('int', (i + 1))
            while (Code02_BigProject1.dfn[nums[j]] > Code02_BigProject1.dfn[pivot]):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', nums[i])
                nums[i] = jcast('int', nums[j])
                nums[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code02_BigProject1.sortByDfn(nums, l, j)
        Code02_BigProject1.sortByDfn(nums, i, r)

    # dfs递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code02_BigProject1.dep[u] = jcast('int', jcast('int', jadd(Code02_BigProject1.dep[fa], 1)))
        jset(Code02_BigProject1.dfn, u, ((_java_obj_7 := Code02_BigProject1), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
        jset(Code02_BigProject1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code02_BigProject1.MAXP):
            jset(Code02_BigProject1.stjump[u], p, Code02_BigProject1.stjump[Code02_BigProject1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code02_BigProject1.headg[u])
        while (e > 0):
            if (Code02_BigProject1.tog[e] != fa):
                Code02_BigProject1.dfs1(Code02_BigProject1.tog[e], u)
            e = jcast('int', Code02_BigProject1.nextg[e])

    # dfs1的迭代版
    @staticmethod
    def dfs2():
        Code02_BigProject1.stacksize = jcast('int', 0)
        Code02_BigProject1.push(1, 0, jcast('int', (-1)))
        while (Code02_BigProject1.stacksize > 0):
            Code02_BigProject1.pop()
            if (Code02_BigProject1.e == jcast('int', (-1))):
                Code02_BigProject1.dep[Code02_BigProject1.u] = jcast('int', jcast('int', jadd(Code02_BigProject1.dep[Code02_BigProject1.f], 1)))
                jset(Code02_BigProject1.dfn, Code02_BigProject1.u, ((_java_obj_10 := Code02_BigProject1), (_java_key_11 := 'cntd'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
                jset(Code02_BigProject1.stjump[Code02_BigProject1.u], 0, Code02_BigProject1.f)
                p = jcast('int', 1)
                while (p < Code02_BigProject1.MAXP):
                    jset(Code02_BigProject1.stjump[Code02_BigProject1.u], p, Code02_BigProject1.stjump[Code02_BigProject1.stjump[Code02_BigProject1.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code02_BigProject1.e = jcast('int', Code02_BigProject1.headg[Code02_BigProject1.u])
            else:
                Code02_BigProject1.e = jcast('int', Code02_BigProject1.nextg[Code02_BigProject1.e])
            if (Code02_BigProject1.e != 0):
                Code02_BigProject1.push(Code02_BigProject1.u, Code02_BigProject1.f, Code02_BigProject1.e)
                if (Code02_BigProject1.tog[Code02_BigProject1.e] != Code02_BigProject1.f):
                    Code02_BigProject1.push(Code02_BigProject1.tog[Code02_BigProject1.e], Code02_BigProject1.u, jcast('int', (-1)))

    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code02_BigProject1.dep[a] < Code02_BigProject1.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code02_BigProject1.MAXP - 1)))
        while (p >= 0):
            if (Code02_BigProject1.dep[Code02_BigProject1.stjump[a][p]] >= Code02_BigProject1.dep[b]):
                a = jcast('int', Code02_BigProject1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code02_BigProject1.MAXP - 1)))
        while (p >= 0):
            if (Code02_BigProject1.stjump[a][p] != Code02_BigProject1.stjump[b][p]):
                a = jcast('int', Code02_BigProject1.stjump[a][p])
                b = jcast('int', Code02_BigProject1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code02_BigProject1.stjump[a][0])

    # 二次排序 + LCA连边的方式建立虚树
    @staticmethod
    def buildVirtualTree1():
        Code02_BigProject1.sortByDfn(Code02_BigProject1.arr, 1, Code02_BigProject1.k)
        len = jcast('int', 0)
        i = jcast('int', 1)
        while (i < Code02_BigProject1.k):
            jset(Code02_BigProject1.tmp, (len := jcast('int', (len + (1)))), Code02_BigProject1.arr[i])
            jset(Code02_BigProject1.tmp, (len := jcast('int', (len + (1)))), Code02_BigProject1.getLca(Code02_BigProject1.arr[i], Code02_BigProject1.arr[jcast('int', jadd(i, 1))]))
            i = jcast('int', (i + 1))
        jset(Code02_BigProject1.tmp, (len := jcast('int', (len + (1)))), Code02_BigProject1.arr[Code02_BigProject1.k])
        Code02_BigProject1.sortByDfn(Code02_BigProject1.tmp, 1, len)
        unique = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= len):
            if (Code02_BigProject1.tmp[unique] != Code02_BigProject1.tmp[i]):
                jset(Code02_BigProject1.tmp, (unique := jcast('int', (unique + (1)))), Code02_BigProject1.tmp[i])
            i = jcast('int', (i + 1))
        Code02_BigProject1.cntv = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= unique):
            jset(Code02_BigProject1.headv, Code02_BigProject1.tmp[i], 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < unique):
            Code02_BigProject1.addEdgeV(Code02_BigProject1.getLca(Code02_BigProject1.tmp[i], Code02_BigProject1.tmp[jcast('int', jadd(i, 1))]), Code02_BigProject1.tmp[jcast('int', jadd(i, 1))])
            i = jcast('int', (i + 1))
        return jcast('int', Code02_BigProject1.tmp[1])

    # 单调栈的方式建立虚树
    @staticmethod
    def buildVirtualTree2():
        Code02_BigProject1.sortByDfn(Code02_BigProject1.arr, 1, Code02_BigProject1.k)
        Code02_BigProject1.cntv = jcast('int', 0)
        jset(Code02_BigProject1.headv, Code02_BigProject1.arr[1], 0)
        top = jcast('int', 0)
        jset(Code02_BigProject1.stk, (top := jcast('int', (top + (1)))), Code02_BigProject1.arr[1])
        i = jcast('int', 2)
        while (i <= Code02_BigProject1.k):
            x = jcast('int', Code02_BigProject1.arr[i])
            y = jcast('int', Code02_BigProject1.stk[top])
            lca = jcast('int', Code02_BigProject1.getLca(x, y))
            while ((top > 1) and (Code02_BigProject1.dfn[Code02_BigProject1.stk[jcast('int', (top - 1))]] >= Code02_BigProject1.dfn[lca])):
                Code02_BigProject1.addEdgeV(Code02_BigProject1.stk[jcast('int', (top - 1))], Code02_BigProject1.stk[top])
                top = jcast('int', (top - 1))
            if (lca != Code02_BigProject1.stk[top]):
                Code02_BigProject1.headv[lca] = jcast('int', 0)
                Code02_BigProject1.addEdgeV(lca, Code02_BigProject1.stk[top])
                Code02_BigProject1.stk[top] = jcast('int', lca)
            Code02_BigProject1.headv[x] = jcast('int', 0)
            jset(Code02_BigProject1.stk, (top := jcast('int', (top + (1)))), x)
            i = jcast('int', (i + 1))
        while (top > 1):
            Code02_BigProject1.addEdgeV(Code02_BigProject1.stk[jcast('int', (top - 1))], Code02_BigProject1.stk[top])
            top = jcast('int', (top - 1))
        return jcast('int', Code02_BigProject1.stk[1])

    # dp递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dp1(u):
        u = jcast('int', u)
        Code02_BigProject1.siz[u] = jcast('int', (1 if Code02_BigProject1.isKey[u] else 0))
        Code02_BigProject1.sum[u] = jcast('long', 0)
        if Code02_BigProject1.isKey[u]:
            jset(Code02_BigProject1.far, u, jset(Code02_BigProject1.near, u, 0))
        else:
            Code02_BigProject1.near[u] = jcast('long', Code02_BigProject1.INF)
            Code02_BigProject1.far[u] = jcast('long', jcast('long', (-Code02_BigProject1.INF)))
        e = jcast('int', Code02_BigProject1.headv[u])
        while (e > 0):
            Code02_BigProject1.dp1(Code02_BigProject1.tov[e])
            e = jcast('int', Code02_BigProject1.nextv[e])
        e = jcast('int', Code02_BigProject1.headv[u])
        while (e > 0):
            v = jcast('int', Code02_BigProject1.tov[e])
            len = jcast('long', jcast('int', (Code02_BigProject1.dep[v] - Code02_BigProject1.dep[u])))
            Code02_BigProject1.costSum = jcast('long', jcast('long', jadd(Code02_BigProject1.costSum, jcast('long', jadd(jcast('long', (jcast('long', jadd(Code02_BigProject1.sum[u], jcast('long', (jcast('long', (1 * Code02_BigProject1.siz[u])) * len)))) * Code02_BigProject1.siz[v])), jcast('long', (Code02_BigProject1.sum[v] * Code02_BigProject1.siz[u])))))))
            Code02_BigProject1.siz[u] = jcast('int', jcast('int', jadd(Code02_BigProject1.siz[u], Code02_BigProject1.siz[v])))
            Code02_BigProject1.sum[u] = jcast('long', jcast('long', jadd(Code02_BigProject1.sum[u], jcast('long', jadd(Code02_BigProject1.sum[v], jcast('long', (len * Code02_BigProject1.siz[v])))))))
            Code02_BigProject1.costMin = jcast('long', jstatic('Math', 'min', Code02_BigProject1.costMin, jcast('long', jadd(jcast('long', jadd(Code02_BigProject1.near[u], Code02_BigProject1.near[v])), len))))
            Code02_BigProject1.costMax = jcast('long', jstatic('Math', 'max', Code02_BigProject1.costMax, jcast('long', jadd(jcast('long', jadd(Code02_BigProject1.far[u], Code02_BigProject1.far[v])), len))))
            jset(Code02_BigProject1.near, u, jstatic('Math', 'min', Code02_BigProject1.near[u], jcast('long', jadd(Code02_BigProject1.near[v], len))))
            jset(Code02_BigProject1.far, u, jstatic('Math', 'max', Code02_BigProject1.far[u], jcast('long', jadd(Code02_BigProject1.far[v], len))))
            e = jcast('int', Code02_BigProject1.nextv[e])

    # dp1的迭代版
    @staticmethod
    def dp2(tree):
        tree = jcast('int', tree)
        Code02_BigProject1.stacksize = jcast('int', 0)
        Code02_BigProject1.push(tree, 0, jcast('int', (-1)))
        while (Code02_BigProject1.stacksize > 0):
            Code02_BigProject1.pop()
            if (Code02_BigProject1.e == jcast('int', (-1))):
                Code02_BigProject1.siz[Code02_BigProject1.u] = jcast('int', (1 if Code02_BigProject1.isKey[Code02_BigProject1.u] else 0))
                Code02_BigProject1.sum[Code02_BigProject1.u] = jcast('long', 0)
                if Code02_BigProject1.isKey[Code02_BigProject1.u]:
                    jset(Code02_BigProject1.far, Code02_BigProject1.u, jset(Code02_BigProject1.near, Code02_BigProject1.u, 0))
                else:
                    Code02_BigProject1.near[Code02_BigProject1.u] = jcast('long', Code02_BigProject1.INF)
                    Code02_BigProject1.far[Code02_BigProject1.u] = jcast('long', jcast('long', (-Code02_BigProject1.INF)))
                Code02_BigProject1.e = jcast('int', Code02_BigProject1.headv[Code02_BigProject1.u])
            else:
                Code02_BigProject1.e = jcast('int', Code02_BigProject1.nextv[Code02_BigProject1.e])
            if (Code02_BigProject1.e != 0):
                Code02_BigProject1.push(Code02_BigProject1.u, 0, Code02_BigProject1.e)
                Code02_BigProject1.push(Code02_BigProject1.tov[Code02_BigProject1.e], 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code02_BigProject1.headv[Code02_BigProject1.u])
                while (ei > 0):
                    v = jcast('int', Code02_BigProject1.tov[ei])
                    len = jcast('long', jcast('int', (Code02_BigProject1.dep[v] - Code02_BigProject1.dep[Code02_BigProject1.u])))
                    Code02_BigProject1.costSum = jcast('long', jcast('long', jadd(Code02_BigProject1.costSum, jcast('long', jadd(jcast('long', (jcast('long', jadd(Code02_BigProject1.sum[Code02_BigProject1.u], jcast('long', (jcast('long', (1 * Code02_BigProject1.siz[Code02_BigProject1.u])) * len)))) * Code02_BigProject1.siz[v])), jcast('long', (Code02_BigProject1.sum[v] * Code02_BigProject1.siz[Code02_BigProject1.u])))))))
                    Code02_BigProject1.siz[Code02_BigProject1.u] = jcast('int', jcast('int', jadd(Code02_BigProject1.siz[Code02_BigProject1.u], Code02_BigProject1.siz[v])))
                    Code02_BigProject1.sum[Code02_BigProject1.u] = jcast('long', jcast('long', jadd(Code02_BigProject1.sum[Code02_BigProject1.u], jcast('long', jadd(Code02_BigProject1.sum[v], jcast('long', (len * Code02_BigProject1.siz[v])))))))
                    Code02_BigProject1.costMin = jcast('long', jstatic('Math', 'min', Code02_BigProject1.costMin, jcast('long', jadd(jcast('long', jadd(Code02_BigProject1.near[Code02_BigProject1.u], Code02_BigProject1.near[v])), len))))
                    Code02_BigProject1.costMax = jcast('long', jstatic('Math', 'max', Code02_BigProject1.costMax, jcast('long', jadd(jcast('long', jadd(Code02_BigProject1.far[Code02_BigProject1.u], Code02_BigProject1.far[v])), len))))
                    jset(Code02_BigProject1.near, Code02_BigProject1.u, jstatic('Math', 'min', Code02_BigProject1.near[Code02_BigProject1.u], jcast('long', jadd(Code02_BigProject1.near[v], len))))
                    jset(Code02_BigProject1.far, Code02_BigProject1.u, jstatic('Math', 'max', Code02_BigProject1.far[Code02_BigProject1.u], jcast('long', jadd(Code02_BigProject1.far[v], len))))
                    ei = jcast('int', Code02_BigProject1.nextv[ei])

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code02_BigProject1.k):
            jset(Code02_BigProject1.isKey, Code02_BigProject1.arr[i], True)
            i = jcast('int', (i + 1))
        tree = jcast('int', Code02_BigProject1.buildVirtualTree1())
        # int tree = buildVirtualTree2();
        Code02_BigProject1.costSum = jcast('long', 0)
        Code02_BigProject1.costMin = jcast('long', Code02_BigProject1.INF)
        Code02_BigProject1.costMax = jcast('long', jcast('long', (-Code02_BigProject1.INF)))
        # dp1(tree);
        Code02_BigProject1.dp2(tree)
        i = jcast('int', 1)
        while (i <= Code02_BigProject1.k):
            jset(Code02_BigProject1.isKey, Code02_BigProject1.arr[i], False)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code02_BigProject1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_BigProject1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code02_BigProject1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code02_BigProject1.addEdgeG(u, v)
            Code02_BigProject1.addEdgeG(v, u)
            i = jcast('int', (i + 1))
        # dfs1(1, 0);
        Code02_BigProject1.dfs2()
        Code02_BigProject1.q = jcast('int', jcall(in_, 'nextInt'))
        t = jcast('int', 1)
        while (t <= Code02_BigProject1.q):
            Code02_BigProject1.k = jcast('int', jcall(in_, 'nextInt'))
            i = jcast('int', 1)
            while (i <= Code02_BigProject1.k):
                jset(Code02_BigProject1.arr, i, jcall(in_, 'nextInt'))
                i = jcast('int', (i + 1))
            Code02_BigProject1.compute()
            jcall(out, 'println', jadd(jadd(jadd(jadd(Code02_BigProject1.costSum, ' '), Code02_BigProject1.costMin), ' '), Code02_BigProject1.costMax))
            t = jcast('int', (t + 1))
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
            return jcast('int', self.buffer[((_java_obj_13 := self), (_java_key_14 := 'ptr'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))), _java_old_15)[4]])

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
            raise TypeError("No matching overload for Code02_BigProject1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_BigProject1.MAXN = jcast('int', 1000001)
Code02_BigProject1.MAXP = jcast('int', 20)
Code02_BigProject1.INF = jcast('long', jcast('long', (1 << (60 & 63))))
Code02_BigProject1.n = jcast('int', 0)
Code02_BigProject1.q = jcast('int', 0)
Code02_BigProject1.k = jcast('int', 0)
Code02_BigProject1.headg = jarray('int', [Code02_BigProject1.MAXN])
Code02_BigProject1.nextg = jarray('int', [jcast('int', (Code02_BigProject1.MAXN << (1 & 31)))])
Code02_BigProject1.tog = jarray('int', [jcast('int', (Code02_BigProject1.MAXN << (1 & 31)))])
Code02_BigProject1.cntg = jcast('int', 0)
Code02_BigProject1.headv = jarray('int', [Code02_BigProject1.MAXN])
Code02_BigProject1.nextv = jarray('int', [Code02_BigProject1.MAXN])
Code02_BigProject1.tov = jarray('int', [Code02_BigProject1.MAXN])
Code02_BigProject1.cntv = jcast('int', 0)
Code02_BigProject1.dep = jarray('int', [Code02_BigProject1.MAXN])
Code02_BigProject1.dfn = jarray('int', [Code02_BigProject1.MAXN])
Code02_BigProject1.stjump = jarray('int', [Code02_BigProject1.MAXN, Code02_BigProject1.MAXP])
Code02_BigProject1.cntd = jcast('int', 0)
Code02_BigProject1.arr = jarray('int', [Code02_BigProject1.MAXN])
Code02_BigProject1.isKey = jarray('boolean', [Code02_BigProject1.MAXN])
Code02_BigProject1.tmp = jarray('int', [jcast('int', (Code02_BigProject1.MAXN << (1 & 31)))])
Code02_BigProject1.stk = jarray('int', [Code02_BigProject1.MAXN])
Code02_BigProject1.siz = jarray('int', [Code02_BigProject1.MAXN])
Code02_BigProject1.sum = jarray('long', [Code02_BigProject1.MAXN])
Code02_BigProject1.near = jarray('long', [Code02_BigProject1.MAXN])
Code02_BigProject1.far = jarray('long', [Code02_BigProject1.MAXN])
Code02_BigProject1.costSum = jcast('long', 0)
Code02_BigProject1.costMin = jcast('long', 0)
Code02_BigProject1.costMax = jcast('long', 0)
Code02_BigProject1.ufe = jarray('int', [Code02_BigProject1.MAXN, 3])
Code02_BigProject1.stacksize = jcast('int', 0)
Code02_BigProject1.u = jcast('int', 0)
Code02_BigProject1.f = jcast('int', 0)
Code02_BigProject1.e = jcast('int', 0)

if __name__ == '__main__':
    Code02_BigProject1.main([])
