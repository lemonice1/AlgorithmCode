# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最优贸易，Python版
# 一共有n个城市，每个城市给定水晶球的销售价格，给定m条道路
# 格式 a b op : op为1代表a到b的单向路，否则表示双向路
# 你要从1号城市出发，可以任选道路，最终来到n号城市，沿途可以买卖一次水晶球
# 在途中你可以任选一座城市买入，可以立即卖出，或者在之后的任何城市卖出
# 如果从1号城市能到达n号城市，打印挣到的最大钱数，如果不能到达打印0
# 1 <= n <= 10^5
# 1 <= m <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P1073
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_OptimalTrade1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'INF': 'INF', 'n': 'n', 'm': 'm', 'val': 'val', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccMin': 'sccMin', 'sccMax': 'sccMax', 'sccCnt': 'sccCnt', 'premin': 'premin', 'dp': 'dp', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    INF = 0
    n = 0
    m = 0
    val = None
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
    sccMin = None
    sccMax = None
    sccCnt = 0
    premin = None
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
        jset(Code04_OptimalTrade1.stack[Code04_OptimalTrade1.stacksize], 0, u)
        jset(Code04_OptimalTrade1.stack[Code04_OptimalTrade1.stacksize], 1, status)
        jset(Code04_OptimalTrade1.stack[Code04_OptimalTrade1.stacksize], 2, e)
        Code04_OptimalTrade1.stacksize = jcast('int', (Code04_OptimalTrade1.stacksize + 1))

    @staticmethod
    def pop():
        Code04_OptimalTrade1.stacksize = jcast('int', (Code04_OptimalTrade1.stacksize - 1))
        Code04_OptimalTrade1.u = jcast('int', Code04_OptimalTrade1.stack[Code04_OptimalTrade1.stacksize][0])
        Code04_OptimalTrade1.status = jcast('int', Code04_OptimalTrade1.stack[Code04_OptimalTrade1.stacksize][1])
        Code04_OptimalTrade1.e = jcast('int', Code04_OptimalTrade1.stack[Code04_OptimalTrade1.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_OptimalTrade1.nxt, ((_java_obj_1 := Code04_OptimalTrade1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_OptimalTrade1.head[u])
        Code04_OptimalTrade1.to[Code04_OptimalTrade1.cntg] = jcast('int', v)
        Code04_OptimalTrade1.head[u] = jcast('int', Code04_OptimalTrade1.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code04_OptimalTrade1.dfn, u, jset(Code04_OptimalTrade1.low, u, ((_java_obj_4 := Code04_OptimalTrade1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code04_OptimalTrade1.sta, ((_java_obj_7 := Code04_OptimalTrade1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code04_OptimalTrade1.head[u])
        while (e > 0):
            v = jcast('int', Code04_OptimalTrade1.to[e])
            if (Code04_OptimalTrade1.dfn[v] == 0):
                Code04_OptimalTrade1.tarjan1(v)
                jset(Code04_OptimalTrade1.low, u, jstatic('Math', 'min', Code04_OptimalTrade1.low[u], Code04_OptimalTrade1.low[v]))
            else:
                if (Code04_OptimalTrade1.belong[v] == 0):
                    jset(Code04_OptimalTrade1.low, u, jstatic('Math', 'min', Code04_OptimalTrade1.low[u], Code04_OptimalTrade1.dfn[v]))
            e = jcast('int', Code04_OptimalTrade1.nxt[e])
        if (Code04_OptimalTrade1.dfn[u] == Code04_OptimalTrade1.low[u]):
            Code04_OptimalTrade1.sccCnt = jcast('int', (Code04_OptimalTrade1.sccCnt + 1))
            Code04_OptimalTrade1.sccMin[Code04_OptimalTrade1.sccCnt] = jcast('int', Code04_OptimalTrade1.INF)
            Code04_OptimalTrade1.sccMax[Code04_OptimalTrade1.sccCnt] = jcast('int', jcast('int', (-Code04_OptimalTrade1.INF)))
            pop = 0
            while True:
                pop = jcast('int', Code04_OptimalTrade1.sta[((_java_obj_10 := Code04_OptimalTrade1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code04_OptimalTrade1.belong[pop] = jcast('int', Code04_OptimalTrade1.sccCnt)
                jset(Code04_OptimalTrade1.sccMin, Code04_OptimalTrade1.sccCnt, jstatic('Math', 'min', Code04_OptimalTrade1.sccMin[Code04_OptimalTrade1.sccCnt], Code04_OptimalTrade1.val[pop]))
                jset(Code04_OptimalTrade1.sccMax, Code04_OptimalTrade1.sccCnt, jstatic('Math', 'max', Code04_OptimalTrade1.sccMax[Code04_OptimalTrade1.sccCnt], Code04_OptimalTrade1.val[pop]))
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code04_OptimalTrade1.stacksize = jcast('int', 0)
        Code04_OptimalTrade1.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code04_OptimalTrade1.stacksize > 0):
            Code04_OptimalTrade1.pop()
            if (Code04_OptimalTrade1.status == jcast('int', (-1))):
                jset(Code04_OptimalTrade1.dfn, Code04_OptimalTrade1.u, jset(Code04_OptimalTrade1.low, Code04_OptimalTrade1.u, ((_java_obj_13 := Code04_OptimalTrade1), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code04_OptimalTrade1.sta, ((_java_obj_16 := Code04_OptimalTrade1), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code04_OptimalTrade1.u)
                Code04_OptimalTrade1.e = jcast('int', Code04_OptimalTrade1.head[Code04_OptimalTrade1.u])
            else:
                v = jcast('int', Code04_OptimalTrade1.to[Code04_OptimalTrade1.e])
                if (Code04_OptimalTrade1.status == 0):
                    jset(Code04_OptimalTrade1.low, Code04_OptimalTrade1.u, jstatic('Math', 'min', Code04_OptimalTrade1.low[Code04_OptimalTrade1.u], Code04_OptimalTrade1.low[v]))
                if ((Code04_OptimalTrade1.status == 1) and (Code04_OptimalTrade1.belong[v] == 0)):
                    jset(Code04_OptimalTrade1.low, Code04_OptimalTrade1.u, jstatic('Math', 'min', Code04_OptimalTrade1.low[Code04_OptimalTrade1.u], Code04_OptimalTrade1.dfn[v]))
                Code04_OptimalTrade1.e = jcast('int', Code04_OptimalTrade1.nxt[Code04_OptimalTrade1.e])
            if (Code04_OptimalTrade1.e != 0):
                v = jcast('int', Code04_OptimalTrade1.to[Code04_OptimalTrade1.e])
                if (Code04_OptimalTrade1.dfn[v] == 0):
                    Code04_OptimalTrade1.push(Code04_OptimalTrade1.u, 0, Code04_OptimalTrade1.e)
                    Code04_OptimalTrade1.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code04_OptimalTrade1.push(Code04_OptimalTrade1.u, 1, Code04_OptimalTrade1.e)
            else:
                if (Code04_OptimalTrade1.dfn[Code04_OptimalTrade1.u] == Code04_OptimalTrade1.low[Code04_OptimalTrade1.u]):
                    Code04_OptimalTrade1.sccCnt = jcast('int', (Code04_OptimalTrade1.sccCnt + 1))
                    Code04_OptimalTrade1.sccMin[Code04_OptimalTrade1.sccCnt] = jcast('int', Code04_OptimalTrade1.INF)
                    Code04_OptimalTrade1.sccMax[Code04_OptimalTrade1.sccCnt] = jcast('int', jcast('int', (-Code04_OptimalTrade1.INF)))
                    pop = 0
                    while True:
                        pop = jcast('int', Code04_OptimalTrade1.sta[((_java_obj_19 := Code04_OptimalTrade1), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                        Code04_OptimalTrade1.belong[pop] = jcast('int', Code04_OptimalTrade1.sccCnt)
                        jset(Code04_OptimalTrade1.sccMin, Code04_OptimalTrade1.sccCnt, jstatic('Math', 'min', Code04_OptimalTrade1.sccMin[Code04_OptimalTrade1.sccCnt], Code04_OptimalTrade1.val[pop]))
                        jset(Code04_OptimalTrade1.sccMax, Code04_OptimalTrade1.sccCnt, jstatic('Math', 'max', Code04_OptimalTrade1.sccMax[Code04_OptimalTrade1.sccCnt], Code04_OptimalTrade1.val[pop]))
                        if not ((pop != Code04_OptimalTrade1.u)):
                            break

    @staticmethod
    def condense():
        Code04_OptimalTrade1.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_OptimalTrade1.sccCnt):
            Code04_OptimalTrade1.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_OptimalTrade1.m):
            scc1 = jcast('int', Code04_OptimalTrade1.belong[Code04_OptimalTrade1.a[i]])
            scc2 = jcast('int', Code04_OptimalTrade1.belong[Code04_OptimalTrade1.b[i]])
            if (((scc1 > 0) and (scc2 > 0)) and (scc1 != scc2)):
                Code04_OptimalTrade1.addEdge(scc1, scc2)
            i = jcast('int', (i + 1))

    @staticmethod
    def dpOnDAG():
        u = jcast('int', 1)
        while (u <= Code04_OptimalTrade1.sccCnt):
            Code04_OptimalTrade1.premin[u] = jcast('int', Code04_OptimalTrade1.INF)
            Code04_OptimalTrade1.dp[u] = jcast('int', jcast('int', (-Code04_OptimalTrade1.INF)))
            u = jcast('int', (u + 1))
        s = jcast('int', Code04_OptimalTrade1.belong[1])
        Code04_OptimalTrade1.premin[s] = jcast('int', Code04_OptimalTrade1.sccMin[s])
        Code04_OptimalTrade1.dp[s] = jcast('int', jcast('int', (Code04_OptimalTrade1.sccMax[s] - Code04_OptimalTrade1.sccMin[s])))
        u = jcast('int', Code04_OptimalTrade1.sccCnt)
        while (u > 0):
            e = jcast('int', Code04_OptimalTrade1.head[u])
            while (e > 0):
                v = jcast('int', Code04_OptimalTrade1.to[e])
                jset(Code04_OptimalTrade1.premin, v, jstatic('Math', 'min', Code04_OptimalTrade1.premin[v], jstatic('Math', 'min', Code04_OptimalTrade1.premin[u], Code04_OptimalTrade1.sccMin[v])))
                jset(Code04_OptimalTrade1.dp, v, jstatic('Math', 'max', Code04_OptimalTrade1.dp[v], jstatic('Math', 'max', Code04_OptimalTrade1.dp[u], jcast('int', (Code04_OptimalTrade1.sccMax[v] - Code04_OptimalTrade1.premin[v])))))
                e = jcast('int', Code04_OptimalTrade1.nxt[e])
            u = jcast('int', (u - 1))
        return jcast('int', Code04_OptimalTrade1.dp[Code04_OptimalTrade1.belong[Code04_OptimalTrade1.n]])

    @staticmethod
    def main(args):
        in_ = Code04_OptimalTrade1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_OptimalTrade1.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_OptimalTrade1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_OptimalTrade1.n):
            jset(Code04_OptimalTrade1.val, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        while (i <= Code04_OptimalTrade1.m):
            jset(Code04_OptimalTrade1.a, i, jcall(in_, 'nextInt'))
            jset(Code04_OptimalTrade1.b, i, jcall(in_, 'nextInt'))
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                Code04_OptimalTrade1.addEdge(Code04_OptimalTrade1.a[i], Code04_OptimalTrade1.b[i])
            else:
                Code04_OptimalTrade1.addEdge(Code04_OptimalTrade1.a[i], Code04_OptimalTrade1.b[i])
                Code04_OptimalTrade1.addEdge(Code04_OptimalTrade1.b[i], Code04_OptimalTrade1.a[i])
            i = jcast('int', (i + 1))
        # tarjan1(1);
        Code04_OptimalTrade1.tarjan2(1)
        if (Code04_OptimalTrade1.belong[Code04_OptimalTrade1.n] == 0):
            jcall(out, 'println', 0)
        else:
            Code04_OptimalTrade1.condense()
            ans = jcast('int', Code04_OptimalTrade1.dpOnDAG())
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
            return jcast('int', self.buffer[((_java_obj_22 := self), (_java_key_23 := 'ptr'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))), _java_old_24)[4]])

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
            raise TypeError("No matching overload for Code04_OptimalTrade1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_OptimalTrade1.MAXN = jcast('int', 100001)
Code04_OptimalTrade1.MAXM = jcast('int', 500001)
Code04_OptimalTrade1.INF = jcast('int', 1000000001)
Code04_OptimalTrade1.n = jcast('int', 0)
Code04_OptimalTrade1.m = jcast('int', 0)
Code04_OptimalTrade1.val = jarray('int', [Code04_OptimalTrade1.MAXN])
Code04_OptimalTrade1.a = jarray('int', [Code04_OptimalTrade1.MAXM])
Code04_OptimalTrade1.b = jarray('int', [Code04_OptimalTrade1.MAXM])
Code04_OptimalTrade1.head = jarray('int', [Code04_OptimalTrade1.MAXN])
Code04_OptimalTrade1.nxt = jarray('int', [jcast('int', (Code04_OptimalTrade1.MAXM << (1 & 31)))])
Code04_OptimalTrade1.to = jarray('int', [jcast('int', (Code04_OptimalTrade1.MAXM << (1 & 31)))])
Code04_OptimalTrade1.cntg = jcast('int', 0)
Code04_OptimalTrade1.dfn = jarray('int', [Code04_OptimalTrade1.MAXN])
Code04_OptimalTrade1.low = jarray('int', [Code04_OptimalTrade1.MAXN])
Code04_OptimalTrade1.cntd = jcast('int', 0)
Code04_OptimalTrade1.sta = jarray('int', [Code04_OptimalTrade1.MAXN])
Code04_OptimalTrade1.top = jcast('int', 0)
Code04_OptimalTrade1.belong = jarray('int', [Code04_OptimalTrade1.MAXN])
Code04_OptimalTrade1.sccMin = jarray('int', [Code04_OptimalTrade1.MAXN])
Code04_OptimalTrade1.sccMax = jarray('int', [Code04_OptimalTrade1.MAXN])
Code04_OptimalTrade1.sccCnt = jcast('int', 0)
Code04_OptimalTrade1.premin = jarray('int', [Code04_OptimalTrade1.MAXN])
Code04_OptimalTrade1.dp = jarray('int', [Code04_OptimalTrade1.MAXN])
Code04_OptimalTrade1.stack = jarray('int', [Code04_OptimalTrade1.MAXN, 3])
Code04_OptimalTrade1.u = jcast('int', 0)
Code04_OptimalTrade1.status = jcast('int', 0)
Code04_OptimalTrade1.e = jcast('int', 0)
Code04_OptimalTrade1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code04_OptimalTrade1.main([])
