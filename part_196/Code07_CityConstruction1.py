# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 城市建设，Python版
# 一共n个点、m条无向边，边有边权，编号1~m，图保证连通
# 接下来有q次修改，格式 e w，代表第e条边的边权修改为w
# 每次修改之后，打印当前图的最小生成树边权和
# 1 <= n <= 2 * 10^4
# 1 <= m、q <= 5 * 10^4
# 0 <= 边权 <= 5 * 10^7
# 测试链接 : https://www.luogu.com.cn/problem/P3206
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 对应实现可参考 Code07_CityConstruction2.py
# 两个版本保留相同的算法逻辑
class Code07_CityConstruction1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXQ': 'MAXQ', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 'q': 'q', 'ex': 'ex', 'ey': 'ey', 'ew': 'ew', 'cnte': 'cnte', 'changeEdge': 'changeEdge', 'endTime': 'endTime', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'rev': 'rev', 'sta': 'sta', 'maxEdge': 'maxEdge', 'rollbackEdge': 'rollbackEdge', 'rollbackType': 'rollbackType', 'opsize': 'opsize', 'mstSum': 'mstSum', 'ans': 'ans'}
    MAXN = 0
    MAXQ = 0
    MAXT = 0
    n = 0
    m = 0
    q = 0
    ex = None
    ey = None
    ew = None
    cnte = 0
    changeEdge = None
    endTime = None
    head = None
    nxt = None
    to = None
    cntg = 0
    fa = None
    ls = None
    rs = None
    rev = None
    sta = None
    maxEdge = None
    rollbackEdge = None
    rollbackType = None
    opsize = 0
    mstSum = 0
    ans = None
    @staticmethod
    def rangeAddEdge(i, e):
        i = jcast('int', i)
        e = jcast('int', e)
        jset(Code07_CityConstruction1.nxt, ((_java_obj_1 := Code07_CityConstruction1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_CityConstruction1.head[i])
        Code07_CityConstruction1.to[Code07_CityConstruction1.cntg] = jcast('int', e)
        Code07_CityConstruction1.head[i] = jcast('int', Code07_CityConstruction1.cntg)

    @staticmethod
    def add(jobl, jobr, jobe, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobe = jcast('int', jobe)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code07_CityConstruction1.rangeAddEdge(i, jobe)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code07_CityConstruction1.add(jobl, jobr, jobe, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code07_CityConstruction1.add(jobl, jobr, jobe, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code07_CityConstruction1.maxEdge[x] = jcast('int', (0 if (x <= Code07_CityConstruction1.n) else jcast('int', (x - Code07_CityConstruction1.n))))
        if (Code07_CityConstruction1.ew[Code07_CityConstruction1.maxEdge[Code07_CityConstruction1.ls[x]]] > Code07_CityConstruction1.ew[Code07_CityConstruction1.maxEdge[x]]):
            Code07_CityConstruction1.maxEdge[x] = jcast('int', Code07_CityConstruction1.maxEdge[Code07_CityConstruction1.ls[x]])
        if (Code07_CityConstruction1.ew[Code07_CityConstruction1.maxEdge[Code07_CityConstruction1.rs[x]]] > Code07_CityConstruction1.ew[Code07_CityConstruction1.maxEdge[x]]):
            Code07_CityConstruction1.maxEdge[x] = jcast('int', Code07_CityConstruction1.maxEdge[Code07_CityConstruction1.rs[x]])

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code07_CityConstruction1.ls[Code07_CityConstruction1.fa[x]] != x) and (Code07_CityConstruction1.rs[Code07_CityConstruction1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code07_CityConstruction1.ls[Code07_CityConstruction1.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code07_CityConstruction1.ls[x])
            Code07_CityConstruction1.ls[x] = jcast('int', Code07_CityConstruction1.rs[x])
            Code07_CityConstruction1.rs[x] = jcast('int', tmp)
            Code07_CityConstruction1.rev[x] = jcast('boolean', (not Code07_CityConstruction1.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code07_CityConstruction1.rev[x]:
            Code07_CityConstruction1.reverse(Code07_CityConstruction1.ls[x])
            Code07_CityConstruction1.reverse(Code07_CityConstruction1.rs[x])
            Code07_CityConstruction1.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code07_CityConstruction1.fa[x])
        g = jcast('int', Code07_CityConstruction1.fa[f])
        if (Code07_CityConstruction1.lr(x) == 0):
            Code07_CityConstruction1.ls[f] = jcast('int', Code07_CityConstruction1.rs[x])
            if (Code07_CityConstruction1.ls[f] != 0):
                jset(Code07_CityConstruction1.fa, Code07_CityConstruction1.ls[f], f)
            Code07_CityConstruction1.rs[x] = jcast('int', f)
        else:
            Code07_CityConstruction1.rs[f] = jcast('int', Code07_CityConstruction1.ls[x])
            if (Code07_CityConstruction1.rs[f] != 0):
                jset(Code07_CityConstruction1.fa, Code07_CityConstruction1.rs[f], f)
            Code07_CityConstruction1.ls[x] = jcast('int', f)
        if (not Code07_CityConstruction1.isroot(f)):
            if (Code07_CityConstruction1.lr(f) == 0):
                Code07_CityConstruction1.ls[g] = jcast('int', x)
            else:
                Code07_CityConstruction1.rs[g] = jcast('int', x)
        Code07_CityConstruction1.fa[f] = jcast('int', x)
        Code07_CityConstruction1.fa[x] = jcast('int', g)
        Code07_CityConstruction1.up(f)
        Code07_CityConstruction1.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code07_CityConstruction1.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code07_CityConstruction1.isroot(y)):
            jset(Code07_CityConstruction1.sta, (siz := jcast('int', (siz + (1)))), Code07_CityConstruction1.fa[y])
            y = jcast('int', Code07_CityConstruction1.fa[y])
        while (siz != 0):
            Code07_CityConstruction1.down(Code07_CityConstruction1.sta[((_java_old_4 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_4)[2]])
        while (not Code07_CityConstruction1.isroot(x)):
            f = jcast('int', Code07_CityConstruction1.fa[x])
            if (not Code07_CityConstruction1.isroot(f)):
                if (Code07_CityConstruction1.lr(x) == Code07_CityConstruction1.lr(f)):
                    Code07_CityConstruction1.rotate(f)
                else:
                    Code07_CityConstruction1.rotate(x)
            Code07_CityConstruction1.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code07_CityConstruction1.splay(x)
            Code07_CityConstruction1.rs[x] = jcast('int', y)
            Code07_CityConstruction1.up(x)
            y = jcast('int', x)
            x = jcast('int', Code07_CityConstruction1.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code07_CityConstruction1.access(x)
        Code07_CityConstruction1.splay(x)
        Code07_CityConstruction1.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code07_CityConstruction1.access(x)
        Code07_CityConstruction1.splay(x)
        Code07_CityConstruction1.down(x)
        while (Code07_CityConstruction1.ls[x] != 0):
            x = jcast('int', Code07_CityConstruction1.ls[x])
            Code07_CityConstruction1.down(x)
        Code07_CityConstruction1.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code07_CityConstruction1.makeroot(x)
        Code07_CityConstruction1.access(y)
        Code07_CityConstruction1.splay(y)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code07_CityConstruction1.makeroot(x)
        if (Code07_CityConstruction1.findroot(y) != x):
            Code07_CityConstruction1.fa[x] = jcast('int', y)

    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code07_CityConstruction1.makeroot(x)
        if ((((Code07_CityConstruction1.findroot(y) == x) and (Code07_CityConstruction1.fa[y] == x)) and (Code07_CityConstruction1.ls[y] == 0)) and (Code07_CityConstruction1.rs[x] == y)):
            jset(Code07_CityConstruction1.fa, y, jset(Code07_CityConstruction1.rs, x, 0))
            Code07_CityConstruction1.up(x)

    @staticmethod
    def backup(edge, type):
        edge = jcast('int', edge)
        type = jcast('int', type)
        jset(Code07_CityConstruction1.rollbackEdge, ((_java_obj_5 := Code07_CityConstruction1), (_java_key_6 := 'opsize'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))))[3], edge)
        Code07_CityConstruction1.rollbackType[Code07_CityConstruction1.opsize] = jcast('int', type)

    @staticmethod
    def addEdge(e):
        e = jcast('int', e)
        x = jcast('int', Code07_CityConstruction1.ex[e])
        y = jcast('int', Code07_CityConstruction1.ey[e])
        Code07_CityConstruction1.makeroot(x)
        if (Code07_CityConstruction1.findroot(y) != x):
            Code07_CityConstruction1.link(x, jcast('int', jadd(Code07_CityConstruction1.n, e)))
            Code07_CityConstruction1.link(y, jcast('int', jadd(Code07_CityConstruction1.n, e)))
            Code07_CityConstruction1.backup(e, 1)
            Code07_CityConstruction1.mstSum = jcast('long', jcast('long', jadd(Code07_CityConstruction1.mstSum, Code07_CityConstruction1.ew[e])))
        else:
            Code07_CityConstruction1.split(x, y)
            pre = jcast('int', Code07_CityConstruction1.maxEdge[y])
            if (Code07_CityConstruction1.ew[pre] > Code07_CityConstruction1.ew[e]):
                Code07_CityConstruction1.cut(Code07_CityConstruction1.ex[pre], jcast('int', jadd(Code07_CityConstruction1.n, pre)))
                Code07_CityConstruction1.cut(Code07_CityConstruction1.ey[pre], jcast('int', jadd(Code07_CityConstruction1.n, pre)))
                Code07_CityConstruction1.backup(pre, 2)
                Code07_CityConstruction1.mstSum = jcast('long', jcast('long', (Code07_CityConstruction1.mstSum - Code07_CityConstruction1.ew[pre])))
                Code07_CityConstruction1.link(x, jcast('int', jadd(Code07_CityConstruction1.n, e)))
                Code07_CityConstruction1.link(y, jcast('int', jadd(Code07_CityConstruction1.n, e)))
                Code07_CityConstruction1.backup(e, 1)
                Code07_CityConstruction1.mstSum = jcast('long', jcast('long', jadd(Code07_CityConstruction1.mstSum, Code07_CityConstruction1.ew[e])))

    @staticmethod
    def undo():
        e = jcast('int', Code07_CityConstruction1.rollbackEdge[Code07_CityConstruction1.opsize])
        t = jcast('int', Code07_CityConstruction1.rollbackType[((_java_obj_8 := Code07_CityConstruction1), (_java_key_9 := 'opsize'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (-1)))), _java_old_10)[4]])
        if (t == 1):
            Code07_CityConstruction1.cut(Code07_CityConstruction1.ex[e], jcast('int', jadd(Code07_CityConstruction1.n, e)))
            Code07_CityConstruction1.cut(Code07_CityConstruction1.ey[e], jcast('int', jadd(Code07_CityConstruction1.n, e)))
            Code07_CityConstruction1.mstSum = jcast('long', jcast('long', (Code07_CityConstruction1.mstSum - Code07_CityConstruction1.ew[e])))
        else:
            Code07_CityConstruction1.link(Code07_CityConstruction1.ex[e], jcast('int', jadd(Code07_CityConstruction1.n, e)))
            Code07_CityConstruction1.link(Code07_CityConstruction1.ey[e], jcast('int', jadd(Code07_CityConstruction1.n, e)))
            Code07_CityConstruction1.mstSum = jcast('long', jcast('long', jadd(Code07_CityConstruction1.mstSum, Code07_CityConstruction1.ew[e])))

    @staticmethod
    def dfs(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        tmp = jcast('int', Code07_CityConstruction1.opsize)
        k = jcast('int', Code07_CityConstruction1.head[i])
        while (k != 0):
            Code07_CityConstruction1.addEdge(Code07_CityConstruction1.to[k])
            k = jcast('int', Code07_CityConstruction1.nxt[k])
        if (l == r):
            Code07_CityConstruction1.ans[l] = jcast('long', Code07_CityConstruction1.mstSum)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code07_CityConstruction1.dfs(l, mid, jcast('int', (i << (1 & 31))))
            Code07_CityConstruction1.dfs(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        while (Code07_CityConstruction1.opsize > tmp):
            Code07_CityConstruction1.undo()

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code07_CityConstruction1.m):
            Code07_CityConstruction1.endTime[i] = jcast('int', jcast('int', jadd(Code07_CityConstruction1.q, 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', Code07_CityConstruction1.q)
        while (i >= 1):
            e = jcast('int', Code07_CityConstruction1.changeEdge[i])
            Code07_CityConstruction1.add(i, jcast('int', (Code07_CityConstruction1.endTime[e] - 1)), jcast('int', jadd(Code07_CityConstruction1.m, i)), 1, Code07_CityConstruction1.q, 1)
            Code07_CityConstruction1.endTime[e] = jcast('int', i)
            i = jcast('int', (i - 1))
        i = jcast('int', 1)
        while (i <= Code07_CityConstruction1.m):
            if (Code07_CityConstruction1.endTime[i] > 1):
                Code07_CityConstruction1.add(1, jcast('int', (Code07_CityConstruction1.endTime[i] - 1)), i, 1, Code07_CityConstruction1.q, 1)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code07_CityConstruction1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_CityConstruction1.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_CityConstruction1.m = jcast('int', jcall(in_, 'nextInt'))
        Code07_CityConstruction1.q = jcast('int', jcall(in_, 'nextInt'))
        Code07_CityConstruction1.cnte = jcast('int', Code07_CityConstruction1.m)
        i = jcast('int', 1)
        while (i <= Code07_CityConstruction1.m):
            jset(Code07_CityConstruction1.ex, i, jcall(in_, 'nextInt'))
            jset(Code07_CityConstruction1.ey, i, jcall(in_, 'nextInt'))
            jset(Code07_CityConstruction1.ew, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_CityConstruction1.q):
            e = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code07_CityConstruction1.changeEdge[i] = jcast('int', e)
            jset(Code07_CityConstruction1.ex, ((_java_obj_11 := Code07_CityConstruction1), (_java_key_12 := 'cnte'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))))[3], Code07_CityConstruction1.ex[e])
            Code07_CityConstruction1.ey[Code07_CityConstruction1.cnte] = jcast('int', Code07_CityConstruction1.ey[e])
            Code07_CityConstruction1.ew[Code07_CityConstruction1.cnte] = jcast('int', w)
            i = jcast('int', (i + 1))
        Code07_CityConstruction1.prepare()
        Code07_CityConstruction1.dfs(1, Code07_CityConstruction1.q, 1)
        i = jcast('int', 1)
        while (i <= Code07_CityConstruction1.q):
            jcall(out, 'println', Code07_CityConstruction1.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_14 := self), (_java_key_15 := 'ptr'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))), _java_old_16)[4]])

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
                val = jcast('int', jcast('int', (jcast('int', jadd(jcast('int', (val * 10)), c)) - jchar('0'))))
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
            raise TypeError("No matching overload for Code07_CityConstruction1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_CityConstruction1.MAXN = jcast('int', 200001)
Code07_CityConstruction1.MAXQ = jcast('int', 50001)
Code07_CityConstruction1.MAXT = jcast('int', 4000001)
Code07_CityConstruction1.n = jcast('int', 0)
Code07_CityConstruction1.m = jcast('int', 0)
Code07_CityConstruction1.q = jcast('int', 0)
Code07_CityConstruction1.ex = jarray('int', [Code07_CityConstruction1.MAXN])
Code07_CityConstruction1.ey = jarray('int', [Code07_CityConstruction1.MAXN])
Code07_CityConstruction1.ew = jarray('int', [Code07_CityConstruction1.MAXN])
Code07_CityConstruction1.cnte = jcast('int', 0)
Code07_CityConstruction1.changeEdge = jarray('int', [Code07_CityConstruction1.MAXQ])
Code07_CityConstruction1.endTime = jarray('int', [Code07_CityConstruction1.MAXN])
Code07_CityConstruction1.head = jarray('int', [jcast('int', (Code07_CityConstruction1.MAXQ << (2 & 31)))])
Code07_CityConstruction1.nxt = jarray('int', [Code07_CityConstruction1.MAXT])
Code07_CityConstruction1.to = jarray('int', [Code07_CityConstruction1.MAXT])
Code07_CityConstruction1.cntg = jcast('int', 0)
Code07_CityConstruction1.fa = jarray('int', [Code07_CityConstruction1.MAXN])
Code07_CityConstruction1.ls = jarray('int', [Code07_CityConstruction1.MAXN])
Code07_CityConstruction1.rs = jarray('int', [Code07_CityConstruction1.MAXN])
Code07_CityConstruction1.rev = jarray('boolean', [Code07_CityConstruction1.MAXN])
Code07_CityConstruction1.sta = jarray('int', [Code07_CityConstruction1.MAXN])
Code07_CityConstruction1.maxEdge = jarray('int', [Code07_CityConstruction1.MAXN])
Code07_CityConstruction1.rollbackEdge = jarray('int', [jcast('int', (Code07_CityConstruction1.MAXN << (1 & 31)))])
Code07_CityConstruction1.rollbackType = jarray('int', [jcast('int', (Code07_CityConstruction1.MAXN << (1 & 31)))])
Code07_CityConstruction1.opsize = jcast('int', 0)
Code07_CityConstruction1.mstSum = jcast('long', 0)
Code07_CityConstruction1.ans = jarray('long', [Code07_CityConstruction1.MAXQ])

if __name__ == '__main__':
    Code07_CityConstruction1.main([])
