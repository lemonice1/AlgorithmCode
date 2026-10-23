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

# 路径最大值与累加和，Python版
# 一共有n个节点，给定n-1条边，节点连成一棵树，每个节点给定权值
# 一共有m条操作，每种操作是如下3种类型中的一种
# 操作 CHANGE x y : x的权值修改为y
# 操作 QMAX x y   : x到y的路径上，打印节点值的最大值
# 操作 QSUM x y   : x到y的路径上，打印节点值的累加和
# 1 <= n <= 3 * 10^4
# 0 <= m <= 2 * 10^5
# -30000 <= 节点权值 <= +30000
# 测试链接 : https://www.luogu.com.cn/problem/P2590
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_PathMaxAndSum1:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'm': 'm', 'arr': 'arr', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'dfn': 'dfn', 'seg': 'seg', 'cntd': 'cntd', 'max': 'max', 'sum': 'sum', 'fse': 'fse', 'stacksize': 'stacksize', 'first': 'first', 'second': 'second', 'edge': 'edge'}
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
    sum = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_PathMaxAndSum1.next, ((_java_obj_1 := Code03_PathMaxAndSum1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_PathMaxAndSum1.head[u])
        Code03_PathMaxAndSum1.to[Code03_PathMaxAndSum1.cntg] = jcast('int', v)
        Code03_PathMaxAndSum1.head[u] = jcast('int', Code03_PathMaxAndSum1.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code03_PathMaxAndSum1.fa[u] = jcast('int', f)
        Code03_PathMaxAndSum1.dep[u] = jcast('int', jcast('int', jadd(Code03_PathMaxAndSum1.dep[f], 1)))
        Code03_PathMaxAndSum1.siz[u] = jcast('int', 1)
        e = jcast('int', Code03_PathMaxAndSum1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code03_PathMaxAndSum1.to[e])
            if (v != f):
                Code03_PathMaxAndSum1.dfs1(v, u)
            e = jcast('int', Code03_PathMaxAndSum1.next[e])
        e = jcast('int', Code03_PathMaxAndSum1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code03_PathMaxAndSum1.to[e])
            if (v != f):
                Code03_PathMaxAndSum1.siz[u] = jcast('int', jcast('int', jadd(Code03_PathMaxAndSum1.siz[u], Code03_PathMaxAndSum1.siz[v])))
                if ((Code03_PathMaxAndSum1.son[u] == 0) or (Code03_PathMaxAndSum1.siz[Code03_PathMaxAndSum1.son[u]] < Code03_PathMaxAndSum1.siz[v])):
                    Code03_PathMaxAndSum1.son[u] = jcast('int', v)
            e = jcast('int', Code03_PathMaxAndSum1.next[e])

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code03_PathMaxAndSum1.top[u] = jcast('int', t)
        jset(Code03_PathMaxAndSum1.dfn, u, ((_java_obj_4 := Code03_PathMaxAndSum1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code03_PathMaxAndSum1.seg[Code03_PathMaxAndSum1.cntd] = jcast('int', u)
        if (Code03_PathMaxAndSum1.son[u] == 0):
            return
        Code03_PathMaxAndSum1.dfs2(Code03_PathMaxAndSum1.son[u], t)
        e = jcast('int', Code03_PathMaxAndSum1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code03_PathMaxAndSum1.to[e])
            if ((v != Code03_PathMaxAndSum1.fa[u]) and (v != Code03_PathMaxAndSum1.son[u])):
                Code03_PathMaxAndSum1.dfs2(v, v)
            e = jcast('int', Code03_PathMaxAndSum1.next[e])

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
        jset(Code03_PathMaxAndSum1.fse[Code03_PathMaxAndSum1.stacksize], 0, fir)
        jset(Code03_PathMaxAndSum1.fse[Code03_PathMaxAndSum1.stacksize], 1, sec)
        jset(Code03_PathMaxAndSum1.fse[Code03_PathMaxAndSum1.stacksize], 2, edg)
        Code03_PathMaxAndSum1.stacksize = jcast('int', (Code03_PathMaxAndSum1.stacksize + 1))

    @staticmethod
    def pop():
        Code03_PathMaxAndSum1.stacksize = jcast('int', (Code03_PathMaxAndSum1.stacksize - 1))
        Code03_PathMaxAndSum1.first = jcast('int', Code03_PathMaxAndSum1.fse[Code03_PathMaxAndSum1.stacksize][0])
        Code03_PathMaxAndSum1.second = jcast('int', Code03_PathMaxAndSum1.fse[Code03_PathMaxAndSum1.stacksize][1])
        Code03_PathMaxAndSum1.edge = jcast('int', Code03_PathMaxAndSum1.fse[Code03_PathMaxAndSum1.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs3():
        Code03_PathMaxAndSum1.stacksize = jcast('int', 0)
        Code03_PathMaxAndSum1.push(1, 0, jcast('int', (-1)))
        while (Code03_PathMaxAndSum1.stacksize > 0):
            Code03_PathMaxAndSum1.pop()
            if (Code03_PathMaxAndSum1.edge == jcast('int', (-1))):
                Code03_PathMaxAndSum1.fa[Code03_PathMaxAndSum1.first] = jcast('int', Code03_PathMaxAndSum1.second)
                Code03_PathMaxAndSum1.dep[Code03_PathMaxAndSum1.first] = jcast('int', jcast('int', jadd(Code03_PathMaxAndSum1.dep[Code03_PathMaxAndSum1.second], 1)))
                Code03_PathMaxAndSum1.siz[Code03_PathMaxAndSum1.first] = jcast('int', 1)
                Code03_PathMaxAndSum1.edge = jcast('int', Code03_PathMaxAndSum1.head[Code03_PathMaxAndSum1.first])
            else:
                Code03_PathMaxAndSum1.edge = jcast('int', Code03_PathMaxAndSum1.next[Code03_PathMaxAndSum1.edge])
            if (Code03_PathMaxAndSum1.edge != 0):
                Code03_PathMaxAndSum1.push(Code03_PathMaxAndSum1.first, Code03_PathMaxAndSum1.second, Code03_PathMaxAndSum1.edge)
                if (Code03_PathMaxAndSum1.to[Code03_PathMaxAndSum1.edge] != Code03_PathMaxAndSum1.second):
                    Code03_PathMaxAndSum1.push(Code03_PathMaxAndSum1.to[Code03_PathMaxAndSum1.edge], Code03_PathMaxAndSum1.first, jcast('int', (-1)))
            else:
                e = jcast('int', Code03_PathMaxAndSum1.head[Code03_PathMaxAndSum1.first])
                v = 0
                while (e > 0):
                    v = jcast('int', Code03_PathMaxAndSum1.to[e])
                    if (v != Code03_PathMaxAndSum1.second):
                        Code03_PathMaxAndSum1.siz[Code03_PathMaxAndSum1.first] = jcast('int', jcast('int', jadd(Code03_PathMaxAndSum1.siz[Code03_PathMaxAndSum1.first], Code03_PathMaxAndSum1.siz[v])))
                        if ((Code03_PathMaxAndSum1.son[Code03_PathMaxAndSum1.first] == 0) or (Code03_PathMaxAndSum1.siz[Code03_PathMaxAndSum1.son[Code03_PathMaxAndSum1.first]] < Code03_PathMaxAndSum1.siz[v])):
                            Code03_PathMaxAndSum1.son[Code03_PathMaxAndSum1.first] = jcast('int', v)
                    e = jcast('int', Code03_PathMaxAndSum1.next[e])

    # dfs2的迭代版
    @staticmethod
    def dfs4():
        Code03_PathMaxAndSum1.stacksize = jcast('int', 0)
        Code03_PathMaxAndSum1.push(1, 1, jcast('int', (-1)))
        while (Code03_PathMaxAndSum1.stacksize > 0):
            try:
                Code03_PathMaxAndSum1.pop()
                # edge == -1，表示第一次来到当前节点，并且先处理重儿子
                if (Code03_PathMaxAndSum1.edge == jcast('int', (-1))):
                    Code03_PathMaxAndSum1.top[Code03_PathMaxAndSum1.first] = jcast('int', Code03_PathMaxAndSum1.second)
                    jset(Code03_PathMaxAndSum1.dfn, Code03_PathMaxAndSum1.first, ((_java_obj_8 := Code03_PathMaxAndSum1), (_java_key_9 := 'cntd'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3])
                    Code03_PathMaxAndSum1.seg[Code03_PathMaxAndSum1.cntd] = jcast('int', Code03_PathMaxAndSum1.first)
                    if (Code03_PathMaxAndSum1.son[Code03_PathMaxAndSum1.first] == 0):
                        raise JContinue(None)
                    Code03_PathMaxAndSum1.push(Code03_PathMaxAndSum1.first, Code03_PathMaxAndSum1.second, jcast('int', (-2)))
                    Code03_PathMaxAndSum1.push(Code03_PathMaxAndSum1.son[Code03_PathMaxAndSum1.first], Code03_PathMaxAndSum1.second, jcast('int', (-1)))
                    raise JContinue(None)
                    # edge == -2，表示处理完当前节点的重儿子，回到了当前节点
                else:
                    if (Code03_PathMaxAndSum1.edge == jcast('int', (-2))):
                        Code03_PathMaxAndSum1.edge = jcast('int', Code03_PathMaxAndSum1.head[Code03_PathMaxAndSum1.first])
                        # edge >= 0, 继续处理其他的边
                    else:
                        Code03_PathMaxAndSum1.edge = jcast('int', Code03_PathMaxAndSum1.next[Code03_PathMaxAndSum1.edge])
                if (Code03_PathMaxAndSum1.edge != 0):
                    Code03_PathMaxAndSum1.push(Code03_PathMaxAndSum1.first, Code03_PathMaxAndSum1.second, Code03_PathMaxAndSum1.edge)
                    if ((Code03_PathMaxAndSum1.to[Code03_PathMaxAndSum1.edge] != Code03_PathMaxAndSum1.fa[Code03_PathMaxAndSum1.first]) and (Code03_PathMaxAndSum1.to[Code03_PathMaxAndSum1.edge] != Code03_PathMaxAndSum1.son[Code03_PathMaxAndSum1.first])):
                        Code03_PathMaxAndSum1.push(Code03_PathMaxAndSum1.to[Code03_PathMaxAndSum1.edge], Code03_PathMaxAndSum1.to[Code03_PathMaxAndSum1.edge], jcast('int', (-1)))
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
        Code03_PathMaxAndSum1.sum[i] = jcast('int', jcast('int', jadd(Code03_PathMaxAndSum1.sum[jcast('int', (i << (1 & 31)))], Code03_PathMaxAndSum1.sum[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
        jset(Code03_PathMaxAndSum1.max, i, jstatic('Math', 'max', Code03_PathMaxAndSum1.max[jcast('int', (i << (1 & 31)))], Code03_PathMaxAndSum1.max[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            jset(Code03_PathMaxAndSum1.sum, i, jset(Code03_PathMaxAndSum1.max, i, Code03_PathMaxAndSum1.arr[Code03_PathMaxAndSum1.seg[l]]))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            Code03_PathMaxAndSum1.build(l, mid, jcast('int', (i << (1 & 31))))
            Code03_PathMaxAndSum1.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code03_PathMaxAndSum1.up(i)

    @staticmethod
    def update(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            jset(Code03_PathMaxAndSum1.sum, i, jset(Code03_PathMaxAndSum1.max, i, jobv))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                Code03_PathMaxAndSum1.update(jobi, jobv, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code03_PathMaxAndSum1.update(jobi, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code03_PathMaxAndSum1.up(i)

    @staticmethod
    def queryMax(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code03_PathMaxAndSum1.max[i])
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        ans = jcast('int', jcast('int', (-Code03_PathMaxAndSum1.INF)))
        if (jobl <= mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code03_PathMaxAndSum1.queryMax(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code03_PathMaxAndSum1.queryMax(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('int', ans)

    @staticmethod
    def querySum(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code03_PathMaxAndSum1.sum[i])
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        ans = jcast('int', 0)
        if (jobl <= mid):
            ans = jcast('int', jcast('int', jadd(ans, Code03_PathMaxAndSum1.querySum(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            ans = jcast('int', jcast('int', jadd(ans, Code03_PathMaxAndSum1.querySum(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('int', ans)

    @staticmethod
    def pointUpdate(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code03_PathMaxAndSum1.update(Code03_PathMaxAndSum1.dfn[u], v, 1, Code03_PathMaxAndSum1.n, 1)

    @staticmethod
    def pathMax(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        ans = jcast('int', jcast('int', (-Code03_PathMaxAndSum1.INF)))
        while (Code03_PathMaxAndSum1.top[x] != Code03_PathMaxAndSum1.top[y]):
            if (Code03_PathMaxAndSum1.dep[Code03_PathMaxAndSum1.top[x]] <= Code03_PathMaxAndSum1.dep[Code03_PathMaxAndSum1.top[y]]):
                ans = jcast('int', jstatic('Math', 'max', ans, Code03_PathMaxAndSum1.queryMax(Code03_PathMaxAndSum1.dfn[Code03_PathMaxAndSum1.top[y]], Code03_PathMaxAndSum1.dfn[y], 1, Code03_PathMaxAndSum1.n, 1)))
                y = jcast('int', Code03_PathMaxAndSum1.fa[Code03_PathMaxAndSum1.top[y]])
            else:
                ans = jcast('int', jstatic('Math', 'max', ans, Code03_PathMaxAndSum1.queryMax(Code03_PathMaxAndSum1.dfn[Code03_PathMaxAndSum1.top[x]], Code03_PathMaxAndSum1.dfn[x], 1, Code03_PathMaxAndSum1.n, 1)))
                x = jcast('int', Code03_PathMaxAndSum1.fa[Code03_PathMaxAndSum1.top[x]])
        ans = jcast('int', jstatic('Math', 'max', ans, Code03_PathMaxAndSum1.queryMax(jstatic('Math', 'min', Code03_PathMaxAndSum1.dfn[x], Code03_PathMaxAndSum1.dfn[y]), jstatic('Math', 'max', Code03_PathMaxAndSum1.dfn[x], Code03_PathMaxAndSum1.dfn[y]), 1, Code03_PathMaxAndSum1.n, 1)))
        return jcast('int', ans)

    @staticmethod
    def pathSum(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        ans = jcast('int', 0)
        while (Code03_PathMaxAndSum1.top[x] != Code03_PathMaxAndSum1.top[y]):
            if (Code03_PathMaxAndSum1.dep[Code03_PathMaxAndSum1.top[x]] <= Code03_PathMaxAndSum1.dep[Code03_PathMaxAndSum1.top[y]]):
                ans = jcast('int', jcast('int', jadd(ans, Code03_PathMaxAndSum1.querySum(Code03_PathMaxAndSum1.dfn[Code03_PathMaxAndSum1.top[y]], Code03_PathMaxAndSum1.dfn[y], 1, Code03_PathMaxAndSum1.n, 1))))
                y = jcast('int', Code03_PathMaxAndSum1.fa[Code03_PathMaxAndSum1.top[y]])
            else:
                ans = jcast('int', jcast('int', jadd(ans, Code03_PathMaxAndSum1.querySum(Code03_PathMaxAndSum1.dfn[Code03_PathMaxAndSum1.top[x]], Code03_PathMaxAndSum1.dfn[x], 1, Code03_PathMaxAndSum1.n, 1))))
                x = jcast('int', Code03_PathMaxAndSum1.fa[Code03_PathMaxAndSum1.top[x]])
        ans = jcast('int', jcast('int', jadd(ans, Code03_PathMaxAndSum1.querySum(jstatic('Math', 'min', Code03_PathMaxAndSum1.dfn[x], Code03_PathMaxAndSum1.dfn[y]), jstatic('Math', 'max', Code03_PathMaxAndSum1.dfn[x], Code03_PathMaxAndSum1.dfn[y]), 1, Code03_PathMaxAndSum1.n, 1))))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        io = Code03_PathMaxAndSum1.Kattio(_java_ctor=0)
        Code03_PathMaxAndSum1.n = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code03_PathMaxAndSum1.n):
            u = jcast('int', jcall(io, 'nextInt'))
            v = jcast('int', jcall(io, 'nextInt'))
            Code03_PathMaxAndSum1.addEdge(u, v)
            Code03_PathMaxAndSum1.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_PathMaxAndSum1.n):
            jset(Code03_PathMaxAndSum1.arr, i, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        # dfs3() 等同于 dfs1(1, 0)，调用迭代版防止爆栈
        Code03_PathMaxAndSum1.dfs3()
        # dfs4() 等同于 dfs2(1, 1)，调用迭代版防止爆栈
        Code03_PathMaxAndSum1.dfs4()
        Code03_PathMaxAndSum1.build(1, Code03_PathMaxAndSum1.n, 1)
        Code03_PathMaxAndSum1.m = jcast('int', jcall(io, 'nextInt'))
        op = None
        x = 0
        y = 0
        i = jcast('int', 1)
        while (i <= Code03_PathMaxAndSum1.m):
            op = jcall(io, 'next')
            x = jcast('int', jcall(io, 'nextInt'))
            y = jcast('int', jcall(io, 'nextInt'))
            if jcall(op, 'equals', 'CHANGE'):
                Code03_PathMaxAndSum1.pointUpdate(x, y)
            else:
                if jcall(op, 'equals', 'QMAX'):
                    jcall(io, 'println', Code03_PathMaxAndSum1.pathMax(x, y))
                else:
                    jcall(io, 'println', Code03_PathMaxAndSum1.pathSum(x, y))
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
            raise TypeError("No matching overload for Code03_PathMaxAndSum1.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_PathMaxAndSum1.MAXN = jcast('int', 30001)
Code03_PathMaxAndSum1.INF = jcast('int', 10000001)
Code03_PathMaxAndSum1.n = jcast('int', 0)
Code03_PathMaxAndSum1.m = jcast('int', 0)
Code03_PathMaxAndSum1.arr = jarray('int', [Code03_PathMaxAndSum1.MAXN])
Code03_PathMaxAndSum1.head = jarray('int', [Code03_PathMaxAndSum1.MAXN])
Code03_PathMaxAndSum1.next = jarray('int', [jcast('int', (Code03_PathMaxAndSum1.MAXN << (1 & 31)))])
Code03_PathMaxAndSum1.to = jarray('int', [jcast('int', (Code03_PathMaxAndSum1.MAXN << (1 & 31)))])
Code03_PathMaxAndSum1.cntg = jcast('int', 0)
Code03_PathMaxAndSum1.fa = jarray('int', [Code03_PathMaxAndSum1.MAXN])
Code03_PathMaxAndSum1.dep = jarray('int', [Code03_PathMaxAndSum1.MAXN])
Code03_PathMaxAndSum1.siz = jarray('int', [Code03_PathMaxAndSum1.MAXN])
Code03_PathMaxAndSum1.son = jarray('int', [Code03_PathMaxAndSum1.MAXN])
Code03_PathMaxAndSum1.top = jarray('int', [Code03_PathMaxAndSum1.MAXN])
Code03_PathMaxAndSum1.dfn = jarray('int', [Code03_PathMaxAndSum1.MAXN])
Code03_PathMaxAndSum1.seg = jarray('int', [Code03_PathMaxAndSum1.MAXN])
Code03_PathMaxAndSum1.cntd = jcast('int', 0)
Code03_PathMaxAndSum1.max = jarray('int', [jcast('int', (Code03_PathMaxAndSum1.MAXN << (2 & 31)))])
Code03_PathMaxAndSum1.sum = jarray('int', [jcast('int', (Code03_PathMaxAndSum1.MAXN << (2 & 31)))])
Code03_PathMaxAndSum1.fse = jarray('int', [Code03_PathMaxAndSum1.MAXN, 3])
Code03_PathMaxAndSum1.stacksize = jcast('int', 0)
Code03_PathMaxAndSum1.first = jcast('int', 0)
Code03_PathMaxAndSum1.second = jcast('int', 0)
Code03_PathMaxAndSum1.edge = jcast('int', 0)

if __name__ == '__main__':
    Code03_PathMaxAndSum1.main([])
