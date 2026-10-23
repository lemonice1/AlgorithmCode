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

# 教父
# 一共有n个节点，编号1~n，有n-1条边形成一棵树
# 返回所有重心点
# 树的重心第二种求解方式
# 以某个节点为根时，每颗子树的节点数不超过总节点数的一半，那么这个节点是重心
# 测试链接 : http://poj.org/problem?id=3107
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Godfather:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'size': 'size', 'maxsub': 'maxsub'}
    MAXN = 0
    n = 0
    head = None
    next = None
    to = None
    cnt = 0
    size = None
    maxsub = None
    @staticmethod
    def build():
        Code02_Godfather.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code02_Godfather.head, 1, jcast('int', jadd(Code02_Godfather.n, 1)), 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code02_Godfather.next[Code02_Godfather.cnt] = jcast('int', Code02_Godfather.head[u])
        Code02_Godfather.to[Code02_Godfather.cnt] = jcast('int', v)
        jset(Code02_Godfather.head, u, ((_java_obj_1 := Code02_Godfather), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dfs(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code02_Godfather.size[u] = jcast('int', 1)
        Code02_Godfather.maxsub[u] = jcast('int', 0)
        e = jcast('int', Code02_Godfather.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code02_Godfather.to[e])
            if (v != f):
                Code02_Godfather.dfs(v, u)
                Code02_Godfather.size[u] = jcast('int', jcast('int', jadd(Code02_Godfather.size[u], Code02_Godfather.size[v])))
                jset(Code02_Godfather.maxsub, u, jstatic('Math', 'max', Code02_Godfather.maxsub[u], Code02_Godfather.size[v]))
            e = jcast('int', Code02_Godfather.next[e])
        jset(Code02_Godfather.maxsub, u, jstatic('Math', 'max', Code02_Godfather.maxsub[u], jcast('int', (Code02_Godfather.n - Code02_Godfather.size[u]))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_Godfather.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code02_Godfather.build()
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code02_Godfather.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_Godfather.addEdge(u, v)
            Code02_Godfather.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code02_Godfather.dfs(1, 0)
        m = jcast('int', 0)
        centers = jarray('int', [2])
        i = jcast('int', 1)
        while (i <= Code02_Godfather.n):
            if (Code02_Godfather.maxsub[i] <= jcast('int', jdiv(Code02_Godfather.n, 2))):
                jset(centers, ((_java_old_4 := m), (m := jcast('int', (m + (1)))), _java_old_4)[2], i)
            i = jcast('int', (i + 1))
        if (m == 1):
            jcall(out, 'println', centers[0])
            # m == 2
        else:
            jcall(out, 'println', jadd(jadd(centers[0], ' '), centers[1]))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Godfather.MAXN = jcast('int', 50001)
Code02_Godfather.n = jcast('int', 0)
Code02_Godfather.head = jarray('int', [Code02_Godfather.MAXN])
Code02_Godfather.next = jarray('int', [jcast('int', (Code02_Godfather.MAXN << (1 & 31)))])
Code02_Godfather.to = jarray('int', [jcast('int', (Code02_Godfather.MAXN << (1 & 31)))])
Code02_Godfather.cnt = jcast('int', 0)
Code02_Godfather.size = jarray('int', [Code02_Godfather.MAXN])
Code02_Godfather.maxsub = jarray('int', [Code02_Godfather.MAXN])

if __name__ == '__main__':
    Code02_Godfather.main([])
