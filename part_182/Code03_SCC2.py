# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 强连通分量模版题3，Python版
# 一共有n个节点，给定m条边，边的格式 a b t
# 如果t为1，表示a到b的单向边，如果t为2，表示a到b的双向边
# 找到图中最大的强连通分量，先打印大小，然后打印包含的节点，编号从小到大输出
# 如果有多个最大的强连通分量，打印字典序最小的结果
# 1 <= n <= 5 * 10^3
# 0 <= m <= 5 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P1726
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_SCC2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccSiz': 'sccSiz', 'sccCnt': 'sccCnt', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
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
    belong = None
    sccSiz = None
    sccCnt = 0
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
        jset(Code03_SCC2.stack[Code03_SCC2.stacksize], 0, u)
        jset(Code03_SCC2.stack[Code03_SCC2.stacksize], 1, status)
        jset(Code03_SCC2.stack[Code03_SCC2.stacksize], 2, e)
        Code03_SCC2.stacksize = jcast('int', (Code03_SCC2.stacksize + 1))

    @staticmethod
    def pop():
        Code03_SCC2.stacksize = jcast('int', (Code03_SCC2.stacksize - 1))
        Code03_SCC2.u = jcast('int', Code03_SCC2.stack[Code03_SCC2.stacksize][0])
        Code03_SCC2.status = jcast('int', Code03_SCC2.stack[Code03_SCC2.stacksize][1])
        Code03_SCC2.e = jcast('int', Code03_SCC2.stack[Code03_SCC2.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_SCC2.nxt, ((_java_obj_1 := Code03_SCC2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_SCC2.head[u])
        Code03_SCC2.to[Code03_SCC2.cntg] = jcast('int', v)
        Code03_SCC2.head[u] = jcast('int', Code03_SCC2.cntg)

    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code03_SCC2.dfn, u, jset(Code03_SCC2.low, u, ((_java_obj_4 := Code03_SCC2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code03_SCC2.sta, ((_java_obj_7 := Code03_SCC2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code03_SCC2.head[u])
        while (e > 0):
            v = jcast('int', Code03_SCC2.to[e])
            if (Code03_SCC2.dfn[v] == 0):
                Code03_SCC2.tarjan1(v)
                jset(Code03_SCC2.low, u, jstatic('Math', 'min', Code03_SCC2.low[u], Code03_SCC2.low[v]))
            else:
                if (Code03_SCC2.belong[v] == 0):
                    jset(Code03_SCC2.low, u, jstatic('Math', 'min', Code03_SCC2.low[u], Code03_SCC2.dfn[v]))
            e = jcast('int', Code03_SCC2.nxt[e])
        if (Code03_SCC2.dfn[u] == Code03_SCC2.low[u]):
            Code03_SCC2.sccCnt = jcast('int', (Code03_SCC2.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code03_SCC2.sta[((_java_obj_10 := Code03_SCC2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code03_SCC2.belong[pop] = jcast('int', Code03_SCC2.sccCnt)
                Code03_SCC2.sccSiz[Code03_SCC2.sccCnt] = jcast('int', (Code03_SCC2.sccSiz[Code03_SCC2.sccCnt] + 1))
                if not ((pop != u)):
                    break

    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code03_SCC2.stacksize = jcast('int', 0)
        Code03_SCC2.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code03_SCC2.stacksize > 0):
            Code03_SCC2.pop()
            if (Code03_SCC2.status == jcast('int', (-1))):
                jset(Code03_SCC2.dfn, Code03_SCC2.u, jset(Code03_SCC2.low, Code03_SCC2.u, ((_java_obj_13 := Code03_SCC2), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code03_SCC2.sta, ((_java_obj_16 := Code03_SCC2), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code03_SCC2.u)
                Code03_SCC2.e = jcast('int', Code03_SCC2.head[Code03_SCC2.u])
            else:
                v = jcast('int', Code03_SCC2.to[Code03_SCC2.e])
                if (Code03_SCC2.status == 0):
                    jset(Code03_SCC2.low, Code03_SCC2.u, jstatic('Math', 'min', Code03_SCC2.low[Code03_SCC2.u], Code03_SCC2.low[v]))
                if ((Code03_SCC2.status == 1) and (Code03_SCC2.belong[v] == 0)):
                    jset(Code03_SCC2.low, Code03_SCC2.u, jstatic('Math', 'min', Code03_SCC2.low[Code03_SCC2.u], Code03_SCC2.dfn[v]))
                Code03_SCC2.e = jcast('int', Code03_SCC2.nxt[Code03_SCC2.e])
            if (Code03_SCC2.e != 0):
                v = jcast('int', Code03_SCC2.to[Code03_SCC2.e])
                if (Code03_SCC2.dfn[v] == 0):
                    Code03_SCC2.push(Code03_SCC2.u, 0, Code03_SCC2.e)
                    Code03_SCC2.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code03_SCC2.push(Code03_SCC2.u, 1, Code03_SCC2.e)
            else:
                if (Code03_SCC2.dfn[Code03_SCC2.u] == Code03_SCC2.low[Code03_SCC2.u]):
                    Code03_SCC2.sccCnt = jcast('int', (Code03_SCC2.sccCnt + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code03_SCC2.sta[((_java_obj_19 := Code03_SCC2), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                        Code03_SCC2.belong[pop] = jcast('int', Code03_SCC2.sccCnt)
                        Code03_SCC2.sccSiz[Code03_SCC2.sccCnt] = jcast('int', (Code03_SCC2.sccSiz[Code03_SCC2.sccCnt] + 1))
                        if not ((pop != Code03_SCC2.u)):
                            break

    @staticmethod
    def main(args):
        in_ = Code03_SCC2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_SCC2.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_SCC2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        a = 0
        b = 0
        t = 0
        while (i <= Code03_SCC2.m):
            a = jcast('int', jcall(in_, 'nextInt'))
            b = jcast('int', jcall(in_, 'nextInt'))
            t = jcast('int', jcall(in_, 'nextInt'))
            if (t == 1):
                Code03_SCC2.addEdge(a, b)
            else:
                Code03_SCC2.addEdge(a, b)
                Code03_SCC2.addEdge(b, a)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_SCC2.n):
            if (Code03_SCC2.dfn[i] == 0):
                # tarjan1(i);
                Code03_SCC2.tarjan2(i)
            i = jcast('int', (i + 1))
        largest = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code03_SCC2.sccCnt):
            largest = jcast('int', jstatic('Math', 'max', largest, Code03_SCC2.sccSiz[i]))
            i = jcast('int', (i + 1))
        jcall(out, 'println', largest)
        i = jcast('int', 1)
        while (i <= Code03_SCC2.n):
            try:
                if (Code03_SCC2.sccSiz[Code03_SCC2.belong[i]] == largest):
                    scc = jcast('int', Code03_SCC2.belong[i])
                    j = jcast('int', i)
                    while (j <= Code03_SCC2.n):
                        if (Code03_SCC2.belong[j] == scc):
                            jcall(out, 'print', jadd(j, ' '))
                        j = jcast('int', (j + 1))
                    raise JBreak(None)
            except JContinue as _java_control_22:
                if _java_control_22.label not in (None,):
                    raise
            except JBreak as _java_control_22:
                if _java_control_22.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        jcall(out, 'println')
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
            return jcast('int', self.buffer[((_java_obj_23 := self), (_java_key_24 := 'ptr'), (_java_old_25 := jget(_java_obj_23, _java_key_24)), jset(_java_obj_23, _java_key_24, jcast('int', (_java_old_25 + (1)))), _java_old_25)[4]])

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
            raise TypeError("No matching overload for Code03_SCC2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_SCC2.MAXN = jcast('int', 5001)
Code03_SCC2.MAXM = jcast('int', 100001)
Code03_SCC2.n = jcast('int', 0)
Code03_SCC2.m = jcast('int', 0)
Code03_SCC2.head = jarray('int', [Code03_SCC2.MAXN])
Code03_SCC2.nxt = jarray('int', [Code03_SCC2.MAXM])
Code03_SCC2.to = jarray('int', [Code03_SCC2.MAXM])
Code03_SCC2.cntg = jcast('int', 0)
Code03_SCC2.dfn = jarray('int', [Code03_SCC2.MAXN])
Code03_SCC2.low = jarray('int', [Code03_SCC2.MAXN])
Code03_SCC2.cntd = jcast('int', 0)
Code03_SCC2.sta = jarray('int', [Code03_SCC2.MAXN])
Code03_SCC2.top = jcast('int', 0)
Code03_SCC2.belong = jarray('int', [Code03_SCC2.MAXN])
Code03_SCC2.sccSiz = jarray('int', [Code03_SCC2.MAXN])
Code03_SCC2.sccCnt = jcast('int', 0)
Code03_SCC2.stack = jarray('int', [Code03_SCC2.MAXN, 3])
Code03_SCC2.u = jcast('int', 0)
Code03_SCC2.status = jcast('int', 0)
Code03_SCC2.e = jcast('int', 0)
Code03_SCC2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code03_SCC2.main([])
