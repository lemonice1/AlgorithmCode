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

# 造公园
# 一共n个节点，编号1~n，有m条边连接，边权都是1
# 所有节点可能形成多个连通区，每个连通区保证是树结构
# 有两种类型的操作
# 操作 1 x   : 返回x到离它最远的点的距离
# 操作 2 x y : 如果x和y已经连通，那么忽略
# 如果不连通，那么执行连通操作，把x和y各自的区域连通起来
# 并且要保证连通成的大区域的直径长度最小
# 测试链接 : https://www.luogu.com.cn/problem/P2195
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_BuildPark:
    __java_fields__ = {'MAXN': 'MAXN', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'father': 'father', 'dist': 'dist', 'diameter': 'diameter'}
    MAXN = 0
    head = None
    next = None
    to = None
    cnt = 0
    # 并查集需要
    father = None
    # 树型dp需要
    # dist[u] : 从u开始必须往下走，能走出的最大距离，可以不选任何边
    dist = None
    # diameter[i] : 如果i是集合的头节点，diameter[i]表示整个集合的直径长度
    # 如果i不再是集合的头节点，diameter[i]的值没有用
    # 并查集 + 集合打标签技巧，不会的看讲解056、讲解057
    diameter = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code03_BuildPark.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code03_BuildPark.head, 1, n, 0)
        i = jcast('int', 1)
        while (i <= n):
            Code03_BuildPark.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'fill', Code03_BuildPark.dist, 1, n, 0)
        jstatic('Arrays', 'fill', Code03_BuildPark.diameter, 1, n, 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code03_BuildPark.next[Code03_BuildPark.cnt] = jcast('int', Code03_BuildPark.head[u])
        Code03_BuildPark.to[Code03_BuildPark.cnt] = jcast('int', v)
        jset(Code03_BuildPark.head, u, ((_java_obj_1 := Code03_BuildPark), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code03_BuildPark.father[i]):
            jset(Code03_BuildPark.father, i, Code03_BuildPark.find(Code03_BuildPark.father[i]))
        return jcast('int', Code03_BuildPark.father[i])

    # 树型dp的方式求直径长度
    @staticmethod
    def dp(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code03_BuildPark.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_BuildPark.to[e])
            if (v != f):
                Code03_BuildPark.dp(v, u)
            e = jcast('int', Code03_BuildPark.next[e])
        e = jcast('int', Code03_BuildPark.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code03_BuildPark.to[e])
            if (v != f):
                jset(Code03_BuildPark.diameter, u, jstatic('Math', 'max', Code03_BuildPark.diameter[u], jstatic('Math', 'max', Code03_BuildPark.diameter[v], jcast('int', jadd(jcast('int', jadd(Code03_BuildPark.dist[u], Code03_BuildPark.dist[v])), 1)))))
                jset(Code03_BuildPark.dist, u, jstatic('Math', 'max', Code03_BuildPark.dist[u], jcast('int', jadd(Code03_BuildPark.dist[v], 1))))
            e = jcast('int', Code03_BuildPark.next[e])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        q = jcast('int', jcast('int', jget(in_, 'nval')))
        Code03_BuildPark.build(n)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_BuildPark.addEdge(u, v)
            Code03_BuildPark.addEdge(v, u)
            u = jcast('int', Code03_BuildPark.find(u))
            v = jcast('int', Code03_BuildPark.find(v))
            Code03_BuildPark.father[u] = jcast('int', v)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= n):
            if (i == Code03_BuildPark.father[i]):
                Code03_BuildPark.dp(i, 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        while (i <= q):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            if (op == 1):
                jcall(in_, 'nextToken')
                x = jcast('int', jcast('int', jget(in_, 'nval')))
                x = jcast('int', Code03_BuildPark.find(x))
                jcall(out, 'println', Code03_BuildPark.diameter[x])
            else:
                jcall(in_, 'nextToken')
                x = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                y = jcast('int', jcast('int', jget(in_, 'nval')))
                x = jcast('int', Code03_BuildPark.find(x))
                y = jcast('int', Code03_BuildPark.find(y))
                if (x != y):
                    Code03_BuildPark.father[x] = jcast('int', y)
                    jset(Code03_BuildPark.diameter, y, jstatic('Math', 'max', jcast('int', jadd(jcast('int', jadd(jcast('int', jdiv(jcast('int', jadd(Code03_BuildPark.diameter[x], 1)), 2)), jcast('int', jdiv(jcast('int', jadd(Code03_BuildPark.diameter[y], 1)), 2)))), 1)), jstatic('Math', 'max', Code03_BuildPark.diameter[x], Code03_BuildPark.diameter[y])))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_BuildPark.MAXN = jcast('int', 300001)
Code03_BuildPark.head = jarray('int', [Code03_BuildPark.MAXN])
Code03_BuildPark.next = jarray('int', [jcast('int', (Code03_BuildPark.MAXN << (1 & 31)))])
Code03_BuildPark.to = jarray('int', [jcast('int', (Code03_BuildPark.MAXN << (1 & 31)))])
Code03_BuildPark.cnt = jcast('int', 0)
Code03_BuildPark.father = jarray('int', [Code03_BuildPark.MAXN])
Code03_BuildPark.dist = jarray('int', [Code03_BuildPark.MAXN])
Code03_BuildPark.diameter = jarray('int', [Code03_BuildPark.MAXN])

if __name__ == '__main__':
    Code03_BuildPark.main([])
