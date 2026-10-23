# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 松鼠的新家(迭代版)
# 有n个节点形成一棵树
# 给定一个由点编号组成的数组，表示松鼠依次要去往的地点
# 松鼠每走到一个节点都必须拿一个糖果，否则松鼠就停止前进
# 松鼠来到最后一个地点时不需要吃糖果
# 打印每个节点上至少准备多少糖果才能让松鼠依次走完数组里的节点
# 测试链接 : https://www.luogu.com.cn/problem/P3258
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_SquirrelHome2:
    __java_fields__ = {'MAXN': 'MAXN', 'travel': 'travel', 'num': 'num', 'headEdge': 'headEdge', 'edgeNext': 'edgeNext', 'edgeTo': 'edgeTo', 'tcnt': 'tcnt', 'headQuery': 'headQuery', 'queryNext': 'queryNext', 'queryTo': 'queryTo', 'queryIndex': 'queryIndex', 'qcnt': 'qcnt', 'visited': 'visited', 'unionfind': 'unionfind', 'father': 'father', 'ans': 'ans', 'stack': 'stack', 'ufe': 'ufe', 'stackSize': 'stackSize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    travel = None
    num = None
    headEdge = None
    edgeNext = None
    edgeTo = None
    tcnt = 0
    headQuery = None
    queryNext = None
    queryTo = None
    queryIndex = None
    qcnt = 0
    visited = None
    unionfind = None
    father = None
    ans = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        jstatic('Arrays', 'fill', Code02_SquirrelHome2.num, 1, jcast('int', jadd(n, 1)), 0)
        Code02_SquirrelHome2.tcnt = jcast('int', jset(Code02_SquirrelHome2, 'qcnt', 1))
        jstatic('Arrays', 'fill', Code02_SquirrelHome2.headEdge, 1, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code02_SquirrelHome2.headQuery, 1, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code02_SquirrelHome2.visited, 1, jcast('int', jadd(n, 1)), False)
        i = jcast('int', 1)
        while (i <= n):
            Code02_SquirrelHome2.unionfind[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code02_SquirrelHome2.edgeNext[Code02_SquirrelHome2.tcnt] = jcast('int', Code02_SquirrelHome2.headEdge[u])
        Code02_SquirrelHome2.edgeTo[Code02_SquirrelHome2.tcnt] = jcast('int', v)
        jset(Code02_SquirrelHome2.headEdge, u, ((_java_obj_1 := Code02_SquirrelHome2), (_java_key_2 := 'tcnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def addQuery(u, v, i):
        u = jcast('int', u)
        v = jcast('int', v)
        i = jcast('int', i)
        Code02_SquirrelHome2.queryNext[Code02_SquirrelHome2.qcnt] = jcast('int', Code02_SquirrelHome2.headQuery[u])
        Code02_SquirrelHome2.queryTo[Code02_SquirrelHome2.qcnt] = jcast('int', v)
        Code02_SquirrelHome2.queryIndex[Code02_SquirrelHome2.qcnt] = jcast('int', i)
        jset(Code02_SquirrelHome2.headQuery, u, ((_java_obj_4 := Code02_SquirrelHome2), (_java_key_5 := 'qcnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4])

    # find方法的递归版改迭代版
    stack = None
    @staticmethod
    def find(i):
        i = jcast('int', i)
        size = jcast('int', 0)
        while (i != Code02_SquirrelHome2.unionfind[i]):
            jset(Code02_SquirrelHome2.stack, ((_java_old_7 := size), (size := jcast('int', (size + (1)))), _java_old_7)[2], i)
            i = jcast('int', Code02_SquirrelHome2.unionfind[i])
        while (size > 0):
            jset(Code02_SquirrelHome2.unionfind, Code02_SquirrelHome2.stack[(size := jcast('int', (size + (-1))))], i)
        return jcast('int', i)

    # tarjan方法的递归版改迭代版
    # 不会改，看讲解118，讲了怎么从递归版改成迭代版
    ufe = None
    stackSize = 0
    u = 0
    f = 0
    e = 0
    @staticmethod
    def push(u, f, e):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', e)
        jset(Code02_SquirrelHome2.ufe[Code02_SquirrelHome2.stackSize], 0, u)
        jset(Code02_SquirrelHome2.ufe[Code02_SquirrelHome2.stackSize], 1, f)
        jset(Code02_SquirrelHome2.ufe[Code02_SquirrelHome2.stackSize], 2, e)
        Code02_SquirrelHome2.stackSize = jcast('int', (Code02_SquirrelHome2.stackSize + 1))

    @staticmethod
    def pop():
        Code02_SquirrelHome2.stackSize = jcast('int', (Code02_SquirrelHome2.stackSize - 1))
        Code02_SquirrelHome2.u = jcast('int', Code02_SquirrelHome2.ufe[Code02_SquirrelHome2.stackSize][0])
        Code02_SquirrelHome2.f = jcast('int', Code02_SquirrelHome2.ufe[Code02_SquirrelHome2.stackSize][1])
        Code02_SquirrelHome2.e = jcast('int', Code02_SquirrelHome2.ufe[Code02_SquirrelHome2.stackSize][2])

    @staticmethod
    def tarjan(root):
        root = jcast('int', root)
        Code02_SquirrelHome2.stackSize = jcast('int', 0)
        Code02_SquirrelHome2.push(root, 0, jcast('int', (-1)))
        while (Code02_SquirrelHome2.stackSize > 0):
            Code02_SquirrelHome2.pop()
            if (Code02_SquirrelHome2.e == jcast('int', (-1))):
                Code02_SquirrelHome2.visited[Code02_SquirrelHome2.u] = jcast('boolean', True)
                Code02_SquirrelHome2.e = jcast('int', Code02_SquirrelHome2.headEdge[Code02_SquirrelHome2.u])
            else:
                Code02_SquirrelHome2.e = jcast('int', Code02_SquirrelHome2.edgeNext[Code02_SquirrelHome2.e])
            if (Code02_SquirrelHome2.e != 0):
                Code02_SquirrelHome2.push(Code02_SquirrelHome2.u, Code02_SquirrelHome2.f, Code02_SquirrelHome2.e)
                if (Code02_SquirrelHome2.edgeTo[Code02_SquirrelHome2.e] != Code02_SquirrelHome2.f):
                    Code02_SquirrelHome2.push(Code02_SquirrelHome2.edgeTo[Code02_SquirrelHome2.e], Code02_SquirrelHome2.u, jcast('int', (-1)))
            else:
                q = jcast('int', Code02_SquirrelHome2.headQuery[Code02_SquirrelHome2.u])
                v = 0
                while (q != 0):
                    v = jcast('int', Code02_SquirrelHome2.queryTo[q])
                    if Code02_SquirrelHome2.visited[v]:
                        jset(Code02_SquirrelHome2.ans, Code02_SquirrelHome2.queryIndex[q], Code02_SquirrelHome2.find(v))
                    q = jcast('int', Code02_SquirrelHome2.queryNext[q])
                Code02_SquirrelHome2.unionfind[Code02_SquirrelHome2.u] = jcast('int', Code02_SquirrelHome2.f)
                Code02_SquirrelHome2.father[Code02_SquirrelHome2.u] = jcast('int', Code02_SquirrelHome2.f)

    # dfs方法的递归版改迭代版
    # 不会改，看讲解118，讲了怎么从递归版改成迭代版
    @staticmethod
    def dfs(root):
        root = jcast('int', root)
        Code02_SquirrelHome2.stackSize = jcast('int', 0)
        Code02_SquirrelHome2.push(root, 0, jcast('int', (-1)))
        while (Code02_SquirrelHome2.stackSize > 0):
            Code02_SquirrelHome2.pop()
            if (Code02_SquirrelHome2.e == jcast('int', (-1))):
                Code02_SquirrelHome2.e = jcast('int', Code02_SquirrelHome2.headEdge[Code02_SquirrelHome2.u])
            else:
                Code02_SquirrelHome2.e = jcast('int', Code02_SquirrelHome2.edgeNext[Code02_SquirrelHome2.e])
            if (Code02_SquirrelHome2.e != 0):
                Code02_SquirrelHome2.push(Code02_SquirrelHome2.u, Code02_SquirrelHome2.f, Code02_SquirrelHome2.e)
                if (Code02_SquirrelHome2.edgeTo[Code02_SquirrelHome2.e] != Code02_SquirrelHome2.f):
                    Code02_SquirrelHome2.push(Code02_SquirrelHome2.edgeTo[Code02_SquirrelHome2.e], Code02_SquirrelHome2.u, jcast('int', (-1)))
            else:
                e = jcast('int', Code02_SquirrelHome2.headEdge[Code02_SquirrelHome2.u])
                v = 0
                while (e != 0):
                    v = jcast('int', Code02_SquirrelHome2.edgeTo[e])
                    if (v != Code02_SquirrelHome2.f):
                        Code02_SquirrelHome2.num[Code02_SquirrelHome2.u] = jcast('int', jcast('int', jadd(Code02_SquirrelHome2.num[Code02_SquirrelHome2.u], Code02_SquirrelHome2.num[v])))
                    e = jcast('int', Code02_SquirrelHome2.edgeNext[e])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code02_SquirrelHome2.build(n)
        i = jcast('int', 1)
        while (i <= n):
            jcall(in_, 'nextToken')
            Code02_SquirrelHome2.travel[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_SquirrelHome2.addEdge(u, v)
            Code02_SquirrelHome2.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < n):
            Code02_SquirrelHome2.addQuery(Code02_SquirrelHome2.travel[i], Code02_SquirrelHome2.travel[jcast('int', jadd(i, 1))], i)
            Code02_SquirrelHome2.addQuery(Code02_SquirrelHome2.travel[jcast('int', jadd(i, 1))], Code02_SquirrelHome2.travel[i], i)
            i = jcast('int', (i + 1))
        Code02_SquirrelHome2.compute(n)
        i = jcast('int', 1)
        while (i <= n):
            jcall(out, 'println', Code02_SquirrelHome2.num[i])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute(n):
        n = jcast('int', n)
        Code02_SquirrelHome2.tarjan(1)
        i = jcast('int', 1)
        u = 0
        v = 0
        lca = 0
        lcafather = 0
        while (i < n):
            u = jcast('int', Code02_SquirrelHome2.travel[i])
            v = jcast('int', Code02_SquirrelHome2.travel[jcast('int', jadd(i, 1))])
            lca = jcast('int', Code02_SquirrelHome2.ans[i])
            lcafather = jcast('int', Code02_SquirrelHome2.father[lca])
            Code02_SquirrelHome2.num[u] = jcast('int', (Code02_SquirrelHome2.num[u] + 1))
            Code02_SquirrelHome2.num[v] = jcast('int', (Code02_SquirrelHome2.num[v] + 1))
            Code02_SquirrelHome2.num[lca] = jcast('int', (Code02_SquirrelHome2.num[lca] - 1))
            Code02_SquirrelHome2.num[lcafather] = jcast('int', (Code02_SquirrelHome2.num[lcafather] - 1))
            i = jcast('int', (i + 1))
        Code02_SquirrelHome2.dfs(1)
        i = jcast('int', 2)
        while (i <= n):
            ((_java_obj_8 := Code02_SquirrelHome2.num), (_java_key_9 := Code02_SquirrelHome2.travel[i]), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (-1)))), _java_old_10)[4]
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_SquirrelHome2.MAXN = jcast('int', 300001)
Code02_SquirrelHome2.travel = jarray('int', [Code02_SquirrelHome2.MAXN])
Code02_SquirrelHome2.num = jarray('int', [Code02_SquirrelHome2.MAXN])
Code02_SquirrelHome2.headEdge = jarray('int', [Code02_SquirrelHome2.MAXN])
Code02_SquirrelHome2.edgeNext = jarray('int', [jcast('int', (Code02_SquirrelHome2.MAXN << (1 & 31)))])
Code02_SquirrelHome2.edgeTo = jarray('int', [jcast('int', (Code02_SquirrelHome2.MAXN << (1 & 31)))])
Code02_SquirrelHome2.tcnt = jcast('int', 0)
Code02_SquirrelHome2.headQuery = jarray('int', [Code02_SquirrelHome2.MAXN])
Code02_SquirrelHome2.queryNext = jarray('int', [jcast('int', (Code02_SquirrelHome2.MAXN << (1 & 31)))])
Code02_SquirrelHome2.queryTo = jarray('int', [jcast('int', (Code02_SquirrelHome2.MAXN << (1 & 31)))])
Code02_SquirrelHome2.queryIndex = jarray('int', [jcast('int', (Code02_SquirrelHome2.MAXN << (1 & 31)))])
Code02_SquirrelHome2.qcnt = jcast('int', 0)
Code02_SquirrelHome2.visited = jarray('boolean', [Code02_SquirrelHome2.MAXN])
Code02_SquirrelHome2.unionfind = jarray('int', [Code02_SquirrelHome2.MAXN])
Code02_SquirrelHome2.father = jarray('int', [Code02_SquirrelHome2.MAXN])
Code02_SquirrelHome2.ans = jarray('int', [Code02_SquirrelHome2.MAXN])
Code02_SquirrelHome2.stack = jarray('int', [Code02_SquirrelHome2.MAXN])
Code02_SquirrelHome2.ufe = jarray('int', [Code02_SquirrelHome2.MAXN, 3])
Code02_SquirrelHome2.stackSize = jcast('int', 0)
Code02_SquirrelHome2.u = jcast('int', 0)
Code02_SquirrelHome2.f = jcast('int', 0)
Code02_SquirrelHome2.e = jcast('int', 0)

if __name__ == '__main__':
    Code02_SquirrelHome2.main([])
