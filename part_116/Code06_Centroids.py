# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 哪些点可以改造成重心
# 给定一棵n个点的树，你可以随便删掉一条边，然后随便加上一条边
# 通过这种方式可以让很多点变成重心
# 打印所有能变成重心的点
# 测试链接 : https://www.luogu.com.cn/problem/CF708C
# 测试链接 : https://codeforces.com/problemset/problem/708/C
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_Centroids:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'size': 'size', 'maxsub': 'maxsub', 'inner1': 'inner1', 'inner2': 'inner2', 'choose': 'choose', 'outer': 'outer'}
    MAXN = 0
    n = 0
    head = None
    next = None
    to = None
    cnt = 0
    # size[i]: i内部，整棵子树大小
    size = None
    # maxsub[i]: i内部，最大子树，是i节点的哪个儿子拥有，记录节点编号
    maxsub = None
    # inner1[i]: i内部，<=n/2且第一大的子树是多大，记录大小
    inner1 = None
    # inner2[i]: i内部，<=n/2且第二大的子树是多大，记录大小
    inner2 = None
    # 注意: inner1[i]和inner2[i]，所代表的子树一定要来自i的不同儿子
    # choose[i]: inner1[i]所代表的子树，是i节点的哪个儿子拥有，记录节点编号
    choose = None
    # outer[i]: i外部，<=n/2且第一大的子树是多大，记录大小
    outer = None
    @staticmethod
    def build():
        Code06_Centroids.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code06_Centroids.head, 1, jcast('int', jadd(Code06_Centroids.n, 1)), 0)
        jstatic('Arrays', 'fill', Code06_Centroids.maxsub, 1, jcast('int', jadd(Code06_Centroids.n, 1)), 0)
        jstatic('Arrays', 'fill', Code06_Centroids.choose, 1, jcast('int', jadd(Code06_Centroids.n, 1)), 0)
        jstatic('Arrays', 'fill', Code06_Centroids.inner1, 1, jcast('int', jadd(Code06_Centroids.n, 1)), 0)
        jstatic('Arrays', 'fill', Code06_Centroids.inner2, 1, jcast('int', jadd(Code06_Centroids.n, 1)), 0)
        jstatic('Arrays', 'fill', Code06_Centroids.outer, 1, jcast('int', jadd(Code06_Centroids.n, 1)), 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code06_Centroids.next[Code06_Centroids.cnt] = jcast('int', Code06_Centroids.head[u])
        Code06_Centroids.to[Code06_Centroids.cnt] = jcast('int', v)
        jset(Code06_Centroids.head, u, ((_java_obj_1 := Code06_Centroids), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code06_Centroids.size[u] = jcast('int', 1)
        e = jcast('int', Code06_Centroids.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code06_Centroids.to[e])
            if (v != f):
                Code06_Centroids.dfs1(v, u)
                Code06_Centroids.size[u] = jcast('int', jcast('int', jadd(Code06_Centroids.size[u], Code06_Centroids.size[v])))
                if (Code06_Centroids.size[Code06_Centroids.maxsub[u]] < Code06_Centroids.size[v]):
                    Code06_Centroids.maxsub[u] = jcast('int', v)
                innerSize = jcast('int', (Code06_Centroids.size[v] if (Code06_Centroids.size[v] <= jcast('int', jdiv(Code06_Centroids.n, 2))) else Code06_Centroids.inner1[v]))
                if (Code06_Centroids.inner1[u] < innerSize):
                    Code06_Centroids.choose[u] = jcast('int', v)
                    Code06_Centroids.inner2[u] = jcast('int', Code06_Centroids.inner1[u])
                    Code06_Centroids.inner1[u] = jcast('int', innerSize)
                else:
                    if (Code06_Centroids.inner2[u] < innerSize):
                        Code06_Centroids.inner2[u] = jcast('int', innerSize)
            e = jcast('int', Code06_Centroids.next[e])

    @staticmethod
    def dfs2(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code06_Centroids.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code06_Centroids.to[e])
            if (v != f):
                if (jcast('int', (Code06_Centroids.n - Code06_Centroids.size[v])) <= jcast('int', jdiv(Code06_Centroids.n, 2))):
                    Code06_Centroids.outer[v] = jcast('int', jcast('int', (Code06_Centroids.n - Code06_Centroids.size[v])))
                else:
                    if (Code06_Centroids.choose[u] != v):
                        jset(Code06_Centroids.outer, v, jstatic('Math', 'max', Code06_Centroids.outer[u], Code06_Centroids.inner1[u]))
                    else:
                        jset(Code06_Centroids.outer, v, jstatic('Math', 'max', Code06_Centroids.outer[u], Code06_Centroids.inner2[u]))
                Code06_Centroids.dfs2(v, u)
            e = jcast('int', Code06_Centroids.next[e])

    @staticmethod
    def check(u):
        u = jcast('int', u)
        if (Code06_Centroids.size[Code06_Centroids.maxsub[u]] > jcast('int', jdiv(Code06_Centroids.n, 2))):
            return jcast('boolean', (jcast('int', (Code06_Centroids.size[Code06_Centroids.maxsub[u]] - Code06_Centroids.inner1[Code06_Centroids.maxsub[u]])) <= jcast('int', jdiv(Code06_Centroids.n, 2))))
        if (jcast('int', (Code06_Centroids.n - Code06_Centroids.size[u])) > jcast('int', jdiv(Code06_Centroids.n, 2))):
            return jcast('boolean', (jcast('int', (jcast('int', (Code06_Centroids.n - Code06_Centroids.size[u])) - Code06_Centroids.outer[u])) <= jcast('int', jdiv(Code06_Centroids.n, 2))))
        return jcast('boolean', True)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code06_Centroids.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code06_Centroids.build()
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code06_Centroids.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code06_Centroids.addEdge(u, v)
            Code06_Centroids.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code06_Centroids.dfs1(1, 0)
        Code06_Centroids.dfs2(1, 0)
        i = jcast('int', 1)
        while (i <= Code06_Centroids.n):
            jcall(out, 'print', ('1 ' if Code06_Centroids.check(i) else '0 '))
            i = jcast('int', (i + 1))
        jcall(out, 'println')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_Centroids.MAXN = jcast('int', 400001)
Code06_Centroids.n = jcast('int', 0)
Code06_Centroids.head = jarray('int', [Code06_Centroids.MAXN])
Code06_Centroids.next = jarray('int', [jcast('int', (Code06_Centroids.MAXN << (1 & 31)))])
Code06_Centroids.to = jarray('int', [jcast('int', (Code06_Centroids.MAXN << (1 & 31)))])
Code06_Centroids.cnt = jcast('int', 0)
Code06_Centroids.size = jarray('int', [Code06_Centroids.MAXN])
Code06_Centroids.maxsub = jarray('int', [Code06_Centroids.MAXN])
Code06_Centroids.inner1 = jarray('int', [Code06_Centroids.MAXN])
Code06_Centroids.inner2 = jarray('int', [Code06_Centroids.MAXN])
Code06_Centroids.choose = jarray('int', [Code06_Centroids.MAXN])
Code06_Centroids.outer = jarray('int', [Code06_Centroids.MAXN])

if __name__ == '__main__':
    Code06_Centroids.main([])
