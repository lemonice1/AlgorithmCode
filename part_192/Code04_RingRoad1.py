# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 城市环路，Python版
# 图中有n个点、n条无向边，每个点有点权，图是一棵基环树
# 图中任意相邻两点不能同时选择，先得到最大的点权累加和
# 然后乘以题目给定的系数k，打印结果
# 1 <= n <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P1453
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_RingRoad1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'k': 'k', 'arr': 'arr', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'cntd': 'cntd', 'x': 'x', 'y': 'y', 'skip': 'skip', 'dp': 'dp', 'stau': 'stau', 'stas': 'stas', 'staf': 'staf', 'stae': 'stae', 'stacksize': 'stacksize', 'u': 'u', 'status': 'status', 'fa': 'fa', 'e': 'e'}
    MAXN = 0
    n = 0
    k = 0.0
    arr = None
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    cntd = 0
    x = 0
    y = 0
    skip = 0
    dp = None
    # 递归改迭代需要的栈
    stau = None
    stas = None
    staf = None
    stae = None
    stacksize = 0
    u = 0
    status = 0
    fa = 0
    e = 0
    @staticmethod
    def push(u, status, fa, e):
        u = jcast('int', u)
        status = jcast('int', status)
        fa = jcast('int', fa)
        e = jcast('int', e)
        Code04_RingRoad1.stau[Code04_RingRoad1.stacksize] = jcast('int', u)
        Code04_RingRoad1.stas[Code04_RingRoad1.stacksize] = jcast('int', status)
        Code04_RingRoad1.staf[Code04_RingRoad1.stacksize] = jcast('int', fa)
        Code04_RingRoad1.stae[Code04_RingRoad1.stacksize] = jcast('int', e)
        Code04_RingRoad1.stacksize = jcast('int', (Code04_RingRoad1.stacksize + 1))

    @staticmethod
    def pop():
        Code04_RingRoad1.stacksize = jcast('int', (Code04_RingRoad1.stacksize - 1))
        Code04_RingRoad1.u = jcast('int', Code04_RingRoad1.stau[Code04_RingRoad1.stacksize])
        Code04_RingRoad1.status = jcast('int', Code04_RingRoad1.stas[Code04_RingRoad1.stacksize])
        Code04_RingRoad1.fa = jcast('int', Code04_RingRoad1.staf[Code04_RingRoad1.stacksize])
        Code04_RingRoad1.e = jcast('int', Code04_RingRoad1.stae[Code04_RingRoad1.stacksize])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_RingRoad1.nxt, ((_java_obj_1 := Code04_RingRoad1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_RingRoad1.head[u])
        Code04_RingRoad1.to[Code04_RingRoad1.cntg] = jcast('int', v)
        Code04_RingRoad1.head[u] = jcast('int', Code04_RingRoad1.cntg)

    # 递归版
    @staticmethod
    def dfs1(u):
        u = jcast('int', u)
        jset(Code04_RingRoad1.dfn, u, ((_java_obj_4 := Code04_RingRoad1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        e = jcast('int', Code04_RingRoad1.head[u])
        while (e > 0):
            v = jcast('int', Code04_RingRoad1.to[e])
            if (Code04_RingRoad1.dfn[v] == 0):
                Code04_RingRoad1.dfs1(v)
            else:
                if (Code04_RingRoad1.dfn[u] < Code04_RingRoad1.dfn[v]):
                    Code04_RingRoad1.x = jcast('int', u)
                    Code04_RingRoad1.y = jcast('int', v)
                    Code04_RingRoad1.skip = jcast('int', jcast('int', (jcast('int', jadd(e, 1)) >> (1 & 31))))
            e = jcast('int', Code04_RingRoad1.nxt[e])

    # 迭代版
    @staticmethod
    def dfs2(cur):
        cur = jcast('int', cur)
        Code04_RingRoad1.stacksize = jcast('int', 0)
        Code04_RingRoad1.push(cur, jcast('int', (-1)), 0, jcast('int', (-1)))
        v = 0
        while (Code04_RingRoad1.stacksize > 0):
            Code04_RingRoad1.pop()
            if (Code04_RingRoad1.status == jcast('int', (-1))):
                jset(Code04_RingRoad1.dfn, Code04_RingRoad1.u, ((_java_obj_7 := Code04_RingRoad1), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
                Code04_RingRoad1.e = jcast('int', Code04_RingRoad1.head[Code04_RingRoad1.u])
            else:
                v = jcast('int', Code04_RingRoad1.to[Code04_RingRoad1.e])
                if ((Code04_RingRoad1.status == 1) and (Code04_RingRoad1.dfn[Code04_RingRoad1.u] < Code04_RingRoad1.dfn[v])):
                    Code04_RingRoad1.x = jcast('int', Code04_RingRoad1.u)
                    Code04_RingRoad1.y = jcast('int', v)
                    Code04_RingRoad1.skip = jcast('int', jcast('int', (jcast('int', jadd(Code04_RingRoad1.e, 1)) >> (1 & 31))))
                Code04_RingRoad1.e = jcast('int', Code04_RingRoad1.nxt[Code04_RingRoad1.e])
            if (Code04_RingRoad1.e != 0):
                v = jcast('int', Code04_RingRoad1.to[Code04_RingRoad1.e])
                if (Code04_RingRoad1.dfn[v] == 0):
                    Code04_RingRoad1.push(Code04_RingRoad1.u, 0, 0, Code04_RingRoad1.e)
                    Code04_RingRoad1.push(v, jcast('int', (-1)), 0, jcast('int', (-1)))
                else:
                    Code04_RingRoad1.push(Code04_RingRoad1.u, 1, 0, Code04_RingRoad1.e)

    # 递归版
    @staticmethod
    def dpOnTree1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code04_RingRoad1.dp[u], 0, 0)
        jset(Code04_RingRoad1.dp[u], 1, Code04_RingRoad1.arr[u])
        e = jcast('int', Code04_RingRoad1.head[u])
        while (e > 0):
            v = jcast('int', Code04_RingRoad1.to[e])
            if ((v != fa) and (jcast('int', (jcast('int', jadd(e, 1)) >> (1 & 31))) != Code04_RingRoad1.skip)):
                Code04_RingRoad1.dpOnTree1(v, u)
                ((_java_obj_10 := Code04_RingRoad1.dp[u]), (_java_key_11 := 0), jset(_java_obj_10, _java_key_11, jcast('int', jadd(jget(_java_obj_10, _java_key_11), jstatic('Math', 'max', Code04_RingRoad1.dp[v][0], Code04_RingRoad1.dp[v][1])))))[2]
                ((_java_obj_12 := Code04_RingRoad1.dp[u]), (_java_key_13 := 1), jset(_java_obj_12, _java_key_13, jcast('int', jadd(jget(_java_obj_12, _java_key_13), Code04_RingRoad1.dp[v][0]))))[2]
            e = jcast('int', Code04_RingRoad1.nxt[e])

    # 迭代版
    @staticmethod
    def dpOnTree2(cur, father):
        cur = jcast('int', cur)
        father = jcast('int', father)
        Code04_RingRoad1.stacksize = jcast('int', 0)
        Code04_RingRoad1.push(cur, 0, father, jcast('int', (-1)))
        while (Code04_RingRoad1.stacksize > 0):
            Code04_RingRoad1.pop()
            if (Code04_RingRoad1.e == jcast('int', (-1))):
                jset(Code04_RingRoad1.dp[Code04_RingRoad1.u], 0, 0)
                jset(Code04_RingRoad1.dp[Code04_RingRoad1.u], 1, Code04_RingRoad1.arr[Code04_RingRoad1.u])
                Code04_RingRoad1.e = jcast('int', Code04_RingRoad1.head[Code04_RingRoad1.u])
            else:
                Code04_RingRoad1.e = jcast('int', Code04_RingRoad1.nxt[Code04_RingRoad1.e])
            if (Code04_RingRoad1.e != 0):
                Code04_RingRoad1.push(Code04_RingRoad1.u, 0, Code04_RingRoad1.fa, Code04_RingRoad1.e)
                if ((Code04_RingRoad1.to[Code04_RingRoad1.e] != Code04_RingRoad1.fa) and (jcast('int', (jcast('int', jadd(Code04_RingRoad1.e, 1)) >> (1 & 31))) != Code04_RingRoad1.skip)):
                    Code04_RingRoad1.push(Code04_RingRoad1.to[Code04_RingRoad1.e], 0, Code04_RingRoad1.u, jcast('int', (-1)))
            else:
                ei = jcast('int', Code04_RingRoad1.head[Code04_RingRoad1.u])
                while (ei > 0):
                    v = jcast('int', Code04_RingRoad1.to[ei])
                    if ((v != Code04_RingRoad1.fa) and (jcast('int', (jcast('int', jadd(ei, 1)) >> (1 & 31))) != Code04_RingRoad1.skip)):
                        ((_java_obj_14 := Code04_RingRoad1.dp[Code04_RingRoad1.u]), (_java_key_15 := 0), jset(_java_obj_14, _java_key_15, jcast('int', jadd(jget(_java_obj_14, _java_key_15), jstatic('Math', 'max', Code04_RingRoad1.dp[v][0], Code04_RingRoad1.dp[v][1])))))[2]
                        ((_java_obj_16 := Code04_RingRoad1.dp[Code04_RingRoad1.u]), (_java_key_17 := 1), jset(_java_obj_16, _java_key_17, jcast('int', jadd(jget(_java_obj_16, _java_key_17), Code04_RingRoad1.dp[v][0]))))[2]
                    ei = jcast('int', Code04_RingRoad1.nxt[ei])

    @staticmethod
    def compute():
        Code04_RingRoad1.x = jcast('int', jset(Code04_RingRoad1, 'y', 0))
        # dfs1(1);
        Code04_RingRoad1.dfs2(1)
        # dpOnTree1(x, 0);
        Code04_RingRoad1.dpOnTree2(Code04_RingRoad1.x, 0)
        ans = jcast('long', Code04_RingRoad1.dp[Code04_RingRoad1.x][0])
        # dpOnTree1(y, 0);
        Code04_RingRoad1.dpOnTree2(Code04_RingRoad1.y, 0)
        ans = jcast('long', jstatic('Math', 'max', ans, Code04_RingRoad1.dp[Code04_RingRoad1.y][0]))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code04_RingRoad1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_RingRoad1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_RingRoad1.n):
            jset(Code04_RingRoad1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code04_RingRoad1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            u = jcast('int', (u + 1))
            v = jcast('int', (v + 1))
            Code04_RingRoad1.addEdge(u, v)
            Code04_RingRoad1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code04_RingRoad1.k = jcast('double', jcall(in_, 'nextDouble'))
        ans = jcast('long', Code04_RingRoad1.compute())
        jcall(out, 'printf', '%.1f\n', (Code04_RingRoad1.k * ans))
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
            return jcast('int', self.buffer[((_java_obj_18 := self), (_java_key_19 := 'ptr'), (_java_old_20 := jget(_java_obj_18, _java_key_19)), jset(_java_obj_18, _java_key_19, jcast('int', (_java_old_20 + (1)))), _java_old_20)[4]])

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

        def nextDouble(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            intPart = jcast('long', 0)
            while (((c > jchar(' ')) and (c != jcast('int', (-1)))) and (c != jchar('.'))):
                intPart = jcast('long', jcast('long', jadd(jcast('long', (intPart * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            val = jcast('double', jcast('double', intPart))
            if (c == jchar('.')):
                c = jcast('int', self.readByte())
                base = jcast('double', 0.1)
                while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                    val = jcast('double', jadd(val, (jcast('int', (c - jchar('0'))) * base)))
                    base = jcast('double', (base * 0.1))
                    c = jcast('int', self.readByte())
            return jcast('double', ((-val) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_RingRoad1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_RingRoad1.MAXN = jcast('int', 100001)
Code04_RingRoad1.n = jcast('int', 0)
Code04_RingRoad1.k = jcast('double', 0.0)
Code04_RingRoad1.arr = jarray('int', [Code04_RingRoad1.MAXN])
Code04_RingRoad1.head = jarray('int', [Code04_RingRoad1.MAXN])
Code04_RingRoad1.nxt = jarray('int', [jcast('int', (Code04_RingRoad1.MAXN << (1 & 31)))])
Code04_RingRoad1.to = jarray('int', [jcast('int', (Code04_RingRoad1.MAXN << (1 & 31)))])
Code04_RingRoad1.cntg = jcast('int', 0)
Code04_RingRoad1.dfn = jarray('int', [Code04_RingRoad1.MAXN])
Code04_RingRoad1.cntd = jcast('int', 0)
Code04_RingRoad1.x = jcast('int', 0)
Code04_RingRoad1.y = jcast('int', 0)
Code04_RingRoad1.skip = jcast('int', 0)
Code04_RingRoad1.dp = jarray('int', [Code04_RingRoad1.MAXN, 2])
Code04_RingRoad1.stau = jarray('int', [Code04_RingRoad1.MAXN])
Code04_RingRoad1.stas = jarray('int', [Code04_RingRoad1.MAXN])
Code04_RingRoad1.staf = jarray('int', [Code04_RingRoad1.MAXN])
Code04_RingRoad1.stae = jarray('int', [Code04_RingRoad1.MAXN])
Code04_RingRoad1.stacksize = jcast('int', 0)
Code04_RingRoad1.u = jcast('int', 0)
Code04_RingRoad1.status = jcast('int', 0)
Code04_RingRoad1.fa = jcast('int', 0)
Code04_RingRoad1.e = jcast('int', 0)

if __name__ == '__main__':
    Code04_RingRoad1.main([])
