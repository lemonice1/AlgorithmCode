# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 货车运输
# 一共有n座城市，编号1 ~ n
# 一共有m条双向道路，每条道路(u, v, w)表示有一条限重为w，从u到v的双向道路
# 从一点到另一点的路途中，汽车载重不能超过每一条道路的限重
# 每条查询(a, b)表示从a到b的路线中，汽车允许的最大载重是多少
# 如果从a到b无法到达，那么认为答案是-1
# 一共有q条查询，返回答案数组
# 1 <= n <= 10^4
# 1 <= m <= 5 * 10^4
# 1 <= q <= 3 * 10^4
# 0 <= w <= 10^5
# 1 <= u, v, a, b <= n
# 测试链接 : https://www.luogu.com.cn/problem/P1967
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Trucking:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'LIMIT': 'LIMIT', 'power': 'power', 'edges': 'edges', 'father': 'father', 'visited': 'visited', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'deep': 'deep', 'stjump': 'stjump', 'stmin': 'stmin'}
    MAXN = 0
    MAXM = 0
    LIMIT = 0
    power = 0
    edges = None
    # 并查集
    father = None
    # 给的树有可能是森林，所以需要判断节点是否访问过了
    visited = None
    # 最大生成树建图
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    deep = None
    # stjump[u][p] : u节点往上跳2的次方步，到达什么节点
    stjump = None
    # stmin[u][p] : u节点往上跳2的次方步的路径中，最小的权值
    stmin = None
    @staticmethod
    def log2(n):
        n = jcast('int', n)
        ans = jcast('int', 0)
        while (jcast('int', (1 << (ans & 31))) <= jcast('int', (n >> (1 & 31)))):
            ans = jcast('int', (ans + 1))
        return jcast('int', ans)

    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code02_Trucking.power = jcast('int', Code02_Trucking.log2(n))
        Code02_Trucking.cnt = jcast('int', 1)
        i = jcast('int', 1)
        while (i <= n):
            Code02_Trucking.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'fill', Code02_Trucking.visited, 1, jcast('int', jadd(n, 1)), False)
        jstatic('Arrays', 'fill', Code02_Trucking.head, 1, jcast('int', jadd(n, 1)), 0)

    @staticmethod
    def kruskal(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        jstatic('Arrays', 'sort', Code02_Trucking.edges, 1, jcast('int', jadd(m, 1)), (lambda a, b: (b[2] - a[2])))
        i = jcast('int', 1)
        a = 0
        b = 0
        fa = 0
        fb = 0
        while (i <= m):
            a = jcast('int', Code02_Trucking.edges[i][0])
            b = jcast('int', Code02_Trucking.edges[i][1])
            fa = jcast('int', Code02_Trucking.find(a))
            fb = jcast('int', Code02_Trucking.find(b))
            if (fa != fb):
                Code02_Trucking.father[fa] = jcast('int', fb)
                Code02_Trucking.addEdge(a, b, Code02_Trucking.edges[i][2])
                Code02_Trucking.addEdge(b, a, Code02_Trucking.edges[i][2])
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code02_Trucking.father[i]):
            jset(Code02_Trucking.father, i, Code02_Trucking.find(Code02_Trucking.father[i]))
        return jcast('int', Code02_Trucking.father[i])

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code02_Trucking.next[Code02_Trucking.cnt] = jcast('int', Code02_Trucking.head[u])
        Code02_Trucking.to[Code02_Trucking.cnt] = jcast('int', v)
        Code02_Trucking.weight[Code02_Trucking.cnt] = jcast('int', w)
        jset(Code02_Trucking.head, u, ((_java_obj_1 := Code02_Trucking), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dfs(u, w, f):
        u = jcast('int', u)
        w = jcast('int', w)
        f = jcast('int', f)
        Code02_Trucking.visited[u] = jcast('boolean', True)
        if (f == 0):
            Code02_Trucking.deep[u] = jcast('int', 1)
            jset(Code02_Trucking.stjump[u], 0, u)
            jset(Code02_Trucking.stmin[u], 0, jget(Integer, 'MAX_VALUE'))
        else:
            Code02_Trucking.deep[u] = jcast('int', jcast('int', jadd(Code02_Trucking.deep[f], 1)))
            jset(Code02_Trucking.stjump[u], 0, f)
            jset(Code02_Trucking.stmin[u], 0, w)
        p = jcast('int', 1)
        while (p <= Code02_Trucking.power):
            jset(Code02_Trucking.stjump[u], p, Code02_Trucking.stjump[Code02_Trucking.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            jset(Code02_Trucking.stmin[u], p, jstatic('Math', 'min', Code02_Trucking.stmin[u][jcast('int', (p - 1))], Code02_Trucking.stmin[Code02_Trucking.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))]))
            p = jcast('int', (p + 1))
        e = jcast('int', Code02_Trucking.head[u])
        while (e != 0):
            if (not Code02_Trucking.visited[Code02_Trucking.to[e]]):
                Code02_Trucking.dfs(Code02_Trucking.to[e], Code02_Trucking.weight[e], u)
            e = jcast('int', Code02_Trucking.next[e])

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code02_Trucking.find(a) != Code02_Trucking.find(b)):
            return jcast('int', jcast('int', (-1)))
        if (Code02_Trucking.deep[a] < Code02_Trucking.deep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        p = jcast('int', Code02_Trucking.power)
        while (p >= 0):
            if (Code02_Trucking.deep[Code02_Trucking.stjump[a][p]] >= Code02_Trucking.deep[b]):
                ans = jcast('int', jstatic('Math', 'min', ans, Code02_Trucking.stmin[a][p]))
                a = jcast('int', Code02_Trucking.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', ans)
        p = jcast('int', Code02_Trucking.power)
        while (p >= 0):
            if (Code02_Trucking.stjump[a][p] != Code02_Trucking.stjump[b][p]):
                ans = jcast('int', jstatic('Math', 'min', ans, jstatic('Math', 'min', Code02_Trucking.stmin[a][p], Code02_Trucking.stmin[b][p])))
                a = jcast('int', Code02_Trucking.stjump[a][p])
                b = jcast('int', Code02_Trucking.stjump[b][p])
            p = jcast('int', (p - 1))
        ans = jcast('int', jstatic('Math', 'min', ans, jstatic('Math', 'min', Code02_Trucking.stmin[a][0], Code02_Trucking.stmin[b][0])))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= m):
            jcall(in_, 'nextToken')
            jset(Code02_Trucking.edges[i], 0, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code02_Trucking.edges[i], 1, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code02_Trucking.edges[i], 2, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code02_Trucking.build(n)
        Code02_Trucking.kruskal(n, m)
        i = jcast('int', 1)
        while (i <= n):
            if (not Code02_Trucking.visited[i]):
                Code02_Trucking.dfs(i, 0, 0)
            i = jcast('int', (i + 1))
        jcall(in_, 'nextToken')
        q = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        a = 0
        b = 0
        while (i <= q):
            jcall(in_, 'nextToken')
            a = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            b = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'println', Code02_Trucking.lca(a, b))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Trucking.MAXN = jcast('int', 10001)
Code02_Trucking.MAXM = jcast('int', 50001)
Code02_Trucking.LIMIT = jcast('int', 21)
Code02_Trucking.power = jcast('int', 0)
Code02_Trucking.edges = jarray('int', [Code02_Trucking.MAXM, 3])
Code02_Trucking.father = jarray('int', [Code02_Trucking.MAXN])
Code02_Trucking.visited = jarray('boolean', [Code02_Trucking.MAXN])
Code02_Trucking.head = jarray('int', [Code02_Trucking.MAXN])
Code02_Trucking.next = jarray('int', [jcast('int', (Code02_Trucking.MAXM << (1 & 31)))])
Code02_Trucking.to = jarray('int', [jcast('int', (Code02_Trucking.MAXM << (1 & 31)))])
Code02_Trucking.weight = jarray('int', [jcast('int', (Code02_Trucking.MAXM << (1 & 31)))])
Code02_Trucking.cnt = jcast('int', 0)
Code02_Trucking.deep = jarray('int', [Code02_Trucking.MAXN])
Code02_Trucking.stjump = jarray('int', [Code02_Trucking.MAXN, Code02_Trucking.LIMIT])
Code02_Trucking.stmin = jarray('int', [Code02_Trucking.MAXN, Code02_Trucking.LIMIT])

if __name__ == '__main__':
    Code02_Trucking.main([])
