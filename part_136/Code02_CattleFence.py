# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 牛场围栏
# 给定一个长度为n的数组arr, arr[i]代表第i种木棍的长度，每种木棍有无穷多个
# 给定一个正数m，表示你可以把任何一根木棍消去最多m的长度，同一种木棍可以消去不同的长度
# 你可以随意拼接木棍形成一个长度，返回不能拼出来的长度中，最大值是多少
# 如果你可以拼出所有的长度，返回-1
# 如果不能拼出来的长度有无穷多，返回-1
# 1 <= n <= 100
# 1 <= arr[i] <= 3000
# 1 <= m <= 3000
# 测试链接 : https://www.luogu.com.cn/problem/P2662
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_CattleFence:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'MAXM': 'MAXM', 'inf': 'inf', 'n': 'n', 'm': 'm', 'x': 'x', 'arr': 'arr', 'set': 'set', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'heap': 'heap', 'distance': 'distance', 'visited': 'visited'}
    MAXN = 0
    MAXV = 0
    MAXM = 0
    inf = 0
    n = 0
    m = 0
    x = 0
    arr = None
    set = None
    # 链式前向星需要
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    # dijkstra算法需要
    # 0 : 当前节点
    # 1 : 源点到当前点距离
    heap = None
    distance = None
    visited = None
    @staticmethod
    def prepare():
        Code02_CattleFence.cnt = jcast('int', 1)
        jcall(Code02_CattleFence.heap, 'clear')
        jstatic('Arrays', 'fill', Code02_CattleFence.set, False)
        jstatic('Arrays', 'fill', Code02_CattleFence.head, 0, Code02_CattleFence.x, 0)
        jstatic('Arrays', 'fill', Code02_CattleFence.distance, 0, Code02_CattleFence.x, Code02_CattleFence.inf)
        jstatic('Arrays', 'fill', Code02_CattleFence.visited, 0, Code02_CattleFence.x, False)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code02_CattleFence.next[Code02_CattleFence.cnt] = jcast('int', Code02_CattleFence.head[u])
        Code02_CattleFence.to[Code02_CattleFence.cnt] = jcast('int', v)
        Code02_CattleFence.weight[Code02_CattleFence.cnt] = jcast('int', w)
        jset(Code02_CattleFence.head, u, ((_java_obj_1 := Code02_CattleFence), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # 来自讲解064，dijkstra算法
    @staticmethod
    def dijkstra():
        jcall(Code02_CattleFence.heap, 'add', jarray('int', [None], [0, 0]))
        Code02_CattleFence.distance[0] = jcast('int', 0)
        cur = None
        u = 0
        w = 0
        while (not jcall(Code02_CattleFence.heap, 'isEmpty')):
            try:
                cur = jcall(Code02_CattleFence.heap, 'poll')
                u = jcast('int', jcast('int', cur[0]))
                w = jcast('int', cur[1])
                if Code02_CattleFence.visited[u]:
                    raise JContinue(None)
                Code02_CattleFence.visited[u] = jcast('boolean', True)
                ei = jcast('int', Code02_CattleFence.head[u])
                v = 0
                while (ei > 0):
                    v = jcast('int', Code02_CattleFence.to[ei])
                    if ((not Code02_CattleFence.visited[v]) and (Code02_CattleFence.distance[v] > jcast('int', jadd(w, Code02_CattleFence.weight[ei])))):
                        Code02_CattleFence.distance[v] = jcast('int', jcast('int', jadd(w, Code02_CattleFence.weight[ei])))
                        jcall(Code02_CattleFence.heap, 'add', jarray('int', [None], [v, Code02_CattleFence.distance[v]]))
                    ei = jcast('int', Code02_CattleFence.next[ei])
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break

    @staticmethod
    def compute():
        ans = jcast('int', 0)
        if (Code02_CattleFence.x == 1):
            ans = jcast('int', jcast('int', (-1)))
        else:
            i = jcast('int', 1)
            while (i <= Code02_CattleFence.n):
                j = jcast('int', jstatic('Math', 'max', 1, jcast('int', (Code02_CattleFence.arr[i] - Code02_CattleFence.m))))
                while (j <= Code02_CattleFence.arr[i]):
                    if (not Code02_CattleFence.set[j]):
                        Code02_CattleFence.set[j] = jcast('boolean', True)
                        k = jcast('int', 0)
                        while (k < Code02_CattleFence.x):
                            Code02_CattleFence.addEdge(k, jcast('int', jmod(jcast('int', jadd(k, j)), Code02_CattleFence.x)), j)
                            k = jcast('int', (k + 1))
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))
            Code02_CattleFence.dijkstra()
            i = jcast('int', 1)
            while (i < Code02_CattleFence.x):
                try:
                    if (Code02_CattleFence.distance[i] == Code02_CattleFence.inf):
                        ans = jcast('int', jcast('int', (-1)))
                        raise JBreak(None)
                    ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', (Code02_CattleFence.distance[i] - Code02_CattleFence.x))))
                except JContinue as _java_control_5:
                    if _java_control_5.label not in (None,):
                        raise
                except JBreak as _java_control_5:
                    if _java_control_5.label not in (None,):
                        raise
                    break
                i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_CattleFence.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_CattleFence.m = jcast('int', jcast('int', jget(in_, 'nval')))
        Code02_CattleFence.x = jcast('int', Code02_CattleFence.inf)
        i = jcast('int', 1)
        while (i <= Code02_CattleFence.n):
            jcall(in_, 'nextToken')
            Code02_CattleFence.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_CattleFence.x = jcast('int', jstatic('Math', 'min', Code02_CattleFence.x, jstatic('Math', 'max', 1, jcast('int', (Code02_CattleFence.arr[i] - Code02_CattleFence.m)))))
            i = jcast('int', (i + 1))
        Code02_CattleFence.prepare()
        jcall(out, 'println', Code02_CattleFence.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_CattleFence.MAXN = jcast('int', 101)
Code02_CattleFence.MAXV = jcast('int', 3001)
Code02_CattleFence.MAXM = jcast('int', 30001)
Code02_CattleFence.inf = jcast('int', jget(Integer, 'MAX_VALUE'))
Code02_CattleFence.n = jcast('int', 0)
Code02_CattleFence.m = jcast('int', 0)
Code02_CattleFence.x = jcast('int', 0)
Code02_CattleFence.arr = jarray('int', [Code02_CattleFence.MAXN])
Code02_CattleFence.set = jarray('boolean', [Code02_CattleFence.MAXV])
Code02_CattleFence.head = jarray('int', [Code02_CattleFence.MAXV])
Code02_CattleFence.next = jarray('int', [Code02_CattleFence.MAXM])
Code02_CattleFence.to = jarray('int', [Code02_CattleFence.MAXM])
Code02_CattleFence.weight = jarray('int', [Code02_CattleFence.MAXM])
Code02_CattleFence.cnt = jcast('int', 0)
Code02_CattleFence.heap = jnew('PriorityQueue', (lambda a, b: (a[1] - b[1])))
Code02_CattleFence.distance = jarray('int', [Code02_CattleFence.MAXV])
Code02_CattleFence.visited = jarray('boolean', [Code02_CattleFence.MAXV])

if __name__ == '__main__':
    Code02_CattleFence.main([])
