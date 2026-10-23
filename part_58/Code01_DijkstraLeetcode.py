# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# Dijkstra算法模版（Leetcode）
# 网络延迟时间
# 有 n 个网络节点，标记为 1 到 n
# 给你一个列表 times，表示信号经过 有向 边的传递时间
# times[i] = (ui, vi, wi)，表示从ui到vi传递信号的时间是wi
# 现在，从某个节点 s 发出一个信号
# 需要多久才能使所有节点都收到信号
# 如果不能使所有节点收到信号，返回 -1
# 测试链接 : https://leetcode.cn/problems/network-delay-time
class Code01_DijkstraLeetcode:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'heap': 'heap', 'where': 'where', 'heapSize': 'heapSize', 'distance': 'distance'}
    # 动态建图+普通堆的实现
    @staticmethod
    def networkDelayTime1(times, n, s):
        n = jcast('int', n)
        s = jcast('int', s)
        graph = jnew('ArrayList')
        i = jcast('int', 0)
        while (i <= n):
            jcall(graph, 'add', jnew('ArrayList'))
            i = jcast('int', (i + 1))
        for edge in times:
            jcall(jcall(graph, 'get', edge[0]), 'add', jarray('int', [None], [edge[1], edge[2]]))
        distance = jarray('int', [jcast('int', jadd(n, 1))])
        jstatic('Arrays', 'fill', distance, jget(Integer, 'MAX_VALUE'))
        distance[s] = jcast('int', 0)
        visited = jarray('boolean', [jcast('int', jadd(n, 1))])
        # 0 : 当前节点
        # 1 : 源点到当前点距离
        heap = jnew('PriorityQueue', (lambda a, b: (a[1] - b[1])))
        jcall(heap, 'add', jarray('int', [None], [s, 0]))
        while (not jcall(heap, 'isEmpty')):
            try:
                u = jcast('int', jcall(heap, 'poll')[0])
                if visited[u]:
                    raise JContinue(None)
                visited[u] = jcast('boolean', True)
                for edge in jcall(graph, 'get', u):
                    v = jcast('int', edge[0])
                    w = jcast('int', edge[1])
                    if ((not visited[v]) and (jcast('int', jadd(distance[u], w)) < distance[v])):
                        distance[v] = jcast('int', jcast('int', jadd(distance[u], w)))
                        jcall(heap, 'add', jarray('int', [None], [v, jcast('int', jadd(distance[u], w))]))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        i = jcast('int', 1)
        while (i <= n):
            if (distance[i] == jget(Integer, 'MAX_VALUE')):
                return jcast('int', jcast('int', (-1)))
            ans = jcast('int', jstatic('Math', 'max', ans, distance[i]))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 链式前向星+反向索引堆的实现
    @staticmethod
    def networkDelayTime2(times, n, s):
        n = jcast('int', n)
        s = jcast('int', s)
        Code01_DijkstraLeetcode.build(n)
        for edge in times:
            Code01_DijkstraLeetcode.addEdge(edge[0], edge[1], edge[2])
        Code01_DijkstraLeetcode.addOrUpdateOrIgnore(s, 0)
        while (not Code01_DijkstraLeetcode.isEmpty()):
            u = jcast('int', Code01_DijkstraLeetcode.pop())
            ei = jcast('int', Code01_DijkstraLeetcode.head[u])
            while (ei > 0):
                Code01_DijkstraLeetcode.addOrUpdateOrIgnore(Code01_DijkstraLeetcode.to[ei], jcast('int', jadd(Code01_DijkstraLeetcode.distance[u], Code01_DijkstraLeetcode.weight[ei])))
                ei = jcast('int', Code01_DijkstraLeetcode.next[ei])
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        i = jcast('int', 1)
        while (i <= n):
            if (Code01_DijkstraLeetcode.distance[i] == jget(Integer, 'MAX_VALUE')):
                return jcast('int', jcast('int', (-1)))
            ans = jcast('int', jstatic('Math', 'max', ans, Code01_DijkstraLeetcode.distance[i]))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    MAXN = 0
    MAXM = 0
    # 链式前向星
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    # 反向索引堆
    heap = None
    # where[v] = -1，表示v这个节点，从来没有进入过堆
    # where[v] = -2，表示v这个节点，已经弹出过了
    # where[v] = i(>=0)，表示v这个节点，在堆上的i位置
    where = None
    heapSize = 0
    distance = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code01_DijkstraLeetcode.cnt = jcast('int', 1)
        Code01_DijkstraLeetcode.heapSize = jcast('int', 0)
        jstatic('Arrays', 'fill', Code01_DijkstraLeetcode.head, 1, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code01_DijkstraLeetcode.where, 1, jcast('int', jadd(n, 1)), jcast('int', (-1)))
        jstatic('Arrays', 'fill', Code01_DijkstraLeetcode.distance, 1, jcast('int', jadd(n, 1)), jget(Integer, 'MAX_VALUE'))

    # 链式前向星建图
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code01_DijkstraLeetcode.next[Code01_DijkstraLeetcode.cnt] = jcast('int', Code01_DijkstraLeetcode.head[u])
        Code01_DijkstraLeetcode.to[Code01_DijkstraLeetcode.cnt] = jcast('int', v)
        Code01_DijkstraLeetcode.weight[Code01_DijkstraLeetcode.cnt] = jcast('int', w)
        jset(Code01_DijkstraLeetcode.head, u, ((_java_obj_2 := Code01_DijkstraLeetcode), (_java_key_3 := 'cnt'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))), _java_old_4)[4])

    @staticmethod
    def addOrUpdateOrIgnore(v, c):
        v = jcast('int', v)
        c = jcast('int', c)
        if (Code01_DijkstraLeetcode.where[v] == jcast('int', (-1))):
            Code01_DijkstraLeetcode.heap[Code01_DijkstraLeetcode.heapSize] = jcast('int', v)
            jset(Code01_DijkstraLeetcode.where, v, ((_java_obj_5 := Code01_DijkstraLeetcode), (_java_key_6 := 'heapSize'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))), _java_old_7)[4])
            Code01_DijkstraLeetcode.distance[v] = jcast('int', c)
            Code01_DijkstraLeetcode.heapInsert(Code01_DijkstraLeetcode.where[v])
        else:
            if (Code01_DijkstraLeetcode.where[v] >= 0):
                jset(Code01_DijkstraLeetcode.distance, v, jstatic('Math', 'min', Code01_DijkstraLeetcode.distance[v], c))
                Code01_DijkstraLeetcode.heapInsert(Code01_DijkstraLeetcode.where[v])

    @staticmethod
    def heapInsert(i):
        i = jcast('int', i)
        while (Code01_DijkstraLeetcode.distance[Code01_DijkstraLeetcode.heap[i]] < Code01_DijkstraLeetcode.distance[Code01_DijkstraLeetcode.heap[jcast('int', jdiv(jcast('int', (i - 1)), 2))]]):
            Code01_DijkstraLeetcode.swap(i, jcast('int', jdiv(jcast('int', (i - 1)), 2)))
            i = jcast('int', jcast('int', jdiv(jcast('int', (i - 1)), 2)))

    @staticmethod
    def pop():
        ans = jcast('int', Code01_DijkstraLeetcode.heap[0])
        Code01_DijkstraLeetcode.swap(0, ((_java_obj_8 := Code01_DijkstraLeetcode), (_java_key_9 := 'heapSize'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (-1)))))[3])
        Code01_DijkstraLeetcode.heapify(0)
        Code01_DijkstraLeetcode.where[ans] = jcast('int', jcast('int', (-2)))
        return jcast('int', ans)

    @staticmethod
    def heapify(i):
        i = jcast('int', i)
        l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
        while (l < Code01_DijkstraLeetcode.heapSize):
            try:
                best = jcast('int', (jcast('int', jadd(l, 1)) if ((jcast('int', jadd(l, 1)) < Code01_DijkstraLeetcode.heapSize) and (Code01_DijkstraLeetcode.distance[Code01_DijkstraLeetcode.heap[jcast('int', jadd(l, 1))]] < Code01_DijkstraLeetcode.distance[Code01_DijkstraLeetcode.heap[l]])) else l))
                best = jcast('int', (best if (Code01_DijkstraLeetcode.distance[Code01_DijkstraLeetcode.heap[best]] < Code01_DijkstraLeetcode.distance[Code01_DijkstraLeetcode.heap[i]]) else i))
                if (best == i):
                    raise JBreak(None)
                Code01_DijkstraLeetcode.swap(best, i)
                i = jcast('int', best)
                l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
            except JContinue as _java_control_11:
                if _java_control_11.label not in (None,):
                    raise
            except JBreak as _java_control_11:
                if _java_control_11.label not in (None,):
                    raise
                break

    @staticmethod
    def isEmpty():
        return jcast('boolean', (Code01_DijkstraLeetcode.heapSize == 0))

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code01_DijkstraLeetcode.heap[i])
        Code01_DijkstraLeetcode.heap[i] = jcast('int', Code01_DijkstraLeetcode.heap[j])
        Code01_DijkstraLeetcode.heap[j] = jcast('int', tmp)
        jset(Code01_DijkstraLeetcode.where, Code01_DijkstraLeetcode.heap[i], i)
        jset(Code01_DijkstraLeetcode.where, Code01_DijkstraLeetcode.heap[j], j)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_DijkstraLeetcode.MAXN = jcast('int', 101)
Code01_DijkstraLeetcode.MAXM = jcast('int', 6001)
Code01_DijkstraLeetcode.head = jarray('int', [Code01_DijkstraLeetcode.MAXN])
Code01_DijkstraLeetcode.next = jarray('int', [Code01_DijkstraLeetcode.MAXM])
Code01_DijkstraLeetcode.to = jarray('int', [Code01_DijkstraLeetcode.MAXM])
Code01_DijkstraLeetcode.weight = jarray('int', [Code01_DijkstraLeetcode.MAXM])
Code01_DijkstraLeetcode.cnt = jcast('int', 0)
Code01_DijkstraLeetcode.heap = jarray('int', [Code01_DijkstraLeetcode.MAXN])
Code01_DijkstraLeetcode.where = jarray('int', [Code01_DijkstraLeetcode.MAXN])
Code01_DijkstraLeetcode.heapSize = jcast('int', 0)
Code01_DijkstraLeetcode.distance = jarray('int', [Code01_DijkstraLeetcode.MAXN])
