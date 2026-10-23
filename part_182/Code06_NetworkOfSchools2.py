# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 校园网络，Python版
# 一共有n个节点，m条有向边，消息只能顺着有向边传递
# 打印至少需要在几个节点投放消息，才能让所有节点，都能收到消息
# 打印至少需要添加几条边，才能让任意两个节点之间，都能传递消息
# 1 <= n <= 10^4
# 1 <= m <= 5 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P2812
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_NetworkOfSchools2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'outdegree': 'outdegree', 'indegree': 'indegree'}
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
    sccCnt = 0
    outdegree = None
    indegree = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code06_NetworkOfSchools2.nxt, ((_java_obj_1 := Code06_NetworkOfSchools2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_NetworkOfSchools2.head[u])
        Code06_NetworkOfSchools2.to[Code06_NetworkOfSchools2.cntg] = jcast('int', v)
        Code06_NetworkOfSchools2.head[u] = jcast('int', Code06_NetworkOfSchools2.cntg)

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code06_NetworkOfSchools2.dfn, u, jset(Code06_NetworkOfSchools2.low, u, ((_java_obj_4 := Code06_NetworkOfSchools2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code06_NetworkOfSchools2.sta, ((_java_obj_7 := Code06_NetworkOfSchools2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code06_NetworkOfSchools2.head[u])
        while (e > 0):
            v = jcast('int', Code06_NetworkOfSchools2.to[e])
            if (Code06_NetworkOfSchools2.dfn[v] == 0):
                Code06_NetworkOfSchools2.tarjan(v)
                jset(Code06_NetworkOfSchools2.low, u, jstatic('Math', 'min', Code06_NetworkOfSchools2.low[u], Code06_NetworkOfSchools2.low[v]))
            else:
                if (Code06_NetworkOfSchools2.belong[v] == 0):
                    jset(Code06_NetworkOfSchools2.low, u, jstatic('Math', 'min', Code06_NetworkOfSchools2.low[u], Code06_NetworkOfSchools2.dfn[v]))
            e = jcast('int', Code06_NetworkOfSchools2.nxt[e])
        if (Code06_NetworkOfSchools2.dfn[u] == Code06_NetworkOfSchools2.low[u]):
            Code06_NetworkOfSchools2.sccCnt = jcast('int', (Code06_NetworkOfSchools2.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code06_NetworkOfSchools2.sta[((_java_obj_10 := Code06_NetworkOfSchools2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code06_NetworkOfSchools2.belong[pop] = jcast('int', Code06_NetworkOfSchools2.sccCnt)
                if not ((pop != u)):
                    break

    @staticmethod
    def main(args):
        in_ = Code06_NetworkOfSchools2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_NetworkOfSchools2.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_NetworkOfSchools2.m = jcast('int', 0)
        i = jcast('int', 1)
        x = 0
        while (i <= Code06_NetworkOfSchools2.n):
            x = jcast('int', jcall(in_, 'nextInt'))
            while (x != 0):
                Code06_NetworkOfSchools2.m = jcast('int', (Code06_NetworkOfSchools2.m + 1))
                Code06_NetworkOfSchools2.a[Code06_NetworkOfSchools2.m] = jcast('int', i)
                Code06_NetworkOfSchools2.b[Code06_NetworkOfSchools2.m] = jcast('int', x)
                Code06_NetworkOfSchools2.addEdge(Code06_NetworkOfSchools2.a[Code06_NetworkOfSchools2.m], Code06_NetworkOfSchools2.b[Code06_NetworkOfSchools2.m])
                x = jcast('int', jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_NetworkOfSchools2.n):
            if (Code06_NetworkOfSchools2.dfn[i] == 0):
                Code06_NetworkOfSchools2.tarjan(i)
            i = jcast('int', (i + 1))
        if (Code06_NetworkOfSchools2.sccCnt == 1):
            jcall(out, 'println', '1')
            jcall(out, 'println', '0')
        else:
            i = jcast('int', 1)
            while (i <= Code06_NetworkOfSchools2.m):
                scc1 = jcast('int', Code06_NetworkOfSchools2.belong[Code06_NetworkOfSchools2.a[i]])
                scc2 = jcast('int', Code06_NetworkOfSchools2.belong[Code06_NetworkOfSchools2.b[i]])
                if (scc1 != scc2):
                    Code06_NetworkOfSchools2.outdegree[scc1] = jcast('int', (Code06_NetworkOfSchools2.outdegree[scc1] + 1))
                    Code06_NetworkOfSchools2.indegree[scc2] = jcast('int', (Code06_NetworkOfSchools2.indegree[scc2] + 1))
                i = jcast('int', (i + 1))
            outZero = jcast('int', 0)
            inZero = jcast('int', 0)
            i = jcast('int', 1)
            while (i <= Code06_NetworkOfSchools2.sccCnt):
                if (Code06_NetworkOfSchools2.outdegree[i] == 0):
                    outZero = jcast('int', (outZero + 1))
                if (Code06_NetworkOfSchools2.indegree[i] == 0):
                    inZero = jcast('int', (inZero + 1))
                i = jcast('int', (i + 1))
            jcall(out, 'println', inZero)
            jcall(out, 'println', jstatic('Math', 'max', outZero, inZero))
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
            return jcast('int', self.buffer[((_java_obj_13 := self), (_java_key_14 := 'ptr'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))), _java_old_15)[4]])

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
            raise TypeError("No matching overload for Code06_NetworkOfSchools2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_NetworkOfSchools2.MAXN = jcast('int', 100001)
Code06_NetworkOfSchools2.MAXM = jcast('int', 500001)
Code06_NetworkOfSchools2.n = jcast('int', 0)
Code06_NetworkOfSchools2.m = jcast('int', 0)
Code06_NetworkOfSchools2.a = jarray('int', [Code06_NetworkOfSchools2.MAXM])
Code06_NetworkOfSchools2.b = jarray('int', [Code06_NetworkOfSchools2.MAXM])
Code06_NetworkOfSchools2.head = jarray('int', [Code06_NetworkOfSchools2.MAXN])
Code06_NetworkOfSchools2.nxt = jarray('int', [Code06_NetworkOfSchools2.MAXM])
Code06_NetworkOfSchools2.to = jarray('int', [Code06_NetworkOfSchools2.MAXM])
Code06_NetworkOfSchools2.cntg = jcast('int', 0)
Code06_NetworkOfSchools2.dfn = jarray('int', [Code06_NetworkOfSchools2.MAXN])
Code06_NetworkOfSchools2.low = jarray('int', [Code06_NetworkOfSchools2.MAXN])
Code06_NetworkOfSchools2.cntd = jcast('int', 0)
Code06_NetworkOfSchools2.sta = jarray('int', [Code06_NetworkOfSchools2.MAXN])
Code06_NetworkOfSchools2.top = jcast('int', 0)
Code06_NetworkOfSchools2.belong = jarray('int', [Code06_NetworkOfSchools2.MAXN])
Code06_NetworkOfSchools2.sccCnt = jcast('int', 0)
Code06_NetworkOfSchools2.outdegree = jarray('int', [Code06_NetworkOfSchools2.MAXN])
Code06_NetworkOfSchools2.indegree = jarray('int', [Code06_NetworkOfSchools2.MAXN])

if __name__ == '__main__':
    Code06_NetworkOfSchools2.main([])
