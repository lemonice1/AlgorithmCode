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

# 战略游戏，Python版
# 给定一张无向图，一共n个点、m条边，所有点保证连通，图中可能有重边
# 一共有q条查询，每条查询格式 s K1 K2 .. Ks，含义如下
# 当前查询涉及s个点，给出s个点的编号，你只能删掉一个另外的点
# 删除该点后，只要这s个点中存在任意两点不连通，就算成功
# 对每条查询，打印你能选择的点的个数
# 2 <= n <= 10^5    1 <= m <= 2 * 10^5    1 <= q <= 10^5
# 所有查询中s的总和 <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4606
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code09_StrategyGame1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 't': 't', 'n': 'n', 'm': 'm', 'q': 'q', 's': 's', 'cntn': 'cntn', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'cnt2': 'cnt2', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'dist': 'dist', 'dep': 'dep', 'stjump': 'stjump', 'nid': 'nid', 'cnti': 'cnti', 'arr': 'arr', 'stack': 'stack', 'u': 'u', 'status': 'status', 'fa': 'fa', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    MAXP = 0
    t = 0
    n = 0
    m = 0
    q = 0
    s = 0
    cntn = 0
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
    # nid是圆方树的点获得的dfn序号
    # cnti是圆方树的dfn序号计数
    dist = None
    dep = None
    stjump = None
    nid = None
    cnti = 0
    arr = None
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stack = None
    u = 0
    status = 0
    fa = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, status, fa, e):
        u = jcast('int', u)
        status = jcast('int', status)
        fa = jcast('int', fa)
        e = jcast('int', e)
        jset(Code09_StrategyGame1.stack[Code09_StrategyGame1.stacksize], 0, u)
        jset(Code09_StrategyGame1.stack[Code09_StrategyGame1.stacksize], 1, status)
        jset(Code09_StrategyGame1.stack[Code09_StrategyGame1.stacksize], 2, fa)
        jset(Code09_StrategyGame1.stack[Code09_StrategyGame1.stacksize], 3, e)
        Code09_StrategyGame1.stacksize = jcast('int', (Code09_StrategyGame1.stacksize + 1))

    @staticmethod
    def pop():
        Code09_StrategyGame1.stacksize = jcast('int', (Code09_StrategyGame1.stacksize - 1))
        Code09_StrategyGame1.u = jcast('int', Code09_StrategyGame1.stack[Code09_StrategyGame1.stacksize][0])
        Code09_StrategyGame1.status = jcast('int', Code09_StrategyGame1.stack[Code09_StrategyGame1.stacksize][1])
        Code09_StrategyGame1.fa = jcast('int', Code09_StrategyGame1.stack[Code09_StrategyGame1.stacksize][2])
        Code09_StrategyGame1.e = jcast('int', Code09_StrategyGame1.stack[Code09_StrategyGame1.stacksize][3])

    @staticmethod
    def addEdge1(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code09_StrategyGame1.next1, ((_java_obj_1 := Code09_StrategyGame1), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code09_StrategyGame1.head1[u])
        Code09_StrategyGame1.to1[Code09_StrategyGame1.cnt1] = jcast('int', v)
        Code09_StrategyGame1.head1[u] = jcast('int', Code09_StrategyGame1.cnt1)

    @staticmethod
    def addEdge2(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code09_StrategyGame1.next2, ((_java_obj_4 := Code09_StrategyGame1), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code09_StrategyGame1.head2[u])
        Code09_StrategyGame1.to2[Code09_StrategyGame1.cnt2] = jcast('int', v)
        Code09_StrategyGame1.head2[u] = jcast('int', Code09_StrategyGame1.cnt2)

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code09_StrategyGame1.dfn, u, jset(Code09_StrategyGame1.low, u, ((_java_obj_7 := Code09_StrategyGame1), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
        jset(Code09_StrategyGame1.sta, ((_java_obj_10 := Code09_StrategyGame1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
        e = jcast('int', Code09_StrategyGame1.head1[u])
        while (e > 0):
            v = jcast('int', Code09_StrategyGame1.to1[e])
            if (Code09_StrategyGame1.dfn[v] == 0):
                Code09_StrategyGame1.tarjan1(v)
                jset(Code09_StrategyGame1.low, u, jstatic('Math', 'min', Code09_StrategyGame1.low[u], Code09_StrategyGame1.low[v]))
                if (Code09_StrategyGame1.low[v] >= Code09_StrategyGame1.dfn[u]):
                    Code09_StrategyGame1.cntn = jcast('int', (Code09_StrategyGame1.cntn + 1))
                    Code09_StrategyGame1.addEdge2(Code09_StrategyGame1.cntn, u)
                    Code09_StrategyGame1.addEdge2(u, Code09_StrategyGame1.cntn)
                    pop = 0
                    while True:
                        pop = jcast('int', Code09_StrategyGame1.sta[((_java_obj_13 := Code09_StrategyGame1), (_java_key_14 := 'top'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]])
                        Code09_StrategyGame1.addEdge2(Code09_StrategyGame1.cntn, pop)
                        Code09_StrategyGame1.addEdge2(pop, Code09_StrategyGame1.cntn)
                        if not ((pop != v)):
                            break
            else:
                jset(Code09_StrategyGame1.low, u, jstatic('Math', 'min', Code09_StrategyGame1.low[u], Code09_StrategyGame1.dfn[v]))
            e = jcast('int', Code09_StrategyGame1.next1[e])

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code09_StrategyGame1.stacksize = jcast('int', 0)
        Code09_StrategyGame1.push(node, jcast('int', (-1)), 0, jcast('int', (-1)))
        v = 0
        while (Code09_StrategyGame1.stacksize > 0):
            Code09_StrategyGame1.pop()
            if (Code09_StrategyGame1.status == jcast('int', (-1))):
                jset(Code09_StrategyGame1.dfn, Code09_StrategyGame1.u, jset(Code09_StrategyGame1.low, Code09_StrategyGame1.u, ((_java_obj_16 := Code09_StrategyGame1), (_java_key_17 := 'cntd'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3]))
                jset(Code09_StrategyGame1.sta, ((_java_obj_19 := Code09_StrategyGame1), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], Code09_StrategyGame1.u)
                Code09_StrategyGame1.e = jcast('int', Code09_StrategyGame1.head1[Code09_StrategyGame1.u])
            else:
                v = jcast('int', Code09_StrategyGame1.to1[Code09_StrategyGame1.e])
                if (Code09_StrategyGame1.status == 0):
                    jset(Code09_StrategyGame1.low, Code09_StrategyGame1.u, jstatic('Math', 'min', Code09_StrategyGame1.low[Code09_StrategyGame1.u], Code09_StrategyGame1.low[v]))
                    if (Code09_StrategyGame1.low[v] >= Code09_StrategyGame1.dfn[Code09_StrategyGame1.u]):
                        Code09_StrategyGame1.cntn = jcast('int', (Code09_StrategyGame1.cntn + 1))
                        Code09_StrategyGame1.addEdge2(Code09_StrategyGame1.cntn, Code09_StrategyGame1.u)
                        Code09_StrategyGame1.addEdge2(Code09_StrategyGame1.u, Code09_StrategyGame1.cntn)
                        pop = 0
                        while True:
                            pop = jcast('int', Code09_StrategyGame1.sta[((_java_obj_22 := Code09_StrategyGame1), (_java_key_23 := 'top'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (-1)))), _java_old_24)[4]])
                            Code09_StrategyGame1.addEdge2(Code09_StrategyGame1.cntn, pop)
                            Code09_StrategyGame1.addEdge2(pop, Code09_StrategyGame1.cntn)
                            if not ((pop != v)):
                                break
                else:
                    jset(Code09_StrategyGame1.low, Code09_StrategyGame1.u, jstatic('Math', 'min', Code09_StrategyGame1.low[Code09_StrategyGame1.u], Code09_StrategyGame1.dfn[v]))
                Code09_StrategyGame1.e = jcast('int', Code09_StrategyGame1.next1[Code09_StrategyGame1.e])
            if (Code09_StrategyGame1.e != 0):
                v = jcast('int', Code09_StrategyGame1.to1[Code09_StrategyGame1.e])
                if (Code09_StrategyGame1.dfn[v] == 0):
                    Code09_StrategyGame1.push(Code09_StrategyGame1.u, 0, 0, Code09_StrategyGame1.e)
                    Code09_StrategyGame1.push(v, jcast('int', (-1)), 0, jcast('int', (-1)))
                else:
                    Code09_StrategyGame1.push(Code09_StrategyGame1.u, 1, 0, Code09_StrategyGame1.e)

    # 递归版
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code09_StrategyGame1.nid, u, ((_java_obj_25 := Code09_StrategyGame1), (_java_key_26 := 'cnti'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3])
        Code09_StrategyGame1.dist[u] = jcast('int', jcast('int', jadd(Code09_StrategyGame1.dist[fa], (1 if (u <= Code09_StrategyGame1.n) else 0))))
        Code09_StrategyGame1.dep[u] = jcast('int', jcast('int', jadd(Code09_StrategyGame1.dep[fa], 1)))
        jset(Code09_StrategyGame1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code09_StrategyGame1.MAXP):
            jset(Code09_StrategyGame1.stjump[u], p, Code09_StrategyGame1.stjump[Code09_StrategyGame1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code09_StrategyGame1.head2[u])
        while (e > 0):
            v = jcast('int', Code09_StrategyGame1.to2[e])
            if (v != fa):
                Code09_StrategyGame1.dfs1(v, u)
            e = jcast('int', Code09_StrategyGame1.next2[e])

    # 迭代版
    @staticmethod
    def dfs2(cur, father):
        cur = jcast('int', cur)
        father = jcast('int', father)
        Code09_StrategyGame1.stacksize = jcast('int', 0)
        Code09_StrategyGame1.push(cur, 0, father, jcast('int', (-1)))
        while (Code09_StrategyGame1.stacksize > 0):
            Code09_StrategyGame1.pop()
            if (Code09_StrategyGame1.e == jcast('int', (-1))):
                jset(Code09_StrategyGame1.nid, Code09_StrategyGame1.u, ((_java_obj_28 := Code09_StrategyGame1), (_java_key_29 := 'cnti'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))))[3])
                Code09_StrategyGame1.dist[Code09_StrategyGame1.u] = jcast('int', jcast('int', jadd(Code09_StrategyGame1.dist[Code09_StrategyGame1.fa], (1 if (Code09_StrategyGame1.u <= Code09_StrategyGame1.n) else 0))))
                Code09_StrategyGame1.dep[Code09_StrategyGame1.u] = jcast('int', jcast('int', jadd(Code09_StrategyGame1.dep[Code09_StrategyGame1.fa], 1)))
                jset(Code09_StrategyGame1.stjump[Code09_StrategyGame1.u], 0, Code09_StrategyGame1.fa)
                p = jcast('int', 1)
                while (p < Code09_StrategyGame1.MAXP):
                    jset(Code09_StrategyGame1.stjump[Code09_StrategyGame1.u], p, Code09_StrategyGame1.stjump[Code09_StrategyGame1.stjump[Code09_StrategyGame1.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code09_StrategyGame1.e = jcast('int', Code09_StrategyGame1.head2[Code09_StrategyGame1.u])
            else:
                Code09_StrategyGame1.e = jcast('int', Code09_StrategyGame1.next2[Code09_StrategyGame1.e])
            if (Code09_StrategyGame1.e != 0):
                Code09_StrategyGame1.push(Code09_StrategyGame1.u, 0, Code09_StrategyGame1.fa, Code09_StrategyGame1.e)
                if (Code09_StrategyGame1.to2[Code09_StrategyGame1.e] != Code09_StrategyGame1.fa):
                    Code09_StrategyGame1.push(Code09_StrategyGame1.to2[Code09_StrategyGame1.e], 0, Code09_StrategyGame1.u, jcast('int', (-1)))

    @staticmethod
    def getLca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code09_StrategyGame1.dep[a] < Code09_StrategyGame1.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code09_StrategyGame1.MAXP - 1)))
        while (p >= 0):
            if (Code09_StrategyGame1.dep[Code09_StrategyGame1.stjump[a][p]] >= Code09_StrategyGame1.dep[b]):
                a = jcast('int', Code09_StrategyGame1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code09_StrategyGame1.MAXP - 1)))
        while (p >= 0):
            if (Code09_StrategyGame1.stjump[a][p] != Code09_StrategyGame1.stjump[b][p]):
                a = jcast('int', Code09_StrategyGame1.stjump[a][p])
                b = jcast('int', Code09_StrategyGame1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code09_StrategyGame1.stjump[a][0])

    @staticmethod
    def getDist(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('int', jcast('int', (jcast('int', jadd(Code09_StrategyGame1.dist[x], Code09_StrategyGame1.dist[y])) - jcast('int', (2 * Code09_StrategyGame1.dist[Code09_StrategyGame1.getLca(x, y)])))))

    @staticmethod
    def sort(nums, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', nums[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        while (i <= j):
            while (Code09_StrategyGame1.nid[nums[i]] < Code09_StrategyGame1.nid[pivot]):
                i = jcast('int', (i + 1))
            while (Code09_StrategyGame1.nid[nums[j]] > Code09_StrategyGame1.nid[pivot]):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', nums[i])
                nums[i] = jcast('int', nums[j])
                nums[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code09_StrategyGame1.sort(nums, l, j)
        Code09_StrategyGame1.sort(nums, i, r)

    @staticmethod
    def compute():
        Code09_StrategyGame1.sort(Code09_StrategyGame1.arr, 1, Code09_StrategyGame1.s)
        sumDist = jcast('int', 0)
        i = jcast('int', 1)
        while (i < Code09_StrategyGame1.s):
            sumDist = jcast('int', jcast('int', jadd(sumDist, Code09_StrategyGame1.getDist(Code09_StrategyGame1.arr[i], Code09_StrategyGame1.arr[jcast('int', jadd(i, 1))]))))
            i = jcast('int', (i + 1))
        sumDist = jcast('int', jcast('int', jadd(sumDist, Code09_StrategyGame1.getDist(Code09_StrategyGame1.arr[1], Code09_StrategyGame1.arr[Code09_StrategyGame1.s]))))
        extra = jcast('int', (1 if (Code09_StrategyGame1.getLca(Code09_StrategyGame1.arr[1], Code09_StrategyGame1.arr[Code09_StrategyGame1.s]) <= Code09_StrategyGame1.n) else 0))
        return jcast('int', jcast('int', (jcast('int', jadd(jcast('int', jdiv(sumDist, 2)), extra)) - Code09_StrategyGame1.s)))

    @staticmethod
    def prepare():
        Code09_StrategyGame1.cnt1 = jcast('int', jset(Code09_StrategyGame1, 'cnt2', jset(Code09_StrategyGame1, 'cntd', jset(Code09_StrategyGame1, 'top', jset(Code09_StrategyGame1, 'cnti', 0)))))
        i = jcast('int', 1)
        while (i <= Code09_StrategyGame1.n):
            jset(Code09_StrategyGame1.head1, i, jset(Code09_StrategyGame1.head2, i, jset(Code09_StrategyGame1.dfn, i, 0)))
            Code09_StrategyGame1.head2[jcast('int', jadd(i, Code09_StrategyGame1.n))] = jcast('int', 0)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code09_StrategyGame1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code09_StrategyGame1.t = jcast('int', jcall(in_, 'nextInt'))
        c = jcast('int', 1)
        while (c <= Code09_StrategyGame1.t):
            Code09_StrategyGame1.n = jcast('int', jcall(in_, 'nextInt'))
            Code09_StrategyGame1.m = jcast('int', jcall(in_, 'nextInt'))
            Code09_StrategyGame1.cntn = jcast('int', Code09_StrategyGame1.n)
            Code09_StrategyGame1.prepare()
            i = jcast('int', 1)
            u = 0
            v = 0
            while (i <= Code09_StrategyGame1.m):
                u = jcast('int', jcall(in_, 'nextInt'))
                v = jcast('int', jcall(in_, 'nextInt'))
                Code09_StrategyGame1.addEdge1(u, v)
                Code09_StrategyGame1.addEdge1(v, u)
                i = jcast('int', (i + 1))
            # tarjan1(1);
            Code09_StrategyGame1.tarjan2(1)
            # dfs1(1, 0);
            Code09_StrategyGame1.dfs2(1, 0)
            Code09_StrategyGame1.q = jcast('int', jcall(in_, 'nextInt'))
            i = jcast('int', 1)
            while (i <= Code09_StrategyGame1.q):
                Code09_StrategyGame1.s = jcast('int', jcall(in_, 'nextInt'))
                j = jcast('int', 1)
                while (j <= Code09_StrategyGame1.s):
                    jset(Code09_StrategyGame1.arr, j, jcall(in_, 'nextInt'))
                    j = jcast('int', (j + 1))
                jcall(out, 'println', Code09_StrategyGame1.compute())
                i = jcast('int', (i + 1))
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
            return jcast('int', self.buffer[((_java_obj_31 := self), (_java_key_32 := 'ptr'), (_java_old_33 := jget(_java_obj_31, _java_key_32)), jset(_java_obj_31, _java_key_32, jcast('int', (_java_old_33 + (1)))), _java_old_33)[4]])

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
            raise TypeError("No matching overload for Code09_StrategyGame1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code09_StrategyGame1.MAXN = jcast('int', 100001)
Code09_StrategyGame1.MAXM = jcast('int', 200001)
Code09_StrategyGame1.MAXP = jcast('int', 20)
Code09_StrategyGame1.t = jcast('int', 0)
Code09_StrategyGame1.n = jcast('int', 0)
Code09_StrategyGame1.m = jcast('int', 0)
Code09_StrategyGame1.q = jcast('int', 0)
Code09_StrategyGame1.s = jcast('int', 0)
Code09_StrategyGame1.cntn = jcast('int', 0)
Code09_StrategyGame1.head1 = jarray('int', [Code09_StrategyGame1.MAXN])
Code09_StrategyGame1.next1 = jarray('int', [jcast('int', (Code09_StrategyGame1.MAXM << (1 & 31)))])
Code09_StrategyGame1.to1 = jarray('int', [jcast('int', (Code09_StrategyGame1.MAXM << (1 & 31)))])
Code09_StrategyGame1.cnt1 = jcast('int', 0)
Code09_StrategyGame1.head2 = jarray('int', [jcast('int', (Code09_StrategyGame1.MAXN << (1 & 31)))])
Code09_StrategyGame1.next2 = jarray('int', [jcast('int', (Code09_StrategyGame1.MAXM << (2 & 31)))])
Code09_StrategyGame1.to2 = jarray('int', [jcast('int', (Code09_StrategyGame1.MAXM << (2 & 31)))])
Code09_StrategyGame1.cnt2 = jcast('int', 0)
Code09_StrategyGame1.dfn = jarray('int', [Code09_StrategyGame1.MAXN])
Code09_StrategyGame1.low = jarray('int', [Code09_StrategyGame1.MAXN])
Code09_StrategyGame1.cntd = jcast('int', 0)
Code09_StrategyGame1.sta = jarray('int', [Code09_StrategyGame1.MAXN])
Code09_StrategyGame1.top = jcast('int', 0)
Code09_StrategyGame1.dist = jarray('int', [jcast('int', (Code09_StrategyGame1.MAXN << (1 & 31)))])
Code09_StrategyGame1.dep = jarray('int', [jcast('int', (Code09_StrategyGame1.MAXN << (1 & 31)))])
Code09_StrategyGame1.stjump = jarray('int', [jcast('int', (Code09_StrategyGame1.MAXN << (1 & 31))), Code09_StrategyGame1.MAXP])
Code09_StrategyGame1.nid = jarray('int', [jcast('int', (Code09_StrategyGame1.MAXN << (1 & 31)))])
Code09_StrategyGame1.cnti = jcast('int', 0)
Code09_StrategyGame1.arr = jarray('int', [Code09_StrategyGame1.MAXN])
Code09_StrategyGame1.stack = jarray('int', [jcast('int', (Code09_StrategyGame1.MAXN << (1 & 31))), 4])
Code09_StrategyGame1.u = jcast('int', 0)
Code09_StrategyGame1.status = jcast('int', 0)
Code09_StrategyGame1.fa = jcast('int', 0)
Code09_StrategyGame1.e = jcast('int', 0)
Code09_StrategyGame1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code09_StrategyGame1.main([])
