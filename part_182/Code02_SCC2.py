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

# 强连通分量模版题2，Python版
# 给定一张n个点，m条边的有向图
# 求出所有强连通分量，先打印强连通分量的数量
# 每个强连通分量先打印大小，然后打印节点编号，顺序随意
# 1 <= n <= 5 * 10^4
# 1 <= m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/U224391
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_SCC2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccArr': 'sccArr', 'sccSiz': 'sccSiz', 'sccl': 'sccl', 'sccr': 'sccr', 'idx': 'idx', 'sccCnt': 'sccCnt', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
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
    sccArr = None
    sccSiz = None
    sccl = None
    sccr = None
    idx = 0
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
        jset(Code02_SCC2.stack[Code02_SCC2.stacksize], 0, u)
        jset(Code02_SCC2.stack[Code02_SCC2.stacksize], 1, status)
        jset(Code02_SCC2.stack[Code02_SCC2.stacksize], 2, e)
        Code02_SCC2.stacksize = jcast('int', (Code02_SCC2.stacksize + 1))

    @staticmethod
    def pop():
        Code02_SCC2.stacksize = jcast('int', (Code02_SCC2.stacksize - 1))
        Code02_SCC2.u = jcast('int', Code02_SCC2.stack[Code02_SCC2.stacksize][0])
        Code02_SCC2.status = jcast('int', Code02_SCC2.stack[Code02_SCC2.stacksize][1])
        Code02_SCC2.e = jcast('int', Code02_SCC2.stack[Code02_SCC2.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_SCC2.nxt, ((_java_obj_1 := Code02_SCC2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_SCC2.head[u])
        Code02_SCC2.to[Code02_SCC2.cntg] = jcast('int', v)
        Code02_SCC2.head[u] = jcast('int', Code02_SCC2.cntg)

    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code02_SCC2.dfn, u, jset(Code02_SCC2.low, u, ((_java_obj_4 := Code02_SCC2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code02_SCC2.sta, ((_java_obj_7 := Code02_SCC2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code02_SCC2.head[u])
        while (e > 0):
            v = jcast('int', Code02_SCC2.to[e])
            if (Code02_SCC2.dfn[v] == 0):
                Code02_SCC2.tarjan1(v)
                jset(Code02_SCC2.low, u, jstatic('Math', 'min', Code02_SCC2.low[u], Code02_SCC2.low[v]))
            else:
                if (Code02_SCC2.belong[v] == 0):
                    jset(Code02_SCC2.low, u, jstatic('Math', 'min', Code02_SCC2.low[u], Code02_SCC2.dfn[v]))
            e = jcast('int', Code02_SCC2.nxt[e])
        if (Code02_SCC2.dfn[u] == Code02_SCC2.low[u]):
            Code02_SCC2.sccCnt = jcast('int', (Code02_SCC2.sccCnt + 1))
            Code02_SCC2.sccl[Code02_SCC2.sccCnt] = jcast('int', jcast('int', jadd(Code02_SCC2.idx, 1)))
            pop = 0
            while True:
                pop = jcast('int', Code02_SCC2.sta[((_java_obj_10 := Code02_SCC2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code02_SCC2.belong[pop] = jcast('int', Code02_SCC2.sccCnt)
                jset(Code02_SCC2.sccArr, ((_java_obj_13 := Code02_SCC2), (_java_key_14 := 'idx'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], pop)
                Code02_SCC2.sccSiz[Code02_SCC2.sccCnt] = jcast('int', (Code02_SCC2.sccSiz[Code02_SCC2.sccCnt] + 1))
                if not ((pop != u)):
                    break
            Code02_SCC2.sccr[Code02_SCC2.sccCnt] = jcast('int', Code02_SCC2.idx)

    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code02_SCC2.stacksize = jcast('int', 0)
        Code02_SCC2.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code02_SCC2.stacksize > 0):
            Code02_SCC2.pop()
            if (Code02_SCC2.status == jcast('int', (-1))):
                jset(Code02_SCC2.dfn, Code02_SCC2.u, jset(Code02_SCC2.low, Code02_SCC2.u, ((_java_obj_16 := Code02_SCC2), (_java_key_17 := 'cntd'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3]))
                jset(Code02_SCC2.sta, ((_java_obj_19 := Code02_SCC2), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], Code02_SCC2.u)
                Code02_SCC2.e = jcast('int', Code02_SCC2.head[Code02_SCC2.u])
            else:
                v = jcast('int', Code02_SCC2.to[Code02_SCC2.e])
                if (Code02_SCC2.status == 0):
                    jset(Code02_SCC2.low, Code02_SCC2.u, jstatic('Math', 'min', Code02_SCC2.low[Code02_SCC2.u], Code02_SCC2.low[v]))
                if ((Code02_SCC2.status == 1) and (Code02_SCC2.belong[v] == 0)):
                    jset(Code02_SCC2.low, Code02_SCC2.u, jstatic('Math', 'min', Code02_SCC2.low[Code02_SCC2.u], Code02_SCC2.dfn[v]))
                Code02_SCC2.e = jcast('int', Code02_SCC2.nxt[Code02_SCC2.e])
            if (Code02_SCC2.e != 0):
                v = jcast('int', Code02_SCC2.to[Code02_SCC2.e])
                if (Code02_SCC2.dfn[v] == 0):
                    Code02_SCC2.push(Code02_SCC2.u, 0, Code02_SCC2.e)
                    Code02_SCC2.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code02_SCC2.push(Code02_SCC2.u, 1, Code02_SCC2.e)
            else:
                if (Code02_SCC2.dfn[Code02_SCC2.u] == Code02_SCC2.low[Code02_SCC2.u]):
                    Code02_SCC2.sccCnt = jcast('int', (Code02_SCC2.sccCnt + 1))
                    Code02_SCC2.sccl[Code02_SCC2.sccCnt] = jcast('int', jcast('int', jadd(Code02_SCC2.idx, 1)))
                    pop = 0
                    while True:
                        pop = jcast('int', Code02_SCC2.sta[((_java_obj_22 := Code02_SCC2), (_java_key_23 := 'top'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (-1)))), _java_old_24)[4]])
                        Code02_SCC2.belong[pop] = jcast('int', Code02_SCC2.sccCnt)
                        jset(Code02_SCC2.sccArr, ((_java_obj_25 := Code02_SCC2), (_java_key_26 := 'idx'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3], pop)
                        Code02_SCC2.sccSiz[Code02_SCC2.sccCnt] = jcast('int', (Code02_SCC2.sccSiz[Code02_SCC2.sccCnt] + 1))
                        if not ((pop != Code02_SCC2.u)):
                            break
                    Code02_SCC2.sccr[Code02_SCC2.sccCnt] = jcast('int', Code02_SCC2.idx)

    @staticmethod
    def main(args):
        in_ = Code02_SCC2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_SCC2.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_SCC2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code02_SCC2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code02_SCC2.addEdge(u, v)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_SCC2.n):
            if (Code02_SCC2.dfn[i] == 0):
                # tarjan1(i);
                Code02_SCC2.tarjan2(i)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code02_SCC2.sccCnt)
        i = jcast('int', 1)
        while (i <= Code02_SCC2.sccCnt):
            jcall(out, 'print', jadd(Code02_SCC2.sccSiz[i], ' '))
            j = jcast('int', Code02_SCC2.sccl[i])
            while (j <= Code02_SCC2.sccr[i]):
                jcall(out, 'print', jadd(Code02_SCC2.sccArr[j], ' '))
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
            return jcast('int', self.buffer[((_java_obj_28 := self), (_java_key_29 := 'ptr'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))), _java_old_30)[4]])

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
            raise TypeError("No matching overload for Code02_SCC2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_SCC2.MAXN = jcast('int', 50001)
Code02_SCC2.MAXM = jcast('int', 100001)
Code02_SCC2.n = jcast('int', 0)
Code02_SCC2.m = jcast('int', 0)
Code02_SCC2.head = jarray('int', [Code02_SCC2.MAXN])
Code02_SCC2.nxt = jarray('int', [Code02_SCC2.MAXM])
Code02_SCC2.to = jarray('int', [Code02_SCC2.MAXM])
Code02_SCC2.cntg = jcast('int', 0)
Code02_SCC2.dfn = jarray('int', [Code02_SCC2.MAXN])
Code02_SCC2.low = jarray('int', [Code02_SCC2.MAXN])
Code02_SCC2.cntd = jcast('int', 0)
Code02_SCC2.sta = jarray('int', [Code02_SCC2.MAXN])
Code02_SCC2.top = jcast('int', 0)
Code02_SCC2.belong = jarray('int', [Code02_SCC2.MAXN])
Code02_SCC2.sccArr = jarray('int', [Code02_SCC2.MAXN])
Code02_SCC2.sccSiz = jarray('int', [Code02_SCC2.MAXN])
Code02_SCC2.sccl = jarray('int', [Code02_SCC2.MAXN])
Code02_SCC2.sccr = jarray('int', [Code02_SCC2.MAXN])
Code02_SCC2.idx = jcast('int', 0)
Code02_SCC2.sccCnt = jcast('int', 0)
Code02_SCC2.stack = jarray('int', [Code02_SCC2.MAXN, 3])
Code02_SCC2.u = jcast('int', 0)
Code02_SCC2.status = jcast('int', 0)
Code02_SCC2.e = jcast('int', 0)
Code02_SCC2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code02_SCC2.main([])
