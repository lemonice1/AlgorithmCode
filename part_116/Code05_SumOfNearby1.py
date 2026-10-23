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

# 每个节点距离k以内的权值和(递归版)
# 给定一棵n个点的树，每个点有点权
# 到达每个节点的距离不超过k的节点就有若干个
# 把这些节点权值加起来，就是该点不超过距离k的点权和
# 打印每个节点不超过距离k的点权和
# 注意k并不大
# 测试链接 : https://www.luogu.com.cn/problem/P3047
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
# 对应实现可参考 Code05_SumOfNearby2.py
class Code05_SumOfNearby1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 'n': 'n', 'k': 'k', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'sum': 'sum', 'dp': 'dp'}
    MAXN = 0
    MAXK = 0
    n = 0
    k = 0
    head = None
    next = None
    to = None
    cnt = 0
    # sum[u][i] : 以u为头的子树内，距离为i的节点权值和
    sum = None
    # dp[u][i] : 以u做根，整棵树上，距离为i的节点权值和
    dp = None
    @staticmethod
    def build():
        Code05_SumOfNearby1.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code05_SumOfNearby1.head, 1, jcast('int', jadd(Code05_SumOfNearby1.n, 1)), 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code05_SumOfNearby1.next[Code05_SumOfNearby1.cnt] = jcast('int', Code05_SumOfNearby1.head[u])
        Code05_SumOfNearby1.to[Code05_SumOfNearby1.cnt] = jcast('int', v)
        jset(Code05_SumOfNearby1.head, u, ((_java_obj_1 := Code05_SumOfNearby1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code05_SumOfNearby1.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code05_SumOfNearby1.to[e])
            if (v != f):
                Code05_SumOfNearby1.dfs1(v, u)
            e = jcast('int', Code05_SumOfNearby1.next[e])
        e = jcast('int', Code05_SumOfNearby1.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code05_SumOfNearby1.to[e])
            if (v != f):
                j = jcast('int', 1)
                while (j <= Code05_SumOfNearby1.k):
                    ((_java_obj_4 := Code05_SumOfNearby1.sum[u]), (_java_key_5 := j), jset(_java_obj_4, _java_key_5, jcast('int', jadd(jget(_java_obj_4, _java_key_5), Code05_SumOfNearby1.sum[v][jcast('int', (j - 1))]))))[2]
                    j = jcast('int', (j + 1))
            e = jcast('int', Code05_SumOfNearby1.next[e])

    @staticmethod
    def dfs2(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code05_SumOfNearby1.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code05_SumOfNearby1.to[e])
            if (v != f):
                jset(Code05_SumOfNearby1.dp[v], 0, Code05_SumOfNearby1.sum[v][0])
                jset(Code05_SumOfNearby1.dp[v], 1, jcast('int', jadd(Code05_SumOfNearby1.sum[v][1], Code05_SumOfNearby1.dp[u][0])))
                i = jcast('int', 2)
                while (i <= Code05_SumOfNearby1.k):
                    jset(Code05_SumOfNearby1.dp[v], i, jcast('int', (jcast('int', jadd(Code05_SumOfNearby1.sum[v][i], Code05_SumOfNearby1.dp[u][jcast('int', (i - 1))])) - Code05_SumOfNearby1.sum[v][jcast('int', (i - 2))])))
                    i = jcast('int', (i + 1))
                Code05_SumOfNearby1.dfs2(v, u)
            e = jcast('int', Code05_SumOfNearby1.next[e])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_SumOfNearby1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code05_SumOfNearby1.build()
        jcall(in_, 'nextToken')
        Code05_SumOfNearby1.k = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code05_SumOfNearby1.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code05_SumOfNearby1.addEdge(u, v)
            Code05_SumOfNearby1.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_SumOfNearby1.n):
            jcall(in_, 'nextToken')
            jset(Code05_SumOfNearby1.sum[i], 0, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code05_SumOfNearby1.dfs1(1, 0)
        i = jcast('int', 0)
        while (i <= Code05_SumOfNearby1.k):
            jset(Code05_SumOfNearby1.dp[1], i, Code05_SumOfNearby1.sum[1][i])
            i = jcast('int', (i + 1))
        Code05_SumOfNearby1.dfs2(1, 0)
        i = jcast('int', 1)
        ans = 0
        while (i <= Code05_SumOfNearby1.n):
            ans = jcast('int', 0)
            j = jcast('int', 0)
            while (j <= Code05_SumOfNearby1.k):
                ans = jcast('int', jcast('int', jadd(ans, Code05_SumOfNearby1.dp[i][j])))
                j = jcast('int', (j + 1))
            jcall(out, 'println', ans)
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_SumOfNearby1.MAXN = jcast('int', 100001)
Code05_SumOfNearby1.MAXK = jcast('int', 21)
Code05_SumOfNearby1.n = jcast('int', 0)
Code05_SumOfNearby1.k = jcast('int', 0)
Code05_SumOfNearby1.head = jarray('int', [Code05_SumOfNearby1.MAXN])
Code05_SumOfNearby1.next = jarray('int', [jcast('int', (Code05_SumOfNearby1.MAXN << (1 & 31)))])
Code05_SumOfNearby1.to = jarray('int', [jcast('int', (Code05_SumOfNearby1.MAXN << (1 & 31)))])
Code05_SumOfNearby1.cnt = jcast('int', 0)
Code05_SumOfNearby1.sum = jarray('int', [Code05_SumOfNearby1.MAXN, Code05_SumOfNearby1.MAXK])
Code05_SumOfNearby1.dp = jarray('int', [Code05_SumOfNearby1.MAXN, Code05_SumOfNearby1.MAXK])

if __name__ == '__main__':
    Code05_SumOfNearby1.main([])
