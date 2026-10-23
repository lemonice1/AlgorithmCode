# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 寻找宝藏，Python版
# 一共有n个宝藏，每个宝藏有a、b、c、d四个属性值，以及拿取之后的收益v
# 可以选择任意顺序拿取宝藏，每次拿的宝藏的四种属性值都不能小于上次拿的宝藏
# 打印能获得的最大收益，打印有多少种最佳拿取方法，方法数对 998244353 取余
# 1 <= n <= 8 * 10^4
# 1 <= a、b、c、d、v <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P4849
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_Treasure1:
    __java_fields__ = {'cmp1': 'cmp1', 'cmp2': 'cmp2', 'cmp3': 'cmp3', 'MAXN': 'MAXN', 'INF': 'INF', 'MOD': 'MOD', 'n': 'n', 's': 's', 'arr': 'arr', 'tmp1': 'tmp1', 'tmp2': 'tmp2', 'sortd': 'sortd', 'treeVal': 'treeVal', 'treeCnt': 'treeCnt', 'dp': 'dp', 'cnt': 'cnt', 'queryVal': 'queryVal', 'queryCnt': 'queryCnt'}
    class Node:
        __java_fields__ = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'i': 'i', 'v': 'v', 'left': 'left'}
        # a：实例字段，在构造函数中初始化。
        # b：实例字段，在构造函数中初始化。
        # c：实例字段，在构造函数中初始化。
        # d：实例字段，在构造函数中初始化。
        # i：实例字段，在构造函数中初始化。
        # v：实例字段，在构造函数中初始化。
        # left：实例字段，在构造函数中初始化。
        def _java_init_0(self, a_, b_, c_, d_, v_):
            a_ = jcast('int', a_)
            b_ = jcast('int', b_)
            c_ = jcast('int', c_)
            d_ = jcast('int', d_)
            v_ = jcast('long', v_)
            self.a = jcast('int', a_)
            self.b = jcast('int', b_)
            self.c = jcast('int', c_)
            self.d = jcast('int', d_)
            self.v = jcast('long', v_)

        def __init__(self, *args, _java_ctor=None):
            self.a = jcast('int', 0)
            self.b = jcast('int', 0)
            self.c = jcast('int', 0)
            self.d = jcast('int', 0)
            self.i = jcast('int', 0)
            self.v = jcast('long', 0)
            self.left = jcast('boolean', False)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int', 'int', 'int', 'int', 'long']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code06_Treasure1.Node.Node")


    class Cmp1:
        __java_fields__ = {}
        def compare(self, x, y):
            if (jget(x, 'a') != jget(y, 'a')):
                return jcast('int', jcast('int', (jget(x, 'a') - jget(y, 'a'))))
            if (jget(x, 'b') != jget(y, 'b')):
                return jcast('int', jcast('int', (jget(x, 'b') - jget(y, 'b'))))
            if (jget(x, 'c') != jget(y, 'c')):
                return jcast('int', jcast('int', (jget(x, 'c') - jget(y, 'c'))))
            return jcast('int', jcast('int', (jget(x, 'd') - jget(y, 'd'))))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    # 根据属性b进行排序，b一样的对象，保持原始次序
    class Cmp2:
        __java_fields__ = {}
        def compare(self, x, y):
            if (jget(x, 'b') != jget(y, 'b')):
                return jcast('int', jcast('int', (jget(x, 'b') - jget(y, 'b'))))
            return jcast('int', jcast('int', (jget(x, 'i') - jget(y, 'i'))))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    # 根据属性c进行排序，c一样的对象，保持原始次序
    class Cmp3:
        __java_fields__ = {}
        def compare(self, x, y):
            if (jget(x, 'c') != jget(y, 'c')):
                return jcast('int', jcast('int', (jget(x, 'c') - jget(y, 'c'))))
            return jcast('int', jcast('int', (jget(x, 'i') - jget(y, 'i'))))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    cmp1 = None
    cmp2 = None
    cmp3 = None
    MAXN = 0
    INF = 0
    MOD = 0
    n = 0
    s = 0
    arr = None
    tmp1 = None
    tmp2 = None
    sortd = None
    treeVal = None
    treeCnt = None
    dp = None
    cnt = None
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def more(i, v, c):
        i = jcast('int', i)
        v = jcast('long', v)
        c = jcast('int', c)
        while (i <= Code06_Treasure1.s):
            if (v > Code06_Treasure1.treeVal[i]):
                Code06_Treasure1.treeVal[i] = jcast('long', v)
                Code06_Treasure1.treeCnt[i] = jcast('int', jcast('int', jmod(c, Code06_Treasure1.MOD)))
            else:
                if (v == Code06_Treasure1.treeVal[i]):
                    Code06_Treasure1.treeCnt[i] = jcast('int', jcast('int', jmod(jcast('int', jadd(Code06_Treasure1.treeCnt[i], c)), Code06_Treasure1.MOD)))
            i = jcast('int', jcast('int', jadd(i, Code06_Treasure1.lowbit(i))))

    queryVal = 0
    queryCnt = 0
    @staticmethod
    def query(i):
        i = jcast('int', i)
        Code06_Treasure1.queryVal = jcast('long', jcast('long', (-Code06_Treasure1.INF)))
        Code06_Treasure1.queryCnt = jcast('int', 0)
        while (i > 0):
            if (Code06_Treasure1.treeVal[i] > Code06_Treasure1.queryVal):
                Code06_Treasure1.queryVal = jcast('long', Code06_Treasure1.treeVal[i])
                Code06_Treasure1.queryCnt = jcast('int', Code06_Treasure1.treeCnt[i])
            else:
                if (Code06_Treasure1.treeVal[i] == Code06_Treasure1.queryVal):
                    Code06_Treasure1.queryCnt = jcast('int', jcast('int', jmod(jcast('int', jadd(Code06_Treasure1.queryCnt, Code06_Treasure1.treeCnt[i])), Code06_Treasure1.MOD)))
            i = jcast('int', jcast('int', (i - Code06_Treasure1.lowbit(i))))

    @staticmethod
    def clear(i):
        i = jcast('int', i)
        while (i <= Code06_Treasure1.s):
            Code06_Treasure1.treeVal[i] = jcast('long', jcast('long', (-Code06_Treasure1.INF)))
            Code06_Treasure1.treeCnt[i] = jcast('int', 0)
            i = jcast('int', jcast('int', jadd(i, Code06_Treasure1.lowbit(i))))

    @staticmethod
    def merge(l, mid, r):
        l = jcast('int', l)
        mid = jcast('int', mid)
        r = jcast('int', r)
        i = jcast('int', l)
        while (i <= r):
            Code06_Treasure1.tmp2[i] = Code06_Treasure1.tmp1[i]
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code06_Treasure1.tmp2, l, jcast('int', jadd(mid, 1)), Code06_Treasure1.cmp3)
        jstatic('Arrays', 'sort', Code06_Treasure1.tmp2, jcast('int', jadd(mid, 1)), jcast('int', jadd(r, 1)), Code06_Treasure1.cmp3)
        p1 = 0
        p2 = 0
        id = 0
        p1 = jcast('int', jcast('int', (l - 1)))
        p2 = jcast('int', jcast('int', jadd(mid, 1)))
        while (p2 <= r):
            while ((jcast('int', jadd(p1, 1)) <= mid) and (jget(Code06_Treasure1.tmp2[jcast('int', jadd(p1, 1))], 'c') <= jget(Code06_Treasure1.tmp2[p2], 'c'))):
                p1 = jcast('int', (p1 + 1))
                if jget(Code06_Treasure1.tmp2[p1], 'left'):
                    Code06_Treasure1.more(jget(Code06_Treasure1.tmp2[p1], 'd'), Code06_Treasure1.dp[jget(Code06_Treasure1.tmp2[p1], 'i')], Code06_Treasure1.cnt[jget(Code06_Treasure1.tmp2[p1], 'i')])
            if (not jget(Code06_Treasure1.tmp2[p2], 'left')):
                Code06_Treasure1.query(jget(Code06_Treasure1.tmp2[p2], 'd'))
                id = jcast('int', jget(Code06_Treasure1.tmp2[p2], 'i'))
                if (jcast('long', jadd(Code06_Treasure1.queryVal, jget(Code06_Treasure1.tmp2[p2], 'v'))) > Code06_Treasure1.dp[id]):
                    Code06_Treasure1.dp[id] = jcast('long', jcast('long', jadd(Code06_Treasure1.queryVal, jget(Code06_Treasure1.tmp2[p2], 'v'))))
                    Code06_Treasure1.cnt[id] = jcast('int', Code06_Treasure1.queryCnt)
                else:
                    if (jcast('long', jadd(Code06_Treasure1.queryVal, jget(Code06_Treasure1.tmp2[p2], 'v'))) == Code06_Treasure1.dp[id]):
                        Code06_Treasure1.cnt[id] = jcast('int', jcast('int', jmod(jcast('int', jadd(Code06_Treasure1.cnt[id], Code06_Treasure1.queryCnt)), Code06_Treasure1.MOD)))
            p2 = jcast('int', (p2 + 1))
        i = jcast('int', l)
        while (i <= p1):
            if jget(Code06_Treasure1.tmp2[i], 'left'):
                Code06_Treasure1.clear(jget(Code06_Treasure1.tmp2[i], 'd'))
            i = jcast('int', (i + 1))

    @staticmethod
    def cdq2(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code06_Treasure1.cdq2(l, mid)
        Code06_Treasure1.merge(l, mid, r)
        Code06_Treasure1.cdq2(jcast('int', jadd(mid, 1)), r)

    @staticmethod
    def cdq1(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code06_Treasure1.cdq1(l, mid)
        i = jcast('int', l)
        while (i <= r):
            Code06_Treasure1.tmp1[i] = Code06_Treasure1.arr[i]
            jset(Code06_Treasure1.tmp1[i], 'left', (i <= mid))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code06_Treasure1.tmp1, l, jcast('int', jadd(r, 1)), Code06_Treasure1.cmp2)
        Code06_Treasure1.cdq2(l, r)
        Code06_Treasure1.cdq1(jcast('int', jadd(mid, 1)), r)

    @staticmethod
    def lower(x):
        x = jcast('int', x)
        l = jcast('int', 1)
        r = jcast('int', Code06_Treasure1.s)
        ans = jcast('int', 1)
        while (l <= r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code06_Treasure1.sortd[mid] >= x):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code06_Treasure1.n):
            Code06_Treasure1.sortd[i] = jcast('int', jget(Code06_Treasure1.arr[i], 'd'))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code06_Treasure1.sortd, 1, jcast('int', jadd(Code06_Treasure1.n, 1)))
        Code06_Treasure1.s = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code06_Treasure1.n):
            if (Code06_Treasure1.sortd[Code06_Treasure1.s] != Code06_Treasure1.sortd[i]):
                jset(Code06_Treasure1.sortd, ((_java_obj_1 := Code06_Treasure1), (_java_key_2 := 's'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_Treasure1.sortd[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_Treasure1.n):
            jset(Code06_Treasure1.arr[i], 'd', Code06_Treasure1.lower(jget(Code06_Treasure1.arr[i], 'd')))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code06_Treasure1.arr, 1, jcast('int', jadd(Code06_Treasure1.n, 1)), Code06_Treasure1.cmp1)
        m = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code06_Treasure1.n):
            if ((((jget(Code06_Treasure1.arr[m], 'a') == jget(Code06_Treasure1.arr[i], 'a')) and (jget(Code06_Treasure1.arr[m], 'b') == jget(Code06_Treasure1.arr[i], 'b'))) and (jget(Code06_Treasure1.arr[m], 'c') == jget(Code06_Treasure1.arr[i], 'c'))) and (jget(Code06_Treasure1.arr[m], 'd') == jget(Code06_Treasure1.arr[i], 'd'))):
                ((_java_obj_4 := Code06_Treasure1.arr[m]), (_java_key_5 := 'v'), jset(_java_obj_4, _java_key_5, jcast('long', jadd(jget(_java_obj_4, _java_key_5), jget(Code06_Treasure1.arr[i], 'v')))))[2]
            else:
                jset(Code06_Treasure1.arr, (m := jcast('int', (m + (1)))), Code06_Treasure1.arr[i])
            i = jcast('int', (i + 1))
        Code06_Treasure1.n = jcast('int', m)
        i = jcast('int', 1)
        while (i <= Code06_Treasure1.n):
            jset(Code06_Treasure1.arr[i], 'i', i)
            Code06_Treasure1.dp[i] = jcast('long', jget(Code06_Treasure1.arr[i], 'v'))
            Code06_Treasure1.cnt[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_Treasure1.s):
            Code06_Treasure1.treeVal[i] = jcast('long', jcast('long', (-Code06_Treasure1.INF)))
            Code06_Treasure1.treeCnt[i] = jcast('int', 0)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code06_Treasure1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_Treasure1.n = jcast('int', jcall(in_, 'nextInt'))
        jcall(in_, 'nextInt')
        i = jcast('int', 1)
        a = 0
        b = 0
        c = 0
        d = 0
        v = 0
        while (i <= Code06_Treasure1.n):
            a = jcast('int', jcall(in_, 'nextInt'))
            b = jcast('int', jcall(in_, 'nextInt'))
            c = jcast('int', jcall(in_, 'nextInt'))
            d = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            jset(Code06_Treasure1.arr, i, Code06_Treasure1.Node(a, b, c, d, v, _java_ctor=0))
            i = jcast('int', (i + 1))
        Code06_Treasure1.prepare()
        Code06_Treasure1.cdq1(1, Code06_Treasure1.n)
        best = jcast('long', 0)
        ways = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code06_Treasure1.n):
            best = jcast('long', jstatic('Math', 'max', best, Code06_Treasure1.dp[i]))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_Treasure1.n):
            if (Code06_Treasure1.dp[i] == best):
                ways = jcast('int', jcast('int', jmod(jcast('int', jadd(ways, Code06_Treasure1.cnt[i])), Code06_Treasure1.MOD)))
            i = jcast('int', (i + 1))
        jcall(out, 'println', best)
        jcall(out, 'println', jcast('int', jmod(ways, Code06_Treasure1.MOD)))
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
            return jcast('int', self.buffer[((_java_obj_6 := self), (_java_key_7 := 'ptr'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))), _java_old_8)[4]])

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
            self.buffer = jarray('byte', [jcast('int', (1 << (12 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code06_Treasure1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_Treasure1.cmp1 = Code06_Treasure1.Cmp1()
Code06_Treasure1.cmp2 = Code06_Treasure1.Cmp2()
Code06_Treasure1.cmp3 = Code06_Treasure1.Cmp3()
Code06_Treasure1.MAXN = jcast('int', 80001)
Code06_Treasure1.INF = jcast('long', jcast('long', jadd(1e+18, 1)))
Code06_Treasure1.MOD = jcast('int', 998244353)
Code06_Treasure1.n = jcast('int', 0)
Code06_Treasure1.s = jcast('int', 0)
Code06_Treasure1.arr = jarray('Node', [Code06_Treasure1.MAXN])
Code06_Treasure1.tmp1 = jarray('Node', [Code06_Treasure1.MAXN])
Code06_Treasure1.tmp2 = jarray('Node', [Code06_Treasure1.MAXN])
Code06_Treasure1.sortd = jarray('int', [Code06_Treasure1.MAXN])
Code06_Treasure1.treeVal = jarray('long', [Code06_Treasure1.MAXN])
Code06_Treasure1.treeCnt = jarray('int', [Code06_Treasure1.MAXN])
Code06_Treasure1.dp = jarray('long', [Code06_Treasure1.MAXN])
Code06_Treasure1.cnt = jarray('int', [Code06_Treasure1.MAXN])
Code06_Treasure1.queryVal = jcast('long', 0)
Code06_Treasure1.queryCnt = jcast('int', 0)

if __name__ == '__main__':
    Code06_Treasure1.main([])
