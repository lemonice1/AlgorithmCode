# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 受欢迎的牛，Python版
# 一共有n只牛，牛和牛之间存在喜欢关系，喜欢关系是有向的
# 喜欢关系可以传递，如果a喜欢b，b喜欢c，那么a也喜欢c
# 每只牛都喜欢自己，如果某只牛被所有牛喜欢，那么这只牛是明星
# 给定m个喜欢关系，打印明星的数量
# 1 <= n <= 10^4
# 1 <= m <= 5 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P2341
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_PopularCow1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccSiz': 'sccSiz', 'sccCnt': 'sccCnt', 'outdegree': 'outdegree'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
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
    sccSiz = None
    sccCnt = 0
    outdegree = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_PopularCow1.nxt, ((_java_obj_1 := Code04_PopularCow1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_PopularCow1.head[u])
        Code04_PopularCow1.to[Code04_PopularCow1.cntg] = jcast('int', v)
        Code04_PopularCow1.head[u] = jcast('int', Code04_PopularCow1.cntg)

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code04_PopularCow1.dfn, u, jset(Code04_PopularCow1.low, u, ((_java_obj_4 := Code04_PopularCow1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code04_PopularCow1.sta, ((_java_obj_7 := Code04_PopularCow1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code04_PopularCow1.head[u])
        while (e > 0):
            v = jcast('int', Code04_PopularCow1.to[e])
            if (Code04_PopularCow1.dfn[v] == 0):
                Code04_PopularCow1.tarjan(v)
                jset(Code04_PopularCow1.low, u, jstatic('Math', 'min', Code04_PopularCow1.low[u], Code04_PopularCow1.low[v]))
            else:
                if (Code04_PopularCow1.belong[v] == 0):
                    jset(Code04_PopularCow1.low, u, jstatic('Math', 'min', Code04_PopularCow1.low[u], Code04_PopularCow1.dfn[v]))
            e = jcast('int', Code04_PopularCow1.nxt[e])
        if (Code04_PopularCow1.dfn[u] == Code04_PopularCow1.low[u]):
            Code04_PopularCow1.sccCnt = jcast('int', (Code04_PopularCow1.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code04_PopularCow1.sta[((_java_obj_10 := Code04_PopularCow1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code04_PopularCow1.belong[pop] = jcast('int', Code04_PopularCow1.sccCnt)
                Code04_PopularCow1.sccSiz[Code04_PopularCow1.sccCnt] = jcast('int', (Code04_PopularCow1.sccSiz[Code04_PopularCow1.sccCnt] + 1))
                if not ((pop != u)):
                    break

    @staticmethod
    def main(args):
        in_ = Code04_PopularCow1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_PopularCow1.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_PopularCow1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_PopularCow1.m):
            jset(Code04_PopularCow1.a, i, jcall(in_, 'nextInt'))
            jset(Code04_PopularCow1.b, i, jcall(in_, 'nextInt'))
            Code04_PopularCow1.addEdge(Code04_PopularCow1.a[i], Code04_PopularCow1.b[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_PopularCow1.n):
            if (Code04_PopularCow1.dfn[i] == 0):
                Code04_PopularCow1.tarjan(i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_PopularCow1.m):
            scc1 = jcast('int', Code04_PopularCow1.belong[Code04_PopularCow1.a[i]])
            scc2 = jcast('int', Code04_PopularCow1.belong[Code04_PopularCow1.b[i]])
            if (scc1 != scc2):
                Code04_PopularCow1.outdegree[scc1] = jcast('int', (Code04_PopularCow1.outdegree[scc1] + 1))
            i = jcast('int', (i + 1))
        num = jcast('int', 0)
        siz = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_PopularCow1.sccCnt):
            try:
                if (Code04_PopularCow1.outdegree[i] == 0):
                    num = jcast('int', (num + 1))
                    siz = jcast('int', Code04_PopularCow1.sccSiz[i])
                if (num > 1):
                    siz = jcast('int', 0)
                    raise JBreak(None)
            except JContinue as _java_control_13:
                if _java_control_13.label not in (None,):
                    raise
            except JBreak as _java_control_13:
                if _java_control_13.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        jcall(out, 'println', siz)
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
            return jcast('int', self.buffer[((_java_obj_14 := self), (_java_key_15 := 'ptr'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))), _java_old_16)[4]])

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
            raise TypeError("No matching overload for Code04_PopularCow1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_PopularCow1.MAXN = jcast('int', 10001)
Code04_PopularCow1.MAXM = jcast('int', 50001)
Code04_PopularCow1.n = jcast('int', 0)
Code04_PopularCow1.m = jcast('int', 0)
Code04_PopularCow1.a = jarray('int', [Code04_PopularCow1.MAXM])
Code04_PopularCow1.b = jarray('int', [Code04_PopularCow1.MAXM])
Code04_PopularCow1.head = jarray('int', [Code04_PopularCow1.MAXN])
Code04_PopularCow1.nxt = jarray('int', [Code04_PopularCow1.MAXM])
Code04_PopularCow1.to = jarray('int', [Code04_PopularCow1.MAXM])
Code04_PopularCow1.cntg = jcast('int', 0)
Code04_PopularCow1.dfn = jarray('int', [Code04_PopularCow1.MAXN])
Code04_PopularCow1.low = jarray('int', [Code04_PopularCow1.MAXN])
Code04_PopularCow1.cntd = jcast('int', 0)
Code04_PopularCow1.sta = jarray('int', [Code04_PopularCow1.MAXN])
Code04_PopularCow1.top = jcast('int', 0)
Code04_PopularCow1.belong = jarray('int', [Code04_PopularCow1.MAXN])
Code04_PopularCow1.sccSiz = jarray('int', [Code04_PopularCow1.MAXN])
Code04_PopularCow1.sccCnt = jcast('int', 0)
Code04_PopularCow1.outdegree = jarray('int', [Code04_PopularCow1.MAXN])

if __name__ == '__main__':
    Code04_PopularCow1.main([])
