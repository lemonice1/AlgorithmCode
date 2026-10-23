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

# 任意两点都有路，Python版
# 给定一张n个点，m条边的有向图
# 两点u、v，不管是从u出发能到达v，还是从v出发能到达u，都叫两点间有路
# 判断这个有向图是否能做到，任意两点都有路，能打印"Yes"，不能打印"No"
# 1 <= n <= 1000
# 1 <= m <= 6000
# 测试链接 : https://www.luogu.com.cn/problem/P10944
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code09_HasPath1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 't': 't', 'n': 'n', 'm': 'm', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'indegree': 'indegree', 'que': 'que'}
    MAXN = 0
    MAXM = 0
    t = 0
    n = 0
    m = 0
    a = None
    b = None
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    belong = None
    sccCnt = 0
    indegree = None
    que = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code09_HasPath1.nxt, ((_java_obj_1 := Code09_HasPath1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code09_HasPath1.head[u])
        Code09_HasPath1.to[Code09_HasPath1.cntg] = jcast('int', v)
        Code09_HasPath1.head[u] = jcast('int', Code09_HasPath1.cntg)

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code09_HasPath1.dfn, u, jset(Code09_HasPath1.low, u, ((_java_obj_4 := Code09_HasPath1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code09_HasPath1.sta, ((_java_obj_7 := Code09_HasPath1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code09_HasPath1.head[u])
        while (e > 0):
            v = jcast('int', Code09_HasPath1.to[e])
            if (Code09_HasPath1.dfn[v] == 0):
                Code09_HasPath1.tarjan(v)
                jset(Code09_HasPath1.low, u, jstatic('Math', 'min', Code09_HasPath1.low[u], Code09_HasPath1.low[v]))
            else:
                if (Code09_HasPath1.belong[v] == 0):
                    jset(Code09_HasPath1.low, u, jstatic('Math', 'min', Code09_HasPath1.low[u], Code09_HasPath1.dfn[v]))
            e = jcast('int', Code09_HasPath1.nxt[e])
        if (Code09_HasPath1.dfn[u] == Code09_HasPath1.low[u]):
            Code09_HasPath1.sccCnt = jcast('int', (Code09_HasPath1.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code09_HasPath1.sta[((_java_obj_10 := Code09_HasPath1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code09_HasPath1.belong[pop] = jcast('int', Code09_HasPath1.sccCnt)
                if not ((pop != u)):
                    break

    @staticmethod
    def condense():
        Code09_HasPath1.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code09_HasPath1.sccCnt):
            Code09_HasPath1.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code09_HasPath1.m):
            scc1 = jcast('int', Code09_HasPath1.belong[Code09_HasPath1.a[i]])
            scc2 = jcast('int', Code09_HasPath1.belong[Code09_HasPath1.b[i]])
            if (scc1 != scc2):
                Code09_HasPath1.indegree[scc2] = jcast('int', (Code09_HasPath1.indegree[scc2] + 1))
                Code09_HasPath1.addEdge(scc1, scc2)
            i = jcast('int', (i + 1))

    @staticmethod
    def topo():
        l = jcast('int', 1)
        r = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code09_HasPath1.sccCnt):
            if (Code09_HasPath1.indegree[i] == 0):
                jset(Code09_HasPath1.que, (r := jcast('int', (r + (1)))), i)
            i = jcast('int', (i + 1))
        while (l <= r):
            siz = jcast('int', jcast('int', jadd(jcast('int', (r - l)), 1)))
            if (siz > 1):
                return jcast('boolean', False)
            u = jcast('int', Code09_HasPath1.que[((_java_old_13 := l), (l := jcast('int', (l + (1)))), _java_old_13)[2]])
            e = jcast('int', Code09_HasPath1.head[u])
            while (e > 0):
                v = jcast('int', Code09_HasPath1.to[e])
                if (((_java_obj_14 := Code09_HasPath1.indegree), (_java_key_15 := v), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (-1)))))[3] == 0):
                    jset(Code09_HasPath1.que, (r := jcast('int', (r + (1)))), v)
                e = jcast('int', Code09_HasPath1.nxt[e])
        return jcast('boolean', True)

    @staticmethod
    def main(args):
        in_ = Code09_HasPath1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code09_HasPath1.t = jcast('int', jcall(in_, 'nextInt'))
        c = jcast('int', 1)
        while (c <= Code09_HasPath1.t):
            Code09_HasPath1.n = jcast('int', jcall(in_, 'nextInt'))
            Code09_HasPath1.m = jcast('int', jcall(in_, 'nextInt'))
            Code09_HasPath1.cntg = jcast('int', jset(Code09_HasPath1, 'cntd', jset(Code09_HasPath1, 'sccCnt', 0)))
            i = jcast('int', 1)
            while (i <= Code09_HasPath1.n):
                jset(Code09_HasPath1.head, i, jset(Code09_HasPath1.dfn, i, jset(Code09_HasPath1.belong, i, jset(Code09_HasPath1.indegree, i, 0))))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code09_HasPath1.m):
                jset(Code09_HasPath1.a, i, jcall(in_, 'nextInt'))
                jset(Code09_HasPath1.b, i, jcall(in_, 'nextInt'))
                Code09_HasPath1.addEdge(Code09_HasPath1.a[i], Code09_HasPath1.b[i])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code09_HasPath1.n):
                if (Code09_HasPath1.dfn[i] == 0):
                    Code09_HasPath1.tarjan(i)
                i = jcast('int', (i + 1))
            Code09_HasPath1.condense()
            ans = jcast('boolean', Code09_HasPath1.topo())
            jcall(out, 'println', ('Yes' if ans else 'No'))
            c = jcast('int', (c + 1))
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
            return jcast('int', self.buffer[((_java_obj_17 := self), (_java_key_18 := 'ptr'), (_java_old_19 := jget(_java_obj_17, _java_key_18)), jset(_java_obj_17, _java_key_18, jcast('int', (_java_old_19 + (1)))), _java_old_19)[4]])

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
            raise TypeError("No matching overload for Code09_HasPath1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code09_HasPath1.MAXN = jcast('int', 1001)
Code09_HasPath1.MAXM = jcast('int', 6001)
Code09_HasPath1.t = jcast('int', 0)
Code09_HasPath1.n = jcast('int', 0)
Code09_HasPath1.m = jcast('int', 0)
Code09_HasPath1.a = jarray('int', [Code09_HasPath1.MAXM])
Code09_HasPath1.b = jarray('int', [Code09_HasPath1.MAXM])
Code09_HasPath1.head = jarray('int', [Code09_HasPath1.MAXN])
Code09_HasPath1.nxt = jarray('int', [Code09_HasPath1.MAXM])
Code09_HasPath1.to = jarray('int', [Code09_HasPath1.MAXM])
Code09_HasPath1.cntg = jcast('int', 0)
Code09_HasPath1.dfn = jarray('int', [Code09_HasPath1.MAXN])
Code09_HasPath1.low = jarray('int', [Code09_HasPath1.MAXN])
Code09_HasPath1.cntd = jcast('int', 0)
Code09_HasPath1.sta = jarray('int', [Code09_HasPath1.MAXN])
Code09_HasPath1.top = jcast('int', 0)
Code09_HasPath1.belong = jarray('int', [Code09_HasPath1.MAXN])
Code09_HasPath1.sccCnt = jcast('int', 0)
Code09_HasPath1.indegree = jarray('int', [Code09_HasPath1.MAXN])
Code09_HasPath1.que = jarray('int', [Code09_HasPath1.MAXN])

if __name__ == '__main__':
    Code09_HasPath1.main([])
