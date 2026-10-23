# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 变化的道路，Python版
# 一共n个点，n-1条无向道路，所有点组成一棵树，这些道路始终存在
# 然后给定m条变化的道路，每条变化的道路，只在第l天到第r天存在
# 道路给定权值代表费用，同一天内，一条道路在第一次经过时收费，之后免费
# 每天从1号点出发并游览所有点，要求游览结束后剩余钱数 > 0
# 打印每天出发时至少需要多少钱，也就是最少总费用+1
# 1 <= n <= 5 * 10^4
# 1 <= m <= 10^5
# 天数固定为32766，输出也固定为32766行
# 测试链接 : https://www.luogu.com.cn/problem/P4319
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_ChangingRoads2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXD': 'MAXD', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 'ex': 'ex', 'ey': 'ey', 'ew': 'ew', 'cnte': 'cnte', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'rev': 'rev', 'sta': 'sta', 'maxEdge': 'maxEdge', 'rollbackEdge': 'rollbackEdge', 'rollbackType': 'rollbackType', 'opsize': 'opsize', 'mstSum': 'mstSum', 'ans': 'ans'}
    MAXN = 0
    MAXD = 0
    MAXT = 0
    n = 0
    m = 0
    # 道路信息，包括初始道路和变化道路
    ex = None
    ey = None
    ew = None
    cnte = 0
    # 时间轴线段树，线段树区间拥有哪些道路的列表
    head = None
    nxt = None
    to = None
    cntg = 0
    # 辅助splay
    fa = None
    ls = None
    rs = None
    rev = None
    sta = None
    # maxEdge[x]表示以x为根的辅助splay中，权值最大的边的编号
    maxEdge = None
    # LCT最小生成树修改的回滚信息，用回滚栈记录
    # type == 1 : 这条边加入
    # type == 2 : 这条边删除
    rollbackEdge = None
    rollbackType = None
    opsize = 0
    # 当前最小生成树的边权和，再加1就是答案
    mstSum = 0
    ans = None
    @staticmethod
    def rangeAddEdge(i, e):
        i = jcast('int', i)
        e = jcast('int', e)
        jset(Code06_ChangingRoads2.nxt, ((_java_obj_1 := Code06_ChangingRoads2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_ChangingRoads2.head[i])
        Code06_ChangingRoads2.to[Code06_ChangingRoads2.cntg] = jcast('int', e)
        Code06_ChangingRoads2.head[i] = jcast('int', Code06_ChangingRoads2.cntg)

    @staticmethod
    def add(jobl, jobr, jobe, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobe = jcast('int', jobe)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code06_ChangingRoads2.rangeAddEdge(i, jobe)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code06_ChangingRoads2.add(jobl, jobr, jobe, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code06_ChangingRoads2.add(jobl, jobr, jobe, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code06_ChangingRoads2.maxEdge[x] = jcast('int', (0 if (x <= Code06_ChangingRoads2.n) else jcast('int', (x - Code06_ChangingRoads2.n))))
        if (Code06_ChangingRoads2.ew[Code06_ChangingRoads2.maxEdge[Code06_ChangingRoads2.ls[x]]] > Code06_ChangingRoads2.ew[Code06_ChangingRoads2.maxEdge[x]]):
            Code06_ChangingRoads2.maxEdge[x] = jcast('int', Code06_ChangingRoads2.maxEdge[Code06_ChangingRoads2.ls[x]])
        if (Code06_ChangingRoads2.ew[Code06_ChangingRoads2.maxEdge[Code06_ChangingRoads2.rs[x]]] > Code06_ChangingRoads2.ew[Code06_ChangingRoads2.maxEdge[x]]):
            Code06_ChangingRoads2.maxEdge[x] = jcast('int', Code06_ChangingRoads2.maxEdge[Code06_ChangingRoads2.rs[x]])

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code06_ChangingRoads2.ls[Code06_ChangingRoads2.fa[x]] != x) and (Code06_ChangingRoads2.rs[Code06_ChangingRoads2.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code06_ChangingRoads2.ls[Code06_ChangingRoads2.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code06_ChangingRoads2.ls[x])
            Code06_ChangingRoads2.ls[x] = jcast('int', Code06_ChangingRoads2.rs[x])
            Code06_ChangingRoads2.rs[x] = jcast('int', tmp)
            Code06_ChangingRoads2.rev[x] = jcast('boolean', (not Code06_ChangingRoads2.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code06_ChangingRoads2.rev[x]:
            Code06_ChangingRoads2.reverse(Code06_ChangingRoads2.ls[x])
            Code06_ChangingRoads2.reverse(Code06_ChangingRoads2.rs[x])
            Code06_ChangingRoads2.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code06_ChangingRoads2.fa[x])
        g = jcast('int', Code06_ChangingRoads2.fa[f])
        if (Code06_ChangingRoads2.lr(x) == 0):
            Code06_ChangingRoads2.ls[f] = jcast('int', Code06_ChangingRoads2.rs[x])
            if (Code06_ChangingRoads2.ls[f] != 0):
                jset(Code06_ChangingRoads2.fa, Code06_ChangingRoads2.ls[f], f)
            Code06_ChangingRoads2.rs[x] = jcast('int', f)
        else:
            Code06_ChangingRoads2.rs[f] = jcast('int', Code06_ChangingRoads2.ls[x])
            if (Code06_ChangingRoads2.rs[f] != 0):
                jset(Code06_ChangingRoads2.fa, Code06_ChangingRoads2.rs[f], f)
            Code06_ChangingRoads2.ls[x] = jcast('int', f)
        if (not Code06_ChangingRoads2.isroot(f)):
            if (Code06_ChangingRoads2.lr(f) == 0):
                Code06_ChangingRoads2.ls[g] = jcast('int', x)
            else:
                Code06_ChangingRoads2.rs[g] = jcast('int', x)
        Code06_ChangingRoads2.fa[f] = jcast('int', x)
        Code06_ChangingRoads2.fa[x] = jcast('int', g)
        Code06_ChangingRoads2.up(f)
        Code06_ChangingRoads2.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code06_ChangingRoads2.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code06_ChangingRoads2.isroot(y)):
            jset(Code06_ChangingRoads2.sta, (siz := jcast('int', (siz + (1)))), Code06_ChangingRoads2.fa[y])
            y = jcast('int', Code06_ChangingRoads2.fa[y])
        while (siz != 0):
            Code06_ChangingRoads2.down(Code06_ChangingRoads2.sta[((_java_old_4 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_4)[2]])
        while (not Code06_ChangingRoads2.isroot(x)):
            f = jcast('int', Code06_ChangingRoads2.fa[x])
            if (not Code06_ChangingRoads2.isroot(f)):
                if (Code06_ChangingRoads2.lr(x) == Code06_ChangingRoads2.lr(f)):
                    Code06_ChangingRoads2.rotate(f)
                else:
                    Code06_ChangingRoads2.rotate(x)
            Code06_ChangingRoads2.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code06_ChangingRoads2.splay(x)
            Code06_ChangingRoads2.rs[x] = jcast('int', y)
            Code06_ChangingRoads2.up(x)
            y = jcast('int', x)
            x = jcast('int', Code06_ChangingRoads2.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code06_ChangingRoads2.access(x)
        Code06_ChangingRoads2.splay(x)
        Code06_ChangingRoads2.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code06_ChangingRoads2.access(x)
        Code06_ChangingRoads2.splay(x)
        Code06_ChangingRoads2.down(x)
        while (Code06_ChangingRoads2.ls[x] != 0):
            x = jcast('int', Code06_ChangingRoads2.ls[x])
            Code06_ChangingRoads2.down(x)
        Code06_ChangingRoads2.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code06_ChangingRoads2.makeroot(x)
        Code06_ChangingRoads2.access(y)
        Code06_ChangingRoads2.splay(y)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code06_ChangingRoads2.makeroot(x)
        if (Code06_ChangingRoads2.findroot(y) != x):
            Code06_ChangingRoads2.fa[x] = jcast('int', y)

    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code06_ChangingRoads2.makeroot(x)
        if ((((Code06_ChangingRoads2.findroot(y) == x) and (Code06_ChangingRoads2.fa[y] == x)) and (Code06_ChangingRoads2.ls[y] == 0)) and (Code06_ChangingRoads2.rs[x] == y)):
            jset(Code06_ChangingRoads2.fa, y, jset(Code06_ChangingRoads2.rs, x, 0))
            Code06_ChangingRoads2.up(x)

    @staticmethod
    def backup(edge, type):
        edge = jcast('int', edge)
        type = jcast('int', type)
        jset(Code06_ChangingRoads2.rollbackEdge, ((_java_obj_5 := Code06_ChangingRoads2), (_java_key_6 := 'opsize'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))))[3], edge)
        Code06_ChangingRoads2.rollbackType[Code06_ChangingRoads2.opsize] = jcast('int', type)

    # 尝试把第e条边加入当前最小生成树
    @staticmethod
    def addEdge(e):
        e = jcast('int', e)
        x = jcast('int', Code06_ChangingRoads2.ex[e])
        y = jcast('int', Code06_ChangingRoads2.ey[e])
        Code06_ChangingRoads2.makeroot(x)
        if (Code06_ChangingRoads2.findroot(y) != x):
            # 两端不连通，直接加入最小生成树
            Code06_ChangingRoads2.link(x, jcast('int', jadd(Code06_ChangingRoads2.n, e)))
            Code06_ChangingRoads2.link(y, jcast('int', jadd(Code06_ChangingRoads2.n, e)))
            Code06_ChangingRoads2.backup(e, 1)
            Code06_ChangingRoads2.mstSum = jcast('long', jcast('long', jadd(Code06_ChangingRoads2.mstSum, Code06_ChangingRoads2.ew[e])))
        else:
            # 两端已经连通，查询路径上的最大边
            Code06_ChangingRoads2.split(x, y)
            pre = jcast('int', Code06_ChangingRoads2.maxEdge[y])
            if (Code06_ChangingRoads2.ew[pre] > Code06_ChangingRoads2.ew[e]):
                # 删除旧边
                Code06_ChangingRoads2.cut(Code06_ChangingRoads2.ex[pre], jcast('int', jadd(Code06_ChangingRoads2.n, pre)))
                Code06_ChangingRoads2.cut(Code06_ChangingRoads2.ey[pre], jcast('int', jadd(Code06_ChangingRoads2.n, pre)))
                Code06_ChangingRoads2.backup(pre, 2)
                Code06_ChangingRoads2.mstSum = jcast('long', jcast('long', (Code06_ChangingRoads2.mstSum - Code06_ChangingRoads2.ew[pre])))
                # 加入新边
                Code06_ChangingRoads2.link(x, jcast('int', jadd(Code06_ChangingRoads2.n, e)))
                Code06_ChangingRoads2.link(y, jcast('int', jadd(Code06_ChangingRoads2.n, e)))
                Code06_ChangingRoads2.backup(e, 1)
                Code06_ChangingRoads2.mstSum = jcast('long', jcast('long', jadd(Code06_ChangingRoads2.mstSum, Code06_ChangingRoads2.ew[e])))

    @staticmethod
    def undo():
        e = jcast('int', Code06_ChangingRoads2.rollbackEdge[Code06_ChangingRoads2.opsize])
        t = jcast('int', Code06_ChangingRoads2.rollbackType[((_java_obj_8 := Code06_ChangingRoads2), (_java_key_9 := 'opsize'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (-1)))), _java_old_10)[4]])
        # 当时加入，现在删除
        if (t == 1):
            Code06_ChangingRoads2.cut(Code06_ChangingRoads2.ex[e], jcast('int', jadd(Code06_ChangingRoads2.n, e)))
            Code06_ChangingRoads2.cut(Code06_ChangingRoads2.ey[e], jcast('int', jadd(Code06_ChangingRoads2.n, e)))
            Code06_ChangingRoads2.mstSum = jcast('long', jcast('long', (Code06_ChangingRoads2.mstSum - Code06_ChangingRoads2.ew[e])))
            # 当时删除，现在加入
        else:
            Code06_ChangingRoads2.link(Code06_ChangingRoads2.ex[e], jcast('int', jadd(Code06_ChangingRoads2.n, e)))
            Code06_ChangingRoads2.link(Code06_ChangingRoads2.ey[e], jcast('int', jadd(Code06_ChangingRoads2.n, e)))
            Code06_ChangingRoads2.mstSum = jcast('long', jcast('long', jadd(Code06_ChangingRoads2.mstSum, Code06_ChangingRoads2.ew[e])))

    @staticmethod
    def dfs(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        tmp = jcast('int', Code06_ChangingRoads2.opsize)
        k = jcast('int', Code06_ChangingRoads2.head[i])
        while (k != 0):
            Code06_ChangingRoads2.addEdge(Code06_ChangingRoads2.to[k])
            k = jcast('int', Code06_ChangingRoads2.nxt[k])
        if (l == r):
            Code06_ChangingRoads2.ans[l] = jcast('long', Code06_ChangingRoads2.mstSum)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code06_ChangingRoads2.dfs(l, mid, jcast('int', (i << (1 & 31))))
            Code06_ChangingRoads2.dfs(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        while (Code06_ChangingRoads2.opsize > tmp):
            Code06_ChangingRoads2.undo()

    @staticmethod
    def main(args):
        in_ = Code06_ChangingRoads2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_ChangingRoads2.n = jcast('int', jcall(in_, 'nextInt'))
        day = jcast('int', jcast('int', (Code06_ChangingRoads2.MAXD - 1)))
        i = jcast('int', 1)
        while (i < Code06_ChangingRoads2.n):
            jset(Code06_ChangingRoads2.ex, ((_java_obj_11 := Code06_ChangingRoads2), (_java_key_12 := 'cnte'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))))[3], jcall(in_, 'nextInt'))
            jset(Code06_ChangingRoads2.ey, Code06_ChangingRoads2.cnte, jcall(in_, 'nextInt'))
            jset(Code06_ChangingRoads2.ew, Code06_ChangingRoads2.cnte, jcall(in_, 'nextInt'))
            Code06_ChangingRoads2.add(1, day, Code06_ChangingRoads2.cnte, 1, day, 1)
            i = jcast('int', (i + 1))
        Code06_ChangingRoads2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        l = 0
        r = 0
        while (i <= Code06_ChangingRoads2.m):
            jset(Code06_ChangingRoads2.ex, ((_java_obj_14 := Code06_ChangingRoads2), (_java_key_15 := 'cnte'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))))[3], jcall(in_, 'nextInt'))
            jset(Code06_ChangingRoads2.ey, Code06_ChangingRoads2.cnte, jcall(in_, 'nextInt'))
            jset(Code06_ChangingRoads2.ew, Code06_ChangingRoads2.cnte, jcall(in_, 'nextInt'))
            l = jcast('int', jcall(in_, 'nextInt'))
            r = jcast('int', jcall(in_, 'nextInt'))
            Code06_ChangingRoads2.add(l, r, Code06_ChangingRoads2.cnte, 1, day, 1)
            i = jcast('int', (i + 1))
        Code06_ChangingRoads2.dfs(1, day, 1)
        i = jcast('int', 1)
        while (i <= day):
            jcall(out, 'println', Code06_ChangingRoads2.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_17 := self), (_java_key_18 := 'ptr'), (_java_old_19 := jget(_java_obj_17, _java_key_18)), jset(_java_obj_17, _java_key_18, jcast('int', (_java_old_19 + (1)))), _java_old_19)[4]])

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
            raise TypeError("No matching overload for Code06_ChangingRoads2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_ChangingRoads2.MAXN = jcast('int', 200001)
Code06_ChangingRoads2.MAXD = jcast('int', 32767)
Code06_ChangingRoads2.MAXT = jcast('int', 4000001)
Code06_ChangingRoads2.n = jcast('int', 0)
Code06_ChangingRoads2.m = jcast('int', 0)
Code06_ChangingRoads2.ex = jarray('int', [Code06_ChangingRoads2.MAXN])
Code06_ChangingRoads2.ey = jarray('int', [Code06_ChangingRoads2.MAXN])
Code06_ChangingRoads2.ew = jarray('int', [Code06_ChangingRoads2.MAXN])
Code06_ChangingRoads2.cnte = jcast('int', 0)
Code06_ChangingRoads2.head = jarray('int', [jcast('int', (Code06_ChangingRoads2.MAXD << (2 & 31)))])
Code06_ChangingRoads2.nxt = jarray('int', [Code06_ChangingRoads2.MAXT])
Code06_ChangingRoads2.to = jarray('int', [Code06_ChangingRoads2.MAXT])
Code06_ChangingRoads2.cntg = jcast('int', 0)
Code06_ChangingRoads2.fa = jarray('int', [Code06_ChangingRoads2.MAXN])
Code06_ChangingRoads2.ls = jarray('int', [Code06_ChangingRoads2.MAXN])
Code06_ChangingRoads2.rs = jarray('int', [Code06_ChangingRoads2.MAXN])
Code06_ChangingRoads2.rev = jarray('boolean', [Code06_ChangingRoads2.MAXN])
Code06_ChangingRoads2.sta = jarray('int', [Code06_ChangingRoads2.MAXN])
Code06_ChangingRoads2.maxEdge = jarray('int', [Code06_ChangingRoads2.MAXN])
Code06_ChangingRoads2.rollbackEdge = jarray('int', [jcast('int', (Code06_ChangingRoads2.MAXN << (1 & 31)))])
Code06_ChangingRoads2.rollbackType = jarray('int', [jcast('int', (Code06_ChangingRoads2.MAXN << (1 & 31)))])
Code06_ChangingRoads2.opsize = jcast('int', 0)
Code06_ChangingRoads2.mstSum = jcast('long', 1)
Code06_ChangingRoads2.ans = jarray('long', [Code06_ChangingRoads2.MAXD])

if __name__ == '__main__':
    Code06_ChangingRoads2.main([])
