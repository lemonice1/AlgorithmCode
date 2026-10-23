# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 缩点结合动态规划模版题，Python版
# 给定一张n个点，m条边的有向图，每个点给定非负点权
# 如果重复经过一个点，点权只获得一次
# 找到一条路径，使得点权累加和最大，打印这个值
# 1 <= n <= 10^4
# 1 <= m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3387
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_CondenseTopo1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'arr': 'arr', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sum': 'sum', 'sccCnt': 'sccCnt', 'indegree': 'indegree', 'que': 'que', 'dp': 'dp'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
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
    sccCnt = 0
    indegree = None
    que = None
    dp = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_CondenseTopo1.nxt, ((_java_obj_1 := Code01_CondenseTopo1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_CondenseTopo1.head[u])
        Code01_CondenseTopo1.to[Code01_CondenseTopo1.cntg] = jcast('int', v)
        Code01_CondenseTopo1.head[u] = jcast('int', Code01_CondenseTopo1.cntg)

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code01_CondenseTopo1.dfn, u, jset(Code01_CondenseTopo1.low, u, ((_java_obj_4 := Code01_CondenseTopo1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code01_CondenseTopo1.sta, ((_java_obj_7 := Code01_CondenseTopo1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code01_CondenseTopo1.head[u])
        while (e > 0):
            v = jcast('int', Code01_CondenseTopo1.to[e])
            if (Code01_CondenseTopo1.dfn[v] == 0):
                Code01_CondenseTopo1.tarjan(v)
                jset(Code01_CondenseTopo1.low, u, jstatic('Math', 'min', Code01_CondenseTopo1.low[u], Code01_CondenseTopo1.low[v]))
            else:
                if (Code01_CondenseTopo1.belong[v] == 0):
                    jset(Code01_CondenseTopo1.low, u, jstatic('Math', 'min', Code01_CondenseTopo1.low[u], Code01_CondenseTopo1.dfn[v]))
            e = jcast('int', Code01_CondenseTopo1.nxt[e])
        if (Code01_CondenseTopo1.dfn[u] == Code01_CondenseTopo1.low[u]):
            Code01_CondenseTopo1.sccCnt = jcast('int', (Code01_CondenseTopo1.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code01_CondenseTopo1.sta[((_java_obj_10 := Code01_CondenseTopo1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code01_CondenseTopo1.belong[pop] = jcast('int', Code01_CondenseTopo1.sccCnt)
                Code01_CondenseTopo1.sum[Code01_CondenseTopo1.sccCnt] = jcast('int', jcast('int', jadd(Code01_CondenseTopo1.sum[Code01_CondenseTopo1.sccCnt], Code01_CondenseTopo1.arr[pop])))
                if not ((pop != u)):
                    break

    @staticmethod
    def condense():
        Code01_CondenseTopo1.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code01_CondenseTopo1.sccCnt):
            Code01_CondenseTopo1.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_CondenseTopo1.m):
            scc1 = jcast('int', Code01_CondenseTopo1.belong[Code01_CondenseTopo1.a[i]])
            scc2 = jcast('int', Code01_CondenseTopo1.belong[Code01_CondenseTopo1.b[i]])
            if (scc1 != scc2):
                Code01_CondenseTopo1.indegree[scc2] = jcast('int', (Code01_CondenseTopo1.indegree[scc2] + 1))
                Code01_CondenseTopo1.addEdge(scc1, scc2)
            i = jcast('int', (i + 1))

    # 拓扑排序的写法
    @staticmethod
    def topo():
        l = jcast('int', 1)
        r = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code01_CondenseTopo1.sccCnt):
            if (Code01_CondenseTopo1.indegree[i] == 0):
                Code01_CondenseTopo1.dp[i] = jcast('int', Code01_CondenseTopo1.sum[i])
                jset(Code01_CondenseTopo1.que, (r := jcast('int', (r + (1)))), i)
            i = jcast('int', (i + 1))
        while (l <= r):
            u = jcast('int', Code01_CondenseTopo1.que[((_java_old_13 := l), (l := jcast('int', (l + (1)))), _java_old_13)[2]])
            e = jcast('int', Code01_CondenseTopo1.head[u])
            while (e > 0):
                v = jcast('int', Code01_CondenseTopo1.to[e])
                jset(Code01_CondenseTopo1.dp, v, jstatic('Math', 'max', Code01_CondenseTopo1.dp[v], jcast('int', jadd(Code01_CondenseTopo1.dp[u], Code01_CondenseTopo1.sum[v]))))
                if (((_java_obj_14 := Code01_CondenseTopo1.indegree), (_java_key_15 := v), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (-1)))))[3] == 0):
                    jset(Code01_CondenseTopo1.que, (r := jcast('int', (r + (1)))), v)
                e = jcast('int', Code01_CondenseTopo1.nxt[e])
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code01_CondenseTopo1.sccCnt):
            ans = jcast('int', jstatic('Math', 'max', ans, Code01_CondenseTopo1.dp[i]))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 直接转移的写法
    @staticmethod
    def dpOnDAG():
        u = jcast('int', Code01_CondenseTopo1.sccCnt)
        while (u > 0):
            if (Code01_CondenseTopo1.indegree[u] == 0):
                Code01_CondenseTopo1.dp[u] = jcast('int', Code01_CondenseTopo1.sum[u])
            e = jcast('int', Code01_CondenseTopo1.head[u])
            while (e > 0):
                v = jcast('int', Code01_CondenseTopo1.to[e])
                jset(Code01_CondenseTopo1.dp, v, jstatic('Math', 'max', Code01_CondenseTopo1.dp[v], jcast('int', jadd(Code01_CondenseTopo1.dp[u], Code01_CondenseTopo1.sum[v]))))
                e = jcast('int', Code01_CondenseTopo1.nxt[e])
            u = jcast('int', (u - 1))
        ans = jcast('int', 0)
        u = jcast('int', 1)
        while (u <= Code01_CondenseTopo1.sccCnt):
            ans = jcast('int', jstatic('Math', 'max', ans, Code01_CondenseTopo1.dp[u]))
            u = jcast('int', (u + 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code01_CondenseTopo1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_CondenseTopo1.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_CondenseTopo1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_CondenseTopo1.n):
            jset(Code01_CondenseTopo1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_CondenseTopo1.m):
            jset(Code01_CondenseTopo1.a, i, jcall(in_, 'nextInt'))
            jset(Code01_CondenseTopo1.b, i, jcall(in_, 'nextInt'))
            Code01_CondenseTopo1.addEdge(Code01_CondenseTopo1.a[i], Code01_CondenseTopo1.b[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_CondenseTopo1.n):
            if (Code01_CondenseTopo1.dfn[i] == 0):
                Code01_CondenseTopo1.tarjan(i)
            i = jcast('int', (i + 1))
        Code01_CondenseTopo1.condense()
        # int ans = topo();
        ans = jcast('int', Code01_CondenseTopo1.dpOnDAG())
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
            return jcast('int', self.buffer[((_java_obj_17 := self), (_java_key_18 := 'ptr'), (_java_old_19 := jget(_java_obj_17, _java_key_18)), jset(_java_obj_17, _java_key_18, jcast('int', (_java_old_19 + (1)))), _java_old_19)[4]])

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
            raise TypeError("No matching overload for Code01_CondenseTopo1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_CondenseTopo1.MAXN = jcast('int', 10001)
Code01_CondenseTopo1.MAXM = jcast('int', 100001)
Code01_CondenseTopo1.n = jcast('int', 0)
Code01_CondenseTopo1.m = jcast('int', 0)
Code01_CondenseTopo1.arr = jarray('int', [Code01_CondenseTopo1.MAXN])
Code01_CondenseTopo1.a = jarray('int', [Code01_CondenseTopo1.MAXM])
Code01_CondenseTopo1.b = jarray('int', [Code01_CondenseTopo1.MAXM])
Code01_CondenseTopo1.head = jarray('int', [Code01_CondenseTopo1.MAXN])
Code01_CondenseTopo1.nxt = jarray('int', [Code01_CondenseTopo1.MAXM])
Code01_CondenseTopo1.to = jarray('int', [Code01_CondenseTopo1.MAXM])
Code01_CondenseTopo1.cntg = jcast('int', 0)
Code01_CondenseTopo1.dfn = jarray('int', [Code01_CondenseTopo1.MAXN])
Code01_CondenseTopo1.low = jarray('int', [Code01_CondenseTopo1.MAXN])
Code01_CondenseTopo1.cntd = jcast('int', 0)
Code01_CondenseTopo1.sta = jarray('int', [Code01_CondenseTopo1.MAXN])
Code01_CondenseTopo1.top = jcast('int', 0)
Code01_CondenseTopo1.belong = jarray('int', [Code01_CondenseTopo1.MAXN])
Code01_CondenseTopo1.sum = jarray('int', [Code01_CondenseTopo1.MAXN])
Code01_CondenseTopo1.sccCnt = jcast('int', 0)
Code01_CondenseTopo1.indegree = jarray('int', [Code01_CondenseTopo1.MAXN])
Code01_CondenseTopo1.que = jarray('int', [Code01_CondenseTopo1.MAXN])
Code01_CondenseTopo1.dp = jarray('int', [Code01_CondenseTopo1.MAXN])

if __name__ == '__main__':
    Code01_CondenseTopo1.main([])
