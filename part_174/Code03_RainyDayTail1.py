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

# 雨天的尾巴，Python版
# 一共有n个节点，给定n-1条边，所有节点组成一棵树
# 给定m条路径，格式 x y v，表示x到y路径上的每个点都收到一个数字v
# 打印第i号点上，收到次数最多的数字，如果不止一种，打印值最小的数字
# 如果某节点没有收到过数字，打印0
# 一共n条打印
# 1 <= n、m、v <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4556
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_RainyDayTail1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'MAXT': 'MAXT', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dep': 'dep', 'stjump': 'stjump', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'maxCnt': 'maxCnt', 'cntt': 'cntt', 'ans': 'ans', 'ufe': 'ufe', 'stacksize': 'stacksize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    MAXV = 0
    MAXT = 0
    MAXP = 0
    n = 0
    m = 0
    head = None
    nxt = None
    to = None
    cntg = 0
    dep = None
    stjump = None
    root = None
    ls = None
    rs = None
    maxCnt = None
    cntt = 0
    ans = None
    # 递归改迭代需要
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
        jset(Code03_RainyDayTail1.ufe[Code03_RainyDayTail1.stacksize], 0, u)
        jset(Code03_RainyDayTail1.ufe[Code03_RainyDayTail1.stacksize], 1, f)
        jset(Code03_RainyDayTail1.ufe[Code03_RainyDayTail1.stacksize], 2, e)
        Code03_RainyDayTail1.stacksize = jcast('int', (Code03_RainyDayTail1.stacksize + 1))

    @staticmethod
    def pop():
        Code03_RainyDayTail1.stacksize = jcast('int', (Code03_RainyDayTail1.stacksize - 1))
        Code03_RainyDayTail1.u = jcast('int', Code03_RainyDayTail1.ufe[Code03_RainyDayTail1.stacksize][0])
        Code03_RainyDayTail1.f = jcast('int', Code03_RainyDayTail1.ufe[Code03_RainyDayTail1.stacksize][1])
        Code03_RainyDayTail1.e = jcast('int', Code03_RainyDayTail1.ufe[Code03_RainyDayTail1.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_RainyDayTail1.nxt, ((_java_obj_1 := Code03_RainyDayTail1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_RainyDayTail1.head[u])
        Code03_RainyDayTail1.to[Code03_RainyDayTail1.cntg] = jcast('int', v)
        Code03_RainyDayTail1.head[u] = jcast('int', Code03_RainyDayTail1.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code03_RainyDayTail1.dep[u] = jcast('int', jcast('int', jadd(Code03_RainyDayTail1.dep[fa], 1)))
        jset(Code03_RainyDayTail1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code03_RainyDayTail1.MAXP):
            jset(Code03_RainyDayTail1.stjump[u], p, Code03_RainyDayTail1.stjump[Code03_RainyDayTail1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code03_RainyDayTail1.head[u])
        while (e > 0):
            v = jcast('int', Code03_RainyDayTail1.to[e])
            if (v != fa):
                Code03_RainyDayTail1.dfs1(v, u)
            e = jcast('int', Code03_RainyDayTail1.nxt[e])

    # dfs1改迭代
    @staticmethod
    def dfs2():
        Code03_RainyDayTail1.stacksize = jcast('int', 0)
        Code03_RainyDayTail1.push(1, 0, jcast('int', (-1)))
        while (Code03_RainyDayTail1.stacksize > 0):
            Code03_RainyDayTail1.pop()
            if (Code03_RainyDayTail1.e == jcast('int', (-1))):
                Code03_RainyDayTail1.dep[Code03_RainyDayTail1.u] = jcast('int', jcast('int', jadd(Code03_RainyDayTail1.dep[Code03_RainyDayTail1.f], 1)))
                jset(Code03_RainyDayTail1.stjump[Code03_RainyDayTail1.u], 0, Code03_RainyDayTail1.f)
                p = jcast('int', 1)
                while (p < Code03_RainyDayTail1.MAXP):
                    jset(Code03_RainyDayTail1.stjump[Code03_RainyDayTail1.u], p, Code03_RainyDayTail1.stjump[Code03_RainyDayTail1.stjump[Code03_RainyDayTail1.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code03_RainyDayTail1.e = jcast('int', Code03_RainyDayTail1.head[Code03_RainyDayTail1.u])
            else:
                Code03_RainyDayTail1.e = jcast('int', Code03_RainyDayTail1.nxt[Code03_RainyDayTail1.e])
            if (Code03_RainyDayTail1.e != 0):
                Code03_RainyDayTail1.push(Code03_RainyDayTail1.u, Code03_RainyDayTail1.f, Code03_RainyDayTail1.e)
                if (Code03_RainyDayTail1.to[Code03_RainyDayTail1.e] != Code03_RainyDayTail1.f):
                    Code03_RainyDayTail1.push(Code03_RainyDayTail1.to[Code03_RainyDayTail1.e], Code03_RainyDayTail1.u, jcast('int', (-1)))

    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code03_RainyDayTail1.dep[a] < Code03_RainyDayTail1.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code03_RainyDayTail1.MAXP - 1)))
        while (p >= 0):
            if (Code03_RainyDayTail1.dep[Code03_RainyDayTail1.stjump[a][p]] >= Code03_RainyDayTail1.dep[b]):
                a = jcast('int', Code03_RainyDayTail1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code03_RainyDayTail1.MAXP - 1)))
        while (p >= 0):
            if (Code03_RainyDayTail1.stjump[a][p] != Code03_RainyDayTail1.stjump[b][p]):
                a = jcast('int', Code03_RainyDayTail1.stjump[a][p])
                b = jcast('int', Code03_RainyDayTail1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code03_RainyDayTail1.stjump[a][0])

    @staticmethod
    def up(i):
        i = jcast('int', i)
        jset(Code03_RainyDayTail1.maxCnt, i, jstatic('Math', 'max', Code03_RainyDayTail1.maxCnt[Code03_RainyDayTail1.ls[i]], Code03_RainyDayTail1.maxCnt[Code03_RainyDayTail1.rs[i]]))

    @staticmethod
    def add(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', i)
        if (rt == 0):
            rt = jcast('int', ((_java_obj_4 := Code03_RainyDayTail1), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        if (l == r):
            Code03_RainyDayTail1.maxCnt[rt] = jcast('int', jcast('int', jadd(Code03_RainyDayTail1.maxCnt[rt], jobv)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code03_RainyDayTail1.ls, rt, Code03_RainyDayTail1.add(jobi, jobv, l, mid, Code03_RainyDayTail1.ls[rt]))
            else:
                jset(Code03_RainyDayTail1.rs, rt, Code03_RainyDayTail1.add(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code03_RainyDayTail1.rs[rt]))
            Code03_RainyDayTail1.up(rt)
        return jcast('int', rt)

    @staticmethod
    def merge(l, r, t1, t2):
        l = jcast('int', l)
        r = jcast('int', r)
        t1 = jcast('int', t1)
        t2 = jcast('int', t2)
        if ((t1 == 0) or (t2 == 0)):
            return jcast('int', jcast('int', jadd(t1, t2)))
        if (l == r):
            Code03_RainyDayTail1.maxCnt[t1] = jcast('int', jcast('int', jadd(Code03_RainyDayTail1.maxCnt[t1], Code03_RainyDayTail1.maxCnt[t2])))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code03_RainyDayTail1.ls, t1, Code03_RainyDayTail1.merge(l, mid, Code03_RainyDayTail1.ls[t1], Code03_RainyDayTail1.ls[t2]))
            jset(Code03_RainyDayTail1.rs, t1, Code03_RainyDayTail1.merge(jcast('int', jadd(mid, 1)), r, Code03_RainyDayTail1.rs[t1], Code03_RainyDayTail1.rs[t2]))
            Code03_RainyDayTail1.up(t1)
        return jcast('int', t1)

    @staticmethod
    def query(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            return jcast('int', l)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        if (Code03_RainyDayTail1.maxCnt[Code03_RainyDayTail1.ls[i]] >= Code03_RainyDayTail1.maxCnt[Code03_RainyDayTail1.rs[i]]):
            return jcast('int', Code03_RainyDayTail1.query(l, mid, Code03_RainyDayTail1.ls[i]))
        else:
            return jcast('int', Code03_RainyDayTail1.query(jcast('int', jadd(mid, 1)), r, Code03_RainyDayTail1.rs[i]))

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def calc1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        e = jcast('int', Code03_RainyDayTail1.head[u])
        while (e > 0):
            v = jcast('int', Code03_RainyDayTail1.to[e])
            if (v != fa):
                Code03_RainyDayTail1.calc1(v, u)
                jset(Code03_RainyDayTail1.root, u, Code03_RainyDayTail1.merge(1, Code03_RainyDayTail1.MAXV, Code03_RainyDayTail1.root[u], Code03_RainyDayTail1.root[v]))
            e = jcast('int', Code03_RainyDayTail1.nxt[e])
        if (Code03_RainyDayTail1.maxCnt[Code03_RainyDayTail1.root[u]] == 0):
            Code03_RainyDayTail1.ans[u] = jcast('int', 0)
        else:
            jset(Code03_RainyDayTail1.ans, u, Code03_RainyDayTail1.query(1, Code03_RainyDayTail1.MAXV, Code03_RainyDayTail1.root[u]))

    # calc1改迭代
    @staticmethod
    def calc2():
        Code03_RainyDayTail1.stacksize = jcast('int', 0)
        Code03_RainyDayTail1.push(1, 0, jcast('int', (-1)))
        while (Code03_RainyDayTail1.stacksize > 0):
            Code03_RainyDayTail1.pop()
            if (Code03_RainyDayTail1.e == jcast('int', (-1))):
                Code03_RainyDayTail1.e = jcast('int', Code03_RainyDayTail1.head[Code03_RainyDayTail1.u])
            else:
                Code03_RainyDayTail1.e = jcast('int', Code03_RainyDayTail1.nxt[Code03_RainyDayTail1.e])
            if (Code03_RainyDayTail1.e != 0):
                Code03_RainyDayTail1.push(Code03_RainyDayTail1.u, Code03_RainyDayTail1.f, Code03_RainyDayTail1.e)
                if (Code03_RainyDayTail1.to[Code03_RainyDayTail1.e] != Code03_RainyDayTail1.f):
                    Code03_RainyDayTail1.push(Code03_RainyDayTail1.to[Code03_RainyDayTail1.e], Code03_RainyDayTail1.u, jcast('int', (-1)))
            else:
                ei = jcast('int', Code03_RainyDayTail1.head[Code03_RainyDayTail1.u])
                while (ei > 0):
                    v = jcast('int', Code03_RainyDayTail1.to[ei])
                    if (v != Code03_RainyDayTail1.f):
                        jset(Code03_RainyDayTail1.root, Code03_RainyDayTail1.u, Code03_RainyDayTail1.merge(1, Code03_RainyDayTail1.MAXV, Code03_RainyDayTail1.root[Code03_RainyDayTail1.u], Code03_RainyDayTail1.root[v]))
                    ei = jcast('int', Code03_RainyDayTail1.nxt[ei])
                if (Code03_RainyDayTail1.maxCnt[Code03_RainyDayTail1.root[Code03_RainyDayTail1.u]] == 0):
                    Code03_RainyDayTail1.ans[Code03_RainyDayTail1.u] = jcast('int', 0)
                else:
                    jset(Code03_RainyDayTail1.ans, Code03_RainyDayTail1.u, Code03_RainyDayTail1.query(1, Code03_RainyDayTail1.MAXV, Code03_RainyDayTail1.root[Code03_RainyDayTail1.u]))

    @staticmethod
    def main(args):
        in_ = Code03_RainyDayTail1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_RainyDayTail1.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_RainyDayTail1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code03_RainyDayTail1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code03_RainyDayTail1.addEdge(u, v)
            Code03_RainyDayTail1.addEdge(v, u)
            i = jcast('int', (i + 1))
        # dfs1(1, 0);
        Code03_RainyDayTail1.dfs2()
        i = jcast('int', 1)
        while (i <= Code03_RainyDayTail1.m):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            lca = jcast('int', Code03_RainyDayTail1.getLca(x, y))
            lcafa = jcast('int', Code03_RainyDayTail1.stjump[lca][0])
            jset(Code03_RainyDayTail1.root, x, Code03_RainyDayTail1.add(v, 1, 1, Code03_RainyDayTail1.MAXV, Code03_RainyDayTail1.root[x]))
            jset(Code03_RainyDayTail1.root, y, Code03_RainyDayTail1.add(v, 1, 1, Code03_RainyDayTail1.MAXV, Code03_RainyDayTail1.root[y]))
            jset(Code03_RainyDayTail1.root, lca, Code03_RainyDayTail1.add(v, jcast('int', (-1)), 1, Code03_RainyDayTail1.MAXV, Code03_RainyDayTail1.root[lca]))
            jset(Code03_RainyDayTail1.root, lcafa, Code03_RainyDayTail1.add(v, jcast('int', (-1)), 1, Code03_RainyDayTail1.MAXV, Code03_RainyDayTail1.root[lcafa]))
            i = jcast('int', (i + 1))
        # calc1(1, 0);
        Code03_RainyDayTail1.calc2()
        i = jcast('int', 1)
        while (i <= Code03_RainyDayTail1.n):
            jcall(out, 'println', Code03_RainyDayTail1.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

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
            raise TypeError("No matching overload for Code03_RainyDayTail1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_RainyDayTail1.MAXN = jcast('int', 100001)
Code03_RainyDayTail1.MAXV = jcast('int', 100000)
Code03_RainyDayTail1.MAXT = jcast('int', jcast('int', (Code03_RainyDayTail1.MAXN * 50)))
Code03_RainyDayTail1.MAXP = jcast('int', 20)
Code03_RainyDayTail1.n = jcast('int', 0)
Code03_RainyDayTail1.m = jcast('int', 0)
Code03_RainyDayTail1.head = jarray('int', [Code03_RainyDayTail1.MAXN])
Code03_RainyDayTail1.nxt = jarray('int', [jcast('int', (Code03_RainyDayTail1.MAXN << (1 & 31)))])
Code03_RainyDayTail1.to = jarray('int', [jcast('int', (Code03_RainyDayTail1.MAXN << (1 & 31)))])
Code03_RainyDayTail1.cntg = jcast('int', 0)
Code03_RainyDayTail1.dep = jarray('int', [Code03_RainyDayTail1.MAXN])
Code03_RainyDayTail1.stjump = jarray('int', [Code03_RainyDayTail1.MAXN, Code03_RainyDayTail1.MAXP])
Code03_RainyDayTail1.root = jarray('int', [Code03_RainyDayTail1.MAXN])
Code03_RainyDayTail1.ls = jarray('int', [Code03_RainyDayTail1.MAXT])
Code03_RainyDayTail1.rs = jarray('int', [Code03_RainyDayTail1.MAXT])
Code03_RainyDayTail1.maxCnt = jarray('int', [Code03_RainyDayTail1.MAXT])
Code03_RainyDayTail1.cntt = jcast('int', 0)
Code03_RainyDayTail1.ans = jarray('int', [Code03_RainyDayTail1.MAXN])
Code03_RainyDayTail1.ufe = jarray('int', [Code03_RainyDayTail1.MAXN, 3])
Code03_RainyDayTail1.stacksize = jcast('int', 0)
Code03_RainyDayTail1.u = jcast('int', 0)
Code03_RainyDayTail1.f = jcast('int', 0)
Code03_RainyDayTail1.e = jcast('int', 0)

if __name__ == '__main__':
    Code03_RainyDayTail1.main([])
