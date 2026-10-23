# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 逛森林，Python版
# 一共n个点，给定出发点s，初始时没有边，一共m条操作，操作类型有两种
# 操作 1 a b c d w : 如果点a和点b不连通，或者点c和点d不连通，忽略该操作
# 点a到点b路径上的任何一点，可以花费w的代价，传送到点c到点d路径上的任何一点
# 该操作是单向传送，不代表加边，判断连通性只考虑2类型的操作加入的边
# 操作 2 u v w : 点u和点v如果已经连通，忽略该操作，否则增加一条边权为w的无向边
# 完成m条操作后，打印从s点出发，到每个节点的最小花费，到达不了的节点打印-1
# 1 <= n <= 5 * 10^4    1 <= m <= 10^6    1 <= w <= 100
# 测试链接 : https://www.luogu.com.cn/problem/P5344
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 对应实现可参考 Code08_Forest2.py
# 两个版本保留相同的算法逻辑
class Code08_Forest1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'MAXP': 'MAXP', 'INF': 'INF', 'n': 'n', 'm': 'm', 's': 's', 'u1': 'u1', 'v1': 'v1', 'u2': 'u2', 'v2': 'v2', 'weight': 'weight', 'cntq': 'cntq', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'weight2': 'weight2', 'cnt2': 'cnt2', 'father': 'father', 'dep': 'dep', 'stjump': 'stjump', 'stout': 'stout', 'stin': 'stin', 'cntt': 'cntt', 'dist': 'dist', 'vis': 'vis', 'heap': 'heap'}
    MAXN = 0
    MAXM = 0
    MAXT = 0
    MAXE = 0
    MAXP = 0
    INF = 0
    n = 0
    m = 0
    s = 0
    # 操作1记录一下，只记录应该发生的操作1
    u1 = None
    v1 = None
    u2 = None
    v2 = None
    weight = None
    cntq = 0
    # 操作2建立的树
    head1 = None
    next1 = None
    to1 = None
    cnt1 = 0
    # 操作1 + 操作2 建立的图
    head2 = None
    next2 = None
    to2 = None
    weight2 = None
    cnt2 = 0
    # 并查集
    father = None
    # 树上倍增
    dep = None
    stjump = None
    stout = None
    stin = None
    cntt = 0
    # dijkstra算法
    dist = None
    vis = None
    heap = None
    @staticmethod
    def addEdge1(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code08_Forest1.next1, ((_java_obj_1 := Code08_Forest1), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code08_Forest1.head1[u])
        Code08_Forest1.to1[Code08_Forest1.cnt1] = jcast('int', v)
        Code08_Forest1.head1[u] = jcast('int', Code08_Forest1.cnt1)

    @staticmethod
    def addEdge2(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code08_Forest1.next2, ((_java_obj_4 := Code08_Forest1), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code08_Forest1.head2[u])
        Code08_Forest1.to2[Code08_Forest1.cnt2] = jcast('int', v)
        Code08_Forest1.weight2[Code08_Forest1.cnt2] = jcast('int', w)
        Code08_Forest1.head2[u] = jcast('int', Code08_Forest1.cnt2)

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code08_Forest1.father[i]):
            jset(Code08_Forest1.father, i, Code08_Forest1.find(Code08_Forest1.father[i]))
        return jcast('int', Code08_Forest1.father[i])

    @staticmethod
    def build(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code08_Forest1.dep[u] = jcast('int', jcast('int', jadd(Code08_Forest1.dep[fa], 1)))
        jset(Code08_Forest1.stjump[u], 0, fa)
        jset(Code08_Forest1.stout[u], 0, ((_java_obj_7 := Code08_Forest1), (_java_key_8 := 'cntt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
        Code08_Forest1.addEdge2(u, Code08_Forest1.cntt, 0)
        Code08_Forest1.addEdge2(fa, Code08_Forest1.cntt, 0)
        jset(Code08_Forest1.stin[u], 0, ((_java_obj_10 := Code08_Forest1), (_java_key_11 := 'cntt'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
        Code08_Forest1.addEdge2(Code08_Forest1.cntt, u, 0)
        Code08_Forest1.addEdge2(Code08_Forest1.cntt, fa, 0)
        p = jcast('int', 1)
        while (p < Code08_Forest1.MAXP):
            jset(Code08_Forest1.stjump[u], p, Code08_Forest1.stjump[Code08_Forest1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            jset(Code08_Forest1.stout[u], p, ((_java_obj_13 := Code08_Forest1), (_java_key_14 := 'cntt'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
            Code08_Forest1.addEdge2(Code08_Forest1.stout[u][jcast('int', (p - 1))], Code08_Forest1.cntt, 0)
            Code08_Forest1.addEdge2(Code08_Forest1.stout[Code08_Forest1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))], Code08_Forest1.cntt, 0)
            jset(Code08_Forest1.stin[u], p, ((_java_obj_16 := Code08_Forest1), (_java_key_17 := 'cntt'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3])
            Code08_Forest1.addEdge2(Code08_Forest1.cntt, Code08_Forest1.stin[u][jcast('int', (p - 1))], 0)
            Code08_Forest1.addEdge2(Code08_Forest1.cntt, Code08_Forest1.stin[Code08_Forest1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))], 0)
            p = jcast('int', (p + 1))
        e = jcast('int', Code08_Forest1.head1[u])
        while (e > 0):
            v = jcast('int', Code08_Forest1.to1[e])
            if (v != fa):
                Code08_Forest1.build(v, u)
            e = jcast('int', Code08_Forest1.next1[e])

    @staticmethod
    def pathOut(x, y, vnode):
        x = jcast('int', x)
        y = jcast('int', y)
        vnode = jcast('int', vnode)
        if (Code08_Forest1.dep[x] < Code08_Forest1.dep[y]):
            tmp = jcast('int', x)
            x = jcast('int', y)
            y = jcast('int', tmp)
        Code08_Forest1.addEdge2(y, vnode, 0)
        p = jcast('int', jcast('int', (Code08_Forest1.MAXP - 1)))
        while (p >= 0):
            if (Code08_Forest1.dep[Code08_Forest1.stjump[x][p]] >= Code08_Forest1.dep[y]):
                Code08_Forest1.addEdge2(Code08_Forest1.stout[x][p], vnode, 0)
                x = jcast('int', Code08_Forest1.stjump[x][p])
            p = jcast('int', (p - 1))
        if (x == y):
            return
        p = jcast('int', jcast('int', (Code08_Forest1.MAXP - 1)))
        while (p >= 0):
            if (Code08_Forest1.stjump[x][p] != Code08_Forest1.stjump[y][p]):
                Code08_Forest1.addEdge2(Code08_Forest1.stout[x][p], vnode, 0)
                Code08_Forest1.addEdge2(Code08_Forest1.stout[y][p], vnode, 0)
                x = jcast('int', Code08_Forest1.stjump[x][p])
                y = jcast('int', Code08_Forest1.stjump[y][p])
            p = jcast('int', (p - 1))
        Code08_Forest1.addEdge2(Code08_Forest1.stout[x][0], vnode, 0)

    @staticmethod
    def pathIn(x, y, vnode):
        x = jcast('int', x)
        y = jcast('int', y)
        vnode = jcast('int', vnode)
        if (Code08_Forest1.dep[x] < Code08_Forest1.dep[y]):
            tmp = jcast('int', x)
            x = jcast('int', y)
            y = jcast('int', tmp)
        Code08_Forest1.addEdge2(vnode, y, 0)
        p = jcast('int', jcast('int', (Code08_Forest1.MAXP - 1)))
        while (p >= 0):
            if (Code08_Forest1.dep[Code08_Forest1.stjump[x][p]] >= Code08_Forest1.dep[y]):
                Code08_Forest1.addEdge2(vnode, Code08_Forest1.stin[x][p], 0)
                x = jcast('int', Code08_Forest1.stjump[x][p])
            p = jcast('int', (p - 1))
        if (x == y):
            return
        p = jcast('int', jcast('int', (Code08_Forest1.MAXP - 1)))
        while (p >= 0):
            if (Code08_Forest1.stjump[x][p] != Code08_Forest1.stjump[y][p]):
                Code08_Forest1.addEdge2(vnode, Code08_Forest1.stin[x][p], 0)
                Code08_Forest1.addEdge2(vnode, Code08_Forest1.stin[y][p], 0)
                x = jcast('int', Code08_Forest1.stjump[x][p])
                y = jcast('int', Code08_Forest1.stjump[y][p])
            p = jcast('int', (p - 1))
        Code08_Forest1.addEdge2(vnode, Code08_Forest1.stin[x][0], 0)

    @staticmethod
    def pathToPath(a, b, c, d, w):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        w = jcast('int', w)
        x = jcast('int', ((_java_obj_19 := Code08_Forest1), (_java_key_20 := 'cntt'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3])
        y = jcast('int', ((_java_obj_22 := Code08_Forest1), (_java_key_23 := 'cntt'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))))[3])
        Code08_Forest1.pathOut(a, b, x)
        Code08_Forest1.pathIn(c, d, y)
        Code08_Forest1.addEdge2(x, y, w)

    @staticmethod
    def dijkstra():
        i = jcast('int', 1)
        while (i <= Code08_Forest1.cntt):
            Code08_Forest1.dist[i] = jcast('int', Code08_Forest1.INF)
            i = jcast('int', (i + 1))
        Code08_Forest1.dist[Code08_Forest1.s] = jcast('int', 0)
        jcall(Code08_Forest1.heap, 'add', jarray('int', [None], [Code08_Forest1.s, 0]))
        while (not jcall(Code08_Forest1.heap, 'isEmpty')):
            cur = jcall(Code08_Forest1.heap, 'poll')
            u = jcast('int', cur[0])
            d = jcast('int', cur[1])
            if (not Code08_Forest1.vis[u]):
                Code08_Forest1.vis[u] = jcast('boolean', True)
                e = jcast('int', Code08_Forest1.head2[u])
                while (e > 0):
                    v = jcast('int', Code08_Forest1.to2[e])
                    w = jcast('int', Code08_Forest1.weight2[e])
                    if ((not Code08_Forest1.vis[v]) and (Code08_Forest1.dist[v] > jcast('int', jadd(d, w)))):
                        Code08_Forest1.dist[v] = jcast('int', jcast('int', jadd(d, w)))
                        jcall(Code08_Forest1.heap, 'add', jarray('int', [None], [v, Code08_Forest1.dist[v]]))
                    e = jcast('int', Code08_Forest1.next2[e])

    @staticmethod
    def main(args):
        in_ = Code08_Forest1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code08_Forest1.n = jcast('int', jcall(in_, 'nextInt'))
        Code08_Forest1.m = jcast('int', jcall(in_, 'nextInt'))
        Code08_Forest1.s = jcast('int', jcall(in_, 'nextInt'))
        Code08_Forest1.cntt = jcast('int', Code08_Forest1.n)
        i = jcast('int', 1)
        while (i <= Code08_Forest1.n):
            Code08_Forest1.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        a = 0
        b = 0
        c = 0
        d = 0
        w = 0
        u = 0
        v = 0
        while (i <= Code08_Forest1.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                a = jcast('int', jcall(in_, 'nextInt'))
                b = jcast('int', jcall(in_, 'nextInt'))
                c = jcast('int', jcall(in_, 'nextInt'))
                d = jcast('int', jcall(in_, 'nextInt'))
                w = jcast('int', jcall(in_, 'nextInt'))
                if ((Code08_Forest1.find(a) == Code08_Forest1.find(b)) and (Code08_Forest1.find(c) == Code08_Forest1.find(d))):
                    jset(Code08_Forest1.u1, ((_java_obj_25 := Code08_Forest1), (_java_key_26 := 'cntq'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3], a)
                    Code08_Forest1.v1[Code08_Forest1.cntq] = jcast('int', b)
                    Code08_Forest1.u2[Code08_Forest1.cntq] = jcast('int', c)
                    Code08_Forest1.v2[Code08_Forest1.cntq] = jcast('int', d)
                    Code08_Forest1.weight[Code08_Forest1.cntq] = jcast('int', w)
            else:
                u = jcast('int', jcall(in_, 'nextInt'))
                v = jcast('int', jcall(in_, 'nextInt'))
                w = jcast('int', jcall(in_, 'nextInt'))
                ufa = jcast('int', Code08_Forest1.find(u))
                vfa = jcast('int', Code08_Forest1.find(v))
                if (ufa != vfa):
                    Code08_Forest1.addEdge1(u, v)
                    Code08_Forest1.addEdge1(v, u)
                    Code08_Forest1.addEdge2(u, v, w)
                    Code08_Forest1.addEdge2(v, u, w)
                    Code08_Forest1.father[ufa] = jcast('int', vfa)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code08_Forest1.n):
            if (Code08_Forest1.dep[i] == 0):
                Code08_Forest1.build(i, i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code08_Forest1.cntq):
            Code08_Forest1.pathToPath(Code08_Forest1.u1[i], Code08_Forest1.v1[i], Code08_Forest1.u2[i], Code08_Forest1.v2[i], Code08_Forest1.weight[i])
            i = jcast('int', (i + 1))
        Code08_Forest1.dijkstra()
        i = jcast('int', 1)
        while (i <= Code08_Forest1.n):
            jcall(out, 'print', (jcast('int', (-1)) if (Code08_Forest1.dist[i] == Code08_Forest1.INF) else Code08_Forest1.dist[i]))
            jcall(out, 'print', ' ')
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
            return jcast('int', self.buffer[((_java_obj_28 := self), (_java_key_29 := 'ptr'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))), _java_old_30)[4]])

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
            raise TypeError("No matching overload for Code08_Forest1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code08_Forest1.MAXN = jcast('int', 50001)
Code08_Forest1.MAXM = jcast('int', 1000001)
Code08_Forest1.MAXT = jcast('int', 4000001)
Code08_Forest1.MAXE = jcast('int', 30000001)
Code08_Forest1.MAXP = jcast('int', 17)
Code08_Forest1.INF = jcast('int', jcast('int', (1 << (30 & 31))))
Code08_Forest1.n = jcast('int', 0)
Code08_Forest1.m = jcast('int', 0)
Code08_Forest1.s = jcast('int', 0)
Code08_Forest1.u1 = jarray('int', [Code08_Forest1.MAXM])
Code08_Forest1.v1 = jarray('int', [Code08_Forest1.MAXM])
Code08_Forest1.u2 = jarray('int', [Code08_Forest1.MAXM])
Code08_Forest1.v2 = jarray('int', [Code08_Forest1.MAXM])
Code08_Forest1.weight = jarray('int', [Code08_Forest1.MAXM])
Code08_Forest1.cntq = jcast('int', 0)
Code08_Forest1.head1 = jarray('int', [Code08_Forest1.MAXN])
Code08_Forest1.next1 = jarray('int', [jcast('int', (Code08_Forest1.MAXN << (1 & 31)))])
Code08_Forest1.to1 = jarray('int', [jcast('int', (Code08_Forest1.MAXN << (1 & 31)))])
Code08_Forest1.cnt1 = jcast('int', 0)
Code08_Forest1.head2 = jarray('int', [Code08_Forest1.MAXT])
Code08_Forest1.next2 = jarray('int', [Code08_Forest1.MAXE])
Code08_Forest1.to2 = jarray('int', [Code08_Forest1.MAXE])
Code08_Forest1.weight2 = jarray('int', [Code08_Forest1.MAXE])
Code08_Forest1.cnt2 = jcast('int', 0)
Code08_Forest1.father = jarray('int', [Code08_Forest1.MAXN])
Code08_Forest1.dep = jarray('int', [Code08_Forest1.MAXN])
Code08_Forest1.stjump = jarray('int', [Code08_Forest1.MAXN, Code08_Forest1.MAXP])
Code08_Forest1.stout = jarray('int', [Code08_Forest1.MAXN, Code08_Forest1.MAXP])
Code08_Forest1.stin = jarray('int', [Code08_Forest1.MAXN, Code08_Forest1.MAXP])
Code08_Forest1.cntt = jcast('int', 0)
Code08_Forest1.dist = jarray('int', [Code08_Forest1.MAXT])
Code08_Forest1.vis = jarray('boolean', [Code08_Forest1.MAXT])
Code08_Forest1.heap = jnew('PriorityQueue', (lambda a, b: (a[1] - b[1])))

if __name__ == '__main__':
    Code08_Forest1.main([])
