# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# Bellman-Ford + SPFA优化模版（洛谷）
# 给定n个点的有向图，请求出图中是否存在从顶点1出发能到达的负环
# 负环的定义是：一条边权之和为负数的回路
# 测试链接 : https://www.luogu.com.cn/problem/P3385
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_SPFA:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'MAXQ': 'MAXQ', 'distance': 'distance', 'updateCnt': 'updateCnt', 'queue': 'queue', 'l': 'l', 'r': 'r', 'enter': 'enter'}
    MAXN = 0
    MAXM = 0
    # 链式前向星建图需要
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    # SPFA需要
    MAXQ = 0
    # 源点出发到每个节点的距离表
    distance = None
    # 节点被松弛的次数
    updateCnt = None
    # 哪些节点被松弛了放入队列
    queue = None
    l = 0
    r = 0
    # 节点是否已经在队列中
    enter = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code04_SPFA.cnt = jcast('int', 1)
        Code04_SPFA.l = jcast('int', jset(Code04_SPFA, 'r', 0))
        jstatic('Arrays', 'fill', Code04_SPFA.head, 1, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code04_SPFA.enter, 1, jcast('int', jadd(n, 1)), False)
        jstatic('Arrays', 'fill', Code04_SPFA.distance, 1, jcast('int', jadd(n, 1)), jget(Integer, 'MAX_VALUE'))
        jstatic('Arrays', 'fill', Code04_SPFA.updateCnt, 1, jcast('int', jadd(n, 1)), 0)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code04_SPFA.next[Code04_SPFA.cnt] = jcast('int', Code04_SPFA.head[u])
        Code04_SPFA.to[Code04_SPFA.cnt] = jcast('int', v)
        Code04_SPFA.weight[Code04_SPFA.cnt] = jcast('int', w)
        jset(Code04_SPFA.head, u, ((_java_obj_1 := Code04_SPFA), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        cases = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 0)
        n = 0
        m = 0
        while (i < cases):
            jcall(in_, 'nextToken')
            n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code04_SPFA.build(n)
            j = jcast('int', 0)
            u = 0
            v = 0
            w = 0
            while (j < m):
                jcall(in_, 'nextToken')
                u = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                w = jcast('int', jcast('int', jget(in_, 'nval')))
                if (w >= 0):
                    Code04_SPFA.addEdge(u, v, w)
                    Code04_SPFA.addEdge(v, u, w)
                else:
                    Code04_SPFA.addEdge(u, v, w)
                j = jcast('int', (j + 1))
            jcall(out, 'println', ('YES' if Code04_SPFA.spfa(n) else 'NO'))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # Bellman-Ford + SPFA优化的模版
    @staticmethod
    def spfa(n):
        n = jcast('int', n)
        Code04_SPFA.distance[1] = jcast('int', 0)
        Code04_SPFA.updateCnt[1] = jcast('int', (Code04_SPFA.updateCnt[1] + 1))
        jset(Code04_SPFA.queue, ((_java_obj_4 := Code04_SPFA), (_java_key_5 := 'r'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], 1)
        Code04_SPFA.enter[1] = jcast('boolean', True)
        while (Code04_SPFA.l < Code04_SPFA.r):
            u = jcast('int', Code04_SPFA.queue[((_java_obj_7 := Code04_SPFA), (_java_key_8 := 'l'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])
            Code04_SPFA.enter[u] = jcast('boolean', False)
            ei = jcast('int', Code04_SPFA.head[u])
            v = 0
            w = 0
            while (ei > 0):
                v = jcast('int', Code04_SPFA.to[ei])
                w = jcast('int', Code04_SPFA.weight[ei])
                if (jcast('int', jadd(Code04_SPFA.distance[u], w)) < Code04_SPFA.distance[v]):
                    Code04_SPFA.distance[v] = jcast('int', jcast('int', jadd(Code04_SPFA.distance[u], w)))
                    if (not Code04_SPFA.enter[v]):
                        # 松弛次数超过n-1就有负环
                        if (((_java_obj_10 := Code04_SPFA.updateCnt), (_java_key_11 := v), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3] > jcast('int', (n - 1))):
                            return jcast('boolean', True)
                        jset(Code04_SPFA.queue, ((_java_obj_13 := Code04_SPFA), (_java_key_14 := 'r'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))), _java_old_15)[4], v)
                        Code04_SPFA.enter[v] = jcast('boolean', True)
                ei = jcast('int', Code04_SPFA.next[ei])
        return jcast('boolean', False)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_SPFA.MAXN = jcast('int', 2001)
Code04_SPFA.MAXM = jcast('int', 6001)
Code04_SPFA.head = jarray('int', [Code04_SPFA.MAXN])
Code04_SPFA.next = jarray('int', [Code04_SPFA.MAXM])
Code04_SPFA.to = jarray('int', [Code04_SPFA.MAXM])
Code04_SPFA.weight = jarray('int', [Code04_SPFA.MAXM])
Code04_SPFA.cnt = jcast('int', 0)
Code04_SPFA.MAXQ = jcast('int', 4000001)
Code04_SPFA.distance = jarray('int', [Code04_SPFA.MAXN])
Code04_SPFA.updateCnt = jarray('int', [Code04_SPFA.MAXN])
Code04_SPFA.queue = jarray('int', [Code04_SPFA.MAXQ])
Code04_SPFA.l = jcast('int', 0)
Code04_SPFA.r = jcast('int', 0)
Code04_SPFA.enter = jarray('boolean', [Code04_SPFA.MAXN])

if __name__ == '__main__':
    Code04_SPFA.main([])
