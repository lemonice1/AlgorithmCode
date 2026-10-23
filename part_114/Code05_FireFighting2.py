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

# 消防(迭代版)
# 一共n个节点，编号1~n，有n-1条边连接成一棵树，每条边上有非负权值
# 给定一个非负整数s，表示可以在树上选择一条长度不超过s的路径
# 然后在这条路径的点上建立消防站，每个居民可以去往这条路径上的任何消防站
# 目标：哪怕最远的居民走到消防站的距离也要尽量少
# 返回最远居民走到消防站的最短距离
# 测试链接 : https://www.luogu.com.cn/problem/P2491
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_FireFighting2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 's': 's', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'start': 'start', 'end': 'end', 'diameter': 'diameter', 'dist': 'dist', 'last': 'last', 'pred': 'pred', 'diameterPath': 'diameterPath', 'maxDist': 'maxDist', 'ufwe': 'ufwe', 'stackSize': 'stackSize', 'u': 'u', 'f': 'f', 'w': 'w', 'e': 'e', 'queue': 'queue'}
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
    pred = None
    diameterPath = None
    maxDist = None
    @staticmethod
    def build():
        Code05_FireFighting2.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code05_FireFighting2.head, 1, jcast('int', jadd(Code05_FireFighting2.n, 1)), 0)
        jstatic('Arrays', 'fill', Code05_FireFighting2.diameterPath, 1, Code05_FireFighting2.n, False)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code05_FireFighting2.next[Code05_FireFighting2.cnt] = jcast('int', Code05_FireFighting2.head[u])
        Code05_FireFighting2.to[Code05_FireFighting2.cnt] = jcast('int', v)
        Code05_FireFighting2.weight[Code05_FireFighting2.cnt] = jcast('int', w)
        jset(Code05_FireFighting2.head, u, ((_java_obj_1 := Code05_FireFighting2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def road():
        Code05_FireFighting2.dfs(1)
        Code05_FireFighting2.start = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code05_FireFighting2.n):
            if (Code05_FireFighting2.dist[i] > Code05_FireFighting2.dist[Code05_FireFighting2.start]):
                Code05_FireFighting2.start = jcast('int', i)
            i = jcast('int', (i + 1))
        Code05_FireFighting2.dfs(Code05_FireFighting2.start)
        Code05_FireFighting2.end = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code05_FireFighting2.n):
            if (Code05_FireFighting2.dist[i] > Code05_FireFighting2.dist[Code05_FireFighting2.end]):
                Code05_FireFighting2.end = jcast('int', i)
            i = jcast('int', (i + 1))
        Code05_FireFighting2.diameter = jcast('int', Code05_FireFighting2.dist[Code05_FireFighting2.end])

    # dfs方法改迭代版
    # 不会改，看讲解118，讲了怎么从递归版改成迭代版
    ufwe = None
    stackSize = 0
    u = 0
    f = 0
    w = 0
    e = 0
    @staticmethod
    def push(u, f, w, e):
        u = jcast('int', u)
        f = jcast('int', f)
        w = jcast('int', w)
        e = jcast('int', e)
        jset(Code05_FireFighting2.ufwe[Code05_FireFighting2.stackSize], 0, u)
        jset(Code05_FireFighting2.ufwe[Code05_FireFighting2.stackSize], 1, f)
        jset(Code05_FireFighting2.ufwe[Code05_FireFighting2.stackSize], 2, w)
        jset(Code05_FireFighting2.ufwe[Code05_FireFighting2.stackSize], 3, e)
        Code05_FireFighting2.stackSize = jcast('int', (Code05_FireFighting2.stackSize + 1))

    @staticmethod
    def pop():
        Code05_FireFighting2.stackSize = jcast('int', (Code05_FireFighting2.stackSize - 1))
        Code05_FireFighting2.u = jcast('int', Code05_FireFighting2.ufwe[Code05_FireFighting2.stackSize][0])
        Code05_FireFighting2.f = jcast('int', Code05_FireFighting2.ufwe[Code05_FireFighting2.stackSize][1])
        Code05_FireFighting2.w = jcast('int', Code05_FireFighting2.ufwe[Code05_FireFighting2.stackSize][2])
        Code05_FireFighting2.e = jcast('int', Code05_FireFighting2.ufwe[Code05_FireFighting2.stackSize][3])

    @staticmethod
    def dfs(root):
        root = jcast('int', root)
        Code05_FireFighting2.stackSize = jcast('int', 0)
        Code05_FireFighting2.push(root, 0, 0, jcast('int', (-1)))
        while (Code05_FireFighting2.stackSize > 0):
            Code05_FireFighting2.pop()
            if (Code05_FireFighting2.e == jcast('int', (-1))):
                Code05_FireFighting2.last[Code05_FireFighting2.u] = jcast('int', Code05_FireFighting2.f)
                Code05_FireFighting2.dist[Code05_FireFighting2.u] = jcast('int', jcast('int', jadd(Code05_FireFighting2.dist[Code05_FireFighting2.f], Code05_FireFighting2.w)))
                Code05_FireFighting2.pred[Code05_FireFighting2.u] = jcast('int', Code05_FireFighting2.w)
                Code05_FireFighting2.e = jcast('int', Code05_FireFighting2.head[Code05_FireFighting2.u])
            else:
                Code05_FireFighting2.e = jcast('int', Code05_FireFighting2.next[Code05_FireFighting2.e])
            if (Code05_FireFighting2.e != 0):
                Code05_FireFighting2.push(Code05_FireFighting2.u, Code05_FireFighting2.f, Code05_FireFighting2.w, Code05_FireFighting2.e)
                if (Code05_FireFighting2.to[Code05_FireFighting2.e] != Code05_FireFighting2.f):
                    Code05_FireFighting2.push(Code05_FireFighting2.to[Code05_FireFighting2.e], Code05_FireFighting2.u, Code05_FireFighting2.weight[Code05_FireFighting2.e], jcast('int', (-1)))

    @staticmethod
    def distance():
        i = jcast('int', Code05_FireFighting2.end)
        while (i != 0):
            Code05_FireFighting2.diameterPath[i] = jcast('boolean', True)
            i = jcast('int', Code05_FireFighting2.last[i])
        i = jcast('int', Code05_FireFighting2.end)
        while (i != 0):
            jset(Code05_FireFighting2.maxDist, i, Code05_FireFighting2.maxDistanceExceptDiameter(i, 0, 0))
            i = jcast('int', Code05_FireFighting2.last[i])

    # maxDistanceExceptDiameter 保留递归写法，深层遍历需考虑调用栈
    # 那就不改了
    @staticmethod
    def maxDistanceExceptDiameter(u, f, c):
        u = jcast('int', u)
        f = jcast('int', f)
        c = jcast('int', c)
        ans = jcast('int', c)
        e = jcast('int', Code05_FireFighting2.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code05_FireFighting2.to[e])
            if ((not Code05_FireFighting2.diameterPath[v]) and (v != f)):
                ans = jcast('int', jstatic('Math', 'max', ans, Code05_FireFighting2.maxDistanceExceptDiameter(v, u, jcast('int', jadd(c, Code05_FireFighting2.weight[e])))))
            e = jcast('int', Code05_FireFighting2.next[e])
        return jcast('int', ans)

    queue = None
    @staticmethod
    def compute():
        suml = jcast('int', 0)
        sumr = jcast('int', 0)
        h = jcast('int', 0)
        t = jcast('int', 0)
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        l = jcast('int', Code05_FireFighting2.end)
        r = jcast('int', Code05_FireFighting2.end)
        while (l != 0):
            while ((r != 0) and (jcast('int', (jcast('int', jadd(sumr, Code05_FireFighting2.pred[r])) - suml)) <= Code05_FireFighting2.s)):
                while ((h < t) and (Code05_FireFighting2.maxDist[Code05_FireFighting2.queue[jcast('int', (t - 1))]] <= Code05_FireFighting2.maxDist[r])):
                    t = jcast('int', (t - 1))
                sumr = jcast('int', jcast('int', jadd(sumr, Code05_FireFighting2.pred[r])))
                jset(Code05_FireFighting2.queue, ((_java_old_4 := t), (t := jcast('int', (t + (1)))), _java_old_4)[2], r)
                r = jcast('int', Code05_FireFighting2.last[r])
            ans = jcast('int', jstatic('Math', 'min', ans, jstatic('Math', 'max', jstatic('Math', 'max', suml, Code05_FireFighting2.maxDist[Code05_FireFighting2.queue[h]]), jcast('int', (Code05_FireFighting2.diameter - sumr)))))
            if (Code05_FireFighting2.queue[h] == l):
                h = jcast('int', (h + 1))
            suml = jcast('int', jcast('int', jadd(suml, Code05_FireFighting2.pred[l])))
            l = jcast('int', Code05_FireFighting2.last[l])
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_FireFighting2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code05_FireFighting2.s = jcast('int', jcast('int', jget(in_, 'nval')))
        Code05_FireFighting2.build()
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code05_FireFighting2.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            w = jcast('int', jcast('int', jget(in_, 'nval')))
            Code05_FireFighting2.addEdge(u, v, w)
            Code05_FireFighting2.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        Code05_FireFighting2.road()
        Code05_FireFighting2.distance()
        jcall(out, 'println', Code05_FireFighting2.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_FireFighting2.MAXN = jcast('int', 300001)
Code05_FireFighting2.n = jcast('int', 0)
Code05_FireFighting2.s = jcast('int', 0)
Code05_FireFighting2.head = jarray('int', [Code05_FireFighting2.MAXN])
Code05_FireFighting2.next = jarray('int', [jcast('int', (Code05_FireFighting2.MAXN << (1 & 31)))])
Code05_FireFighting2.to = jarray('int', [jcast('int', (Code05_FireFighting2.MAXN << (1 & 31)))])
Code05_FireFighting2.weight = jarray('int', [jcast('int', (Code05_FireFighting2.MAXN << (1 & 31)))])
Code05_FireFighting2.cnt = jcast('int', 0)
Code05_FireFighting2.start = jcast('int', 0)
Code05_FireFighting2.end = jcast('int', 0)
Code05_FireFighting2.diameter = jcast('int', 0)
Code05_FireFighting2.dist = jarray('int', [Code05_FireFighting2.MAXN])
Code05_FireFighting2.last = jarray('int', [Code05_FireFighting2.MAXN])
Code05_FireFighting2.pred = jarray('int', [Code05_FireFighting2.MAXN])
Code05_FireFighting2.diameterPath = jarray('boolean', [Code05_FireFighting2.MAXN])
Code05_FireFighting2.maxDist = jarray('int', [Code05_FireFighting2.MAXN])
Code05_FireFighting2.ufwe = jarray('int', [Code05_FireFighting2.MAXN, 4])
Code05_FireFighting2.stackSize = jcast('int', 0)
Code05_FireFighting2.u = jcast('int', 0)
Code05_FireFighting2.f = jcast('int', 0)
Code05_FireFighting2.w = jcast('int', 0)
Code05_FireFighting2.e = jcast('int', 0)
Code05_FireFighting2.queue = jarray('int', [Code05_FireFighting2.MAXN])

if __name__ == '__main__':
    Code05_FireFighting2.main([])
