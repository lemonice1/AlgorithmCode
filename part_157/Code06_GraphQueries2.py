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

# 删边和查询，Python版
# 图里有n个点，m条无向边，初始时点权都不同，图里可能有若干个连通的部分
# 一共有q条操作，每条操作是如下两种类型中的一种
# 操作 1 x : 点x所在的连通区域中，假设点y拥有最大的点权
# 打印y的点权，然后把y的点权修改为0
# 操作 2 x : 删掉第x条边
# 1 <= n <= 2 * 10^5    1 <= m <= 3 * 10^5    1 <= q <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF1416D
# 测试链接 : https://codeforces.com/problemset/problem/1416/D
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_GraphQueries2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 'MAXM': 'MAXM', 'MAXQ': 'MAXQ', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'q': 'q', 'node': 'node', 'edge': 'edge', 'ques': 'ques', 'father': 'father', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'nodeKey': 'nodeKey', 'cntu': 'cntu', 'stjump': 'stjump', 'leafsiz': 'leafsiz', 'leafDfnMin': 'leafDfnMin', 'leafseg': 'leafseg', 'cntd': 'cntd', 'maxValueDfn': 'maxValueDfn'}
    MAXN = 0
    MAXK = 0
    MAXM = 0
    MAXQ = 0
    MAXP = 0
    n = 0
    m = 0
    q = 0
    # 节点值的数组，需要记录，线段树也要使用
    node = None
    # 所有边的数组，逆序处理删除操作，设置每条边的权值
    edge = None
    # 记录所有操作
    ques = None
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
    # 线段树的下标是dfn序号，维护范围内，拥有最大点权的dfn序号
    maxValueDfn = None
    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code06_GraphQueries2.q):
            if (Code06_GraphQueries2.ques[i][0] == 2):
                jset(Code06_GraphQueries2.edge[Code06_GraphQueries2.ques[i][1]], 2, jcast('int', (-1)))
            i = jcast('int', (i + 1))
        weight = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code06_GraphQueries2.m):
            if (Code06_GraphQueries2.edge[i][2] != jcast('int', (-1))):
                jset(Code06_GraphQueries2.edge[i], 2, (weight := jcast('int', (weight + (1)))))
            i = jcast('int', (i + 1))
        i = jcast('int', Code06_GraphQueries2.q)
        while (i >= 1):
            if (Code06_GraphQueries2.ques[i][0] == 2):
                jset(Code06_GraphQueries2.edge[Code06_GraphQueries2.ques[i][1]], 2, (weight := jcast('int', (weight + (1)))))
            i = jcast('int', (i - 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code06_GraphQueries2.father[i]):
            jset(Code06_GraphQueries2.father, i, Code06_GraphQueries2.find(Code06_GraphQueries2.father[i]))
        return jcast('int', Code06_GraphQueries2.father[i])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code06_GraphQueries2.next, ((_java_obj_1 := Code06_GraphQueries2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_GraphQueries2.head[u])
        Code06_GraphQueries2.to[Code06_GraphQueries2.cntg] = jcast('int', v)
        Code06_GraphQueries2.head[u] = jcast('int', Code06_GraphQueries2.cntg)

    @staticmethod
    def kruskalRebuild():
        i = jcast('int', 1)
        while (i <= Code06_GraphQueries2.n):
            Code06_GraphQueries2.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code06_GraphQueries2.edge, 1, jcast('int', jadd(Code06_GraphQueries2.m, 1)), (lambda a, b: (a[2] - b[2])))
        Code06_GraphQueries2.cntu = jcast('int', Code06_GraphQueries2.n)
        i = jcast('int', 1)
        fx = 0
        fy = 0
        while (i <= Code06_GraphQueries2.m):
            fx = jcast('int', Code06_GraphQueries2.find(Code06_GraphQueries2.edge[i][0]))
            fy = jcast('int', Code06_GraphQueries2.find(Code06_GraphQueries2.edge[i][1]))
            if (fx != fy):
                jset(Code06_GraphQueries2.father, fx, jset(Code06_GraphQueries2.father, fy, ((_java_obj_4 := Code06_GraphQueries2), (_java_key_5 := 'cntu'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
                Code06_GraphQueries2.father[Code06_GraphQueries2.cntu] = jcast('int', Code06_GraphQueries2.cntu)
                Code06_GraphQueries2.nodeKey[Code06_GraphQueries2.cntu] = jcast('int', Code06_GraphQueries2.edge[i][2])
                Code06_GraphQueries2.addEdge(Code06_GraphQueries2.cntu, fx)
                Code06_GraphQueries2.addEdge(Code06_GraphQueries2.cntu, fy)
            i = jcast('int', (i + 1))

    @staticmethod
    def dfs(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code06_GraphQueries2.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code06_GraphQueries2.MAXP):
            jset(Code06_GraphQueries2.stjump[u], p, Code06_GraphQueries2.stjump[Code06_GraphQueries2.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code06_GraphQueries2.head[u])
        while (e > 0):
            Code06_GraphQueries2.dfs(Code06_GraphQueries2.to[e], u)
            e = jcast('int', Code06_GraphQueries2.next[e])
        if (u <= Code06_GraphQueries2.n):
            Code06_GraphQueries2.leafsiz[u] = jcast('int', 1)
            jset(Code06_GraphQueries2.leafDfnMin, u, ((_java_obj_7 := Code06_GraphQueries2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
            Code06_GraphQueries2.leafseg[Code06_GraphQueries2.cntd] = jcast('int', u)
        else:
            Code06_GraphQueries2.leafsiz[u] = jcast('int', 0)
            Code06_GraphQueries2.leafDfnMin[u] = jcast('int', jcast('int', jadd(Code06_GraphQueries2.n, 1)))
        e = jcast('int', Code06_GraphQueries2.head[u])
        while (e > 0):
            Code06_GraphQueries2.leafsiz[u] = jcast('int', jcast('int', jadd(Code06_GraphQueries2.leafsiz[u], Code06_GraphQueries2.leafsiz[Code06_GraphQueries2.to[e]])))
            jset(Code06_GraphQueries2.leafDfnMin, u, jstatic('Math', 'min', Code06_GraphQueries2.leafDfnMin[u], Code06_GraphQueries2.leafDfnMin[Code06_GraphQueries2.to[e]]))
            e = jcast('int', Code06_GraphQueries2.next[e])

    @staticmethod
    def getAncestor(u, limit):
        u = jcast('int', u)
        limit = jcast('int', limit)
        p = jcast('int', jcast('int', (Code06_GraphQueries2.MAXP - 1)))
        while (p >= 0):
            if ((Code06_GraphQueries2.stjump[u][p] > 0) and (Code06_GraphQueries2.nodeKey[Code06_GraphQueries2.stjump[u][p]] <= limit)):
                u = jcast('int', Code06_GraphQueries2.stjump[u][p])
            p = jcast('int', (p - 1))
        return jcast('int', u)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        l = jcast('int', jcast('int', (i << (1 & 31))))
        r = jcast('int', jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        if (Code06_GraphQueries2.node[Code06_GraphQueries2.leafseg[Code06_GraphQueries2.maxValueDfn[l]]] > Code06_GraphQueries2.node[Code06_GraphQueries2.leafseg[Code06_GraphQueries2.maxValueDfn[r]]]):
            Code06_GraphQueries2.maxValueDfn[i] = jcast('int', Code06_GraphQueries2.maxValueDfn[l])
        else:
            Code06_GraphQueries2.maxValueDfn[i] = jcast('int', Code06_GraphQueries2.maxValueDfn[r])

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code06_GraphQueries2.maxValueDfn[i] = jcast('int', l)
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            Code06_GraphQueries2.build(l, mid, jcast('int', (i << (1 & 31))))
            Code06_GraphQueries2.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code06_GraphQueries2.up(i)

    # dfn序号为jobi，点权更新成jobv
    @staticmethod
    def update(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            jset(Code06_GraphQueries2.node, Code06_GraphQueries2.leafseg[jobi], jobv)
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                Code06_GraphQueries2.update(jobi, jobv, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code06_GraphQueries2.update(jobi, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code06_GraphQueries2.up(i)

    # dfn范围[jobl..jobr]，哪个节点拥有最大点权，返回该节点的dfn序号
    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code06_GraphQueries2.maxValueDfn[i])
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            ldfn = jcast('int', 0)
            rdfn = jcast('int', 0)
            if (jobl <= mid):
                ldfn = jcast('int', Code06_GraphQueries2.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))
            if (jobr > mid):
                rdfn = jcast('int', Code06_GraphQueries2.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))
            if (Code06_GraphQueries2.node[Code06_GraphQueries2.leafseg[ldfn]] > Code06_GraphQueries2.node[Code06_GraphQueries2.leafseg[rdfn]]):
                return jcast('int', ldfn)
            else:
                return jcast('int', rdfn)

    @staticmethod
    def queryAndUpdate(x, limit):
        x = jcast('int', x)
        limit = jcast('int', limit)
        anc = jcast('int', Code06_GraphQueries2.getAncestor(x, limit))
        dfn = jcast('int', Code06_GraphQueries2.query(Code06_GraphQueries2.leafDfnMin[anc], jcast('int', (jcast('int', jadd(Code06_GraphQueries2.leafDfnMin[anc], Code06_GraphQueries2.leafsiz[anc])) - 1)), 1, Code06_GraphQueries2.n, 1))
        ans = jcast('int', Code06_GraphQueries2.node[Code06_GraphQueries2.leafseg[dfn]])
        Code06_GraphQueries2.update(dfn, 0, 1, Code06_GraphQueries2.n, 1)
        return jcast('int', ans)

    @staticmethod
    def main(args):
        io = Code06_GraphQueries2.FastIO(jget(System, 'in'), jget(System, 'out'), _java_ctor=0)
        Code06_GraphQueries2.n = jcast('int', jcall(io, 'nextInt'))
        Code06_GraphQueries2.m = jcast('int', jcall(io, 'nextInt'))
        Code06_GraphQueries2.q = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_GraphQueries2.n):
            jset(Code06_GraphQueries2.node, i, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_GraphQueries2.m):
            jset(Code06_GraphQueries2.edge[i], 0, jcall(io, 'nextInt'))
            jset(Code06_GraphQueries2.edge[i], 1, jcall(io, 'nextInt'))
            jset(Code06_GraphQueries2.edge[i], 2, 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_GraphQueries2.q):
            jset(Code06_GraphQueries2.ques[i], 0, jcall(io, 'nextInt'))
            jset(Code06_GraphQueries2.ques[i], 1, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        Code06_GraphQueries2.prepare()
        Code06_GraphQueries2.kruskalRebuild()
        i = jcast('int', 1)
        while (i <= Code06_GraphQueries2.cntu):
            if (i == Code06_GraphQueries2.father[i]):
                Code06_GraphQueries2.dfs(i, 0)
            i = jcast('int', (i + 1))
        Code06_GraphQueries2.build(1, Code06_GraphQueries2.n, 1)
        limit = jcast('int', Code06_GraphQueries2.m)
        i = jcast('int', 1)
        while (i <= Code06_GraphQueries2.q):
            if (Code06_GraphQueries2.ques[i][0] == 1):
                jcall(io, 'writelnInt', Code06_GraphQueries2.queryAndUpdate(Code06_GraphQueries2.ques[i][1], limit))
            else:
                limit = jcast('int', (limit - 1))
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
            raise TypeError("No matching overload for Code06_GraphQueries2.FastIO.FastIO")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_GraphQueries2.MAXN = jcast('int', 200001)
Code06_GraphQueries2.MAXK = jcast('int', 400001)
Code06_GraphQueries2.MAXM = jcast('int', 300001)
Code06_GraphQueries2.MAXQ = jcast('int', 500001)
Code06_GraphQueries2.MAXP = jcast('int', 20)
Code06_GraphQueries2.n = jcast('int', 0)
Code06_GraphQueries2.m = jcast('int', 0)
Code06_GraphQueries2.q = jcast('int', 0)
Code06_GraphQueries2.node = jarray('int', [Code06_GraphQueries2.MAXN])
Code06_GraphQueries2.edge = jarray('int', [Code06_GraphQueries2.MAXM, 3])
Code06_GraphQueries2.ques = jarray('int', [Code06_GraphQueries2.MAXQ, 2])
Code06_GraphQueries2.father = jarray('int', [Code06_GraphQueries2.MAXK])
Code06_GraphQueries2.head = jarray('int', [Code06_GraphQueries2.MAXK])
Code06_GraphQueries2.next = jarray('int', [Code06_GraphQueries2.MAXK])
Code06_GraphQueries2.to = jarray('int', [Code06_GraphQueries2.MAXK])
Code06_GraphQueries2.cntg = jcast('int', 0)
Code06_GraphQueries2.nodeKey = jarray('int', [Code06_GraphQueries2.MAXK])
Code06_GraphQueries2.cntu = jcast('int', 0)
Code06_GraphQueries2.stjump = jarray('int', [Code06_GraphQueries2.MAXK, Code06_GraphQueries2.MAXP])
Code06_GraphQueries2.leafsiz = jarray('int', [Code06_GraphQueries2.MAXK])
Code06_GraphQueries2.leafDfnMin = jarray('int', [Code06_GraphQueries2.MAXK])
Code06_GraphQueries2.leafseg = jarray('int', [Code06_GraphQueries2.MAXK])
Code06_GraphQueries2.cntd = jcast('int', 0)
Code06_GraphQueries2.maxValueDfn = jarray('int', [jcast('int', (Code06_GraphQueries2.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code06_GraphQueries2.main([])
