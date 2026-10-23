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

# 边权上限内第k大点权，Python版
# 图里有n个点，m条无向边，点有点权，边有边权，图里可能有若干个连通的部分
# 一共有q条查询，查询格式如下
# 查询 u x k : 从点u开始，只能走过权值<=x的边
# 所有能到达的点中，打印第k大点权，如果不存在打印-1
# 1 <= n <= 10^5
# 0 <= m、q <= 5 * 10^5
# 1 <= 点权、边权 <= 10^9
# 本题要求强制在线，具体规定请打开测试链接查看
# 测试链接 : https://www.luogu.com.cn/problem/P7834
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 本实现包含较大的数组或状态集合，内存开销取决于数据规模和 Python 容器表示
# 对应实现可参考 Code07_Peaks2.py
# 两个版本保留相同的算法逻辑
class Code07_Peaks1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 'MAXM': 'MAXM', 'MAXT': 'MAXT', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'q': 'q', 's': 's', 'node': 'node', 'sorted': 'sorted', 'edge': 'edge', 'father': 'father', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'nodeKey': 'nodeKey', 'cntu': 'cntu', 'stjump': 'stjump', 'leafsiz': 'leafsiz', 'leafDfnMin': 'leafDfnMin', 'leafseg': 'leafseg', 'cntd': 'cntd', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'numcnt': 'numcnt', 'cntt': 'cntt'}
    MAXN = 0
    MAXK = 0
    MAXM = 0
    MAXT = 0
    MAXP = 0
    n = 0
    m = 0
    q = 0
    s = 0
    node = None
    sorted = None
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
    # 倍增表
    stjump = None
    # 子树上的叶节点个数
    leafsiz = None
    # 子树上叶节点的dfn序号最小值
    leafDfnMin = None
    # leafseg[i] = j，表示dfn序号为i的叶节点，原始编号为j
    leafseg = None
    # dfn的计数
    cntd = 0
    # 可持久化线段树
    # 线段树的下标为某个数字，所以是值域线段树
    # 数值范围[l..r]上，一共有几个数字，就是numcnt的含义
    root = None
    ls = None
    rs = None
    numcnt = None
    cntt = 0
    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code07_Peaks1.s)
        mid = 0
        while (left <= right):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(left, right)), 2)))
            if (Code07_Peaks1.sorted[mid] == num):
                return jcast('int', mid)
            else:
                if (Code07_Peaks1.sorted[mid] < num):
                    left = jcast('int', jcast('int', jadd(mid, 1)))
                else:
                    right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code07_Peaks1.n):
            Code07_Peaks1.sorted[i] = jcast('int', Code07_Peaks1.node[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code07_Peaks1.sorted, 1, jcast('int', jadd(Code07_Peaks1.n, 1)))
        Code07_Peaks1.s = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code07_Peaks1.n):
            if (Code07_Peaks1.sorted[Code07_Peaks1.s] != Code07_Peaks1.sorted[i]):
                jset(Code07_Peaks1.sorted, ((_java_obj_1 := Code07_Peaks1), (_java_key_2 := 's'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_Peaks1.sorted[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_Peaks1.n):
            jset(Code07_Peaks1.node, i, Code07_Peaks1.kth(Code07_Peaks1.node[i]))
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_Peaks1.next, ((_java_obj_4 := Code07_Peaks1), (_java_key_5 := 'cntg'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code07_Peaks1.head[u])
        Code07_Peaks1.to[Code07_Peaks1.cntg] = jcast('int', v)
        Code07_Peaks1.head[u] = jcast('int', Code07_Peaks1.cntg)

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code07_Peaks1.father[i]):
            jset(Code07_Peaks1.father, i, Code07_Peaks1.find(Code07_Peaks1.father[i]))
        return jcast('int', Code07_Peaks1.father[i])

    @staticmethod
    def kruskalRebuild():
        i = jcast('int', 1)
        while (i <= Code07_Peaks1.n):
            Code07_Peaks1.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code07_Peaks1.edge, 1, jcast('int', jadd(Code07_Peaks1.m, 1)), (lambda a, b: (a[2] - b[2])))
        Code07_Peaks1.cntu = jcast('int', Code07_Peaks1.n)
        i = jcast('int', 1)
        fx = 0
        fy = 0
        while (i <= Code07_Peaks1.m):
            fx = jcast('int', Code07_Peaks1.find(Code07_Peaks1.edge[i][0]))
            fy = jcast('int', Code07_Peaks1.find(Code07_Peaks1.edge[i][1]))
            if (fx != fy):
                jset(Code07_Peaks1.father, fx, jset(Code07_Peaks1.father, fy, ((_java_obj_7 := Code07_Peaks1), (_java_key_8 := 'cntu'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
                Code07_Peaks1.father[Code07_Peaks1.cntu] = jcast('int', Code07_Peaks1.cntu)
                Code07_Peaks1.nodeKey[Code07_Peaks1.cntu] = jcast('int', Code07_Peaks1.edge[i][2])
                Code07_Peaks1.addEdge(Code07_Peaks1.cntu, fx)
                Code07_Peaks1.addEdge(Code07_Peaks1.cntu, fy)
            i = jcast('int', (i + 1))

    @staticmethod
    def dfs(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code07_Peaks1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code07_Peaks1.MAXP):
            jset(Code07_Peaks1.stjump[u], p, Code07_Peaks1.stjump[Code07_Peaks1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code07_Peaks1.head[u])
        while (e > 0):
            Code07_Peaks1.dfs(Code07_Peaks1.to[e], u)
            e = jcast('int', Code07_Peaks1.next[e])
        if (u <= Code07_Peaks1.n):
            Code07_Peaks1.leafsiz[u] = jcast('int', 1)
            jset(Code07_Peaks1.leafDfnMin, u, ((_java_obj_10 := Code07_Peaks1), (_java_key_11 := 'cntd'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
            Code07_Peaks1.leafseg[Code07_Peaks1.cntd] = jcast('int', u)
        else:
            Code07_Peaks1.leafsiz[u] = jcast('int', 0)
            Code07_Peaks1.leafDfnMin[u] = jcast('int', jcast('int', jadd(Code07_Peaks1.n, 1)))
        e = jcast('int', Code07_Peaks1.head[u])
        while (e > 0):
            Code07_Peaks1.leafsiz[u] = jcast('int', jcast('int', jadd(Code07_Peaks1.leafsiz[u], Code07_Peaks1.leafsiz[Code07_Peaks1.to[e]])))
            jset(Code07_Peaks1.leafDfnMin, u, jstatic('Math', 'min', Code07_Peaks1.leafDfnMin[u], Code07_Peaks1.leafDfnMin[Code07_Peaks1.to[e]]))
            e = jcast('int', Code07_Peaks1.next[e])

    # 可持久化线段树的build
    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_13 := Code07_Peaks1), (_java_key_14 := 'cntt'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
        Code07_Peaks1.numcnt[rt] = jcast('int', 0)
        if (l < r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            jset(Code07_Peaks1.ls, rt, Code07_Peaks1.build(l, mid))
            jset(Code07_Peaks1.rs, rt, Code07_Peaks1.build(jcast('int', jadd(mid, 1)), r))
        return jcast('int', rt)

    # 数值范围[l..r]，加了一个数字jobi，生成新版本的可持久化线段树
    @staticmethod
    def insert(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_16 := Code07_Peaks1), (_java_key_17 := 'cntt'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3])
        Code07_Peaks1.ls[rt] = jcast('int', Code07_Peaks1.ls[i])
        Code07_Peaks1.rs[rt] = jcast('int', Code07_Peaks1.rs[i])
        Code07_Peaks1.numcnt[rt] = jcast('int', jcast('int', jadd(Code07_Peaks1.numcnt[i], 1)))
        if (l < r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                jset(Code07_Peaks1.ls, rt, Code07_Peaks1.insert(jobi, l, mid, Code07_Peaks1.ls[rt]))
            else:
                jset(Code07_Peaks1.rs, rt, Code07_Peaks1.insert(jobi, jcast('int', jadd(mid, 1)), r, Code07_Peaks1.rs[rt]))
        return jcast('int', rt)

    # 可持久化线段树，前版本pre，后版本post，两个版本做差，得到数值范围[l..r]的词频
    # 查询这个数值范围上，第jobk大的数字是什么
    @staticmethod
    def query(jobk, l, r, pre, post):
        jobk = jcast('int', jobk)
        l = jcast('int', l)
        r = jcast('int', r)
        pre = jcast('int', pre)
        post = jcast('int', post)
        if (l == r):
            return jcast('int', l)
        rsize = jcast('int', jcast('int', (Code07_Peaks1.numcnt[Code07_Peaks1.rs[post]] - Code07_Peaks1.numcnt[Code07_Peaks1.rs[pre]])))
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        if (rsize >= jobk):
            return jcast('int', Code07_Peaks1.query(jobk, jcast('int', jadd(mid, 1)), r, Code07_Peaks1.rs[pre], Code07_Peaks1.rs[post]))
        else:
            return jcast('int', Code07_Peaks1.query(jcast('int', (jobk - rsize)), l, mid, Code07_Peaks1.ls[pre], Code07_Peaks1.ls[post]))

    @staticmethod
    def kthMax(u, x, k):
        u = jcast('int', u)
        x = jcast('int', x)
        k = jcast('int', k)
        p = jcast('int', jcast('int', (Code07_Peaks1.MAXP - 1)))
        while (p >= 0):
            if ((Code07_Peaks1.stjump[u][p] > 0) and (Code07_Peaks1.nodeKey[Code07_Peaks1.stjump[u][p]] <= x)):
                u = jcast('int', Code07_Peaks1.stjump[u][p])
            p = jcast('int', (p - 1))
        if (Code07_Peaks1.leafsiz[u] < k):
            return jcast('int', 0)
        idx = jcast('int', Code07_Peaks1.query(k, 1, Code07_Peaks1.s, Code07_Peaks1.root[jcast('int', (Code07_Peaks1.leafDfnMin[u] - 1))], Code07_Peaks1.root[jcast('int', (jcast('int', jadd(Code07_Peaks1.leafDfnMin[u], Code07_Peaks1.leafsiz[u])) - 1))]))
        return jcast('int', Code07_Peaks1.sorted[idx])

    @staticmethod
    def main(args):
        io = Code07_Peaks1.FastIO(jget(System, 'in'), jget(System, 'out'), _java_ctor=0)
        Code07_Peaks1.n = jcast('int', jcall(io, 'nextInt'))
        Code07_Peaks1.m = jcast('int', jcall(io, 'nextInt'))
        Code07_Peaks1.q = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_Peaks1.n):
            jset(Code07_Peaks1.node, i, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_Peaks1.m):
            jset(Code07_Peaks1.edge[i], 0, jcall(io, 'nextInt'))
            jset(Code07_Peaks1.edge[i], 1, jcall(io, 'nextInt'))
            jset(Code07_Peaks1.edge[i], 2, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        Code07_Peaks1.prepare()
        Code07_Peaks1.kruskalRebuild()
        i = jcast('int', 1)
        while (i <= Code07_Peaks1.cntu):
            if (i == Code07_Peaks1.father[i]):
                Code07_Peaks1.dfs(i, 0)
            i = jcast('int', (i + 1))
        jset(Code07_Peaks1.root, 0, Code07_Peaks1.build(1, Code07_Peaks1.s))
        i = jcast('int', 1)
        while (i <= Code07_Peaks1.n):
            jset(Code07_Peaks1.root, i, Code07_Peaks1.insert(Code07_Peaks1.node[Code07_Peaks1.leafseg[i]], 1, Code07_Peaks1.s, Code07_Peaks1.root[jcast('int', (i - 1))]))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        x = 0
        k = 0
        lastAns = jcast('int', 0)
        while (i <= Code07_Peaks1.q):
            u = jcast('int', jcall(io, 'nextInt'))
            x = jcast('int', jcall(io, 'nextInt'))
            k = jcast('int', jcall(io, 'nextInt'))
            u = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', (u ^ lastAns)), Code07_Peaks1.n)), 1)))
            x = jcast('int', jcast('int', (x ^ lastAns)))
            k = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', (k ^ lastAns)), Code07_Peaks1.n)), 1)))
            lastAns = jcast('int', Code07_Peaks1.kthMax(u, x, k))
            if (lastAns == 0):
                jcall(io, 'writelnInt', jcast('int', (-1)))
            else:
                jcall(io, 'writelnInt', lastAns)
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
                except Exception as _java_exception_19:
                    if jinstanceof(_java_exception_19, 'IOException'):
                        e = _java_exception_19
                        raise jnew('RuntimeException', e)
                    else:
                        raise
                if (self.lenbuf == jcast('int', (-1))):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', jcast('int', (self.inbuf[((_java_obj_20 := self), (_java_key_21 := 'ptrbuf'), (_java_old_22 := jget(_java_obj_20, _java_key_21)), jset(_java_obj_20, _java_key_21, jcast('int', (_java_old_22 + (1)))), _java_old_22)[4]] & 255)))

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
            except Exception as _java_exception_23:
                if jinstanceof(_java_exception_23, 'IOException'):
                    e = _java_exception_23
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
            raise TypeError("No matching overload for Code07_Peaks1.FastIO.FastIO")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_Peaks1.MAXN = jcast('int', 100001)
Code07_Peaks1.MAXK = jcast('int', 200001)
Code07_Peaks1.MAXM = jcast('int', 500001)
Code07_Peaks1.MAXT = jcast('int', jcast('int', (Code07_Peaks1.MAXN * 40)))
Code07_Peaks1.MAXP = jcast('int', 20)
Code07_Peaks1.n = jcast('int', 0)
Code07_Peaks1.m = jcast('int', 0)
Code07_Peaks1.q = jcast('int', 0)
Code07_Peaks1.s = jcast('int', 0)
Code07_Peaks1.node = jarray('int', [Code07_Peaks1.MAXN])
Code07_Peaks1.sorted = jarray('int', [Code07_Peaks1.MAXN])
Code07_Peaks1.edge = jarray('int', [Code07_Peaks1.MAXM, 3])
Code07_Peaks1.father = jarray('int', [Code07_Peaks1.MAXK])
Code07_Peaks1.head = jarray('int', [Code07_Peaks1.MAXK])
Code07_Peaks1.next = jarray('int', [Code07_Peaks1.MAXK])
Code07_Peaks1.to = jarray('int', [Code07_Peaks1.MAXK])
Code07_Peaks1.cntg = jcast('int', 0)
Code07_Peaks1.nodeKey = jarray('int', [Code07_Peaks1.MAXK])
Code07_Peaks1.cntu = jcast('int', 0)
Code07_Peaks1.stjump = jarray('int', [Code07_Peaks1.MAXK, Code07_Peaks1.MAXP])
Code07_Peaks1.leafsiz = jarray('int', [Code07_Peaks1.MAXK])
Code07_Peaks1.leafDfnMin = jarray('int', [Code07_Peaks1.MAXK])
Code07_Peaks1.leafseg = jarray('int', [Code07_Peaks1.MAXK])
Code07_Peaks1.cntd = jcast('int', 0)
Code07_Peaks1.root = jarray('int', [Code07_Peaks1.MAXN])
Code07_Peaks1.ls = jarray('int', [Code07_Peaks1.MAXT])
Code07_Peaks1.rs = jarray('int', [Code07_Peaks1.MAXT])
Code07_Peaks1.numcnt = jarray('int', [Code07_Peaks1.MAXT])
Code07_Peaks1.cntt = jcast('int', 0)

if __name__ == '__main__':
    Code07_Peaks1.main([])
