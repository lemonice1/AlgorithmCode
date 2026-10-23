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

# 路径问题，Python版
# 给定一张无向图，一共n个点、m条边，所有点保证连通，无重边和自环
# 给定三个不同的点a、b、c，打印是否存在一条路径
# 从a到达b，然后从b到达c，要求途中不能出现重复的点
# 1 <= n、m <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/AT_abc318_g
# 测试链接 : https://atcoder.jp/contests/abc318/tasks/abc318_g
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_PathProblem2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'a': 'a', 'b': 'b', 'c': 'c', 'cntn': 'cntn', 'head1': 'head1', 'next1': 'next1', 'to1': 'to1', 'cnt1': 'cnt1', 'head2': 'head2', 'next2': 'next2', 'to2': 'to2', 'cnt2': 'cnt2', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'dep': 'dep', 'fa': 'fa', 'flag': 'flag'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    a = 0
    b = 0
    c = 0
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
    dep = None
    fa = None
    flag = None
    @staticmethod
    def addEdge1(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_PathProblem2.next1, ((_java_obj_1 := Code03_PathProblem2), (_java_key_2 := 'cnt1'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_PathProblem2.head1[u])
        Code03_PathProblem2.to1[Code03_PathProblem2.cnt1] = jcast('int', v)
        Code03_PathProblem2.head1[u] = jcast('int', Code03_PathProblem2.cnt1)

    @staticmethod
    def addEdge2(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_PathProblem2.next2, ((_java_obj_4 := Code03_PathProblem2), (_java_key_5 := 'cnt2'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code03_PathProblem2.head2[u])
        Code03_PathProblem2.to2[Code03_PathProblem2.cnt2] = jcast('int', v)
        Code03_PathProblem2.head2[u] = jcast('int', Code03_PathProblem2.cnt2)

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code03_PathProblem2.dfn, u, jset(Code03_PathProblem2.low, u, ((_java_obj_7 := Code03_PathProblem2), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]))
        jset(Code03_PathProblem2.sta, ((_java_obj_10 := Code03_PathProblem2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)
        e = jcast('int', Code03_PathProblem2.head1[u])
        while (e > 0):
            v = jcast('int', Code03_PathProblem2.to1[e])
            if (Code03_PathProblem2.dfn[v] == 0):
                Code03_PathProblem2.tarjan(v)
                jset(Code03_PathProblem2.low, u, jstatic('Math', 'min', Code03_PathProblem2.low[u], Code03_PathProblem2.low[v]))
                if (Code03_PathProblem2.low[v] >= Code03_PathProblem2.dfn[u]):
                    Code03_PathProblem2.cntn = jcast('int', (Code03_PathProblem2.cntn + 1))
                    Code03_PathProblem2.addEdge2(Code03_PathProblem2.cntn, u)
                    Code03_PathProblem2.addEdge2(u, Code03_PathProblem2.cntn)
                    pop = 0
                    while True:
                        pop = jcast('int', Code03_PathProblem2.sta[((_java_obj_13 := Code03_PathProblem2), (_java_key_14 := 'top'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]])
                        Code03_PathProblem2.addEdge2(Code03_PathProblem2.cntn, pop)
                        Code03_PathProblem2.addEdge2(pop, Code03_PathProblem2.cntn)
                        if not ((pop != v)):
                            break
            else:
                jset(Code03_PathProblem2.low, u, jstatic('Math', 'min', Code03_PathProblem2.low[u], Code03_PathProblem2.dfn[v]))
            e = jcast('int', Code03_PathProblem2.next1[e])

    @staticmethod
    def dfs(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code03_PathProblem2.dep[u] = jcast('int', jcast('int', jadd(Code03_PathProblem2.dep[f], 1)))
        Code03_PathProblem2.fa[u] = jcast('int', f)
        e = jcast('int', Code03_PathProblem2.head2[u])
        while (e > 0):
            v = jcast('int', Code03_PathProblem2.to2[e])
            if (v != f):
                Code03_PathProblem2.dfs(v, u)
            e = jcast('int', Code03_PathProblem2.next2[e])

    @staticmethod
    def check():
        e = jcast('int', Code03_PathProblem2.head2[Code03_PathProblem2.b])
        while (e > 0):
            v = jcast('int', Code03_PathProblem2.to2[e])
            Code03_PathProblem2.flag[v] = jcast('boolean', True)
            e = jcast('int', Code03_PathProblem2.next2[e])
        while (Code03_PathProblem2.a != Code03_PathProblem2.c):
            if (Code03_PathProblem2.dep[Code03_PathProblem2.a] < Code03_PathProblem2.dep[Code03_PathProblem2.c]):
                tmp = jcast('int', Code03_PathProblem2.a)
                Code03_PathProblem2.a = jcast('int', Code03_PathProblem2.c)
                Code03_PathProblem2.c = jcast('int', tmp)
            Code03_PathProblem2.a = jcast('int', Code03_PathProblem2.fa[Code03_PathProblem2.a])
            if Code03_PathProblem2.flag[Code03_PathProblem2.a]:
                return jcast('boolean', True)
        return jcast('boolean', False)

    @staticmethod
    def main(args):
        in_ = Code03_PathProblem2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_PathProblem2.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_PathProblem2.m = jcast('int', jcall(in_, 'nextInt'))
        Code03_PathProblem2.a = jcast('int', jcall(in_, 'nextInt'))
        Code03_PathProblem2.b = jcast('int', jcall(in_, 'nextInt'))
        Code03_PathProblem2.c = jcast('int', jcall(in_, 'nextInt'))
        Code03_PathProblem2.cntn = jcast('int', Code03_PathProblem2.n)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code03_PathProblem2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code03_PathProblem2.addEdge1(u, v)
            Code03_PathProblem2.addEdge1(v, u)
            i = jcast('int', (i + 1))
        Code03_PathProblem2.tarjan(1)
        Code03_PathProblem2.dfs(1, 0)
        jcall(out, 'println', ('Yes' if Code03_PathProblem2.check() else 'No'))
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
            raise TypeError("No matching overload for Code03_PathProblem2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_PathProblem2.MAXN = jcast('int', 200001)
Code03_PathProblem2.MAXM = jcast('int', 200001)
Code03_PathProblem2.n = jcast('int', 0)
Code03_PathProblem2.m = jcast('int', 0)
Code03_PathProblem2.a = jcast('int', 0)
Code03_PathProblem2.b = jcast('int', 0)
Code03_PathProblem2.c = jcast('int', 0)
Code03_PathProblem2.cntn = jcast('int', 0)
Code03_PathProblem2.head1 = jarray('int', [Code03_PathProblem2.MAXN])
Code03_PathProblem2.next1 = jarray('int', [jcast('int', (Code03_PathProblem2.MAXM << (1 & 31)))])
Code03_PathProblem2.to1 = jarray('int', [jcast('int', (Code03_PathProblem2.MAXM << (1 & 31)))])
Code03_PathProblem2.cnt1 = jcast('int', 0)
Code03_PathProblem2.head2 = jarray('int', [jcast('int', (Code03_PathProblem2.MAXN << (1 & 31)))])
Code03_PathProblem2.next2 = jarray('int', [jcast('int', (Code03_PathProblem2.MAXM << (2 & 31)))])
Code03_PathProblem2.to2 = jarray('int', [jcast('int', (Code03_PathProblem2.MAXM << (2 & 31)))])
Code03_PathProblem2.cnt2 = jcast('int', 0)
Code03_PathProblem2.dfn = jarray('int', [Code03_PathProblem2.MAXN])
Code03_PathProblem2.low = jarray('int', [Code03_PathProblem2.MAXN])
Code03_PathProblem2.cntd = jcast('int', 0)
Code03_PathProblem2.sta = jarray('int', [Code03_PathProblem2.MAXN])
Code03_PathProblem2.top = jcast('int', 0)
Code03_PathProblem2.dep = jarray('int', [jcast('int', (Code03_PathProblem2.MAXN << (1 & 31)))])
Code03_PathProblem2.fa = jarray('int', [jcast('int', (Code03_PathProblem2.MAXN << (1 & 31)))])
Code03_PathProblem2.flag = jarray('boolean', [jcast('int', (Code03_PathProblem2.MAXN << (1 & 31)))])

if __name__ == '__main__':
    Code03_PathProblem2.main([])
