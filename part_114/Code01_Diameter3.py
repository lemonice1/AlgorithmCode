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

# 树的直径模版(树型dp版逻辑小化简)
# 给定一棵树，边权可能为负，求直径长度
# 测试链接 : https://www.luogu.com.cn/problem/U81904
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_Diameter3:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'dist': 'dist', 'diameter': 'diameter'}
    MAXN = 0
    n = 0
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    dist = None
    # 直径的长度
    diameter = 0
    @staticmethod
    def build():
        Code01_Diameter3.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code01_Diameter3.head, 1, jcast('int', jadd(Code01_Diameter3.n, 1)), 0)
        jstatic('Arrays', 'fill', Code01_Diameter3.dist, 1, jcast('int', jadd(Code01_Diameter3.n, 1)), 0)
        Code01_Diameter3.diameter = jcast('int', jget(Integer, 'MIN_VALUE'))

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code01_Diameter3.next[Code01_Diameter3.cnt] = jcast('int', Code01_Diameter3.head[u])
        Code01_Diameter3.to[Code01_Diameter3.cnt] = jcast('int', v)
        Code01_Diameter3.weight[Code01_Diameter3.cnt] = jcast('int', w)
        jset(Code01_Diameter3.head, u, ((_java_obj_1 := Code01_Diameter3), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dp(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code01_Diameter3.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code01_Diameter3.to[e])
            if (v != f):
                Code01_Diameter3.dp(v, u)
            e = jcast('int', Code01_Diameter3.next[e])
        e = jcast('int', Code01_Diameter3.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code01_Diameter3.to[e])
            if (v != f):
                # 干脆直接去更新diameter
                Code01_Diameter3.diameter = jcast('int', jstatic('Math', 'max', Code01_Diameter3.diameter, jcast('int', jadd(jcast('int', jadd(Code01_Diameter3.dist[u], Code01_Diameter3.dist[v])), Code01_Diameter3.weight[e]))))
                jset(Code01_Diameter3.dist, u, jstatic('Math', 'max', Code01_Diameter3.dist[u], jcast('int', jadd(Code01_Diameter3.dist[v], Code01_Diameter3.weight[e]))))
            e = jcast('int', Code01_Diameter3.next[e])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_Diameter3.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code01_Diameter3.build()
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code01_Diameter3.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            w = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_Diameter3.addEdge(u, v, w)
            Code01_Diameter3.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        Code01_Diameter3.dp(1, 0)
        jcall(out, 'println', Code01_Diameter3.diameter)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_Diameter3.MAXN = jcast('int', 500001)
Code01_Diameter3.n = jcast('int', 0)
Code01_Diameter3.head = jarray('int', [Code01_Diameter3.MAXN])
Code01_Diameter3.next = jarray('int', [jcast('int', (Code01_Diameter3.MAXN << (1 & 31)))])
Code01_Diameter3.to = jarray('int', [jcast('int', (Code01_Diameter3.MAXN << (1 & 31)))])
Code01_Diameter3.weight = jarray('int', [jcast('int', (Code01_Diameter3.MAXN << (1 & 31)))])
Code01_Diameter3.cnt = jcast('int', 0)
Code01_Diameter3.dist = jarray('int', [Code01_Diameter3.MAXN])
Code01_Diameter3.diameter = jcast('int', 0)

if __name__ == '__main__':
    Code01_Diameter3.main([])
