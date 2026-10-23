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

# 国土规划，Python版
# 一张无向图有n个点、m条边，所有点连通，可能有重边，但是无自环
# 初始时所有点的状态都是0，一共q次操作，每次操作只有一个参数x，含义如下
# 点x的状态翻转，0变1，1变0，然后考虑如下问题
# 如果某个状态为0的点删除后，所有状态为1的点依然连通，这样的点叫无所谓点
# 每次操作后都打印无所谓点的数量
# 2 <= n <= 10^5
# 1 <= m、q <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P10517
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code10_LandPlanning2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'q': 'q', 'cntn': 'cntn', 'arr': 'arr', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'cnt2': 'cnt2', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'dist': 'dist', 'dep': 'dep', 'stjump': 'stjump', 'nid': 'nid', 'seg': 'seg', 'cnti': 'cnti', 'set': 'set', 'sumDist': 'sumDist', 'stack': 'stack', 'u': 'u', 'status': 'status', 'fa': 'fa', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    MAXP = 0
    n = 0
    m = 0
    q = 0
    cntn = 0
    arr = None
    head1 = None
    next1 = None
    to1 = None
    cnt1 = 0
    head2 = None
    next2 = None
    to2 = None
    cnt2 = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    # nid是圆方树的点获得的dfn序号
    # seg是dfn序号对应的圆方树节点编号
    # cnti是圆方树的dfn序号计数
    dist = None
    dep = None
    stjump = None
    nid = None
    seg = None
    cnti = 0
    set = None
    sumDist = 0
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stack = None
    u = 0
    status = 0
    fa = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, status, fa, e):
        u = jcast('int', u)
        status = jcast('int', status)
        fa = jcast('int', fa)
        e = jcast('int', e)
        jset(Code10_LandPlanning2.stack[Code10_LandPlanning2.stacksize], 0, u)
        jset(Code10_LandPlanning2.stack[Code10_LandPlanning2.stacksize], 1, status)
        jset(Code10_LandPlanning2.stack[Code10_LandPlanning2.stacksize], 2, fa)
        jset(Code10_LandPlanning2.stack[Code10_LandPlanning2.stacksize], 3, e)
        Code10_LandPlanning2.stacksize = jcast('int', (Code10_LandPlanning2.stacksize + 1))

    @staticmethod
    def pop():
        Code10_LandPlanning2.stacksize = jcast('int', (Code10_LandPlanning2.stacksize - 1))
        Code10_LandPlanning2.u = jcast('int', Code10_LandPlanning2.stack[Code10_LandPlanning2.stacksize][0])
        Code10_LandPlanning2.status = jcast('int', Code10_LandPlanning2.stack[Code10_LandPlanning2.stacksize][1])
        Code10_LandPlanning2.fa = jcast('int', Code10_LandPlanning2.stack[Code10_LandPlanning2.stacksize][2])
        Code10_LandPlanning2.e = jcast('int', Code10_LandPlanning2.stack[Code10_LandPlanning2.stacksize][3])

    @staticmethod
    def addEdge1(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code10_LandPlanning2.next1, ((_java_obj_1 := Code10_LandPlanning2), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code10_LandPlanning2.head1[u])
        Code10_LandPlanning2.to1[Code10_LandPlanning2.cnt1] = jcast('int', v)
        Code10_LandPlanning2.head1[u] = jcast('int', Code10_LandPlanning2.cnt1)

    @staticmethod
    def addEdge2(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code10_LandPlanning2.next2, ((_java_obj_4 := Code10_LandPlanning2), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code10_LandPlanning2.head2[u])
        Code10_LandPlanning2.to2[Code10_LandPlanning2.cnt2] = jcast('int', v)
        Code10_LandPlanning2.head2[u] = jcast('int', Code10_LandPlanning2.cnt2)

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code10_LandPlanning2.dfn, u, jset(Code10_LandPlanning2.low, u, ((_java_obj_7 := Code10_LandPlanning2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
        jset(Code10_LandPlanning2.sta, ((_java_obj_10 := Code10_LandPlanning2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
        e = jcast('int', Code10_LandPlanning2.head1[u])
        while (e > 0):
            v = jcast('int', Code10_LandPlanning2.to1[e])
            if (Code10_LandPlanning2.dfn[v] == 0):
                Code10_LandPlanning2.tarjan1(v)
                jset(Code10_LandPlanning2.low, u, jstatic('Math', 'min', Code10_LandPlanning2.low[u], Code10_LandPlanning2.low[v]))
                if (Code10_LandPlanning2.low[v] >= Code10_LandPlanning2.dfn[u]):
                    Code10_LandPlanning2.cntn = jcast('int', (Code10_LandPlanning2.cntn + 1))
                    Code10_LandPlanning2.addEdge2(Code10_LandPlanning2.cntn, u)
                    Code10_LandPlanning2.addEdge2(u, Code10_LandPlanning2.cntn)
                    pop = 0
                    while True:
                        pop = jcast('int', Code10_LandPlanning2.sta[((_java_obj_13 := Code10_LandPlanning2), (_java_key_14 := 'top'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]])
                        Code10_LandPlanning2.addEdge2(Code10_LandPlanning2.cntn, pop)
                        Code10_LandPlanning2.addEdge2(pop, Code10_LandPlanning2.cntn)
                        if not ((pop != v)):
                            break
            else:
                jset(Code10_LandPlanning2.low, u, jstatic('Math', 'min', Code10_LandPlanning2.low[u], Code10_LandPlanning2.dfn[v]))
            e = jcast('int', Code10_LandPlanning2.next1[e])

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code10_LandPlanning2.stacksize = jcast('int', 0)
        Code10_LandPlanning2.push(node, jcast('int', (-1)), 0, jcast('int', (-1)))
        v = 0
        while (Code10_LandPlanning2.stacksize > 0):
            Code10_LandPlanning2.pop()
            if (Code10_LandPlanning2.status == jcast('int', (-1))):
                jset(Code10_LandPlanning2.dfn, Code10_LandPlanning2.u, jset(Code10_LandPlanning2.low, Code10_LandPlanning2.u, ((_java_obj_16 := Code10_LandPlanning2), (_java_key_17 := 'cntd'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3]))
                jset(Code10_LandPlanning2.sta, ((_java_obj_19 := Code10_LandPlanning2), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], Code10_LandPlanning2.u)
                Code10_LandPlanning2.e = jcast('int', Code10_LandPlanning2.head1[Code10_LandPlanning2.u])
            else:
                v = jcast('int', Code10_LandPlanning2.to1[Code10_LandPlanning2.e])
                if (Code10_LandPlanning2.status == 0):
                    jset(Code10_LandPlanning2.low, Code10_LandPlanning2.u, jstatic('Math', 'min', Code10_LandPlanning2.low[Code10_LandPlanning2.u], Code10_LandPlanning2.low[v]))
                    if (Code10_LandPlanning2.low[v] >= Code10_LandPlanning2.dfn[Code10_LandPlanning2.u]):
                        Code10_LandPlanning2.cntn = jcast('int', (Code10_LandPlanning2.cntn + 1))
                        Code10_LandPlanning2.addEdge2(Code10_LandPlanning2.cntn, Code10_LandPlanning2.u)
                        Code10_LandPlanning2.addEdge2(Code10_LandPlanning2.u, Code10_LandPlanning2.cntn)
                        pop = 0
                        while True:
                            pop = jcast('int', Code10_LandPlanning2.sta[((_java_obj_22 := Code10_LandPlanning2), (_java_key_23 := 'top'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (-1)))), _java_old_24)[4]])
                            Code10_LandPlanning2.addEdge2(Code10_LandPlanning2.cntn, pop)
                            Code10_LandPlanning2.addEdge2(pop, Code10_LandPlanning2.cntn)
                            if not ((pop != v)):
                                break
                else:
                    jset(Code10_LandPlanning2.low, Code10_LandPlanning2.u, jstatic('Math', 'min', Code10_LandPlanning2.low[Code10_LandPlanning2.u], Code10_LandPlanning2.dfn[v]))
                Code10_LandPlanning2.e = jcast('int', Code10_LandPlanning2.next1[Code10_LandPlanning2.e])
            if (Code10_LandPlanning2.e != 0):
                v = jcast('int', Code10_LandPlanning2.to1[Code10_LandPlanning2.e])
                if (Code10_LandPlanning2.dfn[v] == 0):
                    Code10_LandPlanning2.push(Code10_LandPlanning2.u, 0, 0, Code10_LandPlanning2.e)
                    Code10_LandPlanning2.push(v, jcast('int', (-1)), 0, jcast('int', (-1)))
                else:
                    Code10_LandPlanning2.push(Code10_LandPlanning2.u, 1, 0, Code10_LandPlanning2.e)

    # 递归版
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code10_LandPlanning2.nid, u, ((_java_obj_25 := Code10_LandPlanning2), (_java_key_26 := 'cnti'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3])
        Code10_LandPlanning2.seg[Code10_LandPlanning2.cnti] = jcast('int', u)
        Code10_LandPlanning2.dist[u] = jcast('int', jcast('int', jadd(Code10_LandPlanning2.dist[fa], (1 if (u <= Code10_LandPlanning2.n) else 0))))
        Code10_LandPlanning2.dep[u] = jcast('int', jcast('int', jadd(Code10_LandPlanning2.dep[fa], 1)))
        jset(Code10_LandPlanning2.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code10_LandPlanning2.MAXP):
            jset(Code10_LandPlanning2.stjump[u], p, Code10_LandPlanning2.stjump[Code10_LandPlanning2.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code10_LandPlanning2.head2[u])
        while (e > 0):
            v = jcast('int', Code10_LandPlanning2.to2[e])
            if (v != fa):
                Code10_LandPlanning2.dfs1(v, u)
            e = jcast('int', Code10_LandPlanning2.next2[e])

    # 迭代版
    @staticmethod
    def dfs2(cur, father):
        cur = jcast('int', cur)
        father = jcast('int', father)
        Code10_LandPlanning2.stacksize = jcast('int', 0)
        Code10_LandPlanning2.push(cur, 0, father, jcast('int', (-1)))
        while (Code10_LandPlanning2.stacksize > 0):
            Code10_LandPlanning2.pop()
            if (Code10_LandPlanning2.e == jcast('int', (-1))):
                jset(Code10_LandPlanning2.nid, Code10_LandPlanning2.u, ((_java_obj_28 := Code10_LandPlanning2), (_java_key_29 := 'cnti'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))))[3])
                Code10_LandPlanning2.seg[Code10_LandPlanning2.cnti] = jcast('int', Code10_LandPlanning2.u)
                Code10_LandPlanning2.dist[Code10_LandPlanning2.u] = jcast('int', jcast('int', jadd(Code10_LandPlanning2.dist[Code10_LandPlanning2.fa], (1 if (Code10_LandPlanning2.u <= Code10_LandPlanning2.n) else 0))))
                Code10_LandPlanning2.dep[Code10_LandPlanning2.u] = jcast('int', jcast('int', jadd(Code10_LandPlanning2.dep[Code10_LandPlanning2.fa], 1)))
                jset(Code10_LandPlanning2.stjump[Code10_LandPlanning2.u], 0, Code10_LandPlanning2.fa)
                p = jcast('int', 1)
                while (p < Code10_LandPlanning2.MAXP):
                    jset(Code10_LandPlanning2.stjump[Code10_LandPlanning2.u], p, Code10_LandPlanning2.stjump[Code10_LandPlanning2.stjump[Code10_LandPlanning2.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code10_LandPlanning2.e = jcast('int', Code10_LandPlanning2.head2[Code10_LandPlanning2.u])
            else:
                Code10_LandPlanning2.e = jcast('int', Code10_LandPlanning2.next2[Code10_LandPlanning2.e])
            if (Code10_LandPlanning2.e != 0):
                Code10_LandPlanning2.push(Code10_LandPlanning2.u, 0, Code10_LandPlanning2.fa, Code10_LandPlanning2.e)
                if (Code10_LandPlanning2.to2[Code10_LandPlanning2.e] != Code10_LandPlanning2.fa):
                    Code10_LandPlanning2.push(Code10_LandPlanning2.to2[Code10_LandPlanning2.e], 0, Code10_LandPlanning2.u, jcast('int', (-1)))

    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code10_LandPlanning2.dep[a] < Code10_LandPlanning2.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code10_LandPlanning2.MAXP - 1)))
        while (p >= 0):
            if (Code10_LandPlanning2.dep[Code10_LandPlanning2.stjump[a][p]] >= Code10_LandPlanning2.dep[b]):
                a = jcast('int', Code10_LandPlanning2.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code10_LandPlanning2.MAXP - 1)))
        while (p >= 0):
            if (Code10_LandPlanning2.stjump[a][p] != Code10_LandPlanning2.stjump[b][p]):
                a = jcast('int', Code10_LandPlanning2.stjump[a][p])
                b = jcast('int', Code10_LandPlanning2.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code10_LandPlanning2.stjump[a][0])

    @staticmethod
    def getDist(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('int', jcast('int', (jcast('int', jadd(Code10_LandPlanning2.dist[x], Code10_LandPlanning2.dist[y])) - jcast('int', (2 * Code10_LandPlanning2.dist[Code10_LandPlanning2.getLca(x, y)])))))

    @staticmethod
    def compute(u):
        u = jcast('int', u)
        id = jcast('int', Code10_LandPlanning2.nid[u])
        if (not Code10_LandPlanning2.arr[u]):
            Code10_LandPlanning2.arr[u] = jcast('boolean', True)
            jcall(Code10_LandPlanning2.set, 'add', id)
        else:
            Code10_LandPlanning2.arr[u] = jcast('boolean', False)
            jcall(Code10_LandPlanning2.set, 'remove', id)
        if (jcall(Code10_LandPlanning2.set, 'size') <= 1):
            Code10_LandPlanning2.sumDist = jcast('int', 0)
        else:
            low = jcast('int', Code10_LandPlanning2.seg[(jcall(Code10_LandPlanning2.set, 'lower', id) if (jcall(Code10_LandPlanning2.set, 'lower', id) != None) else jcall(Code10_LandPlanning2.set, 'last'))])
            high = jcast('int', Code10_LandPlanning2.seg[(jcall(Code10_LandPlanning2.set, 'higher', id) if (jcall(Code10_LandPlanning2.set, 'higher', id) != None) else jcall(Code10_LandPlanning2.set, 'first'))])
            delta = jcast('int', jcast('int', (jcast('int', jadd(Code10_LandPlanning2.getDist(u, low), Code10_LandPlanning2.getDist(u, high))) - Code10_LandPlanning2.getDist(low, high))))
            if Code10_LandPlanning2.arr[u]:
                Code10_LandPlanning2.sumDist = jcast('int', jcast('int', jadd(Code10_LandPlanning2.sumDist, delta)))
            else:
                Code10_LandPlanning2.sumDist = jcast('int', jcast('int', (Code10_LandPlanning2.sumDist - delta)))
        if jcall(Code10_LandPlanning2.set, 'isEmpty'):
            return jcast('int', 0)
        extra = jcast('int', (1 if (Code10_LandPlanning2.getLca(Code10_LandPlanning2.seg[jcall(Code10_LandPlanning2.set, 'first')], Code10_LandPlanning2.seg[jcall(Code10_LandPlanning2.set, 'last')]) <= Code10_LandPlanning2.n) else 0))
        return jcast('int', jcast('int', jcast('int', jadd(jcast('int', jdiv(Code10_LandPlanning2.sumDist, 2)), extra))))

    @staticmethod
    def main(args):
        in_ = Code10_LandPlanning2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code10_LandPlanning2.n = jcast('int', jcall(in_, 'nextInt'))
        Code10_LandPlanning2.m = jcast('int', jcall(in_, 'nextInt'))
        Code10_LandPlanning2.q = jcast('int', jcall(in_, 'nextInt'))
        Code10_LandPlanning2.cntn = jcast('int', Code10_LandPlanning2.n)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code10_LandPlanning2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code10_LandPlanning2.addEdge1(u, v)
            Code10_LandPlanning2.addEdge1(v, u)
            i = jcast('int', (i + 1))
        # tarjan1(1);
        Code10_LandPlanning2.tarjan2(1)
        # dfs1(1, 0);
        Code10_LandPlanning2.dfs2(1, 0)
        i = jcast('int', 1)
        x = 0
        while (i <= Code10_LandPlanning2.q):
            x = jcast('int', jcall(in_, 'nextInt'))
            ans = jcast('int', jcast('int', (Code10_LandPlanning2.n - Code10_LandPlanning2.compute(x))))
            jcall(out, 'println', ans)
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
            return jcast('int', self.buffer[((_java_obj_31 := self), (_java_key_32 := 'ptr'), (_java_old_33 := jget(_java_obj_31, _java_key_32)), jset(_java_obj_31, _java_key_32, jcast('int', (_java_old_33 + (1)))), _java_old_33)[4]])

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
            raise TypeError("No matching overload for Code10_LandPlanning2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code10_LandPlanning2.MAXN = jcast('int', 100001)
Code10_LandPlanning2.MAXM = jcast('int', 200001)
Code10_LandPlanning2.MAXP = jcast('int', 20)
Code10_LandPlanning2.n = jcast('int', 0)
Code10_LandPlanning2.m = jcast('int', 0)
Code10_LandPlanning2.q = jcast('int', 0)
Code10_LandPlanning2.cntn = jcast('int', 0)
Code10_LandPlanning2.arr = jarray('boolean', [Code10_LandPlanning2.MAXN])
Code10_LandPlanning2.head1 = jarray('int', [Code10_LandPlanning2.MAXN])
Code10_LandPlanning2.next1 = jarray('int', [jcast('int', (Code10_LandPlanning2.MAXM << (1 & 31)))])
Code10_LandPlanning2.to1 = jarray('int', [jcast('int', (Code10_LandPlanning2.MAXM << (1 & 31)))])
Code10_LandPlanning2.cnt1 = jcast('int', 0)
Code10_LandPlanning2.head2 = jarray('int', [jcast('int', (Code10_LandPlanning2.MAXN << (1 & 31)))])
Code10_LandPlanning2.next2 = jarray('int', [jcast('int', (Code10_LandPlanning2.MAXM << (2 & 31)))])
Code10_LandPlanning2.to2 = jarray('int', [jcast('int', (Code10_LandPlanning2.MAXM << (2 & 31)))])
Code10_LandPlanning2.cnt2 = jcast('int', 0)
Code10_LandPlanning2.dfn = jarray('int', [Code10_LandPlanning2.MAXN])
Code10_LandPlanning2.low = jarray('int', [Code10_LandPlanning2.MAXN])
Code10_LandPlanning2.cntd = jcast('int', 0)
Code10_LandPlanning2.sta = jarray('int', [Code10_LandPlanning2.MAXN])
Code10_LandPlanning2.top = jcast('int', 0)
Code10_LandPlanning2.dist = jarray('int', [jcast('int', (Code10_LandPlanning2.MAXN << (1 & 31)))])
Code10_LandPlanning2.dep = jarray('int', [jcast('int', (Code10_LandPlanning2.MAXN << (1 & 31)))])
Code10_LandPlanning2.stjump = jarray('int', [jcast('int', (Code10_LandPlanning2.MAXN << (1 & 31))), Code10_LandPlanning2.MAXP])
Code10_LandPlanning2.nid = jarray('int', [jcast('int', (Code10_LandPlanning2.MAXN << (1 & 31)))])
Code10_LandPlanning2.seg = jarray('int', [jcast('int', (Code10_LandPlanning2.MAXN << (1 & 31)))])
Code10_LandPlanning2.cnti = jcast('int', 0)
Code10_LandPlanning2.set = jnew('TreeSet')
Code10_LandPlanning2.sumDist = jcast('int', 0)
Code10_LandPlanning2.stack = jarray('int', [jcast('int', (Code10_LandPlanning2.MAXN << (1 & 31))), 4])
Code10_LandPlanning2.u = jcast('int', 0)
Code10_LandPlanning2.status = jcast('int', 0)
Code10_LandPlanning2.fa = jcast('int', 0)
Code10_LandPlanning2.e = jcast('int', 0)
Code10_LandPlanning2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code10_LandPlanning2.main([])
