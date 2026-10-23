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

# 松鼠的新家(递归版)
# 有n个节点形成一棵树
# 给定一个由点编号组成的数组，表示松鼠依次要去往的地点
# 松鼠每走到一个节点都必须拿一个糖果，否则松鼠就停止前进
# 松鼠来到最后一个地点时不需要吃糖果
# 打印每个节点上至少准备多少糖果才能让松鼠依次走完数组里的节点
# 测试链接 : https://www.luogu.com.cn/problem/P3258
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
# 对应实现可参考 Code02_SquirrelHome2.py
class Code02_SquirrelHome1:
    __java_fields__ = {'MAXN': 'MAXN', 'travel': 'travel', 'num': 'num', 'headEdge': 'headEdge', 'edgeNext': 'edgeNext', 'edgeTo': 'edgeTo', 'tcnt': 'tcnt', 'headQuery': 'headQuery', 'queryNext': 'queryNext', 'queryTo': 'queryTo', 'queryIndex': 'queryIndex', 'qcnt': 'qcnt', 'visited': 'visited', 'unionfind': 'unionfind', 'father': 'father', 'ans': 'ans'}
    MAXN = 0
    # 依次去往节点的顺序
    travel = None
    # 每个节点需要分配多少糖果
    num = None
    # 链式前向星建图
    headEdge = None
    edgeNext = None
    edgeTo = None
    tcnt = 0
    # 以下结构都是tarjan算法所需要的
    headQuery = None
    queryNext = None
    queryTo = None
    queryIndex = None
    qcnt = 0
    visited = None
    # unionfind数组是tarjan算法专用的并查集结构
    unionfind = None
    # father数组不用作并查集，就是记录每个节点的父亲节点
    father = None
    # ans数组是tarjan算法的输出结果，记录每次旅行两端点的最低公共祖先
    ans = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        jstatic('Arrays', 'fill', Code02_SquirrelHome1.num, 1, jcast('int', jadd(n, 1)), 0)
        Code02_SquirrelHome1.tcnt = jcast('int', jset(Code02_SquirrelHome1, 'qcnt', 1))
        jstatic('Arrays', 'fill', Code02_SquirrelHome1.headEdge, 1, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code02_SquirrelHome1.headQuery, 1, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code02_SquirrelHome1.visited, 1, jcast('int', jadd(n, 1)), False)
        i = jcast('int', 1)
        while (i <= n):
            Code02_SquirrelHome1.unionfind[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code02_SquirrelHome1.edgeNext[Code02_SquirrelHome1.tcnt] = jcast('int', Code02_SquirrelHome1.headEdge[u])
        Code02_SquirrelHome1.edgeTo[Code02_SquirrelHome1.tcnt] = jcast('int', v)
        jset(Code02_SquirrelHome1.headEdge, u, ((_java_obj_1 := Code02_SquirrelHome1), (_java_key_2 := 'tcnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def addQuery(u, v, i):
        u = jcast('int', u)
        v = jcast('int', v)
        i = jcast('int', i)
        Code02_SquirrelHome1.queryNext[Code02_SquirrelHome1.qcnt] = jcast('int', Code02_SquirrelHome1.headQuery[u])
        Code02_SquirrelHome1.queryTo[Code02_SquirrelHome1.qcnt] = jcast('int', v)
        Code02_SquirrelHome1.queryIndex[Code02_SquirrelHome1.qcnt] = jcast('int', i)
        jset(Code02_SquirrelHome1.headQuery, u, ((_java_obj_4 := Code02_SquirrelHome1), (_java_key_5 := 'qcnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4])

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code02_SquirrelHome1.unionfind[i]):
            jset(Code02_SquirrelHome1.unionfind, i, Code02_SquirrelHome1.find(Code02_SquirrelHome1.unionfind[i]))
        return jcast('int', Code02_SquirrelHome1.unionfind[i])

    @staticmethod
    def tarjan(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code02_SquirrelHome1.visited[u] = jcast('boolean', True)
        e = jcast('int', Code02_SquirrelHome1.headEdge[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code02_SquirrelHome1.edgeTo[e])
            if (v != f):
                Code02_SquirrelHome1.tarjan(v, u)
            e = jcast('int', Code02_SquirrelHome1.edgeNext[e])
        e = jcast('int', Code02_SquirrelHome1.headQuery[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code02_SquirrelHome1.queryTo[e])
            if Code02_SquirrelHome1.visited[v]:
                jset(Code02_SquirrelHome1.ans, Code02_SquirrelHome1.queryIndex[e], Code02_SquirrelHome1.find(v))
            e = jcast('int', Code02_SquirrelHome1.queryNext[e])
        Code02_SquirrelHome1.unionfind[u] = jcast('int', f)
        Code02_SquirrelHome1.father[u] = jcast('int', f)

    @staticmethod
    def dfs(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code02_SquirrelHome1.headEdge[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code02_SquirrelHome1.edgeTo[e])
            if (v != f):
                Code02_SquirrelHome1.dfs(v, u)
            e = jcast('int', Code02_SquirrelHome1.edgeNext[e])
        e = jcast('int', Code02_SquirrelHome1.headEdge[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code02_SquirrelHome1.edgeTo[e])
            if (v != f):
                Code02_SquirrelHome1.num[u] = jcast('int', jcast('int', jadd(Code02_SquirrelHome1.num[u], Code02_SquirrelHome1.num[v])))
            e = jcast('int', Code02_SquirrelHome1.edgeNext[e])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code02_SquirrelHome1.build(n)
        i = jcast('int', 1)
        while (i <= n):
            jcall(in_, 'nextToken')
            Code02_SquirrelHome1.travel[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_SquirrelHome1.addEdge(u, v)
            Code02_SquirrelHome1.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < n):
            Code02_SquirrelHome1.addQuery(Code02_SquirrelHome1.travel[i], Code02_SquirrelHome1.travel[jcast('int', jadd(i, 1))], i)
            Code02_SquirrelHome1.addQuery(Code02_SquirrelHome1.travel[jcast('int', jadd(i, 1))], Code02_SquirrelHome1.travel[i], i)
            i = jcast('int', (i + 1))
        Code02_SquirrelHome1.compute(n)
        i = jcast('int', 1)
        while (i <= n):
            jcall(out, 'println', Code02_SquirrelHome1.num[i])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute(n):
        n = jcast('int', n)
        Code02_SquirrelHome1.tarjan(1, 0)
        i = jcast('int', 1)
        u = 0
        v = 0
        lca = 0
        lcafather = 0
        while (i < n):
            u = jcast('int', Code02_SquirrelHome1.travel[i])
            v = jcast('int', Code02_SquirrelHome1.travel[jcast('int', jadd(i, 1))])
            lca = jcast('int', Code02_SquirrelHome1.ans[i])
            lcafather = jcast('int', Code02_SquirrelHome1.father[lca])
            Code02_SquirrelHome1.num[u] = jcast('int', (Code02_SquirrelHome1.num[u] + 1))
            Code02_SquirrelHome1.num[v] = jcast('int', (Code02_SquirrelHome1.num[v] + 1))
            Code02_SquirrelHome1.num[lca] = jcast('int', (Code02_SquirrelHome1.num[lca] - 1))
            Code02_SquirrelHome1.num[lcafather] = jcast('int', (Code02_SquirrelHome1.num[lcafather] - 1))
            i = jcast('int', (i + 1))
        Code02_SquirrelHome1.dfs(1, 0)
        i = jcast('int', 2)
        while (i <= n):
            ((_java_obj_7 := Code02_SquirrelHome1.num), (_java_key_8 := Code02_SquirrelHome1.travel[i]), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_SquirrelHome1.MAXN = jcast('int', 300001)
Code02_SquirrelHome1.travel = jarray('int', [Code02_SquirrelHome1.MAXN])
Code02_SquirrelHome1.num = jarray('int', [Code02_SquirrelHome1.MAXN])
Code02_SquirrelHome1.headEdge = jarray('int', [Code02_SquirrelHome1.MAXN])
Code02_SquirrelHome1.edgeNext = jarray('int', [jcast('int', (Code02_SquirrelHome1.MAXN << (1 & 31)))])
Code02_SquirrelHome1.edgeTo = jarray('int', [jcast('int', (Code02_SquirrelHome1.MAXN << (1 & 31)))])
Code02_SquirrelHome1.tcnt = jcast('int', 0)
Code02_SquirrelHome1.headQuery = jarray('int', [Code02_SquirrelHome1.MAXN])
Code02_SquirrelHome1.queryNext = jarray('int', [jcast('int', (Code02_SquirrelHome1.MAXN << (1 & 31)))])
Code02_SquirrelHome1.queryTo = jarray('int', [jcast('int', (Code02_SquirrelHome1.MAXN << (1 & 31)))])
Code02_SquirrelHome1.queryIndex = jarray('int', [jcast('int', (Code02_SquirrelHome1.MAXN << (1 & 31)))])
Code02_SquirrelHome1.qcnt = jcast('int', 0)
Code02_SquirrelHome1.visited = jarray('boolean', [Code02_SquirrelHome1.MAXN])
Code02_SquirrelHome1.unionfind = jarray('int', [Code02_SquirrelHome1.MAXN])
Code02_SquirrelHome1.father = jarray('int', [Code02_SquirrelHome1.MAXN])
Code02_SquirrelHome1.ans = jarray('int', [Code02_SquirrelHome1.MAXN])

if __name__ == '__main__':
    Code02_SquirrelHome1.main([])
