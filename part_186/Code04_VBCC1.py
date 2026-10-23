# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 点双连通分量模版题1，Python版
# 给定一张无向图，一共n个点、m条边，建图时忽略自环
# 打印点双连通分量的个数
# 打印每个点双连通分量的大小和节点编号
# 打印顺序随意
# 每个孤立点分配一个点双连通分量
# 1 <= n <= 5 * 10^5
# 1 <= m <= 2 * 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P8435
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_VBCC1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'vbccSiz': 'vbccSiz', 'vbccArr': 'vbccArr', 'vbccl': 'vbccl', 'vbccr': 'vbccr', 'idx': 'idx', 'vbccCnt': 'vbccCnt', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
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
    vbccSiz = None
    vbccArr = None
    vbccl = None
    vbccr = None
    idx = 0
    vbccCnt = 0
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
        jset(Code04_VBCC1.stack[Code04_VBCC1.stacksize], 0, u)
        jset(Code04_VBCC1.stack[Code04_VBCC1.stacksize], 1, status)
        jset(Code04_VBCC1.stack[Code04_VBCC1.stacksize], 2, e)
        Code04_VBCC1.stacksize = jcast('int', (Code04_VBCC1.stacksize + 1))

    @staticmethod
    def pop():
        Code04_VBCC1.stacksize = jcast('int', (Code04_VBCC1.stacksize - 1))
        Code04_VBCC1.u = jcast('int', Code04_VBCC1.stack[Code04_VBCC1.stacksize][0])
        Code04_VBCC1.status = jcast('int', Code04_VBCC1.stack[Code04_VBCC1.stacksize][1])
        Code04_VBCC1.e = jcast('int', Code04_VBCC1.stack[Code04_VBCC1.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_VBCC1.nxt, ((_java_obj_1 := Code04_VBCC1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_VBCC1.head[u])
        Code04_VBCC1.to[Code04_VBCC1.cntg] = jcast('int', v)
        Code04_VBCC1.head[u] = jcast('int', Code04_VBCC1.cntg)

    # 递归版，Tarjan算法求解点双连通分量
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code04_VBCC1.dfn, u, jset(Code04_VBCC1.low, u, ((_java_obj_4 := Code04_VBCC1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code04_VBCC1.sta, ((_java_obj_7 := Code04_VBCC1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code04_VBCC1.head[u])
        while (e > 0):
            v = jcast('int', Code04_VBCC1.to[e])
            if (Code04_VBCC1.dfn[v] == 0):
                Code04_VBCC1.tarjan1(v)
                jset(Code04_VBCC1.low, u, jstatic('Math', 'min', Code04_VBCC1.low[u], Code04_VBCC1.low[v]))
                if (Code04_VBCC1.low[v] >= Code04_VBCC1.dfn[u]):
                    Code04_VBCC1.vbccCnt = jcast('int', (Code04_VBCC1.vbccCnt + 1))
                    Code04_VBCC1.vbccSiz[Code04_VBCC1.vbccCnt] = jcast('int', 1)
                    jset(Code04_VBCC1.vbccArr, ((_java_obj_10 := Code04_VBCC1), (_java_key_11 := 'idx'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
                    Code04_VBCC1.vbccl[Code04_VBCC1.vbccCnt] = jcast('int', Code04_VBCC1.idx)
                    pop = 0
                    while True:
                        pop = jcast('int', Code04_VBCC1.sta[((_java_obj_13 := Code04_VBCC1), (_java_key_14 := 'top'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]])
                        Code04_VBCC1.vbccSiz[Code04_VBCC1.vbccCnt] = jcast('int', (Code04_VBCC1.vbccSiz[Code04_VBCC1.vbccCnt] + 1))
                        jset(Code04_VBCC1.vbccArr, ((_java_obj_16 := Code04_VBCC1), (_java_key_17 := 'idx'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], pop)
                        if not ((pop != v)):
                            break
                    Code04_VBCC1.vbccr[Code04_VBCC1.vbccCnt] = jcast('int', Code04_VBCC1.idx)
            else:
                jset(Code04_VBCC1.low, u, jstatic('Math', 'min', Code04_VBCC1.low[u], Code04_VBCC1.dfn[v]))
            e = jcast('int', Code04_VBCC1.nxt[e])

    # 迭代版，Tarjan算法求解点双连通分量
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code04_VBCC1.stacksize = jcast('int', 0)
        Code04_VBCC1.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code04_VBCC1.stacksize > 0):
            Code04_VBCC1.pop()
            if (Code04_VBCC1.status == jcast('int', (-1))):
                jset(Code04_VBCC1.dfn, Code04_VBCC1.u, jset(Code04_VBCC1.low, Code04_VBCC1.u, ((_java_obj_19 := Code04_VBCC1), (_java_key_20 := 'cntd'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3]))
                jset(Code04_VBCC1.sta, ((_java_obj_22 := Code04_VBCC1), (_java_key_23 := 'top'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))))[3], Code04_VBCC1.u)
                Code04_VBCC1.e = jcast('int', Code04_VBCC1.head[Code04_VBCC1.u])
            else:
                v = jcast('int', Code04_VBCC1.to[Code04_VBCC1.e])
                if (Code04_VBCC1.status == 0):
                    jset(Code04_VBCC1.low, Code04_VBCC1.u, jstatic('Math', 'min', Code04_VBCC1.low[Code04_VBCC1.u], Code04_VBCC1.low[v]))
                    if (Code04_VBCC1.low[v] >= Code04_VBCC1.dfn[Code04_VBCC1.u]):
                        Code04_VBCC1.vbccCnt = jcast('int', (Code04_VBCC1.vbccCnt + 1))
                        Code04_VBCC1.vbccSiz[Code04_VBCC1.vbccCnt] = jcast('int', 1)
                        jset(Code04_VBCC1.vbccArr, ((_java_obj_25 := Code04_VBCC1), (_java_key_26 := 'idx'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3], Code04_VBCC1.u)
                        Code04_VBCC1.vbccl[Code04_VBCC1.vbccCnt] = jcast('int', Code04_VBCC1.idx)
                        pop = 0
                        while True:
                            pop = jcast('int', Code04_VBCC1.sta[((_java_obj_28 := Code04_VBCC1), (_java_key_29 := 'top'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (-1)))), _java_old_30)[4]])
                            Code04_VBCC1.vbccSiz[Code04_VBCC1.vbccCnt] = jcast('int', (Code04_VBCC1.vbccSiz[Code04_VBCC1.vbccCnt] + 1))
                            jset(Code04_VBCC1.vbccArr, ((_java_obj_31 := Code04_VBCC1), (_java_key_32 := 'idx'), (_java_old_33 := jget(_java_obj_31, _java_key_32)), jset(_java_obj_31, _java_key_32, jcast('int', (_java_old_33 + (1)))))[3], pop)
                            if not ((pop != v)):
                                break
                        Code04_VBCC1.vbccr[Code04_VBCC1.vbccCnt] = jcast('int', Code04_VBCC1.idx)
                else:
                    jset(Code04_VBCC1.low, Code04_VBCC1.u, jstatic('Math', 'min', Code04_VBCC1.low[Code04_VBCC1.u], Code04_VBCC1.dfn[v]))
                Code04_VBCC1.e = jcast('int', Code04_VBCC1.nxt[Code04_VBCC1.e])
            if (Code04_VBCC1.e != 0):
                v = jcast('int', Code04_VBCC1.to[Code04_VBCC1.e])
                if (Code04_VBCC1.dfn[v] == 0):
                    Code04_VBCC1.push(Code04_VBCC1.u, 0, Code04_VBCC1.e)
                    Code04_VBCC1.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code04_VBCC1.push(Code04_VBCC1.u, 1, Code04_VBCC1.e)

    @staticmethod
    def main(args):
        in_ = Code04_VBCC1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_VBCC1.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_VBCC1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code04_VBCC1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            if (u != v):
                Code04_VBCC1.addEdge(u, v)
                Code04_VBCC1.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_VBCC1.n):
            if (Code04_VBCC1.dfn[i] == 0):
                if (Code04_VBCC1.head[i] == 0):
                    Code04_VBCC1.vbccCnt = jcast('int', (Code04_VBCC1.vbccCnt + 1))
                    Code04_VBCC1.vbccSiz[Code04_VBCC1.vbccCnt] = jcast('int', 1)
                    jset(Code04_VBCC1.vbccArr, ((_java_obj_34 := Code04_VBCC1), (_java_key_35 := 'idx'), (_java_old_36 := jget(_java_obj_34, _java_key_35)), jset(_java_obj_34, _java_key_35, jcast('int', (_java_old_36 + (1)))))[3], i)
                    jset(Code04_VBCC1.vbccl, Code04_VBCC1.vbccCnt, jset(Code04_VBCC1.vbccr, Code04_VBCC1.vbccCnt, Code04_VBCC1.idx))
                else:
                    # tarjan1(i);
                    Code04_VBCC1.tarjan2(i)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code04_VBCC1.vbccCnt)
        i = jcast('int', 1)
        while (i <= Code04_VBCC1.vbccCnt):
            jcall(out, 'println', Code04_VBCC1.vbccSiz[i])
            j = jcast('int', Code04_VBCC1.vbccl[i])
            while (j <= Code04_VBCC1.vbccr[i]):
                jcall(out, 'print', jadd(Code04_VBCC1.vbccArr[j], ' '))
                j = jcast('int', (j + 1))
            jcall(out, 'println')
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
            return jcast('int', self.buffer[((_java_obj_37 := self), (_java_key_38 := 'ptr'), (_java_old_39 := jget(_java_obj_37, _java_key_38)), jset(_java_obj_37, _java_key_38, jcast('int', (_java_old_39 + (1)))), _java_old_39)[4]])

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
            raise TypeError("No matching overload for Code04_VBCC1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_VBCC1.MAXN = jcast('int', 500001)
Code04_VBCC1.MAXM = jcast('int', 2000001)
Code04_VBCC1.n = jcast('int', 0)
Code04_VBCC1.m = jcast('int', 0)
Code04_VBCC1.head = jarray('int', [Code04_VBCC1.MAXN])
Code04_VBCC1.nxt = jarray('int', [jcast('int', (Code04_VBCC1.MAXM << (1 & 31)))])
Code04_VBCC1.to = jarray('int', [jcast('int', (Code04_VBCC1.MAXM << (1 & 31)))])
Code04_VBCC1.cntg = jcast('int', 0)
Code04_VBCC1.dfn = jarray('int', [Code04_VBCC1.MAXN])
Code04_VBCC1.low = jarray('int', [Code04_VBCC1.MAXN])
Code04_VBCC1.cntd = jcast('int', 0)
Code04_VBCC1.sta = jarray('int', [Code04_VBCC1.MAXN])
Code04_VBCC1.top = jcast('int', 0)
Code04_VBCC1.vbccSiz = jarray('int', [Code04_VBCC1.MAXN])
Code04_VBCC1.vbccArr = jarray('int', [jcast('int', (Code04_VBCC1.MAXN << (1 & 31)))])
Code04_VBCC1.vbccl = jarray('int', [Code04_VBCC1.MAXN])
Code04_VBCC1.vbccr = jarray('int', [Code04_VBCC1.MAXN])
Code04_VBCC1.idx = jcast('int', 0)
Code04_VBCC1.vbccCnt = jcast('int', 0)
Code04_VBCC1.stack = jarray('int', [Code04_VBCC1.MAXN, 3])
Code04_VBCC1.u = jcast('int', 0)
Code04_VBCC1.status = jcast('int', 0)
Code04_VBCC1.e = jcast('int', 0)
Code04_VBCC1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code04_VBCC1.main([])
