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

# 巡逻
# 一共n个节点，编号1~n，结构是一棵树，每条边都是双向的
# 警察局在1号点，警车每天从1号点出发，一定要走过树上所有的边，最后回到1号点
# 现在为了减少经过边的数量，你可以新建k条边，把树上任意两点直接相连
# 并且每天警车必须经过新建的道路正好一次
# 计算出最佳的新建道路的方案，返回巡逻走边数量的最小值
# 测试链接 : https://www.luogu.com.cn/problem/P3629
# 1 <= n <= 10^5
# 1 <= k <= 2
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Patrol:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'k': 'k', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'start': 'start', 'end': 'end', 'dist': 'dist', 'last': 'last', 'diameter1': 'diameter1', 'diameter2': 'diameter2', 'diameterPath': 'diameterPath'}
    MAXN = 0
    n = 0
    k = 0
    head = None
    next = None
    to = None
    cnt = 0
    start = 0
    end = 0
    dist = None
    last = None
    diameter1 = 0
    diameter2 = 0
    diameterPath = None
    @staticmethod
    def build():
        Code04_Patrol.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code04_Patrol.head, 1, jcast('int', jadd(Code04_Patrol.n, 1)), 0)
        Code04_Patrol.diameter1 = jcast('int', 0)
        Code04_Patrol.diameter2 = jcast('int', 0)
        jstatic('Arrays', 'fill', Code04_Patrol.diameterPath, 1, Code04_Patrol.n, False)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code04_Patrol.next[Code04_Patrol.cnt] = jcast('int', Code04_Patrol.head[u])
        Code04_Patrol.to[Code04_Patrol.cnt] = jcast('int', v)
        jset(Code04_Patrol.head, u, ((_java_obj_1 := Code04_Patrol), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def road():
        Code04_Patrol.dfs(1, 0, 0)
        Code04_Patrol.start = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code04_Patrol.n):
            if (Code04_Patrol.dist[i] > Code04_Patrol.dist[Code04_Patrol.start]):
                Code04_Patrol.start = jcast('int', i)
            i = jcast('int', (i + 1))
        Code04_Patrol.dfs(Code04_Patrol.start, 0, 0)
        Code04_Patrol.end = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code04_Patrol.n):
            if (Code04_Patrol.dist[i] > Code04_Patrol.dist[Code04_Patrol.end]):
                Code04_Patrol.end = jcast('int', i)
            i = jcast('int', (i + 1))
        Code04_Patrol.diameter1 = jcast('int', Code04_Patrol.dist[Code04_Patrol.end])

    @staticmethod
    def dfs(u, f, w):
        u = jcast('int', u)
        f = jcast('int', f)
        w = jcast('int', w)
        Code04_Patrol.last[u] = jcast('int', f)
        Code04_Patrol.dist[u] = jcast('int', jcast('int', jadd(Code04_Patrol.dist[f], w)))
        e = jcast('int', Code04_Patrol.head[u])
        while (e != 0):
            if (Code04_Patrol.to[e] != f):
                Code04_Patrol.dfs(Code04_Patrol.to[e], u, 1)
            e = jcast('int', Code04_Patrol.next[e])

    # 树型dp第二次求直径长度
    @staticmethod
    def dp(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', Code04_Patrol.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code04_Patrol.to[e])
            if (v != f):
                Code04_Patrol.dp(v, u)
            e = jcast('int', Code04_Patrol.next[e])
        e = jcast('int', Code04_Patrol.head[u])
        v = 0
        w = 0
        while (e != 0):
            v = jcast('int', Code04_Patrol.to[e])
            if (v != f):
                w = jcast('int', (jcast('int', (-1)) if (Code04_Patrol.diameterPath[u] and Code04_Patrol.diameterPath[v]) else 1))
                Code04_Patrol.diameter2 = jcast('int', jstatic('Math', 'max', Code04_Patrol.diameter2, jcast('int', jadd(jcast('int', jadd(Code04_Patrol.dist[u], Code04_Patrol.dist[v])), w))))
                jset(Code04_Patrol.dist, u, jstatic('Math', 'max', Code04_Patrol.dist[u], jcast('int', jadd(Code04_Patrol.dist[v], w))))
            e = jcast('int', Code04_Patrol.next[e])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_Patrol.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_Patrol.k = jcast('int', jcast('int', jget(in_, 'nval')))
        Code04_Patrol.build()
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code04_Patrol.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code04_Patrol.addEdge(u, v)
            Code04_Patrol.addEdge(v, u)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code04_Patrol.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        Code04_Patrol.road()
        if (Code04_Patrol.k == 1):
            return jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (2 * jcast('int', (Code04_Patrol.n - 1)))) - Code04_Patrol.diameter1)), 1)))
        else:
            i = jcast('int', Code04_Patrol.end)
            while (i != 0):
                Code04_Patrol.diameterPath[i] = jcast('boolean', True)
                i = jcast('int', Code04_Patrol.last[i])
            jstatic('Arrays', 'fill', Code04_Patrol.dist, 1, jcast('int', jadd(Code04_Patrol.n, 1)), 0)
            Code04_Patrol.dp(1, 0)
            return jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (jcast('int', (2 * jcast('int', (Code04_Patrol.n - 1)))) - Code04_Patrol.diameter1)) - Code04_Patrol.diameter2)), 2)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Patrol.MAXN = jcast('int', 100001)
Code04_Patrol.n = jcast('int', 0)
Code04_Patrol.k = jcast('int', 0)
Code04_Patrol.head = jarray('int', [Code04_Patrol.MAXN])
Code04_Patrol.next = jarray('int', [jcast('int', (Code04_Patrol.MAXN << (1 & 31)))])
Code04_Patrol.to = jarray('int', [jcast('int', (Code04_Patrol.MAXN << (1 & 31)))])
Code04_Patrol.cnt = jcast('int', 0)
Code04_Patrol.start = jcast('int', 0)
Code04_Patrol.end = jcast('int', 0)
Code04_Patrol.dist = jarray('int', [Code04_Patrol.MAXN])
Code04_Patrol.last = jarray('int', [Code04_Patrol.MAXN])
Code04_Patrol.diameter1 = jcast('int', 0)
Code04_Patrol.diameter2 = jcast('int', 0)
Code04_Patrol.diameterPath = jarray('boolean', [Code04_Patrol.MAXN])

if __name__ == '__main__':
    Code04_Patrol.main([])
