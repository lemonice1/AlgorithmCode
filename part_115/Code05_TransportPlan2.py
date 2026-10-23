# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 运输计划，Python迭代版
# 有n个节点，给定n-1条边使其连接成一棵树，每条边有正数边权
# 给定很多运输计划，每个运输计划(a,b)表示从a去往b
# 每个运输计划的代价就是沿途边权和，运输计划之间完全互不干扰
# 你只能选择一条边，将其边权变成0
# 你的目的是让所有运输计划代价的最大值尽量小
# 返回所有运输计划代价的最大值最小能是多少
# 测试链接 : https://www.luogu.com.cn/problem/P2680
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 有时候可以完全通过，有时候会有一个测试用例超时
# 题目对运行时间限制较紧，应按 Python 实现的实际开销评估
# 对应实现可参考 Code05_TransportPlan3.py
# 两个版本保留相同的算法逻辑
class Code05_TransportPlan2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'num': 'num', 'headEdge': 'headEdge', 'edgeNext': 'edgeNext', 'edgeTo': 'edgeTo', 'edgeWeight': 'edgeWeight', 'tcnt': 'tcnt', 'headQuery': 'headQuery', 'queryNext': 'queryNext', 'queryTo': 'queryTo', 'queryIndex': 'queryIndex', 'qcnt': 'qcnt', 'visited': 'visited', 'unionfind': 'unionfind', 'quesu': 'quesu', 'quesv': 'quesv', 'distance': 'distance', 'lca': 'lca', 'cost': 'cost', 'maxCost': 'maxCost', 'stack': 'stack', 'ufwe': 'ufwe', 'stackSize': 'stackSize', 'u': 'u', 'f': 'f_data', 'w': 'w', 'e': 'e', 'atLeast': 'atLeast', 'beyond': 'beyond'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    num = None
    headEdge = None
    edgeNext = None
    edgeTo = None
    edgeWeight = None
    tcnt = 0
    headQuery = None
    queryNext = None
    queryTo = None
    queryIndex = None
    qcnt = 0
    visited = None
    unionfind = None
    quesu = None
    quesv = None
    distance = None
    lca = None
    cost = None
    maxCost = 0
    @staticmethod
    def build():
        Code05_TransportPlan2.tcnt = jcast('int', jset(Code05_TransportPlan2, 'qcnt', 1))
        jstatic('Arrays', 'fill', Code05_TransportPlan2.headEdge, 1, jcast('int', jadd(Code05_TransportPlan2.n, 1)), 0)
        jstatic('Arrays', 'fill', Code05_TransportPlan2.headQuery, 1, jcast('int', jadd(Code05_TransportPlan2.n, 1)), 0)
        jstatic('Arrays', 'fill', Code05_TransportPlan2.visited, 1, jcast('int', jadd(Code05_TransportPlan2.n, 1)), False)
        i = jcast('int', 1)
        while (i <= Code05_TransportPlan2.n):
            Code05_TransportPlan2.unionfind[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        Code05_TransportPlan2.maxCost = jcast('int', 0)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code05_TransportPlan2.edgeNext[Code05_TransportPlan2.tcnt] = jcast('int', Code05_TransportPlan2.headEdge[u])
        Code05_TransportPlan2.edgeTo[Code05_TransportPlan2.tcnt] = jcast('int', v)
        Code05_TransportPlan2.edgeWeight[Code05_TransportPlan2.tcnt] = jcast('int', w)
        jset(Code05_TransportPlan2.headEdge, u, ((_java_obj_1 := Code05_TransportPlan2), (_java_key_2 := 'tcnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def addQuery(u, v, i):
        u = jcast('int', u)
        v = jcast('int', v)
        i = jcast('int', i)
        Code05_TransportPlan2.queryNext[Code05_TransportPlan2.qcnt] = jcast('int', Code05_TransportPlan2.headQuery[u])
        Code05_TransportPlan2.queryTo[Code05_TransportPlan2.qcnt] = jcast('int', v)
        Code05_TransportPlan2.queryIndex[Code05_TransportPlan2.qcnt] = jcast('int', i)
        jset(Code05_TransportPlan2.headQuery, u, ((_java_obj_4 := Code05_TransportPlan2), (_java_key_5 := 'qcnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4])

    # find方法的递归版改迭代版
    stack = None
    @staticmethod
    def find(i):
        i = jcast('int', i)
        size = jcast('int', 0)
        while (i != Code05_TransportPlan2.unionfind[i]):
            jset(Code05_TransportPlan2.stack, ((_java_old_7 := size), (size := jcast('int', (size + (1)))), _java_old_7)[2], i)
            i = jcast('int', Code05_TransportPlan2.unionfind[i])
        while (size > 0):
            jset(Code05_TransportPlan2.unionfind, Code05_TransportPlan2.stack[(size := jcast('int', (size + (-1))))], i)
        return jcast('int', i)

    # tarjan方法的递归版改迭代版
    # 不会改，看讲解118，讲了怎么从递归版改成迭代版
    ufwe = None
    stackSize = 0
    u = 0
    f_data = 0
    w = 0
    e = 0
    @staticmethod
    def push(u, f, w, e):
        u = jcast('int', u)
        f = jcast('int', f)
        w = jcast('int', w)
        e = jcast('int', e)
        jset(Code05_TransportPlan2.ufwe[Code05_TransportPlan2.stackSize], 0, u)
        jset(Code05_TransportPlan2.ufwe[Code05_TransportPlan2.stackSize], 1, f)
        jset(Code05_TransportPlan2.ufwe[Code05_TransportPlan2.stackSize], 2, w)
        jset(Code05_TransportPlan2.ufwe[Code05_TransportPlan2.stackSize], 3, e)
        Code05_TransportPlan2.stackSize = jcast('int', (Code05_TransportPlan2.stackSize + 1))

    @staticmethod
    def pop():
        Code05_TransportPlan2.stackSize = jcast('int', (Code05_TransportPlan2.stackSize - 1))
        Code05_TransportPlan2.u = jcast('int', Code05_TransportPlan2.ufwe[Code05_TransportPlan2.stackSize][0])
        Code05_TransportPlan2.f_data = jcast('int', Code05_TransportPlan2.ufwe[Code05_TransportPlan2.stackSize][1])
        Code05_TransportPlan2.w = jcast('int', Code05_TransportPlan2.ufwe[Code05_TransportPlan2.stackSize][2])
        Code05_TransportPlan2.e = jcast('int', Code05_TransportPlan2.ufwe[Code05_TransportPlan2.stackSize][3])

    @staticmethod
    def tarjan(root):
        root = jcast('int', root)
        Code05_TransportPlan2.stackSize = jcast('int', 0)
        Code05_TransportPlan2.push(root, 0, 0, jcast('int', (-1)))
        while (Code05_TransportPlan2.stackSize > 0):
            Code05_TransportPlan2.pop()
            if (Code05_TransportPlan2.e == jcast('int', (-1))):
                Code05_TransportPlan2.visited[Code05_TransportPlan2.u] = jcast('boolean', True)
                Code05_TransportPlan2.distance[Code05_TransportPlan2.u] = jcast('int', jcast('int', jadd(Code05_TransportPlan2.distance[Code05_TransportPlan2.f_data], Code05_TransportPlan2.w)))
                Code05_TransportPlan2.e = jcast('int', Code05_TransportPlan2.headEdge[Code05_TransportPlan2.u])
            else:
                Code05_TransportPlan2.e = jcast('int', Code05_TransportPlan2.edgeNext[Code05_TransportPlan2.e])
            if (Code05_TransportPlan2.e != 0):
                Code05_TransportPlan2.push(Code05_TransportPlan2.u, Code05_TransportPlan2.f_data, Code05_TransportPlan2.w, Code05_TransportPlan2.e)
                if (Code05_TransportPlan2.edgeTo[Code05_TransportPlan2.e] != Code05_TransportPlan2.f_data):
                    Code05_TransportPlan2.push(Code05_TransportPlan2.edgeTo[Code05_TransportPlan2.e], Code05_TransportPlan2.u, Code05_TransportPlan2.edgeWeight[Code05_TransportPlan2.e], jcast('int', (-1)))
            else:
                q = jcast('int', Code05_TransportPlan2.headQuery[Code05_TransportPlan2.u])
                v = 0
                i = 0
                while (q != 0):
                    v = jcast('int', Code05_TransportPlan2.queryTo[q])
                    if Code05_TransportPlan2.visited[v]:
                        i = jcast('int', Code05_TransportPlan2.queryIndex[q])
                        jset(Code05_TransportPlan2.lca, i, Code05_TransportPlan2.find(v))
                        Code05_TransportPlan2.cost[i] = jcast('int', jcast('int', (jcast('int', jadd(Code05_TransportPlan2.distance[Code05_TransportPlan2.u], Code05_TransportPlan2.distance[v])) - jcast('int', (2 * Code05_TransportPlan2.distance[Code05_TransportPlan2.lca[i]])))))
                        Code05_TransportPlan2.maxCost = jcast('int', jstatic('Math', 'max', Code05_TransportPlan2.maxCost, Code05_TransportPlan2.cost[i]))
                    q = jcast('int', Code05_TransportPlan2.queryNext[q])
                Code05_TransportPlan2.unionfind[Code05_TransportPlan2.u] = jcast('int', Code05_TransportPlan2.f_data)

    @staticmethod
    def f(limit):
        limit = jcast('int', limit)
        Code05_TransportPlan2.atLeast = jcast('int', jcast('int', (Code05_TransportPlan2.maxCost - limit)))
        jstatic('Arrays', 'fill', Code05_TransportPlan2.num, 1, jcast('int', jadd(Code05_TransportPlan2.n, 1)), 0)
        Code05_TransportPlan2.beyond = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code05_TransportPlan2.m):
            if (Code05_TransportPlan2.cost[i] > limit):
                ((_java_obj_8 := Code05_TransportPlan2.num), (_java_key_9 := Code05_TransportPlan2.quesu[i]), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))), _java_old_10)[4]
                ((_java_obj_11 := Code05_TransportPlan2.num), (_java_key_12 := Code05_TransportPlan2.quesv[i]), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]
                ((_java_obj_14 := Code05_TransportPlan2.num), (_java_key_15 := Code05_TransportPlan2.lca[i]), jset(_java_obj_14, _java_key_15, jcast('int', (jget(_java_obj_14, _java_key_15) - 2))))[2]
                Code05_TransportPlan2.beyond = jcast('int', (Code05_TransportPlan2.beyond + 1))
            i = jcast('int', (i + 1))
        return jcast('boolean', ((Code05_TransportPlan2.beyond == 0) or Code05_TransportPlan2.dfs(1)))

    # 至少要减少多少边权
    atLeast = 0
    # 超过要求的运输计划有几个
    beyond = 0
    # dfs方法的递归版改迭代版
    # 不会改，看讲解118，讲了怎么从递归版改成迭代版
    @staticmethod
    def dfs(root):
        root = jcast('int', root)
        Code05_TransportPlan2.stackSize = jcast('int', 0)
        Code05_TransportPlan2.push(root, 0, 0, jcast('int', (-1)))
        while (Code05_TransportPlan2.stackSize > 0):
            Code05_TransportPlan2.pop()
            if (Code05_TransportPlan2.e == jcast('int', (-1))):
                Code05_TransportPlan2.e = jcast('int', Code05_TransportPlan2.headEdge[Code05_TransportPlan2.u])
            else:
                Code05_TransportPlan2.e = jcast('int', Code05_TransportPlan2.edgeNext[Code05_TransportPlan2.e])
            if (Code05_TransportPlan2.e != 0):
                Code05_TransportPlan2.push(Code05_TransportPlan2.u, Code05_TransportPlan2.f_data, Code05_TransportPlan2.w, Code05_TransportPlan2.e)
                if (Code05_TransportPlan2.edgeTo[Code05_TransportPlan2.e] != Code05_TransportPlan2.f_data):
                    Code05_TransportPlan2.push(Code05_TransportPlan2.edgeTo[Code05_TransportPlan2.e], Code05_TransportPlan2.u, Code05_TransportPlan2.edgeWeight[Code05_TransportPlan2.e], jcast('int', (-1)))
            else:
                e = jcast('int', Code05_TransportPlan2.headEdge[Code05_TransportPlan2.u])
                v = 0
                while (e != 0):
                    v = jcast('int', Code05_TransportPlan2.edgeTo[e])
                    if (v != Code05_TransportPlan2.f_data):
                        Code05_TransportPlan2.num[Code05_TransportPlan2.u] = jcast('int', jcast('int', jadd(Code05_TransportPlan2.num[Code05_TransportPlan2.u], Code05_TransportPlan2.num[v])))
                    e = jcast('int', Code05_TransportPlan2.edgeNext[e])
                if ((Code05_TransportPlan2.num[Code05_TransportPlan2.u] == Code05_TransportPlan2.beyond) and (Code05_TransportPlan2.w >= Code05_TransportPlan2.atLeast)):
                    return jcast('boolean', True)
        return jcast('boolean', False)

    @staticmethod
    def compute():
        Code05_TransportPlan2.tarjan(1)
        l = jcast('int', 0)
        r = jcast('int', Code05_TransportPlan2.maxCost)
        mid = 0
        ans = jcast('int', 0)
        while (l <= r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if Code05_TransportPlan2.f(mid):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code05_TransportPlan2.FastIO(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')), False)
        Code05_TransportPlan2.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_TransportPlan2.build()
        Code05_TransportPlan2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code05_TransportPlan2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code05_TransportPlan2.addEdge(u, v, w)
            Code05_TransportPlan2.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code05_TransportPlan2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code05_TransportPlan2.quesu[i] = jcast('int', u)
            Code05_TransportPlan2.quesv[i] = jcast('int', v)
            Code05_TransportPlan2.addQuery(u, v, i)
            Code05_TransportPlan2.addQuery(v, u, i)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code05_TransportPlan2.compute())
        jcall(out, 'flush')
        jcall(out, 'close')

    # IO工具类
    class FastIO:
        __java_fields__ = {'SIZE': 'SIZE', 'buf': 'buf', 'pos': 'pos', 'count': 'count', 'is': 'is_'}
        # SIZE：实例字段，在构造函数中初始化。
        # buf：实例字段，在构造函数中初始化。
        # pos：实例字段，在构造函数中初始化。
        # count：实例字段，在构造函数中初始化。
        # is_：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.buf = jarray('byte', [self.SIZE])
            self.pos = jcast('int', 0)
            self.count = jcast('int', 0)
            self.is_ = jget(System, 'in')

        def readByte(self):
            if (self.count == jcast('int', (-1))):
                return jcast('int', jcast('int', (-1)))
            if (self.pos >= self.count):
                self.pos = jcast('int', 0)
                self.count = jcast('int', jcall(self.is_, 'read', self.buf))
                if (self.count == jcast('int', (-1))):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', jcast('int', (self.buf[((_java_obj_16 := self), (_java_key_17 := 'pos'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))), _java_old_18)[4]] & 255)))

        def nextInt(self):
            c = 0
            value = jcast('int', 0)
            neg = jcast('boolean', False)
            while True:
                c = jcast('int', self.readByte())
                if (c == jcast('int', (-1))):
                    return jcast('int', jcast('int', (-1)))
                if not ((c <= jchar(' '))):
                    break
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            while ((c >= jchar('0')) and (c <= jchar('9'))):
                value = jcast('int', jcast('int', jadd(jcast('int', (value * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('int', (jcast('int', (-value)) if neg else value))

        def __init__(self, *args, _java_ctor=None):
            self.SIZE = jcast('int', jcast('int', (1 << (20 & 31))))
            self.buf = None
            self.pos = jcast('int', 0)
            self.count = jcast('int', 0)
            self.is_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_TransportPlan2.FastIO.FastIO")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_TransportPlan2.MAXN = jcast('int', 300001)
Code05_TransportPlan2.MAXM = jcast('int', 300001)
Code05_TransportPlan2.n = jcast('int', 0)
Code05_TransportPlan2.m = jcast('int', 0)
Code05_TransportPlan2.num = jarray('int', [Code05_TransportPlan2.MAXN])
Code05_TransportPlan2.headEdge = jarray('int', [Code05_TransportPlan2.MAXN])
Code05_TransportPlan2.edgeNext = jarray('int', [jcast('int', (Code05_TransportPlan2.MAXN << (1 & 31)))])
Code05_TransportPlan2.edgeTo = jarray('int', [jcast('int', (Code05_TransportPlan2.MAXN << (1 & 31)))])
Code05_TransportPlan2.edgeWeight = jarray('int', [jcast('int', (Code05_TransportPlan2.MAXN << (1 & 31)))])
Code05_TransportPlan2.tcnt = jcast('int', 0)
Code05_TransportPlan2.headQuery = jarray('int', [Code05_TransportPlan2.MAXN])
Code05_TransportPlan2.queryNext = jarray('int', [jcast('int', (Code05_TransportPlan2.MAXM << (1 & 31)))])
Code05_TransportPlan2.queryTo = jarray('int', [jcast('int', (Code05_TransportPlan2.MAXM << (1 & 31)))])
Code05_TransportPlan2.queryIndex = jarray('int', [jcast('int', (Code05_TransportPlan2.MAXM << (1 & 31)))])
Code05_TransportPlan2.qcnt = jcast('int', 0)
Code05_TransportPlan2.visited = jarray('boolean', [Code05_TransportPlan2.MAXN])
Code05_TransportPlan2.unionfind = jarray('int', [Code05_TransportPlan2.MAXN])
Code05_TransportPlan2.quesu = jarray('int', [Code05_TransportPlan2.MAXM])
Code05_TransportPlan2.quesv = jarray('int', [Code05_TransportPlan2.MAXM])
Code05_TransportPlan2.distance = jarray('int', [Code05_TransportPlan2.MAXN])
Code05_TransportPlan2.lca = jarray('int', [Code05_TransportPlan2.MAXM])
Code05_TransportPlan2.cost = jarray('int', [Code05_TransportPlan2.MAXM])
Code05_TransportPlan2.maxCost = jcast('int', 0)
Code05_TransportPlan2.stack = jarray('int', [Code05_TransportPlan2.MAXN])
Code05_TransportPlan2.ufwe = jarray('int', [Code05_TransportPlan2.MAXN, 4])
Code05_TransportPlan2.stackSize = jcast('int', 0)
Code05_TransportPlan2.u = jcast('int', 0)
Code05_TransportPlan2.f_data = jcast('int', 0)
Code05_TransportPlan2.w = jcast('int', 0)
Code05_TransportPlan2.e = jcast('int', 0)
Code05_TransportPlan2.atLeast = jcast('int', 0)
Code05_TransportPlan2.beyond = jcast('int', 0)

if __name__ == '__main__':
    Code05_TransportPlan2.main([])
