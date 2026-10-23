# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# Kruskal重构树模版题，Python版
# 图里有n个点，m条无向边，每条边给定边权，图里可能有若干个连通的部分
# 一共有q条查询，每条查询都是如下的格式
# 查询 x y : 点x和点y希望连通起来，其中的最大边权希望尽量小，打印这个值
# 如果怎样都无法联通，打印"impossible"
# 1 <= n <= 10^5
# 1 <= m <= 3 * 10^5
# 1 <= q <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P2245
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_KruskalRebuild1:
    __java_fields__ = {'MAXK': 'MAXK', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'q': 'q', 'edge': 'edge', 'father': 'father', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'nodeKey': 'nodeKey', 'cntu': 'cntu', 'dep': 'dep', 'stjump': 'stjump', 'ufe': 'ufe', 'stacksize': 'stacksize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXK = 0
    MAXM = 0
    MAXP = 0
    n = 0
    m = 0
    q = 0
    # 每条边有三个信息，节点u、节点v、边权w
    edge = None
    # 并查集
    father = None
    # Kruskal重构树的建图
    head = None
    next = None
    to = None
    cntg = 0
    # Kruskal重构树上，节点的权值
    nodeKey = None
    # Kruskal重构树上，点的数量
    cntu = 0
    # Kruskal重构树上，dfs过程建立的信息
    dep = None
    stjump = None
    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code01_KruskalRebuild1.father[i]):
            jset(Code01_KruskalRebuild1.father, i, Code01_KruskalRebuild1.find(Code01_KruskalRebuild1.father[i]))
        return jcast('int', Code01_KruskalRebuild1.father[i])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_KruskalRebuild1.next, ((_java_obj_1 := Code01_KruskalRebuild1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_KruskalRebuild1.head[u])
        Code01_KruskalRebuild1.to[Code01_KruskalRebuild1.cntg] = jcast('int', v)
        Code01_KruskalRebuild1.head[u] = jcast('int', Code01_KruskalRebuild1.cntg)

    @staticmethod
    def kruskalRebuild():
        i = jcast('int', 1)
        while (i <= Code01_KruskalRebuild1.n):
            Code01_KruskalRebuild1.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code01_KruskalRebuild1.edge, 1, jcast('int', jadd(Code01_KruskalRebuild1.m, 1)), (lambda a, b: (a[2] - b[2])))
        Code01_KruskalRebuild1.cntu = jcast('int', Code01_KruskalRebuild1.n)
        i = jcast('int', 1)
        fx = 0
        fy = 0
        while (i <= Code01_KruskalRebuild1.m):
            fx = jcast('int', Code01_KruskalRebuild1.find(Code01_KruskalRebuild1.edge[i][0]))
            fy = jcast('int', Code01_KruskalRebuild1.find(Code01_KruskalRebuild1.edge[i][1]))
            if (fx != fy):
                jset(Code01_KruskalRebuild1.father, fx, jset(Code01_KruskalRebuild1.father, fy, ((_java_obj_4 := Code01_KruskalRebuild1), (_java_key_5 := 'cntu'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
                Code01_KruskalRebuild1.father[Code01_KruskalRebuild1.cntu] = jcast('int', Code01_KruskalRebuild1.cntu)
                Code01_KruskalRebuild1.nodeKey[Code01_KruskalRebuild1.cntu] = jcast('int', Code01_KruskalRebuild1.edge[i][2])
                Code01_KruskalRebuild1.addEdge(Code01_KruskalRebuild1.cntu, fx)
                Code01_KruskalRebuild1.addEdge(Code01_KruskalRebuild1.cntu, fy)
            i = jcast('int', (i + 1))

    # dfs1是递归函数：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code01_KruskalRebuild1.dep[u] = jcast('int', jcast('int', jadd(Code01_KruskalRebuild1.dep[fa], 1)))
        jset(Code01_KruskalRebuild1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code01_KruskalRebuild1.MAXP):
            jset(Code01_KruskalRebuild1.stjump[u], p, Code01_KruskalRebuild1.stjump[Code01_KruskalRebuild1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code01_KruskalRebuild1.head[u])
        while (e > 0):
            Code01_KruskalRebuild1.dfs1(Code01_KruskalRebuild1.to[e], u)
            e = jcast('int', Code01_KruskalRebuild1.next[e])

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
        jset(Code01_KruskalRebuild1.ufe[Code01_KruskalRebuild1.stacksize], 0, u)
        jset(Code01_KruskalRebuild1.ufe[Code01_KruskalRebuild1.stacksize], 1, f)
        jset(Code01_KruskalRebuild1.ufe[Code01_KruskalRebuild1.stacksize], 2, e)
        Code01_KruskalRebuild1.stacksize = jcast('int', (Code01_KruskalRebuild1.stacksize + 1))

    @staticmethod
    def pop():
        Code01_KruskalRebuild1.stacksize = jcast('int', (Code01_KruskalRebuild1.stacksize - 1))
        Code01_KruskalRebuild1.u = jcast('int', Code01_KruskalRebuild1.ufe[Code01_KruskalRebuild1.stacksize][0])
        Code01_KruskalRebuild1.f = jcast('int', Code01_KruskalRebuild1.ufe[Code01_KruskalRebuild1.stacksize][1])
        Code01_KruskalRebuild1.e = jcast('int', Code01_KruskalRebuild1.ufe[Code01_KruskalRebuild1.stacksize][2])

    # dfs2是dfs1的迭代版
    @staticmethod
    def dfs2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code01_KruskalRebuild1.stacksize = jcast('int', 0)
        Code01_KruskalRebuild1.push(cur, fa, jcast('int', (-1)))
        while (Code01_KruskalRebuild1.stacksize > 0):
            Code01_KruskalRebuild1.pop()
            if (Code01_KruskalRebuild1.e == jcast('int', (-1))):
                Code01_KruskalRebuild1.dep[Code01_KruskalRebuild1.u] = jcast('int', jcast('int', jadd(Code01_KruskalRebuild1.dep[Code01_KruskalRebuild1.f], 1)))
                jset(Code01_KruskalRebuild1.stjump[Code01_KruskalRebuild1.u], 0, Code01_KruskalRebuild1.f)
                p = jcast('int', 1)
                while (p < Code01_KruskalRebuild1.MAXP):
                    jset(Code01_KruskalRebuild1.stjump[Code01_KruskalRebuild1.u], p, Code01_KruskalRebuild1.stjump[Code01_KruskalRebuild1.stjump[Code01_KruskalRebuild1.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code01_KruskalRebuild1.e = jcast('int', Code01_KruskalRebuild1.head[Code01_KruskalRebuild1.u])
            else:
                Code01_KruskalRebuild1.e = jcast('int', Code01_KruskalRebuild1.next[Code01_KruskalRebuild1.e])
            if (Code01_KruskalRebuild1.e != 0):
                Code01_KruskalRebuild1.push(Code01_KruskalRebuild1.u, Code01_KruskalRebuild1.f, Code01_KruskalRebuild1.e)
                Code01_KruskalRebuild1.push(Code01_KruskalRebuild1.to[Code01_KruskalRebuild1.e], Code01_KruskalRebuild1.u, jcast('int', (-1)))

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code01_KruskalRebuild1.dep[a] < Code01_KruskalRebuild1.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code01_KruskalRebuild1.MAXP - 1)))
        while (p >= 0):
            if (Code01_KruskalRebuild1.dep[Code01_KruskalRebuild1.stjump[a][p]] >= Code01_KruskalRebuild1.dep[b]):
                a = jcast('int', Code01_KruskalRebuild1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code01_KruskalRebuild1.MAXP - 1)))
        while (p >= 0):
            if (Code01_KruskalRebuild1.stjump[a][p] != Code01_KruskalRebuild1.stjump[b][p]):
                a = jcast('int', Code01_KruskalRebuild1.stjump[a][p])
                b = jcast('int', Code01_KruskalRebuild1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code01_KruskalRebuild1.stjump[a][0])

    @staticmethod
    def main(args):
        io = Code01_KruskalRebuild1.FastIO(jget(System, 'in'), jget(System, 'out'), _java_ctor=0)
        Code01_KruskalRebuild1.n = jcast('int', jcall(io, 'nextInt'))
        Code01_KruskalRebuild1.m = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_KruskalRebuild1.m):
            jset(Code01_KruskalRebuild1.edge[i], 0, jcall(io, 'nextInt'))
            jset(Code01_KruskalRebuild1.edge[i], 1, jcall(io, 'nextInt'))
            jset(Code01_KruskalRebuild1.edge[i], 2, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        Code01_KruskalRebuild1.kruskalRebuild()
        i = jcast('int', 1)
        while (i <= Code01_KruskalRebuild1.cntu):
            if (i == Code01_KruskalRebuild1.father[i]):
                Code01_KruskalRebuild1.dfs2(i, 0)
            i = jcast('int', (i + 1))
        Code01_KruskalRebuild1.q = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= Code01_KruskalRebuild1.q):
            x = jcast('int', jcall(io, 'nextInt'))
            y = jcast('int', jcall(io, 'nextInt'))
            if (Code01_KruskalRebuild1.find(x) != Code01_KruskalRebuild1.find(y)):
                jcall(io, 'write', 'impossible\n')
            else:
                jcall(io, 'writelnInt', Code01_KruskalRebuild1.nodeKey[Code01_KruskalRebuild1.lca(x, y)])
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
            raise TypeError("No matching overload for Code01_KruskalRebuild1.FastIO.FastIO")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_KruskalRebuild1.MAXK = jcast('int', 200001)
Code01_KruskalRebuild1.MAXM = jcast('int', 300001)
Code01_KruskalRebuild1.MAXP = jcast('int', 20)
Code01_KruskalRebuild1.n = jcast('int', 0)
Code01_KruskalRebuild1.m = jcast('int', 0)
Code01_KruskalRebuild1.q = jcast('int', 0)
Code01_KruskalRebuild1.edge = jarray('int', [Code01_KruskalRebuild1.MAXM, 3])
Code01_KruskalRebuild1.father = jarray('int', [Code01_KruskalRebuild1.MAXK])
Code01_KruskalRebuild1.head = jarray('int', [Code01_KruskalRebuild1.MAXK])
Code01_KruskalRebuild1.next = jarray('int', [Code01_KruskalRebuild1.MAXK])
Code01_KruskalRebuild1.to = jarray('int', [Code01_KruskalRebuild1.MAXK])
Code01_KruskalRebuild1.cntg = jcast('int', 0)
Code01_KruskalRebuild1.nodeKey = jarray('int', [Code01_KruskalRebuild1.MAXK])
Code01_KruskalRebuild1.cntu = jcast('int', 0)
Code01_KruskalRebuild1.dep = jarray('int', [Code01_KruskalRebuild1.MAXK])
Code01_KruskalRebuild1.stjump = jarray('int', [Code01_KruskalRebuild1.MAXK, Code01_KruskalRebuild1.MAXP])
Code01_KruskalRebuild1.ufe = jarray('int', [Code01_KruskalRebuild1.MAXK, 3])
Code01_KruskalRebuild1.stacksize = jcast('int', 0)
Code01_KruskalRebuild1.u = jcast('int', 0)
Code01_KruskalRebuild1.f = jcast('int', 0)
Code01_KruskalRebuild1.e = jcast('int', 0)

if __name__ == '__main__':
    Code01_KruskalRebuild1.main([])
