# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 晋升者计数，Python版
# 一共有n个人，给定每个人的能力值arr[i]，所有人组成一棵树，代表公司的组织
# 1号人是整个公司的老板，从2号人开始，给定每个人的上司编号fa[i]
# 打印第i号人为头的子树中，有多少个人的能力值 > 第i号人的能力值，一共n条打印
# 1 <= n <= 10^5
# 1 <= arr[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P3605
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_PromotionCounting1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'arr': 'arr', 'sorted': 'sorted', 'cntv': 'cntv', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'siz': 'siz', 'cntt': 'cntt', 'ans': 'ans', 'ufe': 'ufe', 'stacksize': 'stacksize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    MAXT = 0
    n = 0
    head = None
    nxt = None
    to = None
    cntg = 0
    arr = None
    sorted = None
    cntv = 0
    root = None
    ls = None
    rs = None
    siz = None
    cntt = 0
    ans = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_PromotionCounting1.nxt, ((_java_obj_1 := Code01_PromotionCounting1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_PromotionCounting1.head[u])
        Code01_PromotionCounting1.to[Code01_PromotionCounting1.cntg] = jcast('int', v)
        Code01_PromotionCounting1.head[u] = jcast('int', Code01_PromotionCounting1.cntg)

    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code01_PromotionCounting1.cntv)
        mid = 0
        ret = jcast('int', 0)
        while (left <= right):
            mid = jcast('int', jcast('int', (jcast('int', jadd(left, right)) >> (1 & 31))))
            if (Code01_PromotionCounting1.sorted[mid] <= num):
                ret = jcast('int', mid)
                left = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ret)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code01_PromotionCounting1.siz[i] = jcast('int', jcast('int', jadd(Code01_PromotionCounting1.siz[Code01_PromotionCounting1.ls[i]], Code01_PromotionCounting1.siz[Code01_PromotionCounting1.rs[i]])))

    @staticmethod
    def add(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', i)
        if (rt == 0):
            rt = jcast('int', ((_java_obj_4 := Code01_PromotionCounting1), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        if (l == r):
            Code01_PromotionCounting1.siz[rt] = jcast('int', (Code01_PromotionCounting1.siz[rt] + 1))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code01_PromotionCounting1.ls, rt, Code01_PromotionCounting1.add(jobi, l, mid, Code01_PromotionCounting1.ls[rt]))
            else:
                jset(Code01_PromotionCounting1.rs, rt, Code01_PromotionCounting1.add(jobi, jcast('int', jadd(mid, 1)), r, Code01_PromotionCounting1.rs[rt]))
            Code01_PromotionCounting1.up(rt)
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
            Code01_PromotionCounting1.siz[t1] = jcast('int', jcast('int', jadd(Code01_PromotionCounting1.siz[t1], Code01_PromotionCounting1.siz[t2])))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code01_PromotionCounting1.ls, t1, Code01_PromotionCounting1.merge(l, mid, Code01_PromotionCounting1.ls[t1], Code01_PromotionCounting1.ls[t2]))
            jset(Code01_PromotionCounting1.rs, t1, Code01_PromotionCounting1.merge(jcast('int', jadd(mid, 1)), r, Code01_PromotionCounting1.rs[t1], Code01_PromotionCounting1.rs[t2]))
            Code01_PromotionCounting1.up(t1)
        return jcast('int', t1)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl > jobr) or (i == 0)):
            return jcast('int', 0)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code01_PromotionCounting1.siz[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ret = jcast('int', 0)
        if (jobl <= mid):
            ret = jcast('int', jcast('int', jadd(ret, Code01_PromotionCounting1.query(jobl, jobr, l, mid, Code01_PromotionCounting1.ls[i]))))
        if (jobr > mid):
            ret = jcast('int', jcast('int', jadd(ret, Code01_PromotionCounting1.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code01_PromotionCounting1.rs[i]))))
        return jcast('int', ret)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def calc1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        e = jcast('int', Code01_PromotionCounting1.head[u])
        while (e > 0):
            v = jcast('int', Code01_PromotionCounting1.to[e])
            if (v != fa):
                Code01_PromotionCounting1.calc1(v, u)
                jset(Code01_PromotionCounting1.root, u, Code01_PromotionCounting1.merge(1, Code01_PromotionCounting1.cntv, Code01_PromotionCounting1.root[u], Code01_PromotionCounting1.root[v]))
            e = jcast('int', Code01_PromotionCounting1.nxt[e])
        jset(Code01_PromotionCounting1.ans, u, Code01_PromotionCounting1.query(jcast('int', jadd(Code01_PromotionCounting1.arr[u], 1)), Code01_PromotionCounting1.cntv, 1, Code01_PromotionCounting1.cntv, Code01_PromotionCounting1.root[u]))

    # 递归函数改迭代需要的栈，不会改去看讲解118
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
        jset(Code01_PromotionCounting1.ufe[Code01_PromotionCounting1.stacksize], 0, u)
        jset(Code01_PromotionCounting1.ufe[Code01_PromotionCounting1.stacksize], 1, f)
        jset(Code01_PromotionCounting1.ufe[Code01_PromotionCounting1.stacksize], 2, e)
        Code01_PromotionCounting1.stacksize = jcast('int', (Code01_PromotionCounting1.stacksize + 1))

    @staticmethod
    def pop():
        Code01_PromotionCounting1.stacksize = jcast('int', (Code01_PromotionCounting1.stacksize - 1))
        Code01_PromotionCounting1.u = jcast('int', Code01_PromotionCounting1.ufe[Code01_PromotionCounting1.stacksize][0])
        Code01_PromotionCounting1.f = jcast('int', Code01_PromotionCounting1.ufe[Code01_PromotionCounting1.stacksize][1])
        Code01_PromotionCounting1.e = jcast('int', Code01_PromotionCounting1.ufe[Code01_PromotionCounting1.stacksize][2])

    # calc1改迭代
    @staticmethod
    def calc2():
        Code01_PromotionCounting1.stacksize = jcast('int', 0)
        Code01_PromotionCounting1.push(1, 0, jcast('int', (-1)))
        while (Code01_PromotionCounting1.stacksize > 0):
            Code01_PromotionCounting1.pop()
            if (Code01_PromotionCounting1.e == jcast('int', (-1))):
                Code01_PromotionCounting1.e = jcast('int', Code01_PromotionCounting1.head[Code01_PromotionCounting1.u])
            else:
                Code01_PromotionCounting1.e = jcast('int', Code01_PromotionCounting1.nxt[Code01_PromotionCounting1.e])
            if (Code01_PromotionCounting1.e != 0):
                Code01_PromotionCounting1.push(Code01_PromotionCounting1.u, Code01_PromotionCounting1.f, Code01_PromotionCounting1.e)
                if (Code01_PromotionCounting1.to[Code01_PromotionCounting1.e] != Code01_PromotionCounting1.f):
                    Code01_PromotionCounting1.push(Code01_PromotionCounting1.to[Code01_PromotionCounting1.e], Code01_PromotionCounting1.u, jcast('int', (-1)))
            else:
                ei = jcast('int', Code01_PromotionCounting1.head[Code01_PromotionCounting1.u])
                while (ei > 0):
                    v = jcast('int', Code01_PromotionCounting1.to[ei])
                    if (v != Code01_PromotionCounting1.f):
                        jset(Code01_PromotionCounting1.root, Code01_PromotionCounting1.u, Code01_PromotionCounting1.merge(1, Code01_PromotionCounting1.cntv, Code01_PromotionCounting1.root[Code01_PromotionCounting1.u], Code01_PromotionCounting1.root[v]))
                    ei = jcast('int', Code01_PromotionCounting1.nxt[ei])
                jset(Code01_PromotionCounting1.ans, Code01_PromotionCounting1.u, Code01_PromotionCounting1.query(jcast('int', jadd(Code01_PromotionCounting1.arr[Code01_PromotionCounting1.u], 1)), Code01_PromotionCounting1.cntv, 1, Code01_PromotionCounting1.cntv, Code01_PromotionCounting1.root[Code01_PromotionCounting1.u]))

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code01_PromotionCounting1.n):
            Code01_PromotionCounting1.sorted[i] = jcast('int', Code01_PromotionCounting1.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code01_PromotionCounting1.sorted, 1, jcast('int', jadd(Code01_PromotionCounting1.n, 1)))
        Code01_PromotionCounting1.cntv = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code01_PromotionCounting1.n):
            if (Code01_PromotionCounting1.sorted[Code01_PromotionCounting1.cntv] != Code01_PromotionCounting1.sorted[i]):
                jset(Code01_PromotionCounting1.sorted, ((_java_obj_7 := Code01_PromotionCounting1), (_java_key_8 := 'cntv'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], Code01_PromotionCounting1.sorted[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_PromotionCounting1.n):
            jset(Code01_PromotionCounting1.arr, i, Code01_PromotionCounting1.kth(Code01_PromotionCounting1.arr[i]))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_PromotionCounting1.n):
            jset(Code01_PromotionCounting1.root, i, Code01_PromotionCounting1.add(Code01_PromotionCounting1.arr[i], 1, Code01_PromotionCounting1.cntv, Code01_PromotionCounting1.root[i]))
            i = jcast('int', (i + 1))
        # calc1(1, 0);
        Code01_PromotionCounting1.calc2()

    @staticmethod
    def main(args):
        in_ = Code01_PromotionCounting1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_PromotionCounting1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_PromotionCounting1.n):
            jset(Code01_PromotionCounting1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 2)
        fa = 0
        while (i <= Code01_PromotionCounting1.n):
            fa = jcast('int', jcall(in_, 'nextInt'))
            Code01_PromotionCounting1.addEdge(fa, i)
            Code01_PromotionCounting1.addEdge(i, fa)
            i = jcast('int', (i + 1))
        Code01_PromotionCounting1.compute()
        i = jcast('int', 1)
        while (i <= Code01_PromotionCounting1.n):
            jcall(out, 'println', Code01_PromotionCounting1.ans[i])
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
            raise TypeError("No matching overload for Code01_PromotionCounting1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_PromotionCounting1.MAXN = jcast('int', 100001)
Code01_PromotionCounting1.MAXT = jcast('int', jcast('int', (Code01_PromotionCounting1.MAXN * 40)))
Code01_PromotionCounting1.n = jcast('int', 0)
Code01_PromotionCounting1.head = jarray('int', [Code01_PromotionCounting1.MAXN])
Code01_PromotionCounting1.nxt = jarray('int', [jcast('int', (Code01_PromotionCounting1.MAXN << (1 & 31)))])
Code01_PromotionCounting1.to = jarray('int', [jcast('int', (Code01_PromotionCounting1.MAXN << (1 & 31)))])
Code01_PromotionCounting1.cntg = jcast('int', 0)
Code01_PromotionCounting1.arr = jarray('int', [Code01_PromotionCounting1.MAXN])
Code01_PromotionCounting1.sorted = jarray('int', [Code01_PromotionCounting1.MAXN])
Code01_PromotionCounting1.cntv = jcast('int', 0)
Code01_PromotionCounting1.root = jarray('int', [Code01_PromotionCounting1.MAXN])
Code01_PromotionCounting1.ls = jarray('int', [Code01_PromotionCounting1.MAXT])
Code01_PromotionCounting1.rs = jarray('int', [Code01_PromotionCounting1.MAXT])
Code01_PromotionCounting1.siz = jarray('int', [Code01_PromotionCounting1.MAXT])
Code01_PromotionCounting1.cntt = jcast('int', 0)
Code01_PromotionCounting1.ans = jarray('int', [Code01_PromotionCounting1.MAXN])
Code01_PromotionCounting1.ufe = jarray('int', [Code01_PromotionCounting1.MAXN, 3])
Code01_PromotionCounting1.stacksize = jcast('int', 0)
Code01_PromotionCounting1.u = jcast('int', 0)
Code01_PromotionCounting1.f = jcast('int', 0)
Code01_PromotionCounting1.e = jcast('int', 0)

if __name__ == '__main__':
    Code01_PromotionCounting1.main([])
