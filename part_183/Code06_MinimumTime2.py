# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 缩点最短路，Python版
# 给定一张n个点，m条边的有向图，每条边有非负边权
# 如果两点属同一个强连通分量，认为彼此到达的代价为0
# 找到从1号点到n号点的路径，打印最小的边权累加和，如果不能到达打印-1
# 1 <= n <= 2 * 10^5
# 1 <= m <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P2169
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_MinimumTime2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'INF': 'INF', 'n': 'n', 'm': 'm', 'a': 'a', 'b': 'b', 'val': 'val', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'dist': 'dist', 'vis': 'vis', 'heap': 'heap', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    INF = 0
    n = 0
    m = 0
    a = None
    b = None
    val = None
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    belong = None
    sccCnt = 0
    dist = None
    vis = None
    heap = None
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stack = None
    u = 0
    status = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, status, e):
        u = jcast('int', u)
        status = jcast('int', status)
        e = jcast('int', e)
        jset(Code06_MinimumTime2.stack[Code06_MinimumTime2.stacksize], 0, u)
        jset(Code06_MinimumTime2.stack[Code06_MinimumTime2.stacksize], 1, status)
        jset(Code06_MinimumTime2.stack[Code06_MinimumTime2.stacksize], 2, e)
        Code06_MinimumTime2.stacksize = jcast('int', (Code06_MinimumTime2.stacksize + 1))

    @staticmethod
    def pop():
        Code06_MinimumTime2.stacksize = jcast('int', (Code06_MinimumTime2.stacksize - 1))
        Code06_MinimumTime2.u = jcast('int', Code06_MinimumTime2.stack[Code06_MinimumTime2.stacksize][0])
        Code06_MinimumTime2.status = jcast('int', Code06_MinimumTime2.stack[Code06_MinimumTime2.stacksize][1])
        Code06_MinimumTime2.e = jcast('int', Code06_MinimumTime2.stack[Code06_MinimumTime2.stacksize][2])

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code06_MinimumTime2.nxt, ((_java_obj_1 := Code06_MinimumTime2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_MinimumTime2.head[u])
        Code06_MinimumTime2.to[Code06_MinimumTime2.cntg] = jcast('int', v)
        Code06_MinimumTime2.weight[Code06_MinimumTime2.cntg] = jcast('int', w)
        Code06_MinimumTime2.head[u] = jcast('int', Code06_MinimumTime2.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code06_MinimumTime2.dfn, u, jset(Code06_MinimumTime2.low, u, ((_java_obj_4 := Code06_MinimumTime2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code06_MinimumTime2.sta, ((_java_obj_7 := Code06_MinimumTime2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code06_MinimumTime2.head[u])
        while (e > 0):
            v = jcast('int', Code06_MinimumTime2.to[e])
            if (Code06_MinimumTime2.dfn[v] == 0):
                Code06_MinimumTime2.tarjan1(v)
                jset(Code06_MinimumTime2.low, u, jstatic('Math', 'min', Code06_MinimumTime2.low[u], Code06_MinimumTime2.low[v]))
            else:
                if (Code06_MinimumTime2.belong[v] == 0):
                    jset(Code06_MinimumTime2.low, u, jstatic('Math', 'min', Code06_MinimumTime2.low[u], Code06_MinimumTime2.dfn[v]))
            e = jcast('int', Code06_MinimumTime2.nxt[e])
        if (Code06_MinimumTime2.dfn[u] == Code06_MinimumTime2.low[u]):
            Code06_MinimumTime2.sccCnt = jcast('int', (Code06_MinimumTime2.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code06_MinimumTime2.sta[((_java_obj_10 := Code06_MinimumTime2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code06_MinimumTime2.belong[pop] = jcast('int', Code06_MinimumTime2.sccCnt)
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code06_MinimumTime2.stacksize = jcast('int', 0)
        Code06_MinimumTime2.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code06_MinimumTime2.stacksize > 0):
            Code06_MinimumTime2.pop()
            if (Code06_MinimumTime2.status == jcast('int', (-1))):
                jset(Code06_MinimumTime2.dfn, Code06_MinimumTime2.u, jset(Code06_MinimumTime2.low, Code06_MinimumTime2.u, ((_java_obj_13 := Code06_MinimumTime2), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code06_MinimumTime2.sta, ((_java_obj_16 := Code06_MinimumTime2), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code06_MinimumTime2.u)
                Code06_MinimumTime2.e = jcast('int', Code06_MinimumTime2.head[Code06_MinimumTime2.u])
            else:
                v = jcast('int', Code06_MinimumTime2.to[Code06_MinimumTime2.e])
                if (Code06_MinimumTime2.status == 0):
                    jset(Code06_MinimumTime2.low, Code06_MinimumTime2.u, jstatic('Math', 'min', Code06_MinimumTime2.low[Code06_MinimumTime2.u], Code06_MinimumTime2.low[v]))
                if ((Code06_MinimumTime2.status == 1) and (Code06_MinimumTime2.belong[v] == 0)):
                    jset(Code06_MinimumTime2.low, Code06_MinimumTime2.u, jstatic('Math', 'min', Code06_MinimumTime2.low[Code06_MinimumTime2.u], Code06_MinimumTime2.dfn[v]))
                Code06_MinimumTime2.e = jcast('int', Code06_MinimumTime2.nxt[Code06_MinimumTime2.e])
            if (Code06_MinimumTime2.e != 0):
                v = jcast('int', Code06_MinimumTime2.to[Code06_MinimumTime2.e])
                if (Code06_MinimumTime2.dfn[v] == 0):
                    Code06_MinimumTime2.push(Code06_MinimumTime2.u, 0, Code06_MinimumTime2.e)
                    Code06_MinimumTime2.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code06_MinimumTime2.push(Code06_MinimumTime2.u, 1, Code06_MinimumTime2.e)
            else:
                if (Code06_MinimumTime2.dfn[Code06_MinimumTime2.u] == Code06_MinimumTime2.low[Code06_MinimumTime2.u]):
                    Code06_MinimumTime2.sccCnt = jcast('int', (Code06_MinimumTime2.sccCnt + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code06_MinimumTime2.sta[((_java_obj_19 := Code06_MinimumTime2), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                        Code06_MinimumTime2.belong[pop] = jcast('int', Code06_MinimumTime2.sccCnt)
                        if not ((pop != Code06_MinimumTime2.u)):
                            break

    @staticmethod
    def condense():
        Code06_MinimumTime2.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code06_MinimumTime2.sccCnt):
            Code06_MinimumTime2.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_MinimumTime2.m):
            scc1 = jcast('int', Code06_MinimumTime2.belong[Code06_MinimumTime2.a[i]])
            scc2 = jcast('int', Code06_MinimumTime2.belong[Code06_MinimumTime2.b[i]])
            if (((scc1 > 0) and (scc2 > 0)) and (scc1 != scc2)):
                Code06_MinimumTime2.addEdge(scc1, scc2, Code06_MinimumTime2.val[i])
            i = jcast('int', (i + 1))

    @staticmethod
    def dijkstra():
        i = jcast('int', 1)
        while (i <= Code06_MinimumTime2.sccCnt):
            Code06_MinimumTime2.dist[i] = jcast('int', Code06_MinimumTime2.INF)
            Code06_MinimumTime2.vis[i] = jcast('boolean', False)
            i = jcast('int', (i + 1))
        jset(Code06_MinimumTime2.dist, Code06_MinimumTime2.belong[1], 0)
        jcall(Code06_MinimumTime2.heap, 'add', jarray('int', [None], [Code06_MinimumTime2.belong[1], 0]))
        while (not jcall(Code06_MinimumTime2.heap, 'isEmpty')):
            cur = jcall(Code06_MinimumTime2.heap, 'poll')
            u = jcast('int', cur[0])
            d = jcast('int', cur[1])
            if (not Code06_MinimumTime2.vis[u]):
                Code06_MinimumTime2.vis[u] = jcast('boolean', True)
                e = jcast('int', Code06_MinimumTime2.head[u])
                while (e > 0):
                    v = jcast('int', Code06_MinimumTime2.to[e])
                    w = jcast('int', Code06_MinimumTime2.weight[e])
                    if ((not Code06_MinimumTime2.vis[v]) and (Code06_MinimumTime2.dist[v] > jcast('int', jadd(d, w)))):
                        Code06_MinimumTime2.dist[v] = jcast('int', jcast('int', jadd(d, w)))
                        jcall(Code06_MinimumTime2.heap, 'add', jarray('int', [None], [v, Code06_MinimumTime2.dist[v]]))
                    e = jcast('int', Code06_MinimumTime2.nxt[e])
        return jcast('int', Code06_MinimumTime2.dist[Code06_MinimumTime2.belong[Code06_MinimumTime2.n]])

    @staticmethod
    def main(args):
        in_ = Code06_MinimumTime2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_MinimumTime2.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_MinimumTime2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_MinimumTime2.m):
            jset(Code06_MinimumTime2.a, i, jcall(in_, 'nextInt'))
            jset(Code06_MinimumTime2.b, i, jcall(in_, 'nextInt'))
            jset(Code06_MinimumTime2.val, i, jcall(in_, 'nextInt'))
            Code06_MinimumTime2.addEdge(Code06_MinimumTime2.a[i], Code06_MinimumTime2.b[i], Code06_MinimumTime2.val[i])
            i = jcast('int', (i + 1))
        # tarjan1(1);
        Code06_MinimumTime2.tarjan2(1)
        if (Code06_MinimumTime2.belong[Code06_MinimumTime2.n] == 0):
            jcall(out, 'println', jcast('int', (-1)))
        else:
            Code06_MinimumTime2.condense()
            ans = jcast('int', Code06_MinimumTime2.dijkstra())
            jcall(out, 'println', ans)
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
            return jcast('int', self.buffer[((_java_obj_22 := self), (_java_key_23 := 'ptr'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))), _java_old_24)[4]])

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
            raise TypeError("No matching overload for Code06_MinimumTime2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_MinimumTime2.MAXN = jcast('int', 200001)
Code06_MinimumTime2.MAXM = jcast('int', 1000001)
Code06_MinimumTime2.INF = jcast('int', 1000000001)
Code06_MinimumTime2.n = jcast('int', 0)
Code06_MinimumTime2.m = jcast('int', 0)
Code06_MinimumTime2.a = jarray('int', [Code06_MinimumTime2.MAXM])
Code06_MinimumTime2.b = jarray('int', [Code06_MinimumTime2.MAXM])
Code06_MinimumTime2.val = jarray('int', [Code06_MinimumTime2.MAXM])
Code06_MinimumTime2.head = jarray('int', [Code06_MinimumTime2.MAXN])
Code06_MinimumTime2.nxt = jarray('int', [Code06_MinimumTime2.MAXM])
Code06_MinimumTime2.to = jarray('int', [Code06_MinimumTime2.MAXM])
Code06_MinimumTime2.weight = jarray('int', [Code06_MinimumTime2.MAXM])
Code06_MinimumTime2.cntg = jcast('int', 0)
Code06_MinimumTime2.dfn = jarray('int', [Code06_MinimumTime2.MAXN])
Code06_MinimumTime2.low = jarray('int', [Code06_MinimumTime2.MAXN])
Code06_MinimumTime2.cntd = jcast('int', 0)
Code06_MinimumTime2.sta = jarray('int', [Code06_MinimumTime2.MAXN])
Code06_MinimumTime2.top = jcast('int', 0)
Code06_MinimumTime2.belong = jarray('int', [Code06_MinimumTime2.MAXN])
Code06_MinimumTime2.sccCnt = jcast('int', 0)
Code06_MinimumTime2.dist = jarray('int', [Code06_MinimumTime2.MAXN])
Code06_MinimumTime2.vis = jarray('boolean', [Code06_MinimumTime2.MAXN])
Code06_MinimumTime2.heap = jnew('PriorityQueue', (lambda x, y: (x[1] - y[1])))
Code06_MinimumTime2.stack = jarray('int', [Code06_MinimumTime2.MAXN, 3])
Code06_MinimumTime2.u = jcast('int', 0)
Code06_MinimumTime2.status = jcast('int', 0)
Code06_MinimumTime2.e = jcast('int', 0)
Code06_MinimumTime2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code06_MinimumTime2.main([])
