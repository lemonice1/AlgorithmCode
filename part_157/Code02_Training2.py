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

# youyou的军训，Python版
# 图里有n个点，m条无向边，每条边给定不同的边权，图里可能有若干个连通的部分
# 一开始limit = 0，接下来有q条操作，每种操作的格式如下
# 操作 1 x   : 所有修改操作生效，然后limit设置成x
# 操作 2 x   : 从点x出发，只能走 边权 >= limit 的边，查询最多到达几个点
# 操作 3 x y : 第x条边的边权修改为y，不是立刻生效，等到下次操作1发生时生效
# 题目保证边权不管如何修改，所有边权都不相等，并且每条边的边权排名不发生变化
# 1 <= n、m、q <= 4 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P9638
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Training2:
    __java_fields__ = {'MAXK': 'MAXK', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'q': 'q', 'edge': 'edge', 'edgeToTree': 'edgeToTree', 'pendEdge': 'pendEdge', 'pendVal': 'pendVal', 'cntp': 'cntp', 'father': 'father', 'stack': 'stack', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'nodeKey': 'nodeKey', 'cntu': 'cntu', 'leafsiz': 'leafsiz', 'stjump': 'stjump', 'ufe': 'ufe', 'stacksize': 'stacksize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXK = 0
    MAXM = 0
    MAXP = 0
    n = 0
    m = 0
    q = 0
    # 每条边的信息，节点u、节点v、边权w、边的编号i
    edge = None
    # 边的编号对应重构树上的点的编号
    edgeToTree = None
    # 边权的修改操作先不生效，等到下次操作1发生时生效
    # 修改了哪些边
    pendEdge = None
    # 修改成了什么边权
    pendVal = None
    # 修改操作的个数
    cntp = 0
    # 并查集
    father = None
    stack = None
    # Kruskal重构树
    head = None
    next = None
    to = None
    cntg = 0
    nodeKey = None
    cntu = 0
    # 树上dfs，Kruskal重构树的节点，子树上面有几个叶节点
    leafsiz = None
    # 树上dfs，Kruskal重构树的节点，倍增表
    stjump = None
    # 并查集的find方法：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def find(i):
        i = jcast('int', i)
        size = jcast('int', 0)
        while (i != Code02_Training2.father[i]):
            jset(Code02_Training2.stack, ((_java_old_1 := size), (size := jcast('int', (size + (1)))), _java_old_1)[2], i)
            i = jcast('int', Code02_Training2.father[i])
        while (size > 0):
            jset(Code02_Training2.father, Code02_Training2.stack[(size := jcast('int', (size + (-1))))], i)
        return jcast('int', i)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_Training2.next, ((_java_obj_2 := Code02_Training2), (_java_key_3 := 'cntg'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))))[3], Code02_Training2.head[u])
        Code02_Training2.to[Code02_Training2.cntg] = jcast('int', v)
        Code02_Training2.head[u] = jcast('int', Code02_Training2.cntg)

    @staticmethod
    def kruskalRebuild():
        i = jcast('int', 1)
        while (i <= Code02_Training2.n):
            Code02_Training2.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_Training2.edge, 1, jcast('int', jadd(Code02_Training2.m, 1)), (lambda a, b: (b[2] - a[2])))
        Code02_Training2.cntu = jcast('int', Code02_Training2.n)
        i = jcast('int', 1)
        fx = 0
        fy = 0
        while (i <= Code02_Training2.m):
            fx = jcast('int', Code02_Training2.find(Code02_Training2.edge[i][0]))
            fy = jcast('int', Code02_Training2.find(Code02_Training2.edge[i][1]))
            if (fx != fy):
                jset(Code02_Training2.father, fx, jset(Code02_Training2.father, fy, ((_java_obj_5 := Code02_Training2), (_java_key_6 := 'cntu'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))))[3]))
                Code02_Training2.father[Code02_Training2.cntu] = jcast('int', Code02_Training2.cntu)
                Code02_Training2.nodeKey[Code02_Training2.cntu] = jcast('int', Code02_Training2.edge[i][2])
                Code02_Training2.addEdge(Code02_Training2.cntu, fx)
                Code02_Training2.addEdge(Code02_Training2.cntu, fy)
                jset(Code02_Training2.edgeToTree, Code02_Training2.edge[i][3], Code02_Training2.cntu)
            i = jcast('int', (i + 1))

    # dfs1是递归函数：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code02_Training2.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code02_Training2.MAXP):
            jset(Code02_Training2.stjump[u], p, Code02_Training2.stjump[Code02_Training2.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code02_Training2.head[u])
        while (e > 0):
            Code02_Training2.dfs1(Code02_Training2.to[e], u)
            e = jcast('int', Code02_Training2.next[e])
        if (u <= Code02_Training2.n):
            Code02_Training2.leafsiz[u] = jcast('int', 1)
        else:
            Code02_Training2.leafsiz[u] = jcast('int', 0)
        e = jcast('int', Code02_Training2.head[u])
        while (e > 0):
            Code02_Training2.leafsiz[u] = jcast('int', jcast('int', jadd(Code02_Training2.leafsiz[u], Code02_Training2.leafsiz[Code02_Training2.to[e]])))
            e = jcast('int', Code02_Training2.next[e])

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
        jset(Code02_Training2.ufe[Code02_Training2.stacksize], 0, u)
        jset(Code02_Training2.ufe[Code02_Training2.stacksize], 1, f)
        jset(Code02_Training2.ufe[Code02_Training2.stacksize], 2, e)
        Code02_Training2.stacksize = jcast('int', (Code02_Training2.stacksize + 1))

    @staticmethod
    def pop():
        Code02_Training2.stacksize = jcast('int', (Code02_Training2.stacksize - 1))
        Code02_Training2.u = jcast('int', Code02_Training2.ufe[Code02_Training2.stacksize][0])
        Code02_Training2.f = jcast('int', Code02_Training2.ufe[Code02_Training2.stacksize][1])
        Code02_Training2.e = jcast('int', Code02_Training2.ufe[Code02_Training2.stacksize][2])

    # dfs2是dfs1的迭代版
    @staticmethod
    def dfs2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code02_Training2.stacksize = jcast('int', 0)
        Code02_Training2.push(cur, fa, jcast('int', (-1)))
        while (Code02_Training2.stacksize > 0):
            Code02_Training2.pop()
            if (Code02_Training2.e == jcast('int', (-1))):
                jset(Code02_Training2.stjump[Code02_Training2.u], 0, Code02_Training2.f)
                p = jcast('int', 1)
                while (p < Code02_Training2.MAXP):
                    jset(Code02_Training2.stjump[Code02_Training2.u], p, Code02_Training2.stjump[Code02_Training2.stjump[Code02_Training2.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code02_Training2.e = jcast('int', Code02_Training2.head[Code02_Training2.u])
            else:
                Code02_Training2.e = jcast('int', Code02_Training2.next[Code02_Training2.e])
            if (Code02_Training2.e != 0):
                Code02_Training2.push(Code02_Training2.u, Code02_Training2.f, Code02_Training2.e)
                Code02_Training2.push(Code02_Training2.to[Code02_Training2.e], Code02_Training2.u, jcast('int', (-1)))
            else:
                if (Code02_Training2.u <= Code02_Training2.n):
                    Code02_Training2.leafsiz[Code02_Training2.u] = jcast('int', 1)
                else:
                    Code02_Training2.leafsiz[Code02_Training2.u] = jcast('int', 0)
                ei = jcast('int', Code02_Training2.head[Code02_Training2.u])
                while (ei > 0):
                    Code02_Training2.leafsiz[Code02_Training2.u] = jcast('int', jcast('int', jadd(Code02_Training2.leafsiz[Code02_Training2.u], Code02_Training2.leafsiz[Code02_Training2.to[ei]])))
                    ei = jcast('int', Code02_Training2.next[ei])

    @staticmethod
    def query(u, limit):
        u = jcast('int', u)
        limit = jcast('int', limit)
        p = jcast('int', jcast('int', (Code02_Training2.MAXP - 1)))
        while (p >= 0):
            if ((Code02_Training2.stjump[u][p] > 0) and (Code02_Training2.nodeKey[Code02_Training2.stjump[u][p]] >= limit)):
                u = jcast('int', Code02_Training2.stjump[u][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code02_Training2.leafsiz[u])

    @staticmethod
    def main(args):
        io = Code02_Training2.FastIO(jget(System, 'in'), jget(System, 'out'), _java_ctor=0)
        Code02_Training2.n = jcast('int', jcall(io, 'nextInt'))
        Code02_Training2.m = jcast('int', jcall(io, 'nextInt'))
        Code02_Training2.q = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_Training2.m):
            jset(Code02_Training2.edge[i], 0, jcall(io, 'nextInt'))
            jset(Code02_Training2.edge[i], 1, jcall(io, 'nextInt'))
            jset(Code02_Training2.edge[i], 2, jcall(io, 'nextInt'))
            jset(Code02_Training2.edge[i], 3, i)
            i = jcast('int', (i + 1))
        Code02_Training2.kruskalRebuild()
        i = jcast('int', 1)
        while (i <= Code02_Training2.cntu):
            if (i == Code02_Training2.father[i]):
                Code02_Training2.dfs2(i, 0)
            i = jcast('int', (i + 1))
        op = 0
        x = 0
        y = 0
        limit = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code02_Training2.q):
            op = jcast('int', jcall(io, 'nextInt'))
            if (op == 1):
                # 收集的修改操作生效
                k = jcast('int', 1)
                while (k <= Code02_Training2.cntp):
                    jset(Code02_Training2.nodeKey, Code02_Training2.edgeToTree[Code02_Training2.pendEdge[k]], Code02_Training2.pendVal[k])
                    k = jcast('int', (k + 1))
                Code02_Training2.cntp = jcast('int', 0)
                limit = jcast('int', jcall(io, 'nextInt'))
            else:
                if (op == 2):
                    x = jcast('int', jcall(io, 'nextInt'))
                    jcall(io, 'writelnInt', Code02_Training2.query(x, limit))
                else:
                    x = jcast('int', jcall(io, 'nextInt'))
                    y = jcast('int', jcall(io, 'nextInt'))
                    # 收集修改操作
                    if (Code02_Training2.edgeToTree[x] != 0):
                        jset(Code02_Training2.pendEdge, ((_java_obj_8 := Code02_Training2), (_java_key_9 := 'cntp'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3], x)
                        Code02_Training2.pendVal[Code02_Training2.cntp] = jcast('int', y)
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
                except Exception as _java_exception_11:
                    if jinstanceof(_java_exception_11, 'IOException'):
                        e = _java_exception_11
                        raise jnew('RuntimeException', e)
                    else:
                        raise
                if (self.lenbuf == jcast('int', (-1))):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', jcast('int', (self.inbuf[((_java_obj_12 := self), (_java_key_13 := 'ptrbuf'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))), _java_old_14)[4]] & 255)))

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
            except Exception as _java_exception_15:
                if jinstanceof(_java_exception_15, 'IOException'):
                    e = _java_exception_15
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
            raise TypeError("No matching overload for Code02_Training2.FastIO.FastIO")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Training2.MAXK = jcast('int', 800001)
Code02_Training2.MAXM = jcast('int', 400001)
Code02_Training2.MAXP = jcast('int', 20)
Code02_Training2.n = jcast('int', 0)
Code02_Training2.m = jcast('int', 0)
Code02_Training2.q = jcast('int', 0)
Code02_Training2.edge = jarray('int', [Code02_Training2.MAXM, 4])
Code02_Training2.edgeToTree = jarray('int', [Code02_Training2.MAXM])
Code02_Training2.pendEdge = jarray('int', [Code02_Training2.MAXM])
Code02_Training2.pendVal = jarray('int', [Code02_Training2.MAXM])
Code02_Training2.cntp = jcast('int', 0)
Code02_Training2.father = jarray('int', [Code02_Training2.MAXK])
Code02_Training2.stack = jarray('int', [Code02_Training2.MAXK])
Code02_Training2.head = jarray('int', [Code02_Training2.MAXK])
Code02_Training2.next = jarray('int', [Code02_Training2.MAXK])
Code02_Training2.to = jarray('int', [Code02_Training2.MAXK])
Code02_Training2.cntg = jcast('int', 0)
Code02_Training2.nodeKey = jarray('int', [Code02_Training2.MAXK])
Code02_Training2.cntu = jcast('int', 0)
Code02_Training2.leafsiz = jarray('int', [Code02_Training2.MAXK])
Code02_Training2.stjump = jarray('int', [Code02_Training2.MAXK, Code02_Training2.MAXP])
Code02_Training2.ufe = jarray('int', [Code02_Training2.MAXK, 3])
Code02_Training2.stacksize = jcast('int', 0)
Code02_Training2.u = jcast('int', 0)
Code02_Training2.f = jcast('int', 0)
Code02_Training2.e = jcast('int', 0)

if __name__ == '__main__':
    Code02_Training2.main([])
