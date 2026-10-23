# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 简单路径数量，Python版
# 图中有n个点、n条无向边，图是一棵基环树，图中没有重边和自环
# 点x到点y的简单路径，要求没有重复节点，要求边的数量 >= 1
# 如果两条简单路径只有方向相反，那么认为是同一条简单路径，不要重复统计
# 比如(a, b, c)和(c, b, a)，就是同一条简单路径
# 计算图中简单路径的数量
# 3 <= n <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF1454E
# 测试链接 : https://codeforces.com/problemset/problem/1454/E
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_NumberOfSimplePaths1:
    __java_fields__ = {'MAXN': 'MAXN', 't': 't', 'n': 'n', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'cntd': 'cntd', 'from': 'from_', 'cycle': 'cycle', 'siz': 'siz'}
    MAXN = 0
    t = 0
    n = 0
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    cntd = 0
    from_ = None
    cycle = None
    siz = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_NumberOfSimplePaths1.nxt, ((_java_obj_1 := Code02_NumberOfSimplePaths1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_NumberOfSimplePaths1.head[u])
        Code02_NumberOfSimplePaths1.to[Code02_NumberOfSimplePaths1.cntg] = jcast('int', v)
        Code02_NumberOfSimplePaths1.head[u] = jcast('int', Code02_NumberOfSimplePaths1.cntg)

    @staticmethod
    def dfs(u):
        u = jcast('int', u)
        jset(Code02_NumberOfSimplePaths1.dfn, u, ((_java_obj_4 := Code02_NumberOfSimplePaths1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        e = jcast('int', Code02_NumberOfSimplePaths1.head[u])
        while (e > 0):
            v = jcast('int', Code02_NumberOfSimplePaths1.to[e])
            if (Code02_NumberOfSimplePaths1.dfn[v] == 0):
                Code02_NumberOfSimplePaths1.from_[v] = jcast('int', u)
                Code02_NumberOfSimplePaths1.dfs(v)
            else:
                if (Code02_NumberOfSimplePaths1.dfn[u] < Code02_NumberOfSimplePaths1.dfn[v]):
                    Code02_NumberOfSimplePaths1.cycle[u] = jcast('boolean', True)
                    i = jcast('int', v)
                    while (i != u):
                        Code02_NumberOfSimplePaths1.cycle[i] = jcast('boolean', True)
                        i = jcast('int', Code02_NumberOfSimplePaths1.from_[i])
            e = jcast('int', Code02_NumberOfSimplePaths1.nxt[e])

    @staticmethod
    def dpOnTree(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code02_NumberOfSimplePaths1.siz[u] = jcast('long', 1)
        e = jcast('int', Code02_NumberOfSimplePaths1.head[u])
        while (e > 0):
            v = jcast('int', Code02_NumberOfSimplePaths1.to[e])
            if ((v != fa) and (not Code02_NumberOfSimplePaths1.cycle[v])):
                Code02_NumberOfSimplePaths1.dpOnTree(v, u)
                Code02_NumberOfSimplePaths1.siz[u] = jcast('long', jcast('long', jadd(Code02_NumberOfSimplePaths1.siz[u], Code02_NumberOfSimplePaths1.siz[v])))
            e = jcast('int', Code02_NumberOfSimplePaths1.nxt[e])

    @staticmethod
    def compute():
        Code02_NumberOfSimplePaths1.dfs(1)
        ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code02_NumberOfSimplePaths1.n):
            if Code02_NumberOfSimplePaths1.cycle[i]:
                Code02_NumberOfSimplePaths1.dpOnTree(i, 0)
                ans = jcast('long', jcast('long', jadd(ans, jcast('long', jadd(jcast('long', jdiv(jcast('long', (Code02_NumberOfSimplePaths1.siz[i] * jcast('long', (Code02_NumberOfSimplePaths1.siz[i] - 1)))), 2)), jcast('long', (Code02_NumberOfSimplePaths1.siz[i] * jcast('long', (Code02_NumberOfSimplePaths1.n - Code02_NumberOfSimplePaths1.siz[i])))))))))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def prepare():
        Code02_NumberOfSimplePaths1.cntg = jcast('int', jset(Code02_NumberOfSimplePaths1, 'cntd', 0))
        i = jcast('int', 1)
        while (i <= Code02_NumberOfSimplePaths1.n):
            jset(Code02_NumberOfSimplePaths1.head, i, jset(Code02_NumberOfSimplePaths1.dfn, i, 0))
            Code02_NumberOfSimplePaths1.cycle[i] = jcast('boolean', False)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code02_NumberOfSimplePaths1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_NumberOfSimplePaths1.t = jcast('int', jcall(in_, 'nextInt'))
        c = jcast('int', 1)
        while (c <= Code02_NumberOfSimplePaths1.t):
            Code02_NumberOfSimplePaths1.n = jcast('int', jcall(in_, 'nextInt'))
            Code02_NumberOfSimplePaths1.prepare()
            i = jcast('int', 1)
            u = 0
            v = 0
            while (i <= Code02_NumberOfSimplePaths1.n):
                u = jcast('int', jcall(in_, 'nextInt'))
                v = jcast('int', jcall(in_, 'nextInt'))
                Code02_NumberOfSimplePaths1.addEdge(u, v)
                Code02_NumberOfSimplePaths1.addEdge(v, u)
                i = jcast('int', (i + 1))
            ans = jcast('long', Code02_NumberOfSimplePaths1.compute())
            jcall(out, 'println', ans)
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
            return jcast('int', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

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
            raise TypeError("No matching overload for Code02_NumberOfSimplePaths1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_NumberOfSimplePaths1.MAXN = jcast('int', 200001)
Code02_NumberOfSimplePaths1.t = jcast('int', 0)
Code02_NumberOfSimplePaths1.n = jcast('int', 0)
Code02_NumberOfSimplePaths1.head = jarray('int', [Code02_NumberOfSimplePaths1.MAXN])
Code02_NumberOfSimplePaths1.nxt = jarray('int', [jcast('int', (Code02_NumberOfSimplePaths1.MAXN << (1 & 31)))])
Code02_NumberOfSimplePaths1.to = jarray('int', [jcast('int', (Code02_NumberOfSimplePaths1.MAXN << (1 & 31)))])
Code02_NumberOfSimplePaths1.cntg = jcast('int', 0)
Code02_NumberOfSimplePaths1.dfn = jarray('int', [Code02_NumberOfSimplePaths1.MAXN])
Code02_NumberOfSimplePaths1.cntd = jcast('int', 0)
Code02_NumberOfSimplePaths1.from_ = jarray('int', [Code02_NumberOfSimplePaths1.MAXN])
Code02_NumberOfSimplePaths1.cycle = jarray('boolean', [Code02_NumberOfSimplePaths1.MAXN])
Code02_NumberOfSimplePaths1.siz = jarray('long', [Code02_NumberOfSimplePaths1.MAXN])

if __name__ == '__main__':
    Code02_NumberOfSimplePaths1.main([])
