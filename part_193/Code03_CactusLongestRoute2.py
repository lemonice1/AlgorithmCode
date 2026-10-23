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

# 仙人掌最长路线，Python版
# 给定n个点、m条边的无向连通图，输入保证图是仙人掌
# 路线可以从任何城市开始，但必须在1号点结束
# 路线可以重复经过同一个点，但不能重复经过同一条边
# 计算最长路线的边数
# 1 <= n <= 10^4
# 1 <= m <= 2 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P6335
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_CactusLongestRoute2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'cycle': 'cycle', 'f': 'f', 'g': 'g'}
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
    cycle = None
    # f[u] : 在u向下的结构中（以u为头的子仙人掌），从u出发并最终回到u，能走过的最大边数
    f = None
    # g[u] : 在u向下的结构中（以u为头的子仙人掌），从u出发，终点任意，能走过的最大边数
    g = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_CactusLongestRoute2.nxt, ((_java_obj_1 := Code03_CactusLongestRoute2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_CactusLongestRoute2.head[u])
        Code03_CactusLongestRoute2.to[Code03_CactusLongestRoute2.cntg] = jcast('int', v)
        Code03_CactusLongestRoute2.head[u] = jcast('int', Code03_CactusLongestRoute2.cntg)

    @staticmethod
    def dpOnCycle(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        siz = jcast('int', 0)
        pop = 0
        while True:
            pop = jcast('int', Code03_CactusLongestRoute2.sta[((_java_obj_4 := Code03_CactusLongestRoute2), (_java_key_5 := 'top'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))), _java_old_6)[4]])
            jset(Code03_CactusLongestRoute2.cycle, (siz := jcast('int', (siz + (1)))), pop)
            if not ((pop != v)):
                break
        # best表示，这个环上任选一个点作为最后出去的位置
        # 从u沿两侧之一走到它，能够得到的不回到u的最大边数
        best = jcast('int', 0)
        sum = jcast('int', 1)
        i = jcast('int', 1)
        while (i <= siz):
            best = jcast('int', jstatic('Math', 'max', best, jcast('int', jadd(sum, Code03_CactusLongestRoute2.g[Code03_CactusLongestRoute2.cycle[i]]))))
            sum = jcast('int', jcast('int', jadd(sum, jcast('int', jadd(Code03_CactusLongestRoute2.f[Code03_CactusLongestRoute2.cycle[i]], 1)))))
            i = jcast('int', (i + 1))
        # u可以下方有多个环，所以新增此时的sum
        Code03_CactusLongestRoute2.f[u] = jcast('int', jcast('int', jadd(Code03_CactusLongestRoute2.f[u], sum)))
        otherSide = jcast('int', sum)
        i = jcast('int', 1)
        while (i <= siz):
            otherSide = jcast('int', jcast('int', (otherSide - jcast('int', jadd(Code03_CactusLongestRoute2.f[Code03_CactusLongestRoute2.cycle[i]], 1)))))
            best = jcast('int', jstatic('Math', 'max', best, jcast('int', jadd(otherSide, Code03_CactusLongestRoute2.g[Code03_CactusLongestRoute2.cycle[i]]))))
            i = jcast('int', (i + 1))
        return jcast('int', jcast('int', (best - sum)))

    @staticmethod
    def tarjan(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code03_CactusLongestRoute2.dfn, u, jset(Code03_CactusLongestRoute2.low, u, ((_java_obj_7 := Code03_CactusLongestRoute2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
        jset(Code03_CactusLongestRoute2.sta, ((_java_obj_10 := Code03_CactusLongestRoute2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
        # f[u]表示从u出发并最终回到u的最大边数
        # delta为了计算，g[u] = f[u] + delta
        # 表示额外选择一条最后不回到u的出口路线，能带来的最大增量
        delta = jcast('int', 0)
        e = jcast('int', Code03_CactusLongestRoute2.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code03_CactusLongestRoute2.to[e])
                if (Code03_CactusLongestRoute2.dfn[v] == 0):
                    Code03_CactusLongestRoute2.tarjan(v, e)
                    if (Code03_CactusLongestRoute2.low[v] < Code03_CactusLongestRoute2.dfn[u]):
                        jset(Code03_CactusLongestRoute2.low, u, jstatic('Math', 'min', Code03_CactusLongestRoute2.low[u], Code03_CactusLongestRoute2.low[v]))
                    else:
                        if (Code03_CactusLongestRoute2.low[v] > Code03_CactusLongestRoute2.dfn[u]):
                            Code03_CactusLongestRoute2.top = jcast('int', (Code03_CactusLongestRoute2.top - 1))
                            delta = jcast('int', jstatic('Math', 'max', delta, jcast('int', jadd(Code03_CactusLongestRoute2.g[v], 1))))
                        else:
                            delta = jcast('int', jstatic('Math', 'max', delta, Code03_CactusLongestRoute2.dpOnCycle(u, v)))
                else:
                    if (Code03_CactusLongestRoute2.dfn[v] < Code03_CactusLongestRoute2.dfn[u]):
                        jset(Code03_CactusLongestRoute2.low, u, jstatic('Math', 'min', Code03_CactusLongestRoute2.low[u], Code03_CactusLongestRoute2.dfn[v]))
            except JContinue as _java_control_13:
                if _java_control_13.label not in (None,):
                    raise
            except JBreak as _java_control_13:
                if _java_control_13.label not in (None,):
                    raise
                break
            e = jcast('int', Code03_CactusLongestRoute2.nxt[e])
        Code03_CactusLongestRoute2.g[u] = jcast('int', jcast('int', jadd(Code03_CactusLongestRoute2.f[u], delta)))

    @staticmethod
    def main(args):
        in_ = Code03_CactusLongestRoute2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_CactusLongestRoute2.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_CactusLongestRoute2.m = jcast('int', jcall(in_, 'nextInt'))
        Code03_CactusLongestRoute2.cntg = jcast('int', 1)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code03_CactusLongestRoute2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code03_CactusLongestRoute2.addEdge(u, v)
            Code03_CactusLongestRoute2.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code03_CactusLongestRoute2.tarjan(1, 0)
        jcall(out, 'println', Code03_CactusLongestRoute2.g[1])
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
            return jcast('int', self.buffer[((_java_obj_14 := self), (_java_key_15 := 'ptr'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))), _java_old_16)[4]])

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
            raise TypeError("No matching overload for Code03_CactusLongestRoute2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_CactusLongestRoute2.MAXN = jcast('int', 10001)
Code03_CactusLongestRoute2.MAXM = jcast('int', 20001)
Code03_CactusLongestRoute2.n = jcast('int', 0)
Code03_CactusLongestRoute2.m = jcast('int', 0)
Code03_CactusLongestRoute2.head = jarray('int', [Code03_CactusLongestRoute2.MAXN])
Code03_CactusLongestRoute2.nxt = jarray('int', [jcast('int', (Code03_CactusLongestRoute2.MAXM << (1 & 31)))])
Code03_CactusLongestRoute2.to = jarray('int', [jcast('int', (Code03_CactusLongestRoute2.MAXM << (1 & 31)))])
Code03_CactusLongestRoute2.cntg = jcast('int', 0)
Code03_CactusLongestRoute2.dfn = jarray('int', [Code03_CactusLongestRoute2.MAXN])
Code03_CactusLongestRoute2.low = jarray('int', [Code03_CactusLongestRoute2.MAXN])
Code03_CactusLongestRoute2.cntd = jcast('int', 0)
Code03_CactusLongestRoute2.sta = jarray('int', [Code03_CactusLongestRoute2.MAXN])
Code03_CactusLongestRoute2.top = jcast('int', 0)
Code03_CactusLongestRoute2.cycle = jarray('int', [Code03_CactusLongestRoute2.MAXN])
Code03_CactusLongestRoute2.f = jarray('int', [Code03_CactusLongestRoute2.MAXN])
Code03_CactusLongestRoute2.g = jarray('int', [Code03_CactusLongestRoute2.MAXN])

if __name__ == '__main__':
    Code03_CactusLongestRoute2.main([])
