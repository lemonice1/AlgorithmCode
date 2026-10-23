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

# 边的查询，Python版
# 给定一张无向图，一共n个点、m条边，所有点保证连通
# 一共q条查询，格式 x y，含义如下
# 所有从x到y的简单路径上出现的边中，统计有多少条边满足
# 如果移除该边，x和y仍然可以互相到达，打印这个数量
# 1 <= n、m、q <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF1763F
# 测试链接 : https://codeforces.com/problemset/problem/1763/F
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_EdgeQueries2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'q': 'q', 'cntn': 'cntn', 'a': 'a', 'b': 'b', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'cnt2': 'cnt2', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'dep': 'dep', 'stjump': 'stjump', 'edgeCnt': 'edgeCnt'}
    MAXN = 0
    MAXM = 0
    MAXP = 0
    n = 0
    m = 0
    q = 0
    cntn = 0
    a = None
    b = None
    head1 = None
    next1 = None
    to1 = None
    cnt1 = 0
    head2 = None
    next2 = None
    to2 = None
    cnt2 = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    dep = None
    stjump = None
    edgeCnt = None
    @staticmethod
    def addEdge1(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code06_EdgeQueries2.next1, ((_java_obj_1 := Code06_EdgeQueries2), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_EdgeQueries2.head1[u])
        Code06_EdgeQueries2.to1[Code06_EdgeQueries2.cnt1] = jcast('int', v)
        Code06_EdgeQueries2.head1[u] = jcast('int', Code06_EdgeQueries2.cnt1)

    @staticmethod
    def addEdge2(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code06_EdgeQueries2.next2, ((_java_obj_4 := Code06_EdgeQueries2), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code06_EdgeQueries2.head2[u])
        Code06_EdgeQueries2.to2[Code06_EdgeQueries2.cnt2] = jcast('int', v)
        Code06_EdgeQueries2.head2[u] = jcast('int', Code06_EdgeQueries2.cnt2)

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code06_EdgeQueries2.dfn, u, jset(Code06_EdgeQueries2.low, u, ((_java_obj_7 := Code06_EdgeQueries2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
        jset(Code06_EdgeQueries2.sta, ((_java_obj_10 := Code06_EdgeQueries2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
        e = jcast('int', Code06_EdgeQueries2.head1[u])
        while (e > 0):
            v = jcast('int', Code06_EdgeQueries2.to1[e])
            if (Code06_EdgeQueries2.dfn[v] == 0):
                Code06_EdgeQueries2.tarjan(v)
                jset(Code06_EdgeQueries2.low, u, jstatic('Math', 'min', Code06_EdgeQueries2.low[u], Code06_EdgeQueries2.low[v]))
                if (Code06_EdgeQueries2.low[v] >= Code06_EdgeQueries2.dfn[u]):
                    Code06_EdgeQueries2.cntn = jcast('int', (Code06_EdgeQueries2.cntn + 1))
                    Code06_EdgeQueries2.addEdge2(Code06_EdgeQueries2.cntn, u)
                    Code06_EdgeQueries2.addEdge2(u, Code06_EdgeQueries2.cntn)
                    pop = 0
                    while True:
                        pop = jcast('int', Code06_EdgeQueries2.sta[((_java_obj_13 := Code06_EdgeQueries2), (_java_key_14 := 'top'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]])
                        Code06_EdgeQueries2.addEdge2(Code06_EdgeQueries2.cntn, pop)
                        Code06_EdgeQueries2.addEdge2(pop, Code06_EdgeQueries2.cntn)
                        if not ((pop != v)):
                            break
            else:
                jset(Code06_EdgeQueries2.low, u, jstatic('Math', 'min', Code06_EdgeQueries2.low[u], Code06_EdgeQueries2.dfn[v]))
            e = jcast('int', Code06_EdgeQueries2.next1[e])

    @staticmethod
    def dfs(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code06_EdgeQueries2.dep[u] = jcast('int', jcast('int', jadd(Code06_EdgeQueries2.dep[fa], 1)))
        jset(Code06_EdgeQueries2.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code06_EdgeQueries2.MAXP):
            jset(Code06_EdgeQueries2.stjump[u], p, Code06_EdgeQueries2.stjump[Code06_EdgeQueries2.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code06_EdgeQueries2.head2[u])
        while (e > 0):
            v = jcast('int', Code06_EdgeQueries2.to2[e])
            if (v != fa):
                Code06_EdgeQueries2.dfs(v, u)
            e = jcast('int', Code06_EdgeQueries2.next2[e])

    @staticmethod
    def getLca(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        if (Code06_EdgeQueries2.dep[x] < Code06_EdgeQueries2.dep[y]):
            tmp = jcast('int', x)
            x = jcast('int', y)
            y = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code06_EdgeQueries2.MAXP - 1)))
        while (p >= 0):
            if (Code06_EdgeQueries2.dep[Code06_EdgeQueries2.stjump[x][p]] >= Code06_EdgeQueries2.dep[y]):
                x = jcast('int', Code06_EdgeQueries2.stjump[x][p])
            p = jcast('int', (p - 1))
        if (x == y):
            return jcast('int', x)
        p = jcast('int', jcast('int', (Code06_EdgeQueries2.MAXP - 1)))
        while (p >= 0):
            if (Code06_EdgeQueries2.stjump[x][p] != Code06_EdgeQueries2.stjump[y][p]):
                x = jcast('int', Code06_EdgeQueries2.stjump[x][p])
                y = jcast('int', Code06_EdgeQueries2.stjump[y][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code06_EdgeQueries2.stjump[x][0])

    @staticmethod
    def dfsCnt(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code06_EdgeQueries2.edgeCnt[u] = jcast('int', jcast('int', jadd(Code06_EdgeQueries2.edgeCnt[u], Code06_EdgeQueries2.edgeCnt[fa])))
        e = jcast('int', Code06_EdgeQueries2.head2[u])
        while (e > 0):
            v = jcast('int', Code06_EdgeQueries2.to2[e])
            if (v != fa):
                Code06_EdgeQueries2.dfsCnt(v, u)
            e = jcast('int', Code06_EdgeQueries2.next2[e])

    @staticmethod
    def buildEdgeCnt():
        i = jcast('int', 1)
        while (i <= Code06_EdgeQueries2.m):
            fa = jcast('int', Code06_EdgeQueries2.stjump[Code06_EdgeQueries2.a[i]][0])
            fb = jcast('int', Code06_EdgeQueries2.stjump[Code06_EdgeQueries2.b[i]][0])
            if ((fa == fb) or (Code06_EdgeQueries2.stjump[fa][0] == Code06_EdgeQueries2.b[i])):
                Code06_EdgeQueries2.edgeCnt[fa] = jcast('int', (Code06_EdgeQueries2.edgeCnt[fa] + 1))
            else:
                Code06_EdgeQueries2.edgeCnt[fb] = jcast('int', (Code06_EdgeQueries2.edgeCnt[fb] + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', jcast('int', jadd(Code06_EdgeQueries2.n, 1)))
        while (i <= Code06_EdgeQueries2.cntn):
            if (Code06_EdgeQueries2.edgeCnt[i] == 1):
                Code06_EdgeQueries2.edgeCnt[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        Code06_EdgeQueries2.dfsCnt(1, 0)

    @staticmethod
    def query(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        xylca = jcast('int', Code06_EdgeQueries2.getLca(x, y))
        lcafa = jcast('int', Code06_EdgeQueries2.stjump[xylca][0])
        return jcast('int', jcast('int', (jcast('int', (jcast('int', jadd(Code06_EdgeQueries2.edgeCnt[x], Code06_EdgeQueries2.edgeCnt[y])) - Code06_EdgeQueries2.edgeCnt[xylca])) - Code06_EdgeQueries2.edgeCnt[lcafa])))

    @staticmethod
    def main(args):
        in_ = Code06_EdgeQueries2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_EdgeQueries2.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_EdgeQueries2.m = jcast('int', jcall(in_, 'nextInt'))
        Code06_EdgeQueries2.cntn = jcast('int', Code06_EdgeQueries2.n)
        i = jcast('int', 1)
        while (i <= Code06_EdgeQueries2.m):
            jset(Code06_EdgeQueries2.a, i, jcall(in_, 'nextInt'))
            jset(Code06_EdgeQueries2.b, i, jcall(in_, 'nextInt'))
            Code06_EdgeQueries2.addEdge1(Code06_EdgeQueries2.a[i], Code06_EdgeQueries2.b[i])
            Code06_EdgeQueries2.addEdge1(Code06_EdgeQueries2.b[i], Code06_EdgeQueries2.a[i])
            i = jcast('int', (i + 1))
        Code06_EdgeQueries2.tarjan(1)
        Code06_EdgeQueries2.dfs(1, 0)
        Code06_EdgeQueries2.buildEdgeCnt()
        Code06_EdgeQueries2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= Code06_EdgeQueries2.q):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            jcall(out, 'println', Code06_EdgeQueries2.query(x, y))
            i = jcast('int', (i + 1))
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
            return jcast('int', self.buffer[((_java_obj_16 := self), (_java_key_17 := 'ptr'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))), _java_old_18)[4]])

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
            raise TypeError("No matching overload for Code06_EdgeQueries2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_EdgeQueries2.MAXN = jcast('int', 200001)
Code06_EdgeQueries2.MAXM = jcast('int', 200001)
Code06_EdgeQueries2.MAXP = jcast('int', 20)
Code06_EdgeQueries2.n = jcast('int', 0)
Code06_EdgeQueries2.m = jcast('int', 0)
Code06_EdgeQueries2.q = jcast('int', 0)
Code06_EdgeQueries2.cntn = jcast('int', 0)
Code06_EdgeQueries2.a = jarray('int', [Code06_EdgeQueries2.MAXM])
Code06_EdgeQueries2.b = jarray('int', [Code06_EdgeQueries2.MAXM])
Code06_EdgeQueries2.head1 = jarray('int', [Code06_EdgeQueries2.MAXN])
Code06_EdgeQueries2.next1 = jarray('int', [jcast('int', (Code06_EdgeQueries2.MAXM << (1 & 31)))])
Code06_EdgeQueries2.to1 = jarray('int', [jcast('int', (Code06_EdgeQueries2.MAXM << (1 & 31)))])
Code06_EdgeQueries2.cnt1 = jcast('int', 0)
Code06_EdgeQueries2.head2 = jarray('int', [jcast('int', (Code06_EdgeQueries2.MAXN << (1 & 31)))])
Code06_EdgeQueries2.next2 = jarray('int', [jcast('int', (Code06_EdgeQueries2.MAXM << (2 & 31)))])
Code06_EdgeQueries2.to2 = jarray('int', [jcast('int', (Code06_EdgeQueries2.MAXM << (2 & 31)))])
Code06_EdgeQueries2.cnt2 = jcast('int', 0)
Code06_EdgeQueries2.dfn = jarray('int', [Code06_EdgeQueries2.MAXN])
Code06_EdgeQueries2.low = jarray('int', [Code06_EdgeQueries2.MAXN])
Code06_EdgeQueries2.cntd = jcast('int', 0)
Code06_EdgeQueries2.sta = jarray('int', [Code06_EdgeQueries2.MAXN])
Code06_EdgeQueries2.top = jcast('int', 0)
Code06_EdgeQueries2.dep = jarray('int', [jcast('int', (Code06_EdgeQueries2.MAXN << (1 & 31)))])
Code06_EdgeQueries2.stjump = jarray('int', [jcast('int', (Code06_EdgeQueries2.MAXN << (1 & 31))), Code06_EdgeQueries2.MAXP])
Code06_EdgeQueries2.edgeCnt = jarray('int', [jcast('int', (Code06_EdgeQueries2.MAXN << (1 & 31)))])

if __name__ == '__main__':
    Code06_EdgeQueries2.main([])
