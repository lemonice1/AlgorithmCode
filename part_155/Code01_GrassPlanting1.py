# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 边权转化为点权的模版题，Python版
# 一共有n个节点，给定n-1条边，节点连成一棵树，初始时所有边的权值为0
# 一共有m条操作，每条操作是如下2种类型中的一种
# 操作 P x y : x到y的路径上，每条边的权值增加1
# 操作 Q x y : x和y保证是直接连接的，查询他们之间的边权
# 1 <= n、m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3038
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_GrassPlanting1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'dfn': 'dfn', 'cntd': 'cntd', 'sum': 'sum', 'addTag': 'addTag', 'fse': 'fse', 'stacksize': 'stacksize', 'first': 'first', 'second': 'second', 'edge': 'edge'}
    MAXN = 0
    n = 0
    m = 0
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
    addTag = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_GrassPlanting1.next, ((_java_obj_1 := Code01_GrassPlanting1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_GrassPlanting1.head[u])
        Code01_GrassPlanting1.to[Code01_GrassPlanting1.cntg] = jcast('int', v)
        Code01_GrassPlanting1.head[u] = jcast('int', Code01_GrassPlanting1.cntg)

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code01_GrassPlanting1.fa[u] = jcast('int', f)
        Code01_GrassPlanting1.dep[u] = jcast('int', jcast('int', jadd(Code01_GrassPlanting1.dep[f], 1)))
        Code01_GrassPlanting1.siz[u] = jcast('int', 1)
        e = jcast('int', Code01_GrassPlanting1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code01_GrassPlanting1.to[e])
            if (v != f):
                Code01_GrassPlanting1.dfs1(v, u)
            e = jcast('int', Code01_GrassPlanting1.next[e])
        e = jcast('int', Code01_GrassPlanting1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code01_GrassPlanting1.to[e])
            if (v != f):
                Code01_GrassPlanting1.siz[u] = jcast('int', jcast('int', jadd(Code01_GrassPlanting1.siz[u], Code01_GrassPlanting1.siz[v])))
                if ((Code01_GrassPlanting1.son[u] == 0) or (Code01_GrassPlanting1.siz[Code01_GrassPlanting1.son[u]] < Code01_GrassPlanting1.siz[v])):
                    Code01_GrassPlanting1.son[u] = jcast('int', v)
            e = jcast('int', Code01_GrassPlanting1.next[e])

    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code01_GrassPlanting1.top[u] = jcast('int', t)
        jset(Code01_GrassPlanting1.dfn, u, ((_java_obj_4 := Code01_GrassPlanting1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        if (Code01_GrassPlanting1.son[u] == 0):
            return
        Code01_GrassPlanting1.dfs2(Code01_GrassPlanting1.son[u], t)
        e = jcast('int', Code01_GrassPlanting1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code01_GrassPlanting1.to[e])
            if ((v != Code01_GrassPlanting1.fa[u]) and (v != Code01_GrassPlanting1.son[u])):
                Code01_GrassPlanting1.dfs2(v, v)
            e = jcast('int', Code01_GrassPlanting1.next[e])

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
        jset(Code01_GrassPlanting1.fse[Code01_GrassPlanting1.stacksize], 0, fir)
        jset(Code01_GrassPlanting1.fse[Code01_GrassPlanting1.stacksize], 1, sec)
        jset(Code01_GrassPlanting1.fse[Code01_GrassPlanting1.stacksize], 2, edg)
        Code01_GrassPlanting1.stacksize = jcast('int', (Code01_GrassPlanting1.stacksize + 1))

    @staticmethod
    def pop():
        Code01_GrassPlanting1.stacksize = jcast('int', (Code01_GrassPlanting1.stacksize - 1))
        Code01_GrassPlanting1.first = jcast('int', Code01_GrassPlanting1.fse[Code01_GrassPlanting1.stacksize][0])
        Code01_GrassPlanting1.second = jcast('int', Code01_GrassPlanting1.fse[Code01_GrassPlanting1.stacksize][1])
        Code01_GrassPlanting1.edge = jcast('int', Code01_GrassPlanting1.fse[Code01_GrassPlanting1.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs3():
        Code01_GrassPlanting1.stacksize = jcast('int', 0)
        Code01_GrassPlanting1.push(1, 0, jcast('int', (-1)))
        while (Code01_GrassPlanting1.stacksize > 0):
            Code01_GrassPlanting1.pop()
            if (Code01_GrassPlanting1.edge == jcast('int', (-1))):
                Code01_GrassPlanting1.fa[Code01_GrassPlanting1.first] = jcast('int', Code01_GrassPlanting1.second)
                Code01_GrassPlanting1.dep[Code01_GrassPlanting1.first] = jcast('int', jcast('int', jadd(Code01_GrassPlanting1.dep[Code01_GrassPlanting1.second], 1)))
                Code01_GrassPlanting1.siz[Code01_GrassPlanting1.first] = jcast('int', 1)
                Code01_GrassPlanting1.edge = jcast('int', Code01_GrassPlanting1.head[Code01_GrassPlanting1.first])
            else:
                Code01_GrassPlanting1.edge = jcast('int', Code01_GrassPlanting1.next[Code01_GrassPlanting1.edge])
            if (Code01_GrassPlanting1.edge != 0):
                Code01_GrassPlanting1.push(Code01_GrassPlanting1.first, Code01_GrassPlanting1.second, Code01_GrassPlanting1.edge)
                if (Code01_GrassPlanting1.to[Code01_GrassPlanting1.edge] != Code01_GrassPlanting1.second):
                    Code01_GrassPlanting1.push(Code01_GrassPlanting1.to[Code01_GrassPlanting1.edge], Code01_GrassPlanting1.first, jcast('int', (-1)))
            else:
                e = jcast('int', Code01_GrassPlanting1.head[Code01_GrassPlanting1.first])
                v = 0
                while (e > 0):
                    v = jcast('int', Code01_GrassPlanting1.to[e])
                    if (v != Code01_GrassPlanting1.second):
                        Code01_GrassPlanting1.siz[Code01_GrassPlanting1.first] = jcast('int', jcast('int', jadd(Code01_GrassPlanting1.siz[Code01_GrassPlanting1.first], Code01_GrassPlanting1.siz[v])))
                        if ((Code01_GrassPlanting1.son[Code01_GrassPlanting1.first] == 0) or (Code01_GrassPlanting1.siz[Code01_GrassPlanting1.son[Code01_GrassPlanting1.first]] < Code01_GrassPlanting1.siz[v])):
                            Code01_GrassPlanting1.son[Code01_GrassPlanting1.first] = jcast('int', v)
                    e = jcast('int', Code01_GrassPlanting1.next[e])

    # dfs2的迭代版
    @staticmethod
    def dfs4():
        Code01_GrassPlanting1.stacksize = jcast('int', 0)
        Code01_GrassPlanting1.push(1, 1, jcast('int', (-1)))
        while (Code01_GrassPlanting1.stacksize > 0):
            try:
                Code01_GrassPlanting1.pop()
                if (Code01_GrassPlanting1.edge == jcast('int', (-1))):
                    Code01_GrassPlanting1.top[Code01_GrassPlanting1.first] = jcast('int', Code01_GrassPlanting1.second)
                    jset(Code01_GrassPlanting1.dfn, Code01_GrassPlanting1.first, ((_java_obj_8 := Code01_GrassPlanting1), (_java_key_9 := 'cntd'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3])
                    if (Code01_GrassPlanting1.son[Code01_GrassPlanting1.first] == 0):
                        raise JContinue(None)
                    Code01_GrassPlanting1.push(Code01_GrassPlanting1.first, Code01_GrassPlanting1.second, jcast('int', (-2)))
                    Code01_GrassPlanting1.push(Code01_GrassPlanting1.son[Code01_GrassPlanting1.first], Code01_GrassPlanting1.second, jcast('int', (-1)))
                    raise JContinue(None)
                else:
                    if (Code01_GrassPlanting1.edge == jcast('int', (-2))):
                        Code01_GrassPlanting1.edge = jcast('int', Code01_GrassPlanting1.head[Code01_GrassPlanting1.first])
                    else:
                        Code01_GrassPlanting1.edge = jcast('int', Code01_GrassPlanting1.next[Code01_GrassPlanting1.edge])
                if (Code01_GrassPlanting1.edge != 0):
                    Code01_GrassPlanting1.push(Code01_GrassPlanting1.first, Code01_GrassPlanting1.second, Code01_GrassPlanting1.edge)
                    if ((Code01_GrassPlanting1.to[Code01_GrassPlanting1.edge] != Code01_GrassPlanting1.fa[Code01_GrassPlanting1.first]) and (Code01_GrassPlanting1.to[Code01_GrassPlanting1.edge] != Code01_GrassPlanting1.son[Code01_GrassPlanting1.first])):
                        Code01_GrassPlanting1.push(Code01_GrassPlanting1.to[Code01_GrassPlanting1.edge], Code01_GrassPlanting1.to[Code01_GrassPlanting1.edge], jcast('int', (-1)))
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
        Code01_GrassPlanting1.sum[i] = jcast('int', jcast('int', jadd(Code01_GrassPlanting1.sum[jcast('int', (i << (1 & 31)))], Code01_GrassPlanting1.sum[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))

    @staticmethod
    def lazy(i, v, n):
        i = jcast('int', i)
        v = jcast('int', v)
        n = jcast('int', n)
        Code01_GrassPlanting1.sum[i] = jcast('int', jcast('int', jadd(Code01_GrassPlanting1.sum[i], jcast('int', (v * n)))))
        Code01_GrassPlanting1.addTag[i] = jcast('int', jcast('int', jadd(Code01_GrassPlanting1.addTag[i], v)))

    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        if (Code01_GrassPlanting1.addTag[i] != 0):
            Code01_GrassPlanting1.lazy(jcast('int', (i << (1 & 31))), Code01_GrassPlanting1.addTag[i], ln)
            Code01_GrassPlanting1.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code01_GrassPlanting1.addTag[i], rn)
            Code01_GrassPlanting1.addTag[i] = jcast('int', 0)

    # 范围增加
    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code01_GrassPlanting1.lazy(i, jobv, jcast('int', jadd(jcast('int', (r - l)), 1)))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            Code01_GrassPlanting1.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code01_GrassPlanting1.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code01_GrassPlanting1.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code01_GrassPlanting1.up(i)

    # 单点查询
    @staticmethod
    def query(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            return jcast('int', Code01_GrassPlanting1.sum[i])
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code01_GrassPlanting1.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
        if (jobi <= mid):
            return jcast('int', Code01_GrassPlanting1.query(jobi, l, mid, jcast('int', (i << (1 & 31)))))
        else:
            return jcast('int', Code01_GrassPlanting1.query(jobi, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))

    # x到y的路径上，每条边的边权变成下方点的点权
    # 每条边的边权增加v，就是若干点的点权增加v
    # 但是要注意！x和y的最低公共祖先，不能增加点权！
    @staticmethod
    def pathAdd(x, y, v):
        x = jcast('int', x)
        y = jcast('int', y)
        v = jcast('int', v)
        while (Code01_GrassPlanting1.top[x] != Code01_GrassPlanting1.top[y]):
            if (Code01_GrassPlanting1.dep[Code01_GrassPlanting1.top[x]] <= Code01_GrassPlanting1.dep[Code01_GrassPlanting1.top[y]]):
                Code01_GrassPlanting1.add(Code01_GrassPlanting1.dfn[Code01_GrassPlanting1.top[y]], Code01_GrassPlanting1.dfn[y], v, 1, Code01_GrassPlanting1.n, 1)
                y = jcast('int', Code01_GrassPlanting1.fa[Code01_GrassPlanting1.top[y]])
            else:
                Code01_GrassPlanting1.add(Code01_GrassPlanting1.dfn[Code01_GrassPlanting1.top[x]], Code01_GrassPlanting1.dfn[x], v, 1, Code01_GrassPlanting1.n, 1)
                x = jcast('int', Code01_GrassPlanting1.fa[Code01_GrassPlanting1.top[x]])
        # x和y的最低公共祖先，点权不增加！
        Code01_GrassPlanting1.add(jcast('int', jadd(jstatic('Math', 'min', Code01_GrassPlanting1.dfn[x], Code01_GrassPlanting1.dfn[y]), 1)), jstatic('Math', 'max', Code01_GrassPlanting1.dfn[x], Code01_GrassPlanting1.dfn[y]), v, 1, Code01_GrassPlanting1.n, 1)

    # 返回x和y之间这条边的边权
    @staticmethod
    def edgeQuery(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        down = jcast('int', jstatic('Math', 'max', Code01_GrassPlanting1.dfn[x], Code01_GrassPlanting1.dfn[y]))
        return jcast('int', Code01_GrassPlanting1.query(down, 1, Code01_GrassPlanting1.n, 1))

    @staticmethod
    def main(args):
        io = Code01_GrassPlanting1.Kattio(_java_ctor=0)
        Code01_GrassPlanting1.n = jcast('int', jcall(io, 'nextInt'))
        Code01_GrassPlanting1.m = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code01_GrassPlanting1.n):
            u = jcast('int', jcall(io, 'nextInt'))
            v = jcast('int', jcall(io, 'nextInt'))
            Code01_GrassPlanting1.addEdge(u, v)
            Code01_GrassPlanting1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code01_GrassPlanting1.dfs3()
        Code01_GrassPlanting1.dfs4()
        op = None
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= Code01_GrassPlanting1.m):
            op = jcall(io, 'next')
            x = jcast('int', jcall(io, 'nextInt'))
            y = jcast('int', jcall(io, 'nextInt'))
            if jcall(op, 'equals', 'P'):
                Code01_GrassPlanting1.pathAdd(x, y, 1)
            else:
                jcall(io, 'println', Code01_GrassPlanting1.edgeQuery(x, y))
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
            raise TypeError("No matching overload for Code01_GrassPlanting1.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_GrassPlanting1.MAXN = jcast('int', 100001)
Code01_GrassPlanting1.n = jcast('int', 0)
Code01_GrassPlanting1.m = jcast('int', 0)
Code01_GrassPlanting1.head = jarray('int', [Code01_GrassPlanting1.MAXN])
Code01_GrassPlanting1.next = jarray('int', [jcast('int', (Code01_GrassPlanting1.MAXN << (1 & 31)))])
Code01_GrassPlanting1.to = jarray('int', [jcast('int', (Code01_GrassPlanting1.MAXN << (1 & 31)))])
Code01_GrassPlanting1.cntg = jcast('int', 0)
Code01_GrassPlanting1.fa = jarray('int', [Code01_GrassPlanting1.MAXN])
Code01_GrassPlanting1.dep = jarray('int', [Code01_GrassPlanting1.MAXN])
Code01_GrassPlanting1.siz = jarray('int', [Code01_GrassPlanting1.MAXN])
Code01_GrassPlanting1.son = jarray('int', [Code01_GrassPlanting1.MAXN])
Code01_GrassPlanting1.top = jarray('int', [Code01_GrassPlanting1.MAXN])
Code01_GrassPlanting1.dfn = jarray('int', [Code01_GrassPlanting1.MAXN])
Code01_GrassPlanting1.cntd = jcast('int', 0)
Code01_GrassPlanting1.sum = jarray('int', [jcast('int', (Code01_GrassPlanting1.MAXN << (2 & 31)))])
Code01_GrassPlanting1.addTag = jarray('int', [jcast('int', (Code01_GrassPlanting1.MAXN << (2 & 31)))])
Code01_GrassPlanting1.fse = jarray('int', [Code01_GrassPlanting1.MAXN, 3])
Code01_GrassPlanting1.stacksize = jcast('int', 0)
Code01_GrassPlanting1.first = jcast('int', 0)
Code01_GrassPlanting1.second = jcast('int', 0)
Code01_GrassPlanting1.edge = jcast('int', 0)

if __name__ == '__main__':
    Code01_GrassPlanting1.main([])
