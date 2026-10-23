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

# 边差分实战
# 使图不连通的方法数
# 有n个节点，给定n-1条老边使其连接成一棵树，再给定m条新边额外加在树上
# 你可以切断两条边让这个图不连通，切断的两条边必须是一条老边和一条新边
# 返回方法数
# 测试链接 : http://poj.org/problem?id=3417
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Network:
    __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'power': 'power', 'n': 'n', 'm': 'm', 'num': 'num', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'deep': 'deep', 'stjump': 'stjump', 'ans': 'ans'}
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

    n = 0
    m = 0
    num = None
    head = None
    next = None
    to = None
    cnt = 0
    deep = None
    stjump = None
    ans = 0
    @staticmethod
    def build():
        Code04_Network.power = jcast('int', Code04_Network.log2(Code04_Network.n))
        jstatic('Arrays', 'fill', Code04_Network.num, 1, jcast('int', jadd(Code04_Network.n, 1)), 0)
        Code04_Network.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code04_Network.head, 1, jcast('int', jadd(Code04_Network.n, 1)), 0)
        Code04_Network.ans = jcast('int', 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code04_Network.next[Code04_Network.cnt] = jcast('int', Code04_Network.head[u])
        Code04_Network.to[Code04_Network.cnt] = jcast('int', v)
        jset(Code04_Network.head, u, ((_java_obj_1 := Code04_Network), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code04_Network.deep[u] = jcast('int', jcast('int', jadd(Code04_Network.deep[f], 1)))
        jset(Code04_Network.stjump[u], 0, f)
        p = jcast('int', 1)
        while (p <= Code04_Network.power):
            jset(Code04_Network.stjump[u], p, Code04_Network.stjump[Code04_Network.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code04_Network.head[u])
        while (e != 0):
            if (Code04_Network.to[e] != f):
                Code04_Network.dfs1(Code04_Network.to[e], u)
            e = jcast('int', Code04_Network.next[e])

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code04_Network.deep[a] < Code04_Network.deep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', Code04_Network.power)
        while (p >= 0):
            if (Code04_Network.deep[Code04_Network.stjump[a][p]] >= Code04_Network.deep[b]):
                a = jcast('int', Code04_Network.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', Code04_Network.power)
        while (p >= 0):
            if (Code04_Network.stjump[a][p] != Code04_Network.stjump[b][p]):
                a = jcast('int', Code04_Network.stjump[a][p])
                b = jcast('int', Code04_Network.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code04_Network.stjump[a][0])

    @staticmethod
    def dfs2(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code04_Network.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code04_Network.to[e])
            if (v != f):
                Code04_Network.dfs2(v, u)
            e = jcast('int', Code04_Network.next[e])
        e = jcast('int', Code04_Network.head[u])
        v = 0
        w = 0
        while (e != 0):
            v = jcast('int', Code04_Network.to[e])
            if (v != f):
                w = jcast('int', jcast('int', jadd(0, Code04_Network.num[v])))
                if (w == 0):
                    Code04_Network.ans = jcast('int', jcast('int', jadd(Code04_Network.ans, Code04_Network.m)))
                else:
                    if (w == 1):
                        Code04_Network.ans = jcast('int', jcast('int', jadd(Code04_Network.ans, 1)))
                    else:
                        Code04_Network.ans = jcast('int', jcast('int', jadd(Code04_Network.ans, 0)))
                Code04_Network.num[u] = jcast('int', jcast('int', jadd(Code04_Network.num[u], Code04_Network.num[v])))
            e = jcast('int', Code04_Network.next[e])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_Network.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code04_Network.build()
        jcall(in_, 'nextToken')
        Code04_Network.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code04_Network.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code04_Network.addEdge(u, v)
            Code04_Network.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code04_Network.dfs1(1, 0)
        i = jcast('int', 1)
        u = 0
        v = 0
        lca = 0
        while (i <= Code04_Network.m):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            lca = jcast('int', Code04_Network.lca(u, v))
            Code04_Network.num[u] = jcast('int', (Code04_Network.num[u] + 1))
            Code04_Network.num[v] = jcast('int', (Code04_Network.num[v] + 1))
            Code04_Network.num[lca] = jcast('int', jcast('int', (Code04_Network.num[lca] - 2)))
            i = jcast('int', (i + 1))
        Code04_Network.dfs2(1, 0)
        jcall(out, 'println', Code04_Network.ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Network.MAXN = jcast('int', 100001)
Code04_Network.LIMIT = jcast('int', 17)
Code04_Network.power = jcast('int', 0)
Code04_Network.n = jcast('int', 0)
Code04_Network.m = jcast('int', 0)
Code04_Network.num = jarray('int', [Code04_Network.MAXN])
Code04_Network.head = jarray('int', [Code04_Network.MAXN])
Code04_Network.next = jarray('int', [jcast('int', (Code04_Network.MAXN << (1 & 31)))])
Code04_Network.to = jarray('int', [jcast('int', (Code04_Network.MAXN << (1 & 31)))])
Code04_Network.cnt = jcast('int', 0)
Code04_Network.deep = jarray('int', [Code04_Network.MAXN])
Code04_Network.stjump = jarray('int', [Code04_Network.MAXN, Code04_Network.LIMIT])
Code04_Network.ans = jcast('int', 0)

if __name__ == '__main__':
    Code04_Network.main([])
