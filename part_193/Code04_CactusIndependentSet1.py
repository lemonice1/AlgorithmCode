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

# 仙人掌最大独立集，Python版
# 给定n个点、m条边的无向连通图，输入保证图是仙人掌
# 你可以选择一些点，但是图中任意相邻两点不能同时选择
# 计算能得到的最大点权累加和
# 第一个测试链接，给定每个点的点权
# 第二个测试链接，认为每个点的点权是1
# 1 <= n <= 10^5
# 1 <= m <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4410
# 测试链接 : https://www.luogu.com.cn/problem/P10779
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_CactusIndependentSet1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'INF': 'INF', 'n': 'n', 'm': 'm', 'arr': 'arr', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'cycle': 'cycle', 'dp': 'dp', 'stau': 'stau', 'stap': 'stap', 'stas': 'stas', 'stae': 'stae', 'u': 'u', 'preEdge': 'preEdge', 'status': 'status', 'e': 'e', 'stacksiz': 'stacksiz'}
    MAXN = 0
    MAXM = 0
    INF = 0
    n = 0
    m = 0
    arr = None
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    # 收集环上的节点，不包含环顶
    cycle = None
    # dp[u][0] : 以u为头的子仙人掌中，不选u的情况下，获得的最大收益
    # dp[u][1] : 以u为头的子仙人掌中，选u的情况下，获得的最大收益
    dp = None
    # 递归改迭代需要的栈
    stau = None
    stap = None
    stas = None
    stae = None
    u = 0
    preEdge = 0
    status = 0
    e = 0
    stacksiz = 0
    @staticmethod
    def push(u, preEdge, status, e):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        status = jcast('int', status)
        e = jcast('int', e)
        Code04_CactusIndependentSet1.stau[Code04_CactusIndependentSet1.stacksiz] = jcast('int', u)
        Code04_CactusIndependentSet1.stap[Code04_CactusIndependentSet1.stacksiz] = jcast('int', preEdge)
        Code04_CactusIndependentSet1.stas[Code04_CactusIndependentSet1.stacksiz] = jcast('int', status)
        Code04_CactusIndependentSet1.stae[Code04_CactusIndependentSet1.stacksiz] = jcast('int', e)
        Code04_CactusIndependentSet1.stacksiz = jcast('int', (Code04_CactusIndependentSet1.stacksiz + 1))

    @staticmethod
    def pop():
        Code04_CactusIndependentSet1.stacksiz = jcast('int', (Code04_CactusIndependentSet1.stacksiz - 1))
        Code04_CactusIndependentSet1.u = jcast('int', Code04_CactusIndependentSet1.stau[Code04_CactusIndependentSet1.stacksiz])
        Code04_CactusIndependentSet1.preEdge = jcast('int', Code04_CactusIndependentSet1.stap[Code04_CactusIndependentSet1.stacksiz])
        Code04_CactusIndependentSet1.status = jcast('int', Code04_CactusIndependentSet1.stas[Code04_CactusIndependentSet1.stacksiz])
        Code04_CactusIndependentSet1.e = jcast('int', Code04_CactusIndependentSet1.stae[Code04_CactusIndependentSet1.stacksiz])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_CactusIndependentSet1.nxt, ((_java_obj_1 := Code04_CactusIndependentSet1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_CactusIndependentSet1.head[u])
        Code04_CactusIndependentSet1.to[Code04_CactusIndependentSet1.cntg] = jcast('int', v)
        Code04_CactusIndependentSet1.head[u] = jcast('int', Code04_CactusIndependentSet1.cntg)

    @staticmethod
    def dpOnCycle(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        siz = jcast('int', 0)
        pop = 0
        while True:
            pop = jcast('int', Code04_CactusIndependentSet1.sta[((_java_obj_4 := Code04_CactusIndependentSet1), (_java_key_5 := 'top'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))), _java_old_6)[4]])
            jset(Code04_CactusIndependentSet1.cycle, (siz := jcast('int', (siz + (1)))), pop)
            if not ((pop != v)):
                break
        # 不选u
        pre0 = jcast('int', Code04_CactusIndependentSet1.dp[Code04_CactusIndependentSet1.cycle[1]][0])
        pre1 = jcast('int', Code04_CactusIndependentSet1.dp[Code04_CactusIndependentSet1.cycle[1]][1])
        cur0 = 0
        cur1 = 0
        i = jcast('int', 2)
        while (i <= siz):
            x = jcast('int', Code04_CactusIndependentSet1.cycle[i])
            cur0 = jcast('int', jcast('int', jadd(jstatic('Math', 'max', pre0, pre1), Code04_CactusIndependentSet1.dp[x][0])))
            cur1 = jcast('int', jcast('int', jadd(pre0, Code04_CactusIndependentSet1.dp[x][1])))
            pre0 = jcast('int', cur0)
            pre1 = jcast('int', cur1)
            i = jcast('int', (i + 1))
        ((_java_obj_7 := Code04_CactusIndependentSet1.dp[u]), (_java_key_8 := 0), jset(_java_obj_7, _java_key_8, jcast('int', jadd(jget(_java_obj_7, _java_key_8), jstatic('Math', 'max', pre0, pre1)))))[2]
        # 选u
        pre0 = jcast('int', Code04_CactusIndependentSet1.dp[Code04_CactusIndependentSet1.cycle[1]][0])
        pre1 = jcast('int', jcast('int', (-Code04_CactusIndependentSet1.INF)))
        i = jcast('int', 2)
        while (i <= siz):
            x = jcast('int', Code04_CactusIndependentSet1.cycle[i])
            cur0 = jcast('int', jcast('int', jadd(jstatic('Math', 'max', pre0, pre1), Code04_CactusIndependentSet1.dp[x][0])))
            cur1 = jcast('int', jcast('int', jadd(pre0, Code04_CactusIndependentSet1.dp[x][1])))
            pre0 = jcast('int', cur0)
            pre1 = jcast('int', cur1)
            i = jcast('int', (i + 1))
        ((_java_obj_9 := Code04_CactusIndependentSet1.dp[u]), (_java_key_10 := 1), jset(_java_obj_9, _java_key_10, jcast('int', jadd(jget(_java_obj_9, _java_key_10), pre0))))[2]

    # 递归版
    @staticmethod
    def tarjan1(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code04_CactusIndependentSet1.dfn, u, jset(Code04_CactusIndependentSet1.low, u, ((_java_obj_11 := Code04_CactusIndependentSet1), (_java_key_12 := 'cntd'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))))[3]))
        jset(Code04_CactusIndependentSet1.sta, ((_java_obj_14 := Code04_CactusIndependentSet1), (_java_key_15 := 'top'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))))[3], u)
        jset(Code04_CactusIndependentSet1.dp[u], 0, 0)
        jset(Code04_CactusIndependentSet1.dp[u], 1, Code04_CactusIndependentSet1.arr[u])
        e = jcast('int', Code04_CactusIndependentSet1.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code04_CactusIndependentSet1.to[e])
                if (Code04_CactusIndependentSet1.dfn[v] == 0):
                    Code04_CactusIndependentSet1.tarjan1(v, e)
                    if (Code04_CactusIndependentSet1.low[v] < Code04_CactusIndependentSet1.dfn[u]):
                        jset(Code04_CactusIndependentSet1.low, u, jstatic('Math', 'min', Code04_CactusIndependentSet1.low[u], Code04_CactusIndependentSet1.low[v]))
                    else:
                        if (Code04_CactusIndependentSet1.low[v] > Code04_CactusIndependentSet1.dfn[u]):
                            ((_java_obj_18 := Code04_CactusIndependentSet1.dp[u]), (_java_key_19 := 0), jset(_java_obj_18, _java_key_19, jcast('int', jadd(jget(_java_obj_18, _java_key_19), jstatic('Math', 'max', Code04_CactusIndependentSet1.dp[v][0], Code04_CactusIndependentSet1.dp[v][1])))))[2]
                            ((_java_obj_20 := Code04_CactusIndependentSet1.dp[u]), (_java_key_21 := 1), jset(_java_obj_20, _java_key_21, jcast('int', jadd(jget(_java_obj_20, _java_key_21), Code04_CactusIndependentSet1.dp[v][0]))))[2]
                            Code04_CactusIndependentSet1.top = jcast('int', (Code04_CactusIndependentSet1.top - 1))
                        else:
                            Code04_CactusIndependentSet1.dpOnCycle(u, v)
                else:
                    if (Code04_CactusIndependentSet1.dfn[v] < Code04_CactusIndependentSet1.dfn[u]):
                        jset(Code04_CactusIndependentSet1.low, u, jstatic('Math', 'min', Code04_CactusIndependentSet1.low[u], Code04_CactusIndependentSet1.dfn[v]))
            except JContinue as _java_control_17:
                if _java_control_17.label not in (None,):
                    raise
            except JBreak as _java_control_17:
                if _java_control_17.label not in (None,):
                    raise
                break
            e = jcast('int', Code04_CactusIndependentSet1.nxt[e])

    # 迭代版
    @staticmethod
    def tarjan2(node, pree):
        node = jcast('int', node)
        pree = jcast('int', pree)
        Code04_CactusIndependentSet1.stacksiz = jcast('int', 0)
        Code04_CactusIndependentSet1.push(node, pree, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code04_CactusIndependentSet1.stacksiz > 0):
            Code04_CactusIndependentSet1.pop()
            if (Code04_CactusIndependentSet1.status == jcast('int', (-1))):
                jset(Code04_CactusIndependentSet1.dfn, Code04_CactusIndependentSet1.u, jset(Code04_CactusIndependentSet1.low, Code04_CactusIndependentSet1.u, ((_java_obj_22 := Code04_CactusIndependentSet1), (_java_key_23 := 'cntd'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))))[3]))
                jset(Code04_CactusIndependentSet1.sta, ((_java_obj_25 := Code04_CactusIndependentSet1), (_java_key_26 := 'top'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3], Code04_CactusIndependentSet1.u)
                jset(Code04_CactusIndependentSet1.dp[Code04_CactusIndependentSet1.u], 0, 0)
                jset(Code04_CactusIndependentSet1.dp[Code04_CactusIndependentSet1.u], 1, Code04_CactusIndependentSet1.arr[Code04_CactusIndependentSet1.u])
                Code04_CactusIndependentSet1.e = jcast('int', Code04_CactusIndependentSet1.head[Code04_CactusIndependentSet1.u])
            else:
                v = jcast('int', Code04_CactusIndependentSet1.to[Code04_CactusIndependentSet1.e])
                if (Code04_CactusIndependentSet1.status == 0):
                    if (Code04_CactusIndependentSet1.low[v] < Code04_CactusIndependentSet1.dfn[Code04_CactusIndependentSet1.u]):
                        jset(Code04_CactusIndependentSet1.low, Code04_CactusIndependentSet1.u, jstatic('Math', 'min', Code04_CactusIndependentSet1.low[Code04_CactusIndependentSet1.u], Code04_CactusIndependentSet1.low[v]))
                    else:
                        if (Code04_CactusIndependentSet1.low[v] > Code04_CactusIndependentSet1.dfn[Code04_CactusIndependentSet1.u]):
                            ((_java_obj_28 := Code04_CactusIndependentSet1.dp[Code04_CactusIndependentSet1.u]), (_java_key_29 := 0), jset(_java_obj_28, _java_key_29, jcast('int', jadd(jget(_java_obj_28, _java_key_29), jstatic('Math', 'max', Code04_CactusIndependentSet1.dp[v][0], Code04_CactusIndependentSet1.dp[v][1])))))[2]
                            ((_java_obj_30 := Code04_CactusIndependentSet1.dp[Code04_CactusIndependentSet1.u]), (_java_key_31 := 1), jset(_java_obj_30, _java_key_31, jcast('int', jadd(jget(_java_obj_30, _java_key_31), Code04_CactusIndependentSet1.dp[v][0]))))[2]
                            Code04_CactusIndependentSet1.top = jcast('int', (Code04_CactusIndependentSet1.top - 1))
                        else:
                            Code04_CactusIndependentSet1.dpOnCycle(Code04_CactusIndependentSet1.u, v)
                else:
                    if (Code04_CactusIndependentSet1.dfn[v] < Code04_CactusIndependentSet1.dfn[Code04_CactusIndependentSet1.u]):
                        jset(Code04_CactusIndependentSet1.low, Code04_CactusIndependentSet1.u, jstatic('Math', 'min', Code04_CactusIndependentSet1.low[Code04_CactusIndependentSet1.u], Code04_CactusIndependentSet1.dfn[v]))
                Code04_CactusIndependentSet1.e = jcast('int', Code04_CactusIndependentSet1.nxt[Code04_CactusIndependentSet1.e])
            if (jcast('int', (Code04_CactusIndependentSet1.e ^ 1)) == Code04_CactusIndependentSet1.preEdge):
                Code04_CactusIndependentSet1.e = jcast('int', Code04_CactusIndependentSet1.nxt[Code04_CactusIndependentSet1.e])
            if (Code04_CactusIndependentSet1.e != 0):
                v = jcast('int', Code04_CactusIndependentSet1.to[Code04_CactusIndependentSet1.e])
                if (Code04_CactusIndependentSet1.dfn[v] == 0):
                    Code04_CactusIndependentSet1.push(Code04_CactusIndependentSet1.u, Code04_CactusIndependentSet1.preEdge, 0, Code04_CactusIndependentSet1.e)
                    Code04_CactusIndependentSet1.push(v, Code04_CactusIndependentSet1.e, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code04_CactusIndependentSet1.push(Code04_CactusIndependentSet1.u, Code04_CactusIndependentSet1.preEdge, 1, Code04_CactusIndependentSet1.e)

    @staticmethod
    def main(args):
        in_ = Code04_CactusIndependentSet1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_CactusIndependentSet1.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_CactusIndependentSet1.m = jcast('int', jcall(in_, 'nextInt'))
        Code04_CactusIndependentSet1.cntg = jcast('int', 1)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code04_CactusIndependentSet1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code04_CactusIndependentSet1.addEdge(u, v)
            Code04_CactusIndependentSet1.addEdge(v, u)
            i = jcast('int', (i + 1))
        # 洛谷P4410，使用如下的点权设置
        i = jcast('int', 1)
        while (i <= Code04_CactusIndependentSet1.n):
            jset(Code04_CactusIndependentSet1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        # 洛谷P10779，使用如下的点权设置
        # for (int i = 1; i <= n; i++) {
        # arr[i] = 1;
        # }
        Code04_CactusIndependentSet1.tarjan2(1, 0)
        jcall(out, 'println', jstatic('Math', 'max', Code04_CactusIndependentSet1.dp[1][0], Code04_CactusIndependentSet1.dp[1][1]))
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
            return jcast('int', self.buffer[((_java_obj_32 := self), (_java_key_33 := 'ptr'), (_java_old_34 := jget(_java_obj_32, _java_key_33)), jset(_java_obj_32, _java_key_33, jcast('int', (_java_old_34 + (1)))), _java_old_34)[4]])

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
            raise TypeError("No matching overload for Code04_CactusIndependentSet1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_CactusIndependentSet1.MAXN = jcast('int', 100001)
Code04_CactusIndependentSet1.MAXM = jcast('int', 200001)
Code04_CactusIndependentSet1.INF = jcast('int', 1000000000)
Code04_CactusIndependentSet1.n = jcast('int', 0)
Code04_CactusIndependentSet1.m = jcast('int', 0)
Code04_CactusIndependentSet1.arr = jarray('int', [Code04_CactusIndependentSet1.MAXN])
Code04_CactusIndependentSet1.head = jarray('int', [Code04_CactusIndependentSet1.MAXN])
Code04_CactusIndependentSet1.nxt = jarray('int', [jcast('int', (Code04_CactusIndependentSet1.MAXM << (1 & 31)))])
Code04_CactusIndependentSet1.to = jarray('int', [jcast('int', (Code04_CactusIndependentSet1.MAXM << (1 & 31)))])
Code04_CactusIndependentSet1.cntg = jcast('int', 0)
Code04_CactusIndependentSet1.dfn = jarray('int', [Code04_CactusIndependentSet1.MAXN])
Code04_CactusIndependentSet1.low = jarray('int', [Code04_CactusIndependentSet1.MAXN])
Code04_CactusIndependentSet1.cntd = jcast('int', 0)
Code04_CactusIndependentSet1.sta = jarray('int', [Code04_CactusIndependentSet1.MAXN])
Code04_CactusIndependentSet1.top = jcast('int', 0)
Code04_CactusIndependentSet1.cycle = jarray('int', [Code04_CactusIndependentSet1.MAXN])
Code04_CactusIndependentSet1.dp = jarray('int', [Code04_CactusIndependentSet1.MAXN, 2])
Code04_CactusIndependentSet1.stau = jarray('int', [Code04_CactusIndependentSet1.MAXN])
Code04_CactusIndependentSet1.stap = jarray('int', [Code04_CactusIndependentSet1.MAXN])
Code04_CactusIndependentSet1.stas = jarray('int', [Code04_CactusIndependentSet1.MAXN])
Code04_CactusIndependentSet1.stae = jarray('int', [Code04_CactusIndependentSet1.MAXN])
Code04_CactusIndependentSet1.u = jcast('int', 0)
Code04_CactusIndependentSet1.preEdge = jcast('int', 0)
Code04_CactusIndependentSet1.status = jcast('int', 0)
Code04_CactusIndependentSet1.e = jcast('int', 0)
Code04_CactusIndependentSet1.stacksiz = jcast('int', 0)

if __name__ == '__main__':
    Code04_CactusIndependentSet1.main([])
