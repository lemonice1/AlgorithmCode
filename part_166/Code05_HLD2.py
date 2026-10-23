# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 树上分块模版题，重链序列分块，Python版
# 一共有n个节点，每个节点有点权，给定n-1条边，所有节点连成一棵树
# 接下来有m条操作，每条操作都要打印两个答案，描述如下
# 操作 k x1 y1 x2 y2 .. (一共k个点对)
# 每个点对(x, y)，在树上都有从x到y的路径，那么k个点对就有k条路径
# 先打印k条路径上不同点权的数量，再打印点权集合中没有出现的最小非负数(mex)
# 1 <= n、点对总数 <= 10^5    点权 <= 30000
# 题目要求强制在线，具体规则可以打开测试链接查看
# 测试链接 : https://www.luogu.com.cn/problem/P3603
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_HLD2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'MAXV': 'MAXV', 'n': 'n', 'm': 'm', 'f': 'f', 'k': 'k', 'arr': 'arr', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top', 'dfn': 'dfn', 'val': 'val', 'cntd': 'cntd', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'bl': 'bl', 'br': 'br', 'bitSet': 'bitSet', 'ans': 'ans', 'fse': 'fse', 'stacksize': 'stacksize', 'first': 'first', 'second': 'second', 'edge': 'edge'}
    MAXN = 0
    MAXB = 0
    MAXV = 0
    n = 0
    m = 0
    f = 0
    k = 0
    arr = None
    # 链式前向星
    head = None
    next = None
    to = None
    cntg = 0
    # 重链剖分
    fa = None
    dep = None
    siz = None
    son = None
    top = None
    dfn = None
    val = None
    cntd = 0
    # 分块
    blen = 0
    bnum = 0
    bi = None
    bl = None
    br = None
    bitSet = None
    ans = None
    class BitSet:
        __java_fields__ = {'len': 'len', 'set': 'set'}
        # len：实例字段，在构造函数中初始化。
        # set：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.len = jcast('int', jcast('int', jdiv(jcast('int', jadd(Code05_HLD2.MAXV, 31)), 32)))
            self.set = jarray('int', [self.len])

        def clear(self):
            i = jcast('int', 0)
            while (i < self.len):
                self.set[i] = jcast('int', 0)
                i = jcast('int', (i + 1))

        def setOne(self, v):
            v = jcast('int', v)
            ((_java_obj_1 := self.set), (_java_key_2 := jcast('int', jdiv(v, 32))), jset(_java_obj_1, _java_key_2, jcast('int', (jget(_java_obj_1, _java_key_2) | jcast('int', (1 << (jcast('int', jmod(v, 32)) & 31)))))))[2]

        def or_(self, obj):
            i = jcast('int', 0)
            while (i < self.len):
                self.set[i] = jcast('int', jcast('int', (self.set[i] | jget(obj, 'set')[i])))
                i = jcast('int', (i + 1))

        def getOnes(self):
            ans = jcast('int', 0)
            for x in self.set:
                ans = jcast('int', jcast('int', jadd(ans, jstatic('Integer', 'bitCount', x))))
            return jcast('int', ans)

        def mex(self):
            i = jcast('int', 0)
            inv = 0
            while (i < self.len):
                inv = jcast('int', jcast('int', (~self.set[i])))
                if (inv != 0):
                    return jcast('int', jcast('int', jadd(jcast('int', (i * 32)), jstatic('Integer', 'numberOfTrailingZeros', inv))))
                i = jcast('int', (i + 1))
            return jcast('int', jcast('int', (-1)))

        def __init__(self, *args, _java_ctor=None):
            self.len = jcast('int', 0)
            self.set = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_HLD2.BitSet.BitSet")


    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_HLD2.next, ((_java_obj_3 := Code05_HLD2), (_java_key_4 := 'cntg'), (_java_old_5 := jget(_java_obj_3, _java_key_4)), jset(_java_obj_3, _java_key_4, jcast('int', (_java_old_5 + (1)))))[3], Code05_HLD2.head[u])
        Code05_HLD2.to[Code05_HLD2.cntg] = jcast('int', v)
        Code05_HLD2.head[u] = jcast('int', Code05_HLD2.cntg)

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code05_HLD2.fa[u] = jcast('int', f)
        Code05_HLD2.dep[u] = jcast('int', jcast('int', jadd(Code05_HLD2.dep[f], 1)))
        Code05_HLD2.siz[u] = jcast('int', 1)
        e = jcast('int', Code05_HLD2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code05_HLD2.to[e])
            if (v != f):
                Code05_HLD2.dfs1(v, u)
            e = jcast('int', Code05_HLD2.next[e])
        e = jcast('int', Code05_HLD2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code05_HLD2.to[e])
            if (v != f):
                Code05_HLD2.siz[u] = jcast('int', jcast('int', jadd(Code05_HLD2.siz[u], Code05_HLD2.siz[v])))
                if ((Code05_HLD2.son[u] == 0) or (Code05_HLD2.siz[Code05_HLD2.son[u]] < Code05_HLD2.siz[v])):
                    Code05_HLD2.son[u] = jcast('int', v)
            e = jcast('int', Code05_HLD2.next[e])

    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code05_HLD2.top[u] = jcast('int', t)
        jset(Code05_HLD2.dfn, u, ((_java_obj_6 := Code05_HLD2), (_java_key_7 := 'cntd'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))))[3])
        Code05_HLD2.val[Code05_HLD2.cntd] = jcast('int', Code05_HLD2.arr[u])
        if (Code05_HLD2.son[u] == 0):
            return
        Code05_HLD2.dfs2(Code05_HLD2.son[u], t)
        e = jcast('int', Code05_HLD2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code05_HLD2.to[e])
            if ((v != Code05_HLD2.fa[u]) and (v != Code05_HLD2.son[u])):
                Code05_HLD2.dfs2(v, v)
            e = jcast('int', Code05_HLD2.next[e])

    # 不会改迭代版，去看讲解118，详解了从递归版改迭代版
    fse = None
    stacksize = 0
    first = 0
    second = 0
    edge = 0
    @staticmethod
    def push(fir, sec, edg):
        fir = jcast('int', fir)
        sec = jcast('int', sec)
        edg = jcast('int', edg)
        jset(Code05_HLD2.fse[Code05_HLD2.stacksize], 0, fir)
        jset(Code05_HLD2.fse[Code05_HLD2.stacksize], 1, sec)
        jset(Code05_HLD2.fse[Code05_HLD2.stacksize], 2, edg)
        Code05_HLD2.stacksize = jcast('int', (Code05_HLD2.stacksize + 1))

    @staticmethod
    def pop():
        Code05_HLD2.stacksize = jcast('int', (Code05_HLD2.stacksize - 1))
        Code05_HLD2.first = jcast('int', Code05_HLD2.fse[Code05_HLD2.stacksize][0])
        Code05_HLD2.second = jcast('int', Code05_HLD2.fse[Code05_HLD2.stacksize][1])
        Code05_HLD2.edge = jcast('int', Code05_HLD2.fse[Code05_HLD2.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs3():
        Code05_HLD2.stacksize = jcast('int', 0)
        Code05_HLD2.push(1, 0, jcast('int', (-1)))
        while (Code05_HLD2.stacksize > 0):
            Code05_HLD2.pop()
            if (Code05_HLD2.edge == jcast('int', (-1))):
                Code05_HLD2.fa[Code05_HLD2.first] = jcast('int', Code05_HLD2.second)
                Code05_HLD2.dep[Code05_HLD2.first] = jcast('int', jcast('int', jadd(Code05_HLD2.dep[Code05_HLD2.second], 1)))
                Code05_HLD2.siz[Code05_HLD2.first] = jcast('int', 1)
                Code05_HLD2.edge = jcast('int', Code05_HLD2.head[Code05_HLD2.first])
            else:
                Code05_HLD2.edge = jcast('int', Code05_HLD2.next[Code05_HLD2.edge])
            if (Code05_HLD2.edge != 0):
                Code05_HLD2.push(Code05_HLD2.first, Code05_HLD2.second, Code05_HLD2.edge)
                if (Code05_HLD2.to[Code05_HLD2.edge] != Code05_HLD2.second):
                    Code05_HLD2.push(Code05_HLD2.to[Code05_HLD2.edge], Code05_HLD2.first, jcast('int', (-1)))
            else:
                e = jcast('int', Code05_HLD2.head[Code05_HLD2.first])
                v = 0
                while (e > 0):
                    v = jcast('int', Code05_HLD2.to[e])
                    if (v != Code05_HLD2.second):
                        Code05_HLD2.siz[Code05_HLD2.first] = jcast('int', jcast('int', jadd(Code05_HLD2.siz[Code05_HLD2.first], Code05_HLD2.siz[v])))
                        if ((Code05_HLD2.son[Code05_HLD2.first] == 0) or (Code05_HLD2.siz[Code05_HLD2.son[Code05_HLD2.first]] < Code05_HLD2.siz[v])):
                            Code05_HLD2.son[Code05_HLD2.first] = jcast('int', v)
                    e = jcast('int', Code05_HLD2.next[e])

    # dfs2的迭代版
    @staticmethod
    def dfs4():
        Code05_HLD2.stacksize = jcast('int', 0)
        Code05_HLD2.push(1, 1, jcast('int', (-1)))
        while (Code05_HLD2.stacksize > 0):
            try:
                Code05_HLD2.pop()
                if (Code05_HLD2.edge == jcast('int', (-1))):
                    Code05_HLD2.top[Code05_HLD2.first] = jcast('int', Code05_HLD2.second)
                    jset(Code05_HLD2.dfn, Code05_HLD2.first, ((_java_obj_10 := Code05_HLD2), (_java_key_11 := 'cntd'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
                    Code05_HLD2.val[Code05_HLD2.cntd] = jcast('int', Code05_HLD2.arr[Code05_HLD2.first])
                    if (Code05_HLD2.son[Code05_HLD2.first] == 0):
                        raise JContinue(None)
                    Code05_HLD2.push(Code05_HLD2.first, Code05_HLD2.second, jcast('int', (-2)))
                    Code05_HLD2.push(Code05_HLD2.son[Code05_HLD2.first], Code05_HLD2.second, jcast('int', (-1)))
                    raise JContinue(None)
                else:
                    if (Code05_HLD2.edge == jcast('int', (-2))):
                        Code05_HLD2.edge = jcast('int', Code05_HLD2.head[Code05_HLD2.first])
                    else:
                        Code05_HLD2.edge = jcast('int', Code05_HLD2.next[Code05_HLD2.edge])
                if (Code05_HLD2.edge != 0):
                    Code05_HLD2.push(Code05_HLD2.first, Code05_HLD2.second, Code05_HLD2.edge)
                    if ((Code05_HLD2.to[Code05_HLD2.edge] != Code05_HLD2.fa[Code05_HLD2.first]) and (Code05_HLD2.to[Code05_HLD2.edge] != Code05_HLD2.son[Code05_HLD2.first])):
                        Code05_HLD2.push(Code05_HLD2.to[Code05_HLD2.edge], Code05_HLD2.to[Code05_HLD2.edge], jcast('int', (-1)))
            except JContinue as _java_control_9:
                if _java_control_9.label not in (None,):
                    raise
            except JBreak as _java_control_9:
                if _java_control_9.label not in (None,):
                    raise
                break

    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (Code05_HLD2.bi[l] == Code05_HLD2.bi[r]):
            i = jcast('int', l)
            while (i <= r):
                jcall(Code05_HLD2.ans, 'setOne', Code05_HLD2.val[i])
                i = jcast('int', (i + 1))
        else:
            i = jcast('int', l)
            while (i <= Code05_HLD2.br[Code05_HLD2.bi[l]]):
                jcall(Code05_HLD2.ans, 'setOne', Code05_HLD2.val[i])
                i = jcast('int', (i + 1))
            i = jcast('int', Code05_HLD2.bl[Code05_HLD2.bi[r]])
            while (i <= r):
                jcall(Code05_HLD2.ans, 'setOne', Code05_HLD2.val[i])
                i = jcast('int', (i + 1))
            i = jcast('int', jcast('int', jadd(Code05_HLD2.bi[l], 1)))
            while (i <= jcast('int', (Code05_HLD2.bi[r] - 1))):
                jcall(Code05_HLD2.ans, 'or_', Code05_HLD2.bitSet[i])
                i = jcast('int', (i + 1))

    @staticmethod
    def updateAns(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        while (Code05_HLD2.top[x] != Code05_HLD2.top[y]):
            if (Code05_HLD2.dep[Code05_HLD2.top[x]] < Code05_HLD2.dep[Code05_HLD2.top[y]]):
                tmp = jcast('int', x)
                x = jcast('int', y)
                y = jcast('int', tmp)
            Code05_HLD2.query(Code05_HLD2.dfn[Code05_HLD2.top[x]], Code05_HLD2.dfn[x])
            x = jcast('int', Code05_HLD2.fa[Code05_HLD2.top[x]])
        Code05_HLD2.query(jstatic('Math', 'min', Code05_HLD2.dfn[x], Code05_HLD2.dfn[y]), jstatic('Math', 'max', Code05_HLD2.dfn[x], Code05_HLD2.dfn[y]))

    @staticmethod
    def prepare():
        Code05_HLD2.dfs3()
        Code05_HLD2.dfs4()
        Code05_HLD2.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', jcast('int', (Code05_HLD2.n * 20)))))
        Code05_HLD2.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code05_HLD2.n, Code05_HLD2.blen)) - 1)), Code05_HLD2.blen)))
        i = jcast('int', 1)
        while (i <= Code05_HLD2.n):
            Code05_HLD2.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code05_HLD2.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_HLD2.bnum):
            Code05_HLD2.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code05_HLD2.blen)), 1)))
            jset(Code05_HLD2.br, i, jstatic('Math', 'min', jcast('int', (i * Code05_HLD2.blen)), Code05_HLD2.n))
            jset(Code05_HLD2.bitSet, i, Code05_HLD2.BitSet(_java_ctor=0))
            j = jcast('int', Code05_HLD2.bl[i])
            while (j <= Code05_HLD2.br[i]):
                jcall(Code05_HLD2.bitSet[i], 'setOne', Code05_HLD2.val[j])
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code05_HLD2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_HLD2.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_HLD2.m = jcast('int', jcall(in_, 'nextInt'))
        Code05_HLD2.f = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_HLD2.n):
            jset(Code05_HLD2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code05_HLD2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code05_HLD2.addEdge(u, v)
            Code05_HLD2.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code05_HLD2.prepare()
        i = jcast('int', 1)
        lastAns = jcast('int', 0)
        while (i <= Code05_HLD2.m):
            jcall(Code05_HLD2.ans, 'clear')
            Code05_HLD2.k = jcast('int', jcall(in_, 'nextInt'))
            j = jcast('int', 1)
            x = 0
            y = 0
            while (j <= Code05_HLD2.k):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                if (Code05_HLD2.f > 0):
                    x = jcast('int', jcast('int', (x ^ lastAns)))
                    y = jcast('int', jcast('int', (y ^ lastAns)))
                Code05_HLD2.updateAns(x, y)
                j = jcast('int', (j + 1))
            ans1 = jcast('int', jcall(Code05_HLD2.ans, 'getOnes'))
            ans2 = jcast('int', jcall(Code05_HLD2.ans, 'mex'))
            jcall(out, 'println', jadd(jadd(ans1, ' '), ans2))
            lastAns = jcast('int', jcast('int', jadd(ans1, ans2)))
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
            return jcast('int', self.buffer[((_java_obj_13 := self), (_java_key_14 := 'ptr'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))), _java_old_15)[4]])

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
            self.buffer = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_HLD2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_HLD2.MAXN = jcast('int', 100001)
Code05_HLD2.MAXB = jcast('int', 401)
Code05_HLD2.MAXV = jcast('int', 30001)
Code05_HLD2.n = jcast('int', 0)
Code05_HLD2.m = jcast('int', 0)
Code05_HLD2.f = jcast('int', 0)
Code05_HLD2.k = jcast('int', 0)
Code05_HLD2.arr = jarray('int', [Code05_HLD2.MAXN])
Code05_HLD2.head = jarray('int', [Code05_HLD2.MAXN])
Code05_HLD2.next = jarray('int', [jcast('int', (Code05_HLD2.MAXN << (1 & 31)))])
Code05_HLD2.to = jarray('int', [jcast('int', (Code05_HLD2.MAXN << (1 & 31)))])
Code05_HLD2.cntg = jcast('int', 0)
Code05_HLD2.fa = jarray('int', [Code05_HLD2.MAXN])
Code05_HLD2.dep = jarray('int', [Code05_HLD2.MAXN])
Code05_HLD2.siz = jarray('int', [Code05_HLD2.MAXN])
Code05_HLD2.son = jarray('int', [Code05_HLD2.MAXN])
Code05_HLD2.top = jarray('int', [Code05_HLD2.MAXN])
Code05_HLD2.dfn = jarray('int', [Code05_HLD2.MAXN])
Code05_HLD2.val = jarray('int', [Code05_HLD2.MAXN])
Code05_HLD2.cntd = jcast('int', 0)
Code05_HLD2.blen = jcast('int', 0)
Code05_HLD2.bnum = jcast('int', 0)
Code05_HLD2.bi = jarray('int', [Code05_HLD2.MAXN])
Code05_HLD2.bl = jarray('int', [Code05_HLD2.MAXB])
Code05_HLD2.br = jarray('int', [Code05_HLD2.MAXB])
Code05_HLD2.bitSet = jarray('BitSet', [Code05_HLD2.MAXB])
Code05_HLD2.ans = Code05_HLD2.BitSet(_java_ctor=0)
Code05_HLD2.fse = jarray('int', [Code05_HLD2.MAXN, 3])
Code05_HLD2.stacksize = jcast('int', 0)
Code05_HLD2.first = jcast('int', 0)
Code05_HLD2.second = jcast('int', 0)
Code05_HLD2.edge = jcast('int', 0)

if __name__ == '__main__':
    Code05_HLD2.main([])
