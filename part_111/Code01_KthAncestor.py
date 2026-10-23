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

# 树节点的第K个祖先
# 树上有n个节点，编号0 ~ n-1，树的结构用parent数组代表
# 其中parent[i]是节点i的父节点，树的根节点是编号为0
# 树节点i的第k个祖先节点，是从节点i开始往上跳k步所来到的节点
# 实现TreeAncestor类
# TreeAncestor(int n, int[] parent) : 初始化
# getKthAncestor(int i, int k) : 返回节点i的第k个祖先节点，不存在返回-1
# 测试链接 : https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/
class Code01_KthAncestor:
    __java_fields__ = {}
    class TreeAncestor:
        __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'power': 'power', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'deep': 'deep', 'stjump': 'stjump'}
        MAXN = 0
        LIMIT = 0
        # 根据节点个数n，计算出2的几次方就够用了
        power = 0
        @staticmethod
        def log2(n):
            n = jcast('int', n)
            ans = jcast('int', 0)
            while (jcast('int', (1 << (ans & 31))) <= jcast('int', (n >> (1 & 31)))):
                ans = jcast('int', (ans + 1))
            return jcast('int', ans)

        # 链式前向星建图
        head = None
        next = None
        to = None
        cnt = 0
        # deep[i] : 节点i在第几层
        deep = None
        # stjump[i][p] : 节点i往上跳2的p次方步，到达的节点编号
        stjump = None
        def _java_init_0(self, n, parent):
            n = jcast('int', n)
            jset(Code01_KthAncestor.TreeAncestor, 'power', Code01_KthAncestor.TreeAncestor.log2(n))
            jset(Code01_KthAncestor.TreeAncestor, 'cnt', 1)
            jstatic('Arrays', 'fill', Code01_KthAncestor.TreeAncestor.head, 0, n, 0)
            i = jcast('int', 1)
            while (i < jget(parent, 'length')):
                Code01_KthAncestor.TreeAncestor.addEdge(parent[i], i)
                i = jcast('int', (i + 1))
            Code01_KthAncestor.TreeAncestor.dfs(0, 0)

        @staticmethod
        def addEdge(u, v):
            u = jcast('int', u)
            v = jcast('int', v)
            jset(Code01_KthAncestor.TreeAncestor.next, Code01_KthAncestor.TreeAncestor.cnt, Code01_KthAncestor.TreeAncestor.head[u])
            jset(Code01_KthAncestor.TreeAncestor.to, Code01_KthAncestor.TreeAncestor.cnt, v)
            jset(Code01_KthAncestor.TreeAncestor.head, u, ((_java_obj_1 := Code01_KthAncestor.TreeAncestor), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

        # 当前来到i节点，i节点父亲节点是f
        @staticmethod
        def dfs(i, f):
            i = jcast('int', i)
            f = jcast('int', f)
            if (i == 0):
                jset(Code01_KthAncestor.TreeAncestor.deep, i, 1)
            else:
                jset(Code01_KthAncestor.TreeAncestor.deep, i, jcast('int', jadd(Code01_KthAncestor.TreeAncestor.deep[f], 1)))
            jset(Code01_KthAncestor.TreeAncestor.stjump[i], 0, f)
            p = jcast('int', 1)
            while (p <= Code01_KthAncestor.TreeAncestor.power):
                jset(Code01_KthAncestor.TreeAncestor.stjump[i], p, Code01_KthAncestor.TreeAncestor.stjump[Code01_KthAncestor.TreeAncestor.stjump[i][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                p = jcast('int', (p + 1))
            e = jcast('int', Code01_KthAncestor.TreeAncestor.head[i])
            while (e != 0):
                Code01_KthAncestor.TreeAncestor.dfs(Code01_KthAncestor.TreeAncestor.to[e], i)
                e = jcast('int', Code01_KthAncestor.TreeAncestor.next[e])

        def getKthAncestor(self, i, k):
            i = jcast('int', i)
            k = jcast('int', k)
            if (Code01_KthAncestor.TreeAncestor.deep[i] <= k):
                return jcast('int', jcast('int', (-1)))
            # s是想要去往的层数
            s = jcast('int', jcast('int', (Code01_KthAncestor.TreeAncestor.deep[i] - k)))
            p = jcast('int', Code01_KthAncestor.TreeAncestor.power)
            while (p >= 0):
                if (Code01_KthAncestor.TreeAncestor.deep[Code01_KthAncestor.TreeAncestor.stjump[i][p]] >= s):
                    i = jcast('int', Code01_KthAncestor.TreeAncestor.stjump[i][p])
                p = jcast('int', (p - 1))
            return jcast('int', i)

        def __init__(self, *args, _java_ctor=None):
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int', 'int[]']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_KthAncestor.TreeAncestor.TreeAncestor")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_KthAncestor.TreeAncestor.MAXN = jcast('int', 50001)
Code01_KthAncestor.TreeAncestor.LIMIT = jcast('int', 16)
Code01_KthAncestor.TreeAncestor.power = jcast('int', 0)
Code01_KthAncestor.TreeAncestor.head = jarray('int', [Code01_KthAncestor.TreeAncestor.MAXN])
Code01_KthAncestor.TreeAncestor.next = jarray('int', [Code01_KthAncestor.TreeAncestor.MAXN])
Code01_KthAncestor.TreeAncestor.to = jarray('int', [Code01_KthAncestor.TreeAncestor.MAXN])
Code01_KthAncestor.TreeAncestor.cnt = jcast('int', 0)
Code01_KthAncestor.TreeAncestor.deep = jarray('int', [Code01_KthAncestor.TreeAncestor.MAXN])
Code01_KthAncestor.TreeAncestor.stjump = jarray('int', [Code01_KthAncestor.TreeAncestor.MAXN, Code01_KthAncestor.TreeAncestor.LIMIT])
