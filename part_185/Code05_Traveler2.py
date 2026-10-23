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

# 旅行家，Python版
# 给定一张无向图，一共n个点、m条边，每个点给定点权，保证所有点连通
# 一条路径要求，点可以重复经过，边不能重复经过
# 一共有q条操作，格式 x y : 从点x到点y所有可能的路径都走一遍
# 一共q条操作，可能涉及非常多的路径，如果一条路径通过了某个点
# 该点的点权就算入收益，但是以后再有其他路径通过该点，不重复获得收益
# 打印总收益是多少
# 1 <= n <= 5 * 10^5
# 1 <= m <= 2 * 10^6
# 1 <= q <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P7924
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Traveler2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'q': 'q', 'arr': 'arr', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sum': 'sum', 'ebccCnt': 'ebccCnt', 'lg2': 'lg2', 'rmq': 'rmq', 'useCnt': 'useCnt', 'stack': 'stack', 'u': 'u', 'preEdge': 'preEdge', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    MAXP = 0
    n = 0
    m = 0
    q = 0
    arr = None
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
    sum = None
    ebccCnt = 0
    lg2 = None
    rmq = None
    useCnt = None
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
        jset(Code05_Traveler2.stack[Code05_Traveler2.stacksize], 0, u)
        jset(Code05_Traveler2.stack[Code05_Traveler2.stacksize], 1, preEdge)
        jset(Code05_Traveler2.stack[Code05_Traveler2.stacksize], 2, status)
        jset(Code05_Traveler2.stack[Code05_Traveler2.stacksize], 3, e)
        Code05_Traveler2.stacksize = jcast('int', (Code05_Traveler2.stacksize + 1))

    @staticmethod
    def pop():
        Code05_Traveler2.stacksize = jcast('int', (Code05_Traveler2.stacksize - 1))
        Code05_Traveler2.u = jcast('int', Code05_Traveler2.stack[Code05_Traveler2.stacksize][0])
        Code05_Traveler2.preEdge = jcast('int', Code05_Traveler2.stack[Code05_Traveler2.stacksize][1])
        Code05_Traveler2.status = jcast('int', Code05_Traveler2.stack[Code05_Traveler2.stacksize][2])
        Code05_Traveler2.e = jcast('int', Code05_Traveler2.stack[Code05_Traveler2.stacksize][3])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_Traveler2.nxt, ((_java_obj_1 := Code05_Traveler2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_Traveler2.head[u])
        Code05_Traveler2.to[Code05_Traveler2.cntg] = jcast('int', v)
        Code05_Traveler2.head[u] = jcast('int', Code05_Traveler2.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code05_Traveler2.dfn, u, jset(Code05_Traveler2.low, u, ((_java_obj_4 := Code05_Traveler2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code05_Traveler2.sta, ((_java_obj_7 := Code05_Traveler2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code05_Traveler2.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code05_Traveler2.to[e])
                if (Code05_Traveler2.dfn[v] == 0):
                    Code05_Traveler2.tarjan1(v, e)
                    jset(Code05_Traveler2.low, u, jstatic('Math', 'min', Code05_Traveler2.low[u], Code05_Traveler2.low[v]))
                else:
                    jset(Code05_Traveler2.low, u, jstatic('Math', 'min', Code05_Traveler2.low[u], Code05_Traveler2.dfn[v]))
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
            e = jcast('int', Code05_Traveler2.nxt[e])
        if (Code05_Traveler2.dfn[u] == Code05_Traveler2.low[u]):
            Code05_Traveler2.ebccCnt = jcast('int', (Code05_Traveler2.ebccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code05_Traveler2.sta[((_java_obj_11 := Code05_Traveler2), (_java_key_12 := 'top'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (-1)))), _java_old_13)[4]])
                Code05_Traveler2.belong[pop] = jcast('int', Code05_Traveler2.ebccCnt)
                Code05_Traveler2.sum[Code05_Traveler2.ebccCnt] = jcast('int', jcast('int', jadd(Code05_Traveler2.sum[Code05_Traveler2.ebccCnt], Code05_Traveler2.arr[pop])))
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node, pree):
        node = jcast('int', node)
        pree = jcast('int', pree)
        Code05_Traveler2.stacksize = jcast('int', 0)
        Code05_Traveler2.push(node, pree, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code05_Traveler2.stacksize > 0):
            Code05_Traveler2.pop()
            if (Code05_Traveler2.status == jcast('int', (-1))):
                jset(Code05_Traveler2.dfn, Code05_Traveler2.u, jset(Code05_Traveler2.low, Code05_Traveler2.u, ((_java_obj_14 := Code05_Traveler2), (_java_key_15 := 'cntd'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))))[3]))
                jset(Code05_Traveler2.sta, ((_java_obj_17 := Code05_Traveler2), (_java_key_18 := 'top'), (_java_old_19 := jget(_java_obj_17, _java_key_18)), jset(_java_obj_17, _java_key_18, jcast('int', (_java_old_19 + (1)))))[3], Code05_Traveler2.u)
                Code05_Traveler2.e = jcast('int', Code05_Traveler2.head[Code05_Traveler2.u])
            else:
                v = jcast('int', Code05_Traveler2.to[Code05_Traveler2.e])
                if (Code05_Traveler2.status == 0):
                    jset(Code05_Traveler2.low, Code05_Traveler2.u, jstatic('Math', 'min', Code05_Traveler2.low[Code05_Traveler2.u], Code05_Traveler2.low[v]))
                else:
                    jset(Code05_Traveler2.low, Code05_Traveler2.u, jstatic('Math', 'min', Code05_Traveler2.low[Code05_Traveler2.u], Code05_Traveler2.dfn[v]))
                Code05_Traveler2.e = jcast('int', Code05_Traveler2.nxt[Code05_Traveler2.e])
            if (jcast('int', (Code05_Traveler2.e ^ 1)) == Code05_Traveler2.preEdge):
                Code05_Traveler2.e = jcast('int', Code05_Traveler2.nxt[Code05_Traveler2.e])
            if (Code05_Traveler2.e != 0):
                v = jcast('int', Code05_Traveler2.to[Code05_Traveler2.e])
                if (Code05_Traveler2.dfn[v] == 0):
                    Code05_Traveler2.push(Code05_Traveler2.u, Code05_Traveler2.preEdge, 0, Code05_Traveler2.e)
                    Code05_Traveler2.push(v, Code05_Traveler2.e, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code05_Traveler2.push(Code05_Traveler2.u, Code05_Traveler2.preEdge, 1, Code05_Traveler2.e)
            else:
                if (Code05_Traveler2.dfn[Code05_Traveler2.u] == Code05_Traveler2.low[Code05_Traveler2.u]):
                    Code05_Traveler2.ebccCnt = jcast('int', (Code05_Traveler2.ebccCnt + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code05_Traveler2.sta[((_java_obj_20 := Code05_Traveler2), (_java_key_21 := 'top'), (_java_old_22 := jget(_java_obj_20, _java_key_21)), jset(_java_obj_20, _java_key_21, jcast('int', (_java_old_22 + (-1)))), _java_old_22)[4]])
                        Code05_Traveler2.belong[pop] = jcast('int', Code05_Traveler2.ebccCnt)
                        Code05_Traveler2.sum[Code05_Traveler2.ebccCnt] = jcast('int', jcast('int', jadd(Code05_Traveler2.sum[Code05_Traveler2.ebccCnt], Code05_Traveler2.arr[pop])))
                        if not ((pop != Code05_Traveler2.u)):
                            break

    @staticmethod
    def condense():
        Code05_Traveler2.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code05_Traveler2.ebccCnt):
            Code05_Traveler2.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Traveler2.m):
            ebcc1 = jcast('int', Code05_Traveler2.belong[Code05_Traveler2.a[i]])
            ebcc2 = jcast('int', Code05_Traveler2.belong[Code05_Traveler2.b[i]])
            if (ebcc1 != ebcc2):
                Code05_Traveler2.addEdge(ebcc1, ebcc2)
                Code05_Traveler2.addEdge(ebcc2, ebcc1)
            i = jcast('int', (i + 1))

    @staticmethod
    def getUp(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('int', (x if (Code05_Traveler2.dfn[x] < Code05_Traveler2.dfn[y]) else y))

    @staticmethod
    def dfs(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code05_Traveler2.dfn, u, ((_java_obj_23 := Code05_Traveler2), (_java_key_24 := 'cntd'), (_java_old_25 := jget(_java_obj_23, _java_key_24)), jset(_java_obj_23, _java_key_24, jcast('int', (_java_old_25 + (1)))))[3])
        jset(Code05_Traveler2.rmq[Code05_Traveler2.dfn[u]], 0, fa)
        e = jcast('int', Code05_Traveler2.head[u])
        while (e > 0):
            v = jcast('int', Code05_Traveler2.to[e])
            if (v != fa):
                Code05_Traveler2.dfs(v, u)
            e = jcast('int', Code05_Traveler2.nxt[e])

    @staticmethod
    def buildRmq():
        Code05_Traveler2.cntd = jcast('int', 0)
        Code05_Traveler2.dfs(1, 0)
        i = jcast('int', 2)
        while (i <= Code05_Traveler2.ebccCnt):
            Code05_Traveler2.lg2[i] = jcast('int', jcast('int', jadd(Code05_Traveler2.lg2[jcast('int', (i >> (1 & 31)))], 1)))
            i = jcast('int', (i + 1))
        pre = jcast('int', 0)
        cur = jcast('int', 1)
        while (cur <= Code05_Traveler2.lg2[Code05_Traveler2.ebccCnt]):
            i = jcast('int', 1)
            while (jcast('int', (jcast('int', jadd(i, jcast('int', (1 << (cur & 31))))) - 1)) <= Code05_Traveler2.ebccCnt):
                jset(Code05_Traveler2.rmq[i], cur, Code05_Traveler2.getUp(Code05_Traveler2.rmq[i][pre], Code05_Traveler2.rmq[jcast('int', jadd(i, jcast('int', (1 << (pre & 31)))))][pre]))
                i = jcast('int', (i + 1))
            pre = jcast('int', (pre + 1))
            cur = jcast('int', (cur + 1))

    @staticmethod
    def getFather(x):
        x = jcast('int', x)
        return jcast('int', Code05_Traveler2.rmq[Code05_Traveler2.dfn[x]][0])

    @staticmethod
    def getLCA(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        if (x == y):
            return jcast('int', x)
        x = jcast('int', Code05_Traveler2.dfn[x])
        y = jcast('int', Code05_Traveler2.dfn[y])
        if (x > y):
            tmp = jcast('int', x)
            x = jcast('int', y)
            y = jcast('int', tmp)
        x = jcast('int', (x + 1))
        k = jcast('int', Code05_Traveler2.lg2[jcast('int', jadd(jcast('int', (y - x)), 1))])
        return jcast('int', Code05_Traveler2.getUp(Code05_Traveler2.rmq[x][k], Code05_Traveler2.rmq[jcast('int', jadd(jcast('int', (y - jcast('int', (1 << (k & 31))))), 1))][k]))

    @staticmethod
    def dfsOnTree(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        e = jcast('int', Code05_Traveler2.head[u])
        while (e > 0):
            v = jcast('int', Code05_Traveler2.to[e])
            if (v != fa):
                Code05_Traveler2.dfsOnTree(v, u)
                Code05_Traveler2.useCnt[u] = jcast('int', jcast('int', jadd(Code05_Traveler2.useCnt[u], Code05_Traveler2.useCnt[v])))
            e = jcast('int', Code05_Traveler2.nxt[e])

    @staticmethod
    def main(args):
        in_ = Code05_Traveler2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_Traveler2.cntg = jcast('int', 1)
        Code05_Traveler2.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_Traveler2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_Traveler2.n):
            jset(Code05_Traveler2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Traveler2.m):
            jset(Code05_Traveler2.a, i, jcall(in_, 'nextInt'))
            jset(Code05_Traveler2.b, i, jcall(in_, 'nextInt'))
            Code05_Traveler2.addEdge(Code05_Traveler2.a[i], Code05_Traveler2.b[i])
            Code05_Traveler2.addEdge(Code05_Traveler2.b[i], Code05_Traveler2.a[i])
            i = jcast('int', (i + 1))
        # tarjan1(1, 0);
        Code05_Traveler2.tarjan2(1, 0)
        Code05_Traveler2.condense()
        Code05_Traveler2.buildRmq()
        Code05_Traveler2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        y = 0
        xylca = 0
        lcafa = 0
        while (i <= Code05_Traveler2.q):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', Code05_Traveler2.belong[x])
            y = jcast('int', Code05_Traveler2.belong[y])
            xylca = jcast('int', Code05_Traveler2.getLCA(x, y))
            lcafa = jcast('int', Code05_Traveler2.getFather(xylca))
            Code05_Traveler2.useCnt[x] = jcast('int', (Code05_Traveler2.useCnt[x] + 1))
            Code05_Traveler2.useCnt[y] = jcast('int', (Code05_Traveler2.useCnt[y] + 1))
            Code05_Traveler2.useCnt[xylca] = jcast('int', (Code05_Traveler2.useCnt[xylca] - 1))
            Code05_Traveler2.useCnt[lcafa] = jcast('int', (Code05_Traveler2.useCnt[lcafa] - 1))
            i = jcast('int', (i + 1))
        Code05_Traveler2.dfsOnTree(1, 0)
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code05_Traveler2.ebccCnt):
            if (Code05_Traveler2.useCnt[i] > 0):
                ans = jcast('int', jcast('int', jadd(ans, Code05_Traveler2.sum[i])))
            i = jcast('int', (i + 1))
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
            return jcast('int', self.buffer[((_java_obj_26 := self), (_java_key_27 := 'ptr'), (_java_old_28 := jget(_java_obj_26, _java_key_27)), jset(_java_obj_26, _java_key_27, jcast('int', (_java_old_28 + (1)))), _java_old_28)[4]])

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
            raise TypeError("No matching overload for Code05_Traveler2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Traveler2.MAXN = jcast('int', 500001)
Code05_Traveler2.MAXM = jcast('int', 2000001)
Code05_Traveler2.MAXP = jcast('int', 20)
Code05_Traveler2.n = jcast('int', 0)
Code05_Traveler2.m = jcast('int', 0)
Code05_Traveler2.q = jcast('int', 0)
Code05_Traveler2.arr = jarray('int', [Code05_Traveler2.MAXN])
Code05_Traveler2.a = jarray('int', [Code05_Traveler2.MAXM])
Code05_Traveler2.b = jarray('int', [Code05_Traveler2.MAXM])
Code05_Traveler2.head = jarray('int', [Code05_Traveler2.MAXN])
Code05_Traveler2.nxt = jarray('int', [jcast('int', (Code05_Traveler2.MAXM << (1 & 31)))])
Code05_Traveler2.to = jarray('int', [jcast('int', (Code05_Traveler2.MAXM << (1 & 31)))])
Code05_Traveler2.cntg = jcast('int', 0)
Code05_Traveler2.dfn = jarray('int', [Code05_Traveler2.MAXN])
Code05_Traveler2.low = jarray('int', [Code05_Traveler2.MAXN])
Code05_Traveler2.cntd = jcast('int', 0)
Code05_Traveler2.sta = jarray('int', [Code05_Traveler2.MAXN])
Code05_Traveler2.top = jcast('int', 0)
Code05_Traveler2.belong = jarray('int', [Code05_Traveler2.MAXN])
Code05_Traveler2.sum = jarray('int', [Code05_Traveler2.MAXN])
Code05_Traveler2.ebccCnt = jcast('int', 0)
Code05_Traveler2.lg2 = jarray('int', [Code05_Traveler2.MAXN])
Code05_Traveler2.rmq = jarray('int', [Code05_Traveler2.MAXN, Code05_Traveler2.MAXP])
Code05_Traveler2.useCnt = jarray('int', [Code05_Traveler2.MAXN])
Code05_Traveler2.stack = jarray('int', [Code05_Traveler2.MAXN, 4])
Code05_Traveler2.u = jcast('int', 0)
Code05_Traveler2.preEdge = jcast('int', 0)
Code05_Traveler2.status = jcast('int', 0)
Code05_Traveler2.e = jcast('int', 0)
Code05_Traveler2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code05_Traveler2.main([])
