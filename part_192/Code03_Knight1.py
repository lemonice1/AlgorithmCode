# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 骑士，Python版
# 图中有n个点、n条无向边，每个点有点权
# 图中可能有多个连通块，保证每个连通块都是一棵基环树
# 图中任意相邻两点不能同时选择，计算能得到的最大点权累加和
# 1 <= n、点权 <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P2607
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Knight1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'arr': 'arr', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'cntd': 'cntd', 'x': 'x', 'y': 'y', 'skip': 'skip', 'dp': 'dp'}
    MAXN = 0
    n = 0
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
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_Knight1.nxt, ((_java_obj_1 := Code03_Knight1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_Knight1.head[u])
        Code03_Knight1.to[Code03_Knight1.cntg] = jcast('int', v)
        Code03_Knight1.head[u] = jcast('int', Code03_Knight1.cntg)

    @staticmethod
    def dfs(u):
        u = jcast('int', u)
        jset(Code03_Knight1.dfn, u, ((_java_obj_4 := Code03_Knight1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        e = jcast('int', Code03_Knight1.head[u])
        while (e > 0):
            v = jcast('int', Code03_Knight1.to[e])
            if (Code03_Knight1.dfn[v] == 0):
                Code03_Knight1.dfs(v)
            else:
                if (Code03_Knight1.dfn[u] < Code03_Knight1.dfn[v]):
                    Code03_Knight1.x = jcast('int', u)
                    Code03_Knight1.y = jcast('int', v)
                    Code03_Knight1.skip = jcast('int', jcast('int', (jcast('int', jadd(e, 1)) >> (1 & 31))))
            e = jcast('int', Code03_Knight1.nxt[e])

    @staticmethod
    def dpOnTree(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code03_Knight1.dp[u], 0, 0)
        jset(Code03_Knight1.dp[u], 1, Code03_Knight1.arr[u])
        e = jcast('int', Code03_Knight1.head[u])
        while (e > 0):
            v = jcast('int', Code03_Knight1.to[e])
            if ((v != fa) and (jcast('int', (jcast('int', jadd(e, 1)) >> (1 & 31))) != Code03_Knight1.skip)):
                Code03_Knight1.dpOnTree(v, u)
                ((_java_obj_7 := Code03_Knight1.dp[u]), (_java_key_8 := 0), jset(_java_obj_7, _java_key_8, jcast('long', jadd(jget(_java_obj_7, _java_key_8), jstatic('Math', 'max', Code03_Knight1.dp[v][0], Code03_Knight1.dp[v][1])))))[2]
                ((_java_obj_9 := Code03_Knight1.dp[u]), (_java_key_10 := 1), jset(_java_obj_9, _java_key_10, jcast('long', jadd(jget(_java_obj_9, _java_key_10), Code03_Knight1.dp[v][0]))))[2]
            e = jcast('int', Code03_Knight1.nxt[e])

    @staticmethod
    def compute():
        ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code03_Knight1.n):
            if (Code03_Knight1.dfn[i] == 0):
                Code03_Knight1.x = jcast('int', jset(Code03_Knight1, 'y', 0))
                Code03_Knight1.dfs(i)
                Code03_Knight1.dpOnTree(Code03_Knight1.x, 0)
                cur = jcast('long', Code03_Knight1.dp[Code03_Knight1.x][0])
                Code03_Knight1.dpOnTree(Code03_Knight1.y, 0)
                cur = jcast('long', jstatic('Math', 'max', cur, Code03_Knight1.dp[Code03_Knight1.y][0]))
                ans = jcast('long', jcast('long', jadd(ans, cur)))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code03_Knight1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_Knight1.n = jcast('int', jcall(in_, 'nextInt'))
        x = jcast('int', 1)
        y = 0
        while (x <= Code03_Knight1.n):
            jset(Code03_Knight1.arr, x, jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            Code03_Knight1.addEdge(x, y)
            Code03_Knight1.addEdge(y, x)
            x = jcast('int', (x + 1))
        ans = jcast('long', Code03_Knight1.compute())
        jcall(out, 'println', ans)
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
            return jcast('int', self.buffer[((_java_obj_11 := self), (_java_key_12 := 'ptr'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]])

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
            raise TypeError("No matching overload for Code03_Knight1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Knight1.MAXN = jcast('int', 1000001)
Code03_Knight1.n = jcast('int', 0)
Code03_Knight1.arr = jarray('int', [Code03_Knight1.MAXN])
Code03_Knight1.head = jarray('int', [Code03_Knight1.MAXN])
Code03_Knight1.nxt = jarray('int', [jcast('int', (Code03_Knight1.MAXN << (1 & 31)))])
Code03_Knight1.to = jarray('int', [jcast('int', (Code03_Knight1.MAXN << (1 & 31)))])
Code03_Knight1.cntg = jcast('int', 0)
Code03_Knight1.dfn = jarray('int', [Code03_Knight1.MAXN])
Code03_Knight1.cntd = jcast('int', 0)
Code03_Knight1.x = jcast('int', 0)
Code03_Knight1.y = jcast('int', 0)
Code03_Knight1.skip = jcast('int', 0)
Code03_Knight1.dp = jarray('long', [Code03_Knight1.MAXN, 2])

if __name__ == '__main__':
    Code03_Knight1.main([])
