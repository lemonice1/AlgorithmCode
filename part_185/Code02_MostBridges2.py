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

# 最多的桥，Python版
# 给定一张无向图，一共n个点、m条边，保证所有点连通
# 沿途的边只能经过一次，找到能通过最多割边的路径，打印割边的数量
# 1 <= n、m <= 3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF1000E
# 测试链接 : https://codeforces.com/problemset/problem/1000/E
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_MostBridges2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'ebccCnt': 'ebccCnt', 'dist': 'dist', 'diameter': 'diameter'}
    MAXN = 0
    MAXM = 0
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
    ebccCnt = 0
    dist = None
    diameter = 0
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_MostBridges2.nxt, ((_java_obj_1 := Code02_MostBridges2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_MostBridges2.head[u])
        Code02_MostBridges2.to[Code02_MostBridges2.cntg] = jcast('int', v)
        Code02_MostBridges2.head[u] = jcast('int', Code02_MostBridges2.cntg)

    @staticmethod
    def tarjan(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code02_MostBridges2.dfn, u, jset(Code02_MostBridges2.low, u, ((_java_obj_4 := Code02_MostBridges2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code02_MostBridges2.sta, ((_java_obj_7 := Code02_MostBridges2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code02_MostBridges2.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code02_MostBridges2.to[e])
                if (Code02_MostBridges2.dfn[v] == 0):
                    Code02_MostBridges2.tarjan(v, e)
                    jset(Code02_MostBridges2.low, u, jstatic('Math', 'min', Code02_MostBridges2.low[u], Code02_MostBridges2.low[v]))
                else:
                    jset(Code02_MostBridges2.low, u, jstatic('Math', 'min', Code02_MostBridges2.low[u], Code02_MostBridges2.dfn[v]))
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
            e = jcast('int', Code02_MostBridges2.nxt[e])
        if (Code02_MostBridges2.dfn[u] == Code02_MostBridges2.low[u]):
            Code02_MostBridges2.ebccCnt = jcast('int', (Code02_MostBridges2.ebccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code02_MostBridges2.sta[((_java_obj_11 := Code02_MostBridges2), (_java_key_12 := 'top'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (-1)))), _java_old_13)[4]])
                Code02_MostBridges2.belong[pop] = jcast('int', Code02_MostBridges2.ebccCnt)
                if not ((pop != u)):
                    break

    @staticmethod
    def condense():
        Code02_MostBridges2.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code02_MostBridges2.ebccCnt):
            Code02_MostBridges2.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_MostBridges2.m):
            ebcc1 = jcast('int', Code02_MostBridges2.belong[Code02_MostBridges2.a[i]])
            ebcc2 = jcast('int', Code02_MostBridges2.belong[Code02_MostBridges2.b[i]])
            if (ebcc1 != ebcc2):
                Code02_MostBridges2.addEdge(ebcc1, ebcc2)
                Code02_MostBridges2.addEdge(ebcc2, ebcc1)
            i = jcast('int', (i + 1))

    @staticmethod
    def dpOnTree(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        e = jcast('int', Code02_MostBridges2.head[u])
        while (e > 0):
            v = jcast('int', Code02_MostBridges2.to[e])
            if (v != fa):
                Code02_MostBridges2.dpOnTree(v, u)
                Code02_MostBridges2.diameter = jcast('int', jstatic('Math', 'max', Code02_MostBridges2.diameter, jcast('int', jadd(jcast('int', jadd(Code02_MostBridges2.dist[u], Code02_MostBridges2.dist[v])), 1))))
                jset(Code02_MostBridges2.dist, u, jstatic('Math', 'max', Code02_MostBridges2.dist[u], jcast('int', jadd(Code02_MostBridges2.dist[v], 1))))
            e = jcast('int', Code02_MostBridges2.nxt[e])

    @staticmethod
    def main(args):
        in_ = Code02_MostBridges2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_MostBridges2.cntg = jcast('int', 1)
        Code02_MostBridges2.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_MostBridges2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_MostBridges2.m):
            jset(Code02_MostBridges2.a, i, jcall(in_, 'nextInt'))
            jset(Code02_MostBridges2.b, i, jcall(in_, 'nextInt'))
            Code02_MostBridges2.addEdge(Code02_MostBridges2.a[i], Code02_MostBridges2.b[i])
            Code02_MostBridges2.addEdge(Code02_MostBridges2.b[i], Code02_MostBridges2.a[i])
            i = jcast('int', (i + 1))
        Code02_MostBridges2.tarjan(1, 0)
        Code02_MostBridges2.condense()
        Code02_MostBridges2.dpOnTree(1, 0)
        jcall(out, 'println', Code02_MostBridges2.diameter)
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
            return jcast('int', self.buffer[((_java_obj_14 := self), (_java_key_15 := 'ptr'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))), _java_old_16)[4]])

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
            raise TypeError("No matching overload for Code02_MostBridges2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_MostBridges2.MAXN = jcast('int', 300001)
Code02_MostBridges2.MAXM = jcast('int', 300001)
Code02_MostBridges2.n = jcast('int', 0)
Code02_MostBridges2.m = jcast('int', 0)
Code02_MostBridges2.a = jarray('int', [Code02_MostBridges2.MAXM])
Code02_MostBridges2.b = jarray('int', [Code02_MostBridges2.MAXM])
Code02_MostBridges2.head = jarray('int', [Code02_MostBridges2.MAXN])
Code02_MostBridges2.nxt = jarray('int', [jcast('int', (Code02_MostBridges2.MAXM << (1 & 31)))])
Code02_MostBridges2.to = jarray('int', [jcast('int', (Code02_MostBridges2.MAXM << (1 & 31)))])
Code02_MostBridges2.cntg = jcast('int', 0)
Code02_MostBridges2.dfn = jarray('int', [Code02_MostBridges2.MAXN])
Code02_MostBridges2.low = jarray('int', [Code02_MostBridges2.MAXN])
Code02_MostBridges2.cntd = jcast('int', 0)
Code02_MostBridges2.sta = jarray('int', [Code02_MostBridges2.MAXN])
Code02_MostBridges2.top = jcast('int', 0)
Code02_MostBridges2.belong = jarray('int', [Code02_MostBridges2.MAXN])
Code02_MostBridges2.ebccCnt = jcast('int', 0)
Code02_MostBridges2.dist = jarray('int', [Code02_MostBridges2.MAXN])
Code02_MostBridges2.diameter = jcast('int', 0)

if __name__ == '__main__':
    Code02_MostBridges2.main([])
