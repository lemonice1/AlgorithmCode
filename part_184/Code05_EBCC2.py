# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 边双连通分量模版题，Python版
# 给定一张无向图，一共n个点、m条边
# 图中可能存在多个连通区，对每个连通区求边双连通分量
# 先打印边双连通分量的总数量，然后对每个边双连通分量
# 打印节点个数，然后任意顺序打印该边双连通分量的节点
# 请保证原图即使有重边和自环，答案依然正确
# 1 <= n <= 5 * 10^5
# 1 <= m <= 2 * 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P8436
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_EBCC2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'ebccSiz': 'ebccSiz', 'ebccArr': 'ebccArr', 'ebccl': 'ebccl', 'ebccr': 'ebccr', 'idx': 'idx', 'ebccCnt': 'ebccCnt', 'stack': 'stack', 'u': 'u', 'preEdge': 'preEdge', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
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
    ebccSiz = None
    ebccArr = None
    ebccl = None
    ebccr = None
    idx = 0
    ebccCnt = 0
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stack = None
    u = 0
    preEdge = 0
    status = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, preEdge, status, e):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        status = jcast('int', status)
        e = jcast('int', e)
        jset(Code05_EBCC2.stack[Code05_EBCC2.stacksize], 0, u)
        jset(Code05_EBCC2.stack[Code05_EBCC2.stacksize], 1, preEdge)
        jset(Code05_EBCC2.stack[Code05_EBCC2.stacksize], 2, status)
        jset(Code05_EBCC2.stack[Code05_EBCC2.stacksize], 3, e)
        Code05_EBCC2.stacksize = jcast('int', (Code05_EBCC2.stacksize + 1))

    @staticmethod
    def pop():
        Code05_EBCC2.stacksize = jcast('int', (Code05_EBCC2.stacksize - 1))
        Code05_EBCC2.u = jcast('int', Code05_EBCC2.stack[Code05_EBCC2.stacksize][0])
        Code05_EBCC2.preEdge = jcast('int', Code05_EBCC2.stack[Code05_EBCC2.stacksize][1])
        Code05_EBCC2.status = jcast('int', Code05_EBCC2.stack[Code05_EBCC2.stacksize][2])
        Code05_EBCC2.e = jcast('int', Code05_EBCC2.stack[Code05_EBCC2.stacksize][3])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_EBCC2.nxt, ((_java_obj_1 := Code05_EBCC2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_EBCC2.head[u])
        Code05_EBCC2.to[Code05_EBCC2.cntg] = jcast('int', v)
        Code05_EBCC2.head[u] = jcast('int', Code05_EBCC2.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code05_EBCC2.dfn, u, jset(Code05_EBCC2.low, u, ((_java_obj_4 := Code05_EBCC2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code05_EBCC2.sta, ((_java_obj_7 := Code05_EBCC2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code05_EBCC2.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code05_EBCC2.to[e])
                if (Code05_EBCC2.dfn[v] == 0):
                    Code05_EBCC2.tarjan1(v, e)
                    jset(Code05_EBCC2.low, u, jstatic('Math', 'min', Code05_EBCC2.low[u], Code05_EBCC2.low[v]))
                else:
                    jset(Code05_EBCC2.low, u, jstatic('Math', 'min', Code05_EBCC2.low[u], Code05_EBCC2.dfn[v]))
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
            e = jcast('int', Code05_EBCC2.nxt[e])
        if (Code05_EBCC2.dfn[u] == Code05_EBCC2.low[u]):
            Code05_EBCC2.ebccCnt = jcast('int', (Code05_EBCC2.ebccCnt + 1))
            Code05_EBCC2.ebccSiz[Code05_EBCC2.ebccCnt] = jcast('int', 0)
            Code05_EBCC2.ebccl[Code05_EBCC2.ebccCnt] = jcast('int', jcast('int', jadd(Code05_EBCC2.idx, 1)))
            pop = 0
            while True:
                pop = jcast('int', Code05_EBCC2.sta[((_java_obj_11 := Code05_EBCC2), (_java_key_12 := 'top'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (-1)))), _java_old_13)[4]])
                Code05_EBCC2.ebccSiz[Code05_EBCC2.ebccCnt] = jcast('int', (Code05_EBCC2.ebccSiz[Code05_EBCC2.ebccCnt] + 1))
                jset(Code05_EBCC2.ebccArr, ((_java_obj_14 := Code05_EBCC2), (_java_key_15 := 'idx'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))))[3], pop)
                if not ((pop != u)):
                    break
            Code05_EBCC2.ebccr[Code05_EBCC2.ebccCnt] = jcast('int', Code05_EBCC2.idx)

    # 迭代版
    @staticmethod
    def tarjan2(node, pree):
        node = jcast('int', node)
        pree = jcast('int', pree)
        Code05_EBCC2.stacksize = jcast('int', 0)
        Code05_EBCC2.push(node, pree, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code05_EBCC2.stacksize > 0):
            Code05_EBCC2.pop()
            if (Code05_EBCC2.status == jcast('int', (-1))):
                jset(Code05_EBCC2.dfn, Code05_EBCC2.u, jset(Code05_EBCC2.low, Code05_EBCC2.u, ((_java_obj_17 := Code05_EBCC2), (_java_key_18 := 'cntd'), (_java_old_19 := jget(_java_obj_17, _java_key_18)), jset(_java_obj_17, _java_key_18, jcast('int', (_java_old_19 + (1)))))[3]))
                jset(Code05_EBCC2.sta, ((_java_obj_20 := Code05_EBCC2), (_java_key_21 := 'top'), (_java_old_22 := jget(_java_obj_20, _java_key_21)), jset(_java_obj_20, _java_key_21, jcast('int', (_java_old_22 + (1)))))[3], Code05_EBCC2.u)
                Code05_EBCC2.e = jcast('int', Code05_EBCC2.head[Code05_EBCC2.u])
            else:
                v = jcast('int', Code05_EBCC2.to[Code05_EBCC2.e])
                if (Code05_EBCC2.status == 0):
                    jset(Code05_EBCC2.low, Code05_EBCC2.u, jstatic('Math', 'min', Code05_EBCC2.low[Code05_EBCC2.u], Code05_EBCC2.low[v]))
                else:
                    jset(Code05_EBCC2.low, Code05_EBCC2.u, jstatic('Math', 'min', Code05_EBCC2.low[Code05_EBCC2.u], Code05_EBCC2.dfn[v]))
                Code05_EBCC2.e = jcast('int', Code05_EBCC2.nxt[Code05_EBCC2.e])
            if (jcast('int', (Code05_EBCC2.e ^ 1)) == Code05_EBCC2.preEdge):
                Code05_EBCC2.e = jcast('int', Code05_EBCC2.nxt[Code05_EBCC2.e])
            if (Code05_EBCC2.e != 0):
                v = jcast('int', Code05_EBCC2.to[Code05_EBCC2.e])
                if (Code05_EBCC2.dfn[v] == 0):
                    Code05_EBCC2.push(Code05_EBCC2.u, Code05_EBCC2.preEdge, 0, Code05_EBCC2.e)
                    Code05_EBCC2.push(v, Code05_EBCC2.e, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code05_EBCC2.push(Code05_EBCC2.u, Code05_EBCC2.preEdge, 1, Code05_EBCC2.e)
            else:
                if (Code05_EBCC2.dfn[Code05_EBCC2.u] == Code05_EBCC2.low[Code05_EBCC2.u]):
                    Code05_EBCC2.ebccCnt = jcast('int', (Code05_EBCC2.ebccCnt + 1))
                    Code05_EBCC2.ebccSiz[Code05_EBCC2.ebccCnt] = jcast('int', 0)
                    Code05_EBCC2.ebccl[Code05_EBCC2.ebccCnt] = jcast('int', jcast('int', jadd(Code05_EBCC2.idx, 1)))
                    pop = 0
                    while True:
                        pop = jcast('int', Code05_EBCC2.sta[((_java_obj_23 := Code05_EBCC2), (_java_key_24 := 'top'), (_java_old_25 := jget(_java_obj_23, _java_key_24)), jset(_java_obj_23, _java_key_24, jcast('int', (_java_old_25 + (-1)))), _java_old_25)[4]])
                        Code05_EBCC2.ebccSiz[Code05_EBCC2.ebccCnt] = jcast('int', (Code05_EBCC2.ebccSiz[Code05_EBCC2.ebccCnt] + 1))
                        jset(Code05_EBCC2.ebccArr, ((_java_obj_26 := Code05_EBCC2), (_java_key_27 := 'idx'), (_java_old_28 := jget(_java_obj_26, _java_key_27)), jset(_java_obj_26, _java_key_27, jcast('int', (_java_old_28 + (1)))))[3], pop)
                        if not ((pop != Code05_EBCC2.u)):
                            break
                    Code05_EBCC2.ebccr[Code05_EBCC2.ebccCnt] = jcast('int', Code05_EBCC2.idx)

    @staticmethod
    def main(args):
        in_ = Code05_EBCC2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_EBCC2.cntg = jcast('int', 1)
        Code05_EBCC2.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_EBCC2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code05_EBCC2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code05_EBCC2.addEdge(u, v)
            Code05_EBCC2.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_EBCC2.n):
            if (Code05_EBCC2.dfn[i] == 0):
                # tarjan1(i, 0);
                Code05_EBCC2.tarjan2(i, 0)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code05_EBCC2.ebccCnt)
        i = jcast('int', 1)
        while (i <= Code05_EBCC2.ebccCnt):
            jcall(out, 'println', Code05_EBCC2.ebccSiz[i])
            j = jcast('int', Code05_EBCC2.ebccl[i])
            while (j <= Code05_EBCC2.ebccr[i]):
                jcall(out, 'print', jadd(Code05_EBCC2.ebccArr[j], ' '))
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
            return jcast('int', self.buffer[((_java_obj_29 := self), (_java_key_30 := 'ptr'), (_java_old_31 := jget(_java_obj_29, _java_key_30)), jset(_java_obj_29, _java_key_30, jcast('int', (_java_old_31 + (1)))), _java_old_31)[4]])

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
            raise TypeError("No matching overload for Code05_EBCC2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_EBCC2.MAXN = jcast('int', 500001)
Code05_EBCC2.MAXM = jcast('int', 2000001)
Code05_EBCC2.n = jcast('int', 0)
Code05_EBCC2.m = jcast('int', 0)
Code05_EBCC2.head = jarray('int', [Code05_EBCC2.MAXN])
Code05_EBCC2.nxt = jarray('int', [jcast('int', (Code05_EBCC2.MAXM << (1 & 31)))])
Code05_EBCC2.to = jarray('int', [jcast('int', (Code05_EBCC2.MAXM << (1 & 31)))])
Code05_EBCC2.cntg = jcast('int', 0)
Code05_EBCC2.dfn = jarray('int', [Code05_EBCC2.MAXN])
Code05_EBCC2.low = jarray('int', [Code05_EBCC2.MAXN])
Code05_EBCC2.cntd = jcast('int', 0)
Code05_EBCC2.sta = jarray('int', [Code05_EBCC2.MAXN])
Code05_EBCC2.top = jcast('int', 0)
Code05_EBCC2.ebccSiz = jarray('int', [Code05_EBCC2.MAXN])
Code05_EBCC2.ebccArr = jarray('int', [Code05_EBCC2.MAXN])
Code05_EBCC2.ebccl = jarray('int', [Code05_EBCC2.MAXN])
Code05_EBCC2.ebccr = jarray('int', [Code05_EBCC2.MAXN])
Code05_EBCC2.idx = jcast('int', 0)
Code05_EBCC2.ebccCnt = jcast('int', 0)
Code05_EBCC2.stack = jarray('int', [Code05_EBCC2.MAXN, 4])
Code05_EBCC2.u = jcast('int', 0)
Code05_EBCC2.preEdge = jcast('int', 0)
Code05_EBCC2.status = jcast('int', 0)
Code05_EBCC2.e = jcast('int', 0)
Code05_EBCC2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code05_EBCC2.main([])
