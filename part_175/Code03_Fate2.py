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

# 命运，Python版
# 一共有n个节点，给定n-1条边，所有节点组成一棵树，规定1号节点是树头
# 给定m个点对，每个点对(x, y)，x是y的祖先节点，路径由从上到下的边组成
# 树上的每条边都要涂上白色或者黑色，完全由你决定
# 但是请保证每个点对的路径中，至少有一条黑色的边存在
# 打印给树涂色的方法数，答案对 998244353 取模
# 1 <= n、m <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P6773
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Fate2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MOD': 'MOD', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'sum': 'sum', 'mulLazy': 'mulLazy', 'cntt': 'cntt', 'dep': 'dep', 'maxdep': 'maxdep', 'ufe': 'ufe', 'stacksize': 'stacksize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    MAXT = 0
    MOD = 0
    n = 0
    m = 0
    head = None
    nxt = None
    to = None
    cntg = 0
    root = None
    ls = None
    rs = None
    sum = None
    mulLazy = None
    cntt = 0
    dep = None
    maxdep = None
    # 讲解118，递归改迭代需要的栈
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
        jset(Code03_Fate2.ufe[Code03_Fate2.stacksize], 0, u)
        jset(Code03_Fate2.ufe[Code03_Fate2.stacksize], 1, f)
        jset(Code03_Fate2.ufe[Code03_Fate2.stacksize], 2, e)
        Code03_Fate2.stacksize = jcast('int', (Code03_Fate2.stacksize + 1))

    @staticmethod
    def pop():
        Code03_Fate2.stacksize = jcast('int', (Code03_Fate2.stacksize - 1))
        Code03_Fate2.u = jcast('int', Code03_Fate2.ufe[Code03_Fate2.stacksize][0])
        Code03_Fate2.f = jcast('int', Code03_Fate2.ufe[Code03_Fate2.stacksize][1])
        Code03_Fate2.e = jcast('int', Code03_Fate2.ufe[Code03_Fate2.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_Fate2.nxt, ((_java_obj_1 := Code03_Fate2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_Fate2.head[u])
        Code03_Fate2.to[Code03_Fate2.cntg] = jcast('int', v)
        Code03_Fate2.head[u] = jcast('int', Code03_Fate2.cntg)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code03_Fate2.sum[i] = jcast('long', jcast('long', jmod(jcast('long', jadd(Code03_Fate2.sum[Code03_Fate2.ls[i]], Code03_Fate2.sum[Code03_Fate2.rs[i]])), Code03_Fate2.MOD)))

    @staticmethod
    def lazy(i, v):
        i = jcast('int', i)
        v = jcast('long', v)
        if (i != 0):
            Code03_Fate2.sum[i] = jcast('long', jcast('long', jmod(jcast('long', (Code03_Fate2.sum[i] * v)), Code03_Fate2.MOD)))
            Code03_Fate2.mulLazy[i] = jcast('long', jcast('long', jmod(jcast('long', (Code03_Fate2.mulLazy[i] * v)), Code03_Fate2.MOD)))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if (Code03_Fate2.mulLazy[i] != 1):
            Code03_Fate2.lazy(Code03_Fate2.ls[i], Code03_Fate2.mulLazy[i])
            Code03_Fate2.lazy(Code03_Fate2.rs[i], Code03_Fate2.mulLazy[i])
            Code03_Fate2.mulLazy[i] = jcast('long', 1)

    @staticmethod
    def insert(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', i)
        if (rt == 0):
            rt = jcast('int', ((_java_obj_4 := Code03_Fate2), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
            Code03_Fate2.mulLazy[rt] = jcast('long', 1)
        if (l == r):
            Code03_Fate2.sum[rt] = jcast('long', 1)
        else:
            Code03_Fate2.down(rt)
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code03_Fate2.ls, rt, Code03_Fate2.insert(jobi, l, mid, Code03_Fate2.ls[rt]))
            else:
                jset(Code03_Fate2.rs, rt, Code03_Fate2.insert(jobi, jcast('int', jadd(mid, 1)), r, Code03_Fate2.rs[rt]))
            Code03_Fate2.up(rt)
        return jcast('int', rt)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            return jcast('long', 0)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', jcast('long', jmod(Code03_Fate2.sum[i], Code03_Fate2.MOD)))
        Code03_Fate2.down(i)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('long', 0)
        if (jobl <= mid):
            ans = jcast('long', Code03_Fate2.query(jobl, jobr, l, mid, Code03_Fate2.ls[i]))
        if (jobr > mid):
            ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, Code03_Fate2.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code03_Fate2.rs[i]))), Code03_Fate2.MOD)))
        return jcast('long', ans)

    @staticmethod
    def merge(l, r, t1, t2, sum1, sum2):
        l = jcast('int', l)
        r = jcast('int', r)
        t1 = jcast('int', t1)
        t2 = jcast('int', t2)
        sum1 = jcast('long', sum1)
        sum2 = jcast('long', sum2)
        if ((t1 == 0) or (t2 == 0)):
            if (t1 != 0):
                Code03_Fate2.lazy(t1, sum2)
            if (t2 != 0):
                Code03_Fate2.lazy(t2, sum1)
            return jcast('int', jcast('int', jadd(t1, t2)))
        if (l == r):
            Code03_Fate2.sum[t1] = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(jcast('long', (Code03_Fate2.sum[t1] * jcast('long', jadd(sum2, Code03_Fate2.sum[t2])))), Code03_Fate2.MOD)), jcast('long', jmod(jcast('long', (Code03_Fate2.sum[t2] * sum1)), Code03_Fate2.MOD)))), Code03_Fate2.MOD)))
        else:
            Code03_Fate2.down(t1)
            Code03_Fate2.down(t2)
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            tmp1 = jcast('long', Code03_Fate2.sum[Code03_Fate2.ls[t1]])
            tmp2 = jcast('long', Code03_Fate2.sum[Code03_Fate2.ls[t2]])
            jset(Code03_Fate2.ls, t1, Code03_Fate2.merge(l, mid, Code03_Fate2.ls[t1], Code03_Fate2.ls[t2], sum1, sum2))
            jset(Code03_Fate2.rs, t1, Code03_Fate2.merge(jcast('int', jadd(mid, 1)), r, Code03_Fate2.rs[t1], Code03_Fate2.rs[t2], jcast('long', jadd(sum1, tmp1)), jcast('long', jadd(sum2, tmp2))))
            Code03_Fate2.up(t1)
        return jcast('int', t1)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code03_Fate2.dep[u] = jcast('int', jcast('int', jadd(Code03_Fate2.dep[fa], 1)))
        e = jcast('int', Code03_Fate2.head[u])
        while (e > 0):
            v = jcast('int', Code03_Fate2.to[e])
            if (v != fa):
                Code03_Fate2.dfs1(v, u)
            e = jcast('int', Code03_Fate2.nxt[e])

    # dfs1的迭代版
    @staticmethod
    def dfs2():
        Code03_Fate2.stacksize = jcast('int', 0)
        Code03_Fate2.push(1, 0, jcast('int', (-1)))
        while (Code03_Fate2.stacksize > 0):
            Code03_Fate2.pop()
            if (Code03_Fate2.e == jcast('int', (-1))):
                Code03_Fate2.dep[Code03_Fate2.u] = jcast('int', jcast('int', jadd(Code03_Fate2.dep[Code03_Fate2.f], 1)))
                Code03_Fate2.e = jcast('int', Code03_Fate2.head[Code03_Fate2.u])
            else:
                Code03_Fate2.e = jcast('int', Code03_Fate2.nxt[Code03_Fate2.e])
            if (Code03_Fate2.e != 0):
                Code03_Fate2.push(Code03_Fate2.u, Code03_Fate2.f, Code03_Fate2.e)
                if (Code03_Fate2.to[Code03_Fate2.e] != Code03_Fate2.f):
                    Code03_Fate2.push(Code03_Fate2.to[Code03_Fate2.e], Code03_Fate2.u, jcast('int', (-1)))

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dp1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code03_Fate2.root, u, Code03_Fate2.insert(Code03_Fate2.maxdep[u], 0, Code03_Fate2.n, Code03_Fate2.root[u]))
        e = jcast('int', Code03_Fate2.head[u])
        while (e > 0):
            v = jcast('int', Code03_Fate2.to[e])
            if (v != fa):
                Code03_Fate2.dp1(v, u)
                jset(Code03_Fate2.root, u, Code03_Fate2.merge(0, Code03_Fate2.n, Code03_Fate2.root[u], Code03_Fate2.root[v], 0, Code03_Fate2.query(0, Code03_Fate2.dep[u], 0, Code03_Fate2.n, Code03_Fate2.root[v])))
            e = jcast('int', Code03_Fate2.nxt[e])

    # dp1的迭代版
    @staticmethod
    def dp2():
        Code03_Fate2.stacksize = jcast('int', 0)
        Code03_Fate2.push(1, 0, jcast('int', (-1)))
        while (Code03_Fate2.stacksize > 0):
            Code03_Fate2.pop()
            if (Code03_Fate2.e == jcast('int', (-1))):
                jset(Code03_Fate2.root, Code03_Fate2.u, Code03_Fate2.insert(Code03_Fate2.maxdep[Code03_Fate2.u], 0, Code03_Fate2.n, Code03_Fate2.root[Code03_Fate2.u]))
                Code03_Fate2.e = jcast('int', Code03_Fate2.head[Code03_Fate2.u])
            else:
                Code03_Fate2.e = jcast('int', Code03_Fate2.nxt[Code03_Fate2.e])
            if (Code03_Fate2.e != 0):
                Code03_Fate2.push(Code03_Fate2.u, Code03_Fate2.f, Code03_Fate2.e)
                if (Code03_Fate2.to[Code03_Fate2.e] != Code03_Fate2.f):
                    Code03_Fate2.push(Code03_Fate2.to[Code03_Fate2.e], Code03_Fate2.u, jcast('int', (-1)))
            else:
                ei = jcast('int', Code03_Fate2.head[Code03_Fate2.u])
                while (ei > 0):
                    v = jcast('int', Code03_Fate2.to[ei])
                    if (v != Code03_Fate2.f):
                        jset(Code03_Fate2.root, Code03_Fate2.u, Code03_Fate2.merge(0, Code03_Fate2.n, Code03_Fate2.root[Code03_Fate2.u], Code03_Fate2.root[v], 0, Code03_Fate2.query(0, Code03_Fate2.dep[Code03_Fate2.u], 0, Code03_Fate2.n, Code03_Fate2.root[v])))
                    ei = jcast('int', Code03_Fate2.nxt[ei])

    @staticmethod
    def main(args):
        in_ = Code03_Fate2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_Fate2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code03_Fate2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code03_Fate2.addEdge(u, v)
            Code03_Fate2.addEdge(v, u)
            i = jcast('int', (i + 1))
        # dfs1(1, 0);
        Code03_Fate2.dfs2()
        Code03_Fate2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= Code03_Fate2.m):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            jset(Code03_Fate2.maxdep, y, jstatic('Math', 'max', Code03_Fate2.maxdep[y], Code03_Fate2.dep[x]))
            i = jcast('int', (i + 1))
        # dp1(1, 0);
        Code03_Fate2.dp2()
        ans = jcast('long', jcast('long', jmod(Code03_Fate2.query(0, 0, 0, Code03_Fate2.n, Code03_Fate2.root[1]), Code03_Fate2.MOD)))
        jcall(out, 'println', ans)
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
            raise TypeError("No matching overload for Code03_Fate2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Fate2.MAXN = jcast('int', 500001)
Code03_Fate2.MAXT = jcast('int', jcast('int', (Code03_Fate2.MAXN * 40)))
Code03_Fate2.MOD = jcast('int', 998244353)
Code03_Fate2.n = jcast('int', 0)
Code03_Fate2.m = jcast('int', 0)
Code03_Fate2.head = jarray('int', [Code03_Fate2.MAXN])
Code03_Fate2.nxt = jarray('int', [jcast('int', (Code03_Fate2.MAXN << (1 & 31)))])
Code03_Fate2.to = jarray('int', [jcast('int', (Code03_Fate2.MAXN << (1 & 31)))])
Code03_Fate2.cntg = jcast('int', 0)
Code03_Fate2.root = jarray('int', [Code03_Fate2.MAXN])
Code03_Fate2.ls = jarray('int', [Code03_Fate2.MAXT])
Code03_Fate2.rs = jarray('int', [Code03_Fate2.MAXT])
Code03_Fate2.sum = jarray('long', [Code03_Fate2.MAXT])
Code03_Fate2.mulLazy = jarray('long', [Code03_Fate2.MAXT])
Code03_Fate2.cntt = jcast('int', 0)
Code03_Fate2.dep = jarray('int', [Code03_Fate2.MAXN])
Code03_Fate2.maxdep = jarray('int', [Code03_Fate2.MAXN])
Code03_Fate2.ufe = jarray('int', [Code03_Fate2.MAXN, 3])
Code03_Fate2.stacksize = jcast('int', 0)
Code03_Fate2.u = jcast('int', 0)
Code03_Fate2.f = jcast('int', 0)
Code03_Fate2.e = jcast('int', 0)

if __name__ == '__main__':
    Code03_Fate2.main([])
