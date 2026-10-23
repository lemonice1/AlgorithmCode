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

# 美丽的树，倍增优化建图，Python版
# 一共n个节点，给定n-1条无向边，所有节点组成一棵树，1号节点是根
# 你需要给每个节点赋值，但是不能破坏如下的m条关系，关系的格式如下
# 关系 1 a b c : 节点a到节点b的路径上，值最小的节点必须是节点c，输入保证c一定在路径上
# 关系 2 a b c : 节点a到节点b的路径上，值最大的节点必须是节点c，输入保证c一定在路径上
# 如果存在赋值方案，并且这些值是1到n的一个排列，打印一种方案即可，否则打印-1
# 2 <= n、m <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF1904F
# 测试链接 : https://codeforces.com/problemset/problem/1904/F
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_BeautifulTreeST2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'MAXP': 'MAXP', 'MAXK': 'MAXK', 'n': 'n', 'm': 'm', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'cnt1': 'cnt1', 'indegree': 'indegree', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'cnt2': 'cnt2', 'dep': 'dep', 'dfn': 'dfn', 'siz': 'siz', 'stjump': 'stjump', 'cntd': 'cntd', 'stout': 'stout', 'stin': 'stin', 'cntt': 'cntt', 'que': 'que', 'ans': 'ans'}
    MAXN = 0
    MAXT = 0
    MAXE = 0
    MAXP = 0
    MAXK = 0
    n = 0
    m = 0
    # 原树
    head1 = None
    next1 = None
    to1 = None
    cnt1 = 0
    # 关系图
    indegree = None
    head2 = None
    next2 = None
    to2 = None
    cnt2 = 0
    # 树上倍增
    dep = None
    dfn = None
    siz = None
    stjump = None
    cntd = 0
    # 倍增优化建图，出表和入表
    stout = None
    stin = None
    cntt = 0
    # 拓扑排序
    que = None
    ans = None
    @staticmethod
    def idx(u, p):
        u = jcast('int', u)
        p = jcast('int', p)
        return jcast('int', jcast('int', jadd(jcast('int', (u * Code07_BeautifulTreeST2.MAXP)), p)))

    @staticmethod
    def addEdge1(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_BeautifulTreeST2.next1, ((_java_obj_1 := Code07_BeautifulTreeST2), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_BeautifulTreeST2.head1[u])
        Code07_BeautifulTreeST2.to1[Code07_BeautifulTreeST2.cnt1] = jcast('int', v)
        Code07_BeautifulTreeST2.head1[u] = jcast('int', Code07_BeautifulTreeST2.cnt1)

    @staticmethod
    def addEdge2(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code07_BeautifulTreeST2.indegree[v] = jcast('int', (Code07_BeautifulTreeST2.indegree[v] + 1))
        jset(Code07_BeautifulTreeST2.next2, ((_java_obj_4 := Code07_BeautifulTreeST2), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code07_BeautifulTreeST2.head2[u])
        Code07_BeautifulTreeST2.to2[Code07_BeautifulTreeST2.cnt2] = jcast('int', v)
        Code07_BeautifulTreeST2.head2[u] = jcast('int', Code07_BeautifulTreeST2.cnt2)

    @staticmethod
    def build(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code07_BeautifulTreeST2.dep[u] = jcast('int', jcast('int', jadd(Code07_BeautifulTreeST2.dep[fa], 1)))
        jset(Code07_BeautifulTreeST2.dfn, u, ((_java_obj_7 := Code07_BeautifulTreeST2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
        Code07_BeautifulTreeST2.siz[u] = jcast('int', 1)
        jset(Code07_BeautifulTreeST2.stjump, Code07_BeautifulTreeST2.idx(u, 0), fa)
        jset(Code07_BeautifulTreeST2.stout, Code07_BeautifulTreeST2.idx(u, 0), ((_java_obj_10 := Code07_BeautifulTreeST2), (_java_key_11 := 'cntt'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
        Code07_BeautifulTreeST2.addEdge2(u, Code07_BeautifulTreeST2.cntt)
        Code07_BeautifulTreeST2.addEdge2(fa, Code07_BeautifulTreeST2.cntt)
        jset(Code07_BeautifulTreeST2.stin, Code07_BeautifulTreeST2.idx(u, 0), ((_java_obj_13 := Code07_BeautifulTreeST2), (_java_key_14 := 'cntt'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
        Code07_BeautifulTreeST2.addEdge2(Code07_BeautifulTreeST2.cntt, u)
        Code07_BeautifulTreeST2.addEdge2(Code07_BeautifulTreeST2.cntt, fa)
        p = jcast('int', 1)
        while (p < Code07_BeautifulTreeST2.MAXP):
            jset(Code07_BeautifulTreeST2.stjump, Code07_BeautifulTreeST2.idx(u, p), Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(u, jcast('int', (p - 1)))], jcast('int', (p - 1)))])
            jset(Code07_BeautifulTreeST2.stout, Code07_BeautifulTreeST2.idx(u, p), ((_java_obj_16 := Code07_BeautifulTreeST2), (_java_key_17 := 'cntt'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3])
            Code07_BeautifulTreeST2.addEdge2(Code07_BeautifulTreeST2.stout[Code07_BeautifulTreeST2.idx(u, jcast('int', (p - 1)))], Code07_BeautifulTreeST2.cntt)
            Code07_BeautifulTreeST2.addEdge2(Code07_BeautifulTreeST2.stout[Code07_BeautifulTreeST2.idx(Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(u, jcast('int', (p - 1)))], jcast('int', (p - 1)))], Code07_BeautifulTreeST2.cntt)
            jset(Code07_BeautifulTreeST2.stin, Code07_BeautifulTreeST2.idx(u, p), ((_java_obj_19 := Code07_BeautifulTreeST2), (_java_key_20 := 'cntt'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3])
            Code07_BeautifulTreeST2.addEdge2(Code07_BeautifulTreeST2.cntt, Code07_BeautifulTreeST2.stin[Code07_BeautifulTreeST2.idx(u, jcast('int', (p - 1)))])
            Code07_BeautifulTreeST2.addEdge2(Code07_BeautifulTreeST2.cntt, Code07_BeautifulTreeST2.stin[Code07_BeautifulTreeST2.idx(Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(u, jcast('int', (p - 1)))], jcast('int', (p - 1)))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code07_BeautifulTreeST2.head1[u])
        while (e > 0):
            v = jcast('int', Code07_BeautifulTreeST2.to1[e])
            if (v != fa):
                Code07_BeautifulTreeST2.build(v, u)
                Code07_BeautifulTreeST2.siz[u] = jcast('int', jcast('int', jadd(Code07_BeautifulTreeST2.siz[u], Code07_BeautifulTreeST2.siz[v])))
            e = jcast('int', Code07_BeautifulTreeST2.next1[e])

    @staticmethod
    def isAncestor(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        return jcast('boolean', ((Code07_BeautifulTreeST2.dfn[a] <= Code07_BeautifulTreeST2.dfn[b]) and (Code07_BeautifulTreeST2.dfn[b] < jcast('int', jadd(Code07_BeautifulTreeST2.dfn[a], Code07_BeautifulTreeST2.siz[a])))))

    @staticmethod
    def kthAncestor(x, k):
        x = jcast('int', x)
        k = jcast('int', k)
        p = jcast('int', 0)
        while (p < Code07_BeautifulTreeST2.MAXP):
            if (jcast('int', (jcast('int', (k >> (p & 31))) & 1)) != 0):
                x = jcast('int', Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(x, p)])
            p = jcast('int', (p + 1))
        return jcast('int', x)

    @staticmethod
    def nearest(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        if Code07_BeautifulTreeST2.isAncestor(y, x):
            return jcast('int', Code07_BeautifulTreeST2.kthAncestor(x, jcast('int', (jcast('int', (Code07_BeautifulTreeST2.dep[x] - Code07_BeautifulTreeST2.dep[y])) - 1))))
        else:
            return jcast('int', Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(y, 0)])

    @staticmethod
    def pathOut(x, y, c):
        x = jcast('int', x)
        y = jcast('int', y)
        c = jcast('int', c)
        if (Code07_BeautifulTreeST2.dep[x] < Code07_BeautifulTreeST2.dep[y]):
            tmp = jcast('int', x)
            x = jcast('int', y)
            y = jcast('int', tmp)
        Code07_BeautifulTreeST2.addEdge2(y, c)
        p = jcast('int', jcast('int', (Code07_BeautifulTreeST2.MAXP - 1)))
        while (p >= 0):
            if (Code07_BeautifulTreeST2.dep[Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(x, p)]] >= Code07_BeautifulTreeST2.dep[y]):
                Code07_BeautifulTreeST2.addEdge2(Code07_BeautifulTreeST2.stout[Code07_BeautifulTreeST2.idx(x, p)], c)
                x = jcast('int', Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(x, p)])
            p = jcast('int', (p - 1))
        if (x == y):
            return
        p = jcast('int', jcast('int', (Code07_BeautifulTreeST2.MAXP - 1)))
        while (p >= 0):
            if (Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(x, p)] != Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(y, p)]):
                Code07_BeautifulTreeST2.addEdge2(Code07_BeautifulTreeST2.stout[Code07_BeautifulTreeST2.idx(x, p)], c)
                Code07_BeautifulTreeST2.addEdge2(Code07_BeautifulTreeST2.stout[Code07_BeautifulTreeST2.idx(y, p)], c)
                x = jcast('int', Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(x, p)])
                y = jcast('int', Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(y, p)])
            p = jcast('int', (p - 1))
        Code07_BeautifulTreeST2.addEdge2(Code07_BeautifulTreeST2.stout[Code07_BeautifulTreeST2.idx(x, 0)], c)

    @staticmethod
    def pathIn(x, y, c):
        x = jcast('int', x)
        y = jcast('int', y)
        c = jcast('int', c)
        if (Code07_BeautifulTreeST2.dep[x] < Code07_BeautifulTreeST2.dep[y]):
            tmp = jcast('int', x)
            x = jcast('int', y)
            y = jcast('int', tmp)
        Code07_BeautifulTreeST2.addEdge2(c, y)
        p = jcast('int', jcast('int', (Code07_BeautifulTreeST2.MAXP - 1)))
        while (p >= 0):
            if (Code07_BeautifulTreeST2.dep[Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(x, p)]] >= Code07_BeautifulTreeST2.dep[y]):
                Code07_BeautifulTreeST2.addEdge2(c, Code07_BeautifulTreeST2.stin[Code07_BeautifulTreeST2.idx(x, p)])
                x = jcast('int', Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(x, p)])
            p = jcast('int', (p - 1))
        if (x == y):
            return
        p = jcast('int', jcast('int', (Code07_BeautifulTreeST2.MAXP - 1)))
        while (p >= 0):
            if (Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(x, p)] != Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(y, p)]):
                Code07_BeautifulTreeST2.addEdge2(c, Code07_BeautifulTreeST2.stin[Code07_BeautifulTreeST2.idx(x, p)])
                Code07_BeautifulTreeST2.addEdge2(c, Code07_BeautifulTreeST2.stin[Code07_BeautifulTreeST2.idx(y, p)])
                x = jcast('int', Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(x, p)])
                y = jcast('int', Code07_BeautifulTreeST2.stjump[Code07_BeautifulTreeST2.idx(y, p)])
            p = jcast('int', (p - 1))
        Code07_BeautifulTreeST2.addEdge2(c, Code07_BeautifulTreeST2.stin[Code07_BeautifulTreeST2.idx(x, 0)])

    @staticmethod
    def pathMin(a, b, c):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        if (a != c):
            Code07_BeautifulTreeST2.pathIn(a, Code07_BeautifulTreeST2.nearest(a, c), c)
        if (b != c):
            Code07_BeautifulTreeST2.pathIn(b, Code07_BeautifulTreeST2.nearest(b, c), c)

    @staticmethod
    def pathMax(a, b, c):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        if (a != c):
            Code07_BeautifulTreeST2.pathOut(a, Code07_BeautifulTreeST2.nearest(a, c), c)
        if (b != c):
            Code07_BeautifulTreeST2.pathOut(b, Code07_BeautifulTreeST2.nearest(b, c), c)

    @staticmethod
    def topo():
        qi = jcast('int', 1)
        qsiz = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code07_BeautifulTreeST2.cntt):
            if (Code07_BeautifulTreeST2.indegree[i] == 0):
                jset(Code07_BeautifulTreeST2.que, (qsiz := jcast('int', (qsiz + (1)))), i)
            i = jcast('int', (i + 1))
        val = jcast('int', 0)
        while (qi <= qsiz):
            u = jcast('int', Code07_BeautifulTreeST2.que[((_java_old_22 := qi), (qi := jcast('int', (qi + (1)))), _java_old_22)[2]])
            if (u <= Code07_BeautifulTreeST2.n):
                jset(Code07_BeautifulTreeST2.ans, u, (val := jcast('int', (val + (1)))))
            e = jcast('int', Code07_BeautifulTreeST2.head2[u])
            while (e > 0):
                v = jcast('int', Code07_BeautifulTreeST2.to2[e])
                if (((_java_obj_23 := Code07_BeautifulTreeST2.indegree), (_java_key_24 := v), (_java_old_25 := jget(_java_obj_23, _java_key_24)), jset(_java_obj_23, _java_key_24, jcast('int', (_java_old_25 + (-1)))))[3] == 0):
                    jset(Code07_BeautifulTreeST2.que, (qsiz := jcast('int', (qsiz + (1)))), v)
                e = jcast('int', Code07_BeautifulTreeST2.next2[e])
        return jcast('boolean', (qsiz == Code07_BeautifulTreeST2.cntt))

    @staticmethod
    def main(args):
        in_ = Code07_BeautifulTreeST2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_BeautifulTreeST2.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_BeautifulTreeST2.m = jcast('int', jcall(in_, 'nextInt'))
        Code07_BeautifulTreeST2.cntt = jcast('int', Code07_BeautifulTreeST2.n)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code07_BeautifulTreeST2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code07_BeautifulTreeST2.addEdge1(u, v)
            Code07_BeautifulTreeST2.addEdge1(v, u)
            i = jcast('int', (i + 1))
        Code07_BeautifulTreeST2.build(1, 1)
        i = jcast('int', 1)
        op = 0
        a = 0
        b = 0
        c = 0
        while (i <= Code07_BeautifulTreeST2.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            a = jcast('int', jcall(in_, 'nextInt'))
            b = jcast('int', jcall(in_, 'nextInt'))
            c = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                Code07_BeautifulTreeST2.pathMin(a, b, c)
            else:
                Code07_BeautifulTreeST2.pathMax(a, b, c)
            i = jcast('int', (i + 1))
        check = jcast('boolean', Code07_BeautifulTreeST2.topo())
        if check:
            i = jcast('int', 1)
            while (i <= Code07_BeautifulTreeST2.n):
                jcall(out, 'print', Code07_BeautifulTreeST2.ans[i])
                jcall(out, 'print', ' ')
                i = jcast('int', (i + 1))
        else:
            jcall(out, 'println', jcast('int', (-1)))
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
            return jcast('int', self.buffer[((_java_obj_26 := self), (_java_key_27 := 'ptr'), (_java_old_28 := jget(_java_obj_26, _java_key_27)), jset(_java_obj_26, _java_key_27, jcast('int', (_java_old_28 + (1)))), _java_old_28)[4]])

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
            raise TypeError("No matching overload for Code07_BeautifulTreeST2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_BeautifulTreeST2.MAXN = jcast('int', 200001)
Code07_BeautifulTreeST2.MAXT = jcast('int', jcast('int', (Code07_BeautifulTreeST2.MAXN * 41)))
Code07_BeautifulTreeST2.MAXE = jcast('int', jcast('int', (Code07_BeautifulTreeST2.MAXN * 201)))
Code07_BeautifulTreeST2.MAXP = jcast('int', 17)
Code07_BeautifulTreeST2.MAXK = jcast('int', jcast('int', (Code07_BeautifulTreeST2.MAXN * Code07_BeautifulTreeST2.MAXP)))
Code07_BeautifulTreeST2.n = jcast('int', 0)
Code07_BeautifulTreeST2.m = jcast('int', 0)
Code07_BeautifulTreeST2.head1 = jarray('int', [Code07_BeautifulTreeST2.MAXN])
Code07_BeautifulTreeST2.next1 = jarray('int', [jcast('int', (Code07_BeautifulTreeST2.MAXN << (1 & 31)))])
Code07_BeautifulTreeST2.to1 = jarray('int', [jcast('int', (Code07_BeautifulTreeST2.MAXN << (1 & 31)))])
Code07_BeautifulTreeST2.cnt1 = jcast('int', 0)
Code07_BeautifulTreeST2.indegree = jarray('int', [Code07_BeautifulTreeST2.MAXT])
Code07_BeautifulTreeST2.head2 = jarray('int', [Code07_BeautifulTreeST2.MAXT])
Code07_BeautifulTreeST2.next2 = jarray('int', [Code07_BeautifulTreeST2.MAXE])
Code07_BeautifulTreeST2.to2 = jarray('int', [Code07_BeautifulTreeST2.MAXE])
Code07_BeautifulTreeST2.cnt2 = jcast('int', 0)
Code07_BeautifulTreeST2.dep = jarray('int', [Code07_BeautifulTreeST2.MAXN])
Code07_BeautifulTreeST2.dfn = jarray('int', [Code07_BeautifulTreeST2.MAXN])
Code07_BeautifulTreeST2.siz = jarray('int', [Code07_BeautifulTreeST2.MAXN])
Code07_BeautifulTreeST2.stjump = jarray('int', [Code07_BeautifulTreeST2.MAXK])
Code07_BeautifulTreeST2.cntd = jcast('int', 0)
Code07_BeautifulTreeST2.stout = jarray('int', [Code07_BeautifulTreeST2.MAXK])
Code07_BeautifulTreeST2.stin = jarray('int', [Code07_BeautifulTreeST2.MAXK])
Code07_BeautifulTreeST2.cntt = jcast('int', 0)
Code07_BeautifulTreeST2.que = jarray('int', [Code07_BeautifulTreeST2.MAXT])
Code07_BeautifulTreeST2.ans = jarray('int', [Code07_BeautifulTreeST2.MAXN])

if __name__ == '__main__':
    Code07_BeautifulTreeST2.main([])
