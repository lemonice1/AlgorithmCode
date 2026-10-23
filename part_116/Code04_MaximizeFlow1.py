# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 选择节点做根使流量和最大(递归版)
# 给定一棵n个点的树，边的边权代表流量限制
# 从边上流过的流量，不能超过流量限制
# 现在想知道以某个节点做根时，流到所有叶节点的流量，最大是多少
# 测试链接 : http://poj.org/problem?id=3585
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
# 对应实现可参考 Code04_MaximizeFlow2.py
class Code04_MaximizeFlow1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'degree': 'degree', 'flow': 'flow', 'dp': 'dp'}
    MAXN = 0
    n = 0
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    # degree[u] : 有几条边和u节点相连
    degree = None
    # flow[u] : 从u出发流向u节点为头的子树上，所有的叶节点，流量是多少
    flow = None
    # dp[u] : 从u出发流向u节点为根的整棵树上，所有的叶节点，流量是多少
    dp = None
    @staticmethod
    def build():
        Code04_MaximizeFlow1.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code04_MaximizeFlow1.head, 1, jcast('int', jadd(Code04_MaximizeFlow1.n, 1)), 0)
        jstatic('Arrays', 'fill', Code04_MaximizeFlow1.degree, 1, jcast('int', jadd(Code04_MaximizeFlow1.n, 1)), 0)
        jstatic('Arrays', 'fill', Code04_MaximizeFlow1.flow, 1, jcast('int', jadd(Code04_MaximizeFlow1.n, 1)), 0)
        jstatic('Arrays', 'fill', Code04_MaximizeFlow1.dp, 1, jcast('int', jadd(Code04_MaximizeFlow1.n, 1)), 0)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code04_MaximizeFlow1.next[Code04_MaximizeFlow1.cnt] = jcast('int', Code04_MaximizeFlow1.head[u])
        Code04_MaximizeFlow1.to[Code04_MaximizeFlow1.cnt] = jcast('int', v)
        Code04_MaximizeFlow1.weight[Code04_MaximizeFlow1.cnt] = jcast('int', w)
        jset(Code04_MaximizeFlow1.head, u, ((_java_obj_1 := Code04_MaximizeFlow1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code04_MaximizeFlow1.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code04_MaximizeFlow1.to[e])
            if (v != f):
                Code04_MaximizeFlow1.dfs1(v, u)
            e = jcast('int', Code04_MaximizeFlow1.next[e])
        e = jcast('int', Code04_MaximizeFlow1.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code04_MaximizeFlow1.to[e])
            if (v != f):
                if (Code04_MaximizeFlow1.degree[v] == 1):
                    Code04_MaximizeFlow1.flow[u] = jcast('int', jcast('int', jadd(Code04_MaximizeFlow1.flow[u], Code04_MaximizeFlow1.weight[e])))
                else:
                    ((_java_obj_4 := Code04_MaximizeFlow1.flow), (_java_key_5 := u), jset(_java_obj_4, _java_key_5, jcast('int', jadd(jget(_java_obj_4, _java_key_5), jstatic('Math', 'min', Code04_MaximizeFlow1.flow[v], Code04_MaximizeFlow1.weight[e])))))[2]
            e = jcast('int', Code04_MaximizeFlow1.next[e])

    @staticmethod
    def dfs2(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code04_MaximizeFlow1.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code04_MaximizeFlow1.to[e])
            if (v != f):
                if (Code04_MaximizeFlow1.degree[u] == 1):
                    Code04_MaximizeFlow1.dp[v] = jcast('int', jcast('int', jadd(Code04_MaximizeFlow1.flow[v], Code04_MaximizeFlow1.weight[e])))
                else:
                    # uOut : u流向外的流量
                    uOut = jcast('int', jcast('int', (Code04_MaximizeFlow1.dp[u] - jstatic('Math', 'min', Code04_MaximizeFlow1.flow[v], Code04_MaximizeFlow1.weight[e]))))
                    jset(Code04_MaximizeFlow1.dp, v, jcast('int', jadd(Code04_MaximizeFlow1.flow[v], jstatic('Math', 'min', uOut, Code04_MaximizeFlow1.weight[e]))))
                Code04_MaximizeFlow1.dfs2(v, u)
            e = jcast('int', Code04_MaximizeFlow1.next[e])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        testCase = jcast('int', jcast('int', jget(in_, 'nval')))
        t = jcast('int', 1)
        while (t <= testCase):
            jcall(in_, 'nextToken')
            Code04_MaximizeFlow1.n = jcast('int', jcast('int', jget(in_, 'nval')))
            Code04_MaximizeFlow1.build()
            i = jcast('int', 1)
            u = 0
            v = 0
            w = 0
            while (i < Code04_MaximizeFlow1.n):
                jcall(in_, 'nextToken')
                u = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                w = jcast('int', jcast('int', jget(in_, 'nval')))
                Code04_MaximizeFlow1.addEdge(u, v, w)
                Code04_MaximizeFlow1.addEdge(v, u, w)
                Code04_MaximizeFlow1.degree[u] = jcast('int', (Code04_MaximizeFlow1.degree[u] + 1))
                Code04_MaximizeFlow1.degree[v] = jcast('int', (Code04_MaximizeFlow1.degree[v] + 1))
                i = jcast('int', (i + 1))
            Code04_MaximizeFlow1.dfs1(1, 0)
            Code04_MaximizeFlow1.dp[1] = jcast('int', Code04_MaximizeFlow1.flow[1])
            Code04_MaximizeFlow1.dfs2(1, 0)
            ans = jcast('int', 0)
            i = jcast('int', 1)
            while (i <= Code04_MaximizeFlow1.n):
                ans = jcast('int', jstatic('Math', 'max', ans, Code04_MaximizeFlow1.dp[i]))
                i = jcast('int', (i + 1))
            jcall(out, 'println', ans)
            t = jcast('int', (t + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_MaximizeFlow1.MAXN = jcast('int', 200001)
Code04_MaximizeFlow1.n = jcast('int', 0)
Code04_MaximizeFlow1.head = jarray('int', [Code04_MaximizeFlow1.MAXN])
Code04_MaximizeFlow1.next = jarray('int', [jcast('int', (Code04_MaximizeFlow1.MAXN << (1 & 31)))])
Code04_MaximizeFlow1.to = jarray('int', [jcast('int', (Code04_MaximizeFlow1.MAXN << (1 & 31)))])
Code04_MaximizeFlow1.weight = jarray('int', [jcast('int', (Code04_MaximizeFlow1.MAXN << (1 & 31)))])
Code04_MaximizeFlow1.cnt = jcast('int', 0)
Code04_MaximizeFlow1.degree = jarray('int', [Code04_MaximizeFlow1.MAXN])
Code04_MaximizeFlow1.flow = jarray('int', [Code04_MaximizeFlow1.MAXN])
Code04_MaximizeFlow1.dp = jarray('int', [Code04_MaximizeFlow1.MAXN])

if __name__ == '__main__':
    Code04_MaximizeFlow1.main([])
