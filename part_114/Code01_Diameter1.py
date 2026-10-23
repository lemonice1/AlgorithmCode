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

# 树的直径模版(两遍dfs)
# 给定一棵树，边权可能为负，求直径长度
# 测试链接 : https://www.luogu.com.cn/problem/U81904
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 会有无法通过的用例，因为树上有负边
class Code01_Diameter1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'start': 'start', 'end': 'end', 'diameter': 'diameter', 'dist': 'dist', 'last': 'last'}
    MAXN = 0
    n = 0
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    # 直径的开始点
    start = 0
    # 直径的结束点
    end = 0
    # 直径长度
    diameter = 0
    # dist[i] : 从规定的头节点出发，走到i的距离
    dist = None
    # last[i] : 从规定的头节点出发，i节点的上一个节点
    last = None
    @staticmethod
    def build():
        Code01_Diameter1.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code01_Diameter1.head, 1, jcast('int', jadd(Code01_Diameter1.n, 1)), 0)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code01_Diameter1.next[Code01_Diameter1.cnt] = jcast('int', Code01_Diameter1.head[u])
        Code01_Diameter1.to[Code01_Diameter1.cnt] = jcast('int', v)
        Code01_Diameter1.weight[Code01_Diameter1.cnt] = jcast('int', w)
        jset(Code01_Diameter1.head, u, ((_java_obj_1 := Code01_Diameter1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def road():
        Code01_Diameter1.dfs(1, 0, 0)
        Code01_Diameter1.start = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code01_Diameter1.n):
            if (Code01_Diameter1.dist[i] > Code01_Diameter1.dist[Code01_Diameter1.start]):
                Code01_Diameter1.start = jcast('int', i)
            i = jcast('int', (i + 1))
        Code01_Diameter1.dfs(Code01_Diameter1.start, 0, 0)
        Code01_Diameter1.end = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code01_Diameter1.n):
            if (Code01_Diameter1.dist[i] > Code01_Diameter1.dist[Code01_Diameter1.end]):
                Code01_Diameter1.end = jcast('int', i)
            i = jcast('int', (i + 1))
        Code01_Diameter1.diameter = jcast('int', Code01_Diameter1.dist[Code01_Diameter1.end])

    @staticmethod
    def dfs(u, f, w):
        u = jcast('int', u)
        f = jcast('int', f)
        w = jcast('int', w)
        Code01_Diameter1.last[u] = jcast('int', f)
        Code01_Diameter1.dist[u] = jcast('int', jcast('int', jadd(Code01_Diameter1.dist[f], w)))
        e = jcast('int', Code01_Diameter1.head[u])
        while (e != 0):
            if (Code01_Diameter1.to[e] != f):
                Code01_Diameter1.dfs(Code01_Diameter1.to[e], u, Code01_Diameter1.weight[e])
            e = jcast('int', Code01_Diameter1.next[e])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_Diameter1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code01_Diameter1.build()
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code01_Diameter1.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            w = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_Diameter1.addEdge(u, v, w)
            Code01_Diameter1.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        Code01_Diameter1.road()
        jcall(out, 'println', Code01_Diameter1.diameter)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_Diameter1.MAXN = jcast('int', 500001)
Code01_Diameter1.n = jcast('int', 0)
Code01_Diameter1.head = jarray('int', [Code01_Diameter1.MAXN])
Code01_Diameter1.next = jarray('int', [jcast('int', (Code01_Diameter1.MAXN << (1 & 31)))])
Code01_Diameter1.to = jarray('int', [jcast('int', (Code01_Diameter1.MAXN << (1 & 31)))])
Code01_Diameter1.weight = jarray('int', [jcast('int', (Code01_Diameter1.MAXN << (1 & 31)))])
Code01_Diameter1.cnt = jcast('int', 0)
Code01_Diameter1.start = jcast('int', 0)
Code01_Diameter1.end = jcast('int', 0)
Code01_Diameter1.diameter = jcast('int', 0)
Code01_Diameter1.dist = jarray('int', [Code01_Diameter1.MAXN])
Code01_Diameter1.last = jarray('int', [Code01_Diameter1.MAXN])

if __name__ == '__main__':
    Code01_Diameter1.main([])
