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

# 警察，Python版
# 给定一张无向图，一共n个点、m条边，所有点保证连通并且无重边
# 一共q条查询，每条查询是如下两种类型中的一种
# 查询 1 a b c d : 已知c和d之间有边，如果删去这条边，打印a和b是否连通
# 查询 2 a b c   : 如果删除点c，打印a和b是否连通
# 1 <= n <= 10^5
# 1 <= m <= 5 * 10^5
# 1 <= q <= 3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4334
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
# 对应实现可参考 Code07_Policija2.py
# 两个版本保留相同的算法逻辑
class Code07_Policija1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'q': 'q', 'cntn': 'cntn', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'cnt2': 'cnt2', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'cnts': 'cnts', 'cutMap': 'cutMap', 'fa': 'fa', 'dep': 'dep', 'siz': 'siz', 'son': 'son', 'top': 'top'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    q = 0
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
    cnts = 0
    cutMap = None
    fa = None
    dep = None
    siz = None
    son = None
    top = None
    @staticmethod
    def addEdge1(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_Policija1.next1, ((_java_obj_1 := Code07_Policija1), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_Policija1.head1[u])
        Code07_Policija1.to1[Code07_Policija1.cnt1] = jcast('int', v)
        Code07_Policija1.head1[u] = jcast('int', Code07_Policija1.cnt1)

    @staticmethod
    def addEdge2(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_Policija1.next2, ((_java_obj_4 := Code07_Policija1), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code07_Policija1.head2[u])
        Code07_Policija1.to2[Code07_Policija1.cnt2] = jcast('int', v)
        Code07_Policija1.head2[u] = jcast('int', Code07_Policija1.cnt2)

    @staticmethod
    def addCut(x, y, cut):
        x = jcast('int', x)
        y = jcast('int', y)
        cut = jcast('int', cut)
        a = jcast('int', jstatic('Math', 'min', x, y))
        b = jcast('int', jstatic('Math', 'max', x, y))
        jcall(Code07_Policija1.cutMap, 'put', jcast('long', (jcast('long', (jcast('long', a) << (32 & 63))) | b)), cut)

    @staticmethod
    def getCut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        a = jcast('int', jstatic('Math', 'min', x, y))
        b = jcast('int', jstatic('Math', 'max', x, y))
        ans = jcall(Code07_Policija1.cutMap, 'get', jcast('long', (jcast('long', (jcast('long', a) << (32 & 63))) | b)))
        return jcast('int', (0 if (ans == None) else ans))

    @staticmethod
    def tarjan(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code07_Policija1.dfn, u, jset(Code07_Policija1.low, u, ((_java_obj_7 := Code07_Policija1), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
        jset(Code07_Policija1.sta, ((_java_obj_10 := Code07_Policija1), (_java_key_11 := 'cnts'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
        e = jcast('int', Code07_Policija1.head1[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code07_Policija1.to1[e])
                if (Code07_Policija1.dfn[v] == 0):
                    Code07_Policija1.tarjan(v, e)
                    jset(Code07_Policija1.low, u, jstatic('Math', 'min', Code07_Policija1.low[u], Code07_Policija1.low[v]))
                    if (Code07_Policija1.low[v] >= Code07_Policija1.dfn[u]):
                        Code07_Policija1.cntn = jcast('int', (Code07_Policija1.cntn + 1))
                        if (Code07_Policija1.low[v] > Code07_Policija1.dfn[u]):
                            Code07_Policija1.addCut(u, v, Code07_Policija1.cntn)
                        Code07_Policija1.addEdge2(Code07_Policija1.cntn, u)
                        Code07_Policija1.addEdge2(u, Code07_Policija1.cntn)
                        pop = 0
                        while True:
                            pop = jcast('int', Code07_Policija1.sta[((_java_obj_14 := Code07_Policija1), (_java_key_15 := 'cnts'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (-1)))), _java_old_16)[4]])
                            Code07_Policija1.addEdge2(Code07_Policija1.cntn, pop)
                            Code07_Policija1.addEdge2(pop, Code07_Policija1.cntn)
                            if not ((pop != v)):
                                break
                else:
                    jset(Code07_Policija1.low, u, jstatic('Math', 'min', Code07_Policija1.low[u], Code07_Policija1.dfn[v]))
            except JContinue as _java_control_13:
                if _java_control_13.label not in (None,):
                    raise
            except JBreak as _java_control_13:
                if _java_control_13.label not in (None,):
                    raise
                break
            e = jcast('int', Code07_Policija1.next1[e])

    @staticmethod
    def dfs1(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code07_Policija1.fa[u] = jcast('int', f)
        Code07_Policija1.dep[u] = jcast('int', jcast('int', jadd(Code07_Policija1.dep[f], 1)))
        Code07_Policija1.siz[u] = jcast('int', 1)
        e = jcast('int', Code07_Policija1.head2[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code07_Policija1.to2[e])
            if (v != f):
                Code07_Policija1.dfs1(v, u)
                Code07_Policija1.siz[u] = jcast('int', jcast('int', jadd(Code07_Policija1.siz[u], Code07_Policija1.siz[v])))
                if ((Code07_Policija1.son[u] == 0) or (Code07_Policija1.siz[Code07_Policija1.son[u]] < Code07_Policija1.siz[v])):
                    Code07_Policija1.son[u] = jcast('int', v)
            e = jcast('int', Code07_Policija1.next2[e])

    @staticmethod
    def dfs2(u, t):
        u = jcast('int', u)
        t = jcast('int', t)
        Code07_Policija1.top[u] = jcast('int', t)
        if (Code07_Policija1.son[u] == 0):
            return
        Code07_Policija1.dfs2(Code07_Policija1.son[u], t)
        e = jcast('int', Code07_Policija1.head2[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code07_Policija1.to2[e])
            if ((v != Code07_Policija1.fa[u]) and (v != Code07_Policija1.son[u])):
                Code07_Policija1.dfs2(v, v)
            e = jcast('int', Code07_Policija1.next2[e])

    @staticmethod
    def mustPass(a, b, c):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        while (Code07_Policija1.top[a] != Code07_Policija1.top[b]):
            if (Code07_Policija1.dep[Code07_Policija1.top[a]] < Code07_Policija1.dep[Code07_Policija1.top[b]]):
                tmp = jcast('int', a)
                a = jcast('int', b)
                b = jcast('int', tmp)
            if ((Code07_Policija1.top[c] == Code07_Policija1.top[a]) and (Code07_Policija1.dep[c] <= Code07_Policija1.dep[a])):
                return jcast('boolean', True)
            a = jcast('int', Code07_Policija1.fa[Code07_Policija1.top[a]])
        if (Code07_Policija1.dep[a] < Code07_Policija1.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        return jcast('boolean', (((Code07_Policija1.top[a] == Code07_Policija1.top[c]) and (Code07_Policija1.dep[b] <= Code07_Policija1.dep[c])) and (Code07_Policija1.dep[c] <= Code07_Policija1.dep[a])))

    @staticmethod
    def main(args):
        in_ = Code07_Policija1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_Policija1.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_Policija1.m = jcast('int', jcall(in_, 'nextInt'))
        Code07_Policija1.cntn = jcast('int', Code07_Policija1.n)
        Code07_Policija1.cnt1 = jcast('int', 1)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code07_Policija1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code07_Policija1.addEdge1(u, v)
            Code07_Policija1.addEdge1(v, u)
            i = jcast('int', (i + 1))
        Code07_Policija1.tarjan(1, 0)
        Code07_Policija1.dfs1(1, 0)
        Code07_Policija1.dfs2(1, 1)
        Code07_Policija1.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        op = 0
        a = 0
        b = 0
        c = 0
        d = 0
        while (i <= Code07_Policija1.q):
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                a = jcast('int', jcall(in_, 'nextInt'))
                b = jcast('int', jcall(in_, 'nextInt'))
                c = jcast('int', jcall(in_, 'nextInt'))
                d = jcast('int', jcall(in_, 'nextInt'))
                cut = jcast('int', Code07_Policija1.getCut(c, d))
                if (cut == 0):
                    jcall(out, 'println', 'yes')
                else:
                    jcall(out, 'println', ('no' if Code07_Policija1.mustPass(a, b, cut) else 'yes'))
            else:
                a = jcast('int', jcall(in_, 'nextInt'))
                b = jcast('int', jcall(in_, 'nextInt'))
                c = jcast('int', jcall(in_, 'nextInt'))
                jcall(out, 'println', ('no' if Code07_Policija1.mustPass(a, b, c) else 'yes'))
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
            return jcast('int', self.buffer[((_java_obj_17 := self), (_java_key_18 := 'ptr'), (_java_old_19 := jget(_java_obj_17, _java_key_18)), jset(_java_obj_17, _java_key_18, jcast('int', (_java_old_19 + (1)))), _java_old_19)[4]])

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
            raise TypeError("No matching overload for Code07_Policija1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_Policija1.MAXN = jcast('int', 100001)
Code07_Policija1.MAXM = jcast('int', 500001)
Code07_Policija1.n = jcast('int', 0)
Code07_Policija1.m = jcast('int', 0)
Code07_Policija1.q = jcast('int', 0)
Code07_Policija1.cntn = jcast('int', 0)
Code07_Policija1.head1 = jarray('int', [Code07_Policija1.MAXN])
Code07_Policija1.next1 = jarray('int', [jcast('int', (Code07_Policija1.MAXM << (1 & 31)))])
Code07_Policija1.to1 = jarray('int', [jcast('int', (Code07_Policija1.MAXM << (1 & 31)))])
Code07_Policija1.cnt1 = jcast('int', 0)
Code07_Policija1.head2 = jarray('int', [jcast('int', (Code07_Policija1.MAXN << (1 & 31)))])
Code07_Policija1.next2 = jarray('int', [jcast('int', (Code07_Policija1.MAXM << (2 & 31)))])
Code07_Policija1.to2 = jarray('int', [jcast('int', (Code07_Policija1.MAXM << (2 & 31)))])
Code07_Policija1.cnt2 = jcast('int', 0)
Code07_Policija1.dfn = jarray('int', [Code07_Policija1.MAXN])
Code07_Policija1.low = jarray('int', [Code07_Policija1.MAXN])
Code07_Policija1.cntd = jcast('int', 0)
Code07_Policija1.sta = jarray('int', [Code07_Policija1.MAXN])
Code07_Policija1.cnts = jcast('int', 0)
Code07_Policija1.cutMap = jnew('HashMap')
Code07_Policija1.fa = jarray('int', [jcast('int', (Code07_Policija1.MAXN << (1 & 31)))])
Code07_Policija1.dep = jarray('int', [jcast('int', (Code07_Policija1.MAXN << (1 & 31)))])
Code07_Policija1.siz = jarray('int', [jcast('int', (Code07_Policija1.MAXN << (1 & 31)))])
Code07_Policija1.son = jarray('int', [jcast('int', (Code07_Policija1.MAXN << (1 & 31)))])
Code07_Policija1.top = jarray('int', [jcast('int', (Code07_Policija1.MAXN << (1 & 31)))])

if __name__ == '__main__':
    Code07_Policija1.main([])
