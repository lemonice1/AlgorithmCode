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

# 遥远的国度，Python版
# 一共有n个节点，给定n-1条边，节点连成一棵树，给定树的初始头节点，给定每个点的点权
# 一共有m条操作，每种操作是如下3种类型中的一种
# 操作 1 x     : 树的头节点变成x，整棵树需要重新组织
# 操作 2 x y v : x到y的路径上，所有节点的值改成v
# 操作 3 x     : 在当前树的状态下，打印u的子树中的最小值
# 1 <= n、m <= 10^5
# 任何时候节点值一定是正数
# 测试链接 : https://www.luogu.com.cn/problem/P3979
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_FarAway1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'arr': 'arr', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'dfn': 'dfn', 'seg': 'seg', 'cntd': 'cntd', 'min': 'min', 'change': 'change', 'fse': 'fse', 'stacksize': 'stacksize', 'first': 'first', 'second': 'second', 'edge': 'edge'}
    MAXN = 0
    n = 0
    m = 0
    arr = None
    head = None
    next = None
    to = None
    cntg = 0
    fa = None
    dep = None
    siz = None
    son = None
    top = None
    dfn = None
    seg = None
    cntd = 0
    min = None
    # 重置操作的懒更新信息
    # 因为题目说了，任何时候节点值一定是正数
    # change[i] == 0，表示没有重置懒更新
    # change[i] != 0，表示范围内的数字修改为change[i]
    change = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_FarAway1.next, ((_java_obj_1 := Code07_FarAway1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_FarAway1.head[u])
        Code07_FarAway1.to[Code07_FarAway1.cntg] = jcast('int', v)
        Code07_FarAway1.head[u] = jcast('int', Code07_FarAway1.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code07_FarAway1.fa[u] = jcast('int', f)
        Code07_FarAway1.dep[u] = jcast('int', jcast('int', jadd(Code07_FarAway1.dep[f], 1)))
        Code07_FarAway1.siz[u] = jcast('int', 1)
        e = jcast('int', Code07_FarAway1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code07_FarAway1.to[e])
            if (v != f):
                Code07_FarAway1.dfs1(v, u)
            e = jcast('int', Code07_FarAway1.next[e])
        e = jcast('int', Code07_FarAway1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code07_FarAway1.to[e])
            if (v != f):
                Code07_FarAway1.siz[u] = jcast('int', jcast('int', jadd(Code07_FarAway1.siz[u], Code07_FarAway1.siz[v])))
                if ((Code07_FarAway1.son[u] == 0) or (Code07_FarAway1.siz[Code07_FarAway1.son[u]] < Code07_FarAway1.siz[v])):
                    Code07_FarAway1.son[u] = jcast('int', v)
            e = jcast('int', Code07_FarAway1.next[e])

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code07_FarAway1.top[u] = jcast('int', t)
        jset(Code07_FarAway1.dfn, u, ((_java_obj_4 := Code07_FarAway1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code07_FarAway1.seg[Code07_FarAway1.cntd] = jcast('int', u)
        if (Code07_FarAway1.son[u] == 0):
            return
        Code07_FarAway1.dfs2(Code07_FarAway1.son[u], t)
        e = jcast('int', Code07_FarAway1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code07_FarAway1.to[e])
            if ((v != Code07_FarAway1.fa[u]) and (v != Code07_FarAway1.son[u])):
                Code07_FarAway1.dfs2(v, v)
            e = jcast('int', Code07_FarAway1.next[e])

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
        jset(Code07_FarAway1.fse[Code07_FarAway1.stacksize], 0, fir)
        jset(Code07_FarAway1.fse[Code07_FarAway1.stacksize], 1, sec)
        jset(Code07_FarAway1.fse[Code07_FarAway1.stacksize], 2, edg)
        Code07_FarAway1.stacksize = jcast('int', (Code07_FarAway1.stacksize + 1))

    @staticmethod
    def pop():
        Code07_FarAway1.stacksize = jcast('int', (Code07_FarAway1.stacksize - 1))
        Code07_FarAway1.first = jcast('int', Code07_FarAway1.fse[Code07_FarAway1.stacksize][0])
        Code07_FarAway1.second = jcast('int', Code07_FarAway1.fse[Code07_FarAway1.stacksize][1])
        Code07_FarAway1.edge = jcast('int', Code07_FarAway1.fse[Code07_FarAway1.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs3():
        Code07_FarAway1.stacksize = jcast('int', 0)
        Code07_FarAway1.push(1, 0, jcast('int', (-1)))
        while (Code07_FarAway1.stacksize > 0):
            Code07_FarAway1.pop()
            if (Code07_FarAway1.edge == jcast('int', (-1))):
                Code07_FarAway1.fa[Code07_FarAway1.first] = jcast('int', Code07_FarAway1.second)
                Code07_FarAway1.dep[Code07_FarAway1.first] = jcast('int', jcast('int', jadd(Code07_FarAway1.dep[Code07_FarAway1.second], 1)))
                Code07_FarAway1.siz[Code07_FarAway1.first] = jcast('int', 1)
                Code07_FarAway1.edge = jcast('int', Code07_FarAway1.head[Code07_FarAway1.first])
            else:
                Code07_FarAway1.edge = jcast('int', Code07_FarAway1.next[Code07_FarAway1.edge])
            if (Code07_FarAway1.edge != 0):
                Code07_FarAway1.push(Code07_FarAway1.first, Code07_FarAway1.second, Code07_FarAway1.edge)
                if (Code07_FarAway1.to[Code07_FarAway1.edge] != Code07_FarAway1.second):
                    Code07_FarAway1.push(Code07_FarAway1.to[Code07_FarAway1.edge], Code07_FarAway1.first, jcast('int', (-1)))
            else:
                e = jcast('int', Code07_FarAway1.head[Code07_FarAway1.first])
                v = 0
                while (e > 0):
                    v = jcast('int', Code07_FarAway1.to[e])
                    if (v != Code07_FarAway1.second):
                        Code07_FarAway1.siz[Code07_FarAway1.first] = jcast('int', jcast('int', jadd(Code07_FarAway1.siz[Code07_FarAway1.first], Code07_FarAway1.siz[v])))
                        if ((Code07_FarAway1.son[Code07_FarAway1.first] == 0) or (Code07_FarAway1.siz[Code07_FarAway1.son[Code07_FarAway1.first]] < Code07_FarAway1.siz[v])):
                            Code07_FarAway1.son[Code07_FarAway1.first] = jcast('int', v)
                    e = jcast('int', Code07_FarAway1.next[e])

    # dfs2的迭代版
    @staticmethod
    def dfs4():
        Code07_FarAway1.stacksize = jcast('int', 0)
        Code07_FarAway1.push(1, 1, jcast('int', (-1)))
        while (Code07_FarAway1.stacksize > 0):
            try:
                Code07_FarAway1.pop()
                # edge == -1，表示第一次来到当前节点，并且先处理重儿子
                if (Code07_FarAway1.edge == jcast('int', (-1))):
                    Code07_FarAway1.top[Code07_FarAway1.first] = jcast('int', Code07_FarAway1.second)
                    jset(Code07_FarAway1.dfn, Code07_FarAway1.first, ((_java_obj_8 := Code07_FarAway1), (_java_key_9 := 'cntd'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3])
                    Code07_FarAway1.seg[Code07_FarAway1.cntd] = jcast('int', Code07_FarAway1.first)
                    if (Code07_FarAway1.son[Code07_FarAway1.first] == 0):
                        raise JContinue(None)
                    Code07_FarAway1.push(Code07_FarAway1.first, Code07_FarAway1.second, jcast('int', (-2)))
                    Code07_FarAway1.push(Code07_FarAway1.son[Code07_FarAway1.first], Code07_FarAway1.second, jcast('int', (-1)))
                    raise JContinue(None)
                    # edge == -2，表示处理完当前节点的重儿子，回到了当前节点
                else:
                    if (Code07_FarAway1.edge == jcast('int', (-2))):
                        Code07_FarAway1.edge = jcast('int', Code07_FarAway1.head[Code07_FarAway1.first])
                        # edge >= 0, 继续处理其他的边
                    else:
                        Code07_FarAway1.edge = jcast('int', Code07_FarAway1.next[Code07_FarAway1.edge])
                if (Code07_FarAway1.edge != 0):
                    Code07_FarAway1.push(Code07_FarAway1.first, Code07_FarAway1.second, Code07_FarAway1.edge)
                    if ((Code07_FarAway1.to[Code07_FarAway1.edge] != Code07_FarAway1.fa[Code07_FarAway1.first]) and (Code07_FarAway1.to[Code07_FarAway1.edge] != Code07_FarAway1.son[Code07_FarAway1.first])):
                        Code07_FarAway1.push(Code07_FarAway1.to[Code07_FarAway1.edge], Code07_FarAway1.to[Code07_FarAway1.edge], jcast('int', (-1)))
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
        jset(Code07_FarAway1.min, i, jstatic('Math', 'min', Code07_FarAway1.min[jcast('int', (i << (1 & 31)))], Code07_FarAway1.min[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))

    @staticmethod
    def lazy(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        Code07_FarAway1.min[i] = jcast('int', v)
        Code07_FarAway1.change[i] = jcast('int', v)

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if (Code07_FarAway1.change[i] != 0):
            Code07_FarAway1.lazy(jcast('int', (i << (1 & 31))), Code07_FarAway1.change[i])
            Code07_FarAway1.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code07_FarAway1.change[i])
            Code07_FarAway1.change[i] = jcast('int', 0)

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code07_FarAway1.min[i] = jcast('int', Code07_FarAway1.arr[Code07_FarAway1.seg[l]])
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            Code07_FarAway1.build(l, mid, jcast('int', (i << (1 & 31))))
            Code07_FarAway1.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code07_FarAway1.up(i)

    @staticmethod
    def update(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code07_FarAway1.lazy(i, jobv)
        else:
            Code07_FarAway1.down(i)
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobl <= mid):
                Code07_FarAway1.update(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code07_FarAway1.update(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code07_FarAway1.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code07_FarAway1.min[i])
        Code07_FarAway1.down(i)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        if (jobl <= mid):
            ans = jcast('int', jstatic('Math', 'min', ans, Code07_FarAway1.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('int', jstatic('Math', 'min', ans, Code07_FarAway1.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('int', ans)

    @staticmethod
    def pathUpdate(x, y, v):
        x = jcast('int', x)
        y = jcast('int', y)
        v = jcast('int', v)
        while (Code07_FarAway1.top[x] != Code07_FarAway1.top[y]):
            if (Code07_FarAway1.dep[Code07_FarAway1.top[x]] <= Code07_FarAway1.dep[Code07_FarAway1.top[y]]):
                Code07_FarAway1.update(Code07_FarAway1.dfn[Code07_FarAway1.top[y]], Code07_FarAway1.dfn[y], v, 1, Code07_FarAway1.n, 1)
                y = jcast('int', Code07_FarAway1.fa[Code07_FarAway1.top[y]])
            else:
                Code07_FarAway1.update(Code07_FarAway1.dfn[Code07_FarAway1.top[x]], Code07_FarAway1.dfn[x], v, 1, Code07_FarAway1.n, 1)
                x = jcast('int', Code07_FarAway1.fa[Code07_FarAway1.top[x]])
        Code07_FarAway1.update(jstatic('Math', 'min', Code07_FarAway1.dfn[x], Code07_FarAway1.dfn[y]), jstatic('Math', 'max', Code07_FarAway1.dfn[x], Code07_FarAway1.dfn[y]), v, 1, Code07_FarAway1.n, 1)

    # 已知root一定在u的子树上
    # 找到u哪个儿子的子树里有root，返回那个儿子的编号
    @staticmethod
    def findSon(root, u):
        root = jcast('int', root)
        u = jcast('int', u)
        while (Code07_FarAway1.top[root] != Code07_FarAway1.top[u]):
            if (Code07_FarAway1.fa[Code07_FarAway1.top[root]] == u):
                return jcast('int', Code07_FarAway1.top[root])
            root = jcast('int', Code07_FarAway1.fa[Code07_FarAway1.top[root]])
        return jcast('int', Code07_FarAway1.son[u])

    # 假设树的头节点变成root，在当前树的状态下，查询u的子树中的最小值
    @staticmethod
    def treeQuery(root, u):
        root = jcast('int', root)
        u = jcast('int', u)
        if (root == u):
            return jcast('int', Code07_FarAway1.min[1])
        else:
            if ((Code07_FarAway1.dfn[root] < Code07_FarAway1.dfn[u]) or (jcast('int', jadd(Code07_FarAway1.dfn[u], Code07_FarAway1.siz[u])) <= Code07_FarAway1.dfn[root])):
                return jcast('int', Code07_FarAway1.query(Code07_FarAway1.dfn[u], jcast('int', (jcast('int', jadd(Code07_FarAway1.dfn[u], Code07_FarAway1.siz[u])) - 1)), 1, Code07_FarAway1.n, 1))
            else:
                uson = jcast('int', Code07_FarAway1.findSon(root, u))
                ans = jcast('int', Code07_FarAway1.query(1, jcast('int', (Code07_FarAway1.dfn[uson] - 1)), 1, Code07_FarAway1.n, 1))
                if (jcast('int', jadd(Code07_FarAway1.dfn[uson], Code07_FarAway1.siz[uson])) <= Code07_FarAway1.n):
                    ans = jcast('int', jstatic('Math', 'min', ans, Code07_FarAway1.query(jcast('int', jadd(Code07_FarAway1.dfn[uson], Code07_FarAway1.siz[uson])), Code07_FarAway1.n, 1, Code07_FarAway1.n, 1)))
                return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code07_FarAway1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code07_FarAway1.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code07_FarAway1.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code07_FarAway1.addEdge(u, v)
            Code07_FarAway1.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_FarAway1.n):
            jcall(in_, 'nextToken')
            Code07_FarAway1.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        # dfs3() 等同于 dfs1(1, 0)，调用迭代版防止爆栈
        Code07_FarAway1.dfs3()
        # dfs4() 等同于 dfs2(1, 1)，调用迭代版防止爆栈
        Code07_FarAway1.dfs4()
        Code07_FarAway1.build(1, Code07_FarAway1.n, 1)
        jcall(in_, 'nextToken')
        root = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        v = 0
        while (i <= Code07_FarAway1.m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            if (op == 1):
                jcall(in_, 'nextToken')
                root = jcast('int', jcast('int', jget(in_, 'nval')))
            else:
                if (op == 2):
                    jcall(in_, 'nextToken')
                    x = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    y = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    v = jcast('int', jcast('int', jget(in_, 'nval')))
                    Code07_FarAway1.pathUpdate(x, y, v)
                else:
                    jcall(in_, 'nextToken')
                    x = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(out, 'println', Code07_FarAway1.treeQuery(root, x))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_FarAway1.MAXN = jcast('int', 100001)
Code07_FarAway1.n = jcast('int', 0)
Code07_FarAway1.m = jcast('int', 0)
Code07_FarAway1.arr = jarray('int', [Code07_FarAway1.MAXN])
Code07_FarAway1.head = jarray('int', [Code07_FarAway1.MAXN])
Code07_FarAway1.next = jarray('int', [jcast('int', (Code07_FarAway1.MAXN << (1 & 31)))])
Code07_FarAway1.to = jarray('int', [jcast('int', (Code07_FarAway1.MAXN << (1 & 31)))])
Code07_FarAway1.cntg = jcast('int', 0)
Code07_FarAway1.fa = jarray('int', [Code07_FarAway1.MAXN])
Code07_FarAway1.dep = jarray('int', [Code07_FarAway1.MAXN])
Code07_FarAway1.siz = jarray('int', [Code07_FarAway1.MAXN])
Code07_FarAway1.son = jarray('int', [Code07_FarAway1.MAXN])
Code07_FarAway1.top = jarray('int', [Code07_FarAway1.MAXN])
Code07_FarAway1.dfn = jarray('int', [Code07_FarAway1.MAXN])
Code07_FarAway1.seg = jarray('int', [Code07_FarAway1.MAXN])
Code07_FarAway1.cntd = jcast('int', 0)
Code07_FarAway1.min = jarray('int', [jcast('int', (Code07_FarAway1.MAXN << (2 & 31)))])
Code07_FarAway1.change = jarray('int', [jcast('int', (Code07_FarAway1.MAXN << (2 & 31)))])
Code07_FarAway1.fse = jarray('int', [Code07_FarAway1.MAXN, 3])
Code07_FarAway1.stacksize = jcast('int', 0)
Code07_FarAway1.first = jcast('int', 0)
Code07_FarAway1.second = jcast('int', 0)
Code07_FarAway1.edge = jcast('int', 0)

if __name__ == '__main__':
    Code07_FarAway1.main([])
