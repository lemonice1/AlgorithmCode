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

# 飞行路线（自己手撸的堆）
# Alice和Bob现在要乘飞机旅行，他们选择了一家相对便宜的航空公司
# 该航空公司一共在n个城市设有业务，设这些城市分别标记为0 ~ n−1
# 一共有m种航线，每种航线连接两个城市，并且航线有一定的价格
# Alice 和 Bob 现在要从一个城市沿着航线到达另一个城市，途中可以进行转机
# 航空公司对他们这次旅行也推出优惠，他们可以免费在最多k种航线上搭乘飞机
# 那么 Alice 和 Bob 这次出行最少花费多少
# 测试链接 : https://www.luogu.com.cn/problem/P4568
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_FlightPath2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXK': 'MAXK', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'distance': 'distance', 'visited': 'visited', 'heap': 'heap', 'heapSize': 'heapSize', 'n': 'n', 'm': 'm', 'k': 'k', 's': 's', 't': 't', 'u': 'u', 'use': 'use', 'cost': 'cost'}
    MAXN = 0
    MAXM = 0
    MAXK = 0
    # 链式前向星建图需要
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    # Dijkstra需要
    distance = None
    visited = None
    # 自己写的普通堆，静态结构，推荐
    # 注意是自己写的普通堆，不是反向索引堆
    # 因为(点编号，使用免费路线的次数)，两个参数的组合才是图中的点
    # 两个参数的组合对应一个点(一个堆的下标)，所以反向索引堆不好写
    # 其实也能实现，二维点变成一维下标即可
    # 但是会造成很多困惑，索性算了，就手写普通堆吧
    heap = None
    heapSize = 0
    n = 0
    m = 0
    k = 0
    s = 0
    t = 0
    @staticmethod
    def build():
        Code06_FlightPath2.cnt = jcast('int', 1)
        Code06_FlightPath2.heapSize = jcast('int', 0)
        i = jcast('int', 0)
        while (i < Code06_FlightPath2.n):
            Code06_FlightPath2.head[i] = jcast('int', 0)
            j = jcast('int', 0)
            while (j <= Code06_FlightPath2.k):
                jset(Code06_FlightPath2.distance[i], j, jget(Integer, 'MAX_VALUE'))
                jset(Code06_FlightPath2.visited[i], j, False)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code06_FlightPath2.next[Code06_FlightPath2.cnt] = jcast('int', Code06_FlightPath2.head[u])
        Code06_FlightPath2.to[Code06_FlightPath2.cnt] = jcast('int', v)
        Code06_FlightPath2.weight[Code06_FlightPath2.cnt] = jcast('int', w)
        jset(Code06_FlightPath2.head, u, ((_java_obj_1 := Code06_FlightPath2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def push(u, t, c):
        u = jcast('int', u)
        t = jcast('int', t)
        c = jcast('int', c)
        jset(Code06_FlightPath2.heap[Code06_FlightPath2.heapSize], 0, u)
        jset(Code06_FlightPath2.heap[Code06_FlightPath2.heapSize], 1, t)
        jset(Code06_FlightPath2.heap[Code06_FlightPath2.heapSize], 2, c)
        i = jcast('int', ((_java_obj_4 := Code06_FlightPath2), (_java_key_5 := 'heapSize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4])
        while (Code06_FlightPath2.heap[i][2] < Code06_FlightPath2.heap[jcast('int', jdiv(jcast('int', (i - 1)), 2))][2]):
            Code06_FlightPath2.swap(i, jcast('int', jdiv(jcast('int', (i - 1)), 2)))
            i = jcast('int', jcast('int', jdiv(jcast('int', (i - 1)), 2)))

    u = 0
    use = 0
    cost = 0
    @staticmethod
    def pop():
        Code06_FlightPath2.u = jcast('int', Code06_FlightPath2.heap[0][0])
        Code06_FlightPath2.use = jcast('int', Code06_FlightPath2.heap[0][1])
        Code06_FlightPath2.cost = jcast('int', Code06_FlightPath2.heap[0][2])
        Code06_FlightPath2.swap(0, ((_java_obj_7 := Code06_FlightPath2), (_java_key_8 := 'heapSize'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))))[3])
        Code06_FlightPath2.heapify(0)

    @staticmethod
    def heapify(i):
        i = jcast('int', i)
        l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
        while (l < Code06_FlightPath2.heapSize):
            try:
                best = jcast('int', (jcast('int', jadd(l, 1)) if ((jcast('int', jadd(l, 1)) < Code06_FlightPath2.heapSize) and (Code06_FlightPath2.heap[jcast('int', jadd(l, 1))][2] < Code06_FlightPath2.heap[l][2])) else l))
                best = jcast('int', (best if (Code06_FlightPath2.heap[best][2] < Code06_FlightPath2.heap[i][2]) else i))
                if (best == i):
                    raise JBreak(None)
                Code06_FlightPath2.swap(best, i)
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
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = Code06_FlightPath2.heap[i]
        Code06_FlightPath2.heap[i] = Code06_FlightPath2.heap[j]
        Code06_FlightPath2.heap[j] = tmp

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code06_FlightPath2.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code06_FlightPath2.m = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code06_FlightPath2.k = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code06_FlightPath2.s = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code06_FlightPath2.t = jcast('int', jcast('int', jget(in_, 'nval')))
            Code06_FlightPath2.build()
            i = jcast('int', 0)
            a = 0
            b = 0
            c = 0
            while (i < Code06_FlightPath2.m):
                jcall(in_, 'nextToken')
                a = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                b = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                c = jcast('int', jcast('int', jget(in_, 'nval')))
                Code06_FlightPath2.addEdge(a, b, c)
                Code06_FlightPath2.addEdge(b, a, c)
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code06_FlightPath2.dijkstra())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def dijkstra():
        jset(Code06_FlightPath2.distance[Code06_FlightPath2.s], 0, 0)
        Code06_FlightPath2.push(Code06_FlightPath2.s, 0, 0)
        while (Code06_FlightPath2.heapSize > 0):
            try:
                Code06_FlightPath2.pop()
                if Code06_FlightPath2.visited[Code06_FlightPath2.u][Code06_FlightPath2.use]:
                    raise JContinue(None)
                jset(Code06_FlightPath2.visited[Code06_FlightPath2.u], Code06_FlightPath2.use, True)
                if (Code06_FlightPath2.u == Code06_FlightPath2.t):
                    # 常见剪枝
                    # 发现终点直接返回
                    # 不用等都结束
                    return jcast('int', Code06_FlightPath2.cost)
                ei = jcast('int', Code06_FlightPath2.head[Code06_FlightPath2.u])
                v = 0
                w = 0
                while (ei > 0):
                    v = jcast('int', Code06_FlightPath2.to[ei])
                    w = jcast('int', Code06_FlightPath2.weight[ei])
                    if ((Code06_FlightPath2.use < Code06_FlightPath2.k) and (Code06_FlightPath2.distance[v][jcast('int', jadd(Code06_FlightPath2.use, 1))] > Code06_FlightPath2.distance[Code06_FlightPath2.u][Code06_FlightPath2.use])):
                        # 使用免费
                        jset(Code06_FlightPath2.distance[v], jcast('int', jadd(Code06_FlightPath2.use, 1)), Code06_FlightPath2.distance[Code06_FlightPath2.u][Code06_FlightPath2.use])
                        Code06_FlightPath2.push(v, jcast('int', jadd(Code06_FlightPath2.use, 1)), Code06_FlightPath2.distance[v][jcast('int', jadd(Code06_FlightPath2.use, 1))])
                    if (Code06_FlightPath2.distance[v][Code06_FlightPath2.use] > jcast('int', jadd(Code06_FlightPath2.distance[Code06_FlightPath2.u][Code06_FlightPath2.use], w))):
                        # 不用免费
                        jset(Code06_FlightPath2.distance[v], Code06_FlightPath2.use, jcast('int', jadd(Code06_FlightPath2.distance[Code06_FlightPath2.u][Code06_FlightPath2.use], w)))
                        Code06_FlightPath2.push(v, Code06_FlightPath2.use, Code06_FlightPath2.distance[v][Code06_FlightPath2.use])
                    ei = jcast('int', Code06_FlightPath2.next[ei])
            except JContinue as _java_control_11:
                if _java_control_11.label not in (None,):
                    raise
            except JBreak as _java_control_11:
                if _java_control_11.label not in (None,):
                    raise
                break
        return jcast('int', jcast('int', (-1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_FlightPath2.MAXN = jcast('int', 10001)
Code06_FlightPath2.MAXM = jcast('int', 100001)
Code06_FlightPath2.MAXK = jcast('int', 11)
Code06_FlightPath2.head = jarray('int', [Code06_FlightPath2.MAXN])
Code06_FlightPath2.next = jarray('int', [Code06_FlightPath2.MAXM])
Code06_FlightPath2.to = jarray('int', [Code06_FlightPath2.MAXM])
Code06_FlightPath2.weight = jarray('int', [Code06_FlightPath2.MAXM])
Code06_FlightPath2.cnt = jcast('int', 0)
Code06_FlightPath2.distance = jarray('int', [Code06_FlightPath2.MAXN, Code06_FlightPath2.MAXK])
Code06_FlightPath2.visited = jarray('boolean', [Code06_FlightPath2.MAXN, Code06_FlightPath2.MAXK])
Code06_FlightPath2.heap = jarray('int', [jcast('int', (Code06_FlightPath2.MAXM * Code06_FlightPath2.MAXK)), 3])
Code06_FlightPath2.heapSize = jcast('int', 0)
Code06_FlightPath2.n = jcast('int', 0)
Code06_FlightPath2.m = jcast('int', 0)
Code06_FlightPath2.k = jcast('int', 0)
Code06_FlightPath2.s = jcast('int', 0)
Code06_FlightPath2.t = jcast('int', 0)
Code06_FlightPath2.u = jcast('int', 0)
Code06_FlightPath2.use = jcast('int', 0)
Code06_FlightPath2.cost = jcast('int', 0)

if __name__ == '__main__':
    Code06_FlightPath2.main([])
