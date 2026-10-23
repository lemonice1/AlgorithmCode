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

# 消防(递归版)
# 一共n个节点，编号1~n，有n-1条边连接成一棵树，每条边上有非负权值
# 给定一个非负整数s，表示可以在树上选择一条长度不超过s的路径
# 然后在这条路径的点上建立消防站，每个居民可以去往这条路径上的任何消防站
# 目标：哪怕最远的居民走到消防站的距离也要尽量少
# 返回最远居民走到消防站的最短距离
# 测试链接 : https://www.luogu.com.cn/problem/P2491
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
# 对应实现可参考 Code05_FireFighting2.py
class Code05_FireFighting1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 's': 's', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'start': 'start', 'end': 'end', 'diameter': 'diameter', 'dist': 'dist', 'last': 'last', 'pred': 'pred', 'diameterPath': 'diameterPath', 'maxDist': 'maxDist', 'queue': 'queue'}
    MAXN = 0
    n = 0
    s = 0
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    start = 0
    end = 0
    diameter = 0
    dist = None
    last = None
    # pred[i] : i节点在直径上，和前一个点之间的距离，以start做根
    pred = None
    diameterPath = None
    maxDist = None
    @staticmethod
    def build():
        Code05_FireFighting1.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code05_FireFighting1.head, 1, jcast('int', jadd(Code05_FireFighting1.n, 1)), 0)
        jstatic('Arrays', 'fill', Code05_FireFighting1.diameterPath, 1, Code05_FireFighting1.n, False)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code05_FireFighting1.next[Code05_FireFighting1.cnt] = jcast('int', Code05_FireFighting1.head[u])
        Code05_FireFighting1.to[Code05_FireFighting1.cnt] = jcast('int', v)
        Code05_FireFighting1.weight[Code05_FireFighting1.cnt] = jcast('int', w)
        jset(Code05_FireFighting1.head, u, ((_java_obj_1 := Code05_FireFighting1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def road():
        Code05_FireFighting1.dfs(1, 0, 0)
        Code05_FireFighting1.start = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code05_FireFighting1.n):
            if (Code05_FireFighting1.dist[i] > Code05_FireFighting1.dist[Code05_FireFighting1.start]):
                Code05_FireFighting1.start = jcast('int', i)
            i = jcast('int', (i + 1))
        Code05_FireFighting1.dfs(Code05_FireFighting1.start, 0, 0)
        Code05_FireFighting1.end = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code05_FireFighting1.n):
            if (Code05_FireFighting1.dist[i] > Code05_FireFighting1.dist[Code05_FireFighting1.end]):
                Code05_FireFighting1.end = jcast('int', i)
            i = jcast('int', (i + 1))
        Code05_FireFighting1.diameter = jcast('int', Code05_FireFighting1.dist[Code05_FireFighting1.end])

    @staticmethod
    def dfs(u, f, w):
        u = jcast('int', u)
        f = jcast('int', f)
        w = jcast('int', w)
        Code05_FireFighting1.last[u] = jcast('int', f)
        Code05_FireFighting1.dist[u] = jcast('int', jcast('int', jadd(Code05_FireFighting1.dist[f], w)))
        Code05_FireFighting1.pred[u] = jcast('int', w)
        e = jcast('int', Code05_FireFighting1.head[u])
        while (e != 0):
            if (Code05_FireFighting1.to[e] != f):
                Code05_FireFighting1.dfs(Code05_FireFighting1.to[e], u, Code05_FireFighting1.weight[e])
            e = jcast('int', Code05_FireFighting1.next[e])

    @staticmethod
    def distance():
        i = jcast('int', Code05_FireFighting1.end)
        while (i != 0):
            Code05_FireFighting1.diameterPath[i] = jcast('boolean', True)
            i = jcast('int', Code05_FireFighting1.last[i])
        i = jcast('int', Code05_FireFighting1.end)
        while (i != 0):
            jset(Code05_FireFighting1.maxDist, i, Code05_FireFighting1.maxDistanceExceptDiameter(i, 0, 0))
            i = jcast('int', Code05_FireFighting1.last[i])

    # 不能走向直径路径上的节点
    # 能走出的最大距离
    @staticmethod
    def maxDistanceExceptDiameter(u, f, c):
        u = jcast('int', u)
        f = jcast('int', f)
        c = jcast('int', c)
        ans = jcast('int', c)
        e = jcast('int', Code05_FireFighting1.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code05_FireFighting1.to[e])
            if ((not Code05_FireFighting1.diameterPath[v]) and (v != f)):
                ans = jcast('int', jstatic('Math', 'max', ans, Code05_FireFighting1.maxDistanceExceptDiameter(v, u, jcast('int', jadd(c, Code05_FireFighting1.weight[e])))))
            e = jcast('int', Code05_FireFighting1.next[e])
        return jcast('int', ans)

    # 单调队列维护窗口内最大值
    # 不会的看讲解054
    queue = None
    @staticmethod
    def compute():
        suml = jcast('int', 0)
        sumr = jcast('int', 0)
        # 用h和t表示单调队列的头和尾
        h = jcast('int', 0)
        t = jcast('int', 0)
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        # 窗口范围[l,r)，左闭右开，直径上的窗口[l...r-1]
        # l是窗口左端点，r是窗口右端点的再下一个点
        # 课上图解是从start到end，实际是从end到start，思路没有区别
        l = jcast('int', Code05_FireFighting1.end)
        r = jcast('int', Code05_FireFighting1.end)
        while (l != 0):
            while ((r != 0) and (jcast('int', jadd(jcast('int', (sumr - suml)), Code05_FireFighting1.pred[r])) <= Code05_FireFighting1.s)):
                while ((h < t) and (Code05_FireFighting1.maxDist[Code05_FireFighting1.queue[jcast('int', (t - 1))]] <= Code05_FireFighting1.maxDist[r])):
                    t = jcast('int', (t - 1))
                sumr = jcast('int', jcast('int', jadd(sumr, Code05_FireFighting1.pred[r])))
                jset(Code05_FireFighting1.queue, ((_java_old_4 := t), (t := jcast('int', (t + (1)))), _java_old_4)[2], r)
                r = jcast('int', Code05_FireFighting1.last[r])
            ans = jcast('int', jstatic('Math', 'min', ans, jstatic('Math', 'max', jstatic('Math', 'max', suml, Code05_FireFighting1.maxDist[Code05_FireFighting1.queue[h]]), jcast('int', (Code05_FireFighting1.diameter - sumr)))))
            if (Code05_FireFighting1.queue[h] == l):
                h = jcast('int', (h + 1))
            suml = jcast('int', jcast('int', jadd(suml, Code05_FireFighting1.pred[l])))
            l = jcast('int', Code05_FireFighting1.last[l])
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_FireFighting1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code05_FireFighting1.s = jcast('int', jcast('int', jget(in_, 'nval')))
        Code05_FireFighting1.build()
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code05_FireFighting1.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            w = jcast('int', jcast('int', jget(in_, 'nval')))
            Code05_FireFighting1.addEdge(u, v, w)
            Code05_FireFighting1.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        Code05_FireFighting1.road()
        Code05_FireFighting1.distance()
        jcall(out, 'println', Code05_FireFighting1.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_FireFighting1.MAXN = jcast('int', 300001)
Code05_FireFighting1.n = jcast('int', 0)
Code05_FireFighting1.s = jcast('int', 0)
Code05_FireFighting1.head = jarray('int', [Code05_FireFighting1.MAXN])
Code05_FireFighting1.next = jarray('int', [jcast('int', (Code05_FireFighting1.MAXN << (1 & 31)))])
Code05_FireFighting1.to = jarray('int', [jcast('int', (Code05_FireFighting1.MAXN << (1 & 31)))])
Code05_FireFighting1.weight = jarray('int', [jcast('int', (Code05_FireFighting1.MAXN << (1 & 31)))])
Code05_FireFighting1.cnt = jcast('int', 0)
Code05_FireFighting1.start = jcast('int', 0)
Code05_FireFighting1.end = jcast('int', 0)
Code05_FireFighting1.diameter = jcast('int', 0)
Code05_FireFighting1.dist = jarray('int', [Code05_FireFighting1.MAXN])
Code05_FireFighting1.last = jarray('int', [Code05_FireFighting1.MAXN])
Code05_FireFighting1.pred = jarray('int', [Code05_FireFighting1.MAXN])
Code05_FireFighting1.diameterPath = jarray('boolean', [Code05_FireFighting1.MAXN])
Code05_FireFighting1.maxDist = jarray('int', [Code05_FireFighting1.MAXN])
Code05_FireFighting1.queue = jarray('int', [Code05_FireFighting1.MAXN])

if __name__ == '__main__':
    Code05_FireFighting1.main([])
