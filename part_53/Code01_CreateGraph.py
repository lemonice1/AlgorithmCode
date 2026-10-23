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

class Code01_CreateGraph:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'graph1': 'graph1', 'graph2': 'graph2', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt'}
    # 点的最大数量
    MAXN = 0
    # 边的最大数量
    # 只有链式前向星方式建图需要这个数量
    # 注意如果无向图的最大数量是m条边，数量要准备m*2
    # 因为一条无向边要加两条有向边
    MAXM = 0
    # 邻接矩阵方式建图
    graph1 = None
    # 邻接表方式建图
    # public static ArrayList<ArrayList<Integer>> graph2 = new ArrayList<>();
    graph2 = None
    # 链式前向星方式建图
    head = None
    next = None
    to = None
    # 如果边有权重，那么需要这个数组
    weight = None
    cnt = 0
    @staticmethod
    def build(n):
        n = jcast('int', n)
        # 邻接矩阵清空
        i = jcast('int', 1)
        while (i <= n):
            j = jcast('int', 1)
            while (j <= n):
                jset(Code01_CreateGraph.graph1[i], j, 0)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        # 邻接表清空和准备
        jcall(Code01_CreateGraph.graph2, 'clear')
        # 下标需要支持1~n，所以加入n+1个列表，0下标准备但不用
        i = jcast('int', 0)
        while (i <= n):
            jcall(Code01_CreateGraph.graph2, 'add', jnew('ArrayList'))
            i = jcast('int', (i + 1))
        # 链式前向星清空
        Code01_CreateGraph.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code01_CreateGraph.head, 1, jcast('int', jadd(n, 1)), 0)

    # 链式前向星加边
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        # u -> v , 边权重是w
        Code01_CreateGraph.next[Code01_CreateGraph.cnt] = jcast('int', Code01_CreateGraph.head[u])
        Code01_CreateGraph.to[Code01_CreateGraph.cnt] = jcast('int', v)
        Code01_CreateGraph.weight[Code01_CreateGraph.cnt] = jcast('int', w)
        jset(Code01_CreateGraph.head, u, ((_java_obj_1 := Code01_CreateGraph), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # 三种方式建立有向图带权图
    @staticmethod
    def directGraph(edges):
        # 邻接矩阵建图
        for edge in edges:
            jset(Code01_CreateGraph.graph1[edge[0]], edge[1], edge[2])
        # 邻接表建图
        for edge in edges:
            # graph2.get(edge[0]).add(edge[1]);
            jcall(jcall(Code01_CreateGraph.graph2, 'get', edge[0]), 'add', jarray('int', [None], [edge[1], edge[2]]))
        # 链式前向星建图
        for edge in edges:
            Code01_CreateGraph.addEdge(edge[0], edge[1], edge[2])

    # 三种方式建立无向图带权图
    @staticmethod
    def undirectGraph(edges):
        # 邻接矩阵建图
        for edge in edges:
            jset(Code01_CreateGraph.graph1[edge[0]], edge[1], edge[2])
            jset(Code01_CreateGraph.graph1[edge[1]], edge[0], edge[2])
        # 邻接表建图
        for edge in edges:
            # graph2.get(edge[0]).add(edge[1]);
            # graph2.get(edge[1]).add(edge[0]);
            jcall(jcall(Code01_CreateGraph.graph2, 'get', edge[0]), 'add', jarray('int', [None], [edge[1], edge[2]]))
            jcall(jcall(Code01_CreateGraph.graph2, 'get', edge[1]), 'add', jarray('int', [None], [edge[0], edge[2]]))
        # 链式前向星建图
        for edge in edges:
            Code01_CreateGraph.addEdge(edge[0], edge[1], edge[2])
            Code01_CreateGraph.addEdge(edge[1], edge[0], edge[2])

    @staticmethod
    def traversal(n):
        n = jcast('int', n)
        jprint('邻接矩阵遍历 :', newline=True)
        i = jcast('int', 1)
        while (i <= n):
            j = jcast('int', 1)
            while (j <= n):
                jprint(jadd(Code01_CreateGraph.graph1[i][j], ' '), newline=False)
                j = jcast('int', (j + 1))
            jprint(newline=True)
            i = jcast('int', (i + 1))
        jprint('邻接表遍历 :', newline=True)
        i = jcast('int', 1)
        while (i <= n):
            jprint(jadd(i, '(邻居、边权) : '), newline=False)
            for edge in jcall(Code01_CreateGraph.graph2, 'get', i):
                jprint(jadd(jadd(jadd(jadd('(', edge[0]), ','), edge[1]), ') '), newline=False)
            jprint(newline=True)
            i = jcast('int', (i + 1))
        jprint('链式前向星 :', newline=True)
        i = jcast('int', 1)
        while (i <= n):
            jprint(jadd(i, '(邻居、边权) : '), newline=False)
            # 注意这个for循环，链式前向星的方式遍历
            ei = jcast('int', Code01_CreateGraph.head[i])
            while (ei > 0):
                jprint(jadd(jadd(jadd(jadd('(', Code01_CreateGraph.to[ei]), ','), Code01_CreateGraph.weight[ei]), ') '), newline=False)
                ei = jcast('int', Code01_CreateGraph.next[ei])
            jprint(newline=True)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        # 理解了带权图的建立过程，也就理解了不带权图
        # 点的编号为1...n
        # 例子1自己画一下图，有向带权图，然后打印结果
        n1 = jcast('int', 4)
        edges1 = jarray('int', [None, None], [[1, 3, 6], [4, 3, 4], [2, 4, 2], [1, 2, 7], [2, 3, 5], [3, 1, 1]])
        Code01_CreateGraph.build(n1)
        Code01_CreateGraph.directGraph(edges1)
        Code01_CreateGraph.traversal(n1)
        jprint('==============================', newline=True)
        # 例子2自己画一下图，无向带权图，然后打印结果
        n2 = jcast('int', 5)
        edges2 = jarray('int', [None, None], [[3, 5, 4], [4, 1, 1], [3, 4, 2], [5, 2, 4], [2, 3, 7], [1, 5, 5], [4, 2, 6]])
        Code01_CreateGraph.build(n2)
        Code01_CreateGraph.undirectGraph(edges2)
        Code01_CreateGraph.traversal(n2)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_CreateGraph.MAXN = jcast('int', 11)
Code01_CreateGraph.MAXM = jcast('int', 21)
Code01_CreateGraph.graph1 = jarray('int', [Code01_CreateGraph.MAXN, Code01_CreateGraph.MAXN])
Code01_CreateGraph.graph2 = jnew('ArrayList')
Code01_CreateGraph.head = jarray('int', [Code01_CreateGraph.MAXN])
Code01_CreateGraph.next = jarray('int', [Code01_CreateGraph.MAXM])
Code01_CreateGraph.to = jarray('int', [Code01_CreateGraph.MAXM])
Code01_CreateGraph.weight = jarray('int', [Code01_CreateGraph.MAXM])
Code01_CreateGraph.cnt = jcast('int', 0)

if __name__ == '__main__':
    Code01_CreateGraph.main([])
