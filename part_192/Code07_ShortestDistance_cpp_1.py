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

# 最短距离，巧妙的解法，Python版
# 图中有n个点、n条无向边，每条边有边权，图是一棵基环树
# 一共有m条操作，每条操作是如下两种类型中的一种
# 操作 1 x y : 第x号边的边权修改为y
# 操作 2 x y : 查询点x和点y之间的最短距离
# 1 <= n <= 10^5 + 6
# 1 <= m <= 10^5
# 0 <= 边权 <= 5000
# 测试链接 : https://www.luogu.com.cn/problem/P4949
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_ShortestDistance_cpp_1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'u': 'u', 'v': 'v', 'w': 'w', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'cntd': 'cntd', 'node1': 'node1', 'node2': 'node2', 'skipEdge': 'skipEdge', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'tree': 'tree'}
    MAXN = 0
    n = 0
    m = 0
    u = None
    v = None
    w = None
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    cntd = 0
    node1 = 0
    node2 = 0
    skipEdge = 0
    fa = None
    dep = None
    siz = None
    son = None
    top = None
    tree = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_ShortestDistance_cpp_1.nxt, ((_java_obj_1 := Code07_ShortestDistance_cpp_1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_ShortestDistance_cpp_1.head[u])
        Code07_ShortestDistance_cpp_1.to[Code07_ShortestDistance_cpp_1.cntg] = jcast('int', v)
        Code07_ShortestDistance_cpp_1.head[u] = jcast('int', Code07_ShortestDistance_cpp_1.cntg)

    @staticmethod
    def dfs1(u):
        u = jcast('int', u)
        jset(Code07_ShortestDistance_cpp_1.dfn, u, ((_java_obj_4 := Code07_ShortestDistance_cpp_1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        e = jcast('int', Code07_ShortestDistance_cpp_1.head[u])
        while (e > 0):
            v = jcast('int', Code07_ShortestDistance_cpp_1.to[e])
            if (Code07_ShortestDistance_cpp_1.dfn[v] == 0):
                Code07_ShortestDistance_cpp_1.dfs1(v)
            else:
                if (Code07_ShortestDistance_cpp_1.dfn[u] < Code07_ShortestDistance_cpp_1.dfn[v]):
                    Code07_ShortestDistance_cpp_1.node1 = jcast('int', u)
                    Code07_ShortestDistance_cpp_1.node2 = jcast('int', v)
                    Code07_ShortestDistance_cpp_1.skipEdge = jcast('int', jcast('int', (jcast('int', jadd(e, 1)) >> (1 & 31))))
            e = jcast('int', Code07_ShortestDistance_cpp_1.nxt[e])

    @staticmethod
    def dfs2(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code07_ShortestDistance_cpp_1.fa[u] = jcast('int', f)
        Code07_ShortestDistance_cpp_1.dep[u] = jcast('int', jcast('int', jadd(Code07_ShortestDistance_cpp_1.dep[f], 1)))
        Code07_ShortestDistance_cpp_1.siz[u] = jcast('int', 1)
        e = jcast('int', Code07_ShortestDistance_cpp_1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code07_ShortestDistance_cpp_1.to[e])
            if ((jcast('int', (jcast('int', jadd(e, 1)) >> (1 & 31))) != Code07_ShortestDistance_cpp_1.skipEdge) and (v != f)):
                Code07_ShortestDistance_cpp_1.dfs2(v, u)
                Code07_ShortestDistance_cpp_1.siz[u] = jcast('int', jcast('int', jadd(Code07_ShortestDistance_cpp_1.siz[u], Code07_ShortestDistance_cpp_1.siz[v])))
                if ((Code07_ShortestDistance_cpp_1.son[u] == 0) or (Code07_ShortestDistance_cpp_1.siz[Code07_ShortestDistance_cpp_1.son[u]] < Code07_ShortestDistance_cpp_1.siz[v])):
                    Code07_ShortestDistance_cpp_1.son[u] = jcast('int', v)
            e = jcast('int', Code07_ShortestDistance_cpp_1.nxt[e])

    @staticmethod
    def dfs3(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code07_ShortestDistance_cpp_1.top[u] = jcast('int', t)
        jset(Code07_ShortestDistance_cpp_1.dfn, u, ((_java_obj_7 := Code07_ShortestDistance_cpp_1), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
        if (Code07_ShortestDistance_cpp_1.son[u] != 0):
            Code07_ShortestDistance_cpp_1.dfs3(Code07_ShortestDistance_cpp_1.son[u], t)
        e = jcast('int', Code07_ShortestDistance_cpp_1.head[u])
        while (e > 0):
            v = jcast('int', Code07_ShortestDistance_cpp_1.to[e])
            if (((jcast('int', (jcast('int', jadd(e, 1)) >> (1 & 31))) != Code07_ShortestDistance_cpp_1.skipEdge) and (v != Code07_ShortestDistance_cpp_1.fa[u])) and (v != Code07_ShortestDistance_cpp_1.son[u])):
                Code07_ShortestDistance_cpp_1.dfs3(v, v)
            e = jcast('int', Code07_ShortestDistance_cpp_1.nxt[e])

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code07_ShortestDistance_cpp_1.n):
            Code07_ShortestDistance_cpp_1.tree[i] = jcast('int', jcast('int', jadd(Code07_ShortestDistance_cpp_1.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code07_ShortestDistance_cpp_1.lowbit(i))))

    @staticmethod
    def query(i):
        i = jcast('int', i)
        ans = jcast('int', 0)
        while (i >= 1):
            ans = jcast('int', jcast('int', jadd(ans, Code07_ShortestDistance_cpp_1.tree[i])))
            i = jcast('int', jcast('int', (i - Code07_ShortestDistance_cpp_1.lowbit(i))))
        return jcast('int', ans)

    @staticmethod
    def sum(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l > r):
            return jcast('int', 0)
        return jcast('int', jcast('int', (Code07_ShortestDistance_cpp_1.query(r) - Code07_ShortestDistance_cpp_1.query(jcast('int', (l - 1))))))

    @staticmethod
    def prepare():
        Code07_ShortestDistance_cpp_1.dfs1(1)
        Code07_ShortestDistance_cpp_1.cntd = jcast('int', 0)
        Code07_ShortestDistance_cpp_1.dfs2(1, 0)
        Code07_ShortestDistance_cpp_1.dfs3(1, 1)
        i = jcast('int', 1)
        while (i <= Code07_ShortestDistance_cpp_1.n):
            if (i != Code07_ShortestDistance_cpp_1.skipEdge):
                Code07_ShortestDistance_cpp_1.add(jstatic('Math', 'max', Code07_ShortestDistance_cpp_1.dfn[Code07_ShortestDistance_cpp_1.u[i]], Code07_ShortestDistance_cpp_1.dfn[Code07_ShortestDistance_cpp_1.v[i]]), Code07_ShortestDistance_cpp_1.w[i])
            i = jcast('int', (i + 1))

    @staticmethod
    def setEdge(edge, val):
        edge = jcast('int', edge)
        val = jcast('int', val)
        if (edge != Code07_ShortestDistance_cpp_1.skipEdge):
            Code07_ShortestDistance_cpp_1.add(jstatic('Math', 'max', Code07_ShortestDistance_cpp_1.dfn[Code07_ShortestDistance_cpp_1.u[edge]], Code07_ShortestDistance_cpp_1.dfn[Code07_ShortestDistance_cpp_1.v[edge]]), jcast('int', (val - Code07_ShortestDistance_cpp_1.w[edge])))
        Code07_ShortestDistance_cpp_1.w[edge] = jcast('int', val)

    @staticmethod
    def jump(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        ans = jcast('int', 0)
        while (Code07_ShortestDistance_cpp_1.top[x] != Code07_ShortestDistance_cpp_1.top[y]):
            if (Code07_ShortestDistance_cpp_1.dep[Code07_ShortestDistance_cpp_1.top[x]] < Code07_ShortestDistance_cpp_1.dep[Code07_ShortestDistance_cpp_1.top[y]]):
                ans = jcast('int', jcast('int', jadd(ans, Code07_ShortestDistance_cpp_1.sum(Code07_ShortestDistance_cpp_1.dfn[Code07_ShortestDistance_cpp_1.top[y]], Code07_ShortestDistance_cpp_1.dfn[y]))))
                y = jcast('int', Code07_ShortestDistance_cpp_1.fa[Code07_ShortestDistance_cpp_1.top[y]])
            else:
                ans = jcast('int', jcast('int', jadd(ans, Code07_ShortestDistance_cpp_1.sum(Code07_ShortestDistance_cpp_1.dfn[Code07_ShortestDistance_cpp_1.top[x]], Code07_ShortestDistance_cpp_1.dfn[x]))))
                x = jcast('int', Code07_ShortestDistance_cpp_1.fa[Code07_ShortestDistance_cpp_1.top[x]])
        if (Code07_ShortestDistance_cpp_1.dfn[x] < Code07_ShortestDistance_cpp_1.dfn[y]):
            ans = jcast('int', jcast('int', jadd(ans, Code07_ShortestDistance_cpp_1.sum(jcast('int', jadd(Code07_ShortestDistance_cpp_1.dfn[x], 1)), Code07_ShortestDistance_cpp_1.dfn[y]))))
        else:
            ans = jcast('int', jcast('int', jadd(ans, Code07_ShortestDistance_cpp_1.sum(jcast('int', jadd(Code07_ShortestDistance_cpp_1.dfn[y], 1)), Code07_ShortestDistance_cpp_1.dfn[x]))))
        return jcast('int', ans)

    @staticmethod
    def getDistance(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        p1 = jcast('int', Code07_ShortestDistance_cpp_1.jump(x, y))
        p2 = jcast('int', jcast('int', jadd(jcast('int', jadd(Code07_ShortestDistance_cpp_1.jump(x, Code07_ShortestDistance_cpp_1.node1), Code07_ShortestDistance_cpp_1.w[Code07_ShortestDistance_cpp_1.skipEdge])), Code07_ShortestDistance_cpp_1.jump(Code07_ShortestDistance_cpp_1.node2, y))))
        p3 = jcast('int', jcast('int', jadd(jcast('int', jadd(Code07_ShortestDistance_cpp_1.jump(x, Code07_ShortestDistance_cpp_1.node2), Code07_ShortestDistance_cpp_1.w[Code07_ShortestDistance_cpp_1.skipEdge])), Code07_ShortestDistance_cpp_1.jump(Code07_ShortestDistance_cpp_1.node1, y))))
        return jcast('int', jstatic('Math', 'min', p1, jstatic('Math', 'min', p2, p3)))

    @staticmethod
    def main(args):
        in_ = Code07_ShortestDistance_cpp_1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_ShortestDistance_cpp_1.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_ShortestDistance_cpp_1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_ShortestDistance_cpp_1.n):
            jset(Code07_ShortestDistance_cpp_1.u, i, jcall(in_, 'nextInt'))
            jset(Code07_ShortestDistance_cpp_1.v, i, jcall(in_, 'nextInt'))
            jset(Code07_ShortestDistance_cpp_1.w, i, jcall(in_, 'nextInt'))
            Code07_ShortestDistance_cpp_1.addEdge(Code07_ShortestDistance_cpp_1.u[i], Code07_ShortestDistance_cpp_1.v[i])
            Code07_ShortestDistance_cpp_1.addEdge(Code07_ShortestDistance_cpp_1.v[i], Code07_ShortestDistance_cpp_1.u[i])
            i = jcast('int', (i + 1))
        Code07_ShortestDistance_cpp_1.prepare()
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        while (i <= Code07_ShortestDistance_cpp_1.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                Code07_ShortestDistance_cpp_1.setEdge(x, y)
            else:
                jcall(out, 'println', Code07_ShortestDistance_cpp_1.getDistance(x, y))
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
            return jcast('int', self.buffer[((_java_obj_10 := self), (_java_key_11 := 'ptr'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]])

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
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code07_ShortestDistance_cpp_1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_ShortestDistance_cpp_1.MAXN = jcast('int', 100007)
Code07_ShortestDistance_cpp_1.n = jcast('int', 0)
Code07_ShortestDistance_cpp_1.m = jcast('int', 0)
Code07_ShortestDistance_cpp_1.u = jarray('int', [Code07_ShortestDistance_cpp_1.MAXN])
Code07_ShortestDistance_cpp_1.v = jarray('int', [Code07_ShortestDistance_cpp_1.MAXN])
Code07_ShortestDistance_cpp_1.w = jarray('int', [Code07_ShortestDistance_cpp_1.MAXN])
Code07_ShortestDistance_cpp_1.head = jarray('int', [Code07_ShortestDistance_cpp_1.MAXN])
Code07_ShortestDistance_cpp_1.nxt = jarray('int', [jcast('int', (Code07_ShortestDistance_cpp_1.MAXN << (1 & 31)))])
Code07_ShortestDistance_cpp_1.to = jarray('int', [jcast('int', (Code07_ShortestDistance_cpp_1.MAXN << (1 & 31)))])
Code07_ShortestDistance_cpp_1.cntg = jcast('int', 0)
Code07_ShortestDistance_cpp_1.dfn = jarray('int', [Code07_ShortestDistance_cpp_1.MAXN])
Code07_ShortestDistance_cpp_1.cntd = jcast('int', 0)
Code07_ShortestDistance_cpp_1.node1 = jcast('int', 0)
Code07_ShortestDistance_cpp_1.node2 = jcast('int', 0)
Code07_ShortestDistance_cpp_1.skipEdge = jcast('int', 0)
Code07_ShortestDistance_cpp_1.fa = jarray('int', [Code07_ShortestDistance_cpp_1.MAXN])
Code07_ShortestDistance_cpp_1.dep = jarray('int', [Code07_ShortestDistance_cpp_1.MAXN])
Code07_ShortestDistance_cpp_1.siz = jarray('int', [Code07_ShortestDistance_cpp_1.MAXN])
Code07_ShortestDistance_cpp_1.son = jarray('int', [Code07_ShortestDistance_cpp_1.MAXN])
Code07_ShortestDistance_cpp_1.top = jarray('int', [Code07_ShortestDistance_cpp_1.MAXN])
Code07_ShortestDistance_cpp_1.tree = jarray('int', [Code07_ShortestDistance_cpp_1.MAXN])

if __name__ == '__main__':
    Code07_ShortestDistance_cpp_1.main([])
