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

# 监狱，Python版
# 一共有n个房间，给定n-1条无向边，所有房间组成一棵树
# 一共有m个囚犯，每个囚犯给出卧室房间号和工作室房间号，囚犯初始时都在卧室
# 每个囚犯的卧室和工作室一定不同，任何两个囚犯既不共用卧室，也不共用工作室
# 但是有可能某个房间，作为一个囚犯的卧室，同时作为另一个囚犯的工作室
# 你的任务是让所有囚犯从自己的卧室出发，只走最短路去自己的工作室
# 你可以随意下达指令，每条指令只能选择一个囚犯，沿一条边移动一步
# 任何时刻不能让任何房间里出现两个囚犯，打印你能否完成任务
# 1 <= n、m <= 1.2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P9520
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code09_Jail1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'MAXP': 'MAXP', 't': 't', 'n': 'n', 'm': 'm', 'startTag': 'startTag', 'endTag': 'endTag', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'cnt1': 'cnt1', 'indegree': 'indegree', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'cnt2': 'cnt2', 'dep': 'dep', 'dfn': 'dfn', 'siz': 'siz', 'stjump': 'stjump', 'cntd': 'cntd', 'stout': 'stout', 'stin': 'stin', 'cntt': 'cntt', 'que': 'que', 'ufe': 'ufe', 'stacksize': 'stacksize', 'u': 'u', 'fa': 'fa', 'e': 'e'}
    MAXN = 0
    MAXT = 0
    MAXE = 0
    MAXP = 0
    t = 0
    n = 0
    m = 0
    # 两个标签的编号
    startTag = None
    endTag = None
    # 原始的树
    head1 = None
    next1 = None
    to1 = None
    cnt1 = 0
    # 相对次序的关系图
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
    # 倍增优化建图
    stout = None
    stin = None
    cntt = 0
    # 拓扑排序判环
    que = None
    # 讲解118，递归改迭代需要的栈
    ufe = None
    stacksize = 0
    u = 0
    fa = 0
    e = 0
    @staticmethod
    def push(u, fa, e):
        u = jcast('int', u)
        fa = jcast('int', fa)
        e = jcast('int', e)
        jset(Code09_Jail1.ufe[Code09_Jail1.stacksize], 0, u)
        jset(Code09_Jail1.ufe[Code09_Jail1.stacksize], 1, fa)
        jset(Code09_Jail1.ufe[Code09_Jail1.stacksize], 2, e)
        Code09_Jail1.stacksize = jcast('int', (Code09_Jail1.stacksize + 1))

    @staticmethod
    def pop():
        Code09_Jail1.stacksize = jcast('int', (Code09_Jail1.stacksize - 1))
        Code09_Jail1.u = jcast('int', Code09_Jail1.ufe[Code09_Jail1.stacksize][0])
        Code09_Jail1.fa = jcast('int', Code09_Jail1.ufe[Code09_Jail1.stacksize][1])
        Code09_Jail1.e = jcast('int', Code09_Jail1.ufe[Code09_Jail1.stacksize][2])

    @staticmethod
    def addEdge1(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code09_Jail1.next1, ((_java_obj_1 := Code09_Jail1), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code09_Jail1.head1[u])
        Code09_Jail1.to1[Code09_Jail1.cnt1] = jcast('int', v)
        Code09_Jail1.head1[u] = jcast('int', Code09_Jail1.cnt1)

    @staticmethod
    def addEdge2(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code09_Jail1.indegree[v] = jcast('int', (Code09_Jail1.indegree[v] + 1))
        jset(Code09_Jail1.next2, ((_java_obj_4 := Code09_Jail1), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code09_Jail1.head2[u])
        Code09_Jail1.to2[Code09_Jail1.cnt2] = jcast('int', v)
        Code09_Jail1.head2[u] = jcast('int', Code09_Jail1.cnt2)

    # 递归版
    @staticmethod
    def build1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code09_Jail1.dep[u] = jcast('int', jcast('int', jadd(Code09_Jail1.dep[fa], 1)))
        jset(Code09_Jail1.dfn, u, ((_java_obj_7 := Code09_Jail1), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
        Code09_Jail1.siz[u] = jcast('int', 1)
        jset(Code09_Jail1.stjump[u], 0, fa)
        jset(Code09_Jail1.stout[u], 0, ((_java_obj_10 := Code09_Jail1), (_java_key_11 := 'cntt'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
        Code09_Jail1.addEdge2(Code09_Jail1.startTag[u], Code09_Jail1.cntt)
        Code09_Jail1.addEdge2(Code09_Jail1.startTag[fa], Code09_Jail1.cntt)
        jset(Code09_Jail1.stin[u], 0, ((_java_obj_13 := Code09_Jail1), (_java_key_14 := 'cntt'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
        Code09_Jail1.addEdge2(Code09_Jail1.cntt, Code09_Jail1.endTag[u])
        Code09_Jail1.addEdge2(Code09_Jail1.cntt, Code09_Jail1.endTag[fa])
        p = jcast('int', 1)
        while (p < Code09_Jail1.MAXP):
            jset(Code09_Jail1.stjump[u], p, Code09_Jail1.stjump[Code09_Jail1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            jset(Code09_Jail1.stout[u], p, ((_java_obj_16 := Code09_Jail1), (_java_key_17 := 'cntt'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3])
            Code09_Jail1.addEdge2(Code09_Jail1.stout[u][jcast('int', (p - 1))], Code09_Jail1.cntt)
            Code09_Jail1.addEdge2(Code09_Jail1.stout[Code09_Jail1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))], Code09_Jail1.cntt)
            jset(Code09_Jail1.stin[u], p, ((_java_obj_19 := Code09_Jail1), (_java_key_20 := 'cntt'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3])
            Code09_Jail1.addEdge2(Code09_Jail1.cntt, Code09_Jail1.stin[u][jcast('int', (p - 1))])
            Code09_Jail1.addEdge2(Code09_Jail1.cntt, Code09_Jail1.stin[Code09_Jail1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code09_Jail1.head1[u])
        while (e > 0):
            v = jcast('int', Code09_Jail1.to1[e])
            if (v != fa):
                Code09_Jail1.build1(v, u)
                Code09_Jail1.siz[u] = jcast('int', jcast('int', jadd(Code09_Jail1.siz[u], Code09_Jail1.siz[v])))
            e = jcast('int', Code09_Jail1.next1[e])

    # 迭代版
    @staticmethod
    def build2(cur, father):
        cur = jcast('int', cur)
        father = jcast('int', father)
        Code09_Jail1.stacksize = jcast('int', 0)
        Code09_Jail1.push(cur, father, jcast('int', (-1)))
        while (Code09_Jail1.stacksize > 0):
            Code09_Jail1.pop()
            if (Code09_Jail1.e == jcast('int', (-1))):
                Code09_Jail1.dep[Code09_Jail1.u] = jcast('int', jcast('int', jadd(Code09_Jail1.dep[Code09_Jail1.fa], 1)))
                jset(Code09_Jail1.dfn, Code09_Jail1.u, ((_java_obj_22 := Code09_Jail1), (_java_key_23 := 'cntd'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))))[3])
                Code09_Jail1.siz[Code09_Jail1.u] = jcast('int', 1)
                jset(Code09_Jail1.stjump[Code09_Jail1.u], 0, Code09_Jail1.fa)
                jset(Code09_Jail1.stout[Code09_Jail1.u], 0, ((_java_obj_25 := Code09_Jail1), (_java_key_26 := 'cntt'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3])
                Code09_Jail1.addEdge2(Code09_Jail1.startTag[Code09_Jail1.u], Code09_Jail1.cntt)
                Code09_Jail1.addEdge2(Code09_Jail1.startTag[Code09_Jail1.fa], Code09_Jail1.cntt)
                jset(Code09_Jail1.stin[Code09_Jail1.u], 0, ((_java_obj_28 := Code09_Jail1), (_java_key_29 := 'cntt'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))))[3])
                Code09_Jail1.addEdge2(Code09_Jail1.cntt, Code09_Jail1.endTag[Code09_Jail1.u])
                Code09_Jail1.addEdge2(Code09_Jail1.cntt, Code09_Jail1.endTag[Code09_Jail1.fa])
                p = jcast('int', 1)
                while (p < Code09_Jail1.MAXP):
                    jset(Code09_Jail1.stjump[Code09_Jail1.u], p, Code09_Jail1.stjump[Code09_Jail1.stjump[Code09_Jail1.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    jset(Code09_Jail1.stout[Code09_Jail1.u], p, ((_java_obj_31 := Code09_Jail1), (_java_key_32 := 'cntt'), (_java_old_33 := jget(_java_obj_31, _java_key_32)), jset(_java_obj_31, _java_key_32, jcast('int', (_java_old_33 + (1)))))[3])
                    Code09_Jail1.addEdge2(Code09_Jail1.stout[Code09_Jail1.u][jcast('int', (p - 1))], Code09_Jail1.cntt)
                    Code09_Jail1.addEdge2(Code09_Jail1.stout[Code09_Jail1.stjump[Code09_Jail1.u][jcast('int', (p - 1))]][jcast('int', (p - 1))], Code09_Jail1.cntt)
                    jset(Code09_Jail1.stin[Code09_Jail1.u], p, ((_java_obj_34 := Code09_Jail1), (_java_key_35 := 'cntt'), (_java_old_36 := jget(_java_obj_34, _java_key_35)), jset(_java_obj_34, _java_key_35, jcast('int', (_java_old_36 + (1)))))[3])
                    Code09_Jail1.addEdge2(Code09_Jail1.cntt, Code09_Jail1.stin[Code09_Jail1.u][jcast('int', (p - 1))])
                    Code09_Jail1.addEdge2(Code09_Jail1.cntt, Code09_Jail1.stin[Code09_Jail1.stjump[Code09_Jail1.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code09_Jail1.e = jcast('int', Code09_Jail1.head1[Code09_Jail1.u])
            else:
                Code09_Jail1.e = jcast('int', Code09_Jail1.next1[Code09_Jail1.e])
            if (Code09_Jail1.e != 0):
                Code09_Jail1.push(Code09_Jail1.u, Code09_Jail1.fa, Code09_Jail1.e)
                if (Code09_Jail1.to1[Code09_Jail1.e] != Code09_Jail1.fa):
                    Code09_Jail1.push(Code09_Jail1.to1[Code09_Jail1.e], Code09_Jail1.u, jcast('int', (-1)))
            else:
                ei = jcast('int', Code09_Jail1.head1[Code09_Jail1.u])
                while (ei > 0):
                    v = jcast('int', Code09_Jail1.to1[ei])
                    if (v != Code09_Jail1.fa):
                        Code09_Jail1.siz[Code09_Jail1.u] = jcast('int', jcast('int', jadd(Code09_Jail1.siz[Code09_Jail1.u], Code09_Jail1.siz[v])))
                    ei = jcast('int', Code09_Jail1.next1[ei])

    @staticmethod
    def isAncestor(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        return jcast('boolean', ((Code09_Jail1.dfn[a] <= Code09_Jail1.dfn[b]) and (Code09_Jail1.dfn[b] < jcast('int', jadd(Code09_Jail1.dfn[a], Code09_Jail1.siz[a])))))

    @staticmethod
    def kthAncestor(x, k):
        x = jcast('int', x)
        k = jcast('int', k)
        p = jcast('int', 0)
        while (p < Code09_Jail1.MAXP):
            if (jcast('int', (jcast('int', (k >> (p & 31))) & 1)) != 0):
                x = jcast('int', Code09_Jail1.stjump[x][p])
            p = jcast('int', (p + 1))
        return jcast('int', x)

    @staticmethod
    def nearest(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        if Code09_Jail1.isAncestor(y, x):
            return jcast('int', Code09_Jail1.kthAncestor(x, jcast('int', (jcast('int', (Code09_Jail1.dep[x] - Code09_Jail1.dep[y])) - 1))))
        else:
            return jcast('int', Code09_Jail1.stjump[y][0])

    @staticmethod
    def pathSet(x, y, prisoner):
        x = jcast('int', x)
        y = jcast('int', y)
        prisoner = jcast('int', prisoner)
        if (Code09_Jail1.dep[x] < Code09_Jail1.dep[y]):
            tmp = jcast('int', x)
            x = jcast('int', y)
            y = jcast('int', tmp)
        Code09_Jail1.addEdge2(Code09_Jail1.startTag[y], prisoner)
        Code09_Jail1.addEdge2(prisoner, Code09_Jail1.endTag[y])
        p = jcast('int', jcast('int', (Code09_Jail1.MAXP - 1)))
        while (p >= 0):
            if (Code09_Jail1.dep[Code09_Jail1.stjump[x][p]] >= Code09_Jail1.dep[y]):
                Code09_Jail1.addEdge2(Code09_Jail1.stout[x][p], prisoner)
                Code09_Jail1.addEdge2(prisoner, Code09_Jail1.stin[x][p])
                x = jcast('int', Code09_Jail1.stjump[x][p])
            p = jcast('int', (p - 1))
        if (x == y):
            return
        p = jcast('int', jcast('int', (Code09_Jail1.MAXP - 1)))
        while (p >= 0):
            if (Code09_Jail1.stjump[x][p] != Code09_Jail1.stjump[y][p]):
                Code09_Jail1.addEdge2(Code09_Jail1.stout[x][p], prisoner)
                Code09_Jail1.addEdge2(Code09_Jail1.stout[y][p], prisoner)
                Code09_Jail1.addEdge2(prisoner, Code09_Jail1.stin[x][p])
                Code09_Jail1.addEdge2(prisoner, Code09_Jail1.stin[y][p])
                x = jcast('int', Code09_Jail1.stjump[x][p])
                y = jcast('int', Code09_Jail1.stjump[y][p])
            p = jcast('int', (p - 1))
        Code09_Jail1.addEdge2(Code09_Jail1.stout[x][0], prisoner)
        Code09_Jail1.addEdge2(prisoner, Code09_Jail1.stin[x][0])

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        prisoner = jcast('int', ((_java_obj_37 := Code09_Jail1), (_java_key_38 := 'cntt'), (_java_old_39 := jget(_java_obj_37, _java_key_38)), jset(_java_obj_37, _java_key_38, jcast('int', (_java_old_39 + (1)))))[3])
        Code09_Jail1.addEdge2(prisoner, Code09_Jail1.startTag[x])
        Code09_Jail1.addEdge2(prisoner, Code09_Jail1.endTag[x])
        Code09_Jail1.addEdge2(Code09_Jail1.startTag[y], prisoner)
        Code09_Jail1.addEdge2(Code09_Jail1.endTag[y], prisoner)
        if ((Code09_Jail1.stjump[x][0] != y) and (Code09_Jail1.stjump[y][0] != x)):
            a = jcast('int', Code09_Jail1.nearest(y, x))
            b = jcast('int', Code09_Jail1.nearest(x, y))
            Code09_Jail1.pathSet(a, b, prisoner)

    @staticmethod
    def topo():
        qi = jcast('int', 1)
        qsiz = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code09_Jail1.cntt):
            if (Code09_Jail1.indegree[i] == 0):
                jset(Code09_Jail1.que, (qsiz := jcast('int', (qsiz + (1)))), i)
            i = jcast('int', (i + 1))
        while (qi <= qsiz):
            u = jcast('int', Code09_Jail1.que[((_java_old_40 := qi), (qi := jcast('int', (qi + (1)))), _java_old_40)[2]])
            e = jcast('int', Code09_Jail1.head2[u])
            while (e > 0):
                v = jcast('int', Code09_Jail1.to2[e])
                if (((_java_obj_41 := Code09_Jail1.indegree), (_java_key_42 := v), (_java_old_43 := jget(_java_obj_41, _java_key_42)), jset(_java_obj_41, _java_key_42, jcast('int', (_java_old_43 + (-1)))))[3] == 0):
                    jset(Code09_Jail1.que, (qsiz := jcast('int', (qsiz + (1)))), v)
                e = jcast('int', Code09_Jail1.next2[e])
        return jcast('boolean', (qsiz == Code09_Jail1.cntt))

    @staticmethod
    def clear():
        i = jcast('int', 1)
        while (i <= Code09_Jail1.n):
            Code09_Jail1.head1[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code09_Jail1.cntt):
            jset(Code09_Jail1.head2, i, jset(Code09_Jail1.indegree, i, 0))
            i = jcast('int', (i + 1))
        Code09_Jail1.cnt1 = jcast('int', jset(Code09_Jail1, 'cnt2', jset(Code09_Jail1, 'cntt', jset(Code09_Jail1, 'cntd', 0))))
        Code09_Jail1.dep[1] = jcast('int', 0)

    @staticmethod
    def main(args):
        in_ = Code09_Jail1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code09_Jail1.t = jcast('int', jcall(in_, 'nextInt'))
        c = jcast('int', 1)
        while (c <= Code09_Jail1.t):
            Code09_Jail1.n = jcast('int', jcall(in_, 'nextInt'))
            Code09_Jail1.cntt = jcast('int', jcast('int', (Code09_Jail1.n << (1 & 31))))
            i = jcast('int', 1)
            while (i <= Code09_Jail1.n):
                Code09_Jail1.startTag[i] = jcast('int', i)
                Code09_Jail1.endTag[i] = jcast('int', jcast('int', jadd(i, Code09_Jail1.n)))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            u = 0
            v = 0
            while (i < Code09_Jail1.n):
                u = jcast('int', jcall(in_, 'nextInt'))
                v = jcast('int', jcall(in_, 'nextInt'))
                Code09_Jail1.addEdge1(u, v)
                Code09_Jail1.addEdge1(v, u)
                i = jcast('int', (i + 1))
            # build1(1, 1);
            Code09_Jail1.build2(1, 1)
            Code09_Jail1.m = jcast('int', jcall(in_, 'nextInt'))
            i = jcast('int', 1)
            x = 0
            y = 0
            while (i <= Code09_Jail1.m):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                Code09_Jail1.link(x, y)
                i = jcast('int', (i + 1))
            ans = jcast('boolean', Code09_Jail1.topo())
            jcall(out, 'println', ('Yes' if ans else 'No'))
            Code09_Jail1.clear()
            c = jcast('int', (c + 1))
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
            return jcast('int', self.buffer[((_java_obj_44 := self), (_java_key_45 := 'ptr'), (_java_old_46 := jget(_java_obj_44, _java_key_45)), jset(_java_obj_44, _java_key_45, jcast('int', (_java_old_46 + (1)))), _java_old_46)[4]])

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
            raise TypeError("No matching overload for Code09_Jail1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code09_Jail1.MAXN = jcast('int', 120001)
Code09_Jail1.MAXT = jcast('int', jcast('int', (Code09_Jail1.MAXN * 50)))
Code09_Jail1.MAXE = jcast('int', jcast('int', (Code09_Jail1.MAXN * 200)))
Code09_Jail1.MAXP = jcast('int', 18)
Code09_Jail1.t = jcast('int', 0)
Code09_Jail1.n = jcast('int', 0)
Code09_Jail1.m = jcast('int', 0)
Code09_Jail1.startTag = jarray('int', [Code09_Jail1.MAXN])
Code09_Jail1.endTag = jarray('int', [Code09_Jail1.MAXN])
Code09_Jail1.head1 = jarray('int', [Code09_Jail1.MAXN])
Code09_Jail1.next1 = jarray('int', [jcast('int', (Code09_Jail1.MAXN << (1 & 31)))])
Code09_Jail1.to1 = jarray('int', [jcast('int', (Code09_Jail1.MAXN << (1 & 31)))])
Code09_Jail1.cnt1 = jcast('int', 0)
Code09_Jail1.indegree = jarray('int', [Code09_Jail1.MAXT])
Code09_Jail1.head2 = jarray('int', [Code09_Jail1.MAXT])
Code09_Jail1.next2 = jarray('int', [Code09_Jail1.MAXE])
Code09_Jail1.to2 = jarray('int', [Code09_Jail1.MAXE])
Code09_Jail1.cnt2 = jcast('int', 0)
Code09_Jail1.dep = jarray('int', [Code09_Jail1.MAXN])
Code09_Jail1.dfn = jarray('int', [Code09_Jail1.MAXN])
Code09_Jail1.siz = jarray('int', [Code09_Jail1.MAXN])
Code09_Jail1.stjump = jarray('int', [Code09_Jail1.MAXN, Code09_Jail1.MAXP])
Code09_Jail1.cntd = jcast('int', 0)
Code09_Jail1.stout = jarray('int', [Code09_Jail1.MAXN, Code09_Jail1.MAXP])
Code09_Jail1.stin = jarray('int', [Code09_Jail1.MAXN, Code09_Jail1.MAXP])
Code09_Jail1.cntt = jcast('int', 0)
Code09_Jail1.que = jarray('int', [Code09_Jail1.MAXT])
Code09_Jail1.ufe = jarray('int', [Code09_Jail1.MAXN, 3])
Code09_Jail1.stacksize = jcast('int', 0)
Code09_Jail1.u = jcast('int', 0)
Code09_Jail1.fa = jcast('int', 0)
Code09_Jail1.e = jcast('int', 0)

if __name__ == '__main__':
    Code09_Jail1.main([])
