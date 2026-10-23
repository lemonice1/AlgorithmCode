# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 染色，Python版
# 一共有n个节点，给定n-1条边，节点连成一棵树，每个节点给定初始颜色值
# 连续相同颜色被认为是一段，变化了就认为是另一段
# 比如，112221，有三个颜色段，分别为 11、222、1
# 一共有m条操作，每种操作是如下2种类型中的一种
# 操作 C x y z : x到y的路径上，每个节点的颜色都改为z
# 操作 Q x y   : x到y的路径上，打印有几个颜色段
# 1 <= n、m <= 10^5
# 1 <= 任何时候的颜色值 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P2486
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Coloring2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'arr': 'arr', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'dfn': 'dfn', 'seg': 'seg', 'cntd': 'cntd', 'sum': 'sum', 'lcolor': 'lcolor', 'rcolor': 'rcolor', 'change': 'change', 'fse': 'fse', 'stacksize': 'stacksize', 'first': 'first', 'second': 'second', 'edge': 'edge'}
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
    sum = None
    lcolor = None
    rcolor = None
    # change是线段树的懒更新信息
    # change[i] == 0 代表没有懒更新信息
    # change[i] != 0 代表颜色重置为change[i]
    change = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_Coloring2.next, ((_java_obj_1 := Code05_Coloring2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_Coloring2.head[u])
        Code05_Coloring2.to[Code05_Coloring2.cntg] = jcast('int', v)
        Code05_Coloring2.head[u] = jcast('int', Code05_Coloring2.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code05_Coloring2.fa[u] = jcast('int', f)
        Code05_Coloring2.dep[u] = jcast('int', jcast('int', jadd(Code05_Coloring2.dep[f], 1)))
        Code05_Coloring2.siz[u] = jcast('int', 1)
        e = jcast('int', Code05_Coloring2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code05_Coloring2.to[e])
            if (v != f):
                Code05_Coloring2.dfs1(v, u)
            e = jcast('int', Code05_Coloring2.next[e])
        e = jcast('int', Code05_Coloring2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code05_Coloring2.to[e])
            if (v != f):
                Code05_Coloring2.siz[u] = jcast('int', jcast('int', jadd(Code05_Coloring2.siz[u], Code05_Coloring2.siz[v])))
                if ((Code05_Coloring2.son[u] == 0) or (Code05_Coloring2.siz[Code05_Coloring2.son[u]] < Code05_Coloring2.siz[v])):
                    Code05_Coloring2.son[u] = jcast('int', v)
            e = jcast('int', Code05_Coloring2.next[e])

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code05_Coloring2.top[u] = jcast('int', t)
        jset(Code05_Coloring2.dfn, u, ((_java_obj_4 := Code05_Coloring2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code05_Coloring2.seg[Code05_Coloring2.cntd] = jcast('int', u)
        if (Code05_Coloring2.son[u] == 0):
            return
        Code05_Coloring2.dfs2(Code05_Coloring2.son[u], t)
        e = jcast('int', Code05_Coloring2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code05_Coloring2.to[e])
            if ((v != Code05_Coloring2.fa[u]) and (v != Code05_Coloring2.son[u])):
                Code05_Coloring2.dfs2(v, v)
            e = jcast('int', Code05_Coloring2.next[e])

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
        jset(Code05_Coloring2.fse[Code05_Coloring2.stacksize], 0, fir)
        jset(Code05_Coloring2.fse[Code05_Coloring2.stacksize], 1, sec)
        jset(Code05_Coloring2.fse[Code05_Coloring2.stacksize], 2, edg)
        Code05_Coloring2.stacksize = jcast('int', (Code05_Coloring2.stacksize + 1))

    @staticmethod
    def pop():
        Code05_Coloring2.stacksize = jcast('int', (Code05_Coloring2.stacksize - 1))
        Code05_Coloring2.first = jcast('int', Code05_Coloring2.fse[Code05_Coloring2.stacksize][0])
        Code05_Coloring2.second = jcast('int', Code05_Coloring2.fse[Code05_Coloring2.stacksize][1])
        Code05_Coloring2.edge = jcast('int', Code05_Coloring2.fse[Code05_Coloring2.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs3():
        Code05_Coloring2.stacksize = jcast('int', 0)
        Code05_Coloring2.push(1, 0, jcast('int', (-1)))
        while (Code05_Coloring2.stacksize > 0):
            Code05_Coloring2.pop()
            if (Code05_Coloring2.edge == jcast('int', (-1))):
                Code05_Coloring2.fa[Code05_Coloring2.first] = jcast('int', Code05_Coloring2.second)
                Code05_Coloring2.dep[Code05_Coloring2.first] = jcast('int', jcast('int', jadd(Code05_Coloring2.dep[Code05_Coloring2.second], 1)))
                Code05_Coloring2.siz[Code05_Coloring2.first] = jcast('int', 1)
                Code05_Coloring2.edge = jcast('int', Code05_Coloring2.head[Code05_Coloring2.first])
            else:
                Code05_Coloring2.edge = jcast('int', Code05_Coloring2.next[Code05_Coloring2.edge])
            if (Code05_Coloring2.edge != 0):
                Code05_Coloring2.push(Code05_Coloring2.first, Code05_Coloring2.second, Code05_Coloring2.edge)
                if (Code05_Coloring2.to[Code05_Coloring2.edge] != Code05_Coloring2.second):
                    Code05_Coloring2.push(Code05_Coloring2.to[Code05_Coloring2.edge], Code05_Coloring2.first, jcast('int', (-1)))
            else:
                e = jcast('int', Code05_Coloring2.head[Code05_Coloring2.first])
                v = 0
                while (e > 0):
                    v = jcast('int', Code05_Coloring2.to[e])
                    if (v != Code05_Coloring2.second):
                        Code05_Coloring2.siz[Code05_Coloring2.first] = jcast('int', jcast('int', jadd(Code05_Coloring2.siz[Code05_Coloring2.first], Code05_Coloring2.siz[v])))
                        if ((Code05_Coloring2.son[Code05_Coloring2.first] == 0) or (Code05_Coloring2.siz[Code05_Coloring2.son[Code05_Coloring2.first]] < Code05_Coloring2.siz[v])):
                            Code05_Coloring2.son[Code05_Coloring2.first] = jcast('int', v)
                    e = jcast('int', Code05_Coloring2.next[e])

    # dfs2的迭代版
    @staticmethod
    def dfs4():
        Code05_Coloring2.stacksize = jcast('int', 0)
        Code05_Coloring2.push(1, 1, jcast('int', (-1)))
        while (Code05_Coloring2.stacksize > 0):
            try:
                Code05_Coloring2.pop()
                # edge == -1，表示第一次来到当前节点，并且先处理重儿子
                if (Code05_Coloring2.edge == jcast('int', (-1))):
                    Code05_Coloring2.top[Code05_Coloring2.first] = jcast('int', Code05_Coloring2.second)
                    jset(Code05_Coloring2.dfn, Code05_Coloring2.first, ((_java_obj_8 := Code05_Coloring2), (_java_key_9 := 'cntd'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3])
                    Code05_Coloring2.seg[Code05_Coloring2.cntd] = jcast('int', Code05_Coloring2.first)
                    if (Code05_Coloring2.son[Code05_Coloring2.first] == 0):
                        raise JContinue(None)
                    Code05_Coloring2.push(Code05_Coloring2.first, Code05_Coloring2.second, jcast('int', (-2)))
                    Code05_Coloring2.push(Code05_Coloring2.son[Code05_Coloring2.first], Code05_Coloring2.second, jcast('int', (-1)))
                    raise JContinue(None)
                    # edge == -2，表示处理完当前节点的重儿子，回到了当前节点
                else:
                    if (Code05_Coloring2.edge == jcast('int', (-2))):
                        Code05_Coloring2.edge = jcast('int', Code05_Coloring2.head[Code05_Coloring2.first])
                        # edge >= 0, 继续处理其他的边
                    else:
                        Code05_Coloring2.edge = jcast('int', Code05_Coloring2.next[Code05_Coloring2.edge])
                if (Code05_Coloring2.edge != 0):
                    Code05_Coloring2.push(Code05_Coloring2.first, Code05_Coloring2.second, Code05_Coloring2.edge)
                    if ((Code05_Coloring2.to[Code05_Coloring2.edge] != Code05_Coloring2.fa[Code05_Coloring2.first]) and (Code05_Coloring2.to[Code05_Coloring2.edge] != Code05_Coloring2.son[Code05_Coloring2.first])):
                        Code05_Coloring2.push(Code05_Coloring2.to[Code05_Coloring2.edge], Code05_Coloring2.to[Code05_Coloring2.edge], jcast('int', (-1)))
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
        Code05_Coloring2.sum[i] = jcast('int', jcast('int', jadd(Code05_Coloring2.sum[jcast('int', (i << (1 & 31)))], Code05_Coloring2.sum[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
        if (Code05_Coloring2.rcolor[jcast('int', (i << (1 & 31)))] == Code05_Coloring2.lcolor[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]):
            Code05_Coloring2.sum[i] = jcast('int', (Code05_Coloring2.sum[i] - 1))
        Code05_Coloring2.lcolor[i] = jcast('int', Code05_Coloring2.lcolor[jcast('int', (i << (1 & 31)))])
        Code05_Coloring2.rcolor[i] = jcast('int', Code05_Coloring2.rcolor[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])

    @staticmethod
    def lazy(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        Code05_Coloring2.sum[i] = jcast('int', 1)
        Code05_Coloring2.lcolor[i] = jcast('int', v)
        Code05_Coloring2.rcolor[i] = jcast('int', v)
        Code05_Coloring2.change[i] = jcast('int', v)

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if (Code05_Coloring2.change[i] != 0):
            Code05_Coloring2.lazy(jcast('int', (i << (1 & 31))), Code05_Coloring2.change[i])
            Code05_Coloring2.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code05_Coloring2.change[i])
            Code05_Coloring2.change[i] = jcast('int', 0)

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code05_Coloring2.sum[i] = jcast('int', 1)
            Code05_Coloring2.lcolor[i] = jcast('int', Code05_Coloring2.arr[Code05_Coloring2.seg[l]])
            Code05_Coloring2.rcolor[i] = jcast('int', Code05_Coloring2.arr[Code05_Coloring2.seg[l]])
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            Code05_Coloring2.build(l, mid, jcast('int', (i << (1 & 31))))
            Code05_Coloring2.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code05_Coloring2.up(i)

    @staticmethod
    def update(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code05_Coloring2.lazy(i, jobv)
        else:
            Code05_Coloring2.down(i)
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobl <= mid):
                Code05_Coloring2.update(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code05_Coloring2.update(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code05_Coloring2.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code05_Coloring2.sum[i])
        Code05_Coloring2.down(i)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        if (jobr <= mid):
            return jcast('int', Code05_Coloring2.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))
        else:
            if (jobl > mid):
                return jcast('int', Code05_Coloring2.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))
            else:
                ans = jcast('int', jcast('int', jadd(Code05_Coloring2.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))), Code05_Coloring2.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
                if (Code05_Coloring2.rcolor[jcast('int', (i << (1 & 31)))] == Code05_Coloring2.lcolor[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]):
                    ans = jcast('int', (ans - 1))
                return jcast('int', ans)

    # 查询单点颜色，jobi为节点的dfn序号
    @staticmethod
    def pointColor(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            return jcast('int', Code05_Coloring2.lcolor[i])
        Code05_Coloring2.down(i)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        if (jobi <= mid):
            return jcast('int', Code05_Coloring2.pointColor(jobi, l, mid, jcast('int', (i << (1 & 31)))))
        else:
            return jcast('int', Code05_Coloring2.pointColor(jobi, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))

    @staticmethod
    def pathUpdate(x, y, v):
        x = jcast('int', x)
        y = jcast('int', y)
        v = jcast('int', v)
        while (Code05_Coloring2.top[x] != Code05_Coloring2.top[y]):
            if (Code05_Coloring2.dep[Code05_Coloring2.top[x]] <= Code05_Coloring2.dep[Code05_Coloring2.top[y]]):
                Code05_Coloring2.update(Code05_Coloring2.dfn[Code05_Coloring2.top[y]], Code05_Coloring2.dfn[y], v, 1, Code05_Coloring2.n, 1)
                y = jcast('int', Code05_Coloring2.fa[Code05_Coloring2.top[y]])
            else:
                Code05_Coloring2.update(Code05_Coloring2.dfn[Code05_Coloring2.top[x]], Code05_Coloring2.dfn[x], v, 1, Code05_Coloring2.n, 1)
                x = jcast('int', Code05_Coloring2.fa[Code05_Coloring2.top[x]])
        Code05_Coloring2.update(jstatic('Math', 'min', Code05_Coloring2.dfn[x], Code05_Coloring2.dfn[y]), jstatic('Math', 'max', Code05_Coloring2.dfn[x], Code05_Coloring2.dfn[y]), v, 1, Code05_Coloring2.n, 1)

    @staticmethod
    def pathColors(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        ans = jcast('int', 0)
        sonc = 0
        fac = 0
        while (Code05_Coloring2.top[x] != Code05_Coloring2.top[y]):
            if (Code05_Coloring2.dep[Code05_Coloring2.top[x]] <= Code05_Coloring2.dep[Code05_Coloring2.top[y]]):
                ans = jcast('int', jcast('int', jadd(ans, Code05_Coloring2.query(Code05_Coloring2.dfn[Code05_Coloring2.top[y]], Code05_Coloring2.dfn[y], 1, Code05_Coloring2.n, 1))))
                sonc = jcast('int', Code05_Coloring2.pointColor(Code05_Coloring2.dfn[Code05_Coloring2.top[y]], 1, Code05_Coloring2.n, 1))
                fac = jcast('int', Code05_Coloring2.pointColor(Code05_Coloring2.dfn[Code05_Coloring2.fa[Code05_Coloring2.top[y]]], 1, Code05_Coloring2.n, 1))
                y = jcast('int', Code05_Coloring2.fa[Code05_Coloring2.top[y]])
            else:
                ans = jcast('int', jcast('int', jadd(ans, Code05_Coloring2.query(Code05_Coloring2.dfn[Code05_Coloring2.top[x]], Code05_Coloring2.dfn[x], 1, Code05_Coloring2.n, 1))))
                sonc = jcast('int', Code05_Coloring2.pointColor(Code05_Coloring2.dfn[Code05_Coloring2.top[x]], 1, Code05_Coloring2.n, 1))
                fac = jcast('int', Code05_Coloring2.pointColor(Code05_Coloring2.dfn[Code05_Coloring2.fa[Code05_Coloring2.top[x]]], 1, Code05_Coloring2.n, 1))
                x = jcast('int', Code05_Coloring2.fa[Code05_Coloring2.top[x]])
            if (sonc == fac):
                ans = jcast('int', (ans - 1))
        ans = jcast('int', jcast('int', jadd(ans, Code05_Coloring2.query(jstatic('Math', 'min', Code05_Coloring2.dfn[x], Code05_Coloring2.dfn[y]), jstatic('Math', 'max', Code05_Coloring2.dfn[x], Code05_Coloring2.dfn[y]), 1, Code05_Coloring2.n, 1))))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        io = Code05_Coloring2.Kattio(_java_ctor=0)
        Code05_Coloring2.n = jcast('int', jcall(io, 'nextInt'))
        Code05_Coloring2.m = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_Coloring2.n):
            jset(Code05_Coloring2.arr, i, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code05_Coloring2.n):
            u = jcast('int', jcall(io, 'nextInt'))
            v = jcast('int', jcall(io, 'nextInt'))
            Code05_Coloring2.addEdge(u, v)
            Code05_Coloring2.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code05_Coloring2.dfs3()
        Code05_Coloring2.dfs4()
        Code05_Coloring2.build(1, Code05_Coloring2.n, 1)
        op = None
        x = 0
        y = 0
        z = 0
        i = jcast('int', 1)
        while (i <= Code05_Coloring2.m):
            op = jcall(io, 'next')
            x = jcast('int', jcall(io, 'nextInt'))
            y = jcast('int', jcall(io, 'nextInt'))
            if jcall(op, 'equals', 'C'):
                z = jcast('int', jcall(io, 'nextInt'))
                Code05_Coloring2.pathUpdate(x, y, z)
            else:
                jcall(io, 'println', Code05_Coloring2.pathColors(x, y))
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
            raise TypeError("No matching overload for Code05_Coloring2.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Coloring2.MAXN = jcast('int', 100001)
Code05_Coloring2.n = jcast('int', 0)
Code05_Coloring2.m = jcast('int', 0)
Code05_Coloring2.arr = jarray('int', [Code05_Coloring2.MAXN])
Code05_Coloring2.head = jarray('int', [Code05_Coloring2.MAXN])
Code05_Coloring2.next = jarray('int', [jcast('int', (Code05_Coloring2.MAXN << (1 & 31)))])
Code05_Coloring2.to = jarray('int', [jcast('int', (Code05_Coloring2.MAXN << (1 & 31)))])
Code05_Coloring2.cntg = jcast('int', 0)
Code05_Coloring2.fa = jarray('int', [Code05_Coloring2.MAXN])
Code05_Coloring2.dep = jarray('int', [Code05_Coloring2.MAXN])
Code05_Coloring2.siz = jarray('int', [Code05_Coloring2.MAXN])
Code05_Coloring2.son = jarray('int', [Code05_Coloring2.MAXN])
Code05_Coloring2.top = jarray('int', [Code05_Coloring2.MAXN])
Code05_Coloring2.dfn = jarray('int', [Code05_Coloring2.MAXN])
Code05_Coloring2.seg = jarray('int', [Code05_Coloring2.MAXN])
Code05_Coloring2.cntd = jcast('int', 0)
Code05_Coloring2.sum = jarray('int', [jcast('int', (Code05_Coloring2.MAXN << (2 & 31)))])
Code05_Coloring2.lcolor = jarray('int', [jcast('int', (Code05_Coloring2.MAXN << (2 & 31)))])
Code05_Coloring2.rcolor = jarray('int', [jcast('int', (Code05_Coloring2.MAXN << (2 & 31)))])
Code05_Coloring2.change = jarray('int', [jcast('int', (Code05_Coloring2.MAXN << (2 & 31)))])
Code05_Coloring2.fse = jarray('int', [Code05_Coloring2.MAXN, 3])
Code05_Coloring2.stacksize = jcast('int', 0)
Code05_Coloring2.first = jcast('int', 0)
Code05_Coloring2.second = jcast('int', 0)
Code05_Coloring2.edge = jcast('int', 0)

if __name__ == '__main__':
    Code05_Coloring2.main([])
