# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 遗产，Python版
# 一共n个点，给定起点s，一共q条操作，操作类型如下
# 操作 1 x y w   : 从点x到点y增加有向边，边权是w
# 操作 2 x l r w : 从点x到l~r范围的每个点增加有向边，边权都是w
# 操作 3 x l r w : 从l~r范围的每个点到点x增加有向边，边权都是w
# 所有操作完成后，计算起点s到每个点的最短距离并打印，如果不连通打印-1
# 1 <= n、q <= 10^5
# 1 <= w <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/CF786B
# 测试链接 : https://codeforces.com/problemset/problem/786/B
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_Legacy1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'INF': 'INF', 'n': 'n', 'q': 'q', 's': 's', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'ls': 'ls', 'rs': 'rs', 'rootOut': 'rootOut', 'rootIn': 'rootIn', 'cntt': 'cntt', 'dist': 'dist', 'vis': 'vis', 'heap': 'heap'}
    MAXN = 0
    MAXT = 0
    MAXE = 0
    INF = 0
    n = 0
    q = 0
    s = 0
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    # 出树和入树共用ls和rs
    # 出树的头节点编号rootOut
    # 入树的头节点编号rootIn
    # 空间利用cntt计数来分配
    # 可持久化线段树，即主席树，也是这种设计
    ls = None
    rs = None
    rootOut = 0
    rootIn = 0
    cntt = 0
    dist = None
    vis = None
    # 当前点、源点到当前点的代价
    heap = None
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code01_Legacy1.nxt, ((_java_obj_1 := Code01_Legacy1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_Legacy1.head[u])
        Code01_Legacy1.to[Code01_Legacy1.cntg] = jcast('int', v)
        Code01_Legacy1.weight[Code01_Legacy1.cntg] = jcast('int', w)
        Code01_Legacy1.head[u] = jcast('int', Code01_Legacy1.cntg)

    @staticmethod
    def buildOut(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = 0
        if (l == r):
            rt = jcast('int', l)
        else:
            rt = jcast('int', ((_java_obj_4 := Code01_Legacy1), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code01_Legacy1.ls, rt, Code01_Legacy1.buildOut(l, mid))
            jset(Code01_Legacy1.rs, rt, Code01_Legacy1.buildOut(jcast('int', jadd(mid, 1)), r))
            Code01_Legacy1.addEdge(Code01_Legacy1.ls[rt], rt, 0)
            Code01_Legacy1.addEdge(Code01_Legacy1.rs[rt], rt, 0)
        return jcast('int', rt)

    @staticmethod
    def buildIn(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = 0
        if (l == r):
            rt = jcast('int', l)
        else:
            rt = jcast('int', ((_java_obj_7 := Code01_Legacy1), (_java_key_8 := 'cntt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code01_Legacy1.ls, rt, Code01_Legacy1.buildIn(l, mid))
            jset(Code01_Legacy1.rs, rt, Code01_Legacy1.buildIn(jcast('int', jadd(mid, 1)), r))
            Code01_Legacy1.addEdge(rt, Code01_Legacy1.ls[rt], 0)
            Code01_Legacy1.addEdge(rt, Code01_Legacy1.rs[rt], 0)
        return jcast('int', rt)

    @staticmethod
    def xToRange(jobx, jobl, jobr, jobw, l, r, i):
        jobx = jcast('int', jobx)
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobw = jcast('int', jobw)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code01_Legacy1.addEdge(jobx, i, jobw)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code01_Legacy1.xToRange(jobx, jobl, jobr, jobw, l, mid, Code01_Legacy1.ls[i])
            if (jobr > mid):
                Code01_Legacy1.xToRange(jobx, jobl, jobr, jobw, jcast('int', jadd(mid, 1)), r, Code01_Legacy1.rs[i])

    @staticmethod
    def rangeToX(jobl, jobr, jobx, jobw, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobx = jcast('int', jobx)
        jobw = jcast('int', jobw)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code01_Legacy1.addEdge(i, jobx, jobw)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code01_Legacy1.rangeToX(jobl, jobr, jobx, jobw, l, mid, Code01_Legacy1.ls[i])
            if (jobr > mid):
                Code01_Legacy1.rangeToX(jobl, jobr, jobx, jobw, jcast('int', jadd(mid, 1)), r, Code01_Legacy1.rs[i])

    @staticmethod
    def dijkstra():
        i = jcast('int', 1)
        while (i <= Code01_Legacy1.cntt):
            Code01_Legacy1.dist[i] = jcast('long', Code01_Legacy1.INF)
            i = jcast('int', (i + 1))
        Code01_Legacy1.dist[Code01_Legacy1.s] = jcast('long', 0)
        jcall(Code01_Legacy1.heap, 'add', jarray('long', [None], [Code01_Legacy1.s, 0]))
        while (not jcall(Code01_Legacy1.heap, 'isEmpty')):
            cur = jcall(Code01_Legacy1.heap, 'poll')
            u = jcast('int', jcast('int', cur[0]))
            d = jcast('long', cur[1])
            if (not Code01_Legacy1.vis[u]):
                Code01_Legacy1.vis[u] = jcast('boolean', True)
                e = jcast('int', Code01_Legacy1.head[u])
                while (e > 0):
                    v = jcast('int', Code01_Legacy1.to[e])
                    w = jcast('int', Code01_Legacy1.weight[e])
                    if ((not Code01_Legacy1.vis[v]) and (Code01_Legacy1.dist[v] > jcast('long', jadd(d, w)))):
                        Code01_Legacy1.dist[v] = jcast('long', jcast('long', jadd(d, w)))
                        jcall(Code01_Legacy1.heap, 'add', jarray('long', [None], [v, Code01_Legacy1.dist[v]]))
                    e = jcast('int', Code01_Legacy1.nxt[e])

    @staticmethod
    def main(args):
        in_ = Code01_Legacy1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_Legacy1.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_Legacy1.q = jcast('int', jcall(in_, 'nextInt'))
        Code01_Legacy1.s = jcast('int', jcall(in_, 'nextInt'))
        Code01_Legacy1.cntt = jcast('int', Code01_Legacy1.n)
        Code01_Legacy1.rootOut = jcast('int', Code01_Legacy1.buildOut(1, Code01_Legacy1.n))
        Code01_Legacy1.rootIn = jcast('int', Code01_Legacy1.buildIn(1, Code01_Legacy1.n))
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        l = 0
        r = 0
        w = 0
        while (i <= Code01_Legacy1.q):
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                w = jcast('int', jcall(in_, 'nextInt'))
                Code01_Legacy1.addEdge(x, y, w)
            else:
                if (op == 2):
                    x = jcast('int', jcall(in_, 'nextInt'))
                    l = jcast('int', jcall(in_, 'nextInt'))
                    r = jcast('int', jcall(in_, 'nextInt'))
                    w = jcast('int', jcall(in_, 'nextInt'))
                    Code01_Legacy1.xToRange(x, l, r, w, 1, Code01_Legacy1.n, Code01_Legacy1.rootIn)
                else:
                    x = jcast('int', jcall(in_, 'nextInt'))
                    l = jcast('int', jcall(in_, 'nextInt'))
                    r = jcast('int', jcall(in_, 'nextInt'))
                    w = jcast('int', jcall(in_, 'nextInt'))
                    Code01_Legacy1.rangeToX(l, r, x, w, 1, Code01_Legacy1.n, Code01_Legacy1.rootOut)
            i = jcast('int', (i + 1))
        Code01_Legacy1.dijkstra()
        i = jcast('int', 1)
        while (i <= Code01_Legacy1.n):
            jcall(out, 'print', (jcast('int', (-1)) if (Code01_Legacy1.dist[i] == Code01_Legacy1.INF) else Code01_Legacy1.dist[i]))
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
            return jcast('int', self.buffer[((_java_obj_10 := self), (_java_key_11 := 'ptr'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]])

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
            raise TypeError("No matching overload for Code01_Legacy1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_Legacy1.MAXN = jcast('int', 100001)
Code01_Legacy1.MAXT = jcast('int', jcast('int', (Code01_Legacy1.MAXN * 10)))
Code01_Legacy1.MAXE = jcast('int', jcast('int', (Code01_Legacy1.MAXN * 30)))
Code01_Legacy1.INF = jcast('long', jcast('long', (1 << (60 & 63))))
Code01_Legacy1.n = jcast('int', 0)
Code01_Legacy1.q = jcast('int', 0)
Code01_Legacy1.s = jcast('int', 0)
Code01_Legacy1.head = jarray('int', [Code01_Legacy1.MAXT])
Code01_Legacy1.nxt = jarray('int', [Code01_Legacy1.MAXE])
Code01_Legacy1.to = jarray('int', [Code01_Legacy1.MAXE])
Code01_Legacy1.weight = jarray('int', [Code01_Legacy1.MAXE])
Code01_Legacy1.cntg = jcast('int', 0)
Code01_Legacy1.ls = jarray('int', [Code01_Legacy1.MAXT])
Code01_Legacy1.rs = jarray('int', [Code01_Legacy1.MAXT])
Code01_Legacy1.rootOut = jcast('int', 0)
Code01_Legacy1.rootIn = jcast('int', 0)
Code01_Legacy1.cntt = jcast('int', 0)
Code01_Legacy1.dist = jarray('long', [Code01_Legacy1.MAXT])
Code01_Legacy1.vis = jarray('boolean', [Code01_Legacy1.MAXT])
Code01_Legacy1.heap = jnew('PriorityQueue', (lambda x, y: jstatic('Long', 'compare', x[1], y[1])))

if __name__ == '__main__':
    Code01_Legacy1.main([])
