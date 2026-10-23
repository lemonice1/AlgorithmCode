# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 糖果公园，Python版
# 一共有n个公园，给定n-1条边，所有公园连成一棵树，c[i]为i号公园的糖果型号
# 一共有m种糖果，v[y]表示y号糖果的美味指数，给定长度为n的数组w，用于计算愉悦值
# 假设游客当前遇到了y号糖果，并且是第x次遇到，那么愉悦值会增加 v[y] * w[x]
# 随着游客遇到各种各样的糖果，愉悦值会不断上升，接下来有q条操作，操作类型如下
# 操作 0 x y : 第x号公园的糖果型号改成y
# 操作 1 x y : 游客从点x出发走过简单路径到达y，依次遇到每个公园的糖果，打印最终的愉悦值
# 1 <= n、m、q <= 10^5
# 1 <= v[i]、w[i] <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P4074
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code08_CandyPark2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'q': 'q', 'v': 'v', 'w': 'w', 'c': 'c', 'head': 'head', 'to': 'to', 'next': 'next', 'cntg': 'cntg', 'query': 'query', 'update': 'update', 'cntq': 'cntq', 'cntu': 'cntu', 'dep': 'dep', 'seg': 'seg', 'st': 'st', 'ed': 'ed', 'stjump': 'stjump', 'cntd': 'cntd', 'bi': 'bi', 'vis': 'vis', 'cnt': 'cnt', 'happy': 'happy', 'ans': 'ans', 'ufe': 'ufe', 'stacksize': 'stacksize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    MAXP = 0
    n = 0
    m = 0
    q = 0
    v = None
    w = None
    c = None
    head = None
    to = None
    next = None
    cntg = 0
    # 每条查询 : l、r、t、lca、id
    query = None
    # 每条修改 : pos、val
    update = None
    cntq = 0
    cntu = 0
    dep = None
    seg = None
    st = None
    ed = None
    stjump = None
    cntd = 0
    bi = None
    vis = None
    cnt = None
    happy = 0
    ans = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code08_CandyPark2.next, ((_java_obj_1 := Code08_CandyPark2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code08_CandyPark2.head[u])
        Code08_CandyPark2.to[Code08_CandyPark2.cntg] = jcast('int', v)
        Code08_CandyPark2.head[u] = jcast('int', Code08_CandyPark2.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code08_CandyPark2.dep[u] = jcast('int', jcast('int', jadd(Code08_CandyPark2.dep[fa], 1)))
        jset(Code08_CandyPark2.seg, ((_java_obj_4 := Code08_CandyPark2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], u)
        Code08_CandyPark2.st[u] = jcast('int', Code08_CandyPark2.cntd)
        jset(Code08_CandyPark2.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code08_CandyPark2.MAXP):
            jset(Code08_CandyPark2.stjump[u], p, Code08_CandyPark2.stjump[Code08_CandyPark2.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code08_CandyPark2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code08_CandyPark2.to[e])
            if (v != fa):
                Code08_CandyPark2.dfs1(v, u)
            e = jcast('int', Code08_CandyPark2.next[e])
        jset(Code08_CandyPark2.seg, ((_java_obj_7 := Code08_CandyPark2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        Code08_CandyPark2.ed[u] = jcast('int', Code08_CandyPark2.cntd)

    # 不会改迭代版，去看讲解118，详解了从递归版改迭代版
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
        jset(Code08_CandyPark2.ufe[Code08_CandyPark2.stacksize], 0, u)
        jset(Code08_CandyPark2.ufe[Code08_CandyPark2.stacksize], 1, f)
        jset(Code08_CandyPark2.ufe[Code08_CandyPark2.stacksize], 2, e)
        Code08_CandyPark2.stacksize = jcast('int', (Code08_CandyPark2.stacksize + 1))

    @staticmethod
    def pop():
        Code08_CandyPark2.stacksize = jcast('int', (Code08_CandyPark2.stacksize - 1))
        Code08_CandyPark2.u = jcast('int', Code08_CandyPark2.ufe[Code08_CandyPark2.stacksize][0])
        Code08_CandyPark2.f = jcast('int', Code08_CandyPark2.ufe[Code08_CandyPark2.stacksize][1])
        Code08_CandyPark2.e = jcast('int', Code08_CandyPark2.ufe[Code08_CandyPark2.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs2():
        Code08_CandyPark2.stacksize = jcast('int', 0)
        Code08_CandyPark2.push(1, 0, jcast('int', (-1)))
        while (Code08_CandyPark2.stacksize > 0):
            Code08_CandyPark2.pop()
            if (Code08_CandyPark2.e == jcast('int', (-1))):
                Code08_CandyPark2.dep[Code08_CandyPark2.u] = jcast('int', jcast('int', jadd(Code08_CandyPark2.dep[Code08_CandyPark2.f], 1)))
                jset(Code08_CandyPark2.seg, ((_java_obj_10 := Code08_CandyPark2), (_java_key_11 := 'cntd'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], Code08_CandyPark2.u)
                Code08_CandyPark2.st[Code08_CandyPark2.u] = jcast('int', Code08_CandyPark2.cntd)
                jset(Code08_CandyPark2.stjump[Code08_CandyPark2.u], 0, Code08_CandyPark2.f)
                p = jcast('int', 1)
                while (p < Code08_CandyPark2.MAXP):
                    jset(Code08_CandyPark2.stjump[Code08_CandyPark2.u], p, Code08_CandyPark2.stjump[Code08_CandyPark2.stjump[Code08_CandyPark2.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code08_CandyPark2.e = jcast('int', Code08_CandyPark2.head[Code08_CandyPark2.u])
            else:
                Code08_CandyPark2.e = jcast('int', Code08_CandyPark2.next[Code08_CandyPark2.e])
            if (Code08_CandyPark2.e != 0):
                Code08_CandyPark2.push(Code08_CandyPark2.u, Code08_CandyPark2.f, Code08_CandyPark2.e)
                if (Code08_CandyPark2.to[Code08_CandyPark2.e] != Code08_CandyPark2.f):
                    Code08_CandyPark2.push(Code08_CandyPark2.to[Code08_CandyPark2.e], Code08_CandyPark2.u, jcast('int', (-1)))
            else:
                jset(Code08_CandyPark2.seg, ((_java_obj_13 := Code08_CandyPark2), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], Code08_CandyPark2.u)
                Code08_CandyPark2.ed[Code08_CandyPark2.u] = jcast('int', Code08_CandyPark2.cntd)

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code08_CandyPark2.dep[a] < Code08_CandyPark2.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code08_CandyPark2.MAXP - 1)))
        while (p >= 0):
            if (Code08_CandyPark2.dep[Code08_CandyPark2.stjump[a][p]] >= Code08_CandyPark2.dep[b]):
                a = jcast('int', Code08_CandyPark2.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code08_CandyPark2.MAXP - 1)))
        while (p >= 0):
            if (Code08_CandyPark2.stjump[a][p] != Code08_CandyPark2.stjump[b][p]):
                a = jcast('int', Code08_CandyPark2.stjump[a][p])
                b = jcast('int', Code08_CandyPark2.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code08_CandyPark2.stjump[a][0])

    # 带修莫队经典排序
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code08_CandyPark2.bi[a[0]] != Code08_CandyPark2.bi[b[0]]):
                return jcast('int', jcast('int', (Code08_CandyPark2.bi[a[0]] - Code08_CandyPark2.bi[b[0]])))
            if (Code08_CandyPark2.bi[a[1]] != Code08_CandyPark2.bi[b[1]]):
                return jcast('int', jcast('int', (Code08_CandyPark2.bi[a[1]] - Code08_CandyPark2.bi[b[1]])))
            return jcast('int', jcast('int', (a[2] - b[2])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    # 窗口不管是加入还是删除node
    # 只要遇到node就翻转信息即可
    @staticmethod
    def invert(node):
        node = jcast('int', node)
        candy = jcast('int', Code08_CandyPark2.c[node])
        if Code08_CandyPark2.vis[node]:
            Code08_CandyPark2.happy = jcast('long', jcast('long', (Code08_CandyPark2.happy - jcast('long', (jcast('long', Code08_CandyPark2.v[candy]) * Code08_CandyPark2.w[((_java_obj_16 := Code08_CandyPark2.cnt), (_java_key_17 := candy), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (-1)))), _java_old_18)[4]])))))
        else:
            Code08_CandyPark2.happy = jcast('long', jcast('long', jadd(Code08_CandyPark2.happy, jcast('long', (jcast('long', Code08_CandyPark2.v[candy]) * Code08_CandyPark2.w[((_java_obj_19 := Code08_CandyPark2.cnt), (_java_key_20 := candy), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3]])))))
        Code08_CandyPark2.vis[node] = jcast('boolean', (not Code08_CandyPark2.vis[node]))

    # 上节课带修莫队的重要过程
    # tim为生效或者撤销的修改时间点，公园更换糖果
    @staticmethod
    def moveTime(tim):
        tim = jcast('int', tim)
        pos = jcast('int', Code08_CandyPark2.update[tim][0])
        oldVal = jcast('int', Code08_CandyPark2.c[pos])
        newVal = jcast('int', Code08_CandyPark2.update[tim][1])
        # 如果当前公园生效中
        if Code08_CandyPark2.vis[pos]:
            # 老糖果invert效果
            Code08_CandyPark2.invert(pos)
            # 新老糖果换位
            Code08_CandyPark2.c[pos] = jcast('int', newVal)
            jset(Code08_CandyPark2.update[tim], 1, oldVal)
            # 新糖果invert效果
            Code08_CandyPark2.invert(pos)
            # 如果当前公园不在生效中
        else:
            # 新老糖果换位即可
            Code08_CandyPark2.c[pos] = jcast('int', newVal)
            jset(Code08_CandyPark2.update[tim], 1, oldVal)

    @staticmethod
    def compute():
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        wint = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code08_CandyPark2.cntq):
            jobl = jcast('int', Code08_CandyPark2.query[i][0])
            jobr = jcast('int', Code08_CandyPark2.query[i][1])
            jobt = jcast('int', Code08_CandyPark2.query[i][2])
            lca = jcast('int', Code08_CandyPark2.query[i][3])
            id = jcast('int', Code08_CandyPark2.query[i][4])
            while (winl > jobl):
                Code08_CandyPark2.invert(Code08_CandyPark2.seg[(winl := jcast('int', (winl + (-1))))])
            while (winr < jobr):
                Code08_CandyPark2.invert(Code08_CandyPark2.seg[(winr := jcast('int', (winr + (1))))])
            while (winl < jobl):
                Code08_CandyPark2.invert(Code08_CandyPark2.seg[((_java_old_22 := winl), (winl := jcast('int', (winl + (1)))), _java_old_22)[2]])
            while (winr > jobr):
                Code08_CandyPark2.invert(Code08_CandyPark2.seg[((_java_old_23 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_23)[2]])
            while (wint < jobt):
                Code08_CandyPark2.moveTime((wint := jcast('int', (wint + (1)))))
            while (wint > jobt):
                Code08_CandyPark2.moveTime(((_java_old_24 := wint), (wint := jcast('int', (wint + (-1)))), _java_old_24)[2])
            if (lca > 0):
                Code08_CandyPark2.invert(lca)
            Code08_CandyPark2.ans[id] = jcast('long', Code08_CandyPark2.happy)
            if (lca > 0):
                Code08_CandyPark2.invert(lca)
            i = jcast('int', (i + 1))

    @staticmethod
    def prapare():
        blen = jcast('int', jstatic('Math', 'max', 1, jcast('int', jstatic('Math', 'pow', Code08_CandyPark2.cntd, jdiv(2.0, 3)))))
        i = jcast('int', 1)
        while (i <= Code08_CandyPark2.cntd):
            Code08_CandyPark2.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code08_CandyPark2.query, 1, jcast('int', jadd(Code08_CandyPark2.cntq, 1)), Code08_CandyPark2.QueryCmp())

    @staticmethod
    def main(args):
        in_ = Code08_CandyPark2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code08_CandyPark2.n = jcast('int', jcall(in_, 'nextInt'))
        Code08_CandyPark2.m = jcast('int', jcall(in_, 'nextInt'))
        Code08_CandyPark2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code08_CandyPark2.m):
            jset(Code08_CandyPark2.v, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code08_CandyPark2.n):
            jset(Code08_CandyPark2.w, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code08_CandyPark2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code08_CandyPark2.addEdge(u, v)
            Code08_CandyPark2.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code08_CandyPark2.n):
            jset(Code08_CandyPark2.c, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code08_CandyPark2.dfs2()
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        while (i <= Code08_CandyPark2.q):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            if (op == 0):
                Code08_CandyPark2.cntu = jcast('int', (Code08_CandyPark2.cntu + 1))
                jset(Code08_CandyPark2.update[Code08_CandyPark2.cntu], 0, x)
                jset(Code08_CandyPark2.update[Code08_CandyPark2.cntu], 1, y)
            else:
                if (Code08_CandyPark2.st[x] > Code08_CandyPark2.st[y]):
                    tmp = jcast('int', x)
                    x = jcast('int', y)
                    y = jcast('int', tmp)
                xylca = jcast('int', Code08_CandyPark2.lca(x, y))
                if (x == xylca):
                    jset(Code08_CandyPark2.query[((_java_obj_25 := Code08_CandyPark2), (_java_key_26 := 'cntq'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3]], 0, Code08_CandyPark2.st[x])
                    jset(Code08_CandyPark2.query[Code08_CandyPark2.cntq], 1, Code08_CandyPark2.st[y])
                    jset(Code08_CandyPark2.query[Code08_CandyPark2.cntq], 2, Code08_CandyPark2.cntu)
                    jset(Code08_CandyPark2.query[Code08_CandyPark2.cntq], 3, 0)
                    jset(Code08_CandyPark2.query[Code08_CandyPark2.cntq], 4, Code08_CandyPark2.cntq)
                else:
                    jset(Code08_CandyPark2.query[((_java_obj_28 := Code08_CandyPark2), (_java_key_29 := 'cntq'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))))[3]], 0, Code08_CandyPark2.ed[x])
                    jset(Code08_CandyPark2.query[Code08_CandyPark2.cntq], 1, Code08_CandyPark2.st[y])
                    jset(Code08_CandyPark2.query[Code08_CandyPark2.cntq], 2, Code08_CandyPark2.cntu)
                    jset(Code08_CandyPark2.query[Code08_CandyPark2.cntq], 3, xylca)
                    jset(Code08_CandyPark2.query[Code08_CandyPark2.cntq], 4, Code08_CandyPark2.cntq)
            i = jcast('int', (i + 1))
        Code08_CandyPark2.prapare()
        Code08_CandyPark2.compute()
        i = jcast('int', 1)
        while (i <= Code08_CandyPark2.cntq):
            jcall(out, 'println', Code08_CandyPark2.ans[i])
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
            raise TypeError("No matching overload for Code08_CandyPark2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code08_CandyPark2.MAXN = jcast('int', 100001)
Code08_CandyPark2.MAXP = jcast('int', 20)
Code08_CandyPark2.n = jcast('int', 0)
Code08_CandyPark2.m = jcast('int', 0)
Code08_CandyPark2.q = jcast('int', 0)
Code08_CandyPark2.v = jarray('int', [Code08_CandyPark2.MAXN])
Code08_CandyPark2.w = jarray('int', [Code08_CandyPark2.MAXN])
Code08_CandyPark2.c = jarray('int', [Code08_CandyPark2.MAXN])
Code08_CandyPark2.head = jarray('int', [Code08_CandyPark2.MAXN])
Code08_CandyPark2.to = jarray('int', [jcast('int', (Code08_CandyPark2.MAXN << (1 & 31)))])
Code08_CandyPark2.next = jarray('int', [jcast('int', (Code08_CandyPark2.MAXN << (1 & 31)))])
Code08_CandyPark2.cntg = jcast('int', 0)
Code08_CandyPark2.query = jarray('int', [Code08_CandyPark2.MAXN, 5])
Code08_CandyPark2.update = jarray('int', [Code08_CandyPark2.MAXN, 2])
Code08_CandyPark2.cntq = jcast('int', 0)
Code08_CandyPark2.cntu = jcast('int', 0)
Code08_CandyPark2.dep = jarray('int', [Code08_CandyPark2.MAXN])
Code08_CandyPark2.seg = jarray('int', [jcast('int', (Code08_CandyPark2.MAXN << (1 & 31)))])
Code08_CandyPark2.st = jarray('int', [Code08_CandyPark2.MAXN])
Code08_CandyPark2.ed = jarray('int', [Code08_CandyPark2.MAXN])
Code08_CandyPark2.stjump = jarray('int', [Code08_CandyPark2.MAXN, Code08_CandyPark2.MAXP])
Code08_CandyPark2.cntd = jcast('int', 0)
Code08_CandyPark2.bi = jarray('int', [jcast('int', (Code08_CandyPark2.MAXN << (1 & 31)))])
Code08_CandyPark2.vis = jarray('boolean', [Code08_CandyPark2.MAXN])
Code08_CandyPark2.cnt = jarray('int', [Code08_CandyPark2.MAXN])
Code08_CandyPark2.happy = jcast('long', 0)
Code08_CandyPark2.ans = jarray('long', [Code08_CandyPark2.MAXN])
Code08_CandyPark2.ufe = jarray('int', [Code08_CandyPark2.MAXN, 3])
Code08_CandyPark2.stacksize = jcast('int', 0)
Code08_CandyPark2.u = jcast('int', 0)
Code08_CandyPark2.f = jcast('int', 0)
Code08_CandyPark2.e = jcast('int', 0)

if __name__ == '__main__':
    Code08_CandyPark2.main([])
