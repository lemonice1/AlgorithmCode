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

# 劫掠计划，Python版
# 一共有n个城市，给定m条有向道路，每个城市给定拥有的钱数
# 给定起点城市s，给定p个有酒吧的城市，有酒吧的城市才能作为终点
# 路线必须从s出发到任意终点停止，重复经过城市的话，钱仅获得一次
# 题目保证一定存在这样的路线，打印能获得的最大钱数
# 1 <= n、m <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3627
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_RobberyPlan1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'INF': 'INF', 'n': 'n', 'm': 'm', 's': 's', 'p': 'p', 'money': 'money', 'isBar': 'isBar', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sum': 'sum', 'hasBar': 'hasBar', 'sccCnt': 'sccCnt', 'dp': 'dp', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    INF = 0
    n = 0
    m = 0
    s = 0
    p = 0
    money = None
    isBar = None
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
    hasBar = None
    sccCnt = 0
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
        jset(Code03_RobberyPlan1.stack[Code03_RobberyPlan1.stacksize], 0, u)
        jset(Code03_RobberyPlan1.stack[Code03_RobberyPlan1.stacksize], 1, status)
        jset(Code03_RobberyPlan1.stack[Code03_RobberyPlan1.stacksize], 2, e)
        Code03_RobberyPlan1.stacksize = jcast('int', (Code03_RobberyPlan1.stacksize + 1))

    @staticmethod
    def pop():
        Code03_RobberyPlan1.stacksize = jcast('int', (Code03_RobberyPlan1.stacksize - 1))
        Code03_RobberyPlan1.u = jcast('int', Code03_RobberyPlan1.stack[Code03_RobberyPlan1.stacksize][0])
        Code03_RobberyPlan1.status = jcast('int', Code03_RobberyPlan1.stack[Code03_RobberyPlan1.stacksize][1])
        Code03_RobberyPlan1.e = jcast('int', Code03_RobberyPlan1.stack[Code03_RobberyPlan1.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_RobberyPlan1.nxt, ((_java_obj_1 := Code03_RobberyPlan1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_RobberyPlan1.head[u])
        Code03_RobberyPlan1.to[Code03_RobberyPlan1.cntg] = jcast('int', v)
        Code03_RobberyPlan1.head[u] = jcast('int', Code03_RobberyPlan1.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code03_RobberyPlan1.dfn, u, jset(Code03_RobberyPlan1.low, u, ((_java_obj_4 := Code03_RobberyPlan1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code03_RobberyPlan1.sta, ((_java_obj_7 := Code03_RobberyPlan1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code03_RobberyPlan1.head[u])
        while (e > 0):
            v = jcast('int', Code03_RobberyPlan1.to[e])
            if (Code03_RobberyPlan1.dfn[v] == 0):
                Code03_RobberyPlan1.tarjan1(v)
                jset(Code03_RobberyPlan1.low, u, jstatic('Math', 'min', Code03_RobberyPlan1.low[u], Code03_RobberyPlan1.low[v]))
            else:
                if (Code03_RobberyPlan1.belong[v] == 0):
                    jset(Code03_RobberyPlan1.low, u, jstatic('Math', 'min', Code03_RobberyPlan1.low[u], Code03_RobberyPlan1.dfn[v]))
            e = jcast('int', Code03_RobberyPlan1.nxt[e])
        if (Code03_RobberyPlan1.dfn[u] == Code03_RobberyPlan1.low[u]):
            Code03_RobberyPlan1.sccCnt = jcast('int', (Code03_RobberyPlan1.sccCnt + 1))
            Code03_RobberyPlan1.sum[Code03_RobberyPlan1.sccCnt] = jcast('int', 0)
            Code03_RobberyPlan1.hasBar[Code03_RobberyPlan1.sccCnt] = jcast('boolean', False)
            pop = 0
            while True:
                pop = jcast('int', Code03_RobberyPlan1.sta[((_java_obj_10 := Code03_RobberyPlan1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code03_RobberyPlan1.belong[pop] = jcast('int', Code03_RobberyPlan1.sccCnt)
                Code03_RobberyPlan1.sum[Code03_RobberyPlan1.sccCnt] = jcast('int', jcast('int', jadd(Code03_RobberyPlan1.sum[Code03_RobberyPlan1.sccCnt], Code03_RobberyPlan1.money[pop])))
                Code03_RobberyPlan1.hasBar[Code03_RobberyPlan1.sccCnt] = jcast('boolean', (Code03_RobberyPlan1.hasBar[Code03_RobberyPlan1.sccCnt] | Code03_RobberyPlan1.isBar[pop]))
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code03_RobberyPlan1.stacksize = jcast('int', 0)
        Code03_RobberyPlan1.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code03_RobberyPlan1.stacksize > 0):
            Code03_RobberyPlan1.pop()
            if (Code03_RobberyPlan1.status == jcast('int', (-1))):
                jset(Code03_RobberyPlan1.dfn, Code03_RobberyPlan1.u, jset(Code03_RobberyPlan1.low, Code03_RobberyPlan1.u, ((_java_obj_13 := Code03_RobberyPlan1), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code03_RobberyPlan1.sta, ((_java_obj_16 := Code03_RobberyPlan1), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code03_RobberyPlan1.u)
                Code03_RobberyPlan1.e = jcast('int', Code03_RobberyPlan1.head[Code03_RobberyPlan1.u])
            else:
                v = jcast('int', Code03_RobberyPlan1.to[Code03_RobberyPlan1.e])
                if (Code03_RobberyPlan1.status == 0):
                    jset(Code03_RobberyPlan1.low, Code03_RobberyPlan1.u, jstatic('Math', 'min', Code03_RobberyPlan1.low[Code03_RobberyPlan1.u], Code03_RobberyPlan1.low[v]))
                if ((Code03_RobberyPlan1.status == 1) and (Code03_RobberyPlan1.belong[v] == 0)):
                    jset(Code03_RobberyPlan1.low, Code03_RobberyPlan1.u, jstatic('Math', 'min', Code03_RobberyPlan1.low[Code03_RobberyPlan1.u], Code03_RobberyPlan1.dfn[v]))
                Code03_RobberyPlan1.e = jcast('int', Code03_RobberyPlan1.nxt[Code03_RobberyPlan1.e])
            if (Code03_RobberyPlan1.e != 0):
                v = jcast('int', Code03_RobberyPlan1.to[Code03_RobberyPlan1.e])
                if (Code03_RobberyPlan1.dfn[v] == 0):
                    Code03_RobberyPlan1.push(Code03_RobberyPlan1.u, 0, Code03_RobberyPlan1.e)
                    Code03_RobberyPlan1.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code03_RobberyPlan1.push(Code03_RobberyPlan1.u, 1, Code03_RobberyPlan1.e)
            else:
                if (Code03_RobberyPlan1.dfn[Code03_RobberyPlan1.u] == Code03_RobberyPlan1.low[Code03_RobberyPlan1.u]):
                    Code03_RobberyPlan1.sccCnt = jcast('int', (Code03_RobberyPlan1.sccCnt + 1))
                    Code03_RobberyPlan1.sum[Code03_RobberyPlan1.sccCnt] = jcast('int', 0)
                    Code03_RobberyPlan1.hasBar[Code03_RobberyPlan1.sccCnt] = jcast('boolean', False)
                    pop = 0
                    while True:
                        pop = jcast('int', Code03_RobberyPlan1.sta[((_java_obj_19 := Code03_RobberyPlan1), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                        Code03_RobberyPlan1.belong[pop] = jcast('int', Code03_RobberyPlan1.sccCnt)
                        Code03_RobberyPlan1.sum[Code03_RobberyPlan1.sccCnt] = jcast('int', jcast('int', jadd(Code03_RobberyPlan1.sum[Code03_RobberyPlan1.sccCnt], Code03_RobberyPlan1.money[pop])))
                        Code03_RobberyPlan1.hasBar[Code03_RobberyPlan1.sccCnt] = jcast('boolean', (Code03_RobberyPlan1.hasBar[Code03_RobberyPlan1.sccCnt] | Code03_RobberyPlan1.isBar[pop]))
                        if not ((pop != Code03_RobberyPlan1.u)):
                            break

    @staticmethod
    def condense():
        Code03_RobberyPlan1.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code03_RobberyPlan1.sccCnt):
            Code03_RobberyPlan1.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_RobberyPlan1.m):
            scc1 = jcast('int', Code03_RobberyPlan1.belong[Code03_RobberyPlan1.a[i]])
            scc2 = jcast('int', Code03_RobberyPlan1.belong[Code03_RobberyPlan1.b[i]])
            if (((scc1 > 0) and (scc2 > 0)) and (scc1 != scc2)):
                Code03_RobberyPlan1.addEdge(scc1, scc2)
            i = jcast('int', (i + 1))

    @staticmethod
    def dpOnDAG():
        u = jcast('int', 1)
        while (u <= Code03_RobberyPlan1.sccCnt):
            Code03_RobberyPlan1.dp[u] = jcast('int', jcast('int', (-Code03_RobberyPlan1.INF)))
            u = jcast('int', (u + 1))
        jset(Code03_RobberyPlan1.dp, Code03_RobberyPlan1.belong[Code03_RobberyPlan1.s], Code03_RobberyPlan1.sum[Code03_RobberyPlan1.belong[Code03_RobberyPlan1.s]])
        u = jcast('int', Code03_RobberyPlan1.sccCnt)
        while (u > 0):
            e = jcast('int', Code03_RobberyPlan1.head[u])
            while (e > 0):
                v = jcast('int', Code03_RobberyPlan1.to[e])
                jset(Code03_RobberyPlan1.dp, v, jstatic('Math', 'max', Code03_RobberyPlan1.dp[v], jcast('int', jadd(Code03_RobberyPlan1.dp[u], Code03_RobberyPlan1.sum[v]))))
                e = jcast('int', Code03_RobberyPlan1.nxt[e])
            u = jcast('int', (u - 1))
        ans = jcast('int', 0)
        u = jcast('int', 1)
        while (u <= Code03_RobberyPlan1.sccCnt):
            if Code03_RobberyPlan1.hasBar[u]:
                ans = jcast('int', jstatic('Math', 'max', ans, Code03_RobberyPlan1.dp[u]))
            u = jcast('int', (u + 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code03_RobberyPlan1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_RobberyPlan1.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_RobberyPlan1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_RobberyPlan1.m):
            jset(Code03_RobberyPlan1.a, i, jcall(in_, 'nextInt'))
            jset(Code03_RobberyPlan1.b, i, jcall(in_, 'nextInt'))
            Code03_RobberyPlan1.addEdge(Code03_RobberyPlan1.a[i], Code03_RobberyPlan1.b[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_RobberyPlan1.n):
            jset(Code03_RobberyPlan1.money, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code03_RobberyPlan1.s = jcast('int', jcall(in_, 'nextInt'))
        Code03_RobberyPlan1.p = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        while (i <= Code03_RobberyPlan1.p):
            x = jcast('int', jcall(in_, 'nextInt'))
            Code03_RobberyPlan1.isBar[x] = jcast('boolean', True)
            i = jcast('int', (i + 1))
        # tarjan1(s);
        Code03_RobberyPlan1.tarjan2(Code03_RobberyPlan1.s)
        Code03_RobberyPlan1.condense()
        ans = jcast('int', Code03_RobberyPlan1.dpOnDAG())
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
            raise TypeError("No matching overload for Code03_RobberyPlan1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_RobberyPlan1.MAXN = jcast('int', 500001)
Code03_RobberyPlan1.MAXM = jcast('int', 500001)
Code03_RobberyPlan1.INF = jcast('int', 1000000001)
Code03_RobberyPlan1.n = jcast('int', 0)
Code03_RobberyPlan1.m = jcast('int', 0)
Code03_RobberyPlan1.s = jcast('int', 0)
Code03_RobberyPlan1.p = jcast('int', 0)
Code03_RobberyPlan1.money = jarray('int', [Code03_RobberyPlan1.MAXN])
Code03_RobberyPlan1.isBar = jarray('boolean', [Code03_RobberyPlan1.MAXN])
Code03_RobberyPlan1.a = jarray('int', [Code03_RobberyPlan1.MAXM])
Code03_RobberyPlan1.b = jarray('int', [Code03_RobberyPlan1.MAXM])
Code03_RobberyPlan1.head = jarray('int', [Code03_RobberyPlan1.MAXN])
Code03_RobberyPlan1.nxt = jarray('int', [Code03_RobberyPlan1.MAXM])
Code03_RobberyPlan1.to = jarray('int', [Code03_RobberyPlan1.MAXM])
Code03_RobberyPlan1.cntg = jcast('int', 0)
Code03_RobberyPlan1.dfn = jarray('int', [Code03_RobberyPlan1.MAXN])
Code03_RobberyPlan1.low = jarray('int', [Code03_RobberyPlan1.MAXN])
Code03_RobberyPlan1.cntd = jcast('int', 0)
Code03_RobberyPlan1.sta = jarray('int', [Code03_RobberyPlan1.MAXN])
Code03_RobberyPlan1.top = jcast('int', 0)
Code03_RobberyPlan1.belong = jarray('int', [Code03_RobberyPlan1.MAXN])
Code03_RobberyPlan1.sum = jarray('int', [Code03_RobberyPlan1.MAXN])
Code03_RobberyPlan1.hasBar = jarray('boolean', [Code03_RobberyPlan1.MAXN])
Code03_RobberyPlan1.sccCnt = jcast('int', 0)
Code03_RobberyPlan1.dp = jarray('int', [Code03_RobberyPlan1.MAXN])
Code03_RobberyPlan1.stack = jarray('int', [Code03_RobberyPlan1.MAXN, 3])
Code03_RobberyPlan1.u = jcast('int', 0)
Code03_RobberyPlan1.status = jcast('int', 0)
Code03_RobberyPlan1.e = jcast('int', 0)
Code03_RobberyPlan1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code03_RobberyPlan1.main([])
