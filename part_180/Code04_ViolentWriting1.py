# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 暴力写挂，Python版
# 两棵树t1、t2都有n个节点，都以1号节点作为树头
# 各自给定n-1条边，以及每条边的边权，边权可能为负数
# 在t1中，点x到树头的距离记为dis1(x)，在t2中，该距离记为dis2(x)
# 点x和点y在t1中的LCA记为lca1(x, y)，在t2中的LCA记为lca2(x, y)
# 点对(x, y)的指标 = dis1(x) + dis1(y) - dis1(lca1(x, y)) - dis2(lca2(x, y))
# 点对(x, y)，要求x <= y，打印这个指标的最大值
# 1 <= n <= 366666
# 测试链接 : https://www.luogu.com.cn/problem/P4565
# 测试链接 : https://loj.ac/p/2553
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
# 对应实现可参考 Code04_ViolentWriting2.py
# 两个版本保留相同的算法逻辑
class Code04_ViolentWriting1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXT': 'MAXT', 'INF': 'INF', 'n': 'n', 'cntn': 'cntn', 'head0': 'head0', 'next0': 'next0', 'to0': 'to0', 'weight0': 'weight0', 'cnt0': 'cnt0', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'weight1': 'weight1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'weight2': 'weight2', 'cnt2': 'cnt2', 'dis1': 'dis1', 'vis': 'vis', 'siz': 'siz', 'up': 'up', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'lmax': 'lmax', 'rmax': 'rmax', 'cntt': 'cntt', 'ans': 'ans'}
    MAXN = 0
    MAXM = 0
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
    dis1 = None
    vis = None
    siz = None
    up = None
    root = None
    ls = None
    rs = None
    lmax = None
    rmax = None
    cntt = 0
    ans = 0
    @staticmethod
    def addEdge0(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code04_ViolentWriting1.next0, ((_java_obj_1 := Code04_ViolentWriting1), (_java_key_2 := 'cnt0'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_ViolentWriting1.head0[u])
        Code04_ViolentWriting1.to0[Code04_ViolentWriting1.cnt0] = jcast('int', v)
        Code04_ViolentWriting1.weight0[Code04_ViolentWriting1.cnt0] = jcast('int', w)
        Code04_ViolentWriting1.head0[u] = jcast('int', Code04_ViolentWriting1.cnt0)

    @staticmethod
    def addEdge1(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code04_ViolentWriting1.next1, ((_java_obj_4 := Code04_ViolentWriting1), (_java_key_5 := 'cnt1'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code04_ViolentWriting1.head1[u])
        Code04_ViolentWriting1.to1[Code04_ViolentWriting1.cnt1] = jcast('int', v)
        Code04_ViolentWriting1.weight1[Code04_ViolentWriting1.cnt1] = jcast('int', w)
        Code04_ViolentWriting1.head1[u] = jcast('int', Code04_ViolentWriting1.cnt1)

    @staticmethod
    def addEdge2(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code04_ViolentWriting1.next2, ((_java_obj_7 := Code04_ViolentWriting1), (_java_key_8 := 'cnt2'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], Code04_ViolentWriting1.head2[u])
        Code04_ViolentWriting1.to2[Code04_ViolentWriting1.cnt2] = jcast('int', v)
        Code04_ViolentWriting1.weight2[Code04_ViolentWriting1.cnt2] = jcast('int', w)
        Code04_ViolentWriting1.head2[u] = jcast('int', Code04_ViolentWriting1.cnt2)

    @staticmethod
    def getDist(u, fa, dist1):
        u = jcast('int', u)
        fa = jcast('int', fa)
        dist1 = jcast('long', dist1)
        Code04_ViolentWriting1.dis1[u] = jcast('long', dist1)
        e = jcast('int', Code04_ViolentWriting1.head0[u])
        while (e > 0):
            v = jcast('int', Code04_ViolentWriting1.to0[e])
            if (v != fa):
                Code04_ViolentWriting1.getDist(v, u, jcast('long', jadd(dist1, Code04_ViolentWriting1.weight0[e])))
            e = jcast('int', Code04_ViolentWriting1.next0[e])

    @staticmethod
    def rebuild(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        last = jcast('int', 0)
        e = jcast('int', Code04_ViolentWriting1.head0[u])
        while (e > 0):
            v = jcast('int', Code04_ViolentWriting1.to0[e])
            w = jcast('int', Code04_ViolentWriting1.weight0[e])
            if (v != fa):
                if (last == 0):
                    last = jcast('int', u)
                    Code04_ViolentWriting1.addEdge1(u, v, w)
                    Code04_ViolentWriting1.addEdge1(v, u, w)
                else:
                    add = jcast('int', ((_java_obj_10 := Code04_ViolentWriting1), (_java_key_11 := 'cntn'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
                    Code04_ViolentWriting1.addEdge1(last, add, 0)
                    Code04_ViolentWriting1.addEdge1(add, last, 0)
                    Code04_ViolentWriting1.addEdge1(add, v, w)
                    Code04_ViolentWriting1.addEdge1(v, add, w)
                    last = jcast('int', add)
                Code04_ViolentWriting1.rebuild(v, u)
            e = jcast('int', Code04_ViolentWriting1.next0[e])

    @staticmethod
    def getSize(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code04_ViolentWriting1.siz[u] = jcast('int', 1)
        e = jcast('int', Code04_ViolentWriting1.head1[u])
        while (e > 0):
            v = jcast('int', Code04_ViolentWriting1.to1[e])
            if ((v != fa) and (not Code04_ViolentWriting1.vis[jcast('int', (e >> (1 & 31)))])):
                Code04_ViolentWriting1.getSize(v, u)
                Code04_ViolentWriting1.siz[u] = jcast('int', jcast('int', jadd(Code04_ViolentWriting1.siz[u], Code04_ViolentWriting1.siz[v])))
            e = jcast('int', Code04_ViolentWriting1.next1[e])

    @staticmethod
    def getCentroidEdge(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code04_ViolentWriting1.getSize(u, fa)
        total = jcast('int', Code04_ViolentWriting1.siz[u])
        half = jcast('int', jcast('int', (total >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code04_ViolentWriting1.head1[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code04_ViolentWriting1.to1[e])
                        if (((v != fa) and (not Code04_ViolentWriting1.vis[jcast('int', (e >> (1 & 31)))])) and (Code04_ViolentWriting1.siz[v] > half)):
                            fa = jcast('int', u)
                            u = jcast('int', v)
                            find = jcast('boolean', False)
                            raise JBreak(None)
                    except JContinue as _java_control_14:
                        if _java_control_14.label not in (None,):
                            raise
                    except JBreak as _java_control_14:
                        if _java_control_14.label not in (None,):
                            raise
                        break
                    e = jcast('int', Code04_ViolentWriting1.next1[e])
            except JContinue as _java_control_13:
                if _java_control_13.label not in (None,):
                    raise
            except JBreak as _java_control_13:
                if _java_control_13.label not in (None,):
                    raise
                break
        best = jcast('int', 0)
        edge = jcast('int', 0)
        e = jcast('int', Code04_ViolentWriting1.head1[u])
        while (e > 0):
            if (not Code04_ViolentWriting1.vis[jcast('int', (e >> (1 & 31)))]):
                v = jcast('int', Code04_ViolentWriting1.to1[e])
                sub = jcast('int', (jcast('int', (total - Code04_ViolentWriting1.siz[u])) if (v == fa) else Code04_ViolentWriting1.siz[v]))
                if (sub > best):
                    best = jcast('int', sub)
                    edge = jcast('int', e)
            e = jcast('int', Code04_ViolentWriting1.next1[e])
        return jcast('int', edge)

    @staticmethod
    def dfs(u, fa, path, op):
        u = jcast('int', u)
        fa = jcast('int', fa)
        path = jcast('long', path)
        op = jcast('int', op)
        if (u <= Code04_ViolentWriting1.n):
            if (Code04_ViolentWriting1.up[u] == 0):
                jset(Code04_ViolentWriting1.up, u, ((_java_obj_15 := Code04_ViolentWriting1), (_java_key_16 := 'cntt'), (_java_old_17 := jget(_java_obj_15, _java_key_16)), jset(_java_obj_15, _java_key_16, jcast('int', (_java_old_17 + (1)))))[3])
                Code04_ViolentWriting1.root[u] = jcast('int', Code04_ViolentWriting1.cntt)
            cur = jcast('int', Code04_ViolentWriting1.up[u])
            nxt = jcast('int', ((_java_obj_18 := Code04_ViolentWriting1), (_java_key_19 := 'cntt'), (_java_old_20 := jget(_java_obj_18, _java_key_19)), jset(_java_obj_18, _java_key_19, jcast('int', (_java_old_20 + (1)))))[3])
            if (op == 0):
                Code04_ViolentWriting1.ls[cur] = jcast('int', nxt)
                Code04_ViolentWriting1.lmax[cur] = jcast('long', jcast('long', jadd(Code04_ViolentWriting1.dis1[u], path)))
            else:
                Code04_ViolentWriting1.rs[cur] = jcast('int', nxt)
                Code04_ViolentWriting1.rmax[cur] = jcast('long', jcast('long', jadd(Code04_ViolentWriting1.dis1[u], path)))
            Code04_ViolentWriting1.up[u] = jcast('int', nxt)
        e = jcast('int', Code04_ViolentWriting1.head1[u])
        while (e > 0):
            v = jcast('int', Code04_ViolentWriting1.to1[e])
            if ((v != fa) and (not Code04_ViolentWriting1.vis[jcast('int', (e >> (1 & 31)))])):
                Code04_ViolentWriting1.dfs(v, u, jcast('long', jadd(path, Code04_ViolentWriting1.weight1[e])), op)
            e = jcast('int', Code04_ViolentWriting1.next1[e])

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        edge = jcast('int', Code04_ViolentWriting1.getCentroidEdge(u, 0))
        if (edge > 0):
            Code04_ViolentWriting1.vis[jcast('int', (edge >> (1 & 31)))] = jcast('boolean', True)
            v1 = jcast('int', Code04_ViolentWriting1.to1[edge])
            v2 = jcast('int', Code04_ViolentWriting1.to1[jcast('int', (edge ^ 1))])
            Code04_ViolentWriting1.dfs(v1, 0, 0, 0)
            Code04_ViolentWriting1.dfs(v2, 0, Code04_ViolentWriting1.weight1[edge], 1)
            Code04_ViolentWriting1.solve(v1)
            Code04_ViolentWriting1.solve(v2)

    @staticmethod
    def mergeTree(x, y, add):
        x = jcast('int', x)
        y = jcast('int', y)
        add = jcast('long', add)
        if ((x == 0) or (y == 0)):
            return jcast('int', jcast('int', jadd(x, y)))
        Code04_ViolentWriting1.ans = jcast('long', jstatic('Math', 'max', Code04_ViolentWriting1.ans, jcast('long', jadd(jstatic('Math', 'max', jcast('long', jadd(Code04_ViolentWriting1.lmax[x], Code04_ViolentWriting1.rmax[y])), jcast('long', jadd(Code04_ViolentWriting1.lmax[y], Code04_ViolentWriting1.rmax[x]))), add))))
        jset(Code04_ViolentWriting1.lmax, x, jstatic('Math', 'max', Code04_ViolentWriting1.lmax[x], Code04_ViolentWriting1.lmax[y]))
        jset(Code04_ViolentWriting1.rmax, x, jstatic('Math', 'max', Code04_ViolentWriting1.rmax[x], Code04_ViolentWriting1.rmax[y]))
        jset(Code04_ViolentWriting1.ls, x, Code04_ViolentWriting1.mergeTree(Code04_ViolentWriting1.ls[x], Code04_ViolentWriting1.ls[y], add))
        jset(Code04_ViolentWriting1.rs, x, Code04_ViolentWriting1.mergeTree(Code04_ViolentWriting1.rs[x], Code04_ViolentWriting1.rs[y], add))
        return jcast('int', x)

    @staticmethod
    def compute(u, fa, dist2):
        u = jcast('int', u)
        fa = jcast('int', fa)
        dist2 = jcast('long', dist2)
        Code04_ViolentWriting1.ans = jcast('long', jstatic('Math', 'max', Code04_ViolentWriting1.ans, jcast('long', (jcast('long', (Code04_ViolentWriting1.dis1[u] - dist2)) * 2))))
        e = jcast('int', Code04_ViolentWriting1.head2[u])
        while (e > 0):
            v = jcast('int', Code04_ViolentWriting1.to2[e])
            if (v != fa):
                Code04_ViolentWriting1.compute(v, u, jcast('long', jadd(dist2, Code04_ViolentWriting1.weight2[e])))
                jset(Code04_ViolentWriting1.root, u, Code04_ViolentWriting1.mergeTree(Code04_ViolentWriting1.root[u], Code04_ViolentWriting1.root[v], jcast('long', (jcast('long', (-dist2)) * 2))))
            e = jcast('int', Code04_ViolentWriting1.next2[e])

    @staticmethod
    def main(args):
        in_ = Code04_ViolentWriting1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_ViolentWriting1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code04_ViolentWriting1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code04_ViolentWriting1.addEdge0(u, v, w)
            Code04_ViolentWriting1.addEdge0(v, u, w)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code04_ViolentWriting1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code04_ViolentWriting1.addEdge2(u, v, w)
            Code04_ViolentWriting1.addEdge2(v, u, w)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < Code04_ViolentWriting1.MAXT):
            jset(Code04_ViolentWriting1.lmax, i, jset(Code04_ViolentWriting1.rmax, i, jcast('long', (-Code04_ViolentWriting1.INF))))
            i = jcast('int', (i + 1))
        Code04_ViolentWriting1.cntn = jcast('int', Code04_ViolentWriting1.n)
        Code04_ViolentWriting1.cnt1 = jcast('int', 1)
        Code04_ViolentWriting1.ans = jcast('long', jcast('long', (-Code04_ViolentWriting1.INF)))
        Code04_ViolentWriting1.getDist(1, 0, 0)
        Code04_ViolentWriting1.rebuild(1, 0)
        Code04_ViolentWriting1.solve(1)
        Code04_ViolentWriting1.compute(1, 0, 0)
        jcall(out, 'println', jcast('long', (Code04_ViolentWriting1.ans >> (1 & 63))))
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
            return jcast('int', self.buffer[((_java_obj_21 := self), (_java_key_22 := 'ptr'), (_java_old_23 := jget(_java_obj_21, _java_key_22)), jset(_java_obj_21, _java_key_22, jcast('int', (_java_old_23 + (1)))), _java_old_23)[4]])

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
            raise TypeError("No matching overload for Code04_ViolentWriting1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_ViolentWriting1.MAXN = jcast('int', 366667)
Code04_ViolentWriting1.MAXM = jcast('int', jcast('int', (Code04_ViolentWriting1.MAXN << (1 & 31))))
Code04_ViolentWriting1.MAXT = jcast('int', 10000001)
Code04_ViolentWriting1.INF = jcast('long', jcast('long', (1 << (50 & 63))))
Code04_ViolentWriting1.n = jcast('int', 0)
Code04_ViolentWriting1.cntn = jcast('int', 0)
Code04_ViolentWriting1.head0 = jarray('int', [Code04_ViolentWriting1.MAXN])
Code04_ViolentWriting1.next0 = jarray('int', [jcast('int', (Code04_ViolentWriting1.MAXN << (1 & 31)))])
Code04_ViolentWriting1.to0 = jarray('int', [jcast('int', (Code04_ViolentWriting1.MAXN << (1 & 31)))])
Code04_ViolentWriting1.weight0 = jarray('int', [jcast('int', (Code04_ViolentWriting1.MAXN << (1 & 31)))])
Code04_ViolentWriting1.cnt0 = jcast('int', 0)
Code04_ViolentWriting1.head1 = jarray('int', [Code04_ViolentWriting1.MAXM])
Code04_ViolentWriting1.next1 = jarray('int', [jcast('int', (Code04_ViolentWriting1.MAXM << (1 & 31)))])
Code04_ViolentWriting1.to1 = jarray('int', [jcast('int', (Code04_ViolentWriting1.MAXM << (1 & 31)))])
Code04_ViolentWriting1.weight1 = jarray('int', [jcast('int', (Code04_ViolentWriting1.MAXM << (1 & 31)))])
Code04_ViolentWriting1.cnt1 = jcast('int', 0)
Code04_ViolentWriting1.head2 = jarray('int', [Code04_ViolentWriting1.MAXN])
Code04_ViolentWriting1.next2 = jarray('int', [jcast('int', (Code04_ViolentWriting1.MAXN << (1 & 31)))])
Code04_ViolentWriting1.to2 = jarray('int', [jcast('int', (Code04_ViolentWriting1.MAXN << (1 & 31)))])
Code04_ViolentWriting1.weight2 = jarray('int', [jcast('int', (Code04_ViolentWriting1.MAXN << (1 & 31)))])
Code04_ViolentWriting1.cnt2 = jcast('int', 0)
Code04_ViolentWriting1.dis1 = jarray('long', [Code04_ViolentWriting1.MAXN])
Code04_ViolentWriting1.vis = jarray('boolean', [Code04_ViolentWriting1.MAXM])
Code04_ViolentWriting1.siz = jarray('int', [Code04_ViolentWriting1.MAXM])
Code04_ViolentWriting1.up = jarray('int', [Code04_ViolentWriting1.MAXN])
Code04_ViolentWriting1.root = jarray('int', [Code04_ViolentWriting1.MAXN])
Code04_ViolentWriting1.ls = jarray('int', [Code04_ViolentWriting1.MAXT])
Code04_ViolentWriting1.rs = jarray('int', [Code04_ViolentWriting1.MAXT])
Code04_ViolentWriting1.lmax = jarray('long', [Code04_ViolentWriting1.MAXT])
Code04_ViolentWriting1.rmax = jarray('long', [Code04_ViolentWriting1.MAXT])
Code04_ViolentWriting1.cntt = jcast('int', 0)
Code04_ViolentWriting1.ans = jcast('long', 0)

if __name__ == '__main__':
    Code04_ViolentWriting1.main([])
