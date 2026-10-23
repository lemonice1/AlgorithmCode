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

# 树上点差分模版(递归版)
# 有n个节点形成一棵树，一开始所有点权都是0
# 给定很多操作，每个操作(a,b)表示从a到b路径上所有点的点权增加1
# 所有操作完成后，返回树上的最大点权
# 测试链接 : https://www.luogu.com.cn/problem/P3128
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
# 对应实现可参考 Code01_MaxFlow2.py
class Code01_MaxFlow1:
    __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'power': 'power', 'num': 'num', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'deep': 'deep', 'stjump': 'stjump'}
    MAXN = 0
    LIMIT = 0
    power = 0
    @staticmethod
    def log2(n):
        n = jcast('int', n)
        ans = jcast('int', 0)
        while (jcast('int', (1 << (ans & 31))) <= jcast('int', (n >> (1 & 31)))):
            ans = jcast('int', (ans + 1))
        return jcast('int', ans)

    num = None
    head = None
    next = None
    to = None
    cnt = 0
    deep = None
    stjump = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code01_MaxFlow1.power = jcast('int', Code01_MaxFlow1.log2(n))
        jstatic('Arrays', 'fill', Code01_MaxFlow1.num, 1, jcast('int', jadd(n, 1)), 0)
        Code01_MaxFlow1.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code01_MaxFlow1.head, 1, jcast('int', jadd(n, 1)), 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code01_MaxFlow1.next[Code01_MaxFlow1.cnt] = jcast('int', Code01_MaxFlow1.head[u])
        Code01_MaxFlow1.to[Code01_MaxFlow1.cnt] = jcast('int', v)
        jset(Code01_MaxFlow1.head, u, ((_java_obj_1 := Code01_MaxFlow1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code01_MaxFlow1.deep[u] = jcast('int', jcast('int', jadd(Code01_MaxFlow1.deep[f], 1)))
        jset(Code01_MaxFlow1.stjump[u], 0, f)
        p = jcast('int', 1)
        while (p <= Code01_MaxFlow1.power):
            jset(Code01_MaxFlow1.stjump[u], p, Code01_MaxFlow1.stjump[Code01_MaxFlow1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code01_MaxFlow1.head[u])
        while (e != 0):
            if (Code01_MaxFlow1.to[e] != f):
                Code01_MaxFlow1.dfs1(Code01_MaxFlow1.to[e], u)
            e = jcast('int', Code01_MaxFlow1.next[e])

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code01_MaxFlow1.deep[a] < Code01_MaxFlow1.deep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', Code01_MaxFlow1.power)
        while (p >= 0):
            if (Code01_MaxFlow1.deep[Code01_MaxFlow1.stjump[a][p]] >= Code01_MaxFlow1.deep[b]):
                a = jcast('int', Code01_MaxFlow1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', Code01_MaxFlow1.power)
        while (p >= 0):
            if (Code01_MaxFlow1.stjump[a][p] != Code01_MaxFlow1.stjump[b][p]):
                a = jcast('int', Code01_MaxFlow1.stjump[a][p])
                b = jcast('int', Code01_MaxFlow1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code01_MaxFlow1.stjump[a][0])

    @staticmethod
    def dfs2(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code01_MaxFlow1.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code01_MaxFlow1.to[e])
            if (v != f):
                Code01_MaxFlow1.dfs2(v, u)
            e = jcast('int', Code01_MaxFlow1.next[e])
        e = jcast('int', Code01_MaxFlow1.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code01_MaxFlow1.to[e])
            if (v != f):
                Code01_MaxFlow1.num[u] = jcast('int', jcast('int', jadd(Code01_MaxFlow1.num[u], Code01_MaxFlow1.num[v])))
            e = jcast('int', Code01_MaxFlow1.next[e])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code01_MaxFlow1.build(n)
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_MaxFlow1.addEdge(u, v)
            Code01_MaxFlow1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code01_MaxFlow1.dfs1(1, 0)
        i = jcast('int', 1)
        u = 0
        v = 0
        lca = 0
        lcafather = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            lca = jcast('int', Code01_MaxFlow1.lca(u, v))
            lcafather = jcast('int', Code01_MaxFlow1.stjump[lca][0])
            Code01_MaxFlow1.num[u] = jcast('int', (Code01_MaxFlow1.num[u] + 1))
            Code01_MaxFlow1.num[v] = jcast('int', (Code01_MaxFlow1.num[v] + 1))
            Code01_MaxFlow1.num[lca] = jcast('int', (Code01_MaxFlow1.num[lca] - 1))
            Code01_MaxFlow1.num[lcafather] = jcast('int', (Code01_MaxFlow1.num[lcafather] - 1))
            i = jcast('int', (i + 1))
        Code01_MaxFlow1.dfs2(1, 0)
        max = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= n):
            max = jcast('int', jstatic('Math', 'max', max, Code01_MaxFlow1.num[i]))
            i = jcast('int', (i + 1))
        jcall(out, 'println', max)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_MaxFlow1.MAXN = jcast('int', 50001)
Code01_MaxFlow1.LIMIT = jcast('int', 16)
Code01_MaxFlow1.power = jcast('int', 0)
Code01_MaxFlow1.num = jarray('int', [Code01_MaxFlow1.MAXN])
Code01_MaxFlow1.head = jarray('int', [Code01_MaxFlow1.MAXN])
Code01_MaxFlow1.next = jarray('int', [jcast('int', (Code01_MaxFlow1.MAXN << (1 & 31)))])
Code01_MaxFlow1.to = jarray('int', [jcast('int', (Code01_MaxFlow1.MAXN << (1 & 31)))])
Code01_MaxFlow1.cnt = jcast('int', 0)
Code01_MaxFlow1.deep = jarray('int', [Code01_MaxFlow1.MAXN])
Code01_MaxFlow1.stjump = jarray('int', [Code01_MaxFlow1.MAXN, Code01_MaxFlow1.LIMIT])

if __name__ == '__main__':
    Code01_MaxFlow1.main([])
