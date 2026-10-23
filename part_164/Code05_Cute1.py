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

# 德丽莎世界第一可爱，Python版
# 一共有n个怪兽，每个怪兽有a、b、c、d四个能力值，以及打败之后的收益v
# 可以选择任意顺序打怪兽，每次打的怪兽的四种能力值都不能小于上次打的怪兽
# 打印能获得的最大收益，可能所有怪兽收益都是负数，那也需要至少打一只怪兽
# 1 <= n <= 5 * 10^4
# -10^5 <= a、b、c、d <= +10^5
# -10^9 <= v <= +10^9
# 测试链接 : https://www.luogu.com.cn/problem/P5621
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 题目对运行时间限制较紧，应按 Python 实现的实际开销评估
# 对应实现可参考 Code05_Cute2.py
# 两个版本保留相同的算法逻辑
class Code05_Cute1:
    __java_fields__ = {'cmp1': 'cmp1', 'cmp2': 'cmp2', 'cmp3': 'cmp3', 'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 's': 's', 'arr': 'arr', 'sortd': 'sortd', 'tmp1': 'tmp1', 'tmp2': 'tmp2', 'tree': 'tree', 'dp': 'dp'}
    class Node:
        __java_fields__ = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'i': 'i', 'v': 'v', 'left': 'left'}
        # a：实例字段，在构造函数中初始化。
        # b：实例字段，在构造函数中初始化。
        # c：实例字段，在构造函数中初始化。
        # d：实例字段，在构造函数中初始化。
        # i：实例字段，在构造函数中初始化。
        # v：实例字段，在构造函数中初始化。
        # 是否是原左组的对象
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
            raise TypeError("No matching overload for Code05_Cute1.Node.Node")


    class Cmp1:
        __java_fields__ = {}
        def compare(self, x, y):
            if (jget(x, 'a') != jget(y, 'a')):
                return jcast('int', jcast('int', (jget(x, 'a') - jget(y, 'a'))))
            if (jget(x, 'b') != jget(y, 'b')):
                return jcast('int', jcast('int', (jget(x, 'b') - jget(y, 'b'))))
            if (jget(x, 'c') != jget(y, 'c')):
                return jcast('int', jcast('int', (jget(x, 'c') - jget(y, 'c'))))
            if (jget(x, 'd') != jget(y, 'd')):
                return jcast('int', jcast('int', (jget(x, 'd') - jget(y, 'd'))))
            return jcast('int', jstatic('Long', 'compare', jget(y, 'v'), jget(x, 'v')))

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
    n = 0
    s = 0
    arr = None
    sortd = None
    # 根据b重排时，准备的辅助数组，不改变原始次序
    tmp1 = None
    # 根据c重排时，准备的辅助数组，不改变原始次序
    tmp2 = None
    # 树状数组，维护前缀最大值
    tree = None
    # dp[i]表示i号怪兽最后杀死的情况下，最大的收益
    dp = None
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def more(i, num):
        i = jcast('int', i)
        num = jcast('long', num)
        while (i <= Code05_Cute1.s):
            jset(Code05_Cute1.tree, i, jstatic('Math', 'max', Code05_Cute1.tree[i], num))
            i = jcast('int', jcast('int', jadd(i, Code05_Cute1.lowbit(i))))

    @staticmethod
    def query(i):
        i = jcast('int', i)
        ret = jcast('long', jcast('long', (-Code05_Cute1.INF)))
        while (i > 0):
            ret = jcast('long', jstatic('Math', 'max', ret, Code05_Cute1.tree[i]))
            i = jcast('int', jcast('int', (i - Code05_Cute1.lowbit(i))))
        return jcast('long', ret)

    @staticmethod
    def clear(i):
        i = jcast('int', i)
        while (i <= Code05_Cute1.s):
            Code05_Cute1.tree[i] = jcast('long', jcast('long', (-Code05_Cute1.INF)))
            i = jcast('int', jcast('int', jadd(i, Code05_Cute1.lowbit(i))))

    @staticmethod
    def merge(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        i = jcast('int', l)
        while (i <= r):
            Code05_Cute1.tmp2[i] = Code05_Cute1.tmp1[i]
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_Cute1.tmp2, l, jcast('int', jadd(m, 1)), Code05_Cute1.cmp3)
        jstatic('Arrays', 'sort', Code05_Cute1.tmp2, jcast('int', jadd(m, 1)), jcast('int', jadd(r, 1)), Code05_Cute1.cmp3)
        p1 = 0
        p2 = 0
        p1 = jcast('int', jcast('int', (l - 1)))
        p2 = jcast('int', jcast('int', jadd(m, 1)))
        while (p2 <= r):
            while ((jcast('int', jadd(p1, 1)) <= m) and (jget(Code05_Cute1.tmp2[jcast('int', jadd(p1, 1))], 'c') <= jget(Code05_Cute1.tmp2[p2], 'c'))):
                p1 = jcast('int', (p1 + 1))
                if jget(Code05_Cute1.tmp2[p1], 'left'):
                    Code05_Cute1.more(jget(Code05_Cute1.tmp2[p1], 'd'), Code05_Cute1.dp[jget(Code05_Cute1.tmp2[p1], 'i')])
            if (not jget(Code05_Cute1.tmp2[p2], 'left')):
                jset(Code05_Cute1.dp, jget(Code05_Cute1.tmp2[p2], 'i'), jstatic('Math', 'max', Code05_Cute1.dp[jget(Code05_Cute1.tmp2[p2], 'i')], jcast('long', jadd(Code05_Cute1.query(jget(Code05_Cute1.tmp2[p2], 'd')), jget(Code05_Cute1.tmp2[p2], 'v')))))
            p2 = jcast('int', (p2 + 1))
        i = jcast('int', l)
        while (i <= p1):
            if jget(Code05_Cute1.tmp2[i], 'left'):
                Code05_Cute1.clear(jget(Code05_Cute1.tmp2[i], 'd'))
            i = jcast('int', (i + 1))

    # tmp1[l..r]中所有对象根据b属性值稳定排序了
    # 让每个原左组的对象影响到后面每个原右组对象(更新dp)
    @staticmethod
    def cdq2(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code05_Cute1.cdq2(l, mid)
        Code05_Cute1.merge(l, mid, r)
        Code05_Cute1.cdq2(jcast('int', jadd(mid, 1)), r)

    @staticmethod
    def cdq1(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code05_Cute1.cdq1(l, mid)
        i = jcast('int', l)
        while (i <= r):
            Code05_Cute1.tmp1[i] = Code05_Cute1.arr[i]
            jset(Code05_Cute1.tmp1[i], 'left', (i <= mid))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_Cute1.tmp1, l, jcast('int', jadd(r, 1)), Code05_Cute1.cmp2)
        Code05_Cute1.cdq2(l, r)
        Code05_Cute1.cdq1(jcast('int', jadd(mid, 1)), r)

    @staticmethod
    def lower(num):
        num = jcast('long', num)
        l = jcast('int', 1)
        r = jcast('int', Code05_Cute1.s)
        m = 0
        ans = jcast('int', 1)
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code05_Cute1.sortd[m] >= num):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code05_Cute1.n):
            Code05_Cute1.sortd[i] = jcast('int', jget(Code05_Cute1.arr[i], 'd'))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_Cute1.sortd, 1, jcast('int', jadd(Code05_Cute1.n, 1)))
        Code05_Cute1.s = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code05_Cute1.n):
            if (Code05_Cute1.sortd[Code05_Cute1.s] != Code05_Cute1.sortd[i]):
                jset(Code05_Cute1.sortd, ((_java_obj_1 := Code05_Cute1), (_java_key_2 := 's'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_Cute1.sortd[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Cute1.n):
            jset(Code05_Cute1.arr[i], 'd', Code05_Cute1.lower(jget(Code05_Cute1.arr[i], 'd')))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_Cute1.arr, 1, jcast('int', jadd(Code05_Cute1.n, 1)), Code05_Cute1.cmp1)
        m = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code05_Cute1.n):
            if ((((jget(Code05_Cute1.arr[m], 'a') == jget(Code05_Cute1.arr[i], 'a')) and (jget(Code05_Cute1.arr[m], 'b') == jget(Code05_Cute1.arr[i], 'b'))) and (jget(Code05_Cute1.arr[m], 'c') == jget(Code05_Cute1.arr[i], 'c'))) and (jget(Code05_Cute1.arr[m], 'd') == jget(Code05_Cute1.arr[i], 'd'))):
                if (jget(Code05_Cute1.arr[i], 'v') > 0):
                    ((_java_obj_4 := Code05_Cute1.arr[m]), (_java_key_5 := 'v'), jset(_java_obj_4, _java_key_5, jcast('long', jadd(jget(_java_obj_4, _java_key_5), jget(Code05_Cute1.arr[i], 'v')))))[2]
            else:
                jset(Code05_Cute1.arr, (m := jcast('int', (m + (1)))), Code05_Cute1.arr[i])
            i = jcast('int', (i + 1))
        Code05_Cute1.n = jcast('int', m)
        i = jcast('int', 1)
        while (i <= Code05_Cute1.n):
            jset(Code05_Cute1.arr[i], 'i', i)
            Code05_Cute1.dp[i] = jcast('long', jget(Code05_Cute1.arr[i], 'v'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Cute1.s):
            Code05_Cute1.tree[i] = jcast('long', jcast('long', (-Code05_Cute1.INF)))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code05_Cute1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_Cute1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        a = 0
        b = 0
        c = 0
        d = 0
        v = 0
        while (i <= Code05_Cute1.n):
            a = jcast('int', jcall(in_, 'nextInt'))
            b = jcast('int', jcall(in_, 'nextInt'))
            c = jcast('int', jcall(in_, 'nextInt'))
            d = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            jset(Code05_Cute1.arr, i, Code05_Cute1.Node(a, b, c, d, v, _java_ctor=0))
            i = jcast('int', (i + 1))
        Code05_Cute1.prepare()
        Code05_Cute1.cdq1(1, Code05_Cute1.n)
        ans = jcast('long', jcast('long', (-Code05_Cute1.INF)))
        i = jcast('int', 1)
        while (i <= Code05_Cute1.n):
            ans = jcast('long', jstatic('Math', 'max', ans, Code05_Cute1.dp[i]))
            i = jcast('int', (i + 1))
        jcall(out, 'println', ans)
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
            self.buffer = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_Cute1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Cute1.cmp1 = Code05_Cute1.Cmp1()
Code05_Cute1.cmp2 = Code05_Cute1.Cmp2()
Code05_Cute1.cmp3 = Code05_Cute1.Cmp3()
Code05_Cute1.MAXN = jcast('int', 50001)
Code05_Cute1.INF = jcast('long', jcast('long', jadd(1e+18, 1)))
Code05_Cute1.n = jcast('int', 0)
Code05_Cute1.s = jcast('int', 0)
Code05_Cute1.arr = jarray('Node', [Code05_Cute1.MAXN])
Code05_Cute1.sortd = jarray('int', [Code05_Cute1.MAXN])
Code05_Cute1.tmp1 = jarray('Node', [Code05_Cute1.MAXN])
Code05_Cute1.tmp2 = jarray('Node', [Code05_Cute1.MAXN])
Code05_Cute1.tree = jarray('long', [Code05_Cute1.MAXN])
Code05_Cute1.dp = jarray('long', [Code05_Cute1.MAXN])

if __name__ == '__main__':
    Code05_Cute1.main([])
