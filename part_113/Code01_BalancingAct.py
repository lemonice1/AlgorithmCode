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

# 平衡行为
# 一共有n个节点，编号1~n，有n-1条边形成一棵树
# 返回重心点，返回重心点最大子树的节点数
# 树的重心第一种求解方式
# 以某个节点为根时，最大子树的节点数最少，那么这个节点是重心
# 测试链接 : http://poj.org/problem?id=1655
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_BalancingAct:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'size': 'size', 'center': 'center', 'best': 'best'}
    MAXN = 0
    n = 0
    head = None
    next = None
    to = None
    cnt = 0
    size = None
    center = 0
    best = 0
    @staticmethod
    def build():
        Code01_BalancingAct.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code01_BalancingAct.head, 1, jcast('int', jadd(Code01_BalancingAct.n, 1)), 0)
        Code01_BalancingAct.best = jcast('int', jget(Integer, 'MAX_VALUE'))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code01_BalancingAct.next[Code01_BalancingAct.cnt] = jcast('int', Code01_BalancingAct.head[u])
        Code01_BalancingAct.to[Code01_BalancingAct.cnt] = jcast('int', v)
        jset(Code01_BalancingAct.head, u, ((_java_obj_1 := Code01_BalancingAct), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # 当前来到u节点，父亲节点是f
    @staticmethod
    def dfs(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code01_BalancingAct.size[u] = jcast('int', 1)
        # 以当前节点u做根节点，最大的子树有多少节点
        maxsub = jcast('int', 0)
        e = jcast('int', Code01_BalancingAct.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code01_BalancingAct.to[e])
            if (v != f):
                Code01_BalancingAct.dfs(v, u)
                Code01_BalancingAct.size[u] = jcast('int', jcast('int', jadd(Code01_BalancingAct.size[u], Code01_BalancingAct.size[v])))
                maxsub = jcast('int', jstatic('Math', 'max', maxsub, Code01_BalancingAct.size[v]))
            e = jcast('int', Code01_BalancingAct.next[e])
        maxsub = jcast('int', jstatic('Math', 'max', maxsub, jcast('int', (Code01_BalancingAct.n - Code01_BalancingAct.size[u]))))
        # 题目要求找到编号最小的重心
        if ((maxsub < Code01_BalancingAct.best) or ((maxsub == Code01_BalancingAct.best) and (u < Code01_BalancingAct.center))):
            Code01_BalancingAct.best = jcast('int', maxsub)
            Code01_BalancingAct.center = jcast('int', u)

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
            Code01_BalancingAct.n = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_BalancingAct.build()
            i = jcast('int', 1)
            u = 0
            v = 0
            while (i < Code01_BalancingAct.n):
                jcall(in_, 'nextToken')
                u = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', jget(in_, 'nval')))
                Code01_BalancingAct.addEdge(u, v)
                Code01_BalancingAct.addEdge(v, u)
                i = jcast('int', (i + 1))
            Code01_BalancingAct.dfs(1, 0)
            jcall(out, 'println', jadd(jadd(Code01_BalancingAct.center, ' '), Code01_BalancingAct.best))
            t = jcast('int', (t + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_BalancingAct.MAXN = jcast('int', 20001)
Code01_BalancingAct.n = jcast('int', 0)
Code01_BalancingAct.head = jarray('int', [Code01_BalancingAct.MAXN])
Code01_BalancingAct.next = jarray('int', [jcast('int', (Code01_BalancingAct.MAXN << (1 & 31)))])
Code01_BalancingAct.to = jarray('int', [jcast('int', (Code01_BalancingAct.MAXN << (1 & 31)))])
Code01_BalancingAct.cnt = jcast('int', 0)
Code01_BalancingAct.size = jarray('int', [Code01_BalancingAct.MAXN])
Code01_BalancingAct.center = jcast('int', 0)
Code01_BalancingAct.best = jcast('int', 0)

if __name__ == '__main__':
    Code01_BalancingAct.main([])
