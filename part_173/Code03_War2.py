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

# 消耗战，Python版
# 一共有n个节点，给定n-1条无向边，每条边有边权，所有节点组成一棵树
# 一共有q条查询，每条查询格式如下
# 查询 k a1 a2 ... ak : 给出了k个不同的关键节点，并且一定不包含1号节点
# 你可以随意选择边进行切断，切断的代价就是边权
# 目的是让所有关键点都无法到达1号节点，打印最小总代价
# 1 <= n、q <= 5 * 10^5
# 1 <= 所有查询给出的点的总数 <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P2495
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_War2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'n': 'n', 'q': 'q', 'k': 'k', 'headg': 'headg', 'nextg': 'nextg', 'tog': 'tog', 'weightg': 'weightg', 'cntg': 'cntg', 'headv': 'headv', 'nextv': 'nextv', 'tov': 'tov', 'weightv': 'weightv', 'cntv': 'cntv', 'dep': 'dep', 'dfn': 'dfn', 'stjump': 'stjump', 'mindist': 'mindist', 'cntd': 'cntd', 'arr': 'arr', 'isKey': 'isKey', 'tmp': 'tmp', 'stk': 'stk', 'cost': 'cost'}
    MAXN = 0
    MAXP = 0
    n = 0
    q = 0
    k = 0
    headg = None
    nextg = None
    tog = None
    weightg = None
    cntg = 0
    headv = None
    nextv = None
    tov = None
    weightv = None
    cntv = 0
    dep = None
    dfn = None
    stjump = None
    # 上方最小距离的倍增表
    mindist = None
    cntd = 0
    arr = None
    isKey = None
    tmp = None
    stk = None
    # cost[u]表示虚树中，u下方的所有关键节点，都连不上u的话，最小总代价
    cost = None
    @staticmethod
    def addEdgeG(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code03_War2.nextg, ((_java_obj_1 := Code03_War2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_War2.headg[u])
        Code03_War2.tog[Code03_War2.cntg] = jcast('int', v)
        Code03_War2.weightg[Code03_War2.cntg] = jcast('int', w)
        Code03_War2.headg[u] = jcast('int', Code03_War2.cntg)

    @staticmethod
    def addEdgeV(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code03_War2.nextv, ((_java_obj_4 := Code03_War2), (_java_key_5 := 'cntv'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code03_War2.headv[u])
        Code03_War2.tov[Code03_War2.cntv] = jcast('int', v)
        Code03_War2.weightv[Code03_War2.cntv] = jcast('int', w)
        Code03_War2.headv[u] = jcast('int', Code03_War2.cntv)

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
            while (Code03_War2.dfn[nums[i]] < Code03_War2.dfn[pivot]):
                i = jcast('int', (i + 1))
            while (Code03_War2.dfn[nums[j]] > Code03_War2.dfn[pivot]):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', nums[i])
                nums[i] = jcast('int', nums[j])
                nums[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code03_War2.sortByDfn(nums, l, j)
        Code03_War2.sortByDfn(nums, i, r)

    @staticmethod
    def dfs(u, fa, w):
        u = jcast('int', u)
        fa = jcast('int', fa)
        w = jcast('int', w)
        Code03_War2.dep[u] = jcast('int', jcast('int', jadd(Code03_War2.dep[fa], 1)))
        jset(Code03_War2.dfn, u, ((_java_obj_7 := Code03_War2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
        jset(Code03_War2.stjump[u], 0, fa)
        jset(Code03_War2.mindist[u], 0, w)
        p = jcast('int', 1)
        while (p < Code03_War2.MAXP):
            jset(Code03_War2.stjump[u], p, Code03_War2.stjump[Code03_War2.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            jset(Code03_War2.mindist[u], p, jstatic('Math', 'min', Code03_War2.mindist[u][jcast('int', (p - 1))], Code03_War2.mindist[Code03_War2.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))]))
            p = jcast('int', (p + 1))
        e = jcast('int', Code03_War2.headg[u])
        while (e > 0):
            if (Code03_War2.tog[e] != fa):
                Code03_War2.dfs(Code03_War2.tog[e], u, Code03_War2.weightg[e])
            e = jcast('int', Code03_War2.nextg[e])

    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code03_War2.dep[a] < Code03_War2.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code03_War2.MAXP - 1)))
        while (p >= 0):
            if (Code03_War2.dep[Code03_War2.stjump[a][p]] >= Code03_War2.dep[b]):
                a = jcast('int', Code03_War2.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code03_War2.MAXP - 1)))
        while (p >= 0):
            if (Code03_War2.stjump[a][p] != Code03_War2.stjump[b][p]):
                a = jcast('int', Code03_War2.stjump[a][p])
                b = jcast('int', Code03_War2.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code03_War2.stjump[a][0])

    # 已知u一定是v的祖先节点，返回u到v路径上的最小边权
    @staticmethod
    def getDist(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        dist = jcast('int', 100000001)
        p = jcast('int', jcast('int', (Code03_War2.MAXP - 1)))
        while (p >= 0):
            if (Code03_War2.dep[Code03_War2.stjump[v][p]] >= Code03_War2.dep[u]):
                dist = jcast('int', jstatic('Math', 'min', dist, Code03_War2.mindist[v][p]))
                v = jcast('int', Code03_War2.stjump[v][p])
            p = jcast('int', (p - 1))
        return jcast('int', dist)

    # 二次排序 + LCA连边的方式建立虚树
    @staticmethod
    def buildVirtualTree1():
        Code03_War2.sortByDfn(Code03_War2.arr, 1, Code03_War2.k)
        # 因为题目是让所有关键点不能和1号点连通
        # 所以一定要让1号点加入
        len = jcast('int', 0)
        jset(Code03_War2.tmp, (len := jcast('int', (len + (1)))), 1)
        i = jcast('int', 1)
        while (i < Code03_War2.k):
            jset(Code03_War2.tmp, (len := jcast('int', (len + (1)))), Code03_War2.arr[i])
            jset(Code03_War2.tmp, (len := jcast('int', (len + (1)))), Code03_War2.getLca(Code03_War2.arr[i], Code03_War2.arr[jcast('int', jadd(i, 1))]))
            i = jcast('int', (i + 1))
        jset(Code03_War2.tmp, (len := jcast('int', (len + (1)))), Code03_War2.arr[Code03_War2.k])
        Code03_War2.sortByDfn(Code03_War2.tmp, 1, len)
        unique = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= len):
            if (Code03_War2.tmp[unique] != Code03_War2.tmp[i]):
                jset(Code03_War2.tmp, (unique := jcast('int', (unique + (1)))), Code03_War2.tmp[i])
            i = jcast('int', (i + 1))
        Code03_War2.cntv = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= unique):
            jset(Code03_War2.headv, Code03_War2.tmp[i], 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < unique):
            lca = jcast('int', Code03_War2.getLca(Code03_War2.tmp[i], Code03_War2.tmp[jcast('int', jadd(i, 1))]))
            Code03_War2.addEdgeV(lca, Code03_War2.tmp[jcast('int', jadd(i, 1))], Code03_War2.getDist(lca, Code03_War2.tmp[jcast('int', jadd(i, 1))]))
            i = jcast('int', (i + 1))
        return jcast('int', Code03_War2.tmp[1])

    # 单调栈的方式建立虚树
    @staticmethod
    def buildVirtualTree2():
        Code03_War2.sortByDfn(Code03_War2.arr, 1, Code03_War2.k)
        # 因为题目是让所有关键点不能和1号点连通
        # 所以一定要让1号点加入
        Code03_War2.cntv = jcast('int', 0)
        Code03_War2.headv[1] = jcast('int', 0)
        top = jcast('int', 0)
        jset(Code03_War2.stk, (top := jcast('int', (top + (1)))), 1)
        i = jcast('int', 1)
        while (i <= Code03_War2.k):
            x = jcast('int', Code03_War2.arr[i])
            y = jcast('int', Code03_War2.stk[top])
            lca = jcast('int', Code03_War2.getLca(x, y))
            while ((top > 1) and (Code03_War2.dfn[Code03_War2.stk[jcast('int', (top - 1))]] >= Code03_War2.dfn[lca])):
                Code03_War2.addEdgeV(Code03_War2.stk[jcast('int', (top - 1))], Code03_War2.stk[top], Code03_War2.getDist(Code03_War2.stk[jcast('int', (top - 1))], Code03_War2.stk[top]))
                top = jcast('int', (top - 1))
            if (lca != Code03_War2.stk[top]):
                Code03_War2.headv[lca] = jcast('int', 0)
                Code03_War2.addEdgeV(lca, Code03_War2.stk[top], Code03_War2.getDist(lca, Code03_War2.stk[top]))
                Code03_War2.stk[top] = jcast('int', lca)
            Code03_War2.headv[x] = jcast('int', 0)
            jset(Code03_War2.stk, (top := jcast('int', (top + (1)))), x)
            i = jcast('int', (i + 1))
        while (top > 1):
            Code03_War2.addEdgeV(Code03_War2.stk[jcast('int', (top - 1))], Code03_War2.stk[top], Code03_War2.getDist(Code03_War2.stk[jcast('int', (top - 1))], Code03_War2.stk[top]))
            top = jcast('int', (top - 1))
        return jcast('int', Code03_War2.stk[1])

    @staticmethod
    def dp(u):
        u = jcast('int', u)
        e = jcast('int', Code03_War2.headv[u])
        while (e > 0):
            Code03_War2.dp(Code03_War2.tov[e])
            e = jcast('int', Code03_War2.nextv[e])
        Code03_War2.cost[u] = jcast('long', 0)
        e = jcast('int', Code03_War2.headv[u])
        v = 0
        w = 0
        while (e > 0):
            v = jcast('int', Code03_War2.tov[e])
            w = jcast('int', Code03_War2.weightv[e])
            if Code03_War2.isKey[v]:
                Code03_War2.cost[u] = jcast('long', jcast('long', jadd(Code03_War2.cost[u], w)))
            else:
                ((_java_obj_10 := Code03_War2.cost), (_java_key_11 := u), jset(_java_obj_10, _java_key_11, jcast('long', jadd(jget(_java_obj_10, _java_key_11), jstatic('Math', 'min', Code03_War2.cost[v], w)))))[2]
            e = jcast('int', Code03_War2.nextv[e])

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code03_War2.k):
            jset(Code03_War2.isKey, Code03_War2.arr[i], True)
            i = jcast('int', (i + 1))
        tree = jcast('int', Code03_War2.buildVirtualTree1())
        # int tree = buildVirtualTree2();
        Code03_War2.dp(tree)
        i = jcast('int', 1)
        while (i <= Code03_War2.k):
            jset(Code03_War2.isKey, Code03_War2.arr[i], False)
            i = jcast('int', (i + 1))
        return jcast('long', Code03_War2.cost[tree])

    @staticmethod
    def main(args):
        in_ = Code03_War2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_War2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code03_War2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code03_War2.addEdgeG(u, v, w)
            Code03_War2.addEdgeG(v, u, w)
            i = jcast('int', (i + 1))
        Code03_War2.dfs(1, 0, 0)
        Code03_War2.q = jcast('int', jcall(in_, 'nextInt'))
        t = jcast('int', 1)
        while (t <= Code03_War2.q):
            Code03_War2.k = jcast('int', jcall(in_, 'nextInt'))
            i = jcast('int', 1)
            while (i <= Code03_War2.k):
                jset(Code03_War2.arr, i, jcall(in_, 'nextInt'))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code03_War2.compute())
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
            return jcast('int', self.buffer[((_java_obj_12 := self), (_java_key_13 := 'ptr'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))), _java_old_14)[4]])

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
            raise TypeError("No matching overload for Code03_War2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_War2.MAXN = jcast('int', 500001)
Code03_War2.MAXP = jcast('int', 20)
Code03_War2.n = jcast('int', 0)
Code03_War2.q = jcast('int', 0)
Code03_War2.k = jcast('int', 0)
Code03_War2.headg = jarray('int', [Code03_War2.MAXN])
Code03_War2.nextg = jarray('int', [jcast('int', (Code03_War2.MAXN << (1 & 31)))])
Code03_War2.tog = jarray('int', [jcast('int', (Code03_War2.MAXN << (1 & 31)))])
Code03_War2.weightg = jarray('int', [jcast('int', (Code03_War2.MAXN << (1 & 31)))])
Code03_War2.cntg = jcast('int', 0)
Code03_War2.headv = jarray('int', [Code03_War2.MAXN])
Code03_War2.nextv = jarray('int', [Code03_War2.MAXN])
Code03_War2.tov = jarray('int', [Code03_War2.MAXN])
Code03_War2.weightv = jarray('int', [Code03_War2.MAXN])
Code03_War2.cntv = jcast('int', 0)
Code03_War2.dep = jarray('int', [Code03_War2.MAXN])
Code03_War2.dfn = jarray('int', [Code03_War2.MAXN])
Code03_War2.stjump = jarray('int', [Code03_War2.MAXN, Code03_War2.MAXP])
Code03_War2.mindist = jarray('int', [Code03_War2.MAXN, Code03_War2.MAXP])
Code03_War2.cntd = jcast('int', 0)
Code03_War2.arr = jarray('int', [Code03_War2.MAXN])
Code03_War2.isKey = jarray('boolean', [Code03_War2.MAXN])
Code03_War2.tmp = jarray('int', [jcast('int', (Code03_War2.MAXN << (1 & 31)))])
Code03_War2.stk = jarray('int', [Code03_War2.MAXN])
Code03_War2.cost = jarray('long', [Code03_War2.MAXN])

if __name__ == '__main__':
    Code03_War2.main([])
