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

# 归程，Python版
# 一共有n个点，m条无向边，原图连通，每条边有长度l和海拔a
# 一共有q条查询，格式如下
# 查询 x y : 起初走过海拔 > y的边免费，可视为开车，但是车不能走海拔 <= y的边
# 你可以在任意节点下车，车不能再用
# 下车后经过每条边的长度(包括海拔 > y 的边)，都算入步行长度
# 你想从点x到1号点，打印最小步行长度
# 1 <= n <= 2 * 10^5
# 1 <= m、q <= 4 * 10^5
# 本题要求强制在线，具体规定请打开测试链接查看
# 测试链接 : https://www.luogu.com.cn/problem/P4768
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Journey1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 'INF': 'INF', 't': 't', 'n': 'n', 'm': 'm', 'q': 'q', 'k': 'k', 's': 's', 'edge': 'edge', 'headg': 'headg', 'nextg': 'nextg', 'tog': 'tog', 'weightg': 'weightg', 'cntg': 'cntg', 'dist': 'dist', 'visit': 'visit', 'heap': 'heap', 'father': 'father', 'stack': 'stack', 'headk': 'headk', 'nextk': 'nextk', 'tok': 'tok', 'cntk': 'cntk', 'nodeKey': 'nodeKey', 'cntu': 'cntu', 'mindist': 'mindist', 'stjump': 'stjump', 'ufe': 'ufe', 'stacksize': 'stacksize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    MAXK = 0
    MAXM = 0
    MAXP = 0
    INF = 0
    t = 0
    n = 0
    m = 0
    q = 0
    k = 0
    s = 0
    edge = None
    # 建图
    headg = None
    nextg = None
    tog = None
    weightg = None
    cntg = 0
    # dijkstra算法
    dist = None
    visit = None
    heap = None
    # 并查集
    father = None
    stack = None
    # Kruskal重构树
    headk = None
    nextk = None
    tok = None
    cntk = 0
    nodeKey = None
    cntu = 0
    # 树上dfs，Kruskal重构树的节点，子树中的所有点，走到1号节点的最小距离
    mindist = None
    # 树上dfs，Kruskal重构树的节点，倍增表
    stjump = None
    @staticmethod
    def clear():
        Code04_Journey1.cntg = jcast('int', jset(Code04_Journey1, 'cntk', 0))
        jstatic('Arrays', 'fill', Code04_Journey1.headg, 1, jcast('int', jadd(Code04_Journey1.n, 1)), 0)
        jstatic('Arrays', 'fill', Code04_Journey1.headk, 1, jcast('int', (Code04_Journey1.n * 2)), 0)

    @staticmethod
    def addEdgeG(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code04_Journey1.nextg, ((_java_obj_1 := Code04_Journey1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_Journey1.headg[u])
        Code04_Journey1.tog[Code04_Journey1.cntg] = jcast('int', v)
        Code04_Journey1.weightg[Code04_Journey1.cntg] = jcast('int', w)
        Code04_Journey1.headg[u] = jcast('int', Code04_Journey1.cntg)

    @staticmethod
    def dijkstra():
        i = jcast('int', 1)
        while (i <= Code04_Journey1.m):
            Code04_Journey1.addEdgeG(Code04_Journey1.edge[i][0], Code04_Journey1.edge[i][1], Code04_Journey1.edge[i][2])
            Code04_Journey1.addEdgeG(Code04_Journey1.edge[i][1], Code04_Journey1.edge[i][0], Code04_Journey1.edge[i][2])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'fill', Code04_Journey1.dist, 1, jcast('int', jadd(Code04_Journey1.n, 1)), Code04_Journey1.INF)
        jstatic('Arrays', 'fill', Code04_Journey1.visit, 1, jcast('int', jadd(Code04_Journey1.n, 1)), False)
        Code04_Journey1.dist[1] = jcast('int', 0)
        jcall(Code04_Journey1.heap, 'add', jarray('int', [None], [1, 0]))
        cur = None
        x = 0
        v = 0
        while (not jcall(Code04_Journey1.heap, 'isEmpty')):
            cur = jcall(Code04_Journey1.heap, 'poll')
            x = jcast('int', cur[0])
            v = jcast('int', cur[1])
            if (not Code04_Journey1.visit[x]):
                Code04_Journey1.visit[x] = jcast('boolean', True)
                e = jcast('int', Code04_Journey1.headg[x])
                y = 0
                w = 0
                while (e > 0):
                    y = jcast('int', Code04_Journey1.tog[e])
                    w = jcast('int', Code04_Journey1.weightg[e])
                    if ((not Code04_Journey1.visit[y]) and (Code04_Journey1.dist[y] > jcast('int', jadd(v, w)))):
                        Code04_Journey1.dist[y] = jcast('int', jcast('int', jadd(v, w)))
                        jcall(Code04_Journey1.heap, 'add', jarray('int', [None], [y, Code04_Journey1.dist[y]]))
                    e = jcast('int', Code04_Journey1.nextg[e])

    @staticmethod
    def addEdgeK(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_Journey1.nextk, ((_java_obj_4 := Code04_Journey1), (_java_key_5 := 'cntk'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code04_Journey1.headk[u])
        Code04_Journey1.tok[Code04_Journey1.cntk] = jcast('int', v)
        Code04_Journey1.headk[u] = jcast('int', Code04_Journey1.cntk)

    # 并查集的find方法：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def find(i):
        i = jcast('int', i)
        size = jcast('int', 0)
        while (i != Code04_Journey1.father[i]):
            jset(Code04_Journey1.stack, ((_java_old_7 := size), (size := jcast('int', (size + (1)))), _java_old_7)[2], i)
            i = jcast('int', Code04_Journey1.father[i])
        while (size > 0):
            jset(Code04_Journey1.father, Code04_Journey1.stack[(size := jcast('int', (size + (-1))))], i)
        return jcast('int', i)

    @staticmethod
    def kruskalRebuild():
        i = jcast('int', 1)
        while (i <= Code04_Journey1.n):
            Code04_Journey1.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_Journey1.edge, 1, jcast('int', jadd(Code04_Journey1.m, 1)), (lambda a, b: (b[3] - a[3])))
        Code04_Journey1.cntu = jcast('int', Code04_Journey1.n)
        i = jcast('int', 1)
        fx = 0
        fy = 0
        while (i <= Code04_Journey1.m):
            fx = jcast('int', Code04_Journey1.find(Code04_Journey1.edge[i][0]))
            fy = jcast('int', Code04_Journey1.find(Code04_Journey1.edge[i][1]))
            if (fx != fy):
                jset(Code04_Journey1.father, fx, jset(Code04_Journey1.father, fy, ((_java_obj_8 := Code04_Journey1), (_java_key_9 := 'cntu'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3]))
                Code04_Journey1.father[Code04_Journey1.cntu] = jcast('int', Code04_Journey1.cntu)
                Code04_Journey1.nodeKey[Code04_Journey1.cntu] = jcast('int', Code04_Journey1.edge[i][3])
                Code04_Journey1.addEdgeK(Code04_Journey1.cntu, fx)
                Code04_Journey1.addEdgeK(Code04_Journey1.cntu, fy)
            i = jcast('int', (i + 1))

    # dfs1是递归函数：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code04_Journey1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code04_Journey1.MAXP):
            jset(Code04_Journey1.stjump[u], p, Code04_Journey1.stjump[Code04_Journey1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code04_Journey1.headk[u])
        while (e > 0):
            Code04_Journey1.dfs1(Code04_Journey1.tok[e], u)
            e = jcast('int', Code04_Journey1.nextk[e])
        if (u <= Code04_Journey1.n):
            Code04_Journey1.mindist[u] = jcast('int', Code04_Journey1.dist[u])
        else:
            Code04_Journey1.mindist[u] = jcast('int', Code04_Journey1.INF)
        e = jcast('int', Code04_Journey1.headk[u])
        while (e > 0):
            jset(Code04_Journey1.mindist, u, jstatic('Math', 'min', Code04_Journey1.mindist[u], Code04_Journey1.mindist[Code04_Journey1.tok[e]]))
            e = jcast('int', Code04_Journey1.nextk[e])

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
        jset(Code04_Journey1.ufe[Code04_Journey1.stacksize], 0, u)
        jset(Code04_Journey1.ufe[Code04_Journey1.stacksize], 1, f)
        jset(Code04_Journey1.ufe[Code04_Journey1.stacksize], 2, e)
        Code04_Journey1.stacksize = jcast('int', (Code04_Journey1.stacksize + 1))

    @staticmethod
    def pop():
        Code04_Journey1.stacksize = jcast('int', (Code04_Journey1.stacksize - 1))
        Code04_Journey1.u = jcast('int', Code04_Journey1.ufe[Code04_Journey1.stacksize][0])
        Code04_Journey1.f = jcast('int', Code04_Journey1.ufe[Code04_Journey1.stacksize][1])
        Code04_Journey1.e = jcast('int', Code04_Journey1.ufe[Code04_Journey1.stacksize][2])

    # dfs2是dfs1的迭代版
    @staticmethod
    def dfs2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code04_Journey1.stacksize = jcast('int', 0)
        Code04_Journey1.push(cur, fa, jcast('int', (-1)))
        while (Code04_Journey1.stacksize > 0):
            Code04_Journey1.pop()
            if (Code04_Journey1.e == jcast('int', (-1))):
                jset(Code04_Journey1.stjump[Code04_Journey1.u], 0, Code04_Journey1.f)
                p = jcast('int', 1)
                while (p < Code04_Journey1.MAXP):
                    jset(Code04_Journey1.stjump[Code04_Journey1.u], p, Code04_Journey1.stjump[Code04_Journey1.stjump[Code04_Journey1.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code04_Journey1.e = jcast('int', Code04_Journey1.headk[Code04_Journey1.u])
            else:
                Code04_Journey1.e = jcast('int', Code04_Journey1.nextk[Code04_Journey1.e])
            if (Code04_Journey1.e != 0):
                Code04_Journey1.push(Code04_Journey1.u, Code04_Journey1.f, Code04_Journey1.e)
                Code04_Journey1.push(Code04_Journey1.tok[Code04_Journey1.e], Code04_Journey1.u, jcast('int', (-1)))
            else:
                if (Code04_Journey1.u <= Code04_Journey1.n):
                    Code04_Journey1.mindist[Code04_Journey1.u] = jcast('int', Code04_Journey1.dist[Code04_Journey1.u])
                else:
                    Code04_Journey1.mindist[Code04_Journey1.u] = jcast('int', Code04_Journey1.INF)
                ei = jcast('int', Code04_Journey1.headk[Code04_Journey1.u])
                while (ei > 0):
                    jset(Code04_Journey1.mindist, Code04_Journey1.u, jstatic('Math', 'min', Code04_Journey1.mindist[Code04_Journey1.u], Code04_Journey1.mindist[Code04_Journey1.tok[ei]]))
                    ei = jcast('int', Code04_Journey1.nextk[ei])

    @staticmethod
    def query(node, line):
        node = jcast('int', node)
        line = jcast('int', line)
        p = jcast('int', jcast('int', (Code04_Journey1.MAXP - 1)))
        while (p >= 0):
            if ((Code04_Journey1.stjump[node][p] > 0) and (Code04_Journey1.nodeKey[Code04_Journey1.stjump[node][p]] > line)):
                node = jcast('int', Code04_Journey1.stjump[node][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code04_Journey1.mindist[node])

    @staticmethod
    def main(args):
        io = Code04_Journey1.FastIO(jget(System, 'in'), jget(System, 'out'), _java_ctor=0)
        Code04_Journey1.t = jcast('int', jcall(io, 'nextInt'))
        test = jcast('int', 1)
        while (test <= Code04_Journey1.t):
            Code04_Journey1.n = jcast('int', jcall(io, 'nextInt'))
            Code04_Journey1.m = jcast('int', jcall(io, 'nextInt'))
            Code04_Journey1.clear()
            i = jcast('int', 1)
            while (i <= Code04_Journey1.m):
                jset(Code04_Journey1.edge[i], 0, jcall(io, 'nextInt'))
                jset(Code04_Journey1.edge[i], 1, jcall(io, 'nextInt'))
                jset(Code04_Journey1.edge[i], 2, jcall(io, 'nextInt'))
                jset(Code04_Journey1.edge[i], 3, jcall(io, 'nextInt'))
                i = jcast('int', (i + 1))
            Code04_Journey1.dijkstra()
            Code04_Journey1.kruskalRebuild()
            Code04_Journey1.dfs2(Code04_Journey1.cntu, 0)
            Code04_Journey1.q = jcast('int', jcall(io, 'nextInt'))
            Code04_Journey1.k = jcast('int', jcall(io, 'nextInt'))
            Code04_Journey1.s = jcast('int', jcall(io, 'nextInt'))
            i = jcast('int', 1)
            x = 0
            y = 0
            lastAns = jcast('int', 0)
            while (i <= Code04_Journey1.q):
                x = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', (jcast('int', jadd(jcall(io, 'nextInt'), jcast('int', (Code04_Journey1.k * lastAns)))) - 1)), Code04_Journey1.n)), 1)))
                y = jcast('int', jcast('int', jmod(jcast('int', jadd(jcall(io, 'nextInt'), jcast('int', (Code04_Journey1.k * lastAns)))), jcast('int', jadd(Code04_Journey1.s, 1)))))
                lastAns = jcast('int', Code04_Journey1.query(x, y))
                jcall(io, 'writelnInt', lastAns)
                i = jcast('int', (i + 1))
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
            raise TypeError("No matching overload for Code04_Journey1.FastIO.FastIO")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Journey1.MAXN = jcast('int', 200001)
Code04_Journey1.MAXK = jcast('int', 400001)
Code04_Journey1.MAXM = jcast('int', 400001)
Code04_Journey1.MAXP = jcast('int', 20)
Code04_Journey1.INF = jcast('int', 2000000001)
Code04_Journey1.t = jcast('int', 0)
Code04_Journey1.n = jcast('int', 0)
Code04_Journey1.m = jcast('int', 0)
Code04_Journey1.q = jcast('int', 0)
Code04_Journey1.k = jcast('int', 0)
Code04_Journey1.s = jcast('int', 0)
Code04_Journey1.edge = jarray('int', [Code04_Journey1.MAXM, 4])
Code04_Journey1.headg = jarray('int', [Code04_Journey1.MAXN])
Code04_Journey1.nextg = jarray('int', [jcast('int', (Code04_Journey1.MAXM << (1 & 31)))])
Code04_Journey1.tog = jarray('int', [jcast('int', (Code04_Journey1.MAXM << (1 & 31)))])
Code04_Journey1.weightg = jarray('int', [jcast('int', (Code04_Journey1.MAXM << (1 & 31)))])
Code04_Journey1.cntg = jcast('int', 0)
Code04_Journey1.dist = jarray('int', [Code04_Journey1.MAXN])
Code04_Journey1.visit = jarray('boolean', [Code04_Journey1.MAXN])
Code04_Journey1.heap = jnew('PriorityQueue', (lambda a, b: (a[1] - b[1])))
Code04_Journey1.father = jarray('int', [Code04_Journey1.MAXK])
Code04_Journey1.stack = jarray('int', [Code04_Journey1.MAXK])
Code04_Journey1.headk = jarray('int', [Code04_Journey1.MAXK])
Code04_Journey1.nextk = jarray('int', [Code04_Journey1.MAXK])
Code04_Journey1.tok = jarray('int', [Code04_Journey1.MAXK])
Code04_Journey1.cntk = jcast('int', 0)
Code04_Journey1.nodeKey = jarray('int', [Code04_Journey1.MAXK])
Code04_Journey1.cntu = jcast('int', 0)
Code04_Journey1.mindist = jarray('int', [Code04_Journey1.MAXK])
Code04_Journey1.stjump = jarray('int', [Code04_Journey1.MAXK, Code04_Journey1.MAXP])
Code04_Journey1.ufe = jarray('int', [Code04_Journey1.MAXK, 3])
Code04_Journey1.stacksize = jcast('int', 0)
Code04_Journey1.u = jcast('int', 0)
Code04_Journey1.f = jcast('int', 0)
Code04_Journey1.e = jcast('int', 0)

if __name__ == '__main__':
    Code04_Journey1.main([])
