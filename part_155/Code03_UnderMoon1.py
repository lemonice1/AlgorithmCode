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

# 月下毛景树，Python版
# 一共有n个节点，节点编号从1到n，所有节点连成一棵树
# 给定n-1条边，边的编号从1到n-1，每条边给定初始边权
# 会进行若干次操作，每条操作的类型是如下4种类型中的一种
# 操作 Change x v  : 第x条边的边权改成v
# 操作 Cover x y v : x号点到y号点的路径上，所有边权改成v
# 操作 Add x y v   : x号点到y号点的路径上，所有边权增加v
# 操作 Max x y     : x号点到y号点的路径上，打印最大的边权
# 1 <= n <= 10^5
# 任何时候的边权 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P4315
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_UnderMoon1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'arr': 'arr', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'dfn': 'dfn', 'cntd': 'cntd', 'max': 'max', 'addTag': 'addTag', 'updateTag': 'updateTag', 'change': 'change', 'fse': 'fse', 'stacksize': 'stacksize', 'first': 'first', 'second': 'second', 'edge': 'edge'}
    MAXN = 0
    n = 0
    arr = None
    # 链式前向星
    head = None
    next = None
    to = None
    cntg = 0
    # 重链剖分
    fa = None
    dep = None
    siz = None
    son = None
    top = None
    dfn = None
    cntd = 0
    # 线段树查询区间最大值
    # 但是需要同时兼顾，区间增加、区间重置，这两种操作
    # 那么就牵扯到两种操作相互影响的问题
    # 因为区间重置操作会取消之前的区间增加操作
    # 讲解110，线段树章节，题目5、题目6，重点讲了这种线段树
    # 不会的同学可以看看，讲的非常清楚
    max = None
    addTag = None
    updateTag = None
    change = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_UnderMoon1.next, ((_java_obj_1 := Code03_UnderMoon1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_UnderMoon1.head[u])
        Code03_UnderMoon1.to[Code03_UnderMoon1.cntg] = jcast('int', v)
        Code03_UnderMoon1.head[u] = jcast('int', Code03_UnderMoon1.cntg)

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code03_UnderMoon1.fa[u] = jcast('int', f)
        Code03_UnderMoon1.dep[u] = jcast('int', jcast('int', jadd(Code03_UnderMoon1.dep[f], 1)))
        Code03_UnderMoon1.siz[u] = jcast('int', 1)
        e = jcast('int', Code03_UnderMoon1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code03_UnderMoon1.to[e])
            if (v != f):
                Code03_UnderMoon1.dfs1(v, u)
            e = jcast('int', Code03_UnderMoon1.next[e])
        e = jcast('int', Code03_UnderMoon1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code03_UnderMoon1.to[e])
            if (v != f):
                Code03_UnderMoon1.siz[u] = jcast('int', jcast('int', jadd(Code03_UnderMoon1.siz[u], Code03_UnderMoon1.siz[v])))
                if ((Code03_UnderMoon1.son[u] == 0) or (Code03_UnderMoon1.siz[Code03_UnderMoon1.son[u]] < Code03_UnderMoon1.siz[v])):
                    Code03_UnderMoon1.son[u] = jcast('int', v)
            e = jcast('int', Code03_UnderMoon1.next[e])

    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code03_UnderMoon1.top[u] = jcast('int', t)
        jset(Code03_UnderMoon1.dfn, u, ((_java_obj_4 := Code03_UnderMoon1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        if (Code03_UnderMoon1.son[u] == 0):
            return
        Code03_UnderMoon1.dfs2(Code03_UnderMoon1.son[u], t)
        e = jcast('int', Code03_UnderMoon1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code03_UnderMoon1.to[e])
            if ((v != Code03_UnderMoon1.fa[u]) and (v != Code03_UnderMoon1.son[u])):
                Code03_UnderMoon1.dfs2(v, v)
            e = jcast('int', Code03_UnderMoon1.next[e])

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
        jset(Code03_UnderMoon1.fse[Code03_UnderMoon1.stacksize], 0, fir)
        jset(Code03_UnderMoon1.fse[Code03_UnderMoon1.stacksize], 1, sec)
        jset(Code03_UnderMoon1.fse[Code03_UnderMoon1.stacksize], 2, edg)
        Code03_UnderMoon1.stacksize = jcast('int', (Code03_UnderMoon1.stacksize + 1))

    @staticmethod
    def pop():
        Code03_UnderMoon1.stacksize = jcast('int', (Code03_UnderMoon1.stacksize - 1))
        Code03_UnderMoon1.first = jcast('int', Code03_UnderMoon1.fse[Code03_UnderMoon1.stacksize][0])
        Code03_UnderMoon1.second = jcast('int', Code03_UnderMoon1.fse[Code03_UnderMoon1.stacksize][1])
        Code03_UnderMoon1.edge = jcast('int', Code03_UnderMoon1.fse[Code03_UnderMoon1.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs3():
        Code03_UnderMoon1.stacksize = jcast('int', 0)
        Code03_UnderMoon1.push(1, 0, jcast('int', (-1)))
        while (Code03_UnderMoon1.stacksize > 0):
            Code03_UnderMoon1.pop()
            if (Code03_UnderMoon1.edge == jcast('int', (-1))):
                Code03_UnderMoon1.fa[Code03_UnderMoon1.first] = jcast('int', Code03_UnderMoon1.second)
                Code03_UnderMoon1.dep[Code03_UnderMoon1.first] = jcast('int', jcast('int', jadd(Code03_UnderMoon1.dep[Code03_UnderMoon1.second], 1)))
                Code03_UnderMoon1.siz[Code03_UnderMoon1.first] = jcast('int', 1)
                Code03_UnderMoon1.edge = jcast('int', Code03_UnderMoon1.head[Code03_UnderMoon1.first])
            else:
                Code03_UnderMoon1.edge = jcast('int', Code03_UnderMoon1.next[Code03_UnderMoon1.edge])
            if (Code03_UnderMoon1.edge != 0):
                Code03_UnderMoon1.push(Code03_UnderMoon1.first, Code03_UnderMoon1.second, Code03_UnderMoon1.edge)
                if (Code03_UnderMoon1.to[Code03_UnderMoon1.edge] != Code03_UnderMoon1.second):
                    Code03_UnderMoon1.push(Code03_UnderMoon1.to[Code03_UnderMoon1.edge], Code03_UnderMoon1.first, jcast('int', (-1)))
            else:
                e = jcast('int', Code03_UnderMoon1.head[Code03_UnderMoon1.first])
                v = 0
                while (e > 0):
                    v = jcast('int', Code03_UnderMoon1.to[e])
                    if (v != Code03_UnderMoon1.second):
                        Code03_UnderMoon1.siz[Code03_UnderMoon1.first] = jcast('int', jcast('int', jadd(Code03_UnderMoon1.siz[Code03_UnderMoon1.first], Code03_UnderMoon1.siz[v])))
                        if ((Code03_UnderMoon1.son[Code03_UnderMoon1.first] == 0) or (Code03_UnderMoon1.siz[Code03_UnderMoon1.son[Code03_UnderMoon1.first]] < Code03_UnderMoon1.siz[v])):
                            Code03_UnderMoon1.son[Code03_UnderMoon1.first] = jcast('int', v)
                    e = jcast('int', Code03_UnderMoon1.next[e])

    # dfs2的迭代版
    @staticmethod
    def dfs4():
        Code03_UnderMoon1.stacksize = jcast('int', 0)
        Code03_UnderMoon1.push(1, 1, jcast('int', (-1)))
        while (Code03_UnderMoon1.stacksize > 0):
            try:
                Code03_UnderMoon1.pop()
                if (Code03_UnderMoon1.edge == jcast('int', (-1))):
                    Code03_UnderMoon1.top[Code03_UnderMoon1.first] = jcast('int', Code03_UnderMoon1.second)
                    jset(Code03_UnderMoon1.dfn, Code03_UnderMoon1.first, ((_java_obj_8 := Code03_UnderMoon1), (_java_key_9 := 'cntd'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3])
                    if (Code03_UnderMoon1.son[Code03_UnderMoon1.first] == 0):
                        raise JContinue(None)
                    Code03_UnderMoon1.push(Code03_UnderMoon1.first, Code03_UnderMoon1.second, jcast('int', (-2)))
                    Code03_UnderMoon1.push(Code03_UnderMoon1.son[Code03_UnderMoon1.first], Code03_UnderMoon1.second, jcast('int', (-1)))
                    raise JContinue(None)
                else:
                    if (Code03_UnderMoon1.edge == jcast('int', (-2))):
                        Code03_UnderMoon1.edge = jcast('int', Code03_UnderMoon1.head[Code03_UnderMoon1.first])
                    else:
                        Code03_UnderMoon1.edge = jcast('int', Code03_UnderMoon1.next[Code03_UnderMoon1.edge])
                if (Code03_UnderMoon1.edge != 0):
                    Code03_UnderMoon1.push(Code03_UnderMoon1.first, Code03_UnderMoon1.second, Code03_UnderMoon1.edge)
                    if ((Code03_UnderMoon1.to[Code03_UnderMoon1.edge] != Code03_UnderMoon1.fa[Code03_UnderMoon1.first]) and (Code03_UnderMoon1.to[Code03_UnderMoon1.edge] != Code03_UnderMoon1.son[Code03_UnderMoon1.first])):
                        Code03_UnderMoon1.push(Code03_UnderMoon1.to[Code03_UnderMoon1.edge], Code03_UnderMoon1.to[Code03_UnderMoon1.edge], jcast('int', (-1)))
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break

    @staticmethod
    def up(i):
        i = jcast('int', i)
        jset(Code03_UnderMoon1.max, i, jstatic('Math', 'max', Code03_UnderMoon1.max[jcast('int', (i << (1 & 31)))], Code03_UnderMoon1.max[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))

    @staticmethod
    def addLazy(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        Code03_UnderMoon1.max[i] = jcast('int', jcast('int', jadd(Code03_UnderMoon1.max[i], v)))
        Code03_UnderMoon1.addTag[i] = jcast('int', jcast('int', jadd(Code03_UnderMoon1.addTag[i], v)))

    @staticmethod
    def updateLazy(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        Code03_UnderMoon1.max[i] = jcast('int', v)
        Code03_UnderMoon1.addTag[i] = jcast('int', 0)
        Code03_UnderMoon1.updateTag[i] = jcast('boolean', True)
        Code03_UnderMoon1.change[i] = jcast('int', v)

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if Code03_UnderMoon1.updateTag[i]:
            Code03_UnderMoon1.updateLazy(jcast('int', (i << (1 & 31))), Code03_UnderMoon1.change[i])
            Code03_UnderMoon1.updateLazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code03_UnderMoon1.change[i])
            Code03_UnderMoon1.updateTag[i] = jcast('boolean', False)
        if (Code03_UnderMoon1.addTag[i] != 0):
            Code03_UnderMoon1.addLazy(jcast('int', (i << (1 & 31))), Code03_UnderMoon1.addTag[i])
            Code03_UnderMoon1.addLazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code03_UnderMoon1.addTag[i])
            Code03_UnderMoon1.addTag[i] = jcast('int', 0)

    @staticmethod
    def update(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code03_UnderMoon1.updateLazy(i, jobv)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code03_UnderMoon1.down(i)
            if (jobl <= mid):
                Code03_UnderMoon1.update(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code03_UnderMoon1.update(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code03_UnderMoon1.up(i)

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code03_UnderMoon1.addLazy(i, jobv)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code03_UnderMoon1.down(i)
            if (jobl <= mid):
                Code03_UnderMoon1.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code03_UnderMoon1.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code03_UnderMoon1.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code03_UnderMoon1.max[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        Code03_UnderMoon1.down(i)
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        if (jobl <= mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code03_UnderMoon1.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code03_UnderMoon1.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('int', ans)

    @staticmethod
    def edgeUpdate(ei, val):
        ei = jcast('int', ei)
        val = jcast('int', val)
        x = jcast('int', Code03_UnderMoon1.arr[ei][0])
        y = jcast('int', Code03_UnderMoon1.arr[ei][1])
        down = jcast('int', jstatic('Math', 'max', Code03_UnderMoon1.dfn[x], Code03_UnderMoon1.dfn[y]))
        Code03_UnderMoon1.update(down, down, val, 1, Code03_UnderMoon1.n, 1)

    @staticmethod
    def pathUpdate(x, y, v):
        x = jcast('int', x)
        y = jcast('int', y)
        v = jcast('int', v)
        while (Code03_UnderMoon1.top[x] != Code03_UnderMoon1.top[y]):
            if (Code03_UnderMoon1.dep[Code03_UnderMoon1.top[x]] <= Code03_UnderMoon1.dep[Code03_UnderMoon1.top[y]]):
                Code03_UnderMoon1.update(Code03_UnderMoon1.dfn[Code03_UnderMoon1.top[y]], Code03_UnderMoon1.dfn[y], v, 1, Code03_UnderMoon1.n, 1)
                y = jcast('int', Code03_UnderMoon1.fa[Code03_UnderMoon1.top[y]])
            else:
                Code03_UnderMoon1.update(Code03_UnderMoon1.dfn[Code03_UnderMoon1.top[x]], Code03_UnderMoon1.dfn[x], v, 1, Code03_UnderMoon1.n, 1)
                x = jcast('int', Code03_UnderMoon1.fa[Code03_UnderMoon1.top[x]])
        Code03_UnderMoon1.update(jcast('int', jadd(jstatic('Math', 'min', Code03_UnderMoon1.dfn[x], Code03_UnderMoon1.dfn[y]), 1)), jstatic('Math', 'max', Code03_UnderMoon1.dfn[x], Code03_UnderMoon1.dfn[y]), v, 1, Code03_UnderMoon1.n, 1)

    @staticmethod
    def pathAdd(x, y, v):
        x = jcast('int', x)
        y = jcast('int', y)
        v = jcast('int', v)
        while (Code03_UnderMoon1.top[x] != Code03_UnderMoon1.top[y]):
            if (Code03_UnderMoon1.dep[Code03_UnderMoon1.top[x]] <= Code03_UnderMoon1.dep[Code03_UnderMoon1.top[y]]):
                Code03_UnderMoon1.add(Code03_UnderMoon1.dfn[Code03_UnderMoon1.top[y]], Code03_UnderMoon1.dfn[y], v, 1, Code03_UnderMoon1.n, 1)
                y = jcast('int', Code03_UnderMoon1.fa[Code03_UnderMoon1.top[y]])
            else:
                Code03_UnderMoon1.add(Code03_UnderMoon1.dfn[Code03_UnderMoon1.top[x]], Code03_UnderMoon1.dfn[x], v, 1, Code03_UnderMoon1.n, 1)
                x = jcast('int', Code03_UnderMoon1.fa[Code03_UnderMoon1.top[x]])
        Code03_UnderMoon1.add(jcast('int', jadd(jstatic('Math', 'min', Code03_UnderMoon1.dfn[x], Code03_UnderMoon1.dfn[y]), 1)), jstatic('Math', 'max', Code03_UnderMoon1.dfn[x], Code03_UnderMoon1.dfn[y]), v, 1, Code03_UnderMoon1.n, 1)

    @staticmethod
    def pathMax(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        while (Code03_UnderMoon1.top[x] != Code03_UnderMoon1.top[y]):
            if (Code03_UnderMoon1.dep[Code03_UnderMoon1.top[x]] <= Code03_UnderMoon1.dep[Code03_UnderMoon1.top[y]]):
                ans = jcast('int', jstatic('Math', 'max', ans, Code03_UnderMoon1.query(Code03_UnderMoon1.dfn[Code03_UnderMoon1.top[y]], Code03_UnderMoon1.dfn[y], 1, Code03_UnderMoon1.n, 1)))
                y = jcast('int', Code03_UnderMoon1.fa[Code03_UnderMoon1.top[y]])
            else:
                ans = jcast('int', jstatic('Math', 'max', ans, Code03_UnderMoon1.query(Code03_UnderMoon1.dfn[Code03_UnderMoon1.top[x]], Code03_UnderMoon1.dfn[x], 1, Code03_UnderMoon1.n, 1)))
                x = jcast('int', Code03_UnderMoon1.fa[Code03_UnderMoon1.top[x]])
        ans = jcast('int', jstatic('Math', 'max', ans, Code03_UnderMoon1.query(jcast('int', jadd(jstatic('Math', 'min', Code03_UnderMoon1.dfn[x], Code03_UnderMoon1.dfn[y]), 1)), jstatic('Math', 'max', Code03_UnderMoon1.dfn[x], Code03_UnderMoon1.dfn[y]), 1, Code03_UnderMoon1.n, 1)))
        return jcast('int', ans)

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i < Code03_UnderMoon1.n):
            Code03_UnderMoon1.addEdge(Code03_UnderMoon1.arr[i][0], Code03_UnderMoon1.arr[i][1])
            Code03_UnderMoon1.addEdge(Code03_UnderMoon1.arr[i][1], Code03_UnderMoon1.arr[i][0])
            i = jcast('int', (i + 1))
        Code03_UnderMoon1.dfs3()
        Code03_UnderMoon1.dfs4()
        i = jcast('int', 1)
        while (i < Code03_UnderMoon1.n):
            Code03_UnderMoon1.edgeUpdate(i, Code03_UnderMoon1.arr[i][2])
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        io = Code03_UnderMoon1.Kattio(_java_ctor=0)
        Code03_UnderMoon1.n = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i < Code03_UnderMoon1.n):
            jset(Code03_UnderMoon1.arr[i], 0, jcall(io, 'nextInt'))
            jset(Code03_UnderMoon1.arr[i], 1, jcall(io, 'nextInt'))
            jset(Code03_UnderMoon1.arr[i], 2, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        Code03_UnderMoon1.prepare()
        op = jcall(io, 'next')
        x = 0
        y = 0
        v = 0
        while (not jcall(op, 'equals', 'Stop')):
            if jcall(op, 'equals', 'Change'):
                x = jcast('int', jcall(io, 'nextInt'))
                v = jcast('int', jcall(io, 'nextInt'))
                Code03_UnderMoon1.edgeUpdate(x, v)
            else:
                if jcall(op, 'equals', 'Cover'):
                    x = jcast('int', jcall(io, 'nextInt'))
                    y = jcast('int', jcall(io, 'nextInt'))
                    v = jcast('int', jcall(io, 'nextInt'))
                    Code03_UnderMoon1.pathUpdate(x, y, v)
                else:
                    if jcall(op, 'equals', 'Add'):
                        x = jcast('int', jcall(io, 'nextInt'))
                        y = jcast('int', jcall(io, 'nextInt'))
                        v = jcast('int', jcall(io, 'nextInt'))
                        Code03_UnderMoon1.pathAdd(x, y, v)
                    else:
                        x = jcast('int', jcall(io, 'nextInt'))
                        y = jcast('int', jcall(io, 'nextInt'))
                        jcall(io, 'println', Code03_UnderMoon1.pathMax(x, y))
            op = jcall(io, 'next')
        jcall(io, 'flush')
        jcall(io, 'close')

    # 读写工具类
    class Kattio(jclass('PrintWriter')):
        __java_fields__ = {'r': 'r', 'st': 'st'}
        # r：实例字段，在构造函数中初始化。
        # st：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self._java_init_1(jget(System, 'in'), jget(System, 'out'))

        def _java_init_1(self, i, o):
            super().__init__(o)
            self.r = jnew('BufferedReader', jnew('InputStreamReader', i))

        def _java_init_2(self, intput, output):
            super().__init__(output)
            self.r = jnew('BufferedReader', jnew('FileReader', intput))

        def next(self):
            try:
                while ((self.st == None) or (not jcall(self.st, 'hasMoreTokens'))):
                    self.st = jnew('StringTokenizer', jcall(self.r, 'readLine'))
                return jcall(self.st, 'nextToken')
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_11:
                if jinstanceof(_java_exception_11, 'Exception'):
                    e = _java_exception_11
                    None
                else:
                    raise
            return None

        def nextInt(self):
            return jcast('int', jstatic('Integer', 'parseInt', self.next()))

        def nextDouble(self):
            return jcast('double', jstatic('Double', 'parseDouble', self.next()))

        def nextLong(self):
            return jcast('long', jstatic('Long', 'parseLong', self.next()))

        def __init__(self, *args, _java_ctor=None):
            self.r = None
            self.st = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[], ['InputStream', 'OutputStream'], ['String', 'String']], [False, False, False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            if _java_choice == 1:
                return self._java_init_1(*args)
            if _java_choice == 2:
                return self._java_init_2(*args)
            raise TypeError("No matching overload for Code03_UnderMoon1.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_UnderMoon1.MAXN = jcast('int', 100001)
Code03_UnderMoon1.n = jcast('int', 0)
Code03_UnderMoon1.arr = jarray('int', [Code03_UnderMoon1.MAXN, 3])
Code03_UnderMoon1.head = jarray('int', [Code03_UnderMoon1.MAXN])
Code03_UnderMoon1.next = jarray('int', [jcast('int', (Code03_UnderMoon1.MAXN << (1 & 31)))])
Code03_UnderMoon1.to = jarray('int', [jcast('int', (Code03_UnderMoon1.MAXN << (1 & 31)))])
Code03_UnderMoon1.cntg = jcast('int', 0)
Code03_UnderMoon1.fa = jarray('int', [Code03_UnderMoon1.MAXN])
Code03_UnderMoon1.dep = jarray('int', [Code03_UnderMoon1.MAXN])
Code03_UnderMoon1.siz = jarray('int', [Code03_UnderMoon1.MAXN])
Code03_UnderMoon1.son = jarray('int', [Code03_UnderMoon1.MAXN])
Code03_UnderMoon1.top = jarray('int', [Code03_UnderMoon1.MAXN])
Code03_UnderMoon1.dfn = jarray('int', [Code03_UnderMoon1.MAXN])
Code03_UnderMoon1.cntd = jcast('int', 0)
Code03_UnderMoon1.max = jarray('int', [jcast('int', (Code03_UnderMoon1.MAXN << (2 & 31)))])
Code03_UnderMoon1.addTag = jarray('int', [jcast('int', (Code03_UnderMoon1.MAXN << (2 & 31)))])
Code03_UnderMoon1.updateTag = jarray('boolean', [jcast('int', (Code03_UnderMoon1.MAXN << (2 & 31)))])
Code03_UnderMoon1.change = jarray('int', [jcast('int', (Code03_UnderMoon1.MAXN << (2 & 31)))])
Code03_UnderMoon1.fse = jarray('int', [Code03_UnderMoon1.MAXN, 3])
Code03_UnderMoon1.stacksize = jcast('int', 0)
Code03_UnderMoon1.first = jcast('int', 0)
Code03_UnderMoon1.second = jcast('int', 0)
Code03_UnderMoon1.edge = jcast('int', 0)

if __name__ == '__main__':
    Code03_UnderMoon1.main([])
