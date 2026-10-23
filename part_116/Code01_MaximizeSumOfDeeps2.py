# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最大深度和(迭代版)
# 给定一棵n个点的树，找到一个节点，使得以这个节点为根时，到达所有节点的深度之和最大
# 如果有多个节点满足要求，返回节点编号最小的
# 测试链接 : https://www.luogu.com.cn/problem/P3478
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_MaximizeSumOfDeeps2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'size': 'size', 'sum': 'sum', 'dp': 'dp', 'ufe': 'ufe', 'stackSize': 'stackSize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    n = 0
    head = None
    next = None
    to = None
    cnt = 0
    size = None
    sum = None
    dp = None
    @staticmethod
    def build():
        Code01_MaximizeSumOfDeeps2.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code01_MaximizeSumOfDeeps2.head, 1, jcast('int', jadd(Code01_MaximizeSumOfDeeps2.n, 1)), 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code01_MaximizeSumOfDeeps2.next[Code01_MaximizeSumOfDeeps2.cnt] = jcast('int', Code01_MaximizeSumOfDeeps2.head[u])
        Code01_MaximizeSumOfDeeps2.to[Code01_MaximizeSumOfDeeps2.cnt] = jcast('int', v)
        jset(Code01_MaximizeSumOfDeeps2.head, u, ((_java_obj_1 := Code01_MaximizeSumOfDeeps2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

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
        jset(Code01_MaximizeSumOfDeeps2.ufe[Code01_MaximizeSumOfDeeps2.stackSize], 0, u)
        jset(Code01_MaximizeSumOfDeeps2.ufe[Code01_MaximizeSumOfDeeps2.stackSize], 1, f)
        jset(Code01_MaximizeSumOfDeeps2.ufe[Code01_MaximizeSumOfDeeps2.stackSize], 2, e)
        Code01_MaximizeSumOfDeeps2.stackSize = jcast('int', (Code01_MaximizeSumOfDeeps2.stackSize + 1))

    @staticmethod
    def pop():
        Code01_MaximizeSumOfDeeps2.stackSize = jcast('int', (Code01_MaximizeSumOfDeeps2.stackSize - 1))
        Code01_MaximizeSumOfDeeps2.u = jcast('int', Code01_MaximizeSumOfDeeps2.ufe[Code01_MaximizeSumOfDeeps2.stackSize][0])
        Code01_MaximizeSumOfDeeps2.f = jcast('int', Code01_MaximizeSumOfDeeps2.ufe[Code01_MaximizeSumOfDeeps2.stackSize][1])
        Code01_MaximizeSumOfDeeps2.e = jcast('int', Code01_MaximizeSumOfDeeps2.ufe[Code01_MaximizeSumOfDeeps2.stackSize][2])

    @staticmethod
    def dfs1(root):
        root = jcast('int', root)
        Code01_MaximizeSumOfDeeps2.stackSize = jcast('int', 0)
        Code01_MaximizeSumOfDeeps2.push(root, 0, jcast('int', (-1)))
        while (Code01_MaximizeSumOfDeeps2.stackSize > 0):
            Code01_MaximizeSumOfDeeps2.pop()
            if (Code01_MaximizeSumOfDeeps2.e == jcast('int', (-1))):
                Code01_MaximizeSumOfDeeps2.e = jcast('int', Code01_MaximizeSumOfDeeps2.head[Code01_MaximizeSumOfDeeps2.u])
            else:
                Code01_MaximizeSumOfDeeps2.e = jcast('int', Code01_MaximizeSumOfDeeps2.next[Code01_MaximizeSumOfDeeps2.e])
            if (Code01_MaximizeSumOfDeeps2.e != 0):
                Code01_MaximizeSumOfDeeps2.push(Code01_MaximizeSumOfDeeps2.u, Code01_MaximizeSumOfDeeps2.f, Code01_MaximizeSumOfDeeps2.e)
                if (Code01_MaximizeSumOfDeeps2.to[Code01_MaximizeSumOfDeeps2.e] != Code01_MaximizeSumOfDeeps2.f):
                    Code01_MaximizeSumOfDeeps2.push(Code01_MaximizeSumOfDeeps2.to[Code01_MaximizeSumOfDeeps2.e], Code01_MaximizeSumOfDeeps2.u, jcast('int', (-1)))
            else:
                Code01_MaximizeSumOfDeeps2.size[Code01_MaximizeSumOfDeeps2.u] = jcast('int', 1)
                Code01_MaximizeSumOfDeeps2.sum[Code01_MaximizeSumOfDeeps2.u] = jcast('long', 0)
                e = jcast('int', Code01_MaximizeSumOfDeeps2.head[Code01_MaximizeSumOfDeeps2.u])
                v = 0
                while (e != 0):
                    v = jcast('int', Code01_MaximizeSumOfDeeps2.to[e])
                    if (v != Code01_MaximizeSumOfDeeps2.f):
                        Code01_MaximizeSumOfDeeps2.size[Code01_MaximizeSumOfDeeps2.u] = jcast('int', jcast('int', jadd(Code01_MaximizeSumOfDeeps2.size[Code01_MaximizeSumOfDeeps2.u], Code01_MaximizeSumOfDeeps2.size[v])))
                        Code01_MaximizeSumOfDeeps2.sum[Code01_MaximizeSumOfDeeps2.u] = jcast('long', jcast('long', jadd(Code01_MaximizeSumOfDeeps2.sum[Code01_MaximizeSumOfDeeps2.u], jcast('long', jadd(Code01_MaximizeSumOfDeeps2.sum[v], Code01_MaximizeSumOfDeeps2.size[v])))))
                    e = jcast('int', Code01_MaximizeSumOfDeeps2.next[e])

    # dfs2方法改迭代版
    # 不会改，看讲解118，讲了怎么从递归版改成迭代版
    @staticmethod
    def dfs2(root):
        root = jcast('int', root)
        Code01_MaximizeSumOfDeeps2.stackSize = jcast('int', 0)
        Code01_MaximizeSumOfDeeps2.push(root, 0, jcast('int', (-1)))
        while (Code01_MaximizeSumOfDeeps2.stackSize > 0):
            Code01_MaximizeSumOfDeeps2.pop()
            if (Code01_MaximizeSumOfDeeps2.e == jcast('int', (-1))):
                Code01_MaximizeSumOfDeeps2.e = jcast('int', Code01_MaximizeSumOfDeeps2.head[Code01_MaximizeSumOfDeeps2.u])
            else:
                Code01_MaximizeSumOfDeeps2.e = jcast('int', Code01_MaximizeSumOfDeeps2.next[Code01_MaximizeSumOfDeeps2.e])
            if (Code01_MaximizeSumOfDeeps2.e != 0):
                Code01_MaximizeSumOfDeeps2.push(Code01_MaximizeSumOfDeeps2.u, Code01_MaximizeSumOfDeeps2.f, Code01_MaximizeSumOfDeeps2.e)
                v = jcast('int', Code01_MaximizeSumOfDeeps2.to[Code01_MaximizeSumOfDeeps2.e])
                if (v != Code01_MaximizeSumOfDeeps2.f):
                    Code01_MaximizeSumOfDeeps2.dp[v] = jcast('long', jcast('long', jadd(jcast('long', (Code01_MaximizeSumOfDeeps2.dp[Code01_MaximizeSumOfDeeps2.u] - Code01_MaximizeSumOfDeeps2.size[v])), jcast('int', (Code01_MaximizeSumOfDeeps2.n - Code01_MaximizeSumOfDeeps2.size[v])))))
                    Code01_MaximizeSumOfDeeps2.push(v, Code01_MaximizeSumOfDeeps2.u, jcast('int', (-1)))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_MaximizeSumOfDeeps2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code01_MaximizeSumOfDeeps2.build()
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code01_MaximizeSumOfDeeps2.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_MaximizeSumOfDeeps2.addEdge(u, v)
            Code01_MaximizeSumOfDeeps2.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code01_MaximizeSumOfDeeps2.dfs1(1)
        Code01_MaximizeSumOfDeeps2.dp[1] = jcast('long', Code01_MaximizeSumOfDeeps2.sum[1])
        Code01_MaximizeSumOfDeeps2.dfs2(1)
        max = jcast('long', jget(Long, 'MIN_VALUE'))
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code01_MaximizeSumOfDeeps2.n):
            if (Code01_MaximizeSumOfDeeps2.dp[i] > max):
                max = jcast('long', Code01_MaximizeSumOfDeeps2.dp[i])
                ans = jcast('int', i)
            i = jcast('int', (i + 1))
        jcall(out, 'println', ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_MaximizeSumOfDeeps2.MAXN = jcast('int', 1000001)
Code01_MaximizeSumOfDeeps2.n = jcast('int', 0)
Code01_MaximizeSumOfDeeps2.head = jarray('int', [Code01_MaximizeSumOfDeeps2.MAXN])
Code01_MaximizeSumOfDeeps2.next = jarray('int', [jcast('int', (Code01_MaximizeSumOfDeeps2.MAXN << (1 & 31)))])
Code01_MaximizeSumOfDeeps2.to = jarray('int', [jcast('int', (Code01_MaximizeSumOfDeeps2.MAXN << (1 & 31)))])
Code01_MaximizeSumOfDeeps2.cnt = jcast('int', 0)
Code01_MaximizeSumOfDeeps2.size = jarray('int', [Code01_MaximizeSumOfDeeps2.MAXN])
Code01_MaximizeSumOfDeeps2.sum = jarray('long', [Code01_MaximizeSumOfDeeps2.MAXN])
Code01_MaximizeSumOfDeeps2.dp = jarray('long', [Code01_MaximizeSumOfDeeps2.MAXN])
Code01_MaximizeSumOfDeeps2.ufe = jarray('int', [Code01_MaximizeSumOfDeeps2.MAXN, 3])
Code01_MaximizeSumOfDeeps2.stackSize = jcast('int', 0)
Code01_MaximizeSumOfDeeps2.u = jcast('int', 0)
Code01_MaximizeSumOfDeeps2.f = jcast('int', 0)
Code01_MaximizeSumOfDeeps2.e = jcast('int', 0)

if __name__ == '__main__':
    Code01_MaximizeSumOfDeeps2.main([])
