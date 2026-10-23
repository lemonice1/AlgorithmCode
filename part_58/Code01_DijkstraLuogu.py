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

# Dijkstra算法模版（洛谷）
# 静态空间实现 : 链式前向星 + 反向索引堆
# 测试链接 : https://www.luogu.com.cn/problem/P4779
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_DijkstraLuogu:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'heap': 'heap', 'where': 'where', 'heapSize': 'heapSize', 'distance': 'distance', 'n': 'n', 'm': 'm', 's': 's'}
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
    n = 0
    m = 0
    s = 0
    @staticmethod
    def build():
        Code01_DijkstraLuogu.cnt = jcast('int', 1)
        Code01_DijkstraLuogu.heapSize = jcast('int', 0)
        jstatic('Arrays', 'fill', Code01_DijkstraLuogu.head, 1, jcast('int', jadd(Code01_DijkstraLuogu.n, 1)), 0)
        jstatic('Arrays', 'fill', Code01_DijkstraLuogu.where, 1, jcast('int', jadd(Code01_DijkstraLuogu.n, 1)), jcast('int', (-1)))
        jstatic('Arrays', 'fill', Code01_DijkstraLuogu.distance, 1, jcast('int', jadd(Code01_DijkstraLuogu.n, 1)), jget(Integer, 'MAX_VALUE'))

    # 链式前向星建图
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code01_DijkstraLuogu.next[Code01_DijkstraLuogu.cnt] = jcast('int', Code01_DijkstraLuogu.head[u])
        Code01_DijkstraLuogu.to[Code01_DijkstraLuogu.cnt] = jcast('int', v)
        Code01_DijkstraLuogu.weight[Code01_DijkstraLuogu.cnt] = jcast('int', w)
        jset(Code01_DijkstraLuogu.head, u, ((_java_obj_1 := Code01_DijkstraLuogu), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def addOrUpdateOrIgnore(v, w):
        v = jcast('int', v)
        w = jcast('int', w)
        if (Code01_DijkstraLuogu.where[v] == jcast('int', (-1))):
            Code01_DijkstraLuogu.heap[Code01_DijkstraLuogu.heapSize] = jcast('int', v)
            jset(Code01_DijkstraLuogu.where, v, ((_java_obj_4 := Code01_DijkstraLuogu), (_java_key_5 := 'heapSize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4])
            Code01_DijkstraLuogu.distance[v] = jcast('int', w)
            Code01_DijkstraLuogu.heapInsert(Code01_DijkstraLuogu.where[v])
        else:
            if (Code01_DijkstraLuogu.where[v] >= 0):
                jset(Code01_DijkstraLuogu.distance, v, jstatic('Math', 'min', Code01_DijkstraLuogu.distance[v], w))
                Code01_DijkstraLuogu.heapInsert(Code01_DijkstraLuogu.where[v])

    @staticmethod
    def heapInsert(i):
        i = jcast('int', i)
        while (Code01_DijkstraLuogu.distance[Code01_DijkstraLuogu.heap[i]] < Code01_DijkstraLuogu.distance[Code01_DijkstraLuogu.heap[jcast('int', jdiv(jcast('int', (i - 1)), 2))]]):
            Code01_DijkstraLuogu.swap(i, jcast('int', jdiv(jcast('int', (i - 1)), 2)))
            i = jcast('int', jcast('int', jdiv(jcast('int', (i - 1)), 2)))

    @staticmethod
    def pop():
        ans = jcast('int', Code01_DijkstraLuogu.heap[0])
        Code01_DijkstraLuogu.swap(0, ((_java_obj_7 := Code01_DijkstraLuogu), (_java_key_8 := 'heapSize'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))))[3])
        Code01_DijkstraLuogu.heapify(0)
        Code01_DijkstraLuogu.where[ans] = jcast('int', jcast('int', (-2)))
        return jcast('int', ans)

    @staticmethod
    def heapify(i):
        i = jcast('int', i)
        l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
        while (l < Code01_DijkstraLuogu.heapSize):
            try:
                best = jcast('int', (jcast('int', jadd(l, 1)) if ((jcast('int', jadd(l, 1)) < Code01_DijkstraLuogu.heapSize) and (Code01_DijkstraLuogu.distance[Code01_DijkstraLuogu.heap[jcast('int', jadd(l, 1))]] < Code01_DijkstraLuogu.distance[Code01_DijkstraLuogu.heap[l]])) else l))
                best = jcast('int', (best if (Code01_DijkstraLuogu.distance[Code01_DijkstraLuogu.heap[best]] < Code01_DijkstraLuogu.distance[Code01_DijkstraLuogu.heap[i]]) else i))
                if (best == i):
                    raise JBreak(None)
                Code01_DijkstraLuogu.swap(best, i)
                i = jcast('int', best)
                l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break

    @staticmethod
    def isEmpty():
        return jcast('boolean', (Code01_DijkstraLuogu.heapSize == 0))

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code01_DijkstraLuogu.heap[i])
        Code01_DijkstraLuogu.heap[i] = jcast('int', Code01_DijkstraLuogu.heap[j])
        Code01_DijkstraLuogu.heap[j] = jcast('int', tmp)
        jset(Code01_DijkstraLuogu.where, Code01_DijkstraLuogu.heap[i], i)
        jset(Code01_DijkstraLuogu.where, Code01_DijkstraLuogu.heap[j], j)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code01_DijkstraLuogu.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code01_DijkstraLuogu.m = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code01_DijkstraLuogu.s = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_DijkstraLuogu.build()
            i = jcast('int', 0)
            u = 0
            v = 0
            w = 0
            while (i < Code01_DijkstraLuogu.m):
                jcall(in_, 'nextToken')
                u = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                w = jcast('int', jcast('int', jget(in_, 'nval')))
                Code01_DijkstraLuogu.addEdge(u, v, w)
                i = jcast('int', (i + 1))
            Code01_DijkstraLuogu.dijkstra()
            jcall(out, 'print', Code01_DijkstraLuogu.distance[1])
            i = jcast('int', 2)
            while (i <= Code01_DijkstraLuogu.n):
                jcall(out, 'print', jadd(' ', Code01_DijkstraLuogu.distance[i]))
                i = jcast('int', (i + 1))
            jcall(out, 'println')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def dijkstra():
        Code01_DijkstraLuogu.addOrUpdateOrIgnore(Code01_DijkstraLuogu.s, 0)
        while (not Code01_DijkstraLuogu.isEmpty()):
            v = jcast('int', Code01_DijkstraLuogu.pop())
            ei = jcast('int', Code01_DijkstraLuogu.head[v])
            while (ei > 0):
                Code01_DijkstraLuogu.addOrUpdateOrIgnore(Code01_DijkstraLuogu.to[ei], jcast('int', jadd(Code01_DijkstraLuogu.distance[v], Code01_DijkstraLuogu.weight[ei])))
                ei = jcast('int', Code01_DijkstraLuogu.next[ei])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_DijkstraLuogu.MAXN = jcast('int', 100001)
Code01_DijkstraLuogu.MAXM = jcast('int', 200001)
Code01_DijkstraLuogu.head = jarray('int', [Code01_DijkstraLuogu.MAXN])
Code01_DijkstraLuogu.next = jarray('int', [Code01_DijkstraLuogu.MAXM])
Code01_DijkstraLuogu.to = jarray('int', [Code01_DijkstraLuogu.MAXM])
Code01_DijkstraLuogu.weight = jarray('int', [Code01_DijkstraLuogu.MAXM])
Code01_DijkstraLuogu.cnt = jcast('int', 0)
Code01_DijkstraLuogu.heap = jarray('int', [Code01_DijkstraLuogu.MAXN])
Code01_DijkstraLuogu.where = jarray('int', [Code01_DijkstraLuogu.MAXN])
Code01_DijkstraLuogu.heapSize = jcast('int', 0)
Code01_DijkstraLuogu.distance = jarray('int', [Code01_DijkstraLuogu.MAXN])
Code01_DijkstraLuogu.n = jcast('int', 0)
Code01_DijkstraLuogu.m = jcast('int', 0)
Code01_DijkstraLuogu.s = jcast('int', 0)

if __name__ == '__main__':
    Code01_DijkstraLuogu.main([])
