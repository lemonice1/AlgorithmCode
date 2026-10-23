# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# Johnson全源最短路，Python版
# 一共n个点，m条有向边，边有边权，可能有负边、重边、自环
# 如果图中存在负环，打印-1即可，否则计算任意两点的最短距离
# 如果不存在通路，认为距离是10^9，每个点到自己的距离认为是0
# 无负环时，输出n行结果，点i到点j的最短距离记为dist(i, j)
# 第i行的输出 = 累加所有 { dist(i, j) * j }，1 <= j <= n
# 1 <= n <= 3 * 10^3
# 1 <= m <= 6 * 10^3
# -3 * 10^5 <= 边权 <= +3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P5905
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 使用反向索引堆实现 Dijkstra 算法，参见讲解064
# 使用普通堆实现 Dijkstra 算法
class Code01_JohnsonAlgorithm1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXQ': 'MAXQ', 'INF': 'INF', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'h': 'h', 'update': 'update', 'enter': 'enter', 'que': 'que', 'dist': 'dist', 'heap': 'heap', 'where': 'where', 'heapSize': 'heapSize'}
    MAXN = 0
    MAXQ = 0
    INF = 0
    n = 0
    m = 0
    # 建图
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    # spfa
    h = None
    update = None
    enter = None
    que = None
    # dijkstra，反向索引堆优化
    dist = None
    heap = None
    # where[v] = -1，表示v这个节点，从来没有进入过堆
    # where[v] = -2，表示v这个节点，已经弹出过了
    # where[v] >= 0，表示v这个节点在堆上的位置
    where = None
    heapSize = 0
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code01_JohnsonAlgorithm1.nxt, ((_java_obj_1 := Code01_JohnsonAlgorithm1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_JohnsonAlgorithm1.head[u])
        Code01_JohnsonAlgorithm1.to[Code01_JohnsonAlgorithm1.cntg] = jcast('int', v)
        Code01_JohnsonAlgorithm1.weight[Code01_JohnsonAlgorithm1.cntg] = jcast('int', w)
        Code01_JohnsonAlgorithm1.head[u] = jcast('int', Code01_JohnsonAlgorithm1.cntg)

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code01_JohnsonAlgorithm1.heap[i])
        Code01_JohnsonAlgorithm1.heap[i] = jcast('int', Code01_JohnsonAlgorithm1.heap[j])
        Code01_JohnsonAlgorithm1.heap[j] = jcast('int', tmp)
        jset(Code01_JohnsonAlgorithm1.where, Code01_JohnsonAlgorithm1.heap[i], i)
        jset(Code01_JohnsonAlgorithm1.where, Code01_JohnsonAlgorithm1.heap[j], j)

    @staticmethod
    def heapInsert(i):
        i = jcast('int', i)
        while (Code01_JohnsonAlgorithm1.dist[Code01_JohnsonAlgorithm1.heap[i]] < Code01_JohnsonAlgorithm1.dist[Code01_JohnsonAlgorithm1.heap[jcast('int', jdiv(jcast('int', (i - 1)), 2))]]):
            Code01_JohnsonAlgorithm1.swap(i, jcast('int', jdiv(jcast('int', (i - 1)), 2)))
            i = jcast('int', jcast('int', jdiv(jcast('int', (i - 1)), 2)))

    @staticmethod
    def heapify(i):
        i = jcast('int', i)
        l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
        while (l < Code01_JohnsonAlgorithm1.heapSize):
            try:
                best = jcast('int', (jcast('int', jadd(l, 1)) if ((jcast('int', jadd(l, 1)) < Code01_JohnsonAlgorithm1.heapSize) and (Code01_JohnsonAlgorithm1.dist[Code01_JohnsonAlgorithm1.heap[jcast('int', jadd(l, 1))]] < Code01_JohnsonAlgorithm1.dist[Code01_JohnsonAlgorithm1.heap[l]])) else l))
                best = jcast('int', (best if (Code01_JohnsonAlgorithm1.dist[Code01_JohnsonAlgorithm1.heap[best]] < Code01_JohnsonAlgorithm1.dist[Code01_JohnsonAlgorithm1.heap[i]]) else i))
                if (best == i):
                    raise JBreak(None)
                Code01_JohnsonAlgorithm1.swap(best, i)
                i = jcast('int', best)
                l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break

    @staticmethod
    def isEmpty():
        return jcast('boolean', (Code01_JohnsonAlgorithm1.heapSize == 0))

    @staticmethod
    def pop():
        ans = jcast('int', Code01_JohnsonAlgorithm1.heap[0])
        Code01_JohnsonAlgorithm1.swap(0, ((_java_obj_5 := Code01_JohnsonAlgorithm1), (_java_key_6 := 'heapSize'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))))[3])
        Code01_JohnsonAlgorithm1.heapify(0)
        Code01_JohnsonAlgorithm1.where[ans] = jcast('int', jcast('int', (-2)))
        return jcast('int', ans)

    @staticmethod
    def addOrUpdateOrIgnore(v, d):
        v = jcast('int', v)
        d = jcast('int', d)
        if ((Code01_JohnsonAlgorithm1.where[v] == jcast('int', (-2))) or (Code01_JohnsonAlgorithm1.dist[v] <= d)):
            return
        if (Code01_JohnsonAlgorithm1.where[v] == jcast('int', (-1))):
            Code01_JohnsonAlgorithm1.heap[Code01_JohnsonAlgorithm1.heapSize] = jcast('int', v)
            jset(Code01_JohnsonAlgorithm1.where, v, ((_java_obj_8 := Code01_JohnsonAlgorithm1), (_java_key_9 := 'heapSize'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))), _java_old_10)[4])
        Code01_JohnsonAlgorithm1.dist[v] = jcast('int', d)
        Code01_JohnsonAlgorithm1.heapInsert(Code01_JohnsonAlgorithm1.where[v])

    # 返回是否发现了负环
    @staticmethod
    def spfa(s):
        s = jcast('int', s)
        i = jcast('int', 1)
        while (i <= Code01_JohnsonAlgorithm1.n):
            Code01_JohnsonAlgorithm1.h[i] = jcast('int', Code01_JohnsonAlgorithm1.INF)
            i = jcast('int', (i + 1))
        Code01_JohnsonAlgorithm1.h[s] = jcast('int', 0)
        Code01_JohnsonAlgorithm1.update[s] = jcast('int', 1)
        Code01_JohnsonAlgorithm1.enter[s] = jcast('boolean', True)
        ql = jcast('int', 1)
        qr = jcast('int', 0)
        jset(Code01_JohnsonAlgorithm1.que, (qr := jcast('int', (qr + (1)))), s)
        while (ql <= qr):
            u = jcast('int', Code01_JohnsonAlgorithm1.que[((_java_old_11 := ql), (ql := jcast('int', (ql + (1)))), _java_old_11)[2]])
            Code01_JohnsonAlgorithm1.enter[u] = jcast('boolean', False)
            ei = jcast('int', Code01_JohnsonAlgorithm1.head[u])
            v = 0
            w = 0
            while (ei > 0):
                v = jcast('int', Code01_JohnsonAlgorithm1.to[ei])
                w = jcast('int', Code01_JohnsonAlgorithm1.weight[ei])
                if (Code01_JohnsonAlgorithm1.h[v] > jcast('int', jadd(Code01_JohnsonAlgorithm1.h[u], w))):
                    Code01_JohnsonAlgorithm1.h[v] = jcast('int', jcast('int', jadd(Code01_JohnsonAlgorithm1.h[u], w)))
                    if (not Code01_JohnsonAlgorithm1.enter[v]):
                        if (((_java_obj_12 := Code01_JohnsonAlgorithm1.update), (_java_key_13 := v), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))))[3] > Code01_JohnsonAlgorithm1.n):
                            return jcast('boolean', True)
                        jset(Code01_JohnsonAlgorithm1.que, (qr := jcast('int', (qr + (1)))), v)
                        Code01_JohnsonAlgorithm1.enter[v] = jcast('boolean', True)
                ei = jcast('int', Code01_JohnsonAlgorithm1.nxt[ei])
        return jcast('boolean', False)

    # dijkstra算法，反向索引堆优化，讲解064
    @staticmethod
    def dijkstra(s):
        s = jcast('int', s)
        i = jcast('int', 1)
        while (i <= Code01_JohnsonAlgorithm1.n):
            Code01_JohnsonAlgorithm1.dist[i] = jcast('int', Code01_JohnsonAlgorithm1.INF)
            Code01_JohnsonAlgorithm1.where[i] = jcast('int', jcast('int', (-1)))
            i = jcast('int', (i + 1))
        Code01_JohnsonAlgorithm1.heapSize = jcast('int', 0)
        Code01_JohnsonAlgorithm1.addOrUpdateOrIgnore(s, 0)
        while (not Code01_JohnsonAlgorithm1.isEmpty()):
            u = jcast('int', Code01_JohnsonAlgorithm1.pop())
            d = jcast('int', Code01_JohnsonAlgorithm1.dist[u])
            e = jcast('int', Code01_JohnsonAlgorithm1.head[u])
            while (e > 0):
                Code01_JohnsonAlgorithm1.addOrUpdateOrIgnore(Code01_JohnsonAlgorithm1.to[e], jcast('int', jadd(d, Code01_JohnsonAlgorithm1.weight[e])))
                e = jcast('int', Code01_JohnsonAlgorithm1.nxt[e])

    @staticmethod
    def main(args):
        in_ = Code01_JohnsonAlgorithm1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_JohnsonAlgorithm1.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_JohnsonAlgorithm1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i <= Code01_JohnsonAlgorithm1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code01_JohnsonAlgorithm1.addEdge(u, v, w)
            i = jcast('int', (i + 1))
        virtualNode = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code01_JohnsonAlgorithm1.n):
            Code01_JohnsonAlgorithm1.addEdge(virtualNode, i, 0)
            i = jcast('int', (i + 1))
        if Code01_JohnsonAlgorithm1.spfa(virtualNode):
            jcall(out, 'println', '-1')
        else:
            u = jcast('int', 1)
            while (u <= Code01_JohnsonAlgorithm1.n):
                e = jcast('int', Code01_JohnsonAlgorithm1.head[u])
                while (e > 0):
                    v = jcast('int', Code01_JohnsonAlgorithm1.to[e])
                    Code01_JohnsonAlgorithm1.weight[e] = jcast('int', jcast('int', jadd(Code01_JohnsonAlgorithm1.weight[e], jcast('int', (Code01_JohnsonAlgorithm1.h[u] - Code01_JohnsonAlgorithm1.h[v])))))
                    e = jcast('int', Code01_JohnsonAlgorithm1.nxt[e])
                u = jcast('int', (u + 1))
            i = jcast('int', 1)
            while (i <= Code01_JohnsonAlgorithm1.n):
                Code01_JohnsonAlgorithm1.dijkstra(i)
                ans = jcast('long', 0)
                j = jcast('int', 1)
                while (j <= Code01_JohnsonAlgorithm1.n):
                    if (Code01_JohnsonAlgorithm1.dist[j] == Code01_JohnsonAlgorithm1.INF):
                        ans = jcast('long', jcast('long', jadd(ans, jcast('long', (jcast('long', (1 * j)) * Code01_JohnsonAlgorithm1.INF)))))
                    else:
                        ans = jcast('long', jcast('long', jadd(ans, jcast('long', (jcast('long', (1 * j)) * jcast('int', jadd(jcast('int', (Code01_JohnsonAlgorithm1.dist[j] - Code01_JohnsonAlgorithm1.h[i])), Code01_JohnsonAlgorithm1.h[j])))))))
                    j = jcast('int', (j + 1))
                jcall(out, 'println', ans)
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
            return jcast('int', self.buffer[((_java_obj_15 := self), (_java_key_16 := 'ptr'), (_java_old_17 := jget(_java_obj_15, _java_key_16)), jset(_java_obj_15, _java_key_16, jcast('int', (_java_old_17 + (1)))), _java_old_17)[4]])

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
            raise TypeError("No matching overload for Code01_JohnsonAlgorithm1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_JohnsonAlgorithm1.MAXN = jcast('int', 10001)
Code01_JohnsonAlgorithm1.MAXQ = jcast('int', 5000001)
Code01_JohnsonAlgorithm1.INF = jcast('int', 1000000000)
Code01_JohnsonAlgorithm1.n = jcast('int', 0)
Code01_JohnsonAlgorithm1.m = jcast('int', 0)
Code01_JohnsonAlgorithm1.head = jarray('int', [Code01_JohnsonAlgorithm1.MAXN])
Code01_JohnsonAlgorithm1.nxt = jarray('int', [Code01_JohnsonAlgorithm1.MAXN])
Code01_JohnsonAlgorithm1.to = jarray('int', [Code01_JohnsonAlgorithm1.MAXN])
Code01_JohnsonAlgorithm1.weight = jarray('int', [Code01_JohnsonAlgorithm1.MAXN])
Code01_JohnsonAlgorithm1.cntg = jcast('int', 0)
Code01_JohnsonAlgorithm1.h = jarray('int', [Code01_JohnsonAlgorithm1.MAXN])
Code01_JohnsonAlgorithm1.update = jarray('int', [Code01_JohnsonAlgorithm1.MAXN])
Code01_JohnsonAlgorithm1.enter = jarray('boolean', [Code01_JohnsonAlgorithm1.MAXN])
Code01_JohnsonAlgorithm1.que = jarray('int', [Code01_JohnsonAlgorithm1.MAXQ])
Code01_JohnsonAlgorithm1.dist = jarray('int', [Code01_JohnsonAlgorithm1.MAXN])
Code01_JohnsonAlgorithm1.heap = jarray('int', [Code01_JohnsonAlgorithm1.MAXN])
Code01_JohnsonAlgorithm1.where = jarray('int', [Code01_JohnsonAlgorithm1.MAXN])
Code01_JohnsonAlgorithm1.heapSize = jcast('int', 0)

if __name__ == '__main__':
    Code01_JohnsonAlgorithm1.main([])
