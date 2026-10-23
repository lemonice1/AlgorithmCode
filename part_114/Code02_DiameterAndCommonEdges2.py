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

# 所有直径的公共部分(迭代版)
# 给定一棵树，边权都为正
# 打印直径长度、所有直径的公共部分有几条边
# 测试链接 : https://www.luogu.com.cn/problem/P3304
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_DiameterAndCommonEdges2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'start': 'start', 'end': 'end', 'dist': 'dist', 'last': 'last', 'diameter': 'diameter', 'diameterPath': 'diameterPath', 'commonEdges': 'commonEdges', 'ufeStack': 'ufeStack', 'distStack': 'distStack', 'stackSize': 'stackSize', 'u': 'u', 'f': 'f', 'e': 'e', 'c': 'c'}
    MAXN = 0
    n = 0
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    start = 0
    end = 0
    dist = None
    last = None
    diameter = 0
    diameterPath = None
    commonEdges = 0
    @staticmethod
    def build():
        Code02_DiameterAndCommonEdges2.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code02_DiameterAndCommonEdges2.head, 1, jcast('int', jadd(Code02_DiameterAndCommonEdges2.n, 1)), 0)
        jstatic('Arrays', 'fill', Code02_DiameterAndCommonEdges2.diameterPath, 1, jcast('int', jadd(Code02_DiameterAndCommonEdges2.n, 1)), False)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code02_DiameterAndCommonEdges2.next[Code02_DiameterAndCommonEdges2.cnt] = jcast('int', Code02_DiameterAndCommonEdges2.head[u])
        Code02_DiameterAndCommonEdges2.to[Code02_DiameterAndCommonEdges2.cnt] = jcast('int', v)
        Code02_DiameterAndCommonEdges2.weight[Code02_DiameterAndCommonEdges2.cnt] = jcast('int', w)
        jset(Code02_DiameterAndCommonEdges2.head, u, ((_java_obj_1 := Code02_DiameterAndCommonEdges2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def road():
        Code02_DiameterAndCommonEdges2.dfs(1)
        Code02_DiameterAndCommonEdges2.start = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code02_DiameterAndCommonEdges2.n):
            if (Code02_DiameterAndCommonEdges2.dist[i] > Code02_DiameterAndCommonEdges2.dist[Code02_DiameterAndCommonEdges2.start]):
                Code02_DiameterAndCommonEdges2.start = jcast('int', i)
            i = jcast('int', (i + 1))
        Code02_DiameterAndCommonEdges2.dfs(Code02_DiameterAndCommonEdges2.start)
        Code02_DiameterAndCommonEdges2.end = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code02_DiameterAndCommonEdges2.n):
            if (Code02_DiameterAndCommonEdges2.dist[i] > Code02_DiameterAndCommonEdges2.dist[Code02_DiameterAndCommonEdges2.end]):
                Code02_DiameterAndCommonEdges2.end = jcast('int', i)
            i = jcast('int', (i + 1))
        Code02_DiameterAndCommonEdges2.diameter = jcast('long', Code02_DiameterAndCommonEdges2.dist[Code02_DiameterAndCommonEdges2.end])

    # dfs方法改迭代版
    # 不会改，看讲解118，讲了怎么从递归版改成迭代版
    ufeStack = None
    distStack = None
    stackSize = 0
    u = 0
    f = 0
    e = 0
    c = 0
    @staticmethod
    def push(u, f, e, c):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', e)
        c = jcast('long', c)
        jset(Code02_DiameterAndCommonEdges2.ufeStack[Code02_DiameterAndCommonEdges2.stackSize], 0, u)
        jset(Code02_DiameterAndCommonEdges2.ufeStack[Code02_DiameterAndCommonEdges2.stackSize], 1, f)
        jset(Code02_DiameterAndCommonEdges2.ufeStack[Code02_DiameterAndCommonEdges2.stackSize], 2, e)
        Code02_DiameterAndCommonEdges2.distStack[Code02_DiameterAndCommonEdges2.stackSize] = jcast('long', c)
        Code02_DiameterAndCommonEdges2.stackSize = jcast('int', (Code02_DiameterAndCommonEdges2.stackSize + 1))

    @staticmethod
    def pop():
        Code02_DiameterAndCommonEdges2.stackSize = jcast('int', (Code02_DiameterAndCommonEdges2.stackSize - 1))
        Code02_DiameterAndCommonEdges2.u = jcast('int', Code02_DiameterAndCommonEdges2.ufeStack[Code02_DiameterAndCommonEdges2.stackSize][0])
        Code02_DiameterAndCommonEdges2.f = jcast('int', Code02_DiameterAndCommonEdges2.ufeStack[Code02_DiameterAndCommonEdges2.stackSize][1])
        Code02_DiameterAndCommonEdges2.e = jcast('int', Code02_DiameterAndCommonEdges2.ufeStack[Code02_DiameterAndCommonEdges2.stackSize][2])
        Code02_DiameterAndCommonEdges2.c = jcast('long', Code02_DiameterAndCommonEdges2.distStack[Code02_DiameterAndCommonEdges2.stackSize])

    @staticmethod
    def dfs(root):
        root = jcast('int', root)
        Code02_DiameterAndCommonEdges2.stackSize = jcast('int', 0)
        Code02_DiameterAndCommonEdges2.push(root, 0, jcast('int', (-1)), 0)
        while (Code02_DiameterAndCommonEdges2.stackSize > 0):
            Code02_DiameterAndCommonEdges2.pop()
            if (Code02_DiameterAndCommonEdges2.e == jcast('int', (-1))):
                Code02_DiameterAndCommonEdges2.last[Code02_DiameterAndCommonEdges2.u] = jcast('int', Code02_DiameterAndCommonEdges2.f)
                Code02_DiameterAndCommonEdges2.dist[Code02_DiameterAndCommonEdges2.u] = jcast('long', Code02_DiameterAndCommonEdges2.c)
                Code02_DiameterAndCommonEdges2.e = jcast('int', Code02_DiameterAndCommonEdges2.head[Code02_DiameterAndCommonEdges2.u])
            else:
                Code02_DiameterAndCommonEdges2.e = jcast('int', Code02_DiameterAndCommonEdges2.next[Code02_DiameterAndCommonEdges2.e])
            if (Code02_DiameterAndCommonEdges2.e != 0):
                Code02_DiameterAndCommonEdges2.push(Code02_DiameterAndCommonEdges2.u, Code02_DiameterAndCommonEdges2.f, Code02_DiameterAndCommonEdges2.e, Code02_DiameterAndCommonEdges2.c)
                if (Code02_DiameterAndCommonEdges2.to[Code02_DiameterAndCommonEdges2.e] != Code02_DiameterAndCommonEdges2.f):
                    Code02_DiameterAndCommonEdges2.push(Code02_DiameterAndCommonEdges2.to[Code02_DiameterAndCommonEdges2.e], Code02_DiameterAndCommonEdges2.u, jcast('int', (-1)), jcast('long', jadd(Code02_DiameterAndCommonEdges2.c, Code02_DiameterAndCommonEdges2.weight[Code02_DiameterAndCommonEdges2.e])))

    # maxDistanceExceptDiameter方法改迭代版
    # 不会改，看讲解118，讲了怎么从递归版改成迭代版
    @staticmethod
    def maxDistanceExceptDiameter(root):
        root = jcast('int', root)
        Code02_DiameterAndCommonEdges2.stackSize = jcast('int', 0)
        Code02_DiameterAndCommonEdges2.push(root, 0, jcast('int', (-1)), 0)
        ans = jcast('long', 0)
        while (Code02_DiameterAndCommonEdges2.stackSize > 0):
            Code02_DiameterAndCommonEdges2.pop()
            if (Code02_DiameterAndCommonEdges2.e == jcast('int', (-1))):
                Code02_DiameterAndCommonEdges2.e = jcast('int', Code02_DiameterAndCommonEdges2.head[Code02_DiameterAndCommonEdges2.u])
            else:
                Code02_DiameterAndCommonEdges2.e = jcast('int', Code02_DiameterAndCommonEdges2.next[Code02_DiameterAndCommonEdges2.e])
            v = 0
            if (Code02_DiameterAndCommonEdges2.e != 0):
                Code02_DiameterAndCommonEdges2.push(Code02_DiameterAndCommonEdges2.u, Code02_DiameterAndCommonEdges2.f, Code02_DiameterAndCommonEdges2.e, Code02_DiameterAndCommonEdges2.c)
                v = jcast('int', Code02_DiameterAndCommonEdges2.to[Code02_DiameterAndCommonEdges2.e])
                if ((not Code02_DiameterAndCommonEdges2.diameterPath[v]) and (v != Code02_DiameterAndCommonEdges2.f)):
                    Code02_DiameterAndCommonEdges2.push(v, Code02_DiameterAndCommonEdges2.u, jcast('int', (-1)), jcast('long', jadd(Code02_DiameterAndCommonEdges2.c, Code02_DiameterAndCommonEdges2.weight[Code02_DiameterAndCommonEdges2.e])))
            else:
                ans = jcast('long', jstatic('Math', 'max', ans, Code02_DiameterAndCommonEdges2.c))
        return jcast('long', ans)

    @staticmethod
    def compute():
        Code02_DiameterAndCommonEdges2.road()
        i = jcast('int', Code02_DiameterAndCommonEdges2.end)
        while (i != 0):
            Code02_DiameterAndCommonEdges2.diameterPath[i] = jcast('boolean', True)
            i = jcast('int', Code02_DiameterAndCommonEdges2.last[i])
        l = jcast('int', Code02_DiameterAndCommonEdges2.start)
        r = jcast('int', Code02_DiameterAndCommonEdges2.end)
        maxDist = 0
        i = jcast('int', Code02_DiameterAndCommonEdges2.last[Code02_DiameterAndCommonEdges2.end])
        while (i != Code02_DiameterAndCommonEdges2.start):
            maxDist = jcast('long', Code02_DiameterAndCommonEdges2.maxDistanceExceptDiameter(i))
            if (maxDist == jcast('long', (Code02_DiameterAndCommonEdges2.diameter - Code02_DiameterAndCommonEdges2.dist[i]))):
                r = jcast('int', i)
            if ((maxDist == Code02_DiameterAndCommonEdges2.dist[i]) and (l == Code02_DiameterAndCommonEdges2.start)):
                l = jcast('int', i)
            i = jcast('int', Code02_DiameterAndCommonEdges2.last[i])
        if (l == r):
            Code02_DiameterAndCommonEdges2.commonEdges = jcast('int', 0)
        else:
            Code02_DiameterAndCommonEdges2.commonEdges = jcast('int', 1)
            i = jcast('int', Code02_DiameterAndCommonEdges2.last[r])
            while (i != l):
                Code02_DiameterAndCommonEdges2.commonEdges = jcast('int', (Code02_DiameterAndCommonEdges2.commonEdges + 1))
                i = jcast('int', Code02_DiameterAndCommonEdges2.last[i])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_DiameterAndCommonEdges2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code02_DiameterAndCommonEdges2.build()
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code02_DiameterAndCommonEdges2.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            w = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_DiameterAndCommonEdges2.addEdge(u, v, w)
            Code02_DiameterAndCommonEdges2.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        Code02_DiameterAndCommonEdges2.compute()
        jcall(out, 'println', Code02_DiameterAndCommonEdges2.diameter)
        jcall(out, 'println', Code02_DiameterAndCommonEdges2.commonEdges)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_DiameterAndCommonEdges2.MAXN = jcast('int', 200001)
Code02_DiameterAndCommonEdges2.n = jcast('int', 0)
Code02_DiameterAndCommonEdges2.head = jarray('int', [Code02_DiameterAndCommonEdges2.MAXN])
Code02_DiameterAndCommonEdges2.next = jarray('int', [jcast('int', (Code02_DiameterAndCommonEdges2.MAXN << (1 & 31)))])
Code02_DiameterAndCommonEdges2.to = jarray('int', [jcast('int', (Code02_DiameterAndCommonEdges2.MAXN << (1 & 31)))])
Code02_DiameterAndCommonEdges2.weight = jarray('int', [jcast('int', (Code02_DiameterAndCommonEdges2.MAXN << (1 & 31)))])
Code02_DiameterAndCommonEdges2.cnt = jcast('int', 0)
Code02_DiameterAndCommonEdges2.start = jcast('int', 0)
Code02_DiameterAndCommonEdges2.end = jcast('int', 0)
Code02_DiameterAndCommonEdges2.dist = jarray('long', [Code02_DiameterAndCommonEdges2.MAXN])
Code02_DiameterAndCommonEdges2.last = jarray('int', [Code02_DiameterAndCommonEdges2.MAXN])
Code02_DiameterAndCommonEdges2.diameter = jcast('long', 0)
Code02_DiameterAndCommonEdges2.diameterPath = jarray('boolean', [Code02_DiameterAndCommonEdges2.MAXN])
Code02_DiameterAndCommonEdges2.commonEdges = jcast('int', 0)
Code02_DiameterAndCommonEdges2.ufeStack = jarray('int', [Code02_DiameterAndCommonEdges2.MAXN, 3])
Code02_DiameterAndCommonEdges2.distStack = jarray('long', [Code02_DiameterAndCommonEdges2.MAXN])
Code02_DiameterAndCommonEdges2.stackSize = jcast('int', 0)
Code02_DiameterAndCommonEdges2.u = jcast('int', 0)
Code02_DiameterAndCommonEdges2.f = jcast('int', 0)
Code02_DiameterAndCommonEdges2.e = jcast('int', 0)
Code02_DiameterAndCommonEdges2.c = jcast('long', 0)

if __name__ == '__main__':
    Code02_DiameterAndCommonEdges2.main([])
