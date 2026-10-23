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

# 关键网络线路，Python版
# 给定一张无向图，一共n个点、m条边，保证所有点连通
# 给定k个提供A服务的节点，给定l个提供B服务的节点，保证k和l都是正数
# 一个节点可能不提供服务，也可能提供A服务或者B服务或者两种都有
# 每个节点可以通过边，获得任何节点提供的服务，但是必须同时获得两种服务
# 如果断开某一条边，使得某些节点无法同时获得两种服务，这样的边叫关键边
# 打印关键边的数量，打印每条关键边的两个端点
# 1 <= n <= 10^5
# 1 <= m <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P7687
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_CriticalNetworkLines1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'k': 'k', 'l': 'l', 'acnt': 'acnt', 'bcnt': 'bcnt', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'ans1': 'ans1', 'ans2': 'ans2', 'cnta': 'cnta', 'stau': 'stau', 'stap': 'stap', 'stas': 'stas', 'stae': 'stae', 'u': 'u', 'preEdge': 'preEdge', 'status': 'status', 'e': 'e', 'stasiz': 'stasiz'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    k = 0
    l = 0
    acnt = None
    bcnt = None
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    ans1 = None
    ans2 = None
    cnta = 0
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stau = None
    stap = None
    stas = None
    stae = None
    u = 0
    preEdge = 0
    status = 0
    e = 0
    stasiz = 0
    @staticmethod
    def push(u, preEdge, status, e):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        status = jcast('int', status)
        e = jcast('int', e)
        Code03_CriticalNetworkLines1.stau[Code03_CriticalNetworkLines1.stasiz] = jcast('int', u)
        Code03_CriticalNetworkLines1.stap[Code03_CriticalNetworkLines1.stasiz] = jcast('int', preEdge)
        Code03_CriticalNetworkLines1.stas[Code03_CriticalNetworkLines1.stasiz] = jcast('int', status)
        Code03_CriticalNetworkLines1.stae[Code03_CriticalNetworkLines1.stasiz] = jcast('int', e)
        Code03_CriticalNetworkLines1.stasiz = jcast('int', (Code03_CriticalNetworkLines1.stasiz + 1))

    @staticmethod
    def pop():
        Code03_CriticalNetworkLines1.stasiz = jcast('int', (Code03_CriticalNetworkLines1.stasiz - 1))
        Code03_CriticalNetworkLines1.u = jcast('int', Code03_CriticalNetworkLines1.stau[Code03_CriticalNetworkLines1.stasiz])
        Code03_CriticalNetworkLines1.preEdge = jcast('int', Code03_CriticalNetworkLines1.stap[Code03_CriticalNetworkLines1.stasiz])
        Code03_CriticalNetworkLines1.status = jcast('int', Code03_CriticalNetworkLines1.stas[Code03_CriticalNetworkLines1.stasiz])
        Code03_CriticalNetworkLines1.e = jcast('int', Code03_CriticalNetworkLines1.stae[Code03_CriticalNetworkLines1.stasiz])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_CriticalNetworkLines1.nxt, ((_java_obj_1 := Code03_CriticalNetworkLines1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_CriticalNetworkLines1.head[u])
        Code03_CriticalNetworkLines1.to[Code03_CriticalNetworkLines1.cntg] = jcast('int', v)
        Code03_CriticalNetworkLines1.head[u] = jcast('int', Code03_CriticalNetworkLines1.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code03_CriticalNetworkLines1.dfn, u, jset(Code03_CriticalNetworkLines1.low, u, ((_java_obj_4 := Code03_CriticalNetworkLines1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        e = jcast('int', Code03_CriticalNetworkLines1.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code03_CriticalNetworkLines1.to[e])
                if (Code03_CriticalNetworkLines1.dfn[v] == 0):
                    Code03_CriticalNetworkLines1.tarjan1(v, e)
                    jset(Code03_CriticalNetworkLines1.low, u, jstatic('Math', 'min', Code03_CriticalNetworkLines1.low[u], Code03_CriticalNetworkLines1.low[v]))
                    if (Code03_CriticalNetworkLines1.low[v] > Code03_CriticalNetworkLines1.dfn[u]):
                        if ((((Code03_CriticalNetworkLines1.acnt[v] == 0) or (Code03_CriticalNetworkLines1.acnt[v] == Code03_CriticalNetworkLines1.k)) or (Code03_CriticalNetworkLines1.bcnt[v] == 0)) or (Code03_CriticalNetworkLines1.bcnt[v] == Code03_CriticalNetworkLines1.l)):
                            Code03_CriticalNetworkLines1.cnta = jcast('int', (Code03_CriticalNetworkLines1.cnta + 1))
                            Code03_CriticalNetworkLines1.ans1[Code03_CriticalNetworkLines1.cnta] = jcast('int', v)
                            Code03_CriticalNetworkLines1.ans2[Code03_CriticalNetworkLines1.cnta] = jcast('int', u)
                    Code03_CriticalNetworkLines1.acnt[u] = jcast('int', jcast('int', jadd(Code03_CriticalNetworkLines1.acnt[u], Code03_CriticalNetworkLines1.acnt[v])))
                    Code03_CriticalNetworkLines1.bcnt[u] = jcast('int', jcast('int', jadd(Code03_CriticalNetworkLines1.bcnt[u], Code03_CriticalNetworkLines1.bcnt[v])))
                else:
                    jset(Code03_CriticalNetworkLines1.low, u, jstatic('Math', 'min', Code03_CriticalNetworkLines1.low[u], Code03_CriticalNetworkLines1.dfn[v]))
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break
            e = jcast('int', Code03_CriticalNetworkLines1.nxt[e])

    # 迭代版
    @staticmethod
    def tarjan2(node, pree):
        node = jcast('int', node)
        pree = jcast('int', pree)
        Code03_CriticalNetworkLines1.stasiz = jcast('int', 0)
        Code03_CriticalNetworkLines1.push(node, pree, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code03_CriticalNetworkLines1.stasiz > 0):
            Code03_CriticalNetworkLines1.pop()
            if (Code03_CriticalNetworkLines1.status == jcast('int', (-1))):
                jset(Code03_CriticalNetworkLines1.dfn, Code03_CriticalNetworkLines1.u, jset(Code03_CriticalNetworkLines1.low, Code03_CriticalNetworkLines1.u, ((_java_obj_8 := Code03_CriticalNetworkLines1), (_java_key_9 := 'cntd'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3]))
                Code03_CriticalNetworkLines1.e = jcast('int', Code03_CriticalNetworkLines1.head[Code03_CriticalNetworkLines1.u])
            else:
                v = jcast('int', Code03_CriticalNetworkLines1.to[Code03_CriticalNetworkLines1.e])
                if (Code03_CriticalNetworkLines1.status == 0):
                    jset(Code03_CriticalNetworkLines1.low, Code03_CriticalNetworkLines1.u, jstatic('Math', 'min', Code03_CriticalNetworkLines1.low[Code03_CriticalNetworkLines1.u], Code03_CriticalNetworkLines1.low[v]))
                    if (Code03_CriticalNetworkLines1.low[v] > Code03_CriticalNetworkLines1.dfn[Code03_CriticalNetworkLines1.u]):
                        if ((((Code03_CriticalNetworkLines1.acnt[v] == 0) or (Code03_CriticalNetworkLines1.acnt[v] == Code03_CriticalNetworkLines1.k)) or (Code03_CriticalNetworkLines1.bcnt[v] == 0)) or (Code03_CriticalNetworkLines1.bcnt[v] == Code03_CriticalNetworkLines1.l)):
                            Code03_CriticalNetworkLines1.cnta = jcast('int', (Code03_CriticalNetworkLines1.cnta + 1))
                            Code03_CriticalNetworkLines1.ans1[Code03_CriticalNetworkLines1.cnta] = jcast('int', v)
                            Code03_CriticalNetworkLines1.ans2[Code03_CriticalNetworkLines1.cnta] = jcast('int', Code03_CriticalNetworkLines1.u)
                    Code03_CriticalNetworkLines1.acnt[Code03_CriticalNetworkLines1.u] = jcast('int', jcast('int', jadd(Code03_CriticalNetworkLines1.acnt[Code03_CriticalNetworkLines1.u], Code03_CriticalNetworkLines1.acnt[v])))
                    Code03_CriticalNetworkLines1.bcnt[Code03_CriticalNetworkLines1.u] = jcast('int', jcast('int', jadd(Code03_CriticalNetworkLines1.bcnt[Code03_CriticalNetworkLines1.u], Code03_CriticalNetworkLines1.bcnt[v])))
                else:
                    jset(Code03_CriticalNetworkLines1.low, Code03_CriticalNetworkLines1.u, jstatic('Math', 'min', Code03_CriticalNetworkLines1.low[Code03_CriticalNetworkLines1.u], Code03_CriticalNetworkLines1.dfn[v]))
                Code03_CriticalNetworkLines1.e = jcast('int', Code03_CriticalNetworkLines1.nxt[Code03_CriticalNetworkLines1.e])
            if (jcast('int', (Code03_CriticalNetworkLines1.e ^ 1)) == Code03_CriticalNetworkLines1.preEdge):
                Code03_CriticalNetworkLines1.e = jcast('int', Code03_CriticalNetworkLines1.nxt[Code03_CriticalNetworkLines1.e])
            if (Code03_CriticalNetworkLines1.e != 0):
                v = jcast('int', Code03_CriticalNetworkLines1.to[Code03_CriticalNetworkLines1.e])
                if (Code03_CriticalNetworkLines1.dfn[v] == 0):
                    Code03_CriticalNetworkLines1.push(Code03_CriticalNetworkLines1.u, Code03_CriticalNetworkLines1.preEdge, 0, Code03_CriticalNetworkLines1.e)
                    Code03_CriticalNetworkLines1.push(v, Code03_CriticalNetworkLines1.e, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code03_CriticalNetworkLines1.push(Code03_CriticalNetworkLines1.u, Code03_CriticalNetworkLines1.preEdge, 1, Code03_CriticalNetworkLines1.e)

    @staticmethod
    def main(args):
        in_ = Code03_CriticalNetworkLines1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_CriticalNetworkLines1.cntg = jcast('int', 1)
        Code03_CriticalNetworkLines1.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_CriticalNetworkLines1.m = jcast('int', jcall(in_, 'nextInt'))
        Code03_CriticalNetworkLines1.k = jcast('int', jcall(in_, 'nextInt'))
        Code03_CriticalNetworkLines1.l = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        while (i <= Code03_CriticalNetworkLines1.k):
            x = jcast('int', jcall(in_, 'nextInt'))
            Code03_CriticalNetworkLines1.acnt[x] = jcast('int', 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        x = 0
        while (i <= Code03_CriticalNetworkLines1.l):
            x = jcast('int', jcall(in_, 'nextInt'))
            Code03_CriticalNetworkLines1.bcnt[x] = jcast('int', 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code03_CriticalNetworkLines1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code03_CriticalNetworkLines1.addEdge(u, v)
            Code03_CriticalNetworkLines1.addEdge(v, u)
            i = jcast('int', (i + 1))
        # tarjan1(1, 0);
        Code03_CriticalNetworkLines1.tarjan2(1, 0)
        jcall(out, 'println', Code03_CriticalNetworkLines1.cnta)
        i = jcast('int', 1)
        while (i <= Code03_CriticalNetworkLines1.cnta):
            jcall(out, 'println', jadd(jadd(Code03_CriticalNetworkLines1.ans1[i], ' '), Code03_CriticalNetworkLines1.ans2[i]))
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
            return jcast('int', self.buffer[((_java_obj_11 := self), (_java_key_12 := 'ptr'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]])

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
            raise TypeError("No matching overload for Code03_CriticalNetworkLines1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_CriticalNetworkLines1.MAXN = jcast('int', 100001)
Code03_CriticalNetworkLines1.MAXM = jcast('int', 1000001)
Code03_CriticalNetworkLines1.n = jcast('int', 0)
Code03_CriticalNetworkLines1.m = jcast('int', 0)
Code03_CriticalNetworkLines1.k = jcast('int', 0)
Code03_CriticalNetworkLines1.l = jcast('int', 0)
Code03_CriticalNetworkLines1.acnt = jarray('int', [Code03_CriticalNetworkLines1.MAXN])
Code03_CriticalNetworkLines1.bcnt = jarray('int', [Code03_CriticalNetworkLines1.MAXN])
Code03_CriticalNetworkLines1.head = jarray('int', [Code03_CriticalNetworkLines1.MAXN])
Code03_CriticalNetworkLines1.nxt = jarray('int', [jcast('int', (Code03_CriticalNetworkLines1.MAXM << (1 & 31)))])
Code03_CriticalNetworkLines1.to = jarray('int', [jcast('int', (Code03_CriticalNetworkLines1.MAXM << (1 & 31)))])
Code03_CriticalNetworkLines1.cntg = jcast('int', 0)
Code03_CriticalNetworkLines1.dfn = jarray('int', [Code03_CriticalNetworkLines1.MAXN])
Code03_CriticalNetworkLines1.low = jarray('int', [Code03_CriticalNetworkLines1.MAXN])
Code03_CriticalNetworkLines1.cntd = jcast('int', 0)
Code03_CriticalNetworkLines1.ans1 = jarray('int', [Code03_CriticalNetworkLines1.MAXN])
Code03_CriticalNetworkLines1.ans2 = jarray('int', [Code03_CriticalNetworkLines1.MAXN])
Code03_CriticalNetworkLines1.cnta = jcast('int', 0)
Code03_CriticalNetworkLines1.stau = jarray('int', [Code03_CriticalNetworkLines1.MAXN])
Code03_CriticalNetworkLines1.stap = jarray('int', [Code03_CriticalNetworkLines1.MAXN])
Code03_CriticalNetworkLines1.stas = jarray('int', [Code03_CriticalNetworkLines1.MAXN])
Code03_CriticalNetworkLines1.stae = jarray('int', [Code03_CriticalNetworkLines1.MAXN])
Code03_CriticalNetworkLines1.u = jcast('int', 0)
Code03_CriticalNetworkLines1.preEdge = jcast('int', 0)
Code03_CriticalNetworkLines1.status = jcast('int', 0)
Code03_CriticalNetworkLines1.e = jcast('int', 0)
Code03_CriticalNetworkLines1.stasiz = jcast('int', 0)

if __name__ == '__main__':
    Code03_CriticalNetworkLines1.main([])
