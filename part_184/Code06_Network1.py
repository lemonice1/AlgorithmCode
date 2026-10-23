# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 网络，Python版
# 给定一张无向图，一共n个点、m条边，保证所有点连通
# 一共q条操作，格式 x y : 点x和点y之间新增一条边，打印此时割边的数量
# 1 <= n <= 10^5
# 1 <= m <= 2 * 10^5
# 测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=2460
# 测试链接 : http://poj.org/problem?id=3694
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_Network1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 't': 't', 'n': 'n', 'm': 'm', 'q': 'q', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'ebccCnt': 'ebccCnt', 'up': 'up', 'dep': 'dep', 'fa': 'fa'}
    MAXN = 0
    MAXM = 0
    t = 0
    n = 0
    m = 0
    q = 0
    a = None
    b = None
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    belong = None
    ebccCnt = 0
    up = None
    dep = None
    fa = None
    @staticmethod
    def prepare():
        Code06_Network1.cntg = jcast('int', 1)
        Code06_Network1.cntd = jcast('int', jset(Code06_Network1, 'top', jset(Code06_Network1, 'ebccCnt', 0)))
        i = jcast('int', 1)
        while (i <= Code06_Network1.n):
            jset(Code06_Network1.head, i, jset(Code06_Network1.dfn, i, jset(Code06_Network1.low, i, 0)))
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code06_Network1.nxt, ((_java_obj_1 := Code06_Network1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_Network1.head[u])
        Code06_Network1.to[Code06_Network1.cntg] = jcast('int', v)
        Code06_Network1.head[u] = jcast('int', Code06_Network1.cntg)

    @staticmethod
    def tarjan(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code06_Network1.dfn, u, jset(Code06_Network1.low, u, ((_java_obj_4 := Code06_Network1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code06_Network1.sta, ((_java_obj_7 := Code06_Network1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code06_Network1.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code06_Network1.to[e])
                if (Code06_Network1.dfn[v] == 0):
                    Code06_Network1.tarjan(v, e)
                    jset(Code06_Network1.low, u, jstatic('Math', 'min', Code06_Network1.low[u], Code06_Network1.low[v]))
                else:
                    jset(Code06_Network1.low, u, jstatic('Math', 'min', Code06_Network1.low[u], Code06_Network1.dfn[v]))
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
            e = jcast('int', Code06_Network1.nxt[e])
        if (Code06_Network1.dfn[u] == Code06_Network1.low[u]):
            Code06_Network1.ebccCnt = jcast('int', (Code06_Network1.ebccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code06_Network1.sta[((_java_obj_11 := Code06_Network1), (_java_key_12 := 'top'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (-1)))), _java_old_13)[4]])
                Code06_Network1.belong[pop] = jcast('int', Code06_Network1.ebccCnt)
                if not ((pop != u)):
                    break

    @staticmethod
    def condense():
        Code06_Network1.cntg = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code06_Network1.ebccCnt):
            Code06_Network1.head[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_Network1.m):
            ebcc1 = jcast('int', Code06_Network1.belong[Code06_Network1.a[i]])
            ebcc2 = jcast('int', Code06_Network1.belong[Code06_Network1.b[i]])
            if (ebcc1 != ebcc2):
                Code06_Network1.addEdge(ebcc1, ebcc2)
                Code06_Network1.addEdge(ebcc2, ebcc1)
            i = jcast('int', (i + 1))

    @staticmethod
    def dfs(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code06_Network1.dep[u] = jcast('int', jcast('int', jadd(Code06_Network1.dep[f], 1)))
        Code06_Network1.up[u] = jcast('int', f)
        Code06_Network1.fa[u] = jcast('int', u)
        e = jcast('int', Code06_Network1.head[u])
        while (e > 0):
            v = jcast('int', Code06_Network1.to[e])
            if (v != f):
                Code06_Network1.dfs(v, u)
            e = jcast('int', Code06_Network1.nxt[e])

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code06_Network1.fa[i]):
            jset(Code06_Network1.fa, i, Code06_Network1.find(Code06_Network1.fa[i]))
        return jcast('int', Code06_Network1.fa[i])

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        x = jcast('int', Code06_Network1.find(x))
        y = jcast('int', Code06_Network1.find(y))
        if (x != y):
            if (Code06_Network1.dep[x] < Code06_Network1.dep[y]):
                Code06_Network1.fa[y] = jcast('int', x)
            else:
                Code06_Network1.fa[x] = jcast('int', y)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        x = jcast('int', Code06_Network1.find(Code06_Network1.belong[x]))
        y = jcast('int', Code06_Network1.find(Code06_Network1.belong[y]))
        while (x != y):
            if (Code06_Network1.dep[x] >= Code06_Network1.dep[y]):
                Code06_Network1.union(x, Code06_Network1.up[x])
                x = jcast('int', Code06_Network1.find(x))
            else:
                Code06_Network1.union(y, Code06_Network1.up[y])
                y = jcast('int', Code06_Network1.find(y))
            Code06_Network1.ebccCnt = jcast('int', (Code06_Network1.ebccCnt - 1))

    @staticmethod
    def main(args):
        in_ = Code06_Network1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_Network1.t = jcast('int', 0)
        Code06_Network1.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_Network1.m = jcast('int', jcall(in_, 'nextInt'))
        while ((Code06_Network1.n != 0) or (Code06_Network1.m != 0)):
            Code06_Network1.prepare()
            i = jcast('int', 1)
            while (i <= Code06_Network1.m):
                jset(Code06_Network1.a, i, jcall(in_, 'nextInt'))
                jset(Code06_Network1.b, i, jcall(in_, 'nextInt'))
                Code06_Network1.addEdge(Code06_Network1.a[i], Code06_Network1.b[i])
                Code06_Network1.addEdge(Code06_Network1.b[i], Code06_Network1.a[i])
                i = jcast('int', (i + 1))
            Code06_Network1.tarjan(1, 0)
            Code06_Network1.condense()
            Code06_Network1.dfs(1, 0)
            jcall(out, 'println', jadd(jadd('Case ', ((_java_obj_14 := Code06_Network1), (_java_key_15 := 't'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))))[3]), ':'))
            Code06_Network1.q = jcast('int', jcall(in_, 'nextInt'))
            i = jcast('int', 1)
            x = 0
            y = 0
            while (i <= Code06_Network1.q):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                Code06_Network1.link(x, y)
                jcall(out, 'println', jcast('int', (Code06_Network1.ebccCnt - 1)))
                i = jcast('int', (i + 1))
            jcall(out, 'println')
            Code06_Network1.n = jcast('int', jcall(in_, 'nextInt'))
            Code06_Network1.m = jcast('int', jcall(in_, 'nextInt'))
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
            raise TypeError("No matching overload for Code06_Network1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_Network1.MAXN = jcast('int', 100001)
Code06_Network1.MAXM = jcast('int', 200001)
Code06_Network1.t = jcast('int', 0)
Code06_Network1.n = jcast('int', 0)
Code06_Network1.m = jcast('int', 0)
Code06_Network1.q = jcast('int', 0)
Code06_Network1.a = jarray('int', [Code06_Network1.MAXM])
Code06_Network1.b = jarray('int', [Code06_Network1.MAXM])
Code06_Network1.head = jarray('int', [Code06_Network1.MAXN])
Code06_Network1.nxt = jarray('int', [jcast('int', (Code06_Network1.MAXM << (1 & 31)))])
Code06_Network1.to = jarray('int', [jcast('int', (Code06_Network1.MAXM << (1 & 31)))])
Code06_Network1.cntg = jcast('int', 0)
Code06_Network1.dfn = jarray('int', [Code06_Network1.MAXN])
Code06_Network1.low = jarray('int', [Code06_Network1.MAXN])
Code06_Network1.cntd = jcast('int', 0)
Code06_Network1.sta = jarray('int', [Code06_Network1.MAXN])
Code06_Network1.top = jcast('int', 0)
Code06_Network1.belong = jarray('int', [Code06_Network1.MAXN])
Code06_Network1.ebccCnt = jcast('int', 0)
Code06_Network1.up = jarray('int', [Code06_Network1.MAXN])
Code06_Network1.dep = jarray('int', [Code06_Network1.MAXN])
Code06_Network1.fa = jarray('int', [Code06_Network1.MAXN])

if __name__ == '__main__':
    Code06_Network1.main([])
