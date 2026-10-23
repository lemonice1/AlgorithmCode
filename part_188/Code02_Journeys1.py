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

# 旅程，Python版
# 一共n个点，给定起点p，一共m次操作，格式如下
# 操作 a b c d : a~b范围每个点与c~d范围每个点之间，都增加一条无向边
# 所有操作完成后，计算起点p到每个点经过的最少边数，题目保证整体连通
# 1 <= n <= 5 * 10^5
# 1 <= m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P6348
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Journeys1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'INF': 'INF', 'n': 'n', 'm': 'm', 'p': 'p', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'ls': 'ls', 'rs': 'rs', 'rootOut': 'rootOut', 'rootIn': 'rootIn', 'cntt': 'cntt', 'dist': 'dist', 'deq': 'deq'}
    MAXN = 0
    MAXT = 0
    MAXE = 0
    INF = 0
    n = 0
    m = 0
    p = 0
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    ls = None
    rs = None
    rootOut = 0
    rootIn = 0
    cntt = 0
    dist = None
    deq = None
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code02_Journeys1.nxt, ((_java_obj_1 := Code02_Journeys1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_Journeys1.head[u])
        Code02_Journeys1.to[Code02_Journeys1.cntg] = jcast('int', v)
        Code02_Journeys1.weight[Code02_Journeys1.cntg] = jcast('int', w)
        Code02_Journeys1.head[u] = jcast('int', Code02_Journeys1.cntg)

    @staticmethod
    def buildOut(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = 0
        if (l == r):
            rt = jcast('int', l)
        else:
            rt = jcast('int', ((_java_obj_4 := Code02_Journeys1), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code02_Journeys1.ls, rt, Code02_Journeys1.buildOut(l, mid))
            jset(Code02_Journeys1.rs, rt, Code02_Journeys1.buildOut(jcast('int', jadd(mid, 1)), r))
            Code02_Journeys1.addEdge(Code02_Journeys1.ls[rt], rt, 0)
            Code02_Journeys1.addEdge(Code02_Journeys1.rs[rt], rt, 0)
        return jcast('int', rt)

    @staticmethod
    def buildIn(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = 0
        if (l == r):
            rt = jcast('int', l)
        else:
            rt = jcast('int', ((_java_obj_7 := Code02_Journeys1), (_java_key_8 := 'cntt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code02_Journeys1.ls, rt, Code02_Journeys1.buildIn(l, mid))
            jset(Code02_Journeys1.rs, rt, Code02_Journeys1.buildIn(jcast('int', jadd(mid, 1)), r))
            Code02_Journeys1.addEdge(rt, Code02_Journeys1.ls[rt], 0)
            Code02_Journeys1.addEdge(rt, Code02_Journeys1.rs[rt], 0)
        return jcast('int', rt)

    @staticmethod
    def xToRange(jobx, jobl, jobr, l, r, i):
        jobx = jcast('int', jobx)
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code02_Journeys1.addEdge(jobx, i, 0)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code02_Journeys1.xToRange(jobx, jobl, jobr, l, mid, Code02_Journeys1.ls[i])
            if (jobr > mid):
                Code02_Journeys1.xToRange(jobx, jobl, jobr, jcast('int', jadd(mid, 1)), r, Code02_Journeys1.rs[i])

    @staticmethod
    def rangeToX(jobl, jobr, jobx, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobx = jcast('int', jobx)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code02_Journeys1.addEdge(i, jobx, 0)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code02_Journeys1.rangeToX(jobl, jobr, jobx, l, mid, Code02_Journeys1.ls[i])
            if (jobr > mid):
                Code02_Journeys1.rangeToX(jobl, jobr, jobx, jcast('int', jadd(mid, 1)), r, Code02_Journeys1.rs[i])

    @staticmethod
    def rangeToRange(a, b, c, d):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        x = jcast('int', ((_java_obj_10 := Code02_Journeys1), (_java_key_11 := 'cntt'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
        y = jcast('int', ((_java_obj_13 := Code02_Journeys1), (_java_key_14 := 'cntt'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
        Code02_Journeys1.rangeToX(a, b, x, 1, Code02_Journeys1.n, Code02_Journeys1.rootOut)
        Code02_Journeys1.xToRange(y, c, d, 1, Code02_Journeys1.n, Code02_Journeys1.rootIn)
        Code02_Journeys1.addEdge(x, y, 1)

    @staticmethod
    def bfs01():
        i = jcast('int', 1)
        while (i <= Code02_Journeys1.cntt):
            Code02_Journeys1.dist[i] = jcast('int', Code02_Journeys1.INF)
            i = jcast('int', (i + 1))
        Code02_Journeys1.dist[Code02_Journeys1.p] = jcast('int', 0)
        jcall(Code02_Journeys1.deq, 'addFirst', Code02_Journeys1.p)
        while (not jcall(Code02_Journeys1.deq, 'isEmpty')):
            u = jcast('int', jcall(Code02_Journeys1.deq, 'pollFirst'))
            e = jcast('int', Code02_Journeys1.head[u])
            while (e > 0):
                v = jcast('int', Code02_Journeys1.to[e])
                w = jcast('int', Code02_Journeys1.weight[e])
                if (Code02_Journeys1.dist[v] > jcast('int', jadd(Code02_Journeys1.dist[u], w))):
                    Code02_Journeys1.dist[v] = jcast('int', jcast('int', jadd(Code02_Journeys1.dist[u], w)))
                    if (w == 0):
                        jcall(Code02_Journeys1.deq, 'addFirst', v)
                    else:
                        jcall(Code02_Journeys1.deq, 'addLast', v)
                e = jcast('int', Code02_Journeys1.nxt[e])

    @staticmethod
    def main(args):
        in_ = Code02_Journeys1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_Journeys1.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_Journeys1.m = jcast('int', jcall(in_, 'nextInt'))
        Code02_Journeys1.p = jcast('int', jcall(in_, 'nextInt'))
        Code02_Journeys1.cntt = jcast('int', Code02_Journeys1.n)
        Code02_Journeys1.rootOut = jcast('int', Code02_Journeys1.buildOut(1, Code02_Journeys1.n))
        Code02_Journeys1.rootIn = jcast('int', Code02_Journeys1.buildIn(1, Code02_Journeys1.n))
        i = jcast('int', 1)
        a = 0
        b = 0
        c = 0
        d = 0
        while (i <= Code02_Journeys1.m):
            a = jcast('int', jcall(in_, 'nextInt'))
            b = jcast('int', jcall(in_, 'nextInt'))
            c = jcast('int', jcall(in_, 'nextInt'))
            d = jcast('int', jcall(in_, 'nextInt'))
            Code02_Journeys1.rangeToRange(a, b, c, d)
            Code02_Journeys1.rangeToRange(c, d, a, b)
            i = jcast('int', (i + 1))
        Code02_Journeys1.bfs01()
        i = jcast('int', 1)
        while (i <= Code02_Journeys1.n):
            jcall(out, 'println', Code02_Journeys1.dist[i])
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
            return jcast('int', self.buffer[((_java_obj_16 := self), (_java_key_17 := 'ptr'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))), _java_old_18)[4]])

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
            raise TypeError("No matching overload for Code02_Journeys1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Journeys1.MAXN = jcast('int', 500001)
Code02_Journeys1.MAXT = jcast('int', jcast('int', (Code02_Journeys1.MAXN * 10)))
Code02_Journeys1.MAXE = jcast('int', jcast('int', (Code02_Journeys1.MAXN * 20)))
Code02_Journeys1.INF = jcast('int', jcast('int', (1 << (30 & 31))))
Code02_Journeys1.n = jcast('int', 0)
Code02_Journeys1.m = jcast('int', 0)
Code02_Journeys1.p = jcast('int', 0)
Code02_Journeys1.head = jarray('int', [Code02_Journeys1.MAXT])
Code02_Journeys1.nxt = jarray('int', [Code02_Journeys1.MAXE])
Code02_Journeys1.to = jarray('int', [Code02_Journeys1.MAXE])
Code02_Journeys1.weight = jarray('int', [Code02_Journeys1.MAXE])
Code02_Journeys1.cntg = jcast('int', 0)
Code02_Journeys1.ls = jarray('int', [Code02_Journeys1.MAXT])
Code02_Journeys1.rs = jarray('int', [Code02_Journeys1.MAXT])
Code02_Journeys1.rootOut = jcast('int', 0)
Code02_Journeys1.rootIn = jcast('int', 0)
Code02_Journeys1.cntt = jcast('int', 0)
Code02_Journeys1.dist = jarray('int', [Code02_Journeys1.MAXT])
Code02_Journeys1.deq = jnew('ArrayDeque')

if __name__ == '__main__':
    Code02_Journeys1.main([])
