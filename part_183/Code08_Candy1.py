# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 糖果，Python版
# 一共n个人，每人至少得到一个糖果，一共k条要求，要求有5种类型
# 1 u v : u的糖果 == v的糖果    2 u v : u的糖果 < v的糖果
# 3 u v : u的糖果 >= v的糖果    4 u v : u的糖果 > v的糖果
# 5 u v : u的糖果 <= v的糖果
# 如果无法满足所有要求打印-1，否则打印需要的最少糖果数
# 1 <= n、k <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3275
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code08_Candy1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'k': 'k', 'm': 'm', 'a': 'a', 'b': 'b', 'c': 'c', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccSiz': 'sccSiz', 'sccCnt': 'sccCnt', 'indegree': 'indegree', 'dp': 'dp', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    n = 0
    k = 0
    m = 0
    a = None
    b = None
    c = None
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
    sccSiz = None
    sccCnt = 0
    indegree = None
    dp = None
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
        jset(Code08_Candy1.stack[Code08_Candy1.stacksize], 0, u)
        jset(Code08_Candy1.stack[Code08_Candy1.stacksize], 1, status)
        jset(Code08_Candy1.stack[Code08_Candy1.stacksize], 2, e)
        Code08_Candy1.stacksize = jcast('int', (Code08_Candy1.stacksize + 1))

    @staticmethod
    def pop():
        Code08_Candy1.stacksize = jcast('int', (Code08_Candy1.stacksize - 1))
        Code08_Candy1.u = jcast('int', Code08_Candy1.stack[Code08_Candy1.stacksize][0])
        Code08_Candy1.status = jcast('int', Code08_Candy1.stack[Code08_Candy1.stacksize][1])
        Code08_Candy1.e = jcast('int', Code08_Candy1.stack[Code08_Candy1.stacksize][2])

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code08_Candy1.nxt, ((_java_obj_1 := Code08_Candy1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code08_Candy1.head[u])
        Code08_Candy1.to[Code08_Candy1.cntg] = jcast('int', v)
        Code08_Candy1.weight[Code08_Candy1.cntg] = jcast('int', w)
        Code08_Candy1.head[u] = jcast('int', Code08_Candy1.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code08_Candy1.dfn, u, jset(Code08_Candy1.low, u, ((_java_obj_4 := Code08_Candy1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code08_Candy1.sta, ((_java_obj_7 := Code08_Candy1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code08_Candy1.head[u])
        while (e > 0):
            v = jcast('int', Code08_Candy1.to[e])
            if (Code08_Candy1.dfn[v] == 0):
                Code08_Candy1.tarjan1(v)
                jset(Code08_Candy1.low, u, jstatic('Math', 'min', Code08_Candy1.low[u], Code08_Candy1.low[v]))
            else:
                if (Code08_Candy1.belong[v] == 0):
                    jset(Code08_Candy1.low, u, jstatic('Math', 'min', Code08_Candy1.low[u], Code08_Candy1.dfn[v]))
            e = jcast('int', Code08_Candy1.nxt[e])
        if (Code08_Candy1.dfn[u] == Code08_Candy1.low[u]):
            Code08_Candy1.sccCnt = jcast('int', (Code08_Candy1.sccCnt + 1))
            Code08_Candy1.sccSiz[Code08_Candy1.sccCnt] = jcast('int', 0)
            pop = 0
            while True:
                pop = jcast('int', Code08_Candy1.sta[((_java_obj_10 := Code08_Candy1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code08_Candy1.belong[pop] = jcast('int', Code08_Candy1.sccCnt)
                Code08_Candy1.sccSiz[Code08_Candy1.sccCnt] = jcast('int', (Code08_Candy1.sccSiz[Code08_Candy1.sccCnt] + 1))
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code08_Candy1.stacksize = jcast('int', 0)
        Code08_Candy1.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code08_Candy1.stacksize > 0):
            Code08_Candy1.pop()
            if (Code08_Candy1.status == jcast('int', (-1))):
                jset(Code08_Candy1.dfn, Code08_Candy1.u, jset(Code08_Candy1.low, Code08_Candy1.u, ((_java_obj_13 := Code08_Candy1), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code08_Candy1.sta, ((_java_obj_16 := Code08_Candy1), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code08_Candy1.u)
                Code08_Candy1.e = jcast('int', Code08_Candy1.head[Code08_Candy1.u])
            else:
                v = jcast('int', Code08_Candy1.to[Code08_Candy1.e])
                if (Code08_Candy1.status == 0):
                    jset(Code08_Candy1.low, Code08_Candy1.u, jstatic('Math', 'min', Code08_Candy1.low[Code08_Candy1.u], Code08_Candy1.low[v]))
                if ((Code08_Candy1.status == 1) and (Code08_Candy1.belong[v] == 0)):
                    jset(Code08_Candy1.low, Code08_Candy1.u, jstatic('Math', 'min', Code08_Candy1.low[Code08_Candy1.u], Code08_Candy1.dfn[v]))
                Code08_Candy1.e = jcast('int', Code08_Candy1.nxt[Code08_Candy1.e])
            if (Code08_Candy1.e != 0):
                v = jcast('int', Code08_Candy1.to[Code08_Candy1.e])
                if (Code08_Candy1.dfn[v] == 0):
                    Code08_Candy1.push(Code08_Candy1.u, 0, Code08_Candy1.e)
                    Code08_Candy1.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code08_Candy1.push(Code08_Candy1.u, 1, Code08_Candy1.e)
            else:
                if (Code08_Candy1.dfn[Code08_Candy1.u] == Code08_Candy1.low[Code08_Candy1.u]):
                    Code08_Candy1.sccCnt = jcast('int', (Code08_Candy1.sccCnt + 1))
                    Code08_Candy1.sccSiz[Code08_Candy1.sccCnt] = jcast('int', 0)
                    pop = 0
                    while True:
                        pop = jcast('int', Code08_Candy1.sta[((_java_obj_19 := Code08_Candy1), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                        Code08_Candy1.belong[pop] = jcast('int', Code08_Candy1.sccCnt)
                        Code08_Candy1.sccSiz[Code08_Candy1.sccCnt] = jcast('int', (Code08_Candy1.sccSiz[Code08_Candy1.sccCnt] + 1))
                        if not ((pop != Code08_Candy1.u)):
                            break

    @staticmethod
    def condense():
        Code08_Candy1.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code08_Candy1.sccCnt):
            Code08_Candy1.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code08_Candy1.m):
            scc1 = jcast('int', Code08_Candy1.belong[Code08_Candy1.a[i]])
            scc2 = jcast('int', Code08_Candy1.belong[Code08_Candy1.b[i]])
            w = jcast('int', Code08_Candy1.c[i])
            if ((scc1 == scc2) and (w > 0)):
                return jcast('boolean', False)
            if (scc1 != scc2):
                Code08_Candy1.indegree[scc2] = jcast('int', (Code08_Candy1.indegree[scc2] + 1))
                Code08_Candy1.addEdge(scc1, scc2, w)
            i = jcast('int', (i + 1))
        return jcast('boolean', True)

    @staticmethod
    def dpOnDAG():
        u = jcast('int', Code08_Candy1.sccCnt)
        while (u > 0):
            if (Code08_Candy1.indegree[u] == 0):
                Code08_Candy1.dp[u] = jcast('long', 1)
            e = jcast('int', Code08_Candy1.head[u])
            while (e > 0):
                v = jcast('int', Code08_Candy1.to[e])
                w = jcast('int', Code08_Candy1.weight[e])
                jset(Code08_Candy1.dp, v, jstatic('Math', 'max', Code08_Candy1.dp[v], jcast('long', jadd(Code08_Candy1.dp[u], w))))
                e = jcast('int', Code08_Candy1.nxt[e])
            u = jcast('int', (u - 1))
        ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code08_Candy1.sccCnt):
            ans = jcast('long', jcast('long', jadd(ans, jcast('long', (Code08_Candy1.dp[i] * Code08_Candy1.sccSiz[i])))))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code08_Candy1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code08_Candy1.n = jcast('int', jcall(in_, 'nextInt'))
        Code08_Candy1.k = jcast('int', jcall(in_, 'nextInt'))
        Code08_Candy1.m = jcast('int', 0)
        i = jcast('int', 1)
        op = 0
        u = 0
        v = 0
        while (i <= Code08_Candy1.k):
            op = jcast('int', jcall(in_, 'nextInt'))
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                jset(Code08_Candy1.a, ((_java_obj_22 := Code08_Candy1), (_java_key_23 := 'm'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))))[3], u)
                Code08_Candy1.b[Code08_Candy1.m] = jcast('int', v)
                Code08_Candy1.c[Code08_Candy1.m] = jcast('int', 0)
                jset(Code08_Candy1.a, ((_java_obj_25 := Code08_Candy1), (_java_key_26 := 'm'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3], v)
                Code08_Candy1.b[Code08_Candy1.m] = jcast('int', u)
                Code08_Candy1.c[Code08_Candy1.m] = jcast('int', 0)
            else:
                if (op == 2):
                    jset(Code08_Candy1.a, ((_java_obj_28 := Code08_Candy1), (_java_key_29 := 'm'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))))[3], u)
                    Code08_Candy1.b[Code08_Candy1.m] = jcast('int', v)
                    Code08_Candy1.c[Code08_Candy1.m] = jcast('int', 1)
                else:
                    if (op == 3):
                        jset(Code08_Candy1.a, ((_java_obj_31 := Code08_Candy1), (_java_key_32 := 'm'), (_java_old_33 := jget(_java_obj_31, _java_key_32)), jset(_java_obj_31, _java_key_32, jcast('int', (_java_old_33 + (1)))))[3], v)
                        Code08_Candy1.b[Code08_Candy1.m] = jcast('int', u)
                        Code08_Candy1.c[Code08_Candy1.m] = jcast('int', 0)
                    else:
                        if (op == 4):
                            jset(Code08_Candy1.a, ((_java_obj_34 := Code08_Candy1), (_java_key_35 := 'm'), (_java_old_36 := jget(_java_obj_34, _java_key_35)), jset(_java_obj_34, _java_key_35, jcast('int', (_java_old_36 + (1)))))[3], v)
                            Code08_Candy1.b[Code08_Candy1.m] = jcast('int', u)
                            Code08_Candy1.c[Code08_Candy1.m] = jcast('int', 1)
                        else:
                            jset(Code08_Candy1.a, ((_java_obj_37 := Code08_Candy1), (_java_key_38 := 'm'), (_java_old_39 := jget(_java_obj_37, _java_key_38)), jset(_java_obj_37, _java_key_38, jcast('int', (_java_old_39 + (1)))))[3], u)
                            Code08_Candy1.b[Code08_Candy1.m] = jcast('int', v)
                            Code08_Candy1.c[Code08_Candy1.m] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code08_Candy1.m):
            Code08_Candy1.addEdge(Code08_Candy1.a[i], Code08_Candy1.b[i], Code08_Candy1.c[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code08_Candy1.n):
            if (Code08_Candy1.dfn[i] == 0):
                # tarjan1(i);
                Code08_Candy1.tarjan2(i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', Code08_Candy1.condense())
        if (not check):
            jcall(out, 'println', jcast('int', (-1)))
        else:
            ans = jcast('long', Code08_Candy1.dpOnDAG())
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
            return jcast('int', self.buffer[((_java_obj_40 := self), (_java_key_41 := 'ptr'), (_java_old_42 := jget(_java_obj_40, _java_key_41)), jset(_java_obj_40, _java_key_41, jcast('int', (_java_old_42 + (1)))), _java_old_42)[4]])

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
            raise TypeError("No matching overload for Code08_Candy1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code08_Candy1.MAXN = jcast('int', 100001)
Code08_Candy1.MAXM = jcast('int', 200001)
Code08_Candy1.n = jcast('int', 0)
Code08_Candy1.k = jcast('int', 0)
Code08_Candy1.m = jcast('int', 0)
Code08_Candy1.a = jarray('int', [Code08_Candy1.MAXM])
Code08_Candy1.b = jarray('int', [Code08_Candy1.MAXM])
Code08_Candy1.c = jarray('int', [Code08_Candy1.MAXM])
Code08_Candy1.head = jarray('int', [Code08_Candy1.MAXN])
Code08_Candy1.nxt = jarray('int', [Code08_Candy1.MAXM])
Code08_Candy1.to = jarray('int', [Code08_Candy1.MAXM])
Code08_Candy1.weight = jarray('int', [Code08_Candy1.MAXM])
Code08_Candy1.cntg = jcast('int', 0)
Code08_Candy1.dfn = jarray('int', [Code08_Candy1.MAXN])
Code08_Candy1.low = jarray('int', [Code08_Candy1.MAXN])
Code08_Candy1.cntd = jcast('int', 0)
Code08_Candy1.sta = jarray('int', [Code08_Candy1.MAXN])
Code08_Candy1.top = jcast('int', 0)
Code08_Candy1.belong = jarray('int', [Code08_Candy1.MAXN])
Code08_Candy1.sccSiz = jarray('int', [Code08_Candy1.MAXN])
Code08_Candy1.sccCnt = jcast('int', 0)
Code08_Candy1.indegree = jarray('int', [Code08_Candy1.MAXN])
Code08_Candy1.dp = jarray('long', [Code08_Candy1.MAXN])
Code08_Candy1.stack = jarray('int', [Code08_Candy1.MAXN, 3])
Code08_Candy1.u = jcast('int', 0)
Code08_Candy1.status = jcast('int', 0)
Code08_Candy1.e = jcast('int', 0)
Code08_Candy1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code08_Candy1.main([])
