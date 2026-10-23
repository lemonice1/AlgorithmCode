# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 道路，Python版
# 一共n个点，一共m次操作，格式如下
# 操作 a b c d w: a~b范围每个点与c~d范围每个点之间，都增加权值为w的无向边
# 给定数字k，表示有k次机会，每次在通过一条边时，不用支付这条边的代价
# 所有操作完成后，打印1号点到n号点的最低代价
# 如果不存在通路，打印"CreationAugust is a sb!"
# 1 <= n <= 5 * 10^4
# 1 <= m <= 10^5
# 1 <= k <= 10
# 1 <= w <= 10^3
# 测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=5669
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Road2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'MAXK': 'MAXK', 'INF': 'INF', 't': 't', 'n': 'n', 'm': 'm', 'k': 'k', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'ls': 'ls', 'rs': 'rs', 'rootOut': 'rootOut', 'rootIn': 'rootIn', 'cntt': 'cntt', 'dist': 'dist', 'vis': 'vis', 'heap': 'heap'}
    MAXN = 0
    MAXT = 0
    MAXE = 0
    MAXK = 0
    INF = 0
    t = 0
    n = 0
    m = 0
    k = 0
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
    vis = None
    # 编号、次数、花费
    heap = None
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code03_Road2.nxt, ((_java_obj_1 := Code03_Road2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_Road2.head[u])
        Code03_Road2.to[Code03_Road2.cntg] = jcast('int', v)
        Code03_Road2.weight[Code03_Road2.cntg] = jcast('int', w)
        Code03_Road2.head[u] = jcast('int', Code03_Road2.cntg)

    @staticmethod
    def buildOut(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = 0
        if (l == r):
            rt = jcast('int', l)
        else:
            rt = jcast('int', ((_java_obj_4 := Code03_Road2), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code03_Road2.ls, rt, Code03_Road2.buildOut(l, mid))
            jset(Code03_Road2.rs, rt, Code03_Road2.buildOut(jcast('int', jadd(mid, 1)), r))
            Code03_Road2.addEdge(Code03_Road2.ls[rt], rt, 0)
            Code03_Road2.addEdge(Code03_Road2.rs[rt], rt, 0)
        return jcast('int', rt)

    @staticmethod
    def buildIn(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = 0
        if (l == r):
            rt = jcast('int', l)
        else:
            rt = jcast('int', ((_java_obj_7 := Code03_Road2), (_java_key_8 := 'cntt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code03_Road2.ls, rt, Code03_Road2.buildIn(l, mid))
            jset(Code03_Road2.rs, rt, Code03_Road2.buildIn(jcast('int', jadd(mid, 1)), r))
            Code03_Road2.addEdge(rt, Code03_Road2.ls[rt], 0)
            Code03_Road2.addEdge(rt, Code03_Road2.rs[rt], 0)
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
            Code03_Road2.addEdge(jobx, i, 0)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code03_Road2.xToRange(jobx, jobl, jobr, l, mid, Code03_Road2.ls[i])
            if (jobr > mid):
                Code03_Road2.xToRange(jobx, jobl, jobr, jcast('int', jadd(mid, 1)), r, Code03_Road2.rs[i])

    @staticmethod
    def rangeToX(jobl, jobr, jobx, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobx = jcast('int', jobx)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code03_Road2.addEdge(i, jobx, 0)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code03_Road2.rangeToX(jobl, jobr, jobx, l, mid, Code03_Road2.ls[i])
            if (jobr > mid):
                Code03_Road2.rangeToX(jobl, jobr, jobx, jcast('int', jadd(mid, 1)), r, Code03_Road2.rs[i])

    @staticmethod
    def rangeToRange(a, b, c, d, w):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        w = jcast('int', w)
        x = jcast('int', ((_java_obj_10 := Code03_Road2), (_java_key_11 := 'cntt'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
        y = jcast('int', ((_java_obj_13 := Code03_Road2), (_java_key_14 := 'cntt'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
        Code03_Road2.rangeToX(a, b, x, 1, Code03_Road2.n, Code03_Road2.rootOut)
        Code03_Road2.xToRange(y, c, d, 1, Code03_Road2.n, Code03_Road2.rootIn)
        Code03_Road2.addEdge(x, y, w)

    @staticmethod
    def dijkstra(start, target):
        start = jcast('int', start)
        target = jcast('int', target)
        i = jcast('int', 1)
        while (i <= Code03_Road2.cntt):
            j = jcast('int', 0)
            while (j <= Code03_Road2.k):
                jset(Code03_Road2.dist[i], j, Code03_Road2.INF)
                jset(Code03_Road2.vis[i], j, False)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        jset(Code03_Road2.dist[start], 0, 0)
        jcall(Code03_Road2.heap, 'add', jarray('int', [None], [start, 0, 0]))
        while (not jcall(Code03_Road2.heap, 'isEmpty')):
            cur = jcall(Code03_Road2.heap, 'poll')
            node = jcast('int', cur[0])
            time = jcast('int', cur[1])
            cost = jcast('int', cur[2])
            if (not Code03_Road2.vis[node][time]):
                jset(Code03_Road2.vis[node], time, True)
                if (node == target):
                    return jcast('int', cost)
                e = jcast('int', Code03_Road2.head[node])
                while (e > 0):
                    v = jcast('int', Code03_Road2.to[e])
                    w = jcast('int', Code03_Road2.weight[e])
                    if ((not Code03_Road2.vis[v][time]) and (Code03_Road2.dist[v][time] > jcast('int', jadd(cost, w)))):
                        jset(Code03_Road2.dist[v], time, jcast('int', jadd(cost, w)))
                        jcall(Code03_Road2.heap, 'add', jarray('int', [None], [v, time, Code03_Road2.dist[v][time]]))
                    if (((time < Code03_Road2.k) and (not Code03_Road2.vis[v][jcast('int', jadd(time, 1))])) and (Code03_Road2.dist[v][jcast('int', jadd(time, 1))] > cost)):
                        jset(Code03_Road2.dist[v], jcast('int', jadd(time, 1)), cost)
                        jcall(Code03_Road2.heap, 'add', jarray('int', [None], [v, jcast('int', jadd(time, 1)), Code03_Road2.dist[v][jcast('int', jadd(time, 1))]]))
                    e = jcast('int', Code03_Road2.nxt[e])
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def clear():
        i = jcast('int', 1)
        while (i <= Code03_Road2.cntt):
            Code03_Road2.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        Code03_Road2.cntg = jcast('int', jset(Code03_Road2, 'cntt', 0))
        jcall(Code03_Road2.heap, 'clear')

    @staticmethod
    def main(args):
        in_ = Code03_Road2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_Road2.t = jcast('int', jcall(in_, 'nextInt'))
        test = jcast('int', 1)
        while (test <= Code03_Road2.t):
            Code03_Road2.n = jcast('int', jcall(in_, 'nextInt'))
            Code03_Road2.m = jcast('int', jcall(in_, 'nextInt'))
            Code03_Road2.k = jcast('int', jcall(in_, 'nextInt'))
            Code03_Road2.cntt = jcast('int', Code03_Road2.n)
            Code03_Road2.rootOut = jcast('int', Code03_Road2.buildOut(1, Code03_Road2.n))
            Code03_Road2.rootIn = jcast('int', Code03_Road2.buildIn(1, Code03_Road2.n))
            i = jcast('int', 1)
            a = 0
            b = 0
            c = 0
            d = 0
            w = 0
            while (i <= Code03_Road2.m):
                a = jcast('int', jcall(in_, 'nextInt'))
                b = jcast('int', jcall(in_, 'nextInt'))
                c = jcast('int', jcall(in_, 'nextInt'))
                d = jcast('int', jcall(in_, 'nextInt'))
                w = jcast('int', jcall(in_, 'nextInt'))
                Code03_Road2.rangeToRange(a, b, c, d, w)
                Code03_Road2.rangeToRange(c, d, a, b, w)
                i = jcast('int', (i + 1))
            ans = jcast('int', Code03_Road2.dijkstra(1, Code03_Road2.n))
            if (ans == jcast('int', (-1))):
                jcall(out, 'println', 'CreationAugust is a sb!')
            else:
                jcall(out, 'println', ans)
            Code03_Road2.clear()
            test = jcast('int', (test + 1))
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
            raise TypeError("No matching overload for Code03_Road2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Road2.MAXN = jcast('int', 50001)
Code03_Road2.MAXT = jcast('int', jcast('int', (Code03_Road2.MAXN * 10)))
Code03_Road2.MAXE = jcast('int', jcast('int', (Code03_Road2.MAXN * 20)))
Code03_Road2.MAXK = jcast('int', 11)
Code03_Road2.INF = jcast('int', jcast('int', (1 << (30 & 31))))
Code03_Road2.t = jcast('int', 0)
Code03_Road2.n = jcast('int', 0)
Code03_Road2.m = jcast('int', 0)
Code03_Road2.k = jcast('int', 0)
Code03_Road2.head = jarray('int', [Code03_Road2.MAXT])
Code03_Road2.nxt = jarray('int', [Code03_Road2.MAXE])
Code03_Road2.to = jarray('int', [Code03_Road2.MAXE])
Code03_Road2.weight = jarray('int', [Code03_Road2.MAXE])
Code03_Road2.cntg = jcast('int', 0)
Code03_Road2.ls = jarray('int', [Code03_Road2.MAXT])
Code03_Road2.rs = jarray('int', [Code03_Road2.MAXT])
Code03_Road2.rootOut = jcast('int', 0)
Code03_Road2.rootIn = jcast('int', 0)
Code03_Road2.cntt = jcast('int', 0)
Code03_Road2.dist = jarray('int', [Code03_Road2.MAXT, Code03_Road2.MAXK])
Code03_Road2.vis = jarray('boolean', [Code03_Road2.MAXT, Code03_Road2.MAXK])
Code03_Road2.heap = jnew('PriorityQueue', (lambda a, b: (a[2] - b[2])))

if __name__ == '__main__':
    Code03_Road2.main([])
