# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 天天爱跑步，Python版
# 一共有n个点，给定n-1条边，所有节点组成一棵树
# 每个点上都有一个观察员，给出每个观察员的观测时刻w[i]
# 给出m个跑步者的路线，格式 x y : 该跑步者出发时刻为0，从x跑到y
# 任何跑步者通过任何一条边，耗时都是1秒
# 某个跑步者到达i号点的时刻 == w[i]，那么该跑步者才会被i号点的观察员观测到
# 打印i号点的观察员，能观测到多少人，一共n条打印
# 1 <= n、m、w[i] <= 3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P1600
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_LoveRunning1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'w': 'w', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dep': 'dep', 'stjump': 'stjump', 'rtUp': 'rtUp', 'rtDown': 'rtDown', 'ls': 'ls', 'rs': 'rs', 'sum': 'sum', 'cntt': 'cntt', 'ans': 'ans', 'ufe': 'ufe', 'stacksize': 'stacksize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    MAXT = 0
    MAXP = 0
    n = 0
    m = 0
    w = None
    head = None
    nxt = None
    to = None
    cntg = 0
    dep = None
    stjump = None
    rtUp = None
    rtDown = None
    ls = None
    rs = None
    sum = None
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
        jset(Code04_LoveRunning1.ufe[Code04_LoveRunning1.stacksize], 0, u)
        jset(Code04_LoveRunning1.ufe[Code04_LoveRunning1.stacksize], 1, f)
        jset(Code04_LoveRunning1.ufe[Code04_LoveRunning1.stacksize], 2, e)
        Code04_LoveRunning1.stacksize = jcast('int', (Code04_LoveRunning1.stacksize + 1))

    @staticmethod
    def pop():
        Code04_LoveRunning1.stacksize = jcast('int', (Code04_LoveRunning1.stacksize - 1))
        Code04_LoveRunning1.u = jcast('int', Code04_LoveRunning1.ufe[Code04_LoveRunning1.stacksize][0])
        Code04_LoveRunning1.f = jcast('int', Code04_LoveRunning1.ufe[Code04_LoveRunning1.stacksize][1])
        Code04_LoveRunning1.e = jcast('int', Code04_LoveRunning1.ufe[Code04_LoveRunning1.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_LoveRunning1.nxt, ((_java_obj_1 := Code04_LoveRunning1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_LoveRunning1.head[u])
        Code04_LoveRunning1.to[Code04_LoveRunning1.cntg] = jcast('int', v)
        Code04_LoveRunning1.head[u] = jcast('int', Code04_LoveRunning1.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code04_LoveRunning1.dep[u] = jcast('int', jcast('int', jadd(Code04_LoveRunning1.dep[fa], 1)))
        jset(Code04_LoveRunning1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code04_LoveRunning1.MAXP):
            jset(Code04_LoveRunning1.stjump[u], p, Code04_LoveRunning1.stjump[Code04_LoveRunning1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code04_LoveRunning1.head[u])
        while (e > 0):
            v = jcast('int', Code04_LoveRunning1.to[e])
            if (v != fa):
                Code04_LoveRunning1.dfs1(v, u)
            e = jcast('int', Code04_LoveRunning1.nxt[e])

    # dfs1改迭代
    @staticmethod
    def dfs2():
        Code04_LoveRunning1.stacksize = jcast('int', 0)
        Code04_LoveRunning1.push(1, 0, jcast('int', (-1)))
        while (Code04_LoveRunning1.stacksize > 0):
            Code04_LoveRunning1.pop()
            if (Code04_LoveRunning1.e == jcast('int', (-1))):
                Code04_LoveRunning1.dep[Code04_LoveRunning1.u] = jcast('int', jcast('int', jadd(Code04_LoveRunning1.dep[Code04_LoveRunning1.f], 1)))
                jset(Code04_LoveRunning1.stjump[Code04_LoveRunning1.u], 0, Code04_LoveRunning1.f)
                p = jcast('int', 1)
                while (p < Code04_LoveRunning1.MAXP):
                    jset(Code04_LoveRunning1.stjump[Code04_LoveRunning1.u], p, Code04_LoveRunning1.stjump[Code04_LoveRunning1.stjump[Code04_LoveRunning1.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code04_LoveRunning1.e = jcast('int', Code04_LoveRunning1.head[Code04_LoveRunning1.u])
            else:
                Code04_LoveRunning1.e = jcast('int', Code04_LoveRunning1.nxt[Code04_LoveRunning1.e])
            if (Code04_LoveRunning1.e != 0):
                Code04_LoveRunning1.push(Code04_LoveRunning1.u, Code04_LoveRunning1.f, Code04_LoveRunning1.e)
                if (Code04_LoveRunning1.to[Code04_LoveRunning1.e] != Code04_LoveRunning1.f):
                    Code04_LoveRunning1.push(Code04_LoveRunning1.to[Code04_LoveRunning1.e], Code04_LoveRunning1.u, jcast('int', (-1)))

    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code04_LoveRunning1.dep[a] < Code04_LoveRunning1.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code04_LoveRunning1.MAXP - 1)))
        while (p >= 0):
            if (Code04_LoveRunning1.dep[Code04_LoveRunning1.stjump[a][p]] >= Code04_LoveRunning1.dep[b]):
                a = jcast('int', Code04_LoveRunning1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code04_LoveRunning1.MAXP - 1)))
        while (p >= 0):
            if (Code04_LoveRunning1.stjump[a][p] != Code04_LoveRunning1.stjump[b][p]):
                a = jcast('int', Code04_LoveRunning1.stjump[a][p])
                b = jcast('int', Code04_LoveRunning1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code04_LoveRunning1.stjump[a][0])

    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code04_LoveRunning1.sum[i] = jcast('int', jcast('int', jadd(Code04_LoveRunning1.sum[Code04_LoveRunning1.ls[i]], Code04_LoveRunning1.sum[Code04_LoveRunning1.rs[i]])))

    @staticmethod
    def add(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', i)
        if (rt == 0):
            rt = jcast('int', ((_java_obj_4 := Code04_LoveRunning1), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        if (l == r):
            Code04_LoveRunning1.sum[rt] = jcast('int', jcast('int', jadd(Code04_LoveRunning1.sum[rt], jobv)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code04_LoveRunning1.ls, rt, Code04_LoveRunning1.add(jobi, jobv, l, mid, Code04_LoveRunning1.ls[rt]))
            else:
                jset(Code04_LoveRunning1.rs, rt, Code04_LoveRunning1.add(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code04_LoveRunning1.rs[rt]))
            Code04_LoveRunning1.up(rt)
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
            Code04_LoveRunning1.sum[t1] = jcast('int', jcast('int', jadd(Code04_LoveRunning1.sum[t1], Code04_LoveRunning1.sum[t2])))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code04_LoveRunning1.ls, t1, Code04_LoveRunning1.merge(l, mid, Code04_LoveRunning1.ls[t1], Code04_LoveRunning1.ls[t2]))
            jset(Code04_LoveRunning1.rs, t1, Code04_LoveRunning1.merge(jcast('int', jadd(mid, 1)), r, Code04_LoveRunning1.rs[t1], Code04_LoveRunning1.rs[t2]))
            Code04_LoveRunning1.up(t1)
        return jcast('int', t1)

    @staticmethod
    def query(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (((jobi < l) or (jobi > r)) or (i == 0)):
            return jcast('int', 0)
        if (l == r):
            return jcast('int', Code04_LoveRunning1.sum[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        if (jobi <= mid):
            return jcast('int', Code04_LoveRunning1.query(jobi, l, mid, Code04_LoveRunning1.ls[i]))
        else:
            return jcast('int', Code04_LoveRunning1.query(jobi, jcast('int', jadd(mid, 1)), r, Code04_LoveRunning1.rs[i]))

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def calc1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        e = jcast('int', Code04_LoveRunning1.head[u])
        while (e > 0):
            v = jcast('int', Code04_LoveRunning1.to[e])
            if (v != fa):
                Code04_LoveRunning1.calc1(v, u)
                jset(Code04_LoveRunning1.rtUp, u, Code04_LoveRunning1.merge(1, Code04_LoveRunning1.n, Code04_LoveRunning1.rtUp[u], Code04_LoveRunning1.rtUp[v]))
                jset(Code04_LoveRunning1.rtDown, u, Code04_LoveRunning1.merge(jcast('int', (-Code04_LoveRunning1.n)), Code04_LoveRunning1.n, Code04_LoveRunning1.rtDown[u], Code04_LoveRunning1.rtDown[v]))
            e = jcast('int', Code04_LoveRunning1.nxt[e])
        jset(Code04_LoveRunning1.ans, u, jcast('int', jadd(Code04_LoveRunning1.query(jcast('int', jadd(Code04_LoveRunning1.dep[u], Code04_LoveRunning1.w[u])), 1, Code04_LoveRunning1.n, Code04_LoveRunning1.rtUp[u]), Code04_LoveRunning1.query(jcast('int', (Code04_LoveRunning1.dep[u] - Code04_LoveRunning1.w[u])), jcast('int', (-Code04_LoveRunning1.n)), Code04_LoveRunning1.n, Code04_LoveRunning1.rtDown[u]))))

    # calc1改迭代
    @staticmethod
    def calc2():
        Code04_LoveRunning1.stacksize = jcast('int', 0)
        Code04_LoveRunning1.push(1, 0, jcast('int', (-1)))
        while (Code04_LoveRunning1.stacksize > 0):
            Code04_LoveRunning1.pop()
            if (Code04_LoveRunning1.e == jcast('int', (-1))):
                Code04_LoveRunning1.e = jcast('int', Code04_LoveRunning1.head[Code04_LoveRunning1.u])
            else:
                Code04_LoveRunning1.e = jcast('int', Code04_LoveRunning1.nxt[Code04_LoveRunning1.e])
            if (Code04_LoveRunning1.e != 0):
                Code04_LoveRunning1.push(Code04_LoveRunning1.u, Code04_LoveRunning1.f, Code04_LoveRunning1.e)
                if (Code04_LoveRunning1.to[Code04_LoveRunning1.e] != Code04_LoveRunning1.f):
                    Code04_LoveRunning1.push(Code04_LoveRunning1.to[Code04_LoveRunning1.e], Code04_LoveRunning1.u, jcast('int', (-1)))
            else:
                ei = jcast('int', Code04_LoveRunning1.head[Code04_LoveRunning1.u])
                while (ei > 0):
                    v = jcast('int', Code04_LoveRunning1.to[ei])
                    if (v != Code04_LoveRunning1.f):
                        jset(Code04_LoveRunning1.rtUp, Code04_LoveRunning1.u, Code04_LoveRunning1.merge(1, Code04_LoveRunning1.n, Code04_LoveRunning1.rtUp[Code04_LoveRunning1.u], Code04_LoveRunning1.rtUp[v]))
                        jset(Code04_LoveRunning1.rtDown, Code04_LoveRunning1.u, Code04_LoveRunning1.merge(jcast('int', (-Code04_LoveRunning1.n)), Code04_LoveRunning1.n, Code04_LoveRunning1.rtDown[Code04_LoveRunning1.u], Code04_LoveRunning1.rtDown[v]))
                    ei = jcast('int', Code04_LoveRunning1.nxt[ei])
                jset(Code04_LoveRunning1.ans, Code04_LoveRunning1.u, jcast('int', jadd(Code04_LoveRunning1.query(jcast('int', jadd(Code04_LoveRunning1.dep[Code04_LoveRunning1.u], Code04_LoveRunning1.w[Code04_LoveRunning1.u])), 1, Code04_LoveRunning1.n, Code04_LoveRunning1.rtUp[Code04_LoveRunning1.u]), Code04_LoveRunning1.query(jcast('int', (Code04_LoveRunning1.dep[Code04_LoveRunning1.u] - Code04_LoveRunning1.w[Code04_LoveRunning1.u])), jcast('int', (-Code04_LoveRunning1.n)), Code04_LoveRunning1.n, Code04_LoveRunning1.rtDown[Code04_LoveRunning1.u]))))

    @staticmethod
    def main(args):
        in_ = Code04_LoveRunning1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_LoveRunning1.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_LoveRunning1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code04_LoveRunning1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code04_LoveRunning1.addEdge(u, v)
            Code04_LoveRunning1.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_LoveRunning1.n):
            jset(Code04_LoveRunning1.w, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        # dfs1(1, 0);
        Code04_LoveRunning1.dfs2()
        i = jcast('int', 1)
        while (i <= Code04_LoveRunning1.m):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            lca = jcast('int', Code04_LoveRunning1.getLca(x, y))
            lcafa = jcast('int', Code04_LoveRunning1.stjump[lca][0])
            jset(Code04_LoveRunning1.rtUp, x, Code04_LoveRunning1.add(Code04_LoveRunning1.dep[x], 1, 1, Code04_LoveRunning1.n, Code04_LoveRunning1.rtUp[x]))
            jset(Code04_LoveRunning1.rtUp, lcafa, Code04_LoveRunning1.add(Code04_LoveRunning1.dep[x], jcast('int', (-1)), 1, Code04_LoveRunning1.n, Code04_LoveRunning1.rtUp[lcafa]))
            jset(Code04_LoveRunning1.rtDown, y, Code04_LoveRunning1.add(jcast('int', (jcast('int', (2 * Code04_LoveRunning1.dep[lca])) - Code04_LoveRunning1.dep[x])), 1, jcast('int', (-Code04_LoveRunning1.n)), Code04_LoveRunning1.n, Code04_LoveRunning1.rtDown[y]))
            jset(Code04_LoveRunning1.rtDown, lca, Code04_LoveRunning1.add(jcast('int', (jcast('int', (2 * Code04_LoveRunning1.dep[lca])) - Code04_LoveRunning1.dep[x])), jcast('int', (-1)), jcast('int', (-Code04_LoveRunning1.n)), Code04_LoveRunning1.n, Code04_LoveRunning1.rtDown[lca]))
            i = jcast('int', (i + 1))
        # calc1(1, 0);
        Code04_LoveRunning1.calc2()
        i = jcast('int', 1)
        while (i <= Code04_LoveRunning1.n):
            jcall(out, 'print', jadd(Code04_LoveRunning1.ans[i], ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println')
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
            raise TypeError("No matching overload for Code04_LoveRunning1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_LoveRunning1.MAXN = jcast('int', 300001)
Code04_LoveRunning1.MAXT = jcast('int', jcast('int', (Code04_LoveRunning1.MAXN * 50)))
Code04_LoveRunning1.MAXP = jcast('int', 20)
Code04_LoveRunning1.n = jcast('int', 0)
Code04_LoveRunning1.m = jcast('int', 0)
Code04_LoveRunning1.w = jarray('int', [Code04_LoveRunning1.MAXN])
Code04_LoveRunning1.head = jarray('int', [Code04_LoveRunning1.MAXN])
Code04_LoveRunning1.nxt = jarray('int', [jcast('int', (Code04_LoveRunning1.MAXN << (1 & 31)))])
Code04_LoveRunning1.to = jarray('int', [jcast('int', (Code04_LoveRunning1.MAXN << (1 & 31)))])
Code04_LoveRunning1.cntg = jcast('int', 0)
Code04_LoveRunning1.dep = jarray('int', [Code04_LoveRunning1.MAXN])
Code04_LoveRunning1.stjump = jarray('int', [Code04_LoveRunning1.MAXN, Code04_LoveRunning1.MAXP])
Code04_LoveRunning1.rtUp = jarray('int', [Code04_LoveRunning1.MAXN])
Code04_LoveRunning1.rtDown = jarray('int', [Code04_LoveRunning1.MAXN])
Code04_LoveRunning1.ls = jarray('int', [Code04_LoveRunning1.MAXT])
Code04_LoveRunning1.rs = jarray('int', [Code04_LoveRunning1.MAXT])
Code04_LoveRunning1.sum = jarray('int', [Code04_LoveRunning1.MAXT])
Code04_LoveRunning1.cntt = jcast('int', 0)
Code04_LoveRunning1.ans = jarray('int', [Code04_LoveRunning1.MAXN])
Code04_LoveRunning1.ufe = jarray('int', [Code04_LoveRunning1.MAXN, 3])
Code04_LoveRunning1.stacksize = jcast('int', 0)
Code04_LoveRunning1.u = jcast('int', 0)
Code04_LoveRunning1.f = jcast('int', 0)
Code04_LoveRunning1.e = jcast('int', 0)

if __name__ == '__main__':
    Code04_LoveRunning1.main([])
