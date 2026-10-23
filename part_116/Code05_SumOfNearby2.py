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

# 每个节点距离k以内的权值和(迭代版)
# 给定一棵n个点的树，每个点有点权
# 到达每个节点的距离不超过k的节点就有若干个
# 把这些节点权值加起来，就是该点不超过距离k的点权和
# 打印每个节点不超过距离k的点权和
# 注意k并不大
# 测试链接 : https://www.luogu.com.cn/problem/P3047
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_SumOfNearby2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 'n': 'n', 'k': 'k', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'sum': 'sum', 'dp': 'dp', 'ufe': 'ufe', 'stackSize': 'stackSize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    MAXK = 0
    n = 0
    k = 0
    head = None
    next = None
    to = None
    cnt = 0
    sum = None
    dp = None
    @staticmethod
    def build():
        Code05_SumOfNearby2.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code05_SumOfNearby2.head, 1, jcast('int', jadd(Code05_SumOfNearby2.n, 1)), 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code05_SumOfNearby2.next[Code05_SumOfNearby2.cnt] = jcast('int', Code05_SumOfNearby2.head[u])
        Code05_SumOfNearby2.to[Code05_SumOfNearby2.cnt] = jcast('int', v)
        jset(Code05_SumOfNearby2.head, u, ((_java_obj_1 := Code05_SumOfNearby2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # dfs1方法改迭代版
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
        jset(Code05_SumOfNearby2.ufe[Code05_SumOfNearby2.stackSize], 0, u)
        jset(Code05_SumOfNearby2.ufe[Code05_SumOfNearby2.stackSize], 1, f)
        jset(Code05_SumOfNearby2.ufe[Code05_SumOfNearby2.stackSize], 2, e)
        Code05_SumOfNearby2.stackSize = jcast('int', (Code05_SumOfNearby2.stackSize + 1))

    @staticmethod
    def pop():
        Code05_SumOfNearby2.stackSize = jcast('int', (Code05_SumOfNearby2.stackSize - 1))
        Code05_SumOfNearby2.u = jcast('int', Code05_SumOfNearby2.ufe[Code05_SumOfNearby2.stackSize][0])
        Code05_SumOfNearby2.f = jcast('int', Code05_SumOfNearby2.ufe[Code05_SumOfNearby2.stackSize][1])
        Code05_SumOfNearby2.e = jcast('int', Code05_SumOfNearby2.ufe[Code05_SumOfNearby2.stackSize][2])

    @staticmethod
    def dfs1(root):
        root = jcast('int', root)
        Code05_SumOfNearby2.stackSize = jcast('int', 0)
        Code05_SumOfNearby2.push(root, 0, jcast('int', (-1)))
        while (Code05_SumOfNearby2.stackSize > 0):
            Code05_SumOfNearby2.pop()
            if (Code05_SumOfNearby2.e == jcast('int', (-1))):
                Code05_SumOfNearby2.e = jcast('int', Code05_SumOfNearby2.head[Code05_SumOfNearby2.u])
            else:
                Code05_SumOfNearby2.e = jcast('int', Code05_SumOfNearby2.next[Code05_SumOfNearby2.e])
            if (Code05_SumOfNearby2.e != 0):
                Code05_SumOfNearby2.push(Code05_SumOfNearby2.u, Code05_SumOfNearby2.f, Code05_SumOfNearby2.e)
                if (Code05_SumOfNearby2.to[Code05_SumOfNearby2.e] != Code05_SumOfNearby2.f):
                    Code05_SumOfNearby2.push(Code05_SumOfNearby2.to[Code05_SumOfNearby2.e], Code05_SumOfNearby2.u, jcast('int', (-1)))
            else:
                e = jcast('int', Code05_SumOfNearby2.head[Code05_SumOfNearby2.u])
                v = 0
                while (e != 0):
                    v = jcast('int', Code05_SumOfNearby2.to[e])
                    if (v != Code05_SumOfNearby2.f):
                        j = jcast('int', 1)
                        while (j <= Code05_SumOfNearby2.k):
                            ((_java_obj_4 := Code05_SumOfNearby2.sum[Code05_SumOfNearby2.u]), (_java_key_5 := j), jset(_java_obj_4, _java_key_5, jcast('int', jadd(jget(_java_obj_4, _java_key_5), Code05_SumOfNearby2.sum[v][jcast('int', (j - 1))]))))[2]
                            j = jcast('int', (j + 1))
                    e = jcast('int', Code05_SumOfNearby2.next[e])

    # dfs2方法改迭代版
    # 不会改，看讲解118，讲了怎么从递归版改成迭代版
    @staticmethod
    def dfs2(root):
        root = jcast('int', root)
        Code05_SumOfNearby2.stackSize = jcast('int', 0)
        Code05_SumOfNearby2.push(root, 0, jcast('int', (-1)))
        while (Code05_SumOfNearby2.stackSize > 0):
            Code05_SumOfNearby2.pop()
            if (Code05_SumOfNearby2.e == jcast('int', (-1))):
                Code05_SumOfNearby2.e = jcast('int', Code05_SumOfNearby2.head[Code05_SumOfNearby2.u])
            else:
                Code05_SumOfNearby2.e = jcast('int', Code05_SumOfNearby2.next[Code05_SumOfNearby2.e])
            if (Code05_SumOfNearby2.e != 0):
                Code05_SumOfNearby2.push(Code05_SumOfNearby2.u, Code05_SumOfNearby2.f, Code05_SumOfNearby2.e)
                v = jcast('int', Code05_SumOfNearby2.to[Code05_SumOfNearby2.e])
                if (v != Code05_SumOfNearby2.f):
                    jset(Code05_SumOfNearby2.dp[v], 0, Code05_SumOfNearby2.sum[v][0])
                    jset(Code05_SumOfNearby2.dp[v], 1, jcast('int', jadd(Code05_SumOfNearby2.sum[v][1], Code05_SumOfNearby2.dp[Code05_SumOfNearby2.u][0])))
                    i = jcast('int', 2)
                    while (i <= Code05_SumOfNearby2.k):
                        jset(Code05_SumOfNearby2.dp[v], i, jcast('int', (jcast('int', jadd(Code05_SumOfNearby2.sum[v][i], Code05_SumOfNearby2.dp[Code05_SumOfNearby2.u][jcast('int', (i - 1))])) - Code05_SumOfNearby2.sum[v][jcast('int', (i - 2))])))
                        i = jcast('int', (i + 1))
                    Code05_SumOfNearby2.push(v, Code05_SumOfNearby2.u, jcast('int', (-1)))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_SumOfNearby2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code05_SumOfNearby2.build()
        jcall(in_, 'nextToken')
        Code05_SumOfNearby2.k = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code05_SumOfNearby2.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code05_SumOfNearby2.addEdge(u, v)
            Code05_SumOfNearby2.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_SumOfNearby2.n):
            jcall(in_, 'nextToken')
            jset(Code05_SumOfNearby2.sum[i], 0, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code05_SumOfNearby2.dfs1(1)
        i = jcast('int', 0)
        while (i <= Code05_SumOfNearby2.k):
            jset(Code05_SumOfNearby2.dp[1], i, Code05_SumOfNearby2.sum[1][i])
            i = jcast('int', (i + 1))
        Code05_SumOfNearby2.dfs2(1)
        i = jcast('int', 1)
        ans = 0
        while (i <= Code05_SumOfNearby2.n):
            ans = jcast('int', 0)
            j = jcast('int', 0)
            while (j <= Code05_SumOfNearby2.k):
                ans = jcast('int', jcast('int', jadd(ans, Code05_SumOfNearby2.dp[i][j])))
                j = jcast('int', (j + 1))
            jcall(out, 'println', ans)
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_SumOfNearby2.MAXN = jcast('int', 100001)
Code05_SumOfNearby2.MAXK = jcast('int', 21)
Code05_SumOfNearby2.n = jcast('int', 0)
Code05_SumOfNearby2.k = jcast('int', 0)
Code05_SumOfNearby2.head = jarray('int', [Code05_SumOfNearby2.MAXN])
Code05_SumOfNearby2.next = jarray('int', [jcast('int', (Code05_SumOfNearby2.MAXN << (1 & 31)))])
Code05_SumOfNearby2.to = jarray('int', [jcast('int', (Code05_SumOfNearby2.MAXN << (1 & 31)))])
Code05_SumOfNearby2.cnt = jcast('int', 0)
Code05_SumOfNearby2.sum = jarray('int', [Code05_SumOfNearby2.MAXN, Code05_SumOfNearby2.MAXK])
Code05_SumOfNearby2.dp = jarray('int', [Code05_SumOfNearby2.MAXN, Code05_SumOfNearby2.MAXK])
Code05_SumOfNearby2.ufe = jarray('int', [Code05_SumOfNearby2.MAXN, 3])
Code05_SumOfNearby2.stackSize = jcast('int', 0)
Code05_SumOfNearby2.u = jcast('int', 0)
Code05_SumOfNearby2.f = jcast('int', 0)
Code05_SumOfNearby2.e = jcast('int', 0)

if __name__ == '__main__':
    Code05_SumOfNearby2.main([])
