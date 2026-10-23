# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 飞行路线（语言提供的堆）
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
class Code06_FlightPath1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXK': 'MAXK', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'distance': 'distance', 'visited': 'visited', 'heap': 'heap', 'n': 'n', 'm': 'm', 'k': 'k', 's': 's', 't': 't'}
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
    # 用语言自己提供的堆
    # 动态结构，不推荐
    # 0 : 到达的城市编号
    # 1 : 已经使用的免单次数
    # 2 : 沿途的花费
    heap = None
    n = 0
    m = 0
    k = 0
    s = 0
    t = 0
    @staticmethod
    def build():
        Code06_FlightPath1.cnt = jcast('int', 1)
        i = jcast('int', 0)
        while (i < Code06_FlightPath1.n):
            Code06_FlightPath1.head[i] = jcast('int', 0)
            j = jcast('int', 0)
            while (j <= Code06_FlightPath1.k):
                jset(Code06_FlightPath1.distance[i], j, jget(Integer, 'MAX_VALUE'))
                jset(Code06_FlightPath1.visited[i], j, False)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        jcall(Code06_FlightPath1.heap, 'clear')

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code06_FlightPath1.next[Code06_FlightPath1.cnt] = jcast('int', Code06_FlightPath1.head[u])
        Code06_FlightPath1.to[Code06_FlightPath1.cnt] = jcast('int', v)
        Code06_FlightPath1.weight[Code06_FlightPath1.cnt] = jcast('int', w)
        jset(Code06_FlightPath1.head, u, ((_java_obj_1 := Code06_FlightPath1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code06_FlightPath1.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code06_FlightPath1.m = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code06_FlightPath1.k = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code06_FlightPath1.s = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code06_FlightPath1.t = jcast('int', jcast('int', jget(in_, 'nval')))
            Code06_FlightPath1.build()
            i = jcast('int', 0)
            a = 0
            b = 0
            c = 0
            while (i < Code06_FlightPath1.m):
                jcall(in_, 'nextToken')
                a = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                b = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                c = jcast('int', jcast('int', jget(in_, 'nval')))
                Code06_FlightPath1.addEdge(a, b, c)
                Code06_FlightPath1.addEdge(b, a, c)
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code06_FlightPath1.dijkstra())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def dijkstra():
        jset(Code06_FlightPath1.distance[Code06_FlightPath1.s], 0, 0)
        jcall(Code06_FlightPath1.heap, 'add', jarray('int', [None], [Code06_FlightPath1.s, 0, 0]))
        while (not jcall(Code06_FlightPath1.heap, 'isEmpty')):
            try:
                record = jcall(Code06_FlightPath1.heap, 'poll')
                u = jcast('int', record[0])
                use = jcast('int', record[1])
                cost = jcast('int', record[2])
                if Code06_FlightPath1.visited[u][use]:
                    raise JContinue(None)
                jset(Code06_FlightPath1.visited[u], use, True)
                if (u == Code06_FlightPath1.t):
                    # 常见剪枝
                    # 发现终点直接返回
                    # 不用等都结束
                    return jcast('int', cost)
                ei = jcast('int', Code06_FlightPath1.head[u])
                v = 0
                w = 0
                while (ei > 0):
                    v = jcast('int', Code06_FlightPath1.to[ei])
                    w = jcast('int', Code06_FlightPath1.weight[ei])
                    if ((use < Code06_FlightPath1.k) and (Code06_FlightPath1.distance[v][jcast('int', jadd(use, 1))] > Code06_FlightPath1.distance[u][use])):
                        # 使用免费
                        jset(Code06_FlightPath1.distance[v], jcast('int', jadd(use, 1)), Code06_FlightPath1.distance[u][use])
                        jcall(Code06_FlightPath1.heap, 'add', jarray('int', [None], [v, jcast('int', jadd(use, 1)), Code06_FlightPath1.distance[v][jcast('int', jadd(use, 1))]]))
                    if (Code06_FlightPath1.distance[v][use] > jcast('int', jadd(Code06_FlightPath1.distance[u][use], w))):
                        # 不用免费
                        jset(Code06_FlightPath1.distance[v], use, jcast('int', jadd(Code06_FlightPath1.distance[u][use], w)))
                        jcall(Code06_FlightPath1.heap, 'add', jarray('int', [None], [v, use, Code06_FlightPath1.distance[v][use]]))
                    ei = jcast('int', Code06_FlightPath1.next[ei])
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
        return jcast('int', jcast('int', (-1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_FlightPath1.MAXN = jcast('int', 10001)
Code06_FlightPath1.MAXM = jcast('int', 100001)
Code06_FlightPath1.MAXK = jcast('int', 11)
Code06_FlightPath1.head = jarray('int', [Code06_FlightPath1.MAXN])
Code06_FlightPath1.next = jarray('int', [Code06_FlightPath1.MAXM])
Code06_FlightPath1.to = jarray('int', [Code06_FlightPath1.MAXM])
Code06_FlightPath1.weight = jarray('int', [Code06_FlightPath1.MAXM])
Code06_FlightPath1.cnt = jcast('int', 0)
Code06_FlightPath1.distance = jarray('int', [Code06_FlightPath1.MAXN, Code06_FlightPath1.MAXK])
Code06_FlightPath1.visited = jarray('boolean', [Code06_FlightPath1.MAXN, Code06_FlightPath1.MAXK])
Code06_FlightPath1.heap = jnew('PriorityQueue', (lambda a, b: (a[2] - b[2])))
Code06_FlightPath1.n = jcast('int', 0)
Code06_FlightPath1.m = jcast('int', 0)
Code06_FlightPath1.k = jcast('int', 0)
Code06_FlightPath1.s = jcast('int', 0)
Code06_FlightPath1.t = jcast('int', 0)

if __name__ == '__main__':
    Code06_FlightPath1.main([])
