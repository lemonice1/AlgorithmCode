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

# 割边模版题2，Python版
# 给定一张无向图，一共n个点、m条边
# 点的编号0~n-1，保证所有点连通
# 找出图中所有的割边，返回每条割边的两个端点
# 请保证原图即使有重边和自环，答案依然正确
# 1 <= n、m <= 10^5
# 测试链接 : https://leetcode.cn/problems/critical-connections-in-a-network/
# 在线评测时提交题目要求的方法接口，并一并提供使用到的公共辅助模块
class Code02_CutEdge1:
    __java_fields__ = {}
    class Solution:
        __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'cutEdge': 'cutEdge'}
        MAXN = 0
        MAXM = 0
        n = 0
        m = 0
        a = None
        b = None
        head = None
        nxt = None
        to = None
        cntg = 0
        dfn = None
        low = None
        cntd = 0
        cutEdge = None
        @staticmethod
        def prepare():
            jset(Code02_CutEdge1.Solution, 'cntg', 1)
            jset(Code02_CutEdge1.Solution, 'cntd', 0)
            i = jcast('int', 1)
            while (i <= Code02_CutEdge1.Solution.n):
                jset(Code02_CutEdge1.Solution.head, i, jset(Code02_CutEdge1.Solution.dfn, i, jset(Code02_CutEdge1.Solution.low, i, 0)))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code02_CutEdge1.Solution.m):
                jset(Code02_CutEdge1.Solution.cutEdge, i, False)
                i = jcast('int', (i + 1))

        @staticmethod
        def addEdge(u, v):
            u = jcast('int', u)
            v = jcast('int', v)
            jset(Code02_CutEdge1.Solution.nxt, ((_java_obj_1 := Code02_CutEdge1.Solution), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_CutEdge1.Solution.head[u])
            jset(Code02_CutEdge1.Solution.to, Code02_CutEdge1.Solution.cntg, v)
            jset(Code02_CutEdge1.Solution.head, u, Code02_CutEdge1.Solution.cntg)

        @staticmethod
        def tarjan(u, preEdge):
            u = jcast('int', u)
            preEdge = jcast('int', preEdge)
            jset(Code02_CutEdge1.Solution.dfn, u, jset(Code02_CutEdge1.Solution.low, u, ((_java_obj_4 := Code02_CutEdge1.Solution), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
            e = jcast('int', Code02_CutEdge1.Solution.head[u])
            while (e > 0):
                try:
                    if (jcast('int', (e ^ 1)) == preEdge):
                        raise JContinue(None)
                    v = jcast('int', Code02_CutEdge1.Solution.to[e])
                    if (Code02_CutEdge1.Solution.dfn[v] == 0):
                        Code02_CutEdge1.Solution.tarjan(v, e)
                        jset(Code02_CutEdge1.Solution.low, u, jstatic('Math', 'min', Code02_CutEdge1.Solution.low[u], Code02_CutEdge1.Solution.low[v]))
                        if (Code02_CutEdge1.Solution.low[v] > Code02_CutEdge1.Solution.dfn[u]):
                            jset(Code02_CutEdge1.Solution.cutEdge, jcast('int', (e >> (1 & 31))), True)
                    else:
                        jset(Code02_CutEdge1.Solution.low, u, jstatic('Math', 'min', Code02_CutEdge1.Solution.low[u], Code02_CutEdge1.Solution.dfn[v]))
                except JContinue as _java_control_7:
                    if _java_control_7.label not in (None,):
                        raise
                except JBreak as _java_control_7:
                    if _java_control_7.label not in (None,):
                        raise
                    break
                e = jcast('int', Code02_CutEdge1.Solution.nxt[e])

        @staticmethod
        def criticalConnections(nodeCnt, connections):
            nodeCnt = jcast('int', nodeCnt)
            jset(Code02_CutEdge1.Solution, 'n', nodeCnt)
            jset(Code02_CutEdge1.Solution, 'm', jcall(connections, 'size'))
            Code02_CutEdge1.Solution.prepare()
            i = jcast('int', 1)
            j = jcast('int', 0)
            while (i <= Code02_CutEdge1.Solution.m):
                jset(Code02_CutEdge1.Solution.a, i, jadd(jcall(jcall(connections, 'get', j), 'get', 0), 1))
                jset(Code02_CutEdge1.Solution.b, i, jadd(jcall(jcall(connections, 'get', j), 'get', 1), 1))
                Code02_CutEdge1.Solution.addEdge(Code02_CutEdge1.Solution.a[i], Code02_CutEdge1.Solution.b[i])
                Code02_CutEdge1.Solution.addEdge(Code02_CutEdge1.Solution.b[i], Code02_CutEdge1.Solution.a[i])
                i = jcast('int', (i + 1))
                j = jcast('int', (j + 1))
            Code02_CutEdge1.Solution.tarjan(1, 0)
            ans = jnew('ArrayList')
            i = jcast('int', 1)
            while (i <= Code02_CutEdge1.Solution.m):
                if Code02_CutEdge1.Solution.cutEdge[i]:
                    jcall(ans, 'add', jstatic('Arrays', 'asList', jcast('int', (Code02_CutEdge1.Solution.a[i] - 1)), jcast('int', (Code02_CutEdge1.Solution.b[i] - 1))))
                i = jcast('int', (i + 1))
            return ans

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_CutEdge1.Solution.MAXN = jcast('int', 100001)
Code02_CutEdge1.Solution.MAXM = jcast('int', 100001)
Code02_CutEdge1.Solution.n = jcast('int', 0)
Code02_CutEdge1.Solution.m = jcast('int', 0)
Code02_CutEdge1.Solution.a = jarray('int', [Code02_CutEdge1.Solution.MAXM])
Code02_CutEdge1.Solution.b = jarray('int', [Code02_CutEdge1.Solution.MAXM])
Code02_CutEdge1.Solution.head = jarray('int', [Code02_CutEdge1.Solution.MAXN])
Code02_CutEdge1.Solution.nxt = jarray('int', [jcast('int', (Code02_CutEdge1.Solution.MAXM << (1 & 31)))])
Code02_CutEdge1.Solution.to = jarray('int', [jcast('int', (Code02_CutEdge1.Solution.MAXM << (1 & 31)))])
Code02_CutEdge1.Solution.cntg = jcast('int', 0)
Code02_CutEdge1.Solution.dfn = jarray('int', [Code02_CutEdge1.Solution.MAXN])
Code02_CutEdge1.Solution.low = jarray('int', [Code02_CutEdge1.Solution.MAXN])
Code02_CutEdge1.Solution.cntd = jcast('int', 0)
Code02_CutEdge1.Solution.cutEdge = jarray('boolean', [Code02_CutEdge1.Solution.MAXM])
