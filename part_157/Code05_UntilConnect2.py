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

# 加边直到连通，Python版
# 图里有n个点，m条无向边，点的编号1~n，边的编号1~m，所有点都连通
# 一共有q条查询，每条查询格式如下
# 查询 l r : 至少要加完编号前多少的边，才能使得[l, r]中的所有点连通
# 1 <= n <= 10^5
# 1 <= m、q <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF1706E
# 测试链接 : https://codeforces.com/problemset/problem/1706/E
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_UntilConnect2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 't': 't', 'n': 'n', 'm': 'm', 'q': 'q', 'edge': 'edge', 'father': 'father', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'nodeKey': 'nodeKey', 'cntu': 'cntu', 'dep': 'dep', 'dfn': 'dfn', 'seg': 'seg', 'stjump': 'stjump', 'cntd': 'cntd', 'lg2': 'lg2', 'stmax': 'stmax', 'stmin': 'stmin'}
    MAXN = 0
    MAXK = 0
    MAXM = 0
    MAXP = 0
    t = 0
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
    # 深度
    dep = None
    # dfn序
    dfn = None
    # seg[i] = j，代表树上节点的dfn序号为i，对应原始节点的编号为j
    seg = None
    # 树上的倍增表
    stjump = None
    # dfn序号的计数
    cntd = 0
    # 一维数组的倍增表，查询区间最大值、最小值
    lg2 = None
    stmax = None
    stmin = None
    @staticmethod
    def clear():
        Code05_UntilConnect2.cntg = jcast('int', jset(Code05_UntilConnect2, 'cntd', 0))
        jstatic('Arrays', 'fill', Code05_UntilConnect2.head, 1, jcast('int', (Code05_UntilConnect2.n * 2)), 0)

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code05_UntilConnect2.father[i]):
            jset(Code05_UntilConnect2.father, i, Code05_UntilConnect2.find(Code05_UntilConnect2.father[i]))
        return jcast('int', Code05_UntilConnect2.father[i])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code05_UntilConnect2.next, ((_java_obj_1 := Code05_UntilConnect2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_UntilConnect2.head[u])
        Code05_UntilConnect2.to[Code05_UntilConnect2.cntg] = jcast('int', v)
        Code05_UntilConnect2.head[u] = jcast('int', Code05_UntilConnect2.cntg)

    @staticmethod
    def kruskalRebuild():
        i = jcast('int', 1)
        while (i <= Code05_UntilConnect2.n):
            Code05_UntilConnect2.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_UntilConnect2.edge, 1, jcast('int', jadd(Code05_UntilConnect2.m, 1)), (lambda a, b: (a[2] - b[2])))
        Code05_UntilConnect2.cntu = jcast('int', Code05_UntilConnect2.n)
        i = jcast('int', 1)
        fx = 0
        fy = 0
        while (i <= Code05_UntilConnect2.m):
            fx = jcast('int', Code05_UntilConnect2.find(Code05_UntilConnect2.edge[i][0]))
            fy = jcast('int', Code05_UntilConnect2.find(Code05_UntilConnect2.edge[i][1]))
            if (fx != fy):
                jset(Code05_UntilConnect2.father, fx, jset(Code05_UntilConnect2.father, fy, ((_java_obj_4 := Code05_UntilConnect2), (_java_key_5 := 'cntu'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
                Code05_UntilConnect2.father[Code05_UntilConnect2.cntu] = jcast('int', Code05_UntilConnect2.cntu)
                Code05_UntilConnect2.nodeKey[Code05_UntilConnect2.cntu] = jcast('int', Code05_UntilConnect2.edge[i][2])
                Code05_UntilConnect2.addEdge(Code05_UntilConnect2.cntu, fx)
                Code05_UntilConnect2.addEdge(Code05_UntilConnect2.cntu, fy)
            i = jcast('int', (i + 1))

    @staticmethod
    def dfs(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code05_UntilConnect2.dep[u] = jcast('int', jcast('int', jadd(Code05_UntilConnect2.dep[fa], 1)))
        jset(Code05_UntilConnect2.dfn, u, ((_java_obj_7 := Code05_UntilConnect2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
        Code05_UntilConnect2.seg[Code05_UntilConnect2.cntd] = jcast('int', u)
        jset(Code05_UntilConnect2.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code05_UntilConnect2.MAXP):
            jset(Code05_UntilConnect2.stjump[u], p, Code05_UntilConnect2.stjump[Code05_UntilConnect2.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code05_UntilConnect2.head[u])
        while (e > 0):
            Code05_UntilConnect2.dfs(Code05_UntilConnect2.to[e], u)
            e = jcast('int', Code05_UntilConnect2.next[e])

    # 构建数组上的st表，讲解117进行了详细的讲述
    @staticmethod
    def buildst():
        Code05_UntilConnect2.lg2[0] = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= Code05_UntilConnect2.n):
            Code05_UntilConnect2.lg2[i] = jcast('int', jcast('int', jadd(Code05_UntilConnect2.lg2[jcast('int', (i >> (1 & 31)))], 1)))
            jset(Code05_UntilConnect2.stmax[i], 0, Code05_UntilConnect2.dfn[i])
            jset(Code05_UntilConnect2.stmin[i], 0, Code05_UntilConnect2.dfn[i])
            i = jcast('int', (i + 1))
        p = jcast('int', 1)
        while (p <= Code05_UntilConnect2.lg2[Code05_UntilConnect2.n]):
            i = jcast('int', 1)
            while (jcast('int', (jcast('int', jadd(i, jcast('int', (1 << (p & 31))))) - 1)) <= Code05_UntilConnect2.n):
                jset(Code05_UntilConnect2.stmax[i], p, jstatic('Math', 'max', Code05_UntilConnect2.stmax[i][jcast('int', (p - 1))], Code05_UntilConnect2.stmax[jcast('int', jadd(i, jcast('int', (1 << (jcast('int', (p - 1)) & 31)))))][jcast('int', (p - 1))]))
                jset(Code05_UntilConnect2.stmin[i], p, jstatic('Math', 'min', Code05_UntilConnect2.stmin[i][jcast('int', (p - 1))], Code05_UntilConnect2.stmin[jcast('int', jadd(i, jcast('int', (1 << (jcast('int', (p - 1)) & 31)))))][jcast('int', (p - 1))]))
                i = jcast('int', (i + 1))
            p = jcast('int', (p + 1))

    # 根据st表，[l..r]范围上的最小值，讲解117进行了详细的讲述
    @staticmethod
    def dfnmin(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        p = jcast('int', Code05_UntilConnect2.lg2[jcast('int', jadd(jcast('int', (r - l)), 1))])
        ans = jcast('int', jstatic('Math', 'min', Code05_UntilConnect2.stmin[l][p], Code05_UntilConnect2.stmin[jcast('int', jadd(jcast('int', (r - jcast('int', (1 << (p & 31))))), 1))][p]))
        return jcast('int', ans)

    # 根据st表，[l..r]范围上的最大值，讲解117进行了详细的讲述
    @staticmethod
    def dfnmax(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        p = jcast('int', Code05_UntilConnect2.lg2[jcast('int', jadd(jcast('int', (r - l)), 1))])
        ans = jcast('int', jstatic('Math', 'max', Code05_UntilConnect2.stmax[l][p], Code05_UntilConnect2.stmax[jcast('int', jadd(jcast('int', (r - jcast('int', (1 << (p & 31))))), 1))][p]))
        return jcast('int', ans)

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code05_UntilConnect2.dep[a] < Code05_UntilConnect2.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code05_UntilConnect2.MAXP - 1)))
        while (p >= 0):
            if (Code05_UntilConnect2.dep[Code05_UntilConnect2.stjump[a][p]] >= Code05_UntilConnect2.dep[b]):
                a = jcast('int', Code05_UntilConnect2.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code05_UntilConnect2.MAXP - 1)))
        while (p >= 0):
            if (Code05_UntilConnect2.stjump[a][p] != Code05_UntilConnect2.stjump[b][p]):
                a = jcast('int', Code05_UntilConnect2.stjump[a][p])
                b = jcast('int', Code05_UntilConnect2.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code05_UntilConnect2.stjump[a][0])

    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        x = jcast('int', Code05_UntilConnect2.seg[Code05_UntilConnect2.dfnmin(l, r)])
        y = jcast('int', Code05_UntilConnect2.seg[Code05_UntilConnect2.dfnmax(l, r)])
        return jcast('int', Code05_UntilConnect2.nodeKey[Code05_UntilConnect2.lca(x, y)])

    @staticmethod
    def main(args):
        io = Code05_UntilConnect2.FastIO(jget(System, 'in'), jget(System, 'out'), _java_ctor=0)
        Code05_UntilConnect2.t = jcast('int', jcall(io, 'nextInt'))
        test = jcast('int', 1)
        while (test <= Code05_UntilConnect2.t):
            Code05_UntilConnect2.n = jcast('int', jcall(io, 'nextInt'))
            Code05_UntilConnect2.m = jcast('int', jcall(io, 'nextInt'))
            Code05_UntilConnect2.q = jcast('int', jcall(io, 'nextInt'))
            i = jcast('int', 1)
            while (i <= Code05_UntilConnect2.m):
                jset(Code05_UntilConnect2.edge[i], 0, jcall(io, 'nextInt'))
                jset(Code05_UntilConnect2.edge[i], 1, jcall(io, 'nextInt'))
                jset(Code05_UntilConnect2.edge[i], 2, i)
                i = jcast('int', (i + 1))
            Code05_UntilConnect2.clear()
            Code05_UntilConnect2.kruskalRebuild()
            Code05_UntilConnect2.dfs(Code05_UntilConnect2.cntu, 0)
            Code05_UntilConnect2.buildst()
            i = jcast('int', 1)
            l = 0
            r = 0
            while (i <= Code05_UntilConnect2.q):
                l = jcast('int', jcall(io, 'nextInt'))
                r = jcast('int', jcall(io, 'nextInt'))
                if (l == r):
                    jcall(io, 'write', '0 ')
                else:
                    jcall(io, 'write', jadd(Code05_UntilConnect2.query(l, r), ' '))
                i = jcast('int', (i + 1))
            jcall(io, 'write', '\n')
            test = jcast('int', (test + 1))
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
                except Exception as _java_exception_10:
                    if jinstanceof(_java_exception_10, 'IOException'):
                        e = _java_exception_10
                        raise jnew('RuntimeException', e)
                    else:
                        raise
                if (self.lenbuf == jcast('int', (-1))):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', jcast('int', (self.inbuf[((_java_obj_11 := self), (_java_key_12 := 'ptrbuf'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]] & 255)))

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
            except Exception as _java_exception_14:
                if jinstanceof(_java_exception_14, 'IOException'):
                    e = _java_exception_14
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
            raise TypeError("No matching overload for Code05_UntilConnect2.FastIO.FastIO")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_UntilConnect2.MAXN = jcast('int', 100001)
Code05_UntilConnect2.MAXK = jcast('int', 200001)
Code05_UntilConnect2.MAXM = jcast('int', 200001)
Code05_UntilConnect2.MAXP = jcast('int', 20)
Code05_UntilConnect2.t = jcast('int', 0)
Code05_UntilConnect2.n = jcast('int', 0)
Code05_UntilConnect2.m = jcast('int', 0)
Code05_UntilConnect2.q = jcast('int', 0)
Code05_UntilConnect2.edge = jarray('int', [Code05_UntilConnect2.MAXM, 3])
Code05_UntilConnect2.father = jarray('int', [Code05_UntilConnect2.MAXK])
Code05_UntilConnect2.head = jarray('int', [Code05_UntilConnect2.MAXK])
Code05_UntilConnect2.next = jarray('int', [Code05_UntilConnect2.MAXK])
Code05_UntilConnect2.to = jarray('int', [Code05_UntilConnect2.MAXK])
Code05_UntilConnect2.cntg = jcast('int', 0)
Code05_UntilConnect2.nodeKey = jarray('int', [Code05_UntilConnect2.MAXK])
Code05_UntilConnect2.cntu = jcast('int', 0)
Code05_UntilConnect2.dep = jarray('int', [Code05_UntilConnect2.MAXK])
Code05_UntilConnect2.dfn = jarray('int', [Code05_UntilConnect2.MAXK])
Code05_UntilConnect2.seg = jarray('int', [Code05_UntilConnect2.MAXK])
Code05_UntilConnect2.stjump = jarray('int', [Code05_UntilConnect2.MAXK, Code05_UntilConnect2.MAXP])
Code05_UntilConnect2.cntd = jcast('int', 0)
Code05_UntilConnect2.lg2 = jarray('int', [Code05_UntilConnect2.MAXN])
Code05_UntilConnect2.stmax = jarray('int', [Code05_UntilConnect2.MAXN, Code05_UntilConnect2.MAXP])
Code05_UntilConnect2.stmin = jarray('int', [Code05_UntilConnect2.MAXN, Code05_UntilConnect2.MAXP])

if __name__ == '__main__':
    Code05_UntilConnect2.main([])
