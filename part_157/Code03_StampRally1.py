# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 边的最大编号的最小值，Python版
# 图里有n个点，m条无向边，边的编号1~m，没有边权，所有点都连通
# 一共有q条查询，查询的格式如下
# 查询 x y z : 从两个点x和y出发，希望经过的点数量等于z
# 每个点可以重复经过，但是重复经过只计算一次
# 经过边的最大编号，最小是多少
# 3 <= n、m、q <= 10^5
# 3 <= z <= n
# 测试链接 : https://www.luogu.com.cn/problem/AT_agc002_d
# 测试链接 : https://atcoder.jp/contests/agc002/tasks/agc002_d
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_StampRally1:
    __java_fields__ = {'MAXK': 'MAXK', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'q': 'q', 'edge': 'edge', 'father': 'father', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'nodeKey': 'nodeKey', 'cntu': 'cntu', 'leafsiz': 'leafsiz', 'stjump': 'stjump'}
    MAXK = 0
    MAXM = 0
    MAXP = 0
    n = 0
    m = 0
    q = 0
    edge = None
    # 并查集
    father = None
    # Kruskal重构树
    head = None
    next = None
    to = None
    cntg = 0
    nodeKey = None
    cntu = 0
    # 树上dfs
    leafsiz = None
    stjump = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_StampRally1.next, ((_java_obj_1 := Code03_StampRally1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_StampRally1.head[u])
        Code03_StampRally1.to[Code03_StampRally1.cntg] = jcast('int', v)
        Code03_StampRally1.head[u] = jcast('int', Code03_StampRally1.cntg)

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code03_StampRally1.father[i]):
            jset(Code03_StampRally1.father, i, Code03_StampRally1.find(Code03_StampRally1.father[i]))
        return jcast('int', Code03_StampRally1.father[i])

    @staticmethod
    def kruskalRebuild():
        i = jcast('int', 1)
        while (i <= Code03_StampRally1.n):
            Code03_StampRally1.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code03_StampRally1.edge, 1, jcast('int', jadd(Code03_StampRally1.m, 1)), (lambda a, b: (a[2] - b[2])))
        Code03_StampRally1.cntu = jcast('int', Code03_StampRally1.n)
        i = jcast('int', 1)
        fx = 0
        fy = 0
        while (i <= Code03_StampRally1.m):
            fx = jcast('int', Code03_StampRally1.find(Code03_StampRally1.edge[i][0]))
            fy = jcast('int', Code03_StampRally1.find(Code03_StampRally1.edge[i][1]))
            if (fx != fy):
                jset(Code03_StampRally1.father, fx, jset(Code03_StampRally1.father, fy, ((_java_obj_4 := Code03_StampRally1), (_java_key_5 := 'cntu'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
                Code03_StampRally1.father[Code03_StampRally1.cntu] = jcast('int', Code03_StampRally1.cntu)
                Code03_StampRally1.nodeKey[Code03_StampRally1.cntu] = jcast('int', Code03_StampRally1.edge[i][2])
                Code03_StampRally1.addEdge(Code03_StampRally1.cntu, fx)
                Code03_StampRally1.addEdge(Code03_StampRally1.cntu, fy)
            i = jcast('int', (i + 1))

    @staticmethod
    def dfs(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code03_StampRally1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code03_StampRally1.MAXP):
            jset(Code03_StampRally1.stjump[u], p, Code03_StampRally1.stjump[Code03_StampRally1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code03_StampRally1.head[u])
        while (e > 0):
            Code03_StampRally1.dfs(Code03_StampRally1.to[e], u)
            e = jcast('int', Code03_StampRally1.next[e])
        if (u <= Code03_StampRally1.n):
            Code03_StampRally1.leafsiz[u] = jcast('int', 1)
        else:
            Code03_StampRally1.leafsiz[u] = jcast('int', 0)
        e = jcast('int', Code03_StampRally1.head[u])
        while (e > 0):
            Code03_StampRally1.leafsiz[u] = jcast('int', jcast('int', jadd(Code03_StampRally1.leafsiz[u], Code03_StampRally1.leafsiz[Code03_StampRally1.to[e]])))
            e = jcast('int', Code03_StampRally1.next[e])

    @staticmethod
    def check(x, y, z, limit):
        x = jcast('int', x)
        y = jcast('int', y)
        z = jcast('int', z)
        limit = jcast('int', limit)
        p = jcast('int', jcast('int', (Code03_StampRally1.MAXP - 1)))
        while (p >= 0):
            if ((Code03_StampRally1.stjump[x][p] > 0) and (Code03_StampRally1.nodeKey[Code03_StampRally1.stjump[x][p]] <= limit)):
                x = jcast('int', Code03_StampRally1.stjump[x][p])
            p = jcast('int', (p - 1))
        p = jcast('int', jcast('int', (Code03_StampRally1.MAXP - 1)))
        while (p >= 0):
            if ((Code03_StampRally1.stjump[y][p] > 0) and (Code03_StampRally1.nodeKey[Code03_StampRally1.stjump[y][p]] <= limit)):
                y = jcast('int', Code03_StampRally1.stjump[y][p])
            p = jcast('int', (p - 1))
        if (x == y):
            return jcast('boolean', (Code03_StampRally1.leafsiz[x] >= z))
        else:
            return jcast('boolean', (jcast('int', jadd(Code03_StampRally1.leafsiz[x], Code03_StampRally1.leafsiz[y])) >= z))

    @staticmethod
    def query(x, y, z):
        x = jcast('int', x)
        y = jcast('int', y)
        z = jcast('int', z)
        l = jcast('int', 1)
        r = jcast('int', Code03_StampRally1.m)
        mid = 0
        ans = jcast('int', 0)
        while (l <= r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if Code03_StampRally1.check(x, y, z, mid):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        io = Code03_StampRally1.FastIO(jget(System, 'in'), jget(System, 'out'), _java_ctor=0)
        Code03_StampRally1.n = jcast('int', jcall(io, 'nextInt'))
        Code03_StampRally1.m = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_StampRally1.m):
            jset(Code03_StampRally1.edge[i], 0, jcall(io, 'nextInt'))
            jset(Code03_StampRally1.edge[i], 1, jcall(io, 'nextInt'))
            jset(Code03_StampRally1.edge[i], 2, i)
            i = jcast('int', (i + 1))
        Code03_StampRally1.kruskalRebuild()
        Code03_StampRally1.dfs(Code03_StampRally1.cntu, 0)
        Code03_StampRally1.q = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        y = 0
        z = 0
        while (i <= Code03_StampRally1.q):
            x = jcast('int', jcall(io, 'nextInt'))
            y = jcast('int', jcall(io, 'nextInt'))
            z = jcast('int', jcall(io, 'nextInt'))
            jcall(io, 'writelnInt', Code03_StampRally1.query(x, y, z))
            i = jcast('int', (i + 1))
        jcall(io, 'flush')

    # 读写工具类
    class FastIO:
        __java_fields__ = {'is': 'is_', 'os': 'os', 'inbuf': 'inbuf', 'lenbuf': 'lenbuf', 'ptrbuf': 'ptrbuf', 'outBuf': 'outBuf'}
        # is_：实例字段，在构造函数中初始化。
        # os：实例字段，在构造函数中初始化。
        # inbuf：实例字段，在构造函数中初始化。
        # lenbuf：实例字段，在构造函数中初始化。
        # ptrbuf：实例字段，在构造函数中初始化。
        # outBuf：实例字段，在构造函数中初始化。
        def _java_init_0(self, is_, os):
            self.is_ = is_
            self.os = os

        def readByte(self):
            if (self.ptrbuf >= self.lenbuf):
                self.ptrbuf = jcast('int', 0)
                try:
                    self.lenbuf = jcast('int', jcall(self.is_, 'read', self.inbuf))
                except (JBreak, JContinue):
                    raise
                except Exception as _java_exception_7:
                    if jinstanceof(_java_exception_7, 'IOException'):
                        e = _java_exception_7
                        raise jnew('RuntimeException', e)
                    else:
                        raise
                if (self.lenbuf == jcast('int', (-1))):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', jcast('int', (self.inbuf[((_java_obj_8 := self), (_java_key_9 := 'ptrbuf'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))), _java_old_10)[4]] & 255)))

        def skip(self):
            b = 0
            while ((b := self.readByte()) != jcast('int', (-1))):
                if (b > jchar(' ')):
                    return jcast('int', b)
            return jcast('int', jcast('int', (-1)))

        def nextInt(self):
            b = jcast('int', self.skip())
            if (b == jcast('int', (-1))):
                raise jnew('RuntimeException', 'No more integers (EOF)')
            negative = jcast('boolean', False)
            if (b == jchar('-')):
                negative = jcast('boolean', True)
                b = jcast('int', self.readByte())
            val = jcast('int', 0)
            while ((b >= jchar('0')) and (b <= jchar('9'))):
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (b - jchar('0'))))))
                b = jcast('int', self.readByte())
            return jcast('int', (jcast('int', (-val)) if negative else val))

        def write(self, s):
            jcall(self.outBuf, 'append', s)

        def writeInt(self, x):
            x = jcast('int', x)
            jcall(self.outBuf, 'append', x)

        def writelnInt(self, x):
            x = jcast('int', x)
            jcall(jcall(self.outBuf, 'append', x), 'append', jchar('\n'))

        def flush(self):
            try:
                jcall(self.os, 'write', jcall(jcall(self.outBuf, 'toString'), 'getBytes'))
                jcall(self.os, 'flush')
                jcall(self.outBuf, 'setLength', 0)
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_11:
                if jinstanceof(_java_exception_11, 'IOException'):
                    e = _java_exception_11
                    raise jnew('RuntimeException', e)
                else:
                    raise

        def __init__(self, *args, _java_ctor=None):
            self.is_ = None
            self.os = None
            self.inbuf = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.lenbuf = jcast('int', 0)
            self.ptrbuf = jcast('int', 0)
            self.outBuf = jnew('StringBuilder')
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream', 'OutputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code03_StampRally1.FastIO.FastIO")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_StampRally1.MAXK = jcast('int', 200001)
Code03_StampRally1.MAXM = jcast('int', 100001)
Code03_StampRally1.MAXP = jcast('int', 20)
Code03_StampRally1.n = jcast('int', 0)
Code03_StampRally1.m = jcast('int', 0)
Code03_StampRally1.q = jcast('int', 0)
Code03_StampRally1.edge = jarray('int', [Code03_StampRally1.MAXM, 3])
Code03_StampRally1.father = jarray('int', [Code03_StampRally1.MAXK])
Code03_StampRally1.head = jarray('int', [Code03_StampRally1.MAXK])
Code03_StampRally1.next = jarray('int', [Code03_StampRally1.MAXK])
Code03_StampRally1.to = jarray('int', [Code03_StampRally1.MAXK])
Code03_StampRally1.cntg = jcast('int', 0)
Code03_StampRally1.nodeKey = jarray('int', [Code03_StampRally1.MAXK])
Code03_StampRally1.cntu = jcast('int', 0)
Code03_StampRally1.leafsiz = jarray('int', [Code03_StampRally1.MAXK])
Code03_StampRally1.stjump = jarray('int', [Code03_StampRally1.MAXK, Code03_StampRally1.MAXP])

if __name__ == '__main__':
    Code03_StampRally1.main([])
