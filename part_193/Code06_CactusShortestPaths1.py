# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 仙人掌最短路，Python版
# 给定n个点、m条边的仙人掌图，每条边有边权，没有自环，没有重边
# 一共q条查询，每条查询格式为 x y，查询点x和点y之间的最短路距离
# 1 <= n、q <= 10^4
# 1 <= m <= 2 * 10^4
# 1 <= 边权 <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P5236
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_CactusShortestPaths1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'q': 'q', 'cntn': 'cntn', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'weight1': 'weight1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'weight2': 'weight2', 'cnt2': 'cnt2', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'stasiz': 'stasiz', 'fromWeight': 'fromWeight', 'cycleLen': 'cycleLen', 'cycleSum': 'cycleSum', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'len': 'len', 'son': 'son', 'top': 'top'}
    MAXN = 0
    n = 0
    m = 0
    q = 0
    cntn = 0
    # 原图
    head1 = None
    next1 = None
    to1 = None
    weight1 = None
    cnt1 = 0
    # 圆方树，单向边
    head2 = None
    next2 = None
    to2 = None
    weight2 = None
    cnt2 = 0
    # tarjan算法求圆方树
    dfn = None
    low = None
    cntd = 0
    sta = None
    stasiz = 0
    # 环的信息
    fromWeight = None
    cycleLen = None
    cycleSum = None
    # 树链剖分
    # len[u] : 圆方树上从头节点到u的长度
    fa = None
    dep = None
    siz = None
    len = None
    son = None
    top = None
    @staticmethod
    def addEdge1(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code06_CactusShortestPaths1.next1, ((_java_obj_1 := Code06_CactusShortestPaths1), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_CactusShortestPaths1.head1[u])
        Code06_CactusShortestPaths1.to1[Code06_CactusShortestPaths1.cnt1] = jcast('int', v)
        Code06_CactusShortestPaths1.weight1[Code06_CactusShortestPaths1.cnt1] = jcast('int', w)
        Code06_CactusShortestPaths1.head1[u] = jcast('int', Code06_CactusShortestPaths1.cnt1)

    @staticmethod
    def addEdge2(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code06_CactusShortestPaths1.next2, ((_java_obj_4 := Code06_CactusShortestPaths1), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code06_CactusShortestPaths1.head2[u])
        Code06_CactusShortestPaths1.to2[Code06_CactusShortestPaths1.cnt2] = jcast('int', v)
        Code06_CactusShortestPaths1.weight2[Code06_CactusShortestPaths1.cnt2] = jcast('int', w)
        Code06_CactusShortestPaths1.head2[u] = jcast('int', Code06_CactusShortestPaths1.cnt2)

    @staticmethod
    def cycleLink(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code06_CactusShortestPaths1.cntn = jcast('int', (Code06_CactusShortestPaths1.cntn + 1))
        Code06_CactusShortestPaths1.cycleSum[Code06_CactusShortestPaths1.cntn] = jcast('int', Code06_CactusShortestPaths1.fromWeight[u])
        Code06_CactusShortestPaths1.addEdge2(u, Code06_CactusShortestPaths1.cntn, 0)
        tmp = jcast('int', Code06_CactusShortestPaths1.stasiz)
        pop = 0
        while True:
            pop = jcast('int', Code06_CactusShortestPaths1.sta[((_java_old_7 := tmp), (tmp := jcast('int', (tmp + (-1)))), _java_old_7)[2]])
            Code06_CactusShortestPaths1.cycleLen[pop] = jcast('int', Code06_CactusShortestPaths1.cycleSum[Code06_CactusShortestPaths1.cntn])
            Code06_CactusShortestPaths1.cycleSum[Code06_CactusShortestPaths1.cntn] = jcast('int', jcast('int', jadd(Code06_CactusShortestPaths1.cycleSum[Code06_CactusShortestPaths1.cntn], Code06_CactusShortestPaths1.fromWeight[pop])))
            if not ((pop != v)):
                break
        while True:
            pop = jcast('int', Code06_CactusShortestPaths1.sta[((_java_obj_8 := Code06_CactusShortestPaths1), (_java_key_9 := 'stasiz'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (-1)))), _java_old_10)[4]])
            Code06_CactusShortestPaths1.addEdge2(Code06_CactusShortestPaths1.cntn, pop, jstatic('Math', 'min', Code06_CactusShortestPaths1.cycleLen[pop], jcast('int', (Code06_CactusShortestPaths1.cycleSum[Code06_CactusShortestPaths1.cntn] - Code06_CactusShortestPaths1.cycleLen[pop]))))
            if not ((pop != v)):
                break

    @staticmethod
    def tarjan(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code06_CactusShortestPaths1.dfn, u, jset(Code06_CactusShortestPaths1.low, u, ((_java_obj_11 := Code06_CactusShortestPaths1), (_java_key_12 := 'cntd'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))))[3]))
        jset(Code06_CactusShortestPaths1.sta, ((_java_obj_14 := Code06_CactusShortestPaths1), (_java_key_15 := 'stasiz'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))))[3], u)
        e = jcast('int', Code06_CactusShortestPaths1.head1[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code06_CactusShortestPaths1.to1[e])
                w = jcast('int', Code06_CactusShortestPaths1.weight1[e])
                if (Code06_CactusShortestPaths1.dfn[v] == 0):
                    Code06_CactusShortestPaths1.tarjan(v, e)
                    Code06_CactusShortestPaths1.fromWeight[v] = jcast('int', w)
                    if (Code06_CactusShortestPaths1.low[v] < Code06_CactusShortestPaths1.dfn[u]):
                        jset(Code06_CactusShortestPaths1.low, u, jstatic('Math', 'min', Code06_CactusShortestPaths1.low[u], Code06_CactusShortestPaths1.low[v]))
                    else:
                        if (Code06_CactusShortestPaths1.low[v] > Code06_CactusShortestPaths1.dfn[u]):
                            Code06_CactusShortestPaths1.stasiz = jcast('int', (Code06_CactusShortestPaths1.stasiz - 1))
                            Code06_CactusShortestPaths1.addEdge2(u, v, w)
                        else:
                            Code06_CactusShortestPaths1.cycleLink(u, v)
                else:
                    if (Code06_CactusShortestPaths1.dfn[v] < Code06_CactusShortestPaths1.dfn[u]):
                        Code06_CactusShortestPaths1.fromWeight[v] = jcast('int', w)
                        jset(Code06_CactusShortestPaths1.low, u, jstatic('Math', 'min', Code06_CactusShortestPaths1.low[u], Code06_CactusShortestPaths1.dfn[v]))
            except JContinue as _java_control_17:
                if _java_control_17.label not in (None,):
                    raise
            except JBreak as _java_control_17:
                if _java_control_17.label not in (None,):
                    raise
                break
            e = jcast('int', Code06_CactusShortestPaths1.next1[e])

    @staticmethod
    def dfs1(u, f, l):
        u = jcast('int', u)
        f = jcast('int', f)
        l = jcast('int', l)
        Code06_CactusShortestPaths1.fa[u] = jcast('int', f)
        Code06_CactusShortestPaths1.dep[u] = jcast('int', jcast('int', jadd(Code06_CactusShortestPaths1.dep[f], 1)))
        Code06_CactusShortestPaths1.siz[u] = jcast('int', 1)
        Code06_CactusShortestPaths1.len[u] = jcast('int', l)
        e = jcast('int', Code06_CactusShortestPaths1.head2[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code06_CactusShortestPaths1.to2[e])
            # 因为是单向边，所以不用判断 v != f，但这里保留模版写法
            if (v != f):
                Code06_CactusShortestPaths1.dfs1(v, u, jcast('int', jadd(Code06_CactusShortestPaths1.len[u], Code06_CactusShortestPaths1.weight2[e])))
                Code06_CactusShortestPaths1.siz[u] = jcast('int', jcast('int', jadd(Code06_CactusShortestPaths1.siz[u], Code06_CactusShortestPaths1.siz[v])))
                if ((Code06_CactusShortestPaths1.son[u] == 0) or (Code06_CactusShortestPaths1.siz[Code06_CactusShortestPaths1.son[u]] < Code06_CactusShortestPaths1.siz[v])):
                    Code06_CactusShortestPaths1.son[u] = jcast('int', v)
            e = jcast('int', Code06_CactusShortestPaths1.next2[e])

    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code06_CactusShortestPaths1.top[u] = jcast('int', t)
        if (Code06_CactusShortestPaths1.son[u] != 0):
            Code06_CactusShortestPaths1.dfs2(Code06_CactusShortestPaths1.son[u], t)
        e = jcast('int', Code06_CactusShortestPaths1.head2[u])
        while (e > 0):
            v = jcast('int', Code06_CactusShortestPaths1.to2[e])
            # 因为是单向边，所以不用判断 v != fa[u]，但这里保留模版写法
            if ((v != Code06_CactusShortestPaths1.fa[u]) and (v != Code06_CactusShortestPaths1.son[u])):
                Code06_CactusShortestPaths1.dfs2(v, v)
            e = jcast('int', Code06_CactusShortestPaths1.next2[e])

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        while (Code06_CactusShortestPaths1.top[a] != Code06_CactusShortestPaths1.top[b]):
            if (Code06_CactusShortestPaths1.dep[Code06_CactusShortestPaths1.top[a]] <= Code06_CactusShortestPaths1.dep[Code06_CactusShortestPaths1.top[b]]):
                b = jcast('int', Code06_CactusShortestPaths1.fa[Code06_CactusShortestPaths1.top[b]])
            else:
                a = jcast('int', Code06_CactusShortestPaths1.fa[Code06_CactusShortestPaths1.top[a]])
        return jcast('int', (a if (Code06_CactusShortestPaths1.dep[a] <= Code06_CactusShortestPaths1.dep[b]) else b))

    @staticmethod
    def find(x, square):
        x = jcast('int', x)
        square = jcast('int', square)
        pre = jcast('int', 0)
        while (Code06_CactusShortestPaths1.top[x] != Code06_CactusShortestPaths1.top[square]):
            pre = jcast('int', Code06_CactusShortestPaths1.top[x])
            x = jcast('int', Code06_CactusShortestPaths1.fa[pre])
        return jcast('int', (pre if (x == square) else Code06_CactusShortestPaths1.son[square]))

    @staticmethod
    def query(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        ans = jcast('int', 0)
        xylca = jcast('int', Code06_CactusShortestPaths1.lca(x, y))
        if (xylca <= Code06_CactusShortestPaths1.n):
            ans = jcast('int', jcast('int', (jcast('int', jadd(Code06_CactusShortestPaths1.len[x], Code06_CactusShortestPaths1.len[y])) - jcast('int', (Code06_CactusShortestPaths1.len[xylca] << (1 & 31))))))
        else:
            fx = jcast('int', Code06_CactusShortestPaths1.find(x, xylca))
            fy = jcast('int', Code06_CactusShortestPaths1.find(y, xylca))
            ans = jcast('int', jcast('int', (jcast('int', (jcast('int', jadd(Code06_CactusShortestPaths1.len[x], Code06_CactusShortestPaths1.len[y])) - Code06_CactusShortestPaths1.len[fx])) - Code06_CactusShortestPaths1.len[fy])))
            small = jcast('int', jstatic('Math', 'min', Code06_CactusShortestPaths1.cycleLen[fx], Code06_CactusShortestPaths1.cycleLen[fy]))
            big = jcast('int', jstatic('Math', 'max', Code06_CactusShortestPaths1.cycleLen[fx], Code06_CactusShortestPaths1.cycleLen[fy]))
            ans = jcast('int', jcast('int', jadd(ans, jstatic('Math', 'min', jcast('int', (big - small)), jcast('int', (Code06_CactusShortestPaths1.cycleSum[xylca] - jcast('int', (big - small))))))))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code06_CactusShortestPaths1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_CactusShortestPaths1.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_CactusShortestPaths1.m = jcast('int', jcall(in_, 'nextInt'))
        Code06_CactusShortestPaths1.q = jcast('int', jcall(in_, 'nextInt'))
        Code06_CactusShortestPaths1.cntn = jcast('int', Code06_CactusShortestPaths1.n)
        Code06_CactusShortestPaths1.cnt1 = jcast('int', 1)
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i <= Code06_CactusShortestPaths1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code06_CactusShortestPaths1.addEdge1(u, v, w)
            Code06_CactusShortestPaths1.addEdge1(v, u, w)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_CactusShortestPaths1.n):
            if (Code06_CactusShortestPaths1.dfn[i] == 0):
                Code06_CactusShortestPaths1.tarjan(i, 0)
            i = jcast('int', (i + 1))
        Code06_CactusShortestPaths1.dfs1(1, 0, 0)
        Code06_CactusShortestPaths1.dfs2(1, 1)
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= Code06_CactusShortestPaths1.q):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            jcall(out, 'println', Code06_CactusShortestPaths1.query(x, y))
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
            return jcast('int', self.buffer[((_java_obj_18 := self), (_java_key_19 := 'ptr'), (_java_old_20 := jget(_java_obj_18, _java_key_19)), jset(_java_obj_18, _java_key_19, jcast('int', (_java_old_20 + (1)))), _java_old_20)[4]])

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
            raise TypeError("No matching overload for Code06_CactusShortestPaths1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_CactusShortestPaths1.MAXN = jcast('int', 50001)
Code06_CactusShortestPaths1.n = jcast('int', 0)
Code06_CactusShortestPaths1.m = jcast('int', 0)
Code06_CactusShortestPaths1.q = jcast('int', 0)
Code06_CactusShortestPaths1.cntn = jcast('int', 0)
Code06_CactusShortestPaths1.head1 = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.next1 = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.to1 = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.weight1 = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.cnt1 = jcast('int', 0)
Code06_CactusShortestPaths1.head2 = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.next2 = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.to2 = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.weight2 = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.cnt2 = jcast('int', 0)
Code06_CactusShortestPaths1.dfn = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.low = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.cntd = jcast('int', 0)
Code06_CactusShortestPaths1.sta = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.stasiz = jcast('int', 0)
Code06_CactusShortestPaths1.fromWeight = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.cycleLen = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.cycleSum = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.fa = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.dep = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.siz = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.len = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.son = jarray('int', [Code06_CactusShortestPaths1.MAXN])
Code06_CactusShortestPaths1.top = jarray('int', [Code06_CactusShortestPaths1.MAXN])

if __name__ == '__main__':
    Code06_CactusShortestPaths1.main([])
