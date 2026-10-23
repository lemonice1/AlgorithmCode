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

# 八纵八横，Python版
# 一共有n个点，给定m条边，每条边的边权，用01字符串表达，初始时就保证图连通
# 初始的m条边永不删除，接下来有q条操作，每种操作是如下三种类型中的一种
# 操作 Add x y z  : 加入点x到点y的边，边权是z，z为01字符串，第k条添加操作，边的编号为k
# 操作 Cancel k   : 删除编号为k的边
# 操作 Change k z : 编号为k的边，边权修改成z，z为01字符串
# 从1号点出发，最后回到1号点，边随便走，沿途所有边的边权异或起来
# 打印只有初始m条边的情况下，异或最大值为多少，每一条操作结束后，都打印异或最大值为多少
# 1 <= n、m <= 500    0 <= q <= 1000    1 <= 边权字符串长度 <= 1000
# 测试链接 : https://www.luogu.com.cn/problem/P3733
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_EightVerticalHorizontal2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXQ': 'MAXQ', 'MAXT': 'MAXT', 'BIT': 'BIT', 'INT_BIT': 'INT_BIT', 'n': 'n', 'm': 'm', 'q': 'q', 'x': 'x', 'y': 'y', 'w': 'w', 'edgeCnt': 'edgeCnt', 'last': 'last', 'basis': 'basis', 'inspos': 'inspos', 'basiz': 'basiz', 'father': 'father', 'eor': 'eor', 'head': 'head', 'next': 'next', 'tox': 'tox', 'toy': 'toy', 'tow': 'tow', 'cnt': 'cnt', 'ans': 'ans'}
    MAXN = 0
    MAXQ = 0
    MAXT = 0
    BIT = 0
    INT_BIT = 0
    # 位图
    class BitSet:
        __java_fields__ = {'len': 'len', 'arr': 'arr'}
        # len：实例字段，在构造函数中初始化。
        # arr：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.len = jcast('int', jcast('int', jadd(jcast('int', jdiv(Code05_EightVerticalHorizontal2.BIT, Code05_EightVerticalHorizontal2.INT_BIT)), 1)))
            self.arr = jarray('int', [self.len])

        def _java_init_1(self, s):
            self.len = jcast('int', jcast('int', jadd(jcast('int', jdiv(Code05_EightVerticalHorizontal2.BIT, Code05_EightVerticalHorizontal2.INT_BIT)), 1)))
            self.arr = jarray('int', [self.len])
            i = jcast('int', 0)
            j = jcast('int', jcast('int', (jcall(s, 'length') - 1)))
            while (i < jcall(s, 'length')):
                self.set(i, jcast('int', (jcall(s, 'charAt', j) - jchar('0'))))
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))

        # 返回第i位的状态
        def get(self, i):
            i = jcast('int', i)
            return jcast('int', jcast('int', (jcast('int', (self.arr[jcast('int', jdiv(i, Code05_EightVerticalHorizontal2.INT_BIT))] >> (jcast('int', jmod(i, Code05_EightVerticalHorizontal2.INT_BIT)) & 31))) & 1)))

        # 设置第i位的状态
        def set(self, i, v):
            i = jcast('int', i)
            v = jcast('int', v)
            if (v == 0):
                ((_java_obj_1 := self.arr), (_java_key_2 := jcast('int', jdiv(i, Code05_EightVerticalHorizontal2.INT_BIT))), jset(_java_obj_1, _java_key_2, jcast('int', (jget(_java_obj_1, _java_key_2) & jcast('int', (~jcast('int', (1 << (jcast('int', jmod(i, Code05_EightVerticalHorizontal2.INT_BIT)) & 31)))))))))[2]
            else:
                ((_java_obj_3 := self.arr), (_java_key_4 := jcast('int', jdiv(i, Code05_EightVerticalHorizontal2.INT_BIT))), jset(_java_obj_3, _java_key_4, jcast('int', (jget(_java_obj_3, _java_key_4) | jcast('int', (1 << (jcast('int', jmod(i, Code05_EightVerticalHorizontal2.INT_BIT)) & 31)))))))[2]

        # 异或other每一位
        def eor(self, other):
            i = jcast('int', 0)
            while (i < self.len):
                self.arr[i] = jcast('int', jcast('int', (self.arr[i] ^ jget(other, 'arr')[i])))
                i = jcast('int', (i + 1))

        # 清空每一位
        def clear(self):
            i = jcast('int', 0)
            while (i < self.len):
                self.arr[i] = jcast('int', 0)
                i = jcast('int', (i + 1))

        def __init__(self, *args, _java_ctor=None):
            self.len = jcast('int', 0)
            self.arr = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[], ['String']], [False, False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            if _java_choice == 1:
                return self._java_init_1(*args)
            raise TypeError("No matching overload for Code05_EightVerticalHorizontal2.BitSet.BitSet")


    n = 0
    m = 0
    q = 0
    x = None
    y = None
    w = None
    edgeCnt = 0
    last = None
    # 可撤销线性基
    basis = None
    inspos = None
    basiz = 0
    # 经典带权并查集，只做扁平化，不做小挂大
    father = None
    eor = None
    # 时间轴线段树上的区间任务列表
    head = None
    next = None
    tox = None
    toy = None
    tow = None
    cnt = 0
    # 每一步的最大异或值
    ans = None
    # num插入线性基
    @staticmethod
    def insert(num):
        i = jcast('int', Code05_EightVerticalHorizontal2.BIT)
        while (i >= 0):
            if (jcall(num, 'get', i) == 1):
                if (jcall(Code05_EightVerticalHorizontal2.basis[i], 'get', i) == 0):
                    Code05_EightVerticalHorizontal2.basis[i] = num
                    jset(Code05_EightVerticalHorizontal2.inspos, ((_java_obj_5 := Code05_EightVerticalHorizontal2), (_java_key_6 := 'basiz'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))), _java_old_7)[4], i)
                    return
                jcall(num, 'eor', Code05_EightVerticalHorizontal2.basis[i])
            i = jcast('int', (i - 1))

    # 0这个数字结合线性基，得到的最大异或值返回
    @staticmethod
    def maxEor():
        ans = Code05_EightVerticalHorizontal2.BitSet(_java_ctor=0)
        i = jcast('int', Code05_EightVerticalHorizontal2.BIT)
        while (i >= 0):
            if ((jcall(ans, 'get', i) == 0) and (jcall(Code05_EightVerticalHorizontal2.basis[i], 'get', i) == 1)):
                jcall(ans, 'eor', Code05_EightVerticalHorizontal2.basis[i])
            i = jcast('int', (i - 1))
        return ans

    # 线性基的撤销
    @staticmethod
    def cancel(oldsiz):
        oldsiz = jcast('int', oldsiz)
        while (Code05_EightVerticalHorizontal2.basiz > oldsiz):
            jcall(Code05_EightVerticalHorizontal2.basis[Code05_EightVerticalHorizontal2.inspos[((_java_obj_8 := Code05_EightVerticalHorizontal2), (_java_key_9 := 'basiz'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (-1)))))[3]]], 'clear')

    # 扁平化优化，find的同时修改eor，就是经典的带权并查集
    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code05_EightVerticalHorizontal2.father[i]):
            tmp = jcast('int', Code05_EightVerticalHorizontal2.father[i])
            jset(Code05_EightVerticalHorizontal2.father, i, Code05_EightVerticalHorizontal2.find(tmp))
            jcall(Code05_EightVerticalHorizontal2.eor[i], 'eor', Code05_EightVerticalHorizontal2.eor[tmp])
        return jcast('int', Code05_EightVerticalHorizontal2.father[i])

    @staticmethod
    def getEor(i):
        i = jcast('int', i)
        Code05_EightVerticalHorizontal2.find(i)
        return Code05_EightVerticalHorizontal2.eor[i]

    @staticmethod
    def union(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        fu = jcast('int', Code05_EightVerticalHorizontal2.find(u))
        fv = jcast('int', Code05_EightVerticalHorizontal2.find(v))
        weight = Code05_EightVerticalHorizontal2.BitSet(_java_ctor=0)
        jcall(weight, 'eor', Code05_EightVerticalHorizontal2.getEor(u))
        jcall(weight, 'eor', Code05_EightVerticalHorizontal2.getEor(v))
        jcall(weight, 'eor', w)
        if (fu == fv):
            Code05_EightVerticalHorizontal2.insert(weight)
        else:
            Code05_EightVerticalHorizontal2.father[fv] = jcast('int', fu)
            Code05_EightVerticalHorizontal2.eor[fv] = weight

    @staticmethod
    def addEdge(i, x, y, w):
        i = jcast('int', i)
        x = jcast('int', x)
        y = jcast('int', y)
        jset(Code05_EightVerticalHorizontal2.next, ((_java_obj_11 := Code05_EightVerticalHorizontal2), (_java_key_12 := 'cnt'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))))[3], Code05_EightVerticalHorizontal2.head[i])
        Code05_EightVerticalHorizontal2.tox[Code05_EightVerticalHorizontal2.cnt] = jcast('int', x)
        Code05_EightVerticalHorizontal2.toy[Code05_EightVerticalHorizontal2.cnt] = jcast('int', y)
        Code05_EightVerticalHorizontal2.tow[Code05_EightVerticalHorizontal2.cnt] = w
        Code05_EightVerticalHorizontal2.head[i] = jcast('int', Code05_EightVerticalHorizontal2.cnt)

    @staticmethod
    def add(jobl, jobr, jobx, joby, jobw, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobx = jcast('int', jobx)
        joby = jcast('int', joby)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code05_EightVerticalHorizontal2.addEdge(i, jobx, joby, jobw)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code05_EightVerticalHorizontal2.add(jobl, jobr, jobx, joby, jobw, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code05_EightVerticalHorizontal2.add(jobl, jobr, jobx, joby, jobw, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def dfs(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        oldsiz = jcast('int', Code05_EightVerticalHorizontal2.basiz)
        e = jcast('int', Code05_EightVerticalHorizontal2.head[i])
        while (e > 0):
            Code05_EightVerticalHorizontal2.union(Code05_EightVerticalHorizontal2.tox[e], Code05_EightVerticalHorizontal2.toy[e], Code05_EightVerticalHorizontal2.tow[e])
            e = jcast('int', Code05_EightVerticalHorizontal2.next[e])
        if (l == r):
            jset(Code05_EightVerticalHorizontal2.ans, l, Code05_EightVerticalHorizontal2.maxEor())
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            Code05_EightVerticalHorizontal2.dfs(l, mid, jcast('int', (i << (1 & 31))))
            Code05_EightVerticalHorizontal2.dfs(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code05_EightVerticalHorizontal2.cancel(oldsiz)

    @staticmethod
    def print(bs, out):
        flag = jcast('boolean', False)
        i = jcast('int', Code05_EightVerticalHorizontal2.BIT)
        s = 0
        while (i >= 0):
            s = jcast('int', jcall(bs, 'get', i))
            if (s == 1):
                flag = jcast('boolean', True)
            if flag:
                jcall(out, 'print', s)
            i = jcast('int', (i - 1))
        if (not flag):
            jcall(out, 'print', 0)
        jcall(out, 'println')

    @staticmethod
    def main(args):
        in_ = Code05_EightVerticalHorizontal2.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_EightVerticalHorizontal2.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_EightVerticalHorizontal2.m = jcast('int', jcall(in_, 'nextInt'))
        Code05_EightVerticalHorizontal2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 0)
        while (i <= Code05_EightVerticalHorizontal2.BIT):
            jset(Code05_EightVerticalHorizontal2.basis, i, Code05_EightVerticalHorizontal2.BitSet(_java_ctor=0))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_EightVerticalHorizontal2.n):
            Code05_EightVerticalHorizontal2.father[i] = jcast('int', i)
            jset(Code05_EightVerticalHorizontal2.eor, i, Code05_EightVerticalHorizontal2.BitSet(_java_ctor=0))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_EightVerticalHorizontal2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = Code05_EightVerticalHorizontal2.BitSet(jcall(in_, 'nextString'), _java_ctor=1)
            Code05_EightVerticalHorizontal2.union(u, v, w)
            i = jcast('int', (i + 1))
        jset(Code05_EightVerticalHorizontal2.ans, 0, Code05_EightVerticalHorizontal2.maxEor())
        op = None
        i = jcast('int', 1)
        while (i <= Code05_EightVerticalHorizontal2.q):
            op = jcall(in_, 'nextString')
            if jcall(op, 'equals', 'Add'):
                Code05_EightVerticalHorizontal2.edgeCnt = jcast('int', (Code05_EightVerticalHorizontal2.edgeCnt + 1))
                jset(Code05_EightVerticalHorizontal2.x, Code05_EightVerticalHorizontal2.edgeCnt, jcall(in_, 'nextInt'))
                jset(Code05_EightVerticalHorizontal2.y, Code05_EightVerticalHorizontal2.edgeCnt, jcall(in_, 'nextInt'))
                jset(Code05_EightVerticalHorizontal2.w, Code05_EightVerticalHorizontal2.edgeCnt, Code05_EightVerticalHorizontal2.BitSet(jcall(in_, 'nextString'), _java_ctor=1))
                Code05_EightVerticalHorizontal2.last[Code05_EightVerticalHorizontal2.edgeCnt] = jcast('int', i)
            else:
                if jcall(op, 'equals', 'Cancel'):
                    k = jcast('int', jcall(in_, 'nextInt'))
                    Code05_EightVerticalHorizontal2.add(Code05_EightVerticalHorizontal2.last[k], jcast('int', (i - 1)), Code05_EightVerticalHorizontal2.x[k], Code05_EightVerticalHorizontal2.y[k], Code05_EightVerticalHorizontal2.w[k], 1, Code05_EightVerticalHorizontal2.q, 1)
                    Code05_EightVerticalHorizontal2.last[k] = jcast('int', 0)
                else:
                    k = jcast('int', jcall(in_, 'nextInt'))
                    Code05_EightVerticalHorizontal2.add(Code05_EightVerticalHorizontal2.last[k], jcast('int', (i - 1)), Code05_EightVerticalHorizontal2.x[k], Code05_EightVerticalHorizontal2.y[k], Code05_EightVerticalHorizontal2.w[k], 1, Code05_EightVerticalHorizontal2.q, 1)
                    jset(Code05_EightVerticalHorizontal2.w, k, Code05_EightVerticalHorizontal2.BitSet(jcall(in_, 'nextString'), _java_ctor=1))
                    Code05_EightVerticalHorizontal2.last[k] = jcast('int', i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_EightVerticalHorizontal2.edgeCnt):
            if (Code05_EightVerticalHorizontal2.last[i] != 0):
                Code05_EightVerticalHorizontal2.add(Code05_EightVerticalHorizontal2.last[i], Code05_EightVerticalHorizontal2.q, Code05_EightVerticalHorizontal2.x[i], Code05_EightVerticalHorizontal2.y[i], Code05_EightVerticalHorizontal2.w[i], 1, Code05_EightVerticalHorizontal2.q, 1)
            i = jcast('int', (i + 1))
        if (Code05_EightVerticalHorizontal2.q > 0):
            Code05_EightVerticalHorizontal2.dfs(1, Code05_EightVerticalHorizontal2.q, 1)
        i = jcast('int', 0)
        while (i <= Code05_EightVerticalHorizontal2.q):
            Code05_EightVerticalHorizontal2.print(Code05_EightVerticalHorizontal2.ans[i], out)
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'BUFFER_SIZE': 'BUFFER_SIZE', 'in': 'in_', 'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len'}
        BUFFER_SIZE = 0
        # in_：实例字段，在构造函数中初始化。
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.in_ = jget(System, 'in')
            self.buffer = jarray('byte', [Code05_EightVerticalHorizontal2.FastReader.BUFFER_SIZE])
            self.ptr = jcast('int', jset(self, 'len', 0))

        def hasNextByte(self):
            if (self.ptr < self.len):
                return jcast('boolean', True)
            self.ptr = jcast('int', 0)
            self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
            return jcast('boolean', (self.len > 0))

        def readByte(self):
            if (not self.hasNextByte()):
                return jcast('byte', jcast('int', (-1)))
            return jcast('byte', self.buffer[((_java_obj_14 := self), (_java_key_15 := 'ptr'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))), _java_old_16)[4]])

        def nextInt(self):
            num = jcast('int', 0)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                num = jcast('int', jcast('int', jadd(jcast('int', (num * 10)), jcast('int', (b - jchar('0'))))))
                b = jcast('byte', self.readByte())
            return jcast('int', (jcast('int', (-num)) if minus else num))

        def nextString(self):
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            sb = jnew('StringBuilder', 1000)
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                jcall(sb, 'append', jcast('char', b))
                b = jcast('byte', self.readByte())
            return jcall(sb, 'toString')

        def isWhitespace(self, b):
            b = jcast('byte', b)
            return jcast('boolean', ((((b == jchar(' ')) or (b == jchar('\n'))) or (b == jchar('\r'))) or (b == jchar('\t'))))

        def __init__(self, *args, _java_ctor=None):
            self.in_ = None
            self.buffer = None
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_EightVerticalHorizontal2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_EightVerticalHorizontal2.MAXN = jcast('int', 501)
Code05_EightVerticalHorizontal2.MAXQ = jcast('int', 1001)
Code05_EightVerticalHorizontal2.MAXT = jcast('int', 10001)
Code05_EightVerticalHorizontal2.BIT = jcast('int', 999)
Code05_EightVerticalHorizontal2.INT_BIT = jcast('int', 32)
Code05_EightVerticalHorizontal2.n = jcast('int', 0)
Code05_EightVerticalHorizontal2.m = jcast('int', 0)
Code05_EightVerticalHorizontal2.q = jcast('int', 0)
Code05_EightVerticalHorizontal2.x = jarray('int', [Code05_EightVerticalHorizontal2.MAXQ])
Code05_EightVerticalHorizontal2.y = jarray('int', [Code05_EightVerticalHorizontal2.MAXQ])
Code05_EightVerticalHorizontal2.w = jarray('BitSet', [Code05_EightVerticalHorizontal2.MAXQ])
Code05_EightVerticalHorizontal2.edgeCnt = jcast('int', 0)
Code05_EightVerticalHorizontal2.last = jarray('int', [Code05_EightVerticalHorizontal2.MAXQ])
Code05_EightVerticalHorizontal2.basis = jarray('BitSet', [jcast('int', jadd(Code05_EightVerticalHorizontal2.BIT, 1))])
Code05_EightVerticalHorizontal2.inspos = jarray('int', [jcast('int', jadd(Code05_EightVerticalHorizontal2.BIT, 1))])
Code05_EightVerticalHorizontal2.basiz = jcast('int', 0)
Code05_EightVerticalHorizontal2.father = jarray('int', [Code05_EightVerticalHorizontal2.MAXN])
Code05_EightVerticalHorizontal2.eor = jarray('BitSet', [Code05_EightVerticalHorizontal2.MAXN])
Code05_EightVerticalHorizontal2.head = jarray('int', [jcast('int', (Code05_EightVerticalHorizontal2.MAXQ << (2 & 31)))])
Code05_EightVerticalHorizontal2.next = jarray('int', [Code05_EightVerticalHorizontal2.MAXT])
Code05_EightVerticalHorizontal2.tox = jarray('int', [Code05_EightVerticalHorizontal2.MAXT])
Code05_EightVerticalHorizontal2.toy = jarray('int', [Code05_EightVerticalHorizontal2.MAXT])
Code05_EightVerticalHorizontal2.tow = jarray('BitSet', [Code05_EightVerticalHorizontal2.MAXT])
Code05_EightVerticalHorizontal2.cnt = jcast('int', 0)
Code05_EightVerticalHorizontal2.ans = jarray('BitSet', [Code05_EightVerticalHorizontal2.MAXQ])
Code05_EightVerticalHorizontal2.FastReader.BUFFER_SIZE = jcast('int', jcast('int', (1 << (16 & 31))))

if __name__ == '__main__':
    Code05_EightVerticalHorizontal2.main([])
