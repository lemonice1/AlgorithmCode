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

# 更为厉害，Python版
# 为了方便理解，我改写了题意，但是改写的题意和原始题意等效
# 有n个节点，编号1~n，给定n-1条边，连成一棵树，1号点是树头
# 如果x是y的祖先节点，认为"x比y更厉害"
# 如果x到y的路径上，边的数量 <= 某个常数，认为"x和y是邻居"
# 一共有m条查询，每条查询 a k : 打印有多少三元组(a, b, c)满足如下规定
# a、b、c为三个不同的点；a和b都比c厉害；a和b是邻居，路径边的数量 <= 给定的k
# 1 <= n、m、k <= 3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3899
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_MoreImpressive1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 'depth': 'depth', 'head': 'head', 'to': 'to', 'next': 'next', 'cntg': 'cntg', 'root': 'root', 'left': 'left', 'right': 'right', 'sum': 'sum', 'cntt': 'cntt', 'deep': 'deep', 'size': 'size', 'dfn': 'dfn', 'cntd': 'cntd', 'ufe': 'ufe', 'stackSize': 'stackSize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    MAXT = 0
    n = 0
    m = 0
    depth = 0
    # 链式前向星需要
    head = None
    to = None
    next = None
    cntg = 0
    # 可持久化线段树需要
    root = None
    left = None
    right = None
    sum = None
    cntt = 0
    # dfs需要
    # deep[i] : i号节点的深度
    deep = None
    # size[i] : 以i号节点为头的树，有多少个节点
    size = None
    # dfn[i] : i号节点的dfn序号
    dfn = None
    cntd = 0
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_MoreImpressive1.next, ((_java_obj_1 := Code05_MoreImpressive1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_MoreImpressive1.head[u])
        Code05_MoreImpressive1.to[Code05_MoreImpressive1.cntg] = jcast('int', v)
        Code05_MoreImpressive1.head[u] = jcast('int', Code05_MoreImpressive1.cntg)

    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_4 := Code05_MoreImpressive1), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code05_MoreImpressive1.sum[rt] = jcast('long', 0)
        if (l < r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            jset(Code05_MoreImpressive1.left, rt, Code05_MoreImpressive1.build(l, mid))
            jset(Code05_MoreImpressive1.right, rt, Code05_MoreImpressive1.build(jcast('int', jadd(mid, 1)), r))
        return jcast('int', rt)

    @staticmethod
    def add(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_7 := Code05_MoreImpressive1), (_java_key_8 := 'cntt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
        Code05_MoreImpressive1.left[rt] = jcast('int', Code05_MoreImpressive1.left[i])
        Code05_MoreImpressive1.right[rt] = jcast('int', Code05_MoreImpressive1.right[i])
        Code05_MoreImpressive1.sum[rt] = jcast('long', jcast('long', jadd(Code05_MoreImpressive1.sum[i], jobv)))
        if (l < r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                jset(Code05_MoreImpressive1.left, rt, Code05_MoreImpressive1.add(jobi, jobv, l, mid, Code05_MoreImpressive1.left[rt]))
            else:
                jset(Code05_MoreImpressive1.right, rt, Code05_MoreImpressive1.add(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code05_MoreImpressive1.right[rt]))
        return jcast('int', rt)

    @staticmethod
    def query(jobl, jobr, l, r, u, v):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        u = jcast('int', u)
        v = jcast('int', v)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', jcast('long', (Code05_MoreImpressive1.sum[v] - Code05_MoreImpressive1.sum[u])))
        ans = jcast('long', 0)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        if (jobl <= mid):
            ans = jcast('long', jcast('long', jadd(ans, Code05_MoreImpressive1.query(jobl, jobr, l, mid, Code05_MoreImpressive1.left[u], Code05_MoreImpressive1.left[v]))))
        if (jobr > mid):
            ans = jcast('long', jcast('long', jadd(ans, Code05_MoreImpressive1.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code05_MoreImpressive1.right[u], Code05_MoreImpressive1.right[v]))))
        return jcast('long', ans)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code05_MoreImpressive1.deep[u] = jcast('int', jcast('int', jadd(Code05_MoreImpressive1.deep[f], 1)))
        Code05_MoreImpressive1.depth = jcast('int', jstatic('Math', 'max', Code05_MoreImpressive1.depth, Code05_MoreImpressive1.deep[u]))
        Code05_MoreImpressive1.size[u] = jcast('int', 1)
        jset(Code05_MoreImpressive1.dfn, u, ((_java_obj_10 := Code05_MoreImpressive1), (_java_key_11 := 'cntd'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
        ei = jcast('int', Code05_MoreImpressive1.head[u])
        while (ei > 0):
            if (Code05_MoreImpressive1.to[ei] != f):
                Code05_MoreImpressive1.dfs1(Code05_MoreImpressive1.to[ei], u)
            ei = jcast('int', Code05_MoreImpressive1.next[ei])
        ei = jcast('int', Code05_MoreImpressive1.head[u])
        while (ei > 0):
            if (Code05_MoreImpressive1.to[ei] != f):
                Code05_MoreImpressive1.size[u] = jcast('int', jcast('int', jadd(Code05_MoreImpressive1.size[u], Code05_MoreImpressive1.size[Code05_MoreImpressive1.to[ei]])))
            ei = jcast('int', Code05_MoreImpressive1.next[ei])

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs2(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        jset(Code05_MoreImpressive1.root, Code05_MoreImpressive1.dfn[u], Code05_MoreImpressive1.add(Code05_MoreImpressive1.deep[u], jcast('int', (Code05_MoreImpressive1.size[u] - 1)), 1, Code05_MoreImpressive1.depth, Code05_MoreImpressive1.root[jcast('int', (Code05_MoreImpressive1.dfn[u] - 1))]))
        ei = jcast('int', Code05_MoreImpressive1.head[u])
        while (ei > 0):
            if (Code05_MoreImpressive1.to[ei] != f):
                Code05_MoreImpressive1.dfs2(Code05_MoreImpressive1.to[ei], u)
            ei = jcast('int', Code05_MoreImpressive1.next[ei])

    # dfs1、dfs2，分别改成迭代版，dfs3、dfs4
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
        jset(Code05_MoreImpressive1.ufe[Code05_MoreImpressive1.stackSize], 0, u)
        jset(Code05_MoreImpressive1.ufe[Code05_MoreImpressive1.stackSize], 1, f)
        jset(Code05_MoreImpressive1.ufe[Code05_MoreImpressive1.stackSize], 2, e)
        Code05_MoreImpressive1.stackSize = jcast('int', (Code05_MoreImpressive1.stackSize + 1))

    @staticmethod
    def pop():
        Code05_MoreImpressive1.stackSize = jcast('int', (Code05_MoreImpressive1.stackSize - 1))
        Code05_MoreImpressive1.u = jcast('int', Code05_MoreImpressive1.ufe[Code05_MoreImpressive1.stackSize][0])
        Code05_MoreImpressive1.f = jcast('int', Code05_MoreImpressive1.ufe[Code05_MoreImpressive1.stackSize][1])
        Code05_MoreImpressive1.e = jcast('int', Code05_MoreImpressive1.ufe[Code05_MoreImpressive1.stackSize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs3():
        Code05_MoreImpressive1.stackSize = jcast('int', 0)
        Code05_MoreImpressive1.push(1, 0, jcast('int', (-1)))
        while (Code05_MoreImpressive1.stackSize > 0):
            Code05_MoreImpressive1.pop()
            if (Code05_MoreImpressive1.e == jcast('int', (-1))):
                Code05_MoreImpressive1.deep[Code05_MoreImpressive1.u] = jcast('int', jcast('int', jadd(Code05_MoreImpressive1.deep[Code05_MoreImpressive1.f], 1)))
                Code05_MoreImpressive1.depth = jcast('int', jstatic('Math', 'max', Code05_MoreImpressive1.depth, Code05_MoreImpressive1.deep[Code05_MoreImpressive1.u]))
                Code05_MoreImpressive1.size[Code05_MoreImpressive1.u] = jcast('int', 1)
                jset(Code05_MoreImpressive1.dfn, Code05_MoreImpressive1.u, ((_java_obj_13 := Code05_MoreImpressive1), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
                Code05_MoreImpressive1.e = jcast('int', Code05_MoreImpressive1.head[Code05_MoreImpressive1.u])
            else:
                Code05_MoreImpressive1.e = jcast('int', Code05_MoreImpressive1.next[Code05_MoreImpressive1.e])
            if (Code05_MoreImpressive1.e != 0):
                Code05_MoreImpressive1.push(Code05_MoreImpressive1.u, Code05_MoreImpressive1.f, Code05_MoreImpressive1.e)
                if (Code05_MoreImpressive1.to[Code05_MoreImpressive1.e] != Code05_MoreImpressive1.f):
                    Code05_MoreImpressive1.push(Code05_MoreImpressive1.to[Code05_MoreImpressive1.e], Code05_MoreImpressive1.u, jcast('int', (-1)))
            else:
                ei = jcast('int', Code05_MoreImpressive1.head[Code05_MoreImpressive1.u])
                while (ei > 0):
                    if (Code05_MoreImpressive1.to[ei] != Code05_MoreImpressive1.f):
                        Code05_MoreImpressive1.size[Code05_MoreImpressive1.u] = jcast('int', jcast('int', jadd(Code05_MoreImpressive1.size[Code05_MoreImpressive1.u], Code05_MoreImpressive1.size[Code05_MoreImpressive1.to[ei]])))
                    ei = jcast('int', Code05_MoreImpressive1.next[ei])

    # dfs2的迭代版
    @staticmethod
    def dfs4():
        Code05_MoreImpressive1.stackSize = jcast('int', 0)
        Code05_MoreImpressive1.push(1, 0, jcast('int', (-1)))
        while (Code05_MoreImpressive1.stackSize > 0):
            Code05_MoreImpressive1.pop()
            if (Code05_MoreImpressive1.e == jcast('int', (-1))):
                jset(Code05_MoreImpressive1.root, Code05_MoreImpressive1.dfn[Code05_MoreImpressive1.u], Code05_MoreImpressive1.add(Code05_MoreImpressive1.deep[Code05_MoreImpressive1.u], jcast('int', (Code05_MoreImpressive1.size[Code05_MoreImpressive1.u] - 1)), 1, Code05_MoreImpressive1.depth, Code05_MoreImpressive1.root[jcast('int', (Code05_MoreImpressive1.dfn[Code05_MoreImpressive1.u] - 1))]))
                Code05_MoreImpressive1.e = jcast('int', Code05_MoreImpressive1.head[Code05_MoreImpressive1.u])
            else:
                Code05_MoreImpressive1.e = jcast('int', Code05_MoreImpressive1.next[Code05_MoreImpressive1.e])
            if (Code05_MoreImpressive1.e != 0):
                Code05_MoreImpressive1.push(Code05_MoreImpressive1.u, Code05_MoreImpressive1.f, Code05_MoreImpressive1.e)
                if (Code05_MoreImpressive1.to[Code05_MoreImpressive1.e] != Code05_MoreImpressive1.f):
                    Code05_MoreImpressive1.push(Code05_MoreImpressive1.to[Code05_MoreImpressive1.e], Code05_MoreImpressive1.u, jcast('int', (-1)))

    @staticmethod
    def prepare():
        Code05_MoreImpressive1.depth = jcast('int', 0)
        # 使用迭代版防止爆栈
        Code05_MoreImpressive1.dfs3()
        jset(Code05_MoreImpressive1.root, 0, Code05_MoreImpressive1.build(1, Code05_MoreImpressive1.depth))
        # 使用迭代版防止爆栈
        Code05_MoreImpressive1.dfs4()

    @staticmethod
    def compute(a, k):
        a = jcast('int', a)
        k = jcast('int', k)
        ans = jcast('long', jcast('long', (jcast('long', jcast('int', (Code05_MoreImpressive1.size[a] - 1))) * jstatic('Math', 'min', k, jcast('int', (Code05_MoreImpressive1.deep[a] - 1))))))
        ans = jcast('long', jcast('long', jadd(ans, Code05_MoreImpressive1.query(jcast('int', jadd(Code05_MoreImpressive1.deep[a], 1)), jcast('int', jadd(Code05_MoreImpressive1.deep[a], k)), 1, Code05_MoreImpressive1.depth, Code05_MoreImpressive1.root[jcast('int', (Code05_MoreImpressive1.dfn[a] - 1))], Code05_MoreImpressive1.root[jcast('int', (jcast('int', jadd(Code05_MoreImpressive1.dfn[a], Code05_MoreImpressive1.size[a])) - 1))]))))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_MoreImpressive1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code05_MoreImpressive1.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code05_MoreImpressive1.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code05_MoreImpressive1.addEdge(u, v)
            Code05_MoreImpressive1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code05_MoreImpressive1.prepare()
        i = jcast('int', 1)
        a = 0
        k = 0
        while (i <= Code05_MoreImpressive1.m):
            jcall(in_, 'nextToken')
            a = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            k = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'println', Code05_MoreImpressive1.compute(a, k))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_MoreImpressive1.MAXN = jcast('int', 300001)
Code05_MoreImpressive1.MAXT = jcast('int', jcast('int', (Code05_MoreImpressive1.MAXN * 22)))
Code05_MoreImpressive1.n = jcast('int', 0)
Code05_MoreImpressive1.m = jcast('int', 0)
Code05_MoreImpressive1.depth = jcast('int', 0)
Code05_MoreImpressive1.head = jarray('int', [Code05_MoreImpressive1.MAXN])
Code05_MoreImpressive1.to = jarray('int', [jcast('int', (Code05_MoreImpressive1.MAXN << (1 & 31)))])
Code05_MoreImpressive1.next = jarray('int', [jcast('int', (Code05_MoreImpressive1.MAXN << (1 & 31)))])
Code05_MoreImpressive1.cntg = jcast('int', 0)
Code05_MoreImpressive1.root = jarray('int', [Code05_MoreImpressive1.MAXN])
Code05_MoreImpressive1.left = jarray('int', [Code05_MoreImpressive1.MAXT])
Code05_MoreImpressive1.right = jarray('int', [Code05_MoreImpressive1.MAXT])
Code05_MoreImpressive1.sum = jarray('long', [Code05_MoreImpressive1.MAXT])
Code05_MoreImpressive1.cntt = jcast('int', 0)
Code05_MoreImpressive1.deep = jarray('int', [Code05_MoreImpressive1.MAXN])
Code05_MoreImpressive1.size = jarray('int', [Code05_MoreImpressive1.MAXN])
Code05_MoreImpressive1.dfn = jarray('int', [Code05_MoreImpressive1.MAXN])
Code05_MoreImpressive1.cntd = jcast('int', 0)
Code05_MoreImpressive1.ufe = jarray('int', [Code05_MoreImpressive1.MAXN, 3])
Code05_MoreImpressive1.stackSize = jcast('int', 0)
Code05_MoreImpressive1.u = jcast('int', 0)
Code05_MoreImpressive1.f = jcast('int', 0)
Code05_MoreImpressive1.e = jcast('int', 0)

if __name__ == '__main__':
    Code05_MoreImpressive1.main([])
