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

# 定向道路，Python版
# 图中有n个点、n条无向边
# 图中可能有多个连通块，保证每个连通块都是一棵基环树
# 你可以给每条边分配一个方向，要求得到的有向图不能出现环
# 计算有多少种定向的方案，答案对 1000000007 取余
# 2 <= n <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF711D
# 测试链接 : https://codeforces.com/problemset/problem/711/D
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_DirectedRoads2:
    __java_fields__ = {'MAXN': 'MAXN', 'MOD': 'MOD', 'n': 'n', 'cntb': 'cntb', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'cntd': 'cntd', 'from': 'from_', 'all': 'all', 'cycle': 'cycle'}
    MAXN = 0
    MOD = 0
    n = 0
    cntb = 0
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    cntd = 0
    from_ = None
    # all[x] = 第x棵基环树的节点总数 = 第x棵基环树的边总数
    all = None
    # cycle[x] = 第x棵基环树的环上节点数 = 第x棵基环树的环上边数
    cycle = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_DirectedRoads2.nxt, ((_java_obj_1 := Code01_DirectedRoads2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_DirectedRoads2.head[u])
        Code01_DirectedRoads2.to[Code01_DirectedRoads2.cntg] = jcast('int', v)
        Code01_DirectedRoads2.head[u] = jcast('int', Code01_DirectedRoads2.cntg)

    @staticmethod
    def power(x, p):
        x = jcast('long', x)
        p = jcast('long', p)
        ans = jcast('long', 1)
        while (p > 0):
            if (jcast('long', (p & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), Code01_DirectedRoads2.MOD)))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), Code01_DirectedRoads2.MOD)))
            p = jcast('long', jcast('long', (p >> (1 & 63))))
        return jcast('long', ans)

    @staticmethod
    def dfs(u):
        u = jcast('int', u)
        jset(Code01_DirectedRoads2.dfn, u, ((_java_obj_4 := Code01_DirectedRoads2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code01_DirectedRoads2.all[Code01_DirectedRoads2.cntb] = jcast('int', (Code01_DirectedRoads2.all[Code01_DirectedRoads2.cntb] + 1))
        e = jcast('int', Code01_DirectedRoads2.head[u])
        while (e > 0):
            v = jcast('int', Code01_DirectedRoads2.to[e])
            if (Code01_DirectedRoads2.dfn[v] == 0):
                Code01_DirectedRoads2.from_[v] = jcast('int', u)
                Code01_DirectedRoads2.dfs(v)
            else:
                if (Code01_DirectedRoads2.dfn[u] < Code01_DirectedRoads2.dfn[v]):
                    Code01_DirectedRoads2.cycle[Code01_DirectedRoads2.cntb] = jcast('int', (Code01_DirectedRoads2.cycle[Code01_DirectedRoads2.cntb] + 1))
                    i = jcast('int', v)
                    while (i != u):
                        Code01_DirectedRoads2.cycle[Code01_DirectedRoads2.cntb] = jcast('int', (Code01_DirectedRoads2.cycle[Code01_DirectedRoads2.cntb] + 1))
                        i = jcast('int', Code01_DirectedRoads2.from_[i])
            e = jcast('int', Code01_DirectedRoads2.nxt[e])

    @staticmethod
    def compute():
        ans = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= Code01_DirectedRoads2.n):
            if (Code01_DirectedRoads2.dfn[i] == 0):
                Code01_DirectedRoads2.cntb = jcast('int', (Code01_DirectedRoads2.cntb + 1))
                Code01_DirectedRoads2.dfs(i)
                a = jcast('long', Code01_DirectedRoads2.power(2, Code01_DirectedRoads2.all[Code01_DirectedRoads2.cntb]))
                b = jcast('long', Code01_DirectedRoads2.power(2, jcast('int', jadd(jcast('int', (Code01_DirectedRoads2.all[Code01_DirectedRoads2.cntb] - Code01_DirectedRoads2.cycle[Code01_DirectedRoads2.cntb])), 1))))
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * jcast('long', jmod(jcast('long', jadd(jcast('long', (a - b)), Code01_DirectedRoads2.MOD)), Code01_DirectedRoads2.MOD)))), Code01_DirectedRoads2.MOD)))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code01_DirectedRoads2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_DirectedRoads2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        while (i <= Code01_DirectedRoads2.n):
            x = jcast('int', jcall(in_, 'nextInt'))
            Code01_DirectedRoads2.addEdge(i, x)
            Code01_DirectedRoads2.addEdge(x, i)
            i = jcast('int', (i + 1))
        ans = jcast('long', Code01_DirectedRoads2.compute())
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
            raise TypeError("No matching overload for Code01_DirectedRoads2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_DirectedRoads2.MAXN = jcast('int', 200001)
Code01_DirectedRoads2.MOD = jcast('int', 1000000007)
Code01_DirectedRoads2.n = jcast('int', 0)
Code01_DirectedRoads2.cntb = jcast('int', 0)
Code01_DirectedRoads2.head = jarray('int', [Code01_DirectedRoads2.MAXN])
Code01_DirectedRoads2.nxt = jarray('int', [jcast('int', (Code01_DirectedRoads2.MAXN << (1 & 31)))])
Code01_DirectedRoads2.to = jarray('int', [jcast('int', (Code01_DirectedRoads2.MAXN << (1 & 31)))])
Code01_DirectedRoads2.cntg = jcast('int', 0)
Code01_DirectedRoads2.dfn = jarray('int', [Code01_DirectedRoads2.MAXN])
Code01_DirectedRoads2.cntd = jcast('int', 0)
Code01_DirectedRoads2.from_ = jarray('int', [Code01_DirectedRoads2.MAXN])
Code01_DirectedRoads2.all = jarray('int', [Code01_DirectedRoads2.MAXN])
Code01_DirectedRoads2.cycle = jarray('int', [Code01_DirectedRoads2.MAXN])

if __name__ == '__main__':
    Code01_DirectedRoads2.main([])
