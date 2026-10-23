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

# 重链剖分模版题，Python版
# 一共有n个节点，给定n-1条边，节点连成一棵树
# 给定每个节点的初始权值，给定树的头节点编号root
# 一共有m条操作，每种操作是如下4种类型中的一种
# 操作 1 x y v : x到y的路径上，每个节点值增加v
# 操作 2 x y   : x到y的路径上，打印所有节点值的累加和
# 操作 3 x v   : x为头的子树上，每个节点值增加v
# 操作 4 x     : x为头的子树上，打印所有节点值的累加和
# 1 <= n、m <= 10^5
# 1 <= MOD <= 2^30
# 输入的值都为int类型
# 查询操作时，打印(查询结果 % MOD)，题目会给定MOD值
# 测试链接 : https://www.luogu.com.cn/problem/P3384
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_HLD2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'root': 'root', 'MOD': 'MOD', 'arr': 'arr', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'dfn': 'dfn', 'seg': 'seg', 'cntd': 'cntd', 'sum': 'sum', 'addTag': 'addTag', 'fse': 'fse', 'stacksize': 'stacksize', 'first': 'first', 'second': 'second', 'edge': 'edge'}
    MAXN = 0
    n = 0
    m = 0
    root = 0
    MOD = 0
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
    sum = None
    addTag = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_HLD2.next, ((_java_obj_1 := Code01_HLD2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_HLD2.head[u])
        Code01_HLD2.to[Code01_HLD2.cntg] = jcast('int', v)
        Code01_HLD2.head[u] = jcast('int', Code01_HLD2.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    # 来到节点u，节点u树上的父节点是f
    # dfs1的过程去设置 fa dep siz son
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code01_HLD2.fa[u] = jcast('int', f)
        Code01_HLD2.dep[u] = jcast('int', jcast('int', jadd(Code01_HLD2.dep[f], 1)))
        Code01_HLD2.siz[u] = jcast('int', 1)
        e = jcast('int', Code01_HLD2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code01_HLD2.to[e])
            if (v != f):
                Code01_HLD2.dfs1(v, u)
            e = jcast('int', Code01_HLD2.next[e])
        e = jcast('int', Code01_HLD2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code01_HLD2.to[e])
            if (v != f):
                Code01_HLD2.siz[u] = jcast('int', jcast('int', jadd(Code01_HLD2.siz[u], Code01_HLD2.siz[v])))
                if ((Code01_HLD2.son[u] == 0) or (Code01_HLD2.siz[Code01_HLD2.son[u]] < Code01_HLD2.siz[v])):
                    Code01_HLD2.son[u] = jcast('int', v)
            e = jcast('int', Code01_HLD2.next[e])

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    # 来到节点u，节点u所在重链的头节点是t
    # dfs2的过程去设置 top dfn seg
    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code01_HLD2.top[u] = jcast('int', t)
        jset(Code01_HLD2.dfn, u, ((_java_obj_4 := Code01_HLD2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code01_HLD2.seg[Code01_HLD2.cntd] = jcast('int', u)
        if (Code01_HLD2.son[u] == 0):
            return
        Code01_HLD2.dfs2(Code01_HLD2.son[u], t)
        e = jcast('int', Code01_HLD2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code01_HLD2.to[e])
            if ((v != Code01_HLD2.fa[u]) and (v != Code01_HLD2.son[u])):
                Code01_HLD2.dfs2(v, v)
            e = jcast('int', Code01_HLD2.next[e])

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
        jset(Code01_HLD2.fse[Code01_HLD2.stacksize], 0, fir)
        jset(Code01_HLD2.fse[Code01_HLD2.stacksize], 1, sec)
        jset(Code01_HLD2.fse[Code01_HLD2.stacksize], 2, edg)
        Code01_HLD2.stacksize = jcast('int', (Code01_HLD2.stacksize + 1))

    @staticmethod
    def pop():
        Code01_HLD2.stacksize = jcast('int', (Code01_HLD2.stacksize - 1))
        Code01_HLD2.first = jcast('int', Code01_HLD2.fse[Code01_HLD2.stacksize][0])
        Code01_HLD2.second = jcast('int', Code01_HLD2.fse[Code01_HLD2.stacksize][1])
        Code01_HLD2.edge = jcast('int', Code01_HLD2.fse[Code01_HLD2.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs3():
        Code01_HLD2.stacksize = jcast('int', 0)
        Code01_HLD2.push(Code01_HLD2.root, 0, jcast('int', (-1)))
        while (Code01_HLD2.stacksize > 0):
            Code01_HLD2.pop()
            if (Code01_HLD2.edge == jcast('int', (-1))):
                Code01_HLD2.fa[Code01_HLD2.first] = jcast('int', Code01_HLD2.second)
                Code01_HLD2.dep[Code01_HLD2.first] = jcast('int', jcast('int', jadd(Code01_HLD2.dep[Code01_HLD2.second], 1)))
                Code01_HLD2.siz[Code01_HLD2.first] = jcast('int', 1)
                Code01_HLD2.edge = jcast('int', Code01_HLD2.head[Code01_HLD2.first])
            else:
                Code01_HLD2.edge = jcast('int', Code01_HLD2.next[Code01_HLD2.edge])
            if (Code01_HLD2.edge != 0):
                Code01_HLD2.push(Code01_HLD2.first, Code01_HLD2.second, Code01_HLD2.edge)
                if (Code01_HLD2.to[Code01_HLD2.edge] != Code01_HLD2.second):
                    Code01_HLD2.push(Code01_HLD2.to[Code01_HLD2.edge], Code01_HLD2.first, jcast('int', (-1)))
            else:
                e = jcast('int', Code01_HLD2.head[Code01_HLD2.first])
                v = 0
                while (e > 0):
                    v = jcast('int', Code01_HLD2.to[e])
                    if (v != Code01_HLD2.second):
                        Code01_HLD2.siz[Code01_HLD2.first] = jcast('int', jcast('int', jadd(Code01_HLD2.siz[Code01_HLD2.first], Code01_HLD2.siz[v])))
                        if ((Code01_HLD2.son[Code01_HLD2.first] == 0) or (Code01_HLD2.siz[Code01_HLD2.son[Code01_HLD2.first]] < Code01_HLD2.siz[v])):
                            Code01_HLD2.son[Code01_HLD2.first] = jcast('int', v)
                    e = jcast('int', Code01_HLD2.next[e])

    # dfs2的迭代版
    @staticmethod
    def dfs4():
        Code01_HLD2.stacksize = jcast('int', 0)
        Code01_HLD2.push(Code01_HLD2.root, Code01_HLD2.root, jcast('int', (-1)))
        while (Code01_HLD2.stacksize > 0):
            try:
                Code01_HLD2.pop()
                # edge == -1，表示第一次来到当前节点，并且先处理重儿子
                if (Code01_HLD2.edge == jcast('int', (-1))):
                    Code01_HLD2.top[Code01_HLD2.first] = jcast('int', Code01_HLD2.second)
                    jset(Code01_HLD2.dfn, Code01_HLD2.first, ((_java_obj_8 := Code01_HLD2), (_java_key_9 := 'cntd'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3])
                    Code01_HLD2.seg[Code01_HLD2.cntd] = jcast('int', Code01_HLD2.first)
                    if (Code01_HLD2.son[Code01_HLD2.first] == 0):
                        raise JContinue(None)
                    Code01_HLD2.push(Code01_HLD2.first, Code01_HLD2.second, jcast('int', (-2)))
                    Code01_HLD2.push(Code01_HLD2.son[Code01_HLD2.first], Code01_HLD2.second, jcast('int', (-1)))
                    raise JContinue(None)
                    # edge == -2，表示处理完当前节点的重儿子，回到了当前节点
                else:
                    if (Code01_HLD2.edge == jcast('int', (-2))):
                        Code01_HLD2.edge = jcast('int', Code01_HLD2.head[Code01_HLD2.first])
                        # edge >= 0, 继续处理其他的边
                    else:
                        Code01_HLD2.edge = jcast('int', Code01_HLD2.next[Code01_HLD2.edge])
                if (Code01_HLD2.edge != 0):
                    Code01_HLD2.push(Code01_HLD2.first, Code01_HLD2.second, Code01_HLD2.edge)
                    if ((Code01_HLD2.to[Code01_HLD2.edge] != Code01_HLD2.fa[Code01_HLD2.first]) and (Code01_HLD2.to[Code01_HLD2.edge] != Code01_HLD2.son[Code01_HLD2.first])):
                        Code01_HLD2.push(Code01_HLD2.to[Code01_HLD2.edge], Code01_HLD2.to[Code01_HLD2.edge], jcast('int', (-1)))
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
        Code01_HLD2.sum[i] = jcast('long', jcast('long', jmod(jcast('long', jadd(Code01_HLD2.sum[jcast('int', (i << (1 & 31)))], Code01_HLD2.sum[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])), Code01_HLD2.MOD)))

    @staticmethod
    def lazy(i, v, n):
        i = jcast('int', i)
        v = jcast('long', v)
        n = jcast('int', n)
        Code01_HLD2.sum[i] = jcast('long', jcast('long', jmod(jcast('long', jadd(Code01_HLD2.sum[i], jcast('long', (v * n)))), Code01_HLD2.MOD)))
        Code01_HLD2.addTag[i] = jcast('long', jcast('long', jmod(jcast('long', jadd(Code01_HLD2.addTag[i], v)), Code01_HLD2.MOD)))

    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        if (Code01_HLD2.addTag[i] != 0):
            Code01_HLD2.lazy(jcast('int', (i << (1 & 31))), Code01_HLD2.addTag[i], ln)
            Code01_HLD2.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code01_HLD2.addTag[i], rn)
            Code01_HLD2.addTag[i] = jcast('long', 0)

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code01_HLD2.sum[i] = jcast('long', jcast('int', jmod(Code01_HLD2.arr[Code01_HLD2.seg[l]], Code01_HLD2.MOD)))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            Code01_HLD2.build(l, mid, jcast('int', (i << (1 & 31))))
            Code01_HLD2.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code01_HLD2.up(i)

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code01_HLD2.lazy(i, jobv, jcast('int', jadd(jcast('int', (r - l)), 1)))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            Code01_HLD2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code01_HLD2.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code01_HLD2.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code01_HLD2.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code01_HLD2.sum[i])
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code01_HLD2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
        ans = jcast('long', 0)
        if (jobl <= mid):
            ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, Code01_HLD2.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))), Code01_HLD2.MOD)))
        if (jobr > mid):
            ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, Code01_HLD2.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))), Code01_HLD2.MOD)))
        return jcast('long', ans)

    # 从x到y的路径上，所有节点的值增加v
    @staticmethod
    def pathAdd(x, y, v):
        x = jcast('int', x)
        y = jcast('int', y)
        v = jcast('int', v)
        while (Code01_HLD2.top[x] != Code01_HLD2.top[y]):
            if (Code01_HLD2.dep[Code01_HLD2.top[x]] <= Code01_HLD2.dep[Code01_HLD2.top[y]]):
                Code01_HLD2.add(Code01_HLD2.dfn[Code01_HLD2.top[y]], Code01_HLD2.dfn[y], v, 1, Code01_HLD2.n, 1)
                y = jcast('int', Code01_HLD2.fa[Code01_HLD2.top[y]])
            else:
                Code01_HLD2.add(Code01_HLD2.dfn[Code01_HLD2.top[x]], Code01_HLD2.dfn[x], v, 1, Code01_HLD2.n, 1)
                x = jcast('int', Code01_HLD2.fa[Code01_HLD2.top[x]])
        Code01_HLD2.add(jstatic('Math', 'min', Code01_HLD2.dfn[x], Code01_HLD2.dfn[y]), jstatic('Math', 'max', Code01_HLD2.dfn[x], Code01_HLD2.dfn[y]), v, 1, Code01_HLD2.n, 1)

    # x的子树上，所有节点的值增加v
    @staticmethod
    def subtreeAdd(x, v):
        x = jcast('int', x)
        v = jcast('int', v)
        Code01_HLD2.add(Code01_HLD2.dfn[x], jcast('int', (jcast('int', jadd(Code01_HLD2.dfn[x], Code01_HLD2.siz[x])) - 1)), v, 1, Code01_HLD2.n, 1)

    # 从x到y的路径上，查询所有节点的累加和
    @staticmethod
    def pathSum(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        ans = jcast('long', 0)
        while (Code01_HLD2.top[x] != Code01_HLD2.top[y]):
            if (Code01_HLD2.dep[Code01_HLD2.top[x]] <= Code01_HLD2.dep[Code01_HLD2.top[y]]):
                ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, Code01_HLD2.query(Code01_HLD2.dfn[Code01_HLD2.top[y]], Code01_HLD2.dfn[y], 1, Code01_HLD2.n, 1))), Code01_HLD2.MOD)))
                y = jcast('int', Code01_HLD2.fa[Code01_HLD2.top[y]])
            else:
                ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, Code01_HLD2.query(Code01_HLD2.dfn[Code01_HLD2.top[x]], Code01_HLD2.dfn[x], 1, Code01_HLD2.n, 1))), Code01_HLD2.MOD)))
                x = jcast('int', Code01_HLD2.fa[Code01_HLD2.top[x]])
        ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, Code01_HLD2.query(jstatic('Math', 'min', Code01_HLD2.dfn[x], Code01_HLD2.dfn[y]), jstatic('Math', 'max', Code01_HLD2.dfn[x], Code01_HLD2.dfn[y]), 1, Code01_HLD2.n, 1))), Code01_HLD2.MOD)))
        return jcast('long', ans)

    # x的子树上，查询所有节点的累加和
    @staticmethod
    def subtreeSum(x):
        x = jcast('int', x)
        return jcast('long', Code01_HLD2.query(Code01_HLD2.dfn[x], jcast('int', (jcast('int', jadd(Code01_HLD2.dfn[x], Code01_HLD2.siz[x])) - 1)), 1, Code01_HLD2.n, 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_HLD2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code01_HLD2.m = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code01_HLD2.root = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code01_HLD2.MOD = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code01_HLD2.n):
            jcall(in_, 'nextToken')
            Code01_HLD2.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code01_HLD2.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_HLD2.addEdge(u, v)
            Code01_HLD2.addEdge(v, u)
            i = jcast('int', (i + 1))
        # dfs3() 等同于 dfs1(root, 0)，调用迭代版防止爆栈
        Code01_HLD2.dfs3()
        # dfs4() 等同于 dfs2(root, root)，调用迭代版防止爆栈
        Code01_HLD2.dfs4()
        Code01_HLD2.build(1, Code01_HLD2.n, 1)
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        v = 0
        while (i <= Code01_HLD2.m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            if (op == 1):
                jcall(in_, 'nextToken')
                x = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                y = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', jget(in_, 'nval')))
                Code01_HLD2.pathAdd(x, y, v)
            else:
                if (op == 2):
                    jcall(in_, 'nextToken')
                    x = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    y = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(out, 'println', Code01_HLD2.pathSum(x, y))
                else:
                    if (op == 3):
                        jcall(in_, 'nextToken')
                        x = jcast('int', jcast('int', jget(in_, 'nval')))
                        jcall(in_, 'nextToken')
                        v = jcast('int', jcast('int', jget(in_, 'nval')))
                        Code01_HLD2.subtreeAdd(x, v)
                    else:
                        jcall(in_, 'nextToken')
                        x = jcast('int', jcast('int', jget(in_, 'nval')))
                        jcall(out, 'println', Code01_HLD2.subtreeSum(x))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_HLD2.MAXN = jcast('int', 100001)
Code01_HLD2.n = jcast('int', 0)
Code01_HLD2.m = jcast('int', 0)
Code01_HLD2.root = jcast('int', 0)
Code01_HLD2.MOD = jcast('int', 0)
Code01_HLD2.arr = jarray('int', [Code01_HLD2.MAXN])
Code01_HLD2.head = jarray('int', [Code01_HLD2.MAXN])
Code01_HLD2.next = jarray('int', [jcast('int', (Code01_HLD2.MAXN << (1 & 31)))])
Code01_HLD2.to = jarray('int', [jcast('int', (Code01_HLD2.MAXN << (1 & 31)))])
Code01_HLD2.cntg = jcast('int', 0)
Code01_HLD2.fa = jarray('int', [Code01_HLD2.MAXN])
Code01_HLD2.dep = jarray('int', [Code01_HLD2.MAXN])
Code01_HLD2.siz = jarray('int', [Code01_HLD2.MAXN])
Code01_HLD2.son = jarray('int', [Code01_HLD2.MAXN])
Code01_HLD2.top = jarray('int', [Code01_HLD2.MAXN])
Code01_HLD2.dfn = jarray('int', [Code01_HLD2.MAXN])
Code01_HLD2.seg = jarray('int', [Code01_HLD2.MAXN])
Code01_HLD2.cntd = jcast('int', 0)
Code01_HLD2.sum = jarray('long', [jcast('int', (Code01_HLD2.MAXN << (2 & 31)))])
Code01_HLD2.addTag = jarray('long', [jcast('int', (Code01_HLD2.MAXN << (2 & 31)))])
Code01_HLD2.fse = jarray('int', [Code01_HLD2.MAXN, 3])
Code01_HLD2.stacksize = jcast('int', 0)
Code01_HLD2.first = jcast('int', 0)
Code01_HLD2.second = jcast('int', 0)
Code01_HLD2.edge = jcast('int', 0)

if __name__ == '__main__':
    Code01_HLD2.main([])
