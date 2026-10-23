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

# 可撤销并查集模版题，Python版
# 一共有n个点，每个点有两个小球，每个点给定两个小球的编号
# 一共有n-1条无向边，所有节点连成一棵树
# 对i号点，2 <= i <= n，都计算如下问题的答案并打印
# 从1号点到i号点的最短路径上，每个点只能拿一个小球，最多能拿几个编号不同的小球
# 1 <= n <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/AT_abc302_h
# 测试链接 : https://atcoder.jp/contests/abc302/tasks/abc302_h
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_UndoUnionFind2:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'father': 'father', 'siz': 'siz', 'edgeCnt': 'edgeCnt', 'rollback': 'rollback', 'opsize': 'opsize', 'ans': 'ans', 'ball': 'ball'}
    MAXN = 0
    arr = None
    head = None
    next = None
    to = None
    cnt = 0
    father = None
    siz = None
    edgeCnt = None
    rollback = None
    opsize = 0
    ans = None
    ball = 0
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_UndoUnionFind2.next, ((_java_obj_1 := Code02_UndoUnionFind2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_UndoUnionFind2.head[u])
        Code02_UndoUnionFind2.to[Code02_UndoUnionFind2.cnt] = jcast('int', v)
        Code02_UndoUnionFind2.head[u] = jcast('int', Code02_UndoUnionFind2.cnt)

    @staticmethod
    def find(i):
        i = jcast('int', i)
        while (i != Code02_UndoUnionFind2.father[i]):
            i = jcast('int', Code02_UndoUnionFind2.father[i])
        return jcast('int', i)

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code02_UndoUnionFind2.find(x))
        fy = jcast('int', Code02_UndoUnionFind2.find(y))
        if (Code02_UndoUnionFind2.siz[fx] < Code02_UndoUnionFind2.siz[fy]):
            tmp = jcast('int', fx)
            fx = jcast('int', fy)
            fy = jcast('int', tmp)
        Code02_UndoUnionFind2.father[fy] = jcast('int', fx)
        Code02_UndoUnionFind2.siz[fx] = jcast('int', jcast('int', jadd(Code02_UndoUnionFind2.siz[fx], Code02_UndoUnionFind2.siz[fy])))
        Code02_UndoUnionFind2.edgeCnt[fx] = jcast('int', jcast('int', jadd(Code02_UndoUnionFind2.edgeCnt[fx], jcast('int', jadd(Code02_UndoUnionFind2.edgeCnt[fy], 1)))))
        jset(Code02_UndoUnionFind2.rollback[((_java_obj_4 := Code02_UndoUnionFind2), (_java_key_5 := 'opsize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]], 0, fx)
        jset(Code02_UndoUnionFind2.rollback[Code02_UndoUnionFind2.opsize], 1, fy)

    @staticmethod
    def undo():
        fx = jcast('int', Code02_UndoUnionFind2.rollback[Code02_UndoUnionFind2.opsize][0])
        fy = jcast('int', Code02_UndoUnionFind2.rollback[((_java_obj_7 := Code02_UndoUnionFind2), (_java_key_8 := 'opsize'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]][1])
        Code02_UndoUnionFind2.father[fy] = jcast('int', fy)
        Code02_UndoUnionFind2.siz[fx] = jcast('int', jcast('int', (Code02_UndoUnionFind2.siz[fx] - Code02_UndoUnionFind2.siz[fy])))
        Code02_UndoUnionFind2.edgeCnt[fx] = jcast('int', jcast('int', (Code02_UndoUnionFind2.edgeCnt[fx] - jcast('int', jadd(Code02_UndoUnionFind2.edgeCnt[fy], 1)))))

    @staticmethod
    def dfs(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        fx = jcast('int', Code02_UndoUnionFind2.find(Code02_UndoUnionFind2.arr[u][0]))
        fy = jcast('int', Code02_UndoUnionFind2.find(Code02_UndoUnionFind2.arr[u][1]))
        added = jcast('boolean', False)
        unioned = jcast('boolean', False)
        if (fx == fy):
            if (Code02_UndoUnionFind2.edgeCnt[fx] < Code02_UndoUnionFind2.siz[fx]):
                Code02_UndoUnionFind2.ball = jcast('int', (Code02_UndoUnionFind2.ball + 1))
                added = jcast('boolean', True)
            Code02_UndoUnionFind2.edgeCnt[fx] = jcast('int', (Code02_UndoUnionFind2.edgeCnt[fx] + 1))
        else:
            if ((Code02_UndoUnionFind2.edgeCnt[fx] < Code02_UndoUnionFind2.siz[fx]) or (Code02_UndoUnionFind2.edgeCnt[fy] < Code02_UndoUnionFind2.siz[fy])):
                Code02_UndoUnionFind2.ball = jcast('int', (Code02_UndoUnionFind2.ball + 1))
                added = jcast('boolean', True)
            Code02_UndoUnionFind2.union(fx, fy)
            unioned = jcast('boolean', True)
        Code02_UndoUnionFind2.ans[u] = jcast('int', Code02_UndoUnionFind2.ball)
        e = jcast('int', Code02_UndoUnionFind2.head[u])
        while (e > 0):
            if (Code02_UndoUnionFind2.to[e] != fa):
                Code02_UndoUnionFind2.dfs(Code02_UndoUnionFind2.to[e], u)
            e = jcast('int', Code02_UndoUnionFind2.next[e])
        if added:
            Code02_UndoUnionFind2.ball = jcast('int', (Code02_UndoUnionFind2.ball - 1))
        if unioned:
            Code02_UndoUnionFind2.undo()
        else:
            Code02_UndoUnionFind2.edgeCnt[fx] = jcast('int', (Code02_UndoUnionFind2.edgeCnt[fx] - 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= n):
            jcall(in_, 'nextToken')
            jset(Code02_UndoUnionFind2.arr[i], 0, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code02_UndoUnionFind2.arr[i], 1, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_UndoUnionFind2.addEdge(u, v)
            Code02_UndoUnionFind2.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= n):
            Code02_UndoUnionFind2.father[i] = jcast('int', i)
            Code02_UndoUnionFind2.siz[i] = jcast('int', 1)
            Code02_UndoUnionFind2.edgeCnt[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        Code02_UndoUnionFind2.dfs(1, 0)
        i = jcast('int', 2)
        while (i < n):
            jcall(out, 'print', jadd(Code02_UndoUnionFind2.ans[i], ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code02_UndoUnionFind2.ans[n])
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_UndoUnionFind2.MAXN = jcast('int', 200001)
Code02_UndoUnionFind2.arr = jarray('int', [Code02_UndoUnionFind2.MAXN, 2])
Code02_UndoUnionFind2.head = jarray('int', [Code02_UndoUnionFind2.MAXN])
Code02_UndoUnionFind2.next = jarray('int', [jcast('int', (Code02_UndoUnionFind2.MAXN << (1 & 31)))])
Code02_UndoUnionFind2.to = jarray('int', [jcast('int', (Code02_UndoUnionFind2.MAXN << (1 & 31)))])
Code02_UndoUnionFind2.cnt = jcast('int', 0)
Code02_UndoUnionFind2.father = jarray('int', [Code02_UndoUnionFind2.MAXN])
Code02_UndoUnionFind2.siz = jarray('int', [Code02_UndoUnionFind2.MAXN])
Code02_UndoUnionFind2.edgeCnt = jarray('int', [Code02_UndoUnionFind2.MAXN])
Code02_UndoUnionFind2.rollback = jarray('int', [Code02_UndoUnionFind2.MAXN, 2])
Code02_UndoUnionFind2.opsize = jcast('int', 0)
Code02_UndoUnionFind2.ans = jarray('int', [Code02_UndoUnionFind2.MAXN])
Code02_UndoUnionFind2.ball = jcast('int', 0)

if __name__ == '__main__':
    Code02_UndoUnionFind2.main([])
