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

# 路径上的第k小，Python版
# 有n个节点，编号1~n，每个节点有权值，有n-1条边，所有节点组成一棵树
# 一共有m条查询，每条查询 u v k : 打印u号点到v号点的路径上，第k小的点权
# 题目有强制在线的要求，上一次打印的答案为lastAns，初始时lastAns = 0
# 每次给定的u、v、k，按照如下方式得到真实的u、v、k，查询完成后更新lastAns
# 真实u = 给定u ^ lastAns
# 真实v = 给定v
# 真实k = 给定k
# 1 <= n、m <= 10^5
# 1 <= arr[i] <= 2^32 - 1
# 测试链接 : https://www.luogu.com.cn/problem/P2633
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_CountOnTree1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 's': 's', 'arr': 'arr', 'sorted': 'sorted', 'head': 'head', 'to': 'to', 'next': 'next', 'cntg': 'cntg', 'root': 'root', 'left': 'left', 'right': 'right', 'size': 'size', 'cntt': 'cntt', 'deep': 'deep', 'stjump': 'stjump', 'ufe': 'ufe', 'stackSize': 'stackSize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    MAXP = 0
    MAXT = 0
    n = 0
    m = 0
    s = 0
    # 各个节点权值
    arr = None
    # 收集权值排序并且去重做离散化
    sorted = None
    # 链式前向星需要
    head = None
    to = None
    next = None
    cntg = 0
    # 可持久化线段树需要
    root = None
    left = None
    right = None
    size = None
    cntt = 0
    # 树上倍增找lca需要
    deep = None
    stjump = None
    @staticmethod
    def _java_kth_0(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code04_CountOnTree1.s)
        mid = 0
        while (left <= right):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(left, right)), 2)))
            if (Code04_CountOnTree1.sorted[mid] == num):
                return jcast('int', mid)
            else:
                if (Code04_CountOnTree1.sorted[mid] < num):
                    left = jcast('int', jcast('int', jadd(mid, 1)))
                else:
                    right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_1 := Code04_CountOnTree1), (_java_key_2 := 'cntt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        Code04_CountOnTree1.size[rt] = jcast('int', 0)
        if (l < r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            jset(Code04_CountOnTree1.left, rt, Code04_CountOnTree1.build(l, mid))
            jset(Code04_CountOnTree1.right, rt, Code04_CountOnTree1.build(jcast('int', jadd(mid, 1)), r))
        return jcast('int', rt)

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code04_CountOnTree1.n):
            Code04_CountOnTree1.sorted[i] = jcast('int', Code04_CountOnTree1.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_CountOnTree1.sorted, 1, jcast('int', jadd(Code04_CountOnTree1.n, 1)))
        Code04_CountOnTree1.s = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code04_CountOnTree1.n):
            if (Code04_CountOnTree1.sorted[Code04_CountOnTree1.s] != Code04_CountOnTree1.sorted[i]):
                jset(Code04_CountOnTree1.sorted, ((_java_obj_4 := Code04_CountOnTree1), (_java_key_5 := 's'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code04_CountOnTree1.sorted[i])
            i = jcast('int', (i + 1))
        jset(Code04_CountOnTree1.root, 0, Code04_CountOnTree1.build(1, Code04_CountOnTree1.s))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_CountOnTree1.next, ((_java_obj_7 := Code04_CountOnTree1), (_java_key_8 := 'cntg'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], Code04_CountOnTree1.head[u])
        Code04_CountOnTree1.to[Code04_CountOnTree1.cntg] = jcast('int', v)
        Code04_CountOnTree1.head[u] = jcast('int', Code04_CountOnTree1.cntg)

    @staticmethod
    def insert(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_10 := Code04_CountOnTree1), (_java_key_11 := 'cntt'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
        Code04_CountOnTree1.left[rt] = jcast('int', Code04_CountOnTree1.left[i])
        Code04_CountOnTree1.right[rt] = jcast('int', Code04_CountOnTree1.right[i])
        Code04_CountOnTree1.size[rt] = jcast('int', jcast('int', jadd(Code04_CountOnTree1.size[i], 1)))
        if (l < r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                jset(Code04_CountOnTree1.left, rt, Code04_CountOnTree1.insert(jobi, l, mid, Code04_CountOnTree1.left[rt]))
            else:
                jset(Code04_CountOnTree1.right, rt, Code04_CountOnTree1.insert(jobi, jcast('int', jadd(mid, 1)), r, Code04_CountOnTree1.right[rt]))
        return jcast('int', rt)

    @staticmethod
    def query(jobk, l, r, u, v, lca, lcafa):
        jobk = jcast('int', jobk)
        l = jcast('int', l)
        r = jcast('int', r)
        u = jcast('int', u)
        v = jcast('int', v)
        lca = jcast('int', lca)
        lcafa = jcast('int', lcafa)
        if (l == r):
            return jcast('int', l)
        lsize = jcast('int', jcast('int', (jcast('int', (jcast('int', jadd(Code04_CountOnTree1.size[Code04_CountOnTree1.left[u]], Code04_CountOnTree1.size[Code04_CountOnTree1.left[v]])) - Code04_CountOnTree1.size[Code04_CountOnTree1.left[lca]])) - Code04_CountOnTree1.size[Code04_CountOnTree1.left[lcafa]])))
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        if (lsize >= jobk):
            return jcast('int', Code04_CountOnTree1.query(jobk, l, mid, Code04_CountOnTree1.left[u], Code04_CountOnTree1.left[v], Code04_CountOnTree1.left[lca], Code04_CountOnTree1.left[lcafa]))
        else:
            return jcast('int', Code04_CountOnTree1.query(jcast('int', (jobk - lsize)), jcast('int', jadd(mid, 1)), r, Code04_CountOnTree1.right[u], Code04_CountOnTree1.right[v], Code04_CountOnTree1.right[lca], Code04_CountOnTree1.right[lcafa]))

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        jset(Code04_CountOnTree1.root, u, Code04_CountOnTree1.insert(Code04_CountOnTree1._java_kth_0(Code04_CountOnTree1.arr[u]), 1, Code04_CountOnTree1.s, Code04_CountOnTree1.root[f]))
        Code04_CountOnTree1.deep[u] = jcast('int', jcast('int', jadd(Code04_CountOnTree1.deep[f], 1)))
        jset(Code04_CountOnTree1.stjump[u], 0, f)
        p = jcast('int', 1)
        while (p < Code04_CountOnTree1.MAXP):
            jset(Code04_CountOnTree1.stjump[u], p, Code04_CountOnTree1.stjump[Code04_CountOnTree1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        ei = jcast('int', Code04_CountOnTree1.head[u])
        while (ei > 0):
            if (Code04_CountOnTree1.to[ei] != f):
                Code04_CountOnTree1.dfs1(Code04_CountOnTree1.to[ei], u)
            ei = jcast('int', Code04_CountOnTree1.next[ei])

    # 迭代版：使用显式状态保存遍历进度
    # 讲解118，详解了从递归版改迭代版
    ufe = None
    stackSize = 0
    u = 0
    f = 0
    e = 0
    @staticmethod
    def push(u, f, e):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', e)
        jset(Code04_CountOnTree1.ufe[Code04_CountOnTree1.stackSize], 0, u)
        jset(Code04_CountOnTree1.ufe[Code04_CountOnTree1.stackSize], 1, f)
        jset(Code04_CountOnTree1.ufe[Code04_CountOnTree1.stackSize], 2, e)
        Code04_CountOnTree1.stackSize = jcast('int', (Code04_CountOnTree1.stackSize + 1))

    @staticmethod
    def pop():
        Code04_CountOnTree1.stackSize = jcast('int', (Code04_CountOnTree1.stackSize - 1))
        Code04_CountOnTree1.u = jcast('int', Code04_CountOnTree1.ufe[Code04_CountOnTree1.stackSize][0])
        Code04_CountOnTree1.f = jcast('int', Code04_CountOnTree1.ufe[Code04_CountOnTree1.stackSize][1])
        Code04_CountOnTree1.e = jcast('int', Code04_CountOnTree1.ufe[Code04_CountOnTree1.stackSize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs2():
        Code04_CountOnTree1.stackSize = jcast('int', 0)
        Code04_CountOnTree1.push(1, 0, jcast('int', (-1)))
        while (Code04_CountOnTree1.stackSize > 0):
            Code04_CountOnTree1.pop()
            if (Code04_CountOnTree1.e == jcast('int', (-1))):
                jset(Code04_CountOnTree1.root, Code04_CountOnTree1.u, Code04_CountOnTree1.insert(Code04_CountOnTree1._java_kth_0(Code04_CountOnTree1.arr[Code04_CountOnTree1.u]), 1, Code04_CountOnTree1.s, Code04_CountOnTree1.root[Code04_CountOnTree1.f]))
                Code04_CountOnTree1.deep[Code04_CountOnTree1.u] = jcast('int', jcast('int', jadd(Code04_CountOnTree1.deep[Code04_CountOnTree1.f], 1)))
                jset(Code04_CountOnTree1.stjump[Code04_CountOnTree1.u], 0, Code04_CountOnTree1.f)
                p = jcast('int', 1)
                while (p < Code04_CountOnTree1.MAXP):
                    jset(Code04_CountOnTree1.stjump[Code04_CountOnTree1.u], p, Code04_CountOnTree1.stjump[Code04_CountOnTree1.stjump[Code04_CountOnTree1.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code04_CountOnTree1.e = jcast('int', Code04_CountOnTree1.head[Code04_CountOnTree1.u])
            else:
                Code04_CountOnTree1.e = jcast('int', Code04_CountOnTree1.next[Code04_CountOnTree1.e])
            if (Code04_CountOnTree1.e != 0):
                Code04_CountOnTree1.push(Code04_CountOnTree1.u, Code04_CountOnTree1.f, Code04_CountOnTree1.e)
                if (Code04_CountOnTree1.to[Code04_CountOnTree1.e] != Code04_CountOnTree1.f):
                    Code04_CountOnTree1.push(Code04_CountOnTree1.to[Code04_CountOnTree1.e], Code04_CountOnTree1.u, jcast('int', (-1)))

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code04_CountOnTree1.deep[a] < Code04_CountOnTree1.deep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code04_CountOnTree1.MAXP - 1)))
        while (p >= 0):
            if (Code04_CountOnTree1.deep[Code04_CountOnTree1.stjump[a][p]] >= Code04_CountOnTree1.deep[b]):
                a = jcast('int', Code04_CountOnTree1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code04_CountOnTree1.MAXP - 1)))
        while (p >= 0):
            if (Code04_CountOnTree1.stjump[a][p] != Code04_CountOnTree1.stjump[b][p]):
                a = jcast('int', Code04_CountOnTree1.stjump[a][p])
                b = jcast('int', Code04_CountOnTree1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code04_CountOnTree1.stjump[a][0])

    @staticmethod
    def _java_kth_1(u, v, k):
        u = jcast('int', u)
        v = jcast('int', v)
        k = jcast('int', k)
        lca = jcast('int', Code04_CountOnTree1.lca(u, v))
        i = jcast('int', Code04_CountOnTree1.query(k, 1, Code04_CountOnTree1.s, Code04_CountOnTree1.root[u], Code04_CountOnTree1.root[v], Code04_CountOnTree1.root[lca], Code04_CountOnTree1.root[Code04_CountOnTree1.stjump[lca][0]]))
        return jcast('int', Code04_CountOnTree1.sorted[i])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_CountOnTree1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_CountOnTree1.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code04_CountOnTree1.n):
            jcall(in_, 'nextToken')
            Code04_CountOnTree1.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code04_CountOnTree1.prepare()
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code04_CountOnTree1.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code04_CountOnTree1.addEdge(u, v)
            Code04_CountOnTree1.addEdge(v, u)
            i = jcast('int', (i + 1))
        # 使用迭代版防止爆栈
        Code04_CountOnTree1.dfs2()
        i = jcast('int', 1)
        u = 0
        v = 0
        k = 0
        lastAns = jcast('int', 0)
        while (i <= Code04_CountOnTree1.m):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', (jcast('int', jget(in_, 'nval')) ^ lastAns)))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            k = jcast('int', jcast('int', jget(in_, 'nval')))
            lastAns = jcast('int', Code04_CountOnTree1._java_kth_1(u, v, k))
            jcall(out, 'println', lastAns)
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def kth(*args):
        _java_choice = jselect(args, [['int'], ['int', 'int', 'int']], [False, False])
        if _java_choice == 0:
            return Code04_CountOnTree1._java_kth_0(*args)
        if _java_choice == 1:
            return Code04_CountOnTree1._java_kth_1(*args)
        raise TypeError("No matching overload for Code04_CountOnTree1.kth")


Code04_CountOnTree1.MAXN = jcast('int', 100001)
Code04_CountOnTree1.MAXP = jcast('int', 20)
Code04_CountOnTree1.MAXT = jcast('int', jcast('int', (Code04_CountOnTree1.MAXN * Code04_CountOnTree1.MAXP)))
Code04_CountOnTree1.n = jcast('int', 0)
Code04_CountOnTree1.m = jcast('int', 0)
Code04_CountOnTree1.s = jcast('int', 0)
Code04_CountOnTree1.arr = jarray('int', [Code04_CountOnTree1.MAXN])
Code04_CountOnTree1.sorted = jarray('int', [Code04_CountOnTree1.MAXN])
Code04_CountOnTree1.head = jarray('int', [Code04_CountOnTree1.MAXN])
Code04_CountOnTree1.to = jarray('int', [jcast('int', (Code04_CountOnTree1.MAXN << (1 & 31)))])
Code04_CountOnTree1.next = jarray('int', [jcast('int', (Code04_CountOnTree1.MAXN << (1 & 31)))])
Code04_CountOnTree1.cntg = jcast('int', 0)
Code04_CountOnTree1.root = jarray('int', [Code04_CountOnTree1.MAXN])
Code04_CountOnTree1.left = jarray('int', [Code04_CountOnTree1.MAXT])
Code04_CountOnTree1.right = jarray('int', [Code04_CountOnTree1.MAXT])
Code04_CountOnTree1.size = jarray('int', [Code04_CountOnTree1.MAXT])
Code04_CountOnTree1.cntt = jcast('int', 0)
Code04_CountOnTree1.deep = jarray('int', [Code04_CountOnTree1.MAXN])
Code04_CountOnTree1.stjump = jarray('int', [Code04_CountOnTree1.MAXN, Code04_CountOnTree1.MAXP])
Code04_CountOnTree1.ufe = jarray('int', [Code04_CountOnTree1.MAXN, 3])
Code04_CountOnTree1.stackSize = jcast('int', 0)
Code04_CountOnTree1.u = jcast('int', 0)
Code04_CountOnTree1.f = jcast('int', 0)
Code04_CountOnTree1.e = jcast('int', 0)

if __name__ == '__main__':
    Code04_CountOnTree1.main([])
