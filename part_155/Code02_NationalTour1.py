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

# 国家集训队旅游，Python版
# 一共有n个节点，节点编号从0到n-1，所有节点连成一棵树
# 给定n-1条边，边的编号从1到n-1，每条边给定初始边权
# 一共有m条操作，每条操作的类型是如下5种类型中的一种
# 操作 C x y   : 第x条边的边权改成y
# 操作 N x y   : x号点到y号点的路径上，所有边权变成相反数
# 操作 SUM x y : x号点到y号点的路径上，查询所有边权的累加和
# 操作 MAX x y : x号点到y号点的路径上，查询所有边权的最大值
# 操作 MIN x y : x号点到y号点的路径上，查询所有边权的最小值
# 1 <= n、m <= 2 * 10^5
# -1000 <= 任何时候的边权 <= +1000
# 测试链接 : https://www.luogu.com.cn/problem/P1505
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_NationalTour1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'arr': 'arr', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'dfn': 'dfn', 'cntd': 'cntd', 'sum': 'sum', 'max': 'max', 'min': 'min', 'negativeTag': 'negativeTag', 'fse': 'fse', 'stacksize': 'stacksize', 'first': 'first', 'second': 'second', 'edge': 'edge'}
    MAXN = 0
    n = 0
    m = 0
    # arr[i][0] : 第i条边的其中一点
    # arr[i][1] : 第i条边的另外一点
    # arr[i][2] : 第i条边的初始边权
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
    # 线段树
    sum = None
    max = None
    min = None
    negativeTag = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_NationalTour1.next, ((_java_obj_1 := Code02_NationalTour1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_NationalTour1.head[u])
        Code02_NationalTour1.to[Code02_NationalTour1.cntg] = jcast('int', v)
        Code02_NationalTour1.head[u] = jcast('int', Code02_NationalTour1.cntg)

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code02_NationalTour1.fa[u] = jcast('int', f)
        Code02_NationalTour1.dep[u] = jcast('int', jcast('int', jadd(Code02_NationalTour1.dep[f], 1)))
        Code02_NationalTour1.siz[u] = jcast('int', 1)
        e = jcast('int', Code02_NationalTour1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code02_NationalTour1.to[e])
            if (v != f):
                Code02_NationalTour1.dfs1(v, u)
            e = jcast('int', Code02_NationalTour1.next[e])
        e = jcast('int', Code02_NationalTour1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code02_NationalTour1.to[e])
            if (v != f):
                Code02_NationalTour1.siz[u] = jcast('int', jcast('int', jadd(Code02_NationalTour1.siz[u], Code02_NationalTour1.siz[v])))
                if ((Code02_NationalTour1.son[u] == 0) or (Code02_NationalTour1.siz[Code02_NationalTour1.son[u]] < Code02_NationalTour1.siz[v])):
                    Code02_NationalTour1.son[u] = jcast('int', v)
            e = jcast('int', Code02_NationalTour1.next[e])

    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code02_NationalTour1.top[u] = jcast('int', t)
        jset(Code02_NationalTour1.dfn, u, ((_java_obj_4 := Code02_NationalTour1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        if (Code02_NationalTour1.son[u] == 0):
            return
        Code02_NationalTour1.dfs2(Code02_NationalTour1.son[u], t)
        e = jcast('int', Code02_NationalTour1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code02_NationalTour1.to[e])
            if ((v != Code02_NationalTour1.fa[u]) and (v != Code02_NationalTour1.son[u])):
                Code02_NationalTour1.dfs2(v, v)
            e = jcast('int', Code02_NationalTour1.next[e])

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
        jset(Code02_NationalTour1.fse[Code02_NationalTour1.stacksize], 0, fir)
        jset(Code02_NationalTour1.fse[Code02_NationalTour1.stacksize], 1, sec)
        jset(Code02_NationalTour1.fse[Code02_NationalTour1.stacksize], 2, edg)
        Code02_NationalTour1.stacksize = jcast('int', (Code02_NationalTour1.stacksize + 1))

    @staticmethod
    def pop():
        Code02_NationalTour1.stacksize = jcast('int', (Code02_NationalTour1.stacksize - 1))
        Code02_NationalTour1.first = jcast('int', Code02_NationalTour1.fse[Code02_NationalTour1.stacksize][0])
        Code02_NationalTour1.second = jcast('int', Code02_NationalTour1.fse[Code02_NationalTour1.stacksize][1])
        Code02_NationalTour1.edge = jcast('int', Code02_NationalTour1.fse[Code02_NationalTour1.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs3():
        Code02_NationalTour1.stacksize = jcast('int', 0)
        Code02_NationalTour1.push(1, 0, jcast('int', (-1)))
        while (Code02_NationalTour1.stacksize > 0):
            Code02_NationalTour1.pop()
            if (Code02_NationalTour1.edge == jcast('int', (-1))):
                Code02_NationalTour1.fa[Code02_NationalTour1.first] = jcast('int', Code02_NationalTour1.second)
                Code02_NationalTour1.dep[Code02_NationalTour1.first] = jcast('int', jcast('int', jadd(Code02_NationalTour1.dep[Code02_NationalTour1.second], 1)))
                Code02_NationalTour1.siz[Code02_NationalTour1.first] = jcast('int', 1)
                Code02_NationalTour1.edge = jcast('int', Code02_NationalTour1.head[Code02_NationalTour1.first])
            else:
                Code02_NationalTour1.edge = jcast('int', Code02_NationalTour1.next[Code02_NationalTour1.edge])
            if (Code02_NationalTour1.edge != 0):
                Code02_NationalTour1.push(Code02_NationalTour1.first, Code02_NationalTour1.second, Code02_NationalTour1.edge)
                if (Code02_NationalTour1.to[Code02_NationalTour1.edge] != Code02_NationalTour1.second):
                    Code02_NationalTour1.push(Code02_NationalTour1.to[Code02_NationalTour1.edge], Code02_NationalTour1.first, jcast('int', (-1)))
            else:
                e = jcast('int', Code02_NationalTour1.head[Code02_NationalTour1.first])
                v = 0
                while (e > 0):
                    v = jcast('int', Code02_NationalTour1.to[e])
                    if (v != Code02_NationalTour1.second):
                        Code02_NationalTour1.siz[Code02_NationalTour1.first] = jcast('int', jcast('int', jadd(Code02_NationalTour1.siz[Code02_NationalTour1.first], Code02_NationalTour1.siz[v])))
                        if ((Code02_NationalTour1.son[Code02_NationalTour1.first] == 0) or (Code02_NationalTour1.siz[Code02_NationalTour1.son[Code02_NationalTour1.first]] < Code02_NationalTour1.siz[v])):
                            Code02_NationalTour1.son[Code02_NationalTour1.first] = jcast('int', v)
                    e = jcast('int', Code02_NationalTour1.next[e])

    # dfs2的迭代版
    @staticmethod
    def dfs4():
        Code02_NationalTour1.stacksize = jcast('int', 0)
        Code02_NationalTour1.push(1, 1, jcast('int', (-1)))
        while (Code02_NationalTour1.stacksize > 0):
            try:
                Code02_NationalTour1.pop()
                if (Code02_NationalTour1.edge == jcast('int', (-1))):
                    Code02_NationalTour1.top[Code02_NationalTour1.first] = jcast('int', Code02_NationalTour1.second)
                    jset(Code02_NationalTour1.dfn, Code02_NationalTour1.first, ((_java_obj_8 := Code02_NationalTour1), (_java_key_9 := 'cntd'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3])
                    if (Code02_NationalTour1.son[Code02_NationalTour1.first] == 0):
                        raise JContinue(None)
                    Code02_NationalTour1.push(Code02_NationalTour1.first, Code02_NationalTour1.second, jcast('int', (-2)))
                    Code02_NationalTour1.push(Code02_NationalTour1.son[Code02_NationalTour1.first], Code02_NationalTour1.second, jcast('int', (-1)))
                    raise JContinue(None)
                else:
                    if (Code02_NationalTour1.edge == jcast('int', (-2))):
                        Code02_NationalTour1.edge = jcast('int', Code02_NationalTour1.head[Code02_NationalTour1.first])
                    else:
                        Code02_NationalTour1.edge = jcast('int', Code02_NationalTour1.next[Code02_NationalTour1.edge])
                if (Code02_NationalTour1.edge != 0):
                    Code02_NationalTour1.push(Code02_NationalTour1.first, Code02_NationalTour1.second, Code02_NationalTour1.edge)
                    if ((Code02_NationalTour1.to[Code02_NationalTour1.edge] != Code02_NationalTour1.fa[Code02_NationalTour1.first]) and (Code02_NationalTour1.to[Code02_NationalTour1.edge] != Code02_NationalTour1.son[Code02_NationalTour1.first])):
                        Code02_NationalTour1.push(Code02_NationalTour1.to[Code02_NationalTour1.edge], Code02_NationalTour1.to[Code02_NationalTour1.edge], jcast('int', (-1)))
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
        l = jcast('int', jcast('int', (i << (1 & 31))))
        r = jcast('int', jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code02_NationalTour1.sum[i] = jcast('int', jcast('int', jadd(Code02_NationalTour1.sum[l], Code02_NationalTour1.sum[r])))
        jset(Code02_NationalTour1.max, i, jstatic('Math', 'max', Code02_NationalTour1.max[l], Code02_NationalTour1.max[r]))
        jset(Code02_NationalTour1.min, i, jstatic('Math', 'min', Code02_NationalTour1.min[l], Code02_NationalTour1.min[r]))

    @staticmethod
    def lazy(i):
        i = jcast('int', i)
        Code02_NationalTour1.sum[i] = jcast('int', jcast('int', (-Code02_NationalTour1.sum[i])))
        tmp = jcast('int', Code02_NationalTour1.max[i])
        Code02_NationalTour1.max[i] = jcast('int', jcast('int', (-Code02_NationalTour1.min[i])))
        Code02_NationalTour1.min[i] = jcast('int', jcast('int', (-tmp)))
        Code02_NationalTour1.negativeTag[i] = jcast('boolean', (not Code02_NationalTour1.negativeTag[i]))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if Code02_NationalTour1.negativeTag[i]:
            Code02_NationalTour1.lazy(jcast('int', (i << (1 & 31))))
            Code02_NationalTour1.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code02_NationalTour1.negativeTag[i] = jcast('boolean', False)

    @staticmethod
    def update(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            jset(Code02_NationalTour1.sum, i, jset(Code02_NationalTour1.max, i, jset(Code02_NationalTour1.min, i, jobv)))
        else:
            Code02_NationalTour1.down(i)
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                Code02_NationalTour1.update(jobi, jobv, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code02_NationalTour1.update(jobi, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code02_NationalTour1.up(i)

    @staticmethod
    def negative(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code02_NationalTour1.lazy(i)
        else:
            Code02_NationalTour1.down(i)
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobl <= mid):
                Code02_NationalTour1.negative(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code02_NationalTour1.negative(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code02_NationalTour1.up(i)

    @staticmethod
    def querySum(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code02_NationalTour1.sum[i])
        Code02_NationalTour1.down(i)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        ans = jcast('int', 0)
        if (jobl <= mid):
            ans = jcast('int', jcast('int', jadd(ans, Code02_NationalTour1.querySum(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            ans = jcast('int', jcast('int', jadd(ans, Code02_NationalTour1.querySum(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('int', ans)

    @staticmethod
    def queryMax(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code02_NationalTour1.max[i])
        Code02_NationalTour1.down(i)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        if (jobl <= mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code02_NationalTour1.queryMax(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code02_NationalTour1.queryMax(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('int', ans)

    @staticmethod
    def queryMin(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code02_NationalTour1.min[i])
        Code02_NationalTour1.down(i)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        if (jobl <= mid):
            ans = jcast('int', jstatic('Math', 'min', ans, Code02_NationalTour1.queryMin(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('int', jstatic('Math', 'min', ans, Code02_NationalTour1.queryMin(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('int', ans)

    @staticmethod
    def edgeUpdate(ei, val):
        ei = jcast('int', ei)
        val = jcast('int', val)
        x = jcast('int', Code02_NationalTour1.arr[ei][0])
        y = jcast('int', Code02_NationalTour1.arr[ei][1])
        down = jcast('int', jstatic('Math', 'max', Code02_NationalTour1.dfn[x], Code02_NationalTour1.dfn[y]))
        Code02_NationalTour1.update(down, val, 1, Code02_NationalTour1.n, 1)

    @staticmethod
    def pathNegative(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        while (Code02_NationalTour1.top[x] != Code02_NationalTour1.top[y]):
            if (Code02_NationalTour1.dep[Code02_NationalTour1.top[x]] <= Code02_NationalTour1.dep[Code02_NationalTour1.top[y]]):
                Code02_NationalTour1.negative(Code02_NationalTour1.dfn[Code02_NationalTour1.top[y]], Code02_NationalTour1.dfn[y], 1, Code02_NationalTour1.n, 1)
                y = jcast('int', Code02_NationalTour1.fa[Code02_NationalTour1.top[y]])
            else:
                Code02_NationalTour1.negative(Code02_NationalTour1.dfn[Code02_NationalTour1.top[x]], Code02_NationalTour1.dfn[x], 1, Code02_NationalTour1.n, 1)
                x = jcast('int', Code02_NationalTour1.fa[Code02_NationalTour1.top[x]])
        Code02_NationalTour1.negative(jcast('int', jadd(jstatic('Math', 'min', Code02_NationalTour1.dfn[x], Code02_NationalTour1.dfn[y]), 1)), jstatic('Math', 'max', Code02_NationalTour1.dfn[x], Code02_NationalTour1.dfn[y]), 1, Code02_NationalTour1.n, 1)

    @staticmethod
    def pathSum(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        ans = jcast('int', 0)
        while (Code02_NationalTour1.top[x] != Code02_NationalTour1.top[y]):
            if (Code02_NationalTour1.dep[Code02_NationalTour1.top[x]] <= Code02_NationalTour1.dep[Code02_NationalTour1.top[y]]):
                ans = jcast('int', jcast('int', jadd(ans, Code02_NationalTour1.querySum(Code02_NationalTour1.dfn[Code02_NationalTour1.top[y]], Code02_NationalTour1.dfn[y], 1, Code02_NationalTour1.n, 1))))
                y = jcast('int', Code02_NationalTour1.fa[Code02_NationalTour1.top[y]])
            else:
                ans = jcast('int', jcast('int', jadd(ans, Code02_NationalTour1.querySum(Code02_NationalTour1.dfn[Code02_NationalTour1.top[x]], Code02_NationalTour1.dfn[x], 1, Code02_NationalTour1.n, 1))))
                x = jcast('int', Code02_NationalTour1.fa[Code02_NationalTour1.top[x]])
        ans = jcast('int', jcast('int', jadd(ans, Code02_NationalTour1.querySum(jcast('int', jadd(jstatic('Math', 'min', Code02_NationalTour1.dfn[x], Code02_NationalTour1.dfn[y]), 1)), jstatic('Math', 'max', Code02_NationalTour1.dfn[x], Code02_NationalTour1.dfn[y]), 1, Code02_NationalTour1.n, 1))))
        return jcast('int', ans)

    @staticmethod
    def pathMax(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        while (Code02_NationalTour1.top[x] != Code02_NationalTour1.top[y]):
            if (Code02_NationalTour1.dep[Code02_NationalTour1.top[x]] <= Code02_NationalTour1.dep[Code02_NationalTour1.top[y]]):
                ans = jcast('int', jstatic('Math', 'max', ans, Code02_NationalTour1.queryMax(Code02_NationalTour1.dfn[Code02_NationalTour1.top[y]], Code02_NationalTour1.dfn[y], 1, Code02_NationalTour1.n, 1)))
                y = jcast('int', Code02_NationalTour1.fa[Code02_NationalTour1.top[y]])
            else:
                ans = jcast('int', jstatic('Math', 'max', ans, Code02_NationalTour1.queryMax(Code02_NationalTour1.dfn[Code02_NationalTour1.top[x]], Code02_NationalTour1.dfn[x], 1, Code02_NationalTour1.n, 1)))
                x = jcast('int', Code02_NationalTour1.fa[Code02_NationalTour1.top[x]])
        ans = jcast('int', jstatic('Math', 'max', ans, Code02_NationalTour1.queryMax(jcast('int', jadd(jstatic('Math', 'min', Code02_NationalTour1.dfn[x], Code02_NationalTour1.dfn[y]), 1)), jstatic('Math', 'max', Code02_NationalTour1.dfn[x], Code02_NationalTour1.dfn[y]), 1, Code02_NationalTour1.n, 1)))
        return jcast('int', ans)

    @staticmethod
    def pathMin(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        while (Code02_NationalTour1.top[x] != Code02_NationalTour1.top[y]):
            if (Code02_NationalTour1.dep[Code02_NationalTour1.top[x]] <= Code02_NationalTour1.dep[Code02_NationalTour1.top[y]]):
                ans = jcast('int', jstatic('Math', 'min', ans, Code02_NationalTour1.queryMin(Code02_NationalTour1.dfn[Code02_NationalTour1.top[y]], Code02_NationalTour1.dfn[y], 1, Code02_NationalTour1.n, 1)))
                y = jcast('int', Code02_NationalTour1.fa[Code02_NationalTour1.top[y]])
            else:
                ans = jcast('int', jstatic('Math', 'min', ans, Code02_NationalTour1.queryMin(Code02_NationalTour1.dfn[Code02_NationalTour1.top[x]], Code02_NationalTour1.dfn[x], 1, Code02_NationalTour1.n, 1)))
                x = jcast('int', Code02_NationalTour1.fa[Code02_NationalTour1.top[x]])
        ans = jcast('int', jstatic('Math', 'min', ans, Code02_NationalTour1.queryMin(jcast('int', jadd(jstatic('Math', 'min', Code02_NationalTour1.dfn[x], Code02_NationalTour1.dfn[y]), 1)), jstatic('Math', 'max', Code02_NationalTour1.dfn[x], Code02_NationalTour1.dfn[y]), 1, Code02_NationalTour1.n, 1)))
        return jcast('int', ans)

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i < Code02_NationalTour1.n):
            Code02_NationalTour1.addEdge(Code02_NationalTour1.arr[i][0], Code02_NationalTour1.arr[i][1])
            Code02_NationalTour1.addEdge(Code02_NationalTour1.arr[i][1], Code02_NationalTour1.arr[i][0])
            i = jcast('int', (i + 1))
        Code02_NationalTour1.dfs3()
        Code02_NationalTour1.dfs4()
        i = jcast('int', 1)
        while (i < Code02_NationalTour1.n):
            Code02_NationalTour1.edgeUpdate(i, Code02_NationalTour1.arr[i][2])
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        io = Code02_NationalTour1.Kattio(_java_ctor=0)
        Code02_NationalTour1.n = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i < Code02_NationalTour1.n):
            jset(Code02_NationalTour1.arr[i], 0, jcast('int', jadd(jcall(io, 'nextInt'), 1)))
            jset(Code02_NationalTour1.arr[i], 1, jcast('int', jadd(jcall(io, 'nextInt'), 1)))
            jset(Code02_NationalTour1.arr[i], 2, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        Code02_NationalTour1.prepare()
        Code02_NationalTour1.m = jcast('int', jcall(io, 'nextInt'))
        op = None
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= Code02_NationalTour1.m):
            op = jcall(io, 'next')
            if jcall(op, 'equals', 'C'):
                x = jcast('int', jcall(io, 'nextInt'))
                y = jcast('int', jcall(io, 'nextInt'))
                Code02_NationalTour1.edgeUpdate(x, y)
            else:
                x = jcast('int', jcast('int', jadd(jcall(io, 'nextInt'), 1)))
                y = jcast('int', jcast('int', jadd(jcall(io, 'nextInt'), 1)))
                if jcall(op, 'equals', 'N'):
                    Code02_NationalTour1.pathNegative(x, y)
                else:
                    if jcall(op, 'equals', 'SUM'):
                        jcall(io, 'println', Code02_NationalTour1.pathSum(x, y))
                    else:
                        if jcall(op, 'equals', 'MAX'):
                            jcall(io, 'println', Code02_NationalTour1.pathMax(x, y))
                        else:
                            jcall(io, 'println', Code02_NationalTour1.pathMin(x, y))
            i = jcast('int', (i + 1))
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
            raise TypeError("No matching overload for Code02_NationalTour1.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_NationalTour1.MAXN = jcast('int', 200001)
Code02_NationalTour1.n = jcast('int', 0)
Code02_NationalTour1.m = jcast('int', 0)
Code02_NationalTour1.arr = jarray('int', [Code02_NationalTour1.MAXN, 3])
Code02_NationalTour1.head = jarray('int', [Code02_NationalTour1.MAXN])
Code02_NationalTour1.next = jarray('int', [jcast('int', (Code02_NationalTour1.MAXN << (1 & 31)))])
Code02_NationalTour1.to = jarray('int', [jcast('int', (Code02_NationalTour1.MAXN << (1 & 31)))])
Code02_NationalTour1.cntg = jcast('int', 0)
Code02_NationalTour1.fa = jarray('int', [Code02_NationalTour1.MAXN])
Code02_NationalTour1.dep = jarray('int', [Code02_NationalTour1.MAXN])
Code02_NationalTour1.siz = jarray('int', [Code02_NationalTour1.MAXN])
Code02_NationalTour1.son = jarray('int', [Code02_NationalTour1.MAXN])
Code02_NationalTour1.top = jarray('int', [Code02_NationalTour1.MAXN])
Code02_NationalTour1.dfn = jarray('int', [Code02_NationalTour1.MAXN])
Code02_NationalTour1.cntd = jcast('int', 0)
Code02_NationalTour1.sum = jarray('int', [jcast('int', (Code02_NationalTour1.MAXN << (2 & 31)))])
Code02_NationalTour1.max = jarray('int', [jcast('int', (Code02_NationalTour1.MAXN << (2 & 31)))])
Code02_NationalTour1.min = jarray('int', [jcast('int', (Code02_NationalTour1.MAXN << (2 & 31)))])
Code02_NationalTour1.negativeTag = jarray('boolean', [jcast('int', (Code02_NationalTour1.MAXN << (2 & 31)))])
Code02_NationalTour1.fse = jarray('int', [Code02_NationalTour1.MAXN, 3])
Code02_NationalTour1.stacksize = jcast('int', 0)
Code02_NationalTour1.first = jcast('int', 0)
Code02_NationalTour1.second = jcast('int', 0)
Code02_NationalTour1.edge = jcast('int', 0)

if __name__ == '__main__':
    Code02_NationalTour1.main([])
