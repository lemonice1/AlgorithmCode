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

# 选择节点做根使流量和最大(迭代版)
# 给定一棵n个点的树，边的边权代表流量限制
# 从边上流过的流量，不能超过流量限制
# 现在想知道以某个节点做根时，流到所有叶节点的流量，最大是多少
# 测试链接 : http://poj.org/problem?id=3585
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_MaximizeFlow2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'degree': 'degree', 'flow': 'flow', 'dp': 'dp', 'ufe': 'ufe', 'stackSize': 'stackSize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    n = 0
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    degree = None
    flow = None
    dp = None
    @staticmethod
    def build():
        Code04_MaximizeFlow2.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code04_MaximizeFlow2.head, 1, jcast('int', jadd(Code04_MaximizeFlow2.n, 1)), 0)
        jstatic('Arrays', 'fill', Code04_MaximizeFlow2.degree, 1, jcast('int', jadd(Code04_MaximizeFlow2.n, 1)), 0)
        jstatic('Arrays', 'fill', Code04_MaximizeFlow2.flow, 1, jcast('int', jadd(Code04_MaximizeFlow2.n, 1)), 0)
        jstatic('Arrays', 'fill', Code04_MaximizeFlow2.dp, 1, jcast('int', jadd(Code04_MaximizeFlow2.n, 1)), 0)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code04_MaximizeFlow2.next[Code04_MaximizeFlow2.cnt] = jcast('int', Code04_MaximizeFlow2.head[u])
        Code04_MaximizeFlow2.to[Code04_MaximizeFlow2.cnt] = jcast('int', v)
        Code04_MaximizeFlow2.weight[Code04_MaximizeFlow2.cnt] = jcast('int', w)
        jset(Code04_MaximizeFlow2.head, u, ((_java_obj_1 := Code04_MaximizeFlow2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

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
        jset(Code04_MaximizeFlow2.ufe[Code04_MaximizeFlow2.stackSize], 0, u)
        jset(Code04_MaximizeFlow2.ufe[Code04_MaximizeFlow2.stackSize], 1, f)
        jset(Code04_MaximizeFlow2.ufe[Code04_MaximizeFlow2.stackSize], 2, e)
        Code04_MaximizeFlow2.stackSize = jcast('int', (Code04_MaximizeFlow2.stackSize + 1))

    @staticmethod
    def pop():
        Code04_MaximizeFlow2.stackSize = jcast('int', (Code04_MaximizeFlow2.stackSize - 1))
        Code04_MaximizeFlow2.u = jcast('int', Code04_MaximizeFlow2.ufe[Code04_MaximizeFlow2.stackSize][0])
        Code04_MaximizeFlow2.f = jcast('int', Code04_MaximizeFlow2.ufe[Code04_MaximizeFlow2.stackSize][1])
        Code04_MaximizeFlow2.e = jcast('int', Code04_MaximizeFlow2.ufe[Code04_MaximizeFlow2.stackSize][2])

    @staticmethod
    def dfs1(root):
        root = jcast('int', root)
        Code04_MaximizeFlow2.stackSize = jcast('int', 0)
        Code04_MaximizeFlow2.push(root, 0, jcast('int', (-1)))
        while (Code04_MaximizeFlow2.stackSize > 0):
            Code04_MaximizeFlow2.pop()
            if (Code04_MaximizeFlow2.e == jcast('int', (-1))):
                Code04_MaximizeFlow2.e = jcast('int', Code04_MaximizeFlow2.head[Code04_MaximizeFlow2.u])
            else:
                Code04_MaximizeFlow2.e = jcast('int', Code04_MaximizeFlow2.next[Code04_MaximizeFlow2.e])
            if (Code04_MaximizeFlow2.e != 0):
                Code04_MaximizeFlow2.push(Code04_MaximizeFlow2.u, Code04_MaximizeFlow2.f, Code04_MaximizeFlow2.e)
                if (Code04_MaximizeFlow2.to[Code04_MaximizeFlow2.e] != Code04_MaximizeFlow2.f):
                    Code04_MaximizeFlow2.push(Code04_MaximizeFlow2.to[Code04_MaximizeFlow2.e], Code04_MaximizeFlow2.u, jcast('int', (-1)))
            else:
                e = jcast('int', Code04_MaximizeFlow2.head[Code04_MaximizeFlow2.u])
                v = 0
                while (e != 0):
                    v = jcast('int', Code04_MaximizeFlow2.to[e])
                    if (v != Code04_MaximizeFlow2.f):
                        if (Code04_MaximizeFlow2.degree[v] == 1):
                            Code04_MaximizeFlow2.flow[Code04_MaximizeFlow2.u] = jcast('int', jcast('int', jadd(Code04_MaximizeFlow2.flow[Code04_MaximizeFlow2.u], Code04_MaximizeFlow2.weight[e])))
                        else:
                            ((_java_obj_4 := Code04_MaximizeFlow2.flow), (_java_key_5 := Code04_MaximizeFlow2.u), jset(_java_obj_4, _java_key_5, jcast('int', jadd(jget(_java_obj_4, _java_key_5), jstatic('Math', 'min', Code04_MaximizeFlow2.flow[v], Code04_MaximizeFlow2.weight[e])))))[2]
                    e = jcast('int', Code04_MaximizeFlow2.next[e])

    # dfs2方法改迭代版
    # 不会改，看讲解118，讲了怎么从递归版改成迭代版
    @staticmethod
    def dfs2(root):
        root = jcast('int', root)
        Code04_MaximizeFlow2.stackSize = jcast('int', 0)
        Code04_MaximizeFlow2.push(root, 0, jcast('int', (-1)))
        while (Code04_MaximizeFlow2.stackSize > 0):
            Code04_MaximizeFlow2.pop()
            if (Code04_MaximizeFlow2.e == jcast('int', (-1))):
                Code04_MaximizeFlow2.e = jcast('int', Code04_MaximizeFlow2.head[Code04_MaximizeFlow2.u])
            else:
                Code04_MaximizeFlow2.e = jcast('int', Code04_MaximizeFlow2.next[Code04_MaximizeFlow2.e])
            if (Code04_MaximizeFlow2.e != 0):
                Code04_MaximizeFlow2.push(Code04_MaximizeFlow2.u, Code04_MaximizeFlow2.f, Code04_MaximizeFlow2.e)
                v = jcast('int', Code04_MaximizeFlow2.to[Code04_MaximizeFlow2.e])
                if (v != Code04_MaximizeFlow2.f):
                    if (Code04_MaximizeFlow2.degree[Code04_MaximizeFlow2.u] == 1):
                        Code04_MaximizeFlow2.dp[v] = jcast('int', jcast('int', jadd(Code04_MaximizeFlow2.flow[v], Code04_MaximizeFlow2.weight[Code04_MaximizeFlow2.e])))
                    else:
                        uOut = jcast('int', jcast('int', (Code04_MaximizeFlow2.dp[Code04_MaximizeFlow2.u] - jstatic('Math', 'min', Code04_MaximizeFlow2.flow[v], Code04_MaximizeFlow2.weight[Code04_MaximizeFlow2.e]))))
                        jset(Code04_MaximizeFlow2.dp, v, jcast('int', jadd(Code04_MaximizeFlow2.flow[v], jstatic('Math', 'min', uOut, Code04_MaximizeFlow2.weight[Code04_MaximizeFlow2.e]))))
                    Code04_MaximizeFlow2.push(v, Code04_MaximizeFlow2.u, jcast('int', (-1)))

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
            Code04_MaximizeFlow2.n = jcast('int', jcast('int', jget(in_, 'nval')))
            Code04_MaximizeFlow2.build()
            i = jcast('int', 1)
            u = 0
            v = 0
            w = 0
            while (i < Code04_MaximizeFlow2.n):
                jcall(in_, 'nextToken')
                u = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                w = jcast('int', jcast('int', jget(in_, 'nval')))
                Code04_MaximizeFlow2.addEdge(u, v, w)
                Code04_MaximizeFlow2.addEdge(v, u, w)
                Code04_MaximizeFlow2.degree[u] = jcast('int', (Code04_MaximizeFlow2.degree[u] + 1))
                Code04_MaximizeFlow2.degree[v] = jcast('int', (Code04_MaximizeFlow2.degree[v] + 1))
                i = jcast('int', (i + 1))
            Code04_MaximizeFlow2.dfs1(1)
            Code04_MaximizeFlow2.dp[1] = jcast('int', Code04_MaximizeFlow2.flow[1])
            Code04_MaximizeFlow2.dfs2(1)
            ans = jcast('int', 0)
            i = jcast('int', 1)
            while (i <= Code04_MaximizeFlow2.n):
                ans = jcast('int', jstatic('Math', 'max', ans, Code04_MaximizeFlow2.dp[i]))
                i = jcast('int', (i + 1))
            jcall(out, 'println', ans)
            t = jcast('int', (t + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_MaximizeFlow2.MAXN = jcast('int', 200001)
Code04_MaximizeFlow2.n = jcast('int', 0)
Code04_MaximizeFlow2.head = jarray('int', [Code04_MaximizeFlow2.MAXN])
Code04_MaximizeFlow2.next = jarray('int', [jcast('int', (Code04_MaximizeFlow2.MAXN << (1 & 31)))])
Code04_MaximizeFlow2.to = jarray('int', [jcast('int', (Code04_MaximizeFlow2.MAXN << (1 & 31)))])
Code04_MaximizeFlow2.weight = jarray('int', [jcast('int', (Code04_MaximizeFlow2.MAXN << (1 & 31)))])
Code04_MaximizeFlow2.cnt = jcast('int', 0)
Code04_MaximizeFlow2.degree = jarray('int', [Code04_MaximizeFlow2.MAXN])
Code04_MaximizeFlow2.flow = jarray('int', [Code04_MaximizeFlow2.MAXN])
Code04_MaximizeFlow2.dp = jarray('int', [Code04_MaximizeFlow2.MAXN])
Code04_MaximizeFlow2.ufe = jarray('int', [Code04_MaximizeFlow2.MAXN, 3])
Code04_MaximizeFlow2.stackSize = jcast('int', 0)
Code04_MaximizeFlow2.u = jcast('int', 0)
Code04_MaximizeFlow2.f = jcast('int', 0)
Code04_MaximizeFlow2.e = jcast('int', 0)

if __name__ == '__main__':
    Code04_MaximizeFlow2.main([])
