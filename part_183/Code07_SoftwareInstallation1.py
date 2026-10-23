# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 软件安装，Python版
# 一共有n个物品，你的背包能容纳的总重量为m
# 选择某个物品时，重量消耗为当前物品的w，获得收益为当前物品的v
# 给定每个物品最多一件依赖物品，不拿依赖物品无法选择当前物品
# 如果一批物品循环依赖，想选的话就只能都选，有的物品不存在依赖物品
# 打印你能获得的最大收益
# 0 <= n <= 100
# 0 <= m <= 500
# 测试链接 : https://www.luogu.com.cn/problem/P2515
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_SoftwareInstallation1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'w': 'w', 'v': 'v', 'depend': 'depend', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'wsum': 'wsum', 'vsum': 'vsum', 'sccCnt': 'sccCnt', 'indegree': 'indegree', 'siz': 'siz', 'weight': 'weight', 'value': 'value', 'dfnCnt': 'dfnCnt', 'dp': 'dp'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    w = None
    v = None
    depend = None
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
    wsum = None
    vsum = None
    sccCnt = 0
    indegree = None
    # 树上背包最优解，来自讲解079，题目5
    siz = None
    weight = None
    value = None
    dfnCnt = 0
    dp = None
    @staticmethod
    def addEdge(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        jset(Code07_SoftwareInstallation1.nxt, ((_java_obj_1 := Code07_SoftwareInstallation1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_SoftwareInstallation1.head[a])
        Code07_SoftwareInstallation1.to[Code07_SoftwareInstallation1.cntg] = jcast('int', b)
        Code07_SoftwareInstallation1.head[a] = jcast('int', Code07_SoftwareInstallation1.cntg)

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code07_SoftwareInstallation1.dfn, u, jset(Code07_SoftwareInstallation1.low, u, ((_java_obj_4 := Code07_SoftwareInstallation1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code07_SoftwareInstallation1.sta, ((_java_obj_7 := Code07_SoftwareInstallation1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code07_SoftwareInstallation1.head[u])
        while (e > 0):
            v = jcast('int', Code07_SoftwareInstallation1.to[e])
            if (Code07_SoftwareInstallation1.dfn[v] == 0):
                Code07_SoftwareInstallation1.tarjan(v)
                jset(Code07_SoftwareInstallation1.low, u, jstatic('Math', 'min', Code07_SoftwareInstallation1.low[u], Code07_SoftwareInstallation1.low[v]))
            else:
                if (Code07_SoftwareInstallation1.belong[v] == 0):
                    jset(Code07_SoftwareInstallation1.low, u, jstatic('Math', 'min', Code07_SoftwareInstallation1.low[u], Code07_SoftwareInstallation1.dfn[v]))
            e = jcast('int', Code07_SoftwareInstallation1.nxt[e])
        if (Code07_SoftwareInstallation1.dfn[u] == Code07_SoftwareInstallation1.low[u]):
            Code07_SoftwareInstallation1.sccCnt = jcast('int', (Code07_SoftwareInstallation1.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code07_SoftwareInstallation1.sta[((_java_obj_10 := Code07_SoftwareInstallation1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code07_SoftwareInstallation1.belong[pop] = jcast('int', Code07_SoftwareInstallation1.sccCnt)
                Code07_SoftwareInstallation1.wsum[Code07_SoftwareInstallation1.sccCnt] = jcast('int', jcast('int', jadd(Code07_SoftwareInstallation1.wsum[Code07_SoftwareInstallation1.sccCnt], Code07_SoftwareInstallation1.w[pop])))
                Code07_SoftwareInstallation1.vsum[Code07_SoftwareInstallation1.sccCnt] = jcast('int', jcast('int', jadd(Code07_SoftwareInstallation1.vsum[Code07_SoftwareInstallation1.sccCnt], Code07_SoftwareInstallation1.v[pop])))
                if not ((pop != u)):
                    break

    @staticmethod
    def condense():
        Code07_SoftwareInstallation1.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code07_SoftwareInstallation1.sccCnt):
            Code07_SoftwareInstallation1.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_SoftwareInstallation1.n):
            if (Code07_SoftwareInstallation1.depend[i] > 0):
                scc1 = jcast('int', Code07_SoftwareInstallation1.belong[Code07_SoftwareInstallation1.depend[i]])
                scc2 = jcast('int', Code07_SoftwareInstallation1.belong[i])
                if (scc1 != scc2):
                    Code07_SoftwareInstallation1.indegree[scc2] = jcast('int', (Code07_SoftwareInstallation1.indegree[scc2] + 1))
                    Code07_SoftwareInstallation1.addEdge(scc1, scc2)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_SoftwareInstallation1.sccCnt):
            if (Code07_SoftwareInstallation1.indegree[i] == 0):
                Code07_SoftwareInstallation1.addEdge(0, i)
            i = jcast('int', (i + 1))

    # 缩点后的树，每个节点重新分配dfn序号
    @staticmethod
    def dfs(u):
        u = jcast('int', u)
        i = jcast('int', ((_java_obj_13 := Code07_SoftwareInstallation1), (_java_key_14 := 'dfnCnt'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
        Code07_SoftwareInstallation1.siz[i] = jcast('int', 1)
        Code07_SoftwareInstallation1.weight[i] = jcast('int', Code07_SoftwareInstallation1.wsum[u])
        Code07_SoftwareInstallation1.value[i] = jcast('int', Code07_SoftwareInstallation1.vsum[u])
        e = jcast('int', Code07_SoftwareInstallation1.head[u])
        while (e > 0):
            v = jcast('int', Code07_SoftwareInstallation1.to[e])
            ((_java_obj_16 := Code07_SoftwareInstallation1.siz), (_java_key_17 := i), jset(_java_obj_16, _java_key_17, jcast('int', jadd(jget(_java_obj_16, _java_key_17), Code07_SoftwareInstallation1.dfs(v)))))[2]
            e = jcast('int', Code07_SoftwareInstallation1.nxt[e])
        return jcast('int', Code07_SoftwareInstallation1.siz[i])

    # 树上01背包最优解
    # 讲解079，题目5，树上背包最优解，讲的非常清楚
    @staticmethod
    def knapsackOnTree():
        Code07_SoftwareInstallation1.dfs(0)
        i = jcast('int', Code07_SoftwareInstallation1.dfnCnt)
        while (i >= 2):
            j = jcast('int', 1)
            while (j <= Code07_SoftwareInstallation1.m):
                jset(Code07_SoftwareInstallation1.dp[i], j, Code07_SoftwareInstallation1.dp[jcast('int', jadd(i, Code07_SoftwareInstallation1.siz[i]))][j])
                if (jcast('int', (j - Code07_SoftwareInstallation1.weight[i])) >= 0):
                    jset(Code07_SoftwareInstallation1.dp[i], j, jstatic('Math', 'max', Code07_SoftwareInstallation1.dp[i][j], jcast('int', jadd(Code07_SoftwareInstallation1.value[i], Code07_SoftwareInstallation1.dp[jcast('int', jadd(i, 1))][jcast('int', (j - Code07_SoftwareInstallation1.weight[i]))]))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i - 1))
        return jcast('int', Code07_SoftwareInstallation1.dp[2][Code07_SoftwareInstallation1.m])

    @staticmethod
    def main(args):
        in_ = Code07_SoftwareInstallation1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_SoftwareInstallation1.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_SoftwareInstallation1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_SoftwareInstallation1.n):
            jset(Code07_SoftwareInstallation1.w, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_SoftwareInstallation1.n):
            jset(Code07_SoftwareInstallation1.v, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_SoftwareInstallation1.n):
            jset(Code07_SoftwareInstallation1.depend, i, jcall(in_, 'nextInt'))
            if (Code07_SoftwareInstallation1.depend[i] > 0):
                Code07_SoftwareInstallation1.addEdge(Code07_SoftwareInstallation1.depend[i], i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_SoftwareInstallation1.n):
            if (Code07_SoftwareInstallation1.dfn[i] == 0):
                Code07_SoftwareInstallation1.tarjan(i)
            i = jcast('int', (i + 1))
        Code07_SoftwareInstallation1.condense()
        ans = jcast('int', Code07_SoftwareInstallation1.knapsackOnTree())
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
            return jcast('int', self.buffer[((_java_obj_18 := self), (_java_key_19 := 'ptr'), (_java_old_20 := jget(_java_obj_18, _java_key_19)), jset(_java_obj_18, _java_key_19, jcast('int', (_java_old_20 + (1)))), _java_old_20)[4]])

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
            raise TypeError("No matching overload for Code07_SoftwareInstallation1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_SoftwareInstallation1.MAXN = jcast('int', 301)
Code07_SoftwareInstallation1.MAXM = jcast('int', 601)
Code07_SoftwareInstallation1.n = jcast('int', 0)
Code07_SoftwareInstallation1.m = jcast('int', 0)
Code07_SoftwareInstallation1.w = jarray('int', [Code07_SoftwareInstallation1.MAXN])
Code07_SoftwareInstallation1.v = jarray('int', [Code07_SoftwareInstallation1.MAXN])
Code07_SoftwareInstallation1.depend = jarray('int', [Code07_SoftwareInstallation1.MAXN])
Code07_SoftwareInstallation1.head = jarray('int', [Code07_SoftwareInstallation1.MAXN])
Code07_SoftwareInstallation1.nxt = jarray('int', [Code07_SoftwareInstallation1.MAXN])
Code07_SoftwareInstallation1.to = jarray('int', [Code07_SoftwareInstallation1.MAXN])
Code07_SoftwareInstallation1.cntg = jcast('int', 0)
Code07_SoftwareInstallation1.dfn = jarray('int', [Code07_SoftwareInstallation1.MAXN])
Code07_SoftwareInstallation1.low = jarray('int', [Code07_SoftwareInstallation1.MAXN])
Code07_SoftwareInstallation1.cntd = jcast('int', 0)
Code07_SoftwareInstallation1.sta = jarray('int', [Code07_SoftwareInstallation1.MAXN])
Code07_SoftwareInstallation1.top = jcast('int', 0)
Code07_SoftwareInstallation1.belong = jarray('int', [Code07_SoftwareInstallation1.MAXN])
Code07_SoftwareInstallation1.wsum = jarray('int', [Code07_SoftwareInstallation1.MAXN])
Code07_SoftwareInstallation1.vsum = jarray('int', [Code07_SoftwareInstallation1.MAXN])
Code07_SoftwareInstallation1.sccCnt = jcast('int', 0)
Code07_SoftwareInstallation1.indegree = jarray('int', [Code07_SoftwareInstallation1.MAXN])
Code07_SoftwareInstallation1.siz = jarray('int', [Code07_SoftwareInstallation1.MAXN])
Code07_SoftwareInstallation1.weight = jarray('int', [Code07_SoftwareInstallation1.MAXN])
Code07_SoftwareInstallation1.value = jarray('int', [Code07_SoftwareInstallation1.MAXN])
Code07_SoftwareInstallation1.dfnCnt = jcast('int', 0)
Code07_SoftwareInstallation1.dp = jarray('int', [Code07_SoftwareInstallation1.MAXN, Code07_SoftwareInstallation1.MAXM])

if __name__ == '__main__':
    Code07_SoftwareInstallation1.main([])
