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

# 城市建设，Python版
# 一共n个点、m条无向边，边有边权，编号1~m，图保证连通
# 接下来有q次修改，格式 e w，代表第e条边的边权修改为w
# 每次修改之后，打印当前图的最小生成树边权和
# 1 <= n <= 2 * 10^4
# 1 <= m、q <= 5 * 10^4
# 0 <= 边权 <= 5 * 10^7
# 测试链接 : https://www.luogu.com.cn/problem/P3206
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_CityConstruction2:
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
        jset(Code07_CityConstruction2.nxt, ((_java_obj_1 := Code07_CityConstruction2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_CityConstruction2.head[i])
        Code07_CityConstruction2.to[Code07_CityConstruction2.cntg] = jcast('int', e)
        Code07_CityConstruction2.head[i] = jcast('int', Code07_CityConstruction2.cntg)

    @staticmethod
    def add(jobl, jobr, jobe, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobe = jcast('int', jobe)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code07_CityConstruction2.rangeAddEdge(i, jobe)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code07_CityConstruction2.add(jobl, jobr, jobe, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code07_CityConstruction2.add(jobl, jobr, jobe, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code07_CityConstruction2.maxEdge[x] = jcast('int', (0 if (x <= Code07_CityConstruction2.n) else jcast('int', (x - Code07_CityConstruction2.n))))
        if (Code07_CityConstruction2.ew[Code07_CityConstruction2.maxEdge[Code07_CityConstruction2.ls[x]]] > Code07_CityConstruction2.ew[Code07_CityConstruction2.maxEdge[x]]):
            Code07_CityConstruction2.maxEdge[x] = jcast('int', Code07_CityConstruction2.maxEdge[Code07_CityConstruction2.ls[x]])
        if (Code07_CityConstruction2.ew[Code07_CityConstruction2.maxEdge[Code07_CityConstruction2.rs[x]]] > Code07_CityConstruction2.ew[Code07_CityConstruction2.maxEdge[x]]):
            Code07_CityConstruction2.maxEdge[x] = jcast('int', Code07_CityConstruction2.maxEdge[Code07_CityConstruction2.rs[x]])

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code07_CityConstruction2.ls[Code07_CityConstruction2.fa[x]] != x) and (Code07_CityConstruction2.rs[Code07_CityConstruction2.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code07_CityConstruction2.ls[Code07_CityConstruction2.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code07_CityConstruction2.ls[x])
            Code07_CityConstruction2.ls[x] = jcast('int', Code07_CityConstruction2.rs[x])
            Code07_CityConstruction2.rs[x] = jcast('int', tmp)
            Code07_CityConstruction2.rev[x] = jcast('boolean', (not Code07_CityConstruction2.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code07_CityConstruction2.rev[x]:
            Code07_CityConstruction2.reverse(Code07_CityConstruction2.ls[x])
            Code07_CityConstruction2.reverse(Code07_CityConstruction2.rs[x])
            Code07_CityConstruction2.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code07_CityConstruction2.fa[x])
        g = jcast('int', Code07_CityConstruction2.fa[f])
        if (Code07_CityConstruction2.lr(x) == 0):
            Code07_CityConstruction2.ls[f] = jcast('int', Code07_CityConstruction2.rs[x])
            if (Code07_CityConstruction2.ls[f] != 0):
                jset(Code07_CityConstruction2.fa, Code07_CityConstruction2.ls[f], f)
            Code07_CityConstruction2.rs[x] = jcast('int', f)
        else:
            Code07_CityConstruction2.rs[f] = jcast('int', Code07_CityConstruction2.ls[x])
            if (Code07_CityConstruction2.rs[f] != 0):
                jset(Code07_CityConstruction2.fa, Code07_CityConstruction2.rs[f], f)
            Code07_CityConstruction2.ls[x] = jcast('int', f)
        if (not Code07_CityConstruction2.isroot(f)):
            if (Code07_CityConstruction2.lr(f) == 0):
                Code07_CityConstruction2.ls[g] = jcast('int', x)
            else:
                Code07_CityConstruction2.rs[g] = jcast('int', x)
        Code07_CityConstruction2.fa[f] = jcast('int', x)
        Code07_CityConstruction2.fa[x] = jcast('int', g)
        Code07_CityConstruction2.up(f)
        Code07_CityConstruction2.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code07_CityConstruction2.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code07_CityConstruction2.isroot(y)):
            jset(Code07_CityConstruction2.sta, (siz := jcast('int', (siz + (1)))), Code07_CityConstruction2.fa[y])
            y = jcast('int', Code07_CityConstruction2.fa[y])
        while (siz != 0):
            Code07_CityConstruction2.down(Code07_CityConstruction2.sta[((_java_old_4 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_4)[2]])
        while (not Code07_CityConstruction2.isroot(x)):
            f = jcast('int', Code07_CityConstruction2.fa[x])
            if (not Code07_CityConstruction2.isroot(f)):
                if (Code07_CityConstruction2.lr(x) == Code07_CityConstruction2.lr(f)):
                    Code07_CityConstruction2.rotate(f)
                else:
                    Code07_CityConstruction2.rotate(x)
            Code07_CityConstruction2.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code07_CityConstruction2.splay(x)
            Code07_CityConstruction2.rs[x] = jcast('int', y)
            Code07_CityConstruction2.up(x)
            y = jcast('int', x)
            x = jcast('int', Code07_CityConstruction2.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code07_CityConstruction2.access(x)
        Code07_CityConstruction2.splay(x)
        Code07_CityConstruction2.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code07_CityConstruction2.access(x)
        Code07_CityConstruction2.splay(x)
        Code07_CityConstruction2.down(x)
        while (Code07_CityConstruction2.ls[x] != 0):
            x = jcast('int', Code07_CityConstruction2.ls[x])
            Code07_CityConstruction2.down(x)
        Code07_CityConstruction2.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code07_CityConstruction2.makeroot(x)
        Code07_CityConstruction2.access(y)
        Code07_CityConstruction2.splay(y)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code07_CityConstruction2.makeroot(x)
        if (Code07_CityConstruction2.findroot(y) != x):
            Code07_CityConstruction2.fa[x] = jcast('int', y)

    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code07_CityConstruction2.makeroot(x)
        if ((((Code07_CityConstruction2.findroot(y) == x) and (Code07_CityConstruction2.fa[y] == x)) and (Code07_CityConstruction2.ls[y] == 0)) and (Code07_CityConstruction2.rs[x] == y)):
            jset(Code07_CityConstruction2.fa, y, jset(Code07_CityConstruction2.rs, x, 0))
            Code07_CityConstruction2.up(x)

    @staticmethod
    def backup(edge, type):
        edge = jcast('int', edge)
        type = jcast('int', type)
        jset(Code07_CityConstruction2.rollbackEdge, ((_java_obj_5 := Code07_CityConstruction2), (_java_key_6 := 'opsize'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))))[3], edge)
        Code07_CityConstruction2.rollbackType[Code07_CityConstruction2.opsize] = jcast('int', type)

    @staticmethod
    def addEdge(e):
        e = jcast('int', e)
        x = jcast('int', Code07_CityConstruction2.ex[e])
        y = jcast('int', Code07_CityConstruction2.ey[e])
        Code07_CityConstruction2.makeroot(x)
        if (Code07_CityConstruction2.findroot(y) != x):
            Code07_CityConstruction2.link(x, jcast('int', jadd(Code07_CityConstruction2.n, e)))
            Code07_CityConstruction2.link(y, jcast('int', jadd(Code07_CityConstruction2.n, e)))
            Code07_CityConstruction2.backup(e, 1)
            Code07_CityConstruction2.mstSum = jcast('long', jcast('long', jadd(Code07_CityConstruction2.mstSum, Code07_CityConstruction2.ew[e])))
        else:
            Code07_CityConstruction2.split(x, y)
            pre = jcast('int', Code07_CityConstruction2.maxEdge[y])
            if (Code07_CityConstruction2.ew[pre] > Code07_CityConstruction2.ew[e]):
                Code07_CityConstruction2.cut(Code07_CityConstruction2.ex[pre], jcast('int', jadd(Code07_CityConstruction2.n, pre)))
                Code07_CityConstruction2.cut(Code07_CityConstruction2.ey[pre], jcast('int', jadd(Code07_CityConstruction2.n, pre)))
                Code07_CityConstruction2.backup(pre, 2)
                Code07_CityConstruction2.mstSum = jcast('long', jcast('long', (Code07_CityConstruction2.mstSum - Code07_CityConstruction2.ew[pre])))
                Code07_CityConstruction2.link(x, jcast('int', jadd(Code07_CityConstruction2.n, e)))
                Code07_CityConstruction2.link(y, jcast('int', jadd(Code07_CityConstruction2.n, e)))
                Code07_CityConstruction2.backup(e, 1)
                Code07_CityConstruction2.mstSum = jcast('long', jcast('long', jadd(Code07_CityConstruction2.mstSum, Code07_CityConstruction2.ew[e])))

    @staticmethod
    def undo():
        e = jcast('int', Code07_CityConstruction2.rollbackEdge[Code07_CityConstruction2.opsize])
        t = jcast('int', Code07_CityConstruction2.rollbackType[((_java_obj_8 := Code07_CityConstruction2), (_java_key_9 := 'opsize'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (-1)))), _java_old_10)[4]])
        if (t == 1):
            Code07_CityConstruction2.cut(Code07_CityConstruction2.ex[e], jcast('int', jadd(Code07_CityConstruction2.n, e)))
            Code07_CityConstruction2.cut(Code07_CityConstruction2.ey[e], jcast('int', jadd(Code07_CityConstruction2.n, e)))
            Code07_CityConstruction2.mstSum = jcast('long', jcast('long', (Code07_CityConstruction2.mstSum - Code07_CityConstruction2.ew[e])))
        else:
            Code07_CityConstruction2.link(Code07_CityConstruction2.ex[e], jcast('int', jadd(Code07_CityConstruction2.n, e)))
            Code07_CityConstruction2.link(Code07_CityConstruction2.ey[e], jcast('int', jadd(Code07_CityConstruction2.n, e)))
            Code07_CityConstruction2.mstSum = jcast('long', jcast('long', jadd(Code07_CityConstruction2.mstSum, Code07_CityConstruction2.ew[e])))

    @staticmethod
    def dfs(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        tmp = jcast('int', Code07_CityConstruction2.opsize)
        k = jcast('int', Code07_CityConstruction2.head[i])
        while (k != 0):
            Code07_CityConstruction2.addEdge(Code07_CityConstruction2.to[k])
            k = jcast('int', Code07_CityConstruction2.nxt[k])
        if (l == r):
            Code07_CityConstruction2.ans[l] = jcast('long', Code07_CityConstruction2.mstSum)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code07_CityConstruction2.dfs(l, mid, jcast('int', (i << (1 & 31))))
            Code07_CityConstruction2.dfs(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        while (Code07_CityConstruction2.opsize > tmp):
            Code07_CityConstruction2.undo()

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code07_CityConstruction2.m):
            Code07_CityConstruction2.endTime[i] = jcast('int', jcast('int', jadd(Code07_CityConstruction2.q, 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', Code07_CityConstruction2.q)
        while (i >= 1):
            e = jcast('int', Code07_CityConstruction2.changeEdge[i])
            Code07_CityConstruction2.add(i, jcast('int', (Code07_CityConstruction2.endTime[e] - 1)), jcast('int', jadd(Code07_CityConstruction2.m, i)), 1, Code07_CityConstruction2.q, 1)
            Code07_CityConstruction2.endTime[e] = jcast('int', i)
            i = jcast('int', (i - 1))
        i = jcast('int', 1)
        while (i <= Code07_CityConstruction2.m):
            if (Code07_CityConstruction2.endTime[i] > 1):
                Code07_CityConstruction2.add(1, jcast('int', (Code07_CityConstruction2.endTime[i] - 1)), i, 1, Code07_CityConstruction2.q, 1)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code07_CityConstruction2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_CityConstruction2.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_CityConstruction2.m = jcast('int', jcall(in_, 'nextInt'))
        Code07_CityConstruction2.q = jcast('int', jcall(in_, 'nextInt'))
        Code07_CityConstruction2.cnte = jcast('int', Code07_CityConstruction2.m)
        i = jcast('int', 1)
        while (i <= Code07_CityConstruction2.m):
            jset(Code07_CityConstruction2.ex, i, jcall(in_, 'nextInt'))
            jset(Code07_CityConstruction2.ey, i, jcall(in_, 'nextInt'))
            jset(Code07_CityConstruction2.ew, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_CityConstruction2.q):
            e = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code07_CityConstruction2.changeEdge[i] = jcast('int', e)
            jset(Code07_CityConstruction2.ex, ((_java_obj_11 := Code07_CityConstruction2), (_java_key_12 := 'cnte'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))))[3], Code07_CityConstruction2.ex[e])
            Code07_CityConstruction2.ey[Code07_CityConstruction2.cnte] = jcast('int', Code07_CityConstruction2.ey[e])
            Code07_CityConstruction2.ew[Code07_CityConstruction2.cnte] = jcast('int', w)
            i = jcast('int', (i + 1))
        Code07_CityConstruction2.prepare()
        Code07_CityConstruction2.dfs(1, Code07_CityConstruction2.q, 1)
        i = jcast('int', 1)
        while (i <= Code07_CityConstruction2.q):
            jcall(out, 'println', Code07_CityConstruction2.ans[i])
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
            raise TypeError("No matching overload for Code07_CityConstruction2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_CityConstruction2.MAXN = jcast('int', 200001)
Code07_CityConstruction2.MAXQ = jcast('int', 50001)
Code07_CityConstruction2.MAXT = jcast('int', 4000001)
Code07_CityConstruction2.n = jcast('int', 0)
Code07_CityConstruction2.m = jcast('int', 0)
Code07_CityConstruction2.q = jcast('int', 0)
Code07_CityConstruction2.ex = jarray('int', [Code07_CityConstruction2.MAXN])
Code07_CityConstruction2.ey = jarray('int', [Code07_CityConstruction2.MAXN])
Code07_CityConstruction2.ew = jarray('int', [Code07_CityConstruction2.MAXN])
Code07_CityConstruction2.cnte = jcast('int', 0)
Code07_CityConstruction2.changeEdge = jarray('int', [Code07_CityConstruction2.MAXQ])
Code07_CityConstruction2.endTime = jarray('int', [Code07_CityConstruction2.MAXN])
Code07_CityConstruction2.head = jarray('int', [jcast('int', (Code07_CityConstruction2.MAXQ << (2 & 31)))])
Code07_CityConstruction2.nxt = jarray('int', [Code07_CityConstruction2.MAXT])
Code07_CityConstruction2.to = jarray('int', [Code07_CityConstruction2.MAXT])
Code07_CityConstruction2.cntg = jcast('int', 0)
Code07_CityConstruction2.fa = jarray('int', [Code07_CityConstruction2.MAXN])
Code07_CityConstruction2.ls = jarray('int', [Code07_CityConstruction2.MAXN])
Code07_CityConstruction2.rs = jarray('int', [Code07_CityConstruction2.MAXN])
Code07_CityConstruction2.rev = jarray('boolean', [Code07_CityConstruction2.MAXN])
Code07_CityConstruction2.sta = jarray('int', [Code07_CityConstruction2.MAXN])
Code07_CityConstruction2.maxEdge = jarray('int', [Code07_CityConstruction2.MAXN])
Code07_CityConstruction2.rollbackEdge = jarray('int', [jcast('int', (Code07_CityConstruction2.MAXN << (1 & 31)))])
Code07_CityConstruction2.rollbackType = jarray('int', [jcast('int', (Code07_CityConstruction2.MAXN << (1 & 31)))])
Code07_CityConstruction2.opsize = jcast('int', 0)
Code07_CityConstruction2.mstSum = jcast('long', 0)
Code07_CityConstruction2.ans = jarray('long', [Code07_CityConstruction2.MAXQ])

if __name__ == '__main__':
    Code07_CityConstruction2.main([])
