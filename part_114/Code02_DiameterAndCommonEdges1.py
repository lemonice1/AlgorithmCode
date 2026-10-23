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

# 所有直径的公共部分(递归版)
# 给定一棵树，边权都为正
# 打印直径长度、所有直径的公共部分有几条边
# 测试链接 : https://www.luogu.com.cn/problem/P3304
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
# 对应实现可参考 Code02_DiameterAndCommonEdges2.py
class Code02_DiameterAndCommonEdges1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'start': 'start', 'end': 'end', 'dist': 'dist', 'last': 'last', 'diameter': 'diameter', 'diameterPath': 'diameterPath', 'commonEdges': 'commonEdges'}
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
        Code02_DiameterAndCommonEdges1.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code02_DiameterAndCommonEdges1.head, 1, jcast('int', jadd(Code02_DiameterAndCommonEdges1.n, 1)), 0)
        jstatic('Arrays', 'fill', Code02_DiameterAndCommonEdges1.diameterPath, 1, jcast('int', jadd(Code02_DiameterAndCommonEdges1.n, 1)), False)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code02_DiameterAndCommonEdges1.next[Code02_DiameterAndCommonEdges1.cnt] = jcast('int', Code02_DiameterAndCommonEdges1.head[u])
        Code02_DiameterAndCommonEdges1.to[Code02_DiameterAndCommonEdges1.cnt] = jcast('int', v)
        Code02_DiameterAndCommonEdges1.weight[Code02_DiameterAndCommonEdges1.cnt] = jcast('int', w)
        jset(Code02_DiameterAndCommonEdges1.head, u, ((_java_obj_1 := Code02_DiameterAndCommonEdges1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def road():
        Code02_DiameterAndCommonEdges1.dfs(1, 0, 0)
        Code02_DiameterAndCommonEdges1.start = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code02_DiameterAndCommonEdges1.n):
            if (Code02_DiameterAndCommonEdges1.dist[i] > Code02_DiameterAndCommonEdges1.dist[Code02_DiameterAndCommonEdges1.start]):
                Code02_DiameterAndCommonEdges1.start = jcast('int', i)
            i = jcast('int', (i + 1))
        Code02_DiameterAndCommonEdges1.dfs(Code02_DiameterAndCommonEdges1.start, 0, 0)
        Code02_DiameterAndCommonEdges1.end = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code02_DiameterAndCommonEdges1.n):
            if (Code02_DiameterAndCommonEdges1.dist[i] > Code02_DiameterAndCommonEdges1.dist[Code02_DiameterAndCommonEdges1.end]):
                Code02_DiameterAndCommonEdges1.end = jcast('int', i)
            i = jcast('int', (i + 1))
        Code02_DiameterAndCommonEdges1.diameter = jcast('long', Code02_DiameterAndCommonEdges1.dist[Code02_DiameterAndCommonEdges1.end])

    @staticmethod
    def dfs(u, f, c):
        u = jcast('int', u)
        f = jcast('int', f)
        c = jcast('long', c)
        Code02_DiameterAndCommonEdges1.last[u] = jcast('int', f)
        Code02_DiameterAndCommonEdges1.dist[u] = jcast('long', c)
        e = jcast('int', Code02_DiameterAndCommonEdges1.head[u])
        while (e != 0):
            if (Code02_DiameterAndCommonEdges1.to[e] != f):
                Code02_DiameterAndCommonEdges1.dfs(Code02_DiameterAndCommonEdges1.to[e], u, jcast('long', jadd(c, Code02_DiameterAndCommonEdges1.weight[e])))
            e = jcast('int', Code02_DiameterAndCommonEdges1.next[e])

    # 不能走向直径路径上的节点
    # 能走出的最大距离
    @staticmethod
    def maxDistanceExceptDiameter(u, f, c):
        u = jcast('int', u)
        f = jcast('int', f)
        c = jcast('long', c)
        ans = jcast('long', c)
        e = jcast('int', Code02_DiameterAndCommonEdges1.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code02_DiameterAndCommonEdges1.to[e])
            if ((not Code02_DiameterAndCommonEdges1.diameterPath[v]) and (v != f)):
                ans = jcast('long', jstatic('Math', 'max', ans, Code02_DiameterAndCommonEdges1.maxDistanceExceptDiameter(v, u, jcast('long', jadd(c, Code02_DiameterAndCommonEdges1.weight[e])))))
            e = jcast('int', Code02_DiameterAndCommonEdges1.next[e])
        return jcast('long', ans)

    @staticmethod
    def compute():
        Code02_DiameterAndCommonEdges1.road()
        i = jcast('int', Code02_DiameterAndCommonEdges1.end)
        while (i != 0):
            Code02_DiameterAndCommonEdges1.diameterPath[i] = jcast('boolean', True)
            i = jcast('int', Code02_DiameterAndCommonEdges1.last[i])
        l = jcast('int', Code02_DiameterAndCommonEdges1.start)
        r = jcast('int', Code02_DiameterAndCommonEdges1.end)
        maxDist = 0
        i = jcast('int', Code02_DiameterAndCommonEdges1.last[Code02_DiameterAndCommonEdges1.end])
        while (i != Code02_DiameterAndCommonEdges1.start):
            maxDist = jcast('long', Code02_DiameterAndCommonEdges1.maxDistanceExceptDiameter(i, 0, 0))
            if (maxDist == jcast('long', (Code02_DiameterAndCommonEdges1.diameter - Code02_DiameterAndCommonEdges1.dist[i]))):
                r = jcast('int', i)
            if ((maxDist == Code02_DiameterAndCommonEdges1.dist[i]) and (l == Code02_DiameterAndCommonEdges1.start)):
                l = jcast('int', i)
            i = jcast('int', Code02_DiameterAndCommonEdges1.last[i])
        if (l == r):
            Code02_DiameterAndCommonEdges1.commonEdges = jcast('int', 0)
        else:
            Code02_DiameterAndCommonEdges1.commonEdges = jcast('int', 1)
            i = jcast('int', Code02_DiameterAndCommonEdges1.last[r])
            while (i != l):
                Code02_DiameterAndCommonEdges1.commonEdges = jcast('int', (Code02_DiameterAndCommonEdges1.commonEdges + 1))
                i = jcast('int', Code02_DiameterAndCommonEdges1.last[i])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_DiameterAndCommonEdges1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code02_DiameterAndCommonEdges1.build()
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code02_DiameterAndCommonEdges1.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            w = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_DiameterAndCommonEdges1.addEdge(u, v, w)
            Code02_DiameterAndCommonEdges1.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        Code02_DiameterAndCommonEdges1.compute()
        jcall(out, 'println', Code02_DiameterAndCommonEdges1.diameter)
        jcall(out, 'println', Code02_DiameterAndCommonEdges1.commonEdges)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_DiameterAndCommonEdges1.MAXN = jcast('int', 200001)
Code02_DiameterAndCommonEdges1.n = jcast('int', 0)
Code02_DiameterAndCommonEdges1.head = jarray('int', [Code02_DiameterAndCommonEdges1.MAXN])
Code02_DiameterAndCommonEdges1.next = jarray('int', [jcast('int', (Code02_DiameterAndCommonEdges1.MAXN << (1 & 31)))])
Code02_DiameterAndCommonEdges1.to = jarray('int', [jcast('int', (Code02_DiameterAndCommonEdges1.MAXN << (1 & 31)))])
Code02_DiameterAndCommonEdges1.weight = jarray('int', [jcast('int', (Code02_DiameterAndCommonEdges1.MAXN << (1 & 31)))])
Code02_DiameterAndCommonEdges1.cnt = jcast('int', 0)
Code02_DiameterAndCommonEdges1.start = jcast('int', 0)
Code02_DiameterAndCommonEdges1.end = jcast('int', 0)
Code02_DiameterAndCommonEdges1.dist = jarray('long', [Code02_DiameterAndCommonEdges1.MAXN])
Code02_DiameterAndCommonEdges1.last = jarray('int', [Code02_DiameterAndCommonEdges1.MAXN])
Code02_DiameterAndCommonEdges1.diameter = jcast('long', 0)
Code02_DiameterAndCommonEdges1.diameterPath = jarray('boolean', [Code02_DiameterAndCommonEdges1.MAXN])
Code02_DiameterAndCommonEdges1.commonEdges = jcast('int', 0)

if __name__ == '__main__':
    Code02_DiameterAndCommonEdges1.main([])
