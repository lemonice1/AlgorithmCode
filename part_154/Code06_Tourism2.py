# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 旅游，Python版
# 一共有n个城市，给定n-1条边，城市连成一棵树，每个城市给定初始的宝石价格
# 一共有m条操作，操作类型如下
# 操作 x y v : 城市x到城市y的最短路途中，你可以选择一城买入宝石
# 继续行进的过程中，再选一城卖出宝石，以此获得利润
# 打印你能获得的最大利润，如果为负数，打印0
# 当你结束旅途后，沿途所有城市的宝石价格增加v
# 1 <= n、m <= 5 * 10^4
# 0 <= 任何时候的宝石价格 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P3976
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_Tourism2:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'm': 'm', 'arr': 'arr', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'dfn': 'dfn', 'seg': 'seg', 'cntd': 'cntd', 'max': 'max', 'min': 'min', 'lprofit': 'lprofit', 'rprofit': 'rprofit', 'addTag': 'addTag', 'fse': 'fse', 'stacksize': 'stacksize', 'first': 'first', 'second': 'second', 'edge': 'edge'}
    MAXN = 0
    INF = 0
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
    max = None
    min = None
    lprofit = None
    rprofit = None
    # 线段树范围增加的懒更新信息
    addTag = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code06_Tourism2.next, ((_java_obj_1 := Code06_Tourism2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_Tourism2.head[u])
        Code06_Tourism2.to[Code06_Tourism2.cntg] = jcast('int', v)
        Code06_Tourism2.head[u] = jcast('int', Code06_Tourism2.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code06_Tourism2.fa[u] = jcast('int', f)
        Code06_Tourism2.dep[u] = jcast('int', jcast('int', jadd(Code06_Tourism2.dep[f], 1)))
        Code06_Tourism2.siz[u] = jcast('int', 1)
        e = jcast('int', Code06_Tourism2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code06_Tourism2.to[e])
            if (v != f):
                Code06_Tourism2.dfs1(v, u)
            e = jcast('int', Code06_Tourism2.next[e])
        e = jcast('int', Code06_Tourism2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code06_Tourism2.to[e])
            if (v != f):
                Code06_Tourism2.siz[u] = jcast('int', jcast('int', jadd(Code06_Tourism2.siz[u], Code06_Tourism2.siz[v])))
                if ((Code06_Tourism2.son[u] == 0) or (Code06_Tourism2.siz[Code06_Tourism2.son[u]] < Code06_Tourism2.siz[v])):
                    Code06_Tourism2.son[u] = jcast('int', v)
            e = jcast('int', Code06_Tourism2.next[e])

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code06_Tourism2.top[u] = jcast('int', t)
        jset(Code06_Tourism2.dfn, u, ((_java_obj_4 := Code06_Tourism2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code06_Tourism2.seg[Code06_Tourism2.cntd] = jcast('int', u)
        if (Code06_Tourism2.son[u] == 0):
            return
        Code06_Tourism2.dfs2(Code06_Tourism2.son[u], t)
        e = jcast('int', Code06_Tourism2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code06_Tourism2.to[e])
            if ((v != Code06_Tourism2.fa[u]) and (v != Code06_Tourism2.son[u])):
                Code06_Tourism2.dfs2(v, v)
            e = jcast('int', Code06_Tourism2.next[e])

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
        jset(Code06_Tourism2.fse[Code06_Tourism2.stacksize], 0, fir)
        jset(Code06_Tourism2.fse[Code06_Tourism2.stacksize], 1, sec)
        jset(Code06_Tourism2.fse[Code06_Tourism2.stacksize], 2, edg)
        Code06_Tourism2.stacksize = jcast('int', (Code06_Tourism2.stacksize + 1))

    @staticmethod
    def pop():
        Code06_Tourism2.stacksize = jcast('int', (Code06_Tourism2.stacksize - 1))
        Code06_Tourism2.first = jcast('int', Code06_Tourism2.fse[Code06_Tourism2.stacksize][0])
        Code06_Tourism2.second = jcast('int', Code06_Tourism2.fse[Code06_Tourism2.stacksize][1])
        Code06_Tourism2.edge = jcast('int', Code06_Tourism2.fse[Code06_Tourism2.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs3():
        Code06_Tourism2.stacksize = jcast('int', 0)
        Code06_Tourism2.push(1, 0, jcast('int', (-1)))
        while (Code06_Tourism2.stacksize > 0):
            Code06_Tourism2.pop()
            if (Code06_Tourism2.edge == jcast('int', (-1))):
                Code06_Tourism2.fa[Code06_Tourism2.first] = jcast('int', Code06_Tourism2.second)
                Code06_Tourism2.dep[Code06_Tourism2.first] = jcast('int', jcast('int', jadd(Code06_Tourism2.dep[Code06_Tourism2.second], 1)))
                Code06_Tourism2.siz[Code06_Tourism2.first] = jcast('int', 1)
                Code06_Tourism2.edge = jcast('int', Code06_Tourism2.head[Code06_Tourism2.first])
            else:
                Code06_Tourism2.edge = jcast('int', Code06_Tourism2.next[Code06_Tourism2.edge])
            if (Code06_Tourism2.edge != 0):
                Code06_Tourism2.push(Code06_Tourism2.first, Code06_Tourism2.second, Code06_Tourism2.edge)
                if (Code06_Tourism2.to[Code06_Tourism2.edge] != Code06_Tourism2.second):
                    Code06_Tourism2.push(Code06_Tourism2.to[Code06_Tourism2.edge], Code06_Tourism2.first, jcast('int', (-1)))
            else:
                e = jcast('int', Code06_Tourism2.head[Code06_Tourism2.first])
                v = 0
                while (e > 0):
                    v = jcast('int', Code06_Tourism2.to[e])
                    if (v != Code06_Tourism2.second):
                        Code06_Tourism2.siz[Code06_Tourism2.first] = jcast('int', jcast('int', jadd(Code06_Tourism2.siz[Code06_Tourism2.first], Code06_Tourism2.siz[v])))
                        if ((Code06_Tourism2.son[Code06_Tourism2.first] == 0) or (Code06_Tourism2.siz[Code06_Tourism2.son[Code06_Tourism2.first]] < Code06_Tourism2.siz[v])):
                            Code06_Tourism2.son[Code06_Tourism2.first] = jcast('int', v)
                    e = jcast('int', Code06_Tourism2.next[e])

    # dfs2的迭代版
    @staticmethod
    def dfs4():
        Code06_Tourism2.stacksize = jcast('int', 0)
        Code06_Tourism2.push(1, 1, jcast('int', (-1)))
        while (Code06_Tourism2.stacksize > 0):
            try:
                Code06_Tourism2.pop()
                # edge == -1，表示第一次来到当前节点，并且先处理重儿子
                if (Code06_Tourism2.edge == jcast('int', (-1))):
                    Code06_Tourism2.top[Code06_Tourism2.first] = jcast('int', Code06_Tourism2.second)
                    jset(Code06_Tourism2.dfn, Code06_Tourism2.first, ((_java_obj_8 := Code06_Tourism2), (_java_key_9 := 'cntd'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3])
                    Code06_Tourism2.seg[Code06_Tourism2.cntd] = jcast('int', Code06_Tourism2.first)
                    if (Code06_Tourism2.son[Code06_Tourism2.first] == 0):
                        raise JContinue(None)
                    Code06_Tourism2.push(Code06_Tourism2.first, Code06_Tourism2.second, jcast('int', (-2)))
                    Code06_Tourism2.push(Code06_Tourism2.son[Code06_Tourism2.first], Code06_Tourism2.second, jcast('int', (-1)))
                    raise JContinue(None)
                    # edge == -2，表示处理完当前节点的重儿子，回到了当前节点
                else:
                    if (Code06_Tourism2.edge == jcast('int', (-2))):
                        Code06_Tourism2.edge = jcast('int', Code06_Tourism2.head[Code06_Tourism2.first])
                        # edge >= 0, 继续处理其他的边
                    else:
                        Code06_Tourism2.edge = jcast('int', Code06_Tourism2.next[Code06_Tourism2.edge])
                if (Code06_Tourism2.edge != 0):
                    Code06_Tourism2.push(Code06_Tourism2.first, Code06_Tourism2.second, Code06_Tourism2.edge)
                    if ((Code06_Tourism2.to[Code06_Tourism2.edge] != Code06_Tourism2.fa[Code06_Tourism2.first]) and (Code06_Tourism2.to[Code06_Tourism2.edge] != Code06_Tourism2.son[Code06_Tourism2.first])):
                        Code06_Tourism2.push(Code06_Tourism2.to[Code06_Tourism2.edge], Code06_Tourism2.to[Code06_Tourism2.edge], jcast('int', (-1)))
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
        jset(Code06_Tourism2.max, i, jstatic('Math', 'max', Code06_Tourism2.max[l], Code06_Tourism2.max[r]))
        jset(Code06_Tourism2.min, i, jstatic('Math', 'min', Code06_Tourism2.min[l], Code06_Tourism2.min[r]))
        jset(Code06_Tourism2.lprofit, i, jstatic('Math', 'max', jstatic('Math', 'max', Code06_Tourism2.lprofit[l], Code06_Tourism2.lprofit[r]), jcast('int', (Code06_Tourism2.max[r] - Code06_Tourism2.min[l]))))
        jset(Code06_Tourism2.rprofit, i, jstatic('Math', 'max', jstatic('Math', 'max', Code06_Tourism2.rprofit[l], Code06_Tourism2.rprofit[r]), jcast('int', (Code06_Tourism2.max[l] - Code06_Tourism2.min[r]))))

    @staticmethod
    def lazy(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        Code06_Tourism2.max[i] = jcast('int', jcast('int', jadd(Code06_Tourism2.max[i], v)))
        Code06_Tourism2.min[i] = jcast('int', jcast('int', jadd(Code06_Tourism2.min[i], v)))
        Code06_Tourism2.addTag[i] = jcast('int', jcast('int', jadd(Code06_Tourism2.addTag[i], v)))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if (Code06_Tourism2.addTag[i] != 0):
            Code06_Tourism2.lazy(jcast('int', (i << (1 & 31))), Code06_Tourism2.addTag[i])
            Code06_Tourism2.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code06_Tourism2.addTag[i])
            Code06_Tourism2.addTag[i] = jcast('int', 0)

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            jset(Code06_Tourism2.max, i, jset(Code06_Tourism2.min, i, Code06_Tourism2.arr[Code06_Tourism2.seg[l]]))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            Code06_Tourism2.build(l, mid, jcast('int', (i << (1 & 31))))
            Code06_Tourism2.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code06_Tourism2.up(i)

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code06_Tourism2.lazy(i, jobv)
        else:
            Code06_Tourism2.down(i)
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobl <= mid):
                Code06_Tourism2.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code06_Tourism2.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code06_Tourism2.up(i)

    # ans[0] : 线段树更左侧部分的max
    # ans[1] : 线段树更左侧部分的min
    # ans[2] : 线段树更左侧部分的lprofit
    # ans[3] : 线段树更左侧部分的rprofit
    # rmax : 线段树更右侧部分的max
    # rmin : 线段树更右侧部分的min
    # rlpro : 线段树更右侧部分的lprofit
    # rrpro : 线段树更右侧部分的rprofit
    # 左侧部分和右侧部分的信息整合在一起得到整个范围的max、min、lprofit、rprofit
    @staticmethod
    def merge(ans, rmax, rmin, rlpro, rrpro):
        rmax = jcast('int', rmax)
        rmin = jcast('int', rmin)
        rlpro = jcast('int', rlpro)
        rrpro = jcast('int', rrpro)
        lmax = jcast('int', ans[0])
        lmin = jcast('int', ans[1])
        llpro = jcast('int', ans[2])
        lrpro = jcast('int', ans[3])
        jset(ans, 0, jstatic('Math', 'max', lmax, rmax))
        jset(ans, 1, jstatic('Math', 'min', lmin, rmin))
        jset(ans, 2, jstatic('Math', 'max', jstatic('Math', 'max', llpro, rlpro), jcast('int', (rmax - lmin))))
        jset(ans, 3, jstatic('Math', 'max', jstatic('Math', 'max', lrpro, rrpro), jcast('int', (lmax - rmin))))

    # ans[0] : 线段树更左侧部分的max
    # ans[1] : 线段树更左侧部分的min
    # ans[2] : 线段树更左侧部分的lprofit
    # ans[3] : 线段树更左侧部分的rprofit
    # 随着线段树查询的展开，会有更右部分的信息整合进ans，最终整合出整体信息
    @staticmethod
    def _java_query_0(ans, jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code06_Tourism2.merge(ans, Code06_Tourism2.max[i], Code06_Tourism2.min[i], Code06_Tourism2.lprofit[i], Code06_Tourism2.rprofit[i])
        else:
            Code06_Tourism2.down(i)
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobl <= mid):
                Code06_Tourism2._java_query_0(ans, jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code06_Tourism2._java_query_0(ans, jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def _java_query_1(ans, jobl, jobr):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        ans[0] = jcast('int', jcast('int', (-Code06_Tourism2.INF)))
        ans[1] = jcast('int', Code06_Tourism2.INF)
        ans[2] = jcast('int', 0)
        ans[3] = jcast('int', 0)
        Code06_Tourism2._java_query_0(ans, jobl, jobr, 1, Code06_Tourism2.n, 1)

    @staticmethod
    def clone(a, b):
        a[0] = jcast('int', b[0])
        a[1] = jcast('int', b[1])
        a[2] = jcast('int', b[2])
        a[3] = jcast('int', b[3])

    @staticmethod
    def compute(x, y, v):
        x = jcast('int', x)
        y = jcast('int', y)
        v = jcast('int', v)
        tmpx = jcast('int', x)
        tmpy = jcast('int', y)
        xpath = jarray('int', [None], [jcast('int', (-Code06_Tourism2.INF)), Code06_Tourism2.INF, 0, 0])
        ypath = jarray('int', [None], [jcast('int', (-Code06_Tourism2.INF)), Code06_Tourism2.INF, 0, 0])
        cur = jarray('int', [4])
        while (Code06_Tourism2.top[x] != Code06_Tourism2.top[y]):
            if (Code06_Tourism2.dep[Code06_Tourism2.top[x]] <= Code06_Tourism2.dep[Code06_Tourism2.top[y]]):
                Code06_Tourism2._java_query_1(cur, Code06_Tourism2.dfn[Code06_Tourism2.top[y]], Code06_Tourism2.dfn[y])
                Code06_Tourism2.merge(cur, ypath[0], ypath[1], ypath[2], ypath[3])
                Code06_Tourism2.clone(ypath, cur)
                y = jcast('int', Code06_Tourism2.fa[Code06_Tourism2.top[y]])
            else:
                Code06_Tourism2._java_query_1(cur, Code06_Tourism2.dfn[Code06_Tourism2.top[x]], Code06_Tourism2.dfn[x])
                Code06_Tourism2.merge(cur, xpath[0], xpath[1], xpath[2], xpath[3])
                Code06_Tourism2.clone(xpath, cur)
                x = jcast('int', Code06_Tourism2.fa[Code06_Tourism2.top[x]])
        if (Code06_Tourism2.dep[x] <= Code06_Tourism2.dep[y]):
            Code06_Tourism2._java_query_1(cur, Code06_Tourism2.dfn[x], Code06_Tourism2.dfn[y])
            Code06_Tourism2.merge(cur, ypath[0], ypath[1], ypath[2], ypath[3])
            Code06_Tourism2.clone(ypath, cur)
        else:
            Code06_Tourism2._java_query_1(cur, Code06_Tourism2.dfn[y], Code06_Tourism2.dfn[x])
            Code06_Tourism2.merge(cur, xpath[0], xpath[1], xpath[2], xpath[3])
            Code06_Tourism2.clone(xpath, cur)
        ans = jcast('int', jstatic('Math', 'max', jstatic('Math', 'max', xpath[3], ypath[2]), jcast('int', (ypath[0] - xpath[1]))))
        x = jcast('int', tmpx)
        y = jcast('int', tmpy)
        while (Code06_Tourism2.top[x] != Code06_Tourism2.top[y]):
            if (Code06_Tourism2.dep[Code06_Tourism2.top[x]] <= Code06_Tourism2.dep[Code06_Tourism2.top[y]]):
                Code06_Tourism2.add(Code06_Tourism2.dfn[Code06_Tourism2.top[y]], Code06_Tourism2.dfn[y], v, 1, Code06_Tourism2.n, 1)
                y = jcast('int', Code06_Tourism2.fa[Code06_Tourism2.top[y]])
            else:
                Code06_Tourism2.add(Code06_Tourism2.dfn[Code06_Tourism2.top[x]], Code06_Tourism2.dfn[x], v, 1, Code06_Tourism2.n, 1)
                x = jcast('int', Code06_Tourism2.fa[Code06_Tourism2.top[x]])
        Code06_Tourism2.add(jstatic('Math', 'min', Code06_Tourism2.dfn[x], Code06_Tourism2.dfn[y]), jstatic('Math', 'max', Code06_Tourism2.dfn[x], Code06_Tourism2.dfn[y]), v, 1, Code06_Tourism2.n, 1)
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code06_Tourism2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code06_Tourism2.n):
            jcall(in_, 'nextToken')
            Code06_Tourism2.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code06_Tourism2.n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code06_Tourism2.addEdge(u, v)
            Code06_Tourism2.addEdge(v, u)
            i = jcast('int', (i + 1))
        # dfs3() 等同于 dfs1(1, 0)，调用迭代版防止爆栈
        Code06_Tourism2.dfs3()
        # dfs4() 等同于 dfs2(1, 1)，调用迭代版防止爆栈
        Code06_Tourism2.dfs4()
        Code06_Tourism2.build(1, Code06_Tourism2.n, 1)
        jcall(in_, 'nextToken')
        Code06_Tourism2.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        x = 0
        y = 0
        v = 0
        while (i <= Code06_Tourism2.m):
            jcall(in_, 'nextToken')
            x = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            y = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'println', Code06_Tourism2.compute(x, y, v))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def query(*args):
        _java_choice = jselect(args, [['int[]', 'int', 'int', 'int', 'int', 'int'], ['int[]', 'int', 'int']], [False, False])
        if _java_choice == 0:
            return Code06_Tourism2._java_query_0(*args)
        if _java_choice == 1:
            return Code06_Tourism2._java_query_1(*args)
        raise TypeError("No matching overload for Code06_Tourism2.query")


Code06_Tourism2.MAXN = jcast('int', 50001)
Code06_Tourism2.INF = jcast('int', 1000000001)
Code06_Tourism2.n = jcast('int', 0)
Code06_Tourism2.m = jcast('int', 0)
Code06_Tourism2.arr = jarray('int', [Code06_Tourism2.MAXN])
Code06_Tourism2.head = jarray('int', [Code06_Tourism2.MAXN])
Code06_Tourism2.next = jarray('int', [jcast('int', (Code06_Tourism2.MAXN << (1 & 31)))])
Code06_Tourism2.to = jarray('int', [jcast('int', (Code06_Tourism2.MAXN << (1 & 31)))])
Code06_Tourism2.cntg = jcast('int', 0)
Code06_Tourism2.fa = jarray('int', [Code06_Tourism2.MAXN])
Code06_Tourism2.dep = jarray('int', [Code06_Tourism2.MAXN])
Code06_Tourism2.siz = jarray('int', [Code06_Tourism2.MAXN])
Code06_Tourism2.son = jarray('int', [Code06_Tourism2.MAXN])
Code06_Tourism2.top = jarray('int', [Code06_Tourism2.MAXN])
Code06_Tourism2.dfn = jarray('int', [Code06_Tourism2.MAXN])
Code06_Tourism2.seg = jarray('int', [Code06_Tourism2.MAXN])
Code06_Tourism2.cntd = jcast('int', 0)
Code06_Tourism2.max = jarray('int', [jcast('int', (Code06_Tourism2.MAXN << (2 & 31)))])
Code06_Tourism2.min = jarray('int', [jcast('int', (Code06_Tourism2.MAXN << (2 & 31)))])
Code06_Tourism2.lprofit = jarray('int', [jcast('int', (Code06_Tourism2.MAXN << (2 & 31)))])
Code06_Tourism2.rprofit = jarray('int', [jcast('int', (Code06_Tourism2.MAXN << (2 & 31)))])
Code06_Tourism2.addTag = jarray('int', [jcast('int', (Code06_Tourism2.MAXN << (2 & 31)))])
Code06_Tourism2.fse = jarray('int', [Code06_Tourism2.MAXN, 3])
Code06_Tourism2.stacksize = jcast('int', 0)
Code06_Tourism2.first = jcast('int', 0)
Code06_Tourism2.second = jcast('int', 0)
Code06_Tourism2.edge = jcast('int', 0)

if __name__ == '__main__':
    Code06_Tourism2.main([])
