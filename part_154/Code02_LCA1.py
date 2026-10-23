# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 重链剖分解决LCA查询，Python版
# 一共有n个节点，给定n-1条边，节点连成一棵树，给定头节点编号root
# 一共有m条查询，每条查询给定a和b，打印a和b的最低公共祖先
# 请用树链剖分的方式实现
# 1 <= n、m <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3379
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_LCA1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'root': 'root', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'fse': 'fse', 'stacksize': 'stacksize', 'first': 'first', 'second': 'second', 'edge': 'edge'}
    MAXN = 0
    n = 0
    m = 0
    root = 0
    head = None
    next = None
    to = None
    cnt = 0
    fa = None
    dep = None
    siz = None
    son = None
    top = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_LCA1.next, ((_java_obj_1 := Code02_LCA1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_LCA1.head[u])
        Code02_LCA1.to[Code02_LCA1.cnt] = jcast('int', v)
        Code02_LCA1.head[u] = jcast('int', Code02_LCA1.cnt)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code02_LCA1.fa[u] = jcast('int', f)
        Code02_LCA1.dep[u] = jcast('int', jcast('int', jadd(Code02_LCA1.dep[f], 1)))
        Code02_LCA1.siz[u] = jcast('int', 1)
        e = jcast('int', Code02_LCA1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code02_LCA1.to[e])
            if (v != f):
                Code02_LCA1.dfs1(v, u)
            e = jcast('int', Code02_LCA1.next[e])
        e = jcast('int', Code02_LCA1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code02_LCA1.to[e])
            if (v != f):
                Code02_LCA1.siz[u] = jcast('int', jcast('int', jadd(Code02_LCA1.siz[u], Code02_LCA1.siz[v])))
                if ((Code02_LCA1.son[u] == 0) or (Code02_LCA1.siz[Code02_LCA1.son[u]] < Code02_LCA1.siz[v])):
                    Code02_LCA1.son[u] = jcast('int', v)
            e = jcast('int', Code02_LCA1.next[e])

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code02_LCA1.top[u] = jcast('int', t)
        if (Code02_LCA1.son[u] == 0):
            return
        Code02_LCA1.dfs2(Code02_LCA1.son[u], t)
        e = jcast('int', Code02_LCA1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code02_LCA1.to[e])
            if ((v != Code02_LCA1.fa[u]) and (v != Code02_LCA1.son[u])):
                Code02_LCA1.dfs2(v, v)
            e = jcast('int', Code02_LCA1.next[e])

    # 不会改迭代版，去看讲解118，详解了从递归版改迭代版
    fse = None
    stacksize = 0
    first = 0
    second = 0
    edge = 0
    @staticmethod
    def push(fir, sec, edg):
        fir = jcast('int', fir)
        sec = jcast('int', sec)
        edg = jcast('int', edg)
        jset(Code02_LCA1.fse[Code02_LCA1.stacksize], 0, fir)
        jset(Code02_LCA1.fse[Code02_LCA1.stacksize], 1, sec)
        jset(Code02_LCA1.fse[Code02_LCA1.stacksize], 2, edg)
        Code02_LCA1.stacksize = jcast('int', (Code02_LCA1.stacksize + 1))

    @staticmethod
    def pop():
        Code02_LCA1.stacksize = jcast('int', (Code02_LCA1.stacksize - 1))
        Code02_LCA1.first = jcast('int', Code02_LCA1.fse[Code02_LCA1.stacksize][0])
        Code02_LCA1.second = jcast('int', Code02_LCA1.fse[Code02_LCA1.stacksize][1])
        Code02_LCA1.edge = jcast('int', Code02_LCA1.fse[Code02_LCA1.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs3():
        Code02_LCA1.stacksize = jcast('int', 0)
        Code02_LCA1.push(Code02_LCA1.root, 0, jcast('int', (-1)))
        while (Code02_LCA1.stacksize > 0):
            Code02_LCA1.pop()
            if (Code02_LCA1.edge == jcast('int', (-1))):
                Code02_LCA1.fa[Code02_LCA1.first] = jcast('int', Code02_LCA1.second)
                Code02_LCA1.dep[Code02_LCA1.first] = jcast('int', jcast('int', jadd(Code02_LCA1.dep[Code02_LCA1.second], 1)))
                Code02_LCA1.siz[Code02_LCA1.first] = jcast('int', 1)
                Code02_LCA1.edge = jcast('int', Code02_LCA1.head[Code02_LCA1.first])
            else:
                Code02_LCA1.edge = jcast('int', Code02_LCA1.next[Code02_LCA1.edge])
            if (Code02_LCA1.edge != 0):
                Code02_LCA1.push(Code02_LCA1.first, Code02_LCA1.second, Code02_LCA1.edge)
                if (Code02_LCA1.to[Code02_LCA1.edge] != Code02_LCA1.second):
                    Code02_LCA1.push(Code02_LCA1.to[Code02_LCA1.edge], Code02_LCA1.first, jcast('int', (-1)))
            else:
                e = jcast('int', Code02_LCA1.head[Code02_LCA1.first])
                v = 0
                while (e > 0):
                    v = jcast('int', Code02_LCA1.to[e])
                    if (v != Code02_LCA1.second):
                        Code02_LCA1.siz[Code02_LCA1.first] = jcast('int', jcast('int', jadd(Code02_LCA1.siz[Code02_LCA1.first], Code02_LCA1.siz[v])))
                        if ((Code02_LCA1.son[Code02_LCA1.first] == 0) or (Code02_LCA1.siz[Code02_LCA1.son[Code02_LCA1.first]] < Code02_LCA1.siz[v])):
                            Code02_LCA1.son[Code02_LCA1.first] = jcast('int', v)
                    e = jcast('int', Code02_LCA1.next[e])

    # dfs2的迭代版
    @staticmethod
    def dfs4():
        Code02_LCA1.stacksize = jcast('int', 0)
        Code02_LCA1.push(Code02_LCA1.root, Code02_LCA1.root, jcast('int', (-1)))
        while (Code02_LCA1.stacksize > 0):
            try:
                Code02_LCA1.pop()
                # edge == -1，表示第一次来到当前节点，并且先处理重儿子
                if (Code02_LCA1.edge == jcast('int', (-1))):
                    Code02_LCA1.top[Code02_LCA1.first] = jcast('int', Code02_LCA1.second)
                    if (Code02_LCA1.son[Code02_LCA1.first] == 0):
                        raise JContinue(None)
                    Code02_LCA1.push(Code02_LCA1.first, Code02_LCA1.second, jcast('int', (-2)))
                    Code02_LCA1.push(Code02_LCA1.son[Code02_LCA1.first], Code02_LCA1.second, jcast('int', (-1)))
                    raise JContinue(None)
                    # edge == -2，表示处理完当前节点的重儿子，回到了当前节点
                else:
                    if (Code02_LCA1.edge == jcast('int', (-2))):
                        Code02_LCA1.edge = jcast('int', Code02_LCA1.head[Code02_LCA1.first])
                        # edge >= 0, 继续处理其他的边
                    else:
                        Code02_LCA1.edge = jcast('int', Code02_LCA1.next[Code02_LCA1.edge])
                if (Code02_LCA1.edge != 0):
                    Code02_LCA1.push(Code02_LCA1.first, Code02_LCA1.second, Code02_LCA1.edge)
                    if ((Code02_LCA1.to[Code02_LCA1.edge] != Code02_LCA1.fa[Code02_LCA1.first]) and (Code02_LCA1.to[Code02_LCA1.edge] != Code02_LCA1.son[Code02_LCA1.first])):
                        Code02_LCA1.push(Code02_LCA1.to[Code02_LCA1.edge], Code02_LCA1.to[Code02_LCA1.edge], jcast('int', (-1)))
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        while (Code02_LCA1.top[a] != Code02_LCA1.top[b]):
            if (Code02_LCA1.dep[Code02_LCA1.top[a]] <= Code02_LCA1.dep[Code02_LCA1.top[b]]):
                b = jcast('int', Code02_LCA1.fa[Code02_LCA1.top[b]])
            else:
                a = jcast('int', Code02_LCA1.fa[Code02_LCA1.top[a]])
        return jcast('int', (a if (Code02_LCA1.dep[a] <= Code02_LCA1.dep[b]) else b))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_LCA1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_LCA1.m = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_LCA1.root = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code02_LCA1.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_LCA1.addEdge(u, v)
            Code02_LCA1.addEdge(v, u)
            i = jcast('int', (i + 1))
        # dfs3() 等同于 dfs1(root, 0)，调用迭代版防止爆栈
        Code02_LCA1.dfs3()
        # dfs4() 等同于 dfs2(root, root)，调用迭代版防止爆栈
        Code02_LCA1.dfs4()
        i = jcast('int', 1)
        a = 0
        b = 0
        while (i <= Code02_LCA1.m):
            jcall(in_, 'nextToken')
            a = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            b = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'println', Code02_LCA1.lca(a, b))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_LCA1.MAXN = jcast('int', 500001)
Code02_LCA1.n = jcast('int', 0)
Code02_LCA1.m = jcast('int', 0)
Code02_LCA1.root = jcast('int', 0)
Code02_LCA1.head = jarray('int', [Code02_LCA1.MAXN])
Code02_LCA1.next = jarray('int', [jcast('int', (Code02_LCA1.MAXN << (1 & 31)))])
Code02_LCA1.to = jarray('int', [jcast('int', (Code02_LCA1.MAXN << (1 & 31)))])
Code02_LCA1.cnt = jcast('int', 0)
Code02_LCA1.fa = jarray('int', [Code02_LCA1.MAXN])
Code02_LCA1.dep = jarray('int', [Code02_LCA1.MAXN])
Code02_LCA1.siz = jarray('int', [Code02_LCA1.MAXN])
Code02_LCA1.son = jarray('int', [Code02_LCA1.MAXN])
Code02_LCA1.top = jarray('int', [Code02_LCA1.MAXN])
Code02_LCA1.fse = jarray('int', [Code02_LCA1.MAXN, 3])
Code02_LCA1.stacksize = jcast('int', 0)
Code02_LCA1.first = jcast('int', 0)
Code02_LCA1.second = jcast('int', 0)
Code02_LCA1.edge = jcast('int', 0)

if __name__ == '__main__':
    Code02_LCA1.main([])
