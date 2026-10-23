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

# 间谍网络，Python版
# 一共有n个间谍，其中有p个间谍可以贿赂，给定各自的价格，剩下的间谍不能贿赂
# 然后给定m个控制关系，控制关系是单向的，也是可传递的
# 如果间谍a能控制间谍b，间谍b能控制间谍c，那么间谍a就能控制间谍c
# 当你贿赂了某个间谍，该间谍连同他能控制的所有人，都能被你控制
# 如果你不能控制所有间谍，打印"NO"，然后打印不能控制的间谍中，最小的编号
# 如果你可以控制所有间谍，打印"YES"，然后打印需要花费的最少钱数
# 1 <= n <= 3000    0 <= 各自的价格 <= 20000    1 <= m <= 8000
# 测试链接 : https://www.luogu.com.cn/problem/P1262
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_Spy1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'INF': 'INF', 'n': 'n', 'p': 'p', 'm': 'm', 'cost': 'cost', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'minVal': 'minVal', 'sccCnt': 'sccCnt', 'indegree': 'indegree'}
    MAXN = 0
    MAXM = 0
    INF = 0
    n = 0
    p = 0
    m = 0
    cost = None
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
    minVal = None
    sccCnt = 0
    indegree = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_Spy1.nxt, ((_java_obj_1 := Code07_Spy1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_Spy1.head[u])
        Code07_Spy1.to[Code07_Spy1.cntg] = jcast('int', v)
        Code07_Spy1.head[u] = jcast('int', Code07_Spy1.cntg)

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code07_Spy1.dfn, u, jset(Code07_Spy1.low, u, ((_java_obj_4 := Code07_Spy1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code07_Spy1.sta, ((_java_obj_7 := Code07_Spy1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code07_Spy1.head[u])
        while (e > 0):
            v = jcast('int', Code07_Spy1.to[e])
            if (Code07_Spy1.dfn[v] == 0):
                Code07_Spy1.tarjan(v)
                jset(Code07_Spy1.low, u, jstatic('Math', 'min', Code07_Spy1.low[u], Code07_Spy1.low[v]))
            else:
                if (Code07_Spy1.belong[v] == 0):
                    jset(Code07_Spy1.low, u, jstatic('Math', 'min', Code07_Spy1.low[u], Code07_Spy1.dfn[v]))
            e = jcast('int', Code07_Spy1.nxt[e])
        if (Code07_Spy1.dfn[u] == Code07_Spy1.low[u]):
            Code07_Spy1.sccCnt = jcast('int', (Code07_Spy1.sccCnt + 1))
            Code07_Spy1.minVal[Code07_Spy1.sccCnt] = jcast('int', Code07_Spy1.INF)
            pop = 0
            while True:
                pop = jcast('int', Code07_Spy1.sta[((_java_obj_10 := Code07_Spy1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code07_Spy1.belong[pop] = jcast('int', Code07_Spy1.sccCnt)
                jset(Code07_Spy1.minVal, Code07_Spy1.sccCnt, jstatic('Math', 'min', Code07_Spy1.minVal[Code07_Spy1.sccCnt], Code07_Spy1.cost[pop]))
                if not ((pop != u)):
                    break

    @staticmethod
    def main(args):
        in_ = Code07_Spy1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_Spy1.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_Spy1.p = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_Spy1.n):
            Code07_Spy1.cost[i] = jcast('int', Code07_Spy1.INF)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        c = 0
        while (i <= Code07_Spy1.p):
            u = jcast('int', jcall(in_, 'nextInt'))
            c = jcast('int', jcall(in_, 'nextInt'))
            Code07_Spy1.cost[u] = jcast('int', c)
            i = jcast('int', (i + 1))
        Code07_Spy1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_Spy1.m):
            jset(Code07_Spy1.a, i, jcall(in_, 'nextInt'))
            jset(Code07_Spy1.b, i, jcall(in_, 'nextInt'))
            Code07_Spy1.addEdge(Code07_Spy1.a[i], Code07_Spy1.b[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_Spy1.n):
            if ((Code07_Spy1.cost[i] != Code07_Spy1.INF) and (Code07_Spy1.dfn[i] == 0)):
                Code07_Spy1.tarjan(i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', True)
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code07_Spy1.n):
            try:
                if (Code07_Spy1.belong[i] == 0):
                    check = jcast('boolean', False)
                    ans = jcast('int', i)
                    raise JBreak(None)
            except JContinue as _java_control_13:
                if _java_control_13.label not in (None,):
                    raise
            except JBreak as _java_control_13:
                if _java_control_13.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if (not check):
            jcall(out, 'println', 'NO')
            jcall(out, 'println', ans)
        else:
            i = jcast('int', 1)
            while (i <= Code07_Spy1.m):
                scc1 = jcast('int', Code07_Spy1.belong[Code07_Spy1.a[i]])
                scc2 = jcast('int', Code07_Spy1.belong[Code07_Spy1.b[i]])
                if (scc1 != scc2):
                    Code07_Spy1.indegree[scc2] = jcast('int', (Code07_Spy1.indegree[scc2] + 1))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code07_Spy1.sccCnt):
                if (Code07_Spy1.indegree[i] == 0):
                    ans = jcast('int', jcast('int', jadd(ans, Code07_Spy1.minVal[i])))
                i = jcast('int', (i + 1))
            jcall(out, 'println', 'YES')
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
            raise TypeError("No matching overload for Code07_Spy1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_Spy1.MAXN = jcast('int', 3001)
Code07_Spy1.MAXM = jcast('int', 8001)
Code07_Spy1.INF = jcast('int', 1000000001)
Code07_Spy1.n = jcast('int', 0)
Code07_Spy1.p = jcast('int', 0)
Code07_Spy1.m = jcast('int', 0)
Code07_Spy1.cost = jarray('int', [Code07_Spy1.MAXN])
Code07_Spy1.a = jarray('int', [Code07_Spy1.MAXM])
Code07_Spy1.b = jarray('int', [Code07_Spy1.MAXM])
Code07_Spy1.head = jarray('int', [Code07_Spy1.MAXN])
Code07_Spy1.nxt = jarray('int', [Code07_Spy1.MAXM])
Code07_Spy1.to = jarray('int', [Code07_Spy1.MAXM])
Code07_Spy1.cntg = jcast('int', 0)
Code07_Spy1.dfn = jarray('int', [Code07_Spy1.MAXN])
Code07_Spy1.low = jarray('int', [Code07_Spy1.MAXN])
Code07_Spy1.cntd = jcast('int', 0)
Code07_Spy1.sta = jarray('int', [Code07_Spy1.MAXN])
Code07_Spy1.top = jcast('int', 0)
Code07_Spy1.belong = jarray('int', [Code07_Spy1.MAXN])
Code07_Spy1.minVal = jarray('int', [Code07_Spy1.MAXN])
Code07_Spy1.sccCnt = jcast('int', 0)
Code07_Spy1.indegree = jarray('int', [Code07_Spy1.MAXN])

if __name__ == '__main__':
    Code07_Spy1.main([])
