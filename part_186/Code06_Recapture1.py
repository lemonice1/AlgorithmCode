# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 夺回据点，Python版
# 一共n个据点，m条双向道路，所有据点连通在一起
# 每个据点给定点权，代表夺取这个据点需要的花费
# 当夺取某个据点之后，再夺取相邻的据点，认为没有花费
# 你可以按照任意顺序夺取所有据点，但是过程中必须保证
# 那些还没夺取的据点都在同一个连通区里，不被已经夺取的据点隔开
# 打印最小的总花费
# 1 <= n、m <= 10^5
# 1 <= 点权 <= 10^9
# 测试链接 : https://leetcode.cn/problems/s5kipK/
# 在线评测时提交题目要求的方法接口，并一并提供使用到的公共辅助模块
class Code06_Recapture1:
    __java_fields__ = {}
    class Solution:
        __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'cutVertex': 'cutVertex', 'vbccArr': 'vbccArr'}
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
        cutVertex = None
        vbccArr = None
        @staticmethod
        def prepare():
            jset(Code06_Recapture1.Solution, 'cntg', jset(Code06_Recapture1.Solution, 'cntd', jset(Code06_Recapture1.Solution, 'top', 0)))
            i = jcast('int', 1)
            while (i <= Code06_Recapture1.Solution.n):
                jset(Code06_Recapture1.Solution.head, i, jset(Code06_Recapture1.Solution.dfn, i, jset(Code06_Recapture1.Solution.low, i, 0)))
                jset(Code06_Recapture1.Solution.cutVertex, i, False)
                i = jcast('int', (i + 1))
            jcall(Code06_Recapture1.Solution.vbccArr, 'clear')

        @staticmethod
        def addEdge(u, v):
            u = jcast('int', u)
            v = jcast('int', v)
            jset(Code06_Recapture1.Solution.nxt, ((_java_obj_1 := Code06_Recapture1.Solution), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_Recapture1.Solution.head[u])
            jset(Code06_Recapture1.Solution.to, Code06_Recapture1.Solution.cntg, v)
            jset(Code06_Recapture1.Solution.head, u, Code06_Recapture1.Solution.cntg)

        @staticmethod
        def tarjan(u, root):
            u = jcast('int', u)
            root = jcast('boolean', root)
            jset(Code06_Recapture1.Solution.dfn, u, jset(Code06_Recapture1.Solution.low, u, ((_java_obj_4 := Code06_Recapture1.Solution), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
            jset(Code06_Recapture1.Solution.sta, ((_java_obj_7 := Code06_Recapture1.Solution), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
            son = jcast('int', 0)
            e = jcast('int', Code06_Recapture1.Solution.head[u])
            while (e > 0):
                v = jcast('int', Code06_Recapture1.Solution.to[e])
                if (Code06_Recapture1.Solution.dfn[v] == 0):
                    son = jcast('int', (son + 1))
                    Code06_Recapture1.Solution.tarjan(v, False)
                    jset(Code06_Recapture1.Solution.low, u, jstatic('Math', 'min', Code06_Recapture1.Solution.low[u], Code06_Recapture1.Solution.low[v]))
                    if (Code06_Recapture1.Solution.low[v] >= Code06_Recapture1.Solution.dfn[u]):
                        if ((not root) or (son >= 2)):
                            jset(Code06_Recapture1.Solution.cutVertex, u, True)
                        list = jnew('ArrayList')
                        jcall(list, 'add', u)
                        pop = 0
                        while True:
                            pop = jcast('int', Code06_Recapture1.Solution.sta[((_java_obj_10 := Code06_Recapture1.Solution), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                            jcall(list, 'add', pop)
                            if not ((pop != v)):
                                break
                        jcall(Code06_Recapture1.Solution.vbccArr, 'add', list)
                else:
                    jset(Code06_Recapture1.Solution.low, u, jstatic('Math', 'min', Code06_Recapture1.Solution.low[u], Code06_Recapture1.Solution.dfn[v]))
                e = jcast('int', Code06_Recapture1.Solution.nxt[e])

        @staticmethod
        def minimumCost(cost, roads):
            jset(Code06_Recapture1.Solution, 'n', jget(cost, 'length'))
            jset(Code06_Recapture1.Solution, 'm', jget(roads, 'length'))
            Code06_Recapture1.Solution.prepare()
            i = jcast('int', 0)
            u = 0
            v = 0
            while (i < Code06_Recapture1.Solution.m):
                u = jcast('int', jcast('int', jadd(roads[i][0], 1)))
                v = jcast('int', jcast('int', jadd(roads[i][1], 1)))
                Code06_Recapture1.Solution.addEdge(u, v)
                Code06_Recapture1.Solution.addEdge(v, u)
                i = jcast('int', (i + 1))
            Code06_Recapture1.Solution.tarjan(1, True)
            ans = jcast('long', 0)
            if (jcall(Code06_Recapture1.Solution.vbccArr, 'size') == 1):
                ans = jcast('long', jget(Long, 'MAX_VALUE'))
                i = jcast('int', 0)
                while (i < Code06_Recapture1.Solution.n):
                    ans = jcast('long', jstatic('Math', 'min', ans, cost[i]))
                    i = jcast('int', (i + 1))
            else:
                maxVal = jcast('int', jget(Integer, 'MIN_VALUE'))
                for vbcc in Code06_Recapture1.Solution.vbccArr:
                    cut = jcast('int', 0)
                    val = jcast('int', jget(Integer, 'MAX_VALUE'))
                    for cur in vbcc:
                        if Code06_Recapture1.Solution.cutVertex[cur]:
                            cut = jcast('int', (cut + 1))
                        else:
                            val = jcast('int', jstatic('Math', 'min', val, cost[jcast('int', (cur - 1))]))
                    if (cut == 1):
                        ans = jcast('long', jcast('long', jadd(ans, val)))
                        maxVal = jcast('int', jstatic('Math', 'max', maxVal, val))
                ans = jcast('long', jcast('long', (ans - maxVal)))
            return jcast('long', ans)

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_Recapture1.Solution.MAXN = jcast('int', 100001)
Code06_Recapture1.Solution.MAXM = jcast('int', 100001)
Code06_Recapture1.Solution.n = jcast('int', 0)
Code06_Recapture1.Solution.m = jcast('int', 0)
Code06_Recapture1.Solution.head = jarray('int', [Code06_Recapture1.Solution.MAXN])
Code06_Recapture1.Solution.nxt = jarray('int', [jcast('int', (Code06_Recapture1.Solution.MAXM << (1 & 31)))])
Code06_Recapture1.Solution.to = jarray('int', [jcast('int', (Code06_Recapture1.Solution.MAXM << (1 & 31)))])
Code06_Recapture1.Solution.cntg = jcast('int', 0)
Code06_Recapture1.Solution.dfn = jarray('int', [Code06_Recapture1.Solution.MAXN])
Code06_Recapture1.Solution.low = jarray('int', [Code06_Recapture1.Solution.MAXN])
Code06_Recapture1.Solution.cntd = jcast('int', 0)
Code06_Recapture1.Solution.sta = jarray('int', [Code06_Recapture1.Solution.MAXN])
Code06_Recapture1.Solution.top = jcast('int', 0)
Code06_Recapture1.Solution.cutVertex = jarray('boolean', [Code06_Recapture1.Solution.MAXN])
Code06_Recapture1.Solution.vbccArr = jnew('ArrayList')
