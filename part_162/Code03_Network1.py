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

# 网络，Python版
# 一共有n个服务器，给定n-1条边，所有服务器连成一棵树
# 某两个服务器之间的路径上，可能接受一条请求，路径上的所有服务器都需要保存该请求的重要度
# 一共有m条操作，每条操作是如下3种类型中的一种，操作依次发生，第i条操作发生的时间为i
# 操作 0 x y v : x号服务器到y号服务器的路径上，增加了一个重要度为v的请求
# 操作 1 t     : 当初时间为t的操作，一定是增加请求的操作，现在这个请求结束了
# 操作 2 x     : 当前时间下，和x号服务器无关的所有请求中，打印最大的重要度
# 关于操作2，如果当前时间下，没有任何请求、或者所有请求都和x号服务器有关，打印-1
# 2 <= n <= 10^5    1 <= m <= 2 * 10^5    1 <= 重要度 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P3250
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Network1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 'INF': 'INF', 'n': 'n', 'm': 'm', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'dfn': 'dfn', 'stjump': 'stjump', 'cntd': 'cntd', 'tree': 'tree', 'eid': 'eid', 'op': 'op', 'x': 'x', 'y': 'y', 'v': 'v', 'cntq': 'cntq', 'lset': 'lset', 'rset': 'rset', 'ans': 'ans', 'ufe': 'ufe', 'stacksize': 'stacksize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    MAXM = 0
    MAXP = 0
    INF = 0
    n = 0
    m = 0
    # 链式前向星
    head = None
    next = None
    to = None
    cntg = 0
    # 树上点差分 + 树上倍增
    fa = None
    dep = None
    siz = None
    dfn = None
    stjump = None
    cntd = 0
    # 树状数组
    tree = None
    # 事件编号组成的数组
    eid = None
    # 如果op == 0，添加点x到点y，重要度为v的路径
    # 如果op == 1，删除点x到点y，重要度为v的路径
    # 如果op == 2，查询和x相关的答案，y表示问题的编号
    op = None
    x = None
    y = None
    v = None
    cntq = 0
    # 整体二分
    lset = None
    rset = None
    ans = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_Network1.next, ((_java_obj_1 := Code03_Network1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_Network1.head[u])
        Code03_Network1.to[Code03_Network1.cntg] = jcast('int', v)
        Code03_Network1.head[u] = jcast('int', Code03_Network1.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code03_Network1.fa[u] = jcast('int', f)
        Code03_Network1.dep[u] = jcast('int', jcast('int', jadd(Code03_Network1.dep[f], 1)))
        Code03_Network1.siz[u] = jcast('int', 1)
        jset(Code03_Network1.dfn, u, ((_java_obj_4 := Code03_Network1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        jset(Code03_Network1.stjump[u], 0, f)
        p = jcast('int', 1)
        while (p < Code03_Network1.MAXP):
            jset(Code03_Network1.stjump[u], p, Code03_Network1.stjump[Code03_Network1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code03_Network1.head[u])
        while (e != 0):
            if (Code03_Network1.to[e] != f):
                Code03_Network1.dfs1(Code03_Network1.to[e], u)
            e = jcast('int', Code03_Network1.next[e])
        e = jcast('int', Code03_Network1.head[u])
        while (e != 0):
            if (Code03_Network1.to[e] != f):
                Code03_Network1.siz[u] = jcast('int', jcast('int', jadd(Code03_Network1.siz[u], Code03_Network1.siz[Code03_Network1.to[e]])))
            e = jcast('int', Code03_Network1.next[e])

    # 不会改迭代版，去看讲解118，详解了从递归版改迭代版
    ufe = None
    stacksize = 0
    u = 0
    f = 0
    e = 0
    @staticmethod
    def push(u, f, e):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', e)
        jset(Code03_Network1.ufe[Code03_Network1.stacksize], 0, u)
        jset(Code03_Network1.ufe[Code03_Network1.stacksize], 1, f)
        jset(Code03_Network1.ufe[Code03_Network1.stacksize], 2, e)
        Code03_Network1.stacksize = jcast('int', (Code03_Network1.stacksize + 1))

    @staticmethod
    def pop():
        Code03_Network1.stacksize = jcast('int', (Code03_Network1.stacksize - 1))
        Code03_Network1.u = jcast('int', Code03_Network1.ufe[Code03_Network1.stacksize][0])
        Code03_Network1.f = jcast('int', Code03_Network1.ufe[Code03_Network1.stacksize][1])
        Code03_Network1.e = jcast('int', Code03_Network1.ufe[Code03_Network1.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs2():
        Code03_Network1.stacksize = jcast('int', 0)
        Code03_Network1.push(1, 0, jcast('int', (-1)))
        while (Code03_Network1.stacksize > 0):
            Code03_Network1.pop()
            if (Code03_Network1.e == jcast('int', (-1))):
                Code03_Network1.fa[Code03_Network1.u] = jcast('int', Code03_Network1.f)
                Code03_Network1.dep[Code03_Network1.u] = jcast('int', jcast('int', jadd(Code03_Network1.dep[Code03_Network1.f], 1)))
                Code03_Network1.siz[Code03_Network1.u] = jcast('int', 1)
                jset(Code03_Network1.dfn, Code03_Network1.u, ((_java_obj_7 := Code03_Network1), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
                jset(Code03_Network1.stjump[Code03_Network1.u], 0, Code03_Network1.f)
                p = jcast('int', 1)
                while (p < Code03_Network1.MAXP):
                    jset(Code03_Network1.stjump[Code03_Network1.u], p, Code03_Network1.stjump[Code03_Network1.stjump[Code03_Network1.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code03_Network1.e = jcast('int', Code03_Network1.head[Code03_Network1.u])
            else:
                Code03_Network1.e = jcast('int', Code03_Network1.next[Code03_Network1.e])
            if (Code03_Network1.e != 0):
                Code03_Network1.push(Code03_Network1.u, Code03_Network1.f, Code03_Network1.e)
                if (Code03_Network1.to[Code03_Network1.e] != Code03_Network1.f):
                    Code03_Network1.push(Code03_Network1.to[Code03_Network1.e], Code03_Network1.u, jcast('int', (-1)))
            else:
                e = jcast('int', Code03_Network1.head[Code03_Network1.u])
                while (e != 0):
                    if (Code03_Network1.to[e] != Code03_Network1.f):
                        Code03_Network1.siz[Code03_Network1.u] = jcast('int', jcast('int', jadd(Code03_Network1.siz[Code03_Network1.u], Code03_Network1.siz[Code03_Network1.to[e]])))
                    e = jcast('int', Code03_Network1.next[e])

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code03_Network1.dep[a] < Code03_Network1.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code03_Network1.MAXP - 1)))
        while (p >= 0):
            if (Code03_Network1.dep[Code03_Network1.stjump[a][p]] >= Code03_Network1.dep[b]):
                a = jcast('int', Code03_Network1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code03_Network1.MAXP - 1)))
        while (p >= 0):
            if (Code03_Network1.stjump[a][p] != Code03_Network1.stjump[b][p]):
                a = jcast('int', Code03_Network1.stjump[a][p])
                b = jcast('int', Code03_Network1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code03_Network1.stjump[a][0])

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code03_Network1.n):
            Code03_Network1.tree[i] = jcast('int', jcast('int', jadd(Code03_Network1.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code03_Network1.lowbit(i))))

    @staticmethod
    def query(i):
        i = jcast('int', i)
        ret = jcast('int', 0)
        while (i > 0):
            ret = jcast('int', jcast('int', jadd(ret, Code03_Network1.tree[i])))
            i = jcast('int', jcast('int', (i - Code03_Network1.lowbit(i))))
        return jcast('int', ret)

    # 点x到点y的路径上，每个点增加v个请求数量
    @staticmethod
    def pathAdd(x, y, v):
        x = jcast('int', x)
        y = jcast('int', y)
        v = jcast('int', v)
        xylca = jcast('int', Code03_Network1.lca(x, y))
        lcafa = jcast('int', Code03_Network1.fa[xylca])
        Code03_Network1.add(Code03_Network1.dfn[x], v)
        Code03_Network1.add(Code03_Network1.dfn[y], v)
        Code03_Network1.add(Code03_Network1.dfn[xylca], jcast('int', (-v)))
        if (lcafa != 0):
            Code03_Network1.add(Code03_Network1.dfn[lcafa], jcast('int', (-v)))

    # 查询和x点相关的请求数量
    @staticmethod
    def pointQuery(x):
        x = jcast('int', x)
        return jcast('int', jcast('int', (Code03_Network1.query(jcast('int', (jcast('int', jadd(Code03_Network1.dfn[x], Code03_Network1.siz[x])) - 1))) - Code03_Network1.query(jcast('int', (Code03_Network1.dfn[x] - 1))))))

    @staticmethod
    def compute(el, er, vl, vr):
        el = jcast('int', el)
        er = jcast('int', er)
        vl = jcast('int', vl)
        vr = jcast('int', vr)
        if (el > er):
            return
        if (vl == vr):
            i = jcast('int', el)
            while (i <= er):
                id = jcast('int', Code03_Network1.eid[i])
                if (Code03_Network1.op[id] == 2):
                    jset(Code03_Network1.ans, Code03_Network1.y[id], vl)
                i = jcast('int', (i + 1))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(vl, vr)), 2)))
            lsiz = jcast('int', 0)
            rsiz = jcast('int', 0)
            request = jcast('int', 0)
            i = jcast('int', el)
            while (i <= er):
                id = jcast('int', Code03_Network1.eid[i])
                if (Code03_Network1.op[id] == 0):
                    if (Code03_Network1.v[id] <= mid):
                        jset(Code03_Network1.lset, (lsiz := jcast('int', (lsiz + (1)))), id)
                    else:
                        Code03_Network1.pathAdd(Code03_Network1.x[id], Code03_Network1.y[id], 1)
                        request = jcast('int', (request + 1))
                        jset(Code03_Network1.rset, (rsiz := jcast('int', (rsiz + (1)))), id)
                else:
                    if (Code03_Network1.op[id] == 1):
                        if (Code03_Network1.v[id] <= mid):
                            jset(Code03_Network1.lset, (lsiz := jcast('int', (lsiz + (1)))), id)
                        else:
                            Code03_Network1.pathAdd(Code03_Network1.x[id], Code03_Network1.y[id], jcast('int', (-1)))
                            request = jcast('int', (request - 1))
                            jset(Code03_Network1.rset, (rsiz := jcast('int', (rsiz + (1)))), id)
                    else:
                        if (Code03_Network1.pointQuery(Code03_Network1.x[id]) == request):
                            jset(Code03_Network1.lset, (lsiz := jcast('int', (lsiz + (1)))), id)
                        else:
                            jset(Code03_Network1.rset, (rsiz := jcast('int', (rsiz + (1)))), id)
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= lsiz):
                Code03_Network1.eid[jcast('int', (jcast('int', jadd(el, i)) - 1))] = jcast('int', Code03_Network1.lset[i])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= rsiz):
                Code03_Network1.eid[jcast('int', (jcast('int', jadd(jcast('int', jadd(el, lsiz)), i)) - 1))] = jcast('int', Code03_Network1.rset[i])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= rsiz):
                id = jcast('int', Code03_Network1.rset[i])
                if ((Code03_Network1.op[id] == 0) and (Code03_Network1.v[id] > mid)):
                    Code03_Network1.pathAdd(Code03_Network1.x[id], Code03_Network1.y[id], jcast('int', (-1)))
                if ((Code03_Network1.op[id] == 1) and (Code03_Network1.v[id] > mid)):
                    Code03_Network1.pathAdd(Code03_Network1.x[id], Code03_Network1.y[id], 1)
                i = jcast('int', (i + 1))
            Code03_Network1.compute(el, jcast('int', (jcast('int', jadd(el, lsiz)) - 1)), vl, mid)
            Code03_Network1.compute(jcast('int', jadd(el, lsiz)), er, jcast('int', jadd(mid, 1)), vr)

    @staticmethod
    def prepare():
        Code03_Network1.dfs2()
        i = jcast('int', 1)
        while (i <= Code03_Network1.m):
            if (Code03_Network1.op[i] == 1):
                pre = jcast('int', Code03_Network1.x[i])
                Code03_Network1.x[i] = jcast('int', Code03_Network1.x[pre])
                Code03_Network1.y[i] = jcast('int', Code03_Network1.y[pre])
                Code03_Network1.v[i] = jcast('int', Code03_Network1.v[pre])
            if (Code03_Network1.op[i] == 2):
                jset(Code03_Network1.y, i, ((_java_obj_10 := Code03_Network1), (_java_key_11 := 'cntq'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_Network1.m):
            Code03_Network1.eid[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code03_Network1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_Network1.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_Network1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code03_Network1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code03_Network1.addEdge(u, v)
            Code03_Network1.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_Network1.m):
            jset(Code03_Network1.op, i, jcall(in_, 'nextInt'))
            jset(Code03_Network1.x, i, jcall(in_, 'nextInt'))
            if (Code03_Network1.op[i] == 0):
                jset(Code03_Network1.y, i, jcall(in_, 'nextInt'))
                jset(Code03_Network1.v, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code03_Network1.prepare()
        Code03_Network1.compute(1, Code03_Network1.m, 0, Code03_Network1.INF)
        i = jcast('int', 1)
        while (i <= Code03_Network1.cntq):
            if (Code03_Network1.ans[i] == 0):
                jcall(out, 'println', jcast('int', (-1)))
            else:
                jcall(out, 'println', Code03_Network1.ans[i])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len', 'in': 'in_'}
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        def _java_init_0(self, in_):
            self.in_ = in_

        def readByte(self):
            if (self.ptr >= self.len):
                self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
                self.ptr = jcast('int', 0)
                if (self.len <= 0):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', self.buffer[((_java_obj_13 := self), (_java_key_14 := 'ptr'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))), _java_old_15)[4]])

        def nextInt(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('int', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('int', (jcast('int', (-val)) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code03_Network1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Network1.MAXN = jcast('int', 100001)
Code03_Network1.MAXM = jcast('int', 200001)
Code03_Network1.MAXP = jcast('int', 20)
Code03_Network1.INF = jcast('int', 1000000001)
Code03_Network1.n = jcast('int', 0)
Code03_Network1.m = jcast('int', 0)
Code03_Network1.head = jarray('int', [Code03_Network1.MAXN])
Code03_Network1.next = jarray('int', [jcast('int', (Code03_Network1.MAXN << (1 & 31)))])
Code03_Network1.to = jarray('int', [jcast('int', (Code03_Network1.MAXN << (1 & 31)))])
Code03_Network1.cntg = jcast('int', 0)
Code03_Network1.fa = jarray('int', [Code03_Network1.MAXN])
Code03_Network1.dep = jarray('int', [Code03_Network1.MAXN])
Code03_Network1.siz = jarray('int', [Code03_Network1.MAXN])
Code03_Network1.dfn = jarray('int', [Code03_Network1.MAXN])
Code03_Network1.stjump = jarray('int', [Code03_Network1.MAXN, Code03_Network1.MAXP])
Code03_Network1.cntd = jcast('int', 0)
Code03_Network1.tree = jarray('int', [Code03_Network1.MAXN])
Code03_Network1.eid = jarray('int', [Code03_Network1.MAXM])
Code03_Network1.op = jarray('int', [Code03_Network1.MAXM])
Code03_Network1.x = jarray('int', [Code03_Network1.MAXM])
Code03_Network1.y = jarray('int', [Code03_Network1.MAXM])
Code03_Network1.v = jarray('int', [Code03_Network1.MAXM])
Code03_Network1.cntq = jcast('int', 0)
Code03_Network1.lset = jarray('int', [Code03_Network1.MAXM])
Code03_Network1.rset = jarray('int', [Code03_Network1.MAXM])
Code03_Network1.ans = jarray('int', [Code03_Network1.MAXM])
Code03_Network1.ufe = jarray('int', [Code03_Network1.MAXN, 3])
Code03_Network1.stacksize = jcast('int', 0)
Code03_Network1.u = jcast('int', 0)
Code03_Network1.f = jcast('int', 0)
Code03_Network1.e = jcast('int', 0)

if __name__ == '__main__':
    Code03_Network1.main([])
