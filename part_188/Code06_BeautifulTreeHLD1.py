# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 美丽的树，树剖优化建图，Python版
# 一共n个节点，给定n-1条无向边，所有节点组成一棵树，1号节点是根
# 你需要给每个节点赋值，但是不能破坏如下的m条关系，关系的格式如下
# 关系 1 a b c : 节点a到节点b的路径上，值最小的节点必须是节点c，输入保证c一定在路径上
# 关系 2 a b c : 节点a到节点b的路径上，值最大的节点必须是节点c，输入保证c一定在路径上
# 如果存在赋值方案，并且这些值是1到n的一个排列，打印一种方案即可，否则打印-1
# 2 <= n、m <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF1904F
# 测试链接 : https://codeforces.com/problemset/problem/1904/F
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_BeautifulTreeHLD1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'n': 'n', 'm': 'm', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'cnt1': 'cnt1', 'indegree': 'indegree', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'cnt2': 'cnt2', 'ls': 'ls', 'rs': 'rs', 'rootOut': 'rootOut', 'rootIn': 'rootIn', 'cntt': 'cntt', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'dfn': 'dfn', 'seg': 'seg', 'cntd': 'cntd', 'que': 'que', 'ans': 'ans'}
    MAXN = 0
    MAXT = 0
    MAXE = 0
    n = 0
    m = 0
    # 原始的树
    head1 = None
    next1 = None
    to1 = None
    cnt1 = 0
    # 关系图，x -> y，x的值严格小于y
    indegree = None
    head2 = None
    next2 = None
    to2 = None
    cnt2 = 0
    # 线段树优化建图，出树和入树
    ls = None
    rs = None
    rootOut = 0
    rootIn = 0
    cntt = 0
    # 树链剖分
    fa = None
    dep = None
    siz = None
    son = None
    top = None
    dfn = None
    seg = None
    cntd = 0
    # 拓扑排序
    que = None
    ans = None
    @staticmethod
    def addEdge1(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code06_BeautifulTreeHLD1.next1, ((_java_obj_1 := Code06_BeautifulTreeHLD1), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_BeautifulTreeHLD1.head1[u])
        Code06_BeautifulTreeHLD1.to1[Code06_BeautifulTreeHLD1.cnt1] = jcast('int', v)
        Code06_BeautifulTreeHLD1.head1[u] = jcast('int', Code06_BeautifulTreeHLD1.cnt1)

    @staticmethod
    def addEdge2(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code06_BeautifulTreeHLD1.indegree[v] = jcast('int', (Code06_BeautifulTreeHLD1.indegree[v] + 1))
        jset(Code06_BeautifulTreeHLD1.next2, ((_java_obj_4 := Code06_BeautifulTreeHLD1), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code06_BeautifulTreeHLD1.head2[u])
        Code06_BeautifulTreeHLD1.to2[Code06_BeautifulTreeHLD1.cnt2] = jcast('int', v)
        Code06_BeautifulTreeHLD1.head2[u] = jcast('int', Code06_BeautifulTreeHLD1.cnt2)

    @staticmethod
    def buildOut(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = 0
        if (l == r):
            rt = jcast('int', l)
        else:
            rt = jcast('int', ((_java_obj_7 := Code06_BeautifulTreeHLD1), (_java_key_8 := 'cntt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code06_BeautifulTreeHLD1.ls, rt, Code06_BeautifulTreeHLD1.buildOut(l, mid))
            jset(Code06_BeautifulTreeHLD1.rs, rt, Code06_BeautifulTreeHLD1.buildOut(jcast('int', jadd(mid, 1)), r))
            Code06_BeautifulTreeHLD1.addEdge2(Code06_BeautifulTreeHLD1.ls[rt], rt)
            Code06_BeautifulTreeHLD1.addEdge2(Code06_BeautifulTreeHLD1.rs[rt], rt)
        return jcast('int', rt)

    @staticmethod
    def buildIn(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = 0
        if (l == r):
            rt = jcast('int', l)
        else:
            rt = jcast('int', ((_java_obj_10 := Code06_BeautifulTreeHLD1), (_java_key_11 := 'cntt'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code06_BeautifulTreeHLD1.ls, rt, Code06_BeautifulTreeHLD1.buildIn(l, mid))
            jset(Code06_BeautifulTreeHLD1.rs, rt, Code06_BeautifulTreeHLD1.buildIn(jcast('int', jadd(mid, 1)), r))
            Code06_BeautifulTreeHLD1.addEdge2(rt, Code06_BeautifulTreeHLD1.ls[rt])
            Code06_BeautifulTreeHLD1.addEdge2(rt, Code06_BeautifulTreeHLD1.rs[rt])
        return jcast('int', rt)

    @staticmethod
    def xToRange(jobx, jobl, jobr, l, r, i):
        jobx = jcast('int', jobx)
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (jobl > jobr):
            return
        if ((jobl <= l) and (r <= jobr)):
            Code06_BeautifulTreeHLD1.addEdge2(jobx, i)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code06_BeautifulTreeHLD1.xToRange(jobx, jobl, jobr, l, mid, Code06_BeautifulTreeHLD1.ls[i])
            if (jobr > mid):
                Code06_BeautifulTreeHLD1.xToRange(jobx, jobl, jobr, jcast('int', jadd(mid, 1)), r, Code06_BeautifulTreeHLD1.rs[i])

    @staticmethod
    def rangeToX(jobl, jobr, jobx, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobx = jcast('int', jobx)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (jobl > jobr):
            return
        if ((jobl <= l) and (r <= jobr)):
            Code06_BeautifulTreeHLD1.addEdge2(i, jobx)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code06_BeautifulTreeHLD1.rangeToX(jobl, jobr, jobx, l, mid, Code06_BeautifulTreeHLD1.ls[i])
            if (jobr > mid):
                Code06_BeautifulTreeHLD1.rangeToX(jobl, jobr, jobx, jcast('int', jadd(mid, 1)), r, Code06_BeautifulTreeHLD1.rs[i])

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code06_BeautifulTreeHLD1.fa[u] = jcast('int', f)
        Code06_BeautifulTreeHLD1.dep[u] = jcast('int', jcast('int', jadd(Code06_BeautifulTreeHLD1.dep[f], 1)))
        Code06_BeautifulTreeHLD1.siz[u] = jcast('int', 1)
        e = jcast('int', Code06_BeautifulTreeHLD1.head1[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code06_BeautifulTreeHLD1.to1[e])
            if (v != f):
                Code06_BeautifulTreeHLD1.dfs1(v, u)
                Code06_BeautifulTreeHLD1.siz[u] = jcast('int', jcast('int', jadd(Code06_BeautifulTreeHLD1.siz[u], Code06_BeautifulTreeHLD1.siz[v])))
                if ((Code06_BeautifulTreeHLD1.son[u] == 0) or (Code06_BeautifulTreeHLD1.siz[Code06_BeautifulTreeHLD1.son[u]] < Code06_BeautifulTreeHLD1.siz[v])):
                    Code06_BeautifulTreeHLD1.son[u] = jcast('int', v)
            e = jcast('int', Code06_BeautifulTreeHLD1.next1[e])

    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code06_BeautifulTreeHLD1.top[u] = jcast('int', t)
        jset(Code06_BeautifulTreeHLD1.dfn, u, ((_java_obj_13 := Code06_BeautifulTreeHLD1), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
        Code06_BeautifulTreeHLD1.seg[Code06_BeautifulTreeHLD1.cntd] = jcast('int', u)
        if (Code06_BeautifulTreeHLD1.son[u] == 0):
            return
        Code06_BeautifulTreeHLD1.dfs2(Code06_BeautifulTreeHLD1.son[u], t)
        e = jcast('int', Code06_BeautifulTreeHLD1.head1[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code06_BeautifulTreeHLD1.to1[e])
            if ((v != Code06_BeautifulTreeHLD1.fa[u]) and (v != Code06_BeautifulTreeHLD1.son[u])):
                Code06_BeautifulTreeHLD1.dfs2(v, v)
            e = jcast('int', Code06_BeautifulTreeHLD1.next1[e])

    @staticmethod
    def pathSet(op, x, y, z):
        op = jcast('int', op)
        x = jcast('int', x)
        y = jcast('int', y)
        z = jcast('int', z)
        if (op == 1):
            if ((x <= z) and (z <= y)):
                Code06_BeautifulTreeHLD1.xToRange(z, x, jcast('int', (z - 1)), 1, Code06_BeautifulTreeHLD1.n, Code06_BeautifulTreeHLD1.rootIn)
                Code06_BeautifulTreeHLD1.xToRange(z, jcast('int', jadd(z, 1)), y, 1, Code06_BeautifulTreeHLD1.n, Code06_BeautifulTreeHLD1.rootIn)
            else:
                Code06_BeautifulTreeHLD1.xToRange(z, x, y, 1, Code06_BeautifulTreeHLD1.n, Code06_BeautifulTreeHLD1.rootIn)
        else:
            if ((x <= z) and (z <= y)):
                Code06_BeautifulTreeHLD1.rangeToX(x, jcast('int', (z - 1)), z, 1, Code06_BeautifulTreeHLD1.n, Code06_BeautifulTreeHLD1.rootOut)
                Code06_BeautifulTreeHLD1.rangeToX(jcast('int', jadd(z, 1)), y, z, 1, Code06_BeautifulTreeHLD1.n, Code06_BeautifulTreeHLD1.rootOut)
            else:
                Code06_BeautifulTreeHLD1.rangeToX(x, y, z, 1, Code06_BeautifulTreeHLD1.n, Code06_BeautifulTreeHLD1.rootOut)

    @staticmethod
    def link(op, a, b, c):
        op = jcast('int', op)
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        while (Code06_BeautifulTreeHLD1.top[a] != Code06_BeautifulTreeHLD1.top[b]):
            if (Code06_BeautifulTreeHLD1.dep[Code06_BeautifulTreeHLD1.top[a]] < Code06_BeautifulTreeHLD1.dep[Code06_BeautifulTreeHLD1.top[b]]):
                tmp = jcast('int', a)
                a = jcast('int', b)
                b = jcast('int', tmp)
            Code06_BeautifulTreeHLD1.pathSet(op, Code06_BeautifulTreeHLD1.dfn[Code06_BeautifulTreeHLD1.top[a]], Code06_BeautifulTreeHLD1.dfn[a], Code06_BeautifulTreeHLD1.dfn[c])
            a = jcast('int', Code06_BeautifulTreeHLD1.fa[Code06_BeautifulTreeHLD1.top[a]])
        Code06_BeautifulTreeHLD1.pathSet(op, jstatic('Math', 'min', Code06_BeautifulTreeHLD1.dfn[a], Code06_BeautifulTreeHLD1.dfn[b]), jstatic('Math', 'max', Code06_BeautifulTreeHLD1.dfn[a], Code06_BeautifulTreeHLD1.dfn[b]), Code06_BeautifulTreeHLD1.dfn[c])

    @staticmethod
    def topo():
        qi = jcast('int', 1)
        qsiz = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code06_BeautifulTreeHLD1.cntt):
            if (Code06_BeautifulTreeHLD1.indegree[i] == 0):
                jset(Code06_BeautifulTreeHLD1.que, (qsiz := jcast('int', (qsiz + (1)))), i)
            i = jcast('int', (i + 1))
        val = jcast('int', 0)
        while (qi <= qsiz):
            u = jcast('int', Code06_BeautifulTreeHLD1.que[((_java_old_16 := qi), (qi := jcast('int', (qi + (1)))), _java_old_16)[2]])
            if (u <= Code06_BeautifulTreeHLD1.n):
                jset(Code06_BeautifulTreeHLD1.ans, Code06_BeautifulTreeHLD1.seg[u], (val := jcast('int', (val + (1)))))
            e = jcast('int', Code06_BeautifulTreeHLD1.head2[u])
            while (e > 0):
                v = jcast('int', Code06_BeautifulTreeHLD1.to2[e])
                if (((_java_obj_17 := Code06_BeautifulTreeHLD1.indegree), (_java_key_18 := v), (_java_old_19 := jget(_java_obj_17, _java_key_18)), jset(_java_obj_17, _java_key_18, jcast('int', (_java_old_19 + (-1)))))[3] == 0):
                    jset(Code06_BeautifulTreeHLD1.que, (qsiz := jcast('int', (qsiz + (1)))), v)
                e = jcast('int', Code06_BeautifulTreeHLD1.next2[e])
        return jcast('boolean', (qsiz == Code06_BeautifulTreeHLD1.cntt))

    @staticmethod
    def main(args):
        in_ = Code06_BeautifulTreeHLD1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_BeautifulTreeHLD1.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_BeautifulTreeHLD1.m = jcast('int', jcall(in_, 'nextInt'))
        Code06_BeautifulTreeHLD1.cntt = jcast('int', Code06_BeautifulTreeHLD1.n)
        Code06_BeautifulTreeHLD1.rootOut = jcast('int', Code06_BeautifulTreeHLD1.buildOut(1, Code06_BeautifulTreeHLD1.n))
        Code06_BeautifulTreeHLD1.rootIn = jcast('int', Code06_BeautifulTreeHLD1.buildIn(1, Code06_BeautifulTreeHLD1.n))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code06_BeautifulTreeHLD1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code06_BeautifulTreeHLD1.addEdge1(u, v)
            Code06_BeautifulTreeHLD1.addEdge1(v, u)
            i = jcast('int', (i + 1))
        Code06_BeautifulTreeHLD1.dfs1(1, 0)
        Code06_BeautifulTreeHLD1.dfs2(1, 1)
        i = jcast('int', 1)
        op = 0
        a = 0
        b = 0
        c = 0
        while (i <= Code06_BeautifulTreeHLD1.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            a = jcast('int', jcall(in_, 'nextInt'))
            b = jcast('int', jcall(in_, 'nextInt'))
            c = jcast('int', jcall(in_, 'nextInt'))
            Code06_BeautifulTreeHLD1.link(op, a, b, c)
            i = jcast('int', (i + 1))
        check = jcast('boolean', Code06_BeautifulTreeHLD1.topo())
        if check:
            i = jcast('int', 1)
            while (i <= Code06_BeautifulTreeHLD1.n):
                jcall(out, 'print', Code06_BeautifulTreeHLD1.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_20 := self), (_java_key_21 := 'ptr'), (_java_old_22 := jget(_java_obj_20, _java_key_21)), jset(_java_obj_20, _java_key_21, jcast('int', (_java_old_22 + (1)))), _java_old_22)[4]])

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
            raise TypeError("No matching overload for Code06_BeautifulTreeHLD1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_BeautifulTreeHLD1.MAXN = jcast('int', 200001)
Code06_BeautifulTreeHLD1.MAXT = jcast('int', jcast('int', (Code06_BeautifulTreeHLD1.MAXN * 10)))
Code06_BeautifulTreeHLD1.MAXE = jcast('int', jcast('int', (Code06_BeautifulTreeHLD1.MAXN * 50)))
Code06_BeautifulTreeHLD1.n = jcast('int', 0)
Code06_BeautifulTreeHLD1.m = jcast('int', 0)
Code06_BeautifulTreeHLD1.head1 = jarray('int', [Code06_BeautifulTreeHLD1.MAXN])
Code06_BeautifulTreeHLD1.next1 = jarray('int', [jcast('int', (Code06_BeautifulTreeHLD1.MAXN << (1 & 31)))])
Code06_BeautifulTreeHLD1.to1 = jarray('int', [jcast('int', (Code06_BeautifulTreeHLD1.MAXN << (1 & 31)))])
Code06_BeautifulTreeHLD1.cnt1 = jcast('int', 0)
Code06_BeautifulTreeHLD1.indegree = jarray('int', [Code06_BeautifulTreeHLD1.MAXT])
Code06_BeautifulTreeHLD1.head2 = jarray('int', [Code06_BeautifulTreeHLD1.MAXT])
Code06_BeautifulTreeHLD1.next2 = jarray('int', [Code06_BeautifulTreeHLD1.MAXE])
Code06_BeautifulTreeHLD1.to2 = jarray('int', [Code06_BeautifulTreeHLD1.MAXE])
Code06_BeautifulTreeHLD1.cnt2 = jcast('int', 0)
Code06_BeautifulTreeHLD1.ls = jarray('int', [Code06_BeautifulTreeHLD1.MAXT])
Code06_BeautifulTreeHLD1.rs = jarray('int', [Code06_BeautifulTreeHLD1.MAXT])
Code06_BeautifulTreeHLD1.rootOut = jcast('int', 0)
Code06_BeautifulTreeHLD1.rootIn = jcast('int', 0)
Code06_BeautifulTreeHLD1.cntt = jcast('int', 0)
Code06_BeautifulTreeHLD1.fa = jarray('int', [Code06_BeautifulTreeHLD1.MAXN])
Code06_BeautifulTreeHLD1.dep = jarray('int', [Code06_BeautifulTreeHLD1.MAXN])
Code06_BeautifulTreeHLD1.siz = jarray('int', [Code06_BeautifulTreeHLD1.MAXN])
Code06_BeautifulTreeHLD1.son = jarray('int', [Code06_BeautifulTreeHLD1.MAXN])
Code06_BeautifulTreeHLD1.top = jarray('int', [Code06_BeautifulTreeHLD1.MAXN])
Code06_BeautifulTreeHLD1.dfn = jarray('int', [Code06_BeautifulTreeHLD1.MAXN])
Code06_BeautifulTreeHLD1.seg = jarray('int', [Code06_BeautifulTreeHLD1.MAXN])
Code06_BeautifulTreeHLD1.cntd = jcast('int', 0)
Code06_BeautifulTreeHLD1.que = jarray('int', [Code06_BeautifulTreeHLD1.MAXT])
Code06_BeautifulTreeHLD1.ans = jarray('int', [Code06_BeautifulTreeHLD1.MAXN])

if __name__ == '__main__':
    Code06_BeautifulTreeHLD1.main([])
