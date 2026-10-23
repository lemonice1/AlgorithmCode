# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 仙人掌直径，Python版
# 给定n个点、m条路径表示无向图，每条路径的相邻两点之间都有边
# 点x到点y的距离，是指x到y的最短路径中的边数
# 仙人掌直径，是指任意两点距离的最大值
# 输入保证图是仙人掌，计算仙人掌直径
# 1 <= n <= 5 * 10^4
# 1 <= 边总数 <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P4244
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_CactusDiameter2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'dist': 'dist', 'arr': 'arr', 'que': 'que', 'diameter': 'diameter', 'stau': 'stau', 'stap': 'stap', 'stas': 'stas', 'stae': 'stae', 'u': 'u', 'preEdge': 'preEdge', 'status': 'status', 'e': 'e', 'stacksiz': 'stacksiz'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    # dist[u] : 以u为头的子仙人掌中，u到任意点的最短路距离的最大值
    dist = None
    # 收集环中每个点的dist，然后复制一份
    arr = None
    # 单调队列
    que = None
    # 答案
    diameter = 0
    # 递归改迭代需要的栈
    stau = None
    stap = None
    stas = None
    stae = None
    u = 0
    preEdge = 0
    status = 0
    e = 0
    stacksiz = 0
    @staticmethod
    def push(u, preEdge, status, e):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        status = jcast('int', status)
        e = jcast('int', e)
        Code05_CactusDiameter2.stau[Code05_CactusDiameter2.stacksiz] = jcast('int', u)
        Code05_CactusDiameter2.stap[Code05_CactusDiameter2.stacksiz] = jcast('int', preEdge)
        Code05_CactusDiameter2.stas[Code05_CactusDiameter2.stacksiz] = jcast('int', status)
        Code05_CactusDiameter2.stae[Code05_CactusDiameter2.stacksiz] = jcast('int', e)
        Code05_CactusDiameter2.stacksiz = jcast('int', (Code05_CactusDiameter2.stacksiz + 1))

    @staticmethod
    def pop():
        Code05_CactusDiameter2.stacksiz = jcast('int', (Code05_CactusDiameter2.stacksiz - 1))
        Code05_CactusDiameter2.u = jcast('int', Code05_CactusDiameter2.stau[Code05_CactusDiameter2.stacksiz])
        Code05_CactusDiameter2.preEdge = jcast('int', Code05_CactusDiameter2.stap[Code05_CactusDiameter2.stacksiz])
        Code05_CactusDiameter2.status = jcast('int', Code05_CactusDiameter2.stas[Code05_CactusDiameter2.stacksiz])
        Code05_CactusDiameter2.e = jcast('int', Code05_CactusDiameter2.stae[Code05_CactusDiameter2.stacksiz])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_CactusDiameter2.nxt, ((_java_obj_1 := Code05_CactusDiameter2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_CactusDiameter2.head[u])
        Code05_CactusDiameter2.to[Code05_CactusDiameter2.cntg] = jcast('int', v)
        Code05_CactusDiameter2.head[u] = jcast('int', Code05_CactusDiameter2.cntg)

    @staticmethod
    def dpOnCycle(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        siz = jcast('int', 0)
        jset(Code05_CactusDiameter2.arr, (siz := jcast('int', (siz + (1)))), Code05_CactusDiameter2.dist[u])
        pop = 0
        while True:
            pop = jcast('int', Code05_CactusDiameter2.sta[((_java_obj_4 := Code05_CactusDiameter2), (_java_key_5 := 'top'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))), _java_old_6)[4]])
            jset(Code05_CactusDiameter2.arr, (siz := jcast('int', (siz + (1)))), Code05_CactusDiameter2.dist[pop])
            if not ((pop != v)):
                break
        i = jcast('int', 1)
        while (i <= siz):
            Code05_CactusDiameter2.arr[jcast('int', jadd(i, siz))] = jcast('int', Code05_CactusDiameter2.arr[i])
            i = jcast('int', (i + 1))
        l = jcast('int', 1)
        r = jcast('int', 0)
        jset(Code05_CactusDiameter2.que, (r := jcast('int', (r + (1)))), 1)
        i = jcast('int', 2)
        while (i <= jcast('int', (siz << (1 & 31)))):
            while ((l <= r) and (jcast('int', (jcast('int', (i - Code05_CactusDiameter2.que[l])) * 2)) > siz)):
                l = jcast('int', (l + 1))
            Code05_CactusDiameter2.diameter = jcast('int', jstatic('Math', 'max', Code05_CactusDiameter2.diameter, jcast('int', (jcast('int', jadd(jcast('int', jadd(Code05_CactusDiameter2.arr[i], i)), Code05_CactusDiameter2.arr[Code05_CactusDiameter2.que[l]])) - Code05_CactusDiameter2.que[l]))))
            while ((l <= r) and (jcast('int', (Code05_CactusDiameter2.arr[Code05_CactusDiameter2.que[r]] - Code05_CactusDiameter2.que[r])) <= jcast('int', (Code05_CactusDiameter2.arr[i] - i)))):
                r = jcast('int', (r - 1))
            jset(Code05_CactusDiameter2.que, (r := jcast('int', (r + (1)))), i)
            i = jcast('int', (i + 1))
        i = jcast('int', 2)
        while (i <= siz):
            jset(Code05_CactusDiameter2.dist, u, jstatic('Math', 'max', Code05_CactusDiameter2.dist[u], jcast('int', jadd(Code05_CactusDiameter2.arr[i], jstatic('Math', 'min', jcast('int', (i - 1)), jcast('int', (siz - jcast('int', (i - 1)))))))))
            i = jcast('int', (i + 1))

    # 递归版
    @staticmethod
    def tarjan1(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code05_CactusDiameter2.dfn, u, jset(Code05_CactusDiameter2.low, u, ((_java_obj_7 := Code05_CactusDiameter2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
        jset(Code05_CactusDiameter2.sta, ((_java_obj_10 := Code05_CactusDiameter2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
        e = jcast('int', Code05_CactusDiameter2.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code05_CactusDiameter2.to[e])
                if (Code05_CactusDiameter2.dfn[v] == 0):
                    Code05_CactusDiameter2.tarjan1(v, e)
                    if (Code05_CactusDiameter2.low[v] < Code05_CactusDiameter2.dfn[u]):
                        jset(Code05_CactusDiameter2.low, u, jstatic('Math', 'min', Code05_CactusDiameter2.low[u], Code05_CactusDiameter2.low[v]))
                    else:
                        if (Code05_CactusDiameter2.low[v] > Code05_CactusDiameter2.dfn[u]):
                            Code05_CactusDiameter2.top = jcast('int', (Code05_CactusDiameter2.top - 1))
                            Code05_CactusDiameter2.diameter = jcast('int', jstatic('Math', 'max', Code05_CactusDiameter2.diameter, jcast('int', jadd(jcast('int', jadd(Code05_CactusDiameter2.dist[u], Code05_CactusDiameter2.dist[v])), 1))))
                            jset(Code05_CactusDiameter2.dist, u, jstatic('Math', 'max', Code05_CactusDiameter2.dist[u], jcast('int', jadd(Code05_CactusDiameter2.dist[v], 1))))
                        else:
                            Code05_CactusDiameter2.dpOnCycle(u, v)
                else:
                    if (Code05_CactusDiameter2.dfn[v] < Code05_CactusDiameter2.dfn[u]):
                        jset(Code05_CactusDiameter2.low, u, jstatic('Math', 'min', Code05_CactusDiameter2.low[u], Code05_CactusDiameter2.dfn[v]))
            except JContinue as _java_control_13:
                if _java_control_13.label not in (None,):
                    raise
            except JBreak as _java_control_13:
                if _java_control_13.label not in (None,):
                    raise
                break
            e = jcast('int', Code05_CactusDiameter2.nxt[e])

    # 迭代版
    @staticmethod
    def tarjan2(node, pree):
        node = jcast('int', node)
        pree = jcast('int', pree)
        Code05_CactusDiameter2.stacksiz = jcast('int', 0)
        Code05_CactusDiameter2.push(node, pree, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code05_CactusDiameter2.stacksiz > 0):
            Code05_CactusDiameter2.pop()
            if (Code05_CactusDiameter2.status == jcast('int', (-1))):
                jset(Code05_CactusDiameter2.dfn, Code05_CactusDiameter2.u, jset(Code05_CactusDiameter2.low, Code05_CactusDiameter2.u, ((_java_obj_14 := Code05_CactusDiameter2), (_java_key_15 := 'cntd'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))))[3]))
                jset(Code05_CactusDiameter2.sta, ((_java_obj_17 := Code05_CactusDiameter2), (_java_key_18 := 'top'), (_java_old_19 := jget(_java_obj_17, _java_key_18)), jset(_java_obj_17, _java_key_18, jcast('int', (_java_old_19 + (1)))))[3], Code05_CactusDiameter2.u)
                Code05_CactusDiameter2.e = jcast('int', Code05_CactusDiameter2.head[Code05_CactusDiameter2.u])
            else:
                v = jcast('int', Code05_CactusDiameter2.to[Code05_CactusDiameter2.e])
                if (Code05_CactusDiameter2.status == 0):
                    if (Code05_CactusDiameter2.low[v] < Code05_CactusDiameter2.dfn[Code05_CactusDiameter2.u]):
                        jset(Code05_CactusDiameter2.low, Code05_CactusDiameter2.u, jstatic('Math', 'min', Code05_CactusDiameter2.low[Code05_CactusDiameter2.u], Code05_CactusDiameter2.low[v]))
                    else:
                        if (Code05_CactusDiameter2.low[v] > Code05_CactusDiameter2.dfn[Code05_CactusDiameter2.u]):
                            Code05_CactusDiameter2.top = jcast('int', (Code05_CactusDiameter2.top - 1))
                            Code05_CactusDiameter2.diameter = jcast('int', jstatic('Math', 'max', Code05_CactusDiameter2.diameter, jcast('int', jadd(jcast('int', jadd(Code05_CactusDiameter2.dist[Code05_CactusDiameter2.u], Code05_CactusDiameter2.dist[v])), 1))))
                            jset(Code05_CactusDiameter2.dist, Code05_CactusDiameter2.u, jstatic('Math', 'max', Code05_CactusDiameter2.dist[Code05_CactusDiameter2.u], jcast('int', jadd(Code05_CactusDiameter2.dist[v], 1))))
                        else:
                            Code05_CactusDiameter2.dpOnCycle(Code05_CactusDiameter2.u, v)
                else:
                    if (Code05_CactusDiameter2.dfn[v] < Code05_CactusDiameter2.dfn[Code05_CactusDiameter2.u]):
                        jset(Code05_CactusDiameter2.low, Code05_CactusDiameter2.u, jstatic('Math', 'min', Code05_CactusDiameter2.low[Code05_CactusDiameter2.u], Code05_CactusDiameter2.dfn[v]))
                Code05_CactusDiameter2.e = jcast('int', Code05_CactusDiameter2.nxt[Code05_CactusDiameter2.e])
            if (jcast('int', (Code05_CactusDiameter2.e ^ 1)) == Code05_CactusDiameter2.preEdge):
                Code05_CactusDiameter2.e = jcast('int', Code05_CactusDiameter2.nxt[Code05_CactusDiameter2.e])
            if (Code05_CactusDiameter2.e != 0):
                v = jcast('int', Code05_CactusDiameter2.to[Code05_CactusDiameter2.e])
                if (Code05_CactusDiameter2.dfn[v] == 0):
                    Code05_CactusDiameter2.push(Code05_CactusDiameter2.u, Code05_CactusDiameter2.preEdge, 0, Code05_CactusDiameter2.e)
                    Code05_CactusDiameter2.push(v, Code05_CactusDiameter2.e, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code05_CactusDiameter2.push(Code05_CactusDiameter2.u, Code05_CactusDiameter2.preEdge, 1, Code05_CactusDiameter2.e)

    @staticmethod
    def main(args):
        in_ = Code05_CactusDiameter2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_CactusDiameter2.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_CactusDiameter2.m = jcast('int', jcall(in_, 'nextInt'))
        Code05_CactusDiameter2.cntg = jcast('int', 1)
        i = jcast('int', 1)
        k = 0
        x = 0
        y = 0
        while (i <= Code05_CactusDiameter2.m):
            k = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            j = jcast('int', 2)
            while (j <= k):
                y = jcast('int', jcall(in_, 'nextInt'))
                Code05_CactusDiameter2.addEdge(x, y)
                Code05_CactusDiameter2.addEdge(y, x)
                x = jcast('int', y)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        # tarjan1(1, 0);
        Code05_CactusDiameter2.tarjan2(1, 0)
        jcall(out, 'println', Code05_CactusDiameter2.diameter)
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
            return jcast('int', self.buffer[((_java_obj_20 := self), (_java_key_21 := 'ptr'), (_java_old_22 := jget(_java_obj_20, _java_key_21)), jset(_java_obj_20, _java_key_21, jcast('int', (_java_old_22 + (1)))), _java_old_22)[4]])

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
            raise TypeError("No matching overload for Code05_CactusDiameter2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_CactusDiameter2.MAXN = jcast('int', 50001)
Code05_CactusDiameter2.MAXM = jcast('int', 1000001)
Code05_CactusDiameter2.n = jcast('int', 0)
Code05_CactusDiameter2.m = jcast('int', 0)
Code05_CactusDiameter2.head = jarray('int', [Code05_CactusDiameter2.MAXN])
Code05_CactusDiameter2.nxt = jarray('int', [jcast('int', (Code05_CactusDiameter2.MAXM << (1 & 31)))])
Code05_CactusDiameter2.to = jarray('int', [jcast('int', (Code05_CactusDiameter2.MAXM << (1 & 31)))])
Code05_CactusDiameter2.cntg = jcast('int', 0)
Code05_CactusDiameter2.dfn = jarray('int', [Code05_CactusDiameter2.MAXN])
Code05_CactusDiameter2.low = jarray('int', [Code05_CactusDiameter2.MAXN])
Code05_CactusDiameter2.cntd = jcast('int', 0)
Code05_CactusDiameter2.sta = jarray('int', [Code05_CactusDiameter2.MAXN])
Code05_CactusDiameter2.top = jcast('int', 0)
Code05_CactusDiameter2.dist = jarray('int', [Code05_CactusDiameter2.MAXN])
Code05_CactusDiameter2.arr = jarray('int', [jcast('int', (Code05_CactusDiameter2.MAXN << (1 & 31)))])
Code05_CactusDiameter2.que = jarray('int', [jcast('int', (Code05_CactusDiameter2.MAXN << (1 & 31)))])
Code05_CactusDiameter2.diameter = jcast('int', 0)
Code05_CactusDiameter2.stau = jarray('int', [Code05_CactusDiameter2.MAXN])
Code05_CactusDiameter2.stap = jarray('int', [Code05_CactusDiameter2.MAXN])
Code05_CactusDiameter2.stas = jarray('int', [Code05_CactusDiameter2.MAXN])
Code05_CactusDiameter2.stae = jarray('int', [Code05_CactusDiameter2.MAXN])
Code05_CactusDiameter2.u = jcast('int', 0)
Code05_CactusDiameter2.preEdge = jcast('int', 0)
Code05_CactusDiameter2.status = jcast('int', 0)
Code05_CactusDiameter2.e = jcast('int', 0)
Code05_CactusDiameter2.stacksiz = jcast('int', 0)

if __name__ == '__main__':
    Code05_CactusDiameter2.main([])
