# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 区间最大匹配，Python版
# 给定长度为n的数组a、长度为m的数组b、一个正数z
# 数组a中数字x、数组b中数字y，如果x + y <= z，那么构成一个匹配
# 已经匹配的数字，不可以重复使用，一共有q条查询，格式如下
# 查询 l r : 数组b[l..r]范围上的数字，随意选择数组a中的数字，打印最多匹配数
# 1 <= n <= 152501
# 1 <= m、q <= 52501
# 1 <= a[i]、b[i]、z <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P4477
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_MaximumMatch1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXQ': 'MAXQ', 'n': 'n', 'm': 'm', 'z': 'z', 'q': 'q', 'a': 'a', 'b': 'b', 'query': 'query', 'bi': 'bi', 'match': 'match', 'resta': 'resta', 'overb': 'overb', 'ans': 'ans'}
    MAXN = 0
    MAXM = 0
    MAXQ = 0
    n = 0
    m = 0
    z = 0
    q = 0
    a = None
    b = None
    query = None
    bi = None
    # 线段树维护匹配信息，a[l..r]和b数组的数字进行匹配，l..r对应的信息在i位置
    # match[i] = v，a[l..r]和b数组的数字，一共匹配了v对
    # resta[i] = v，a[l..r]中还有v个数，可用于匹配b数组的数字
    # overb[i] = v，a[l..r]已经耗尽，但是还有v个b数组的数字没有满足
    match = None
    resta = None
    overb = None
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code04_MaximumMatch1.bi[a[0]] != Code04_MaximumMatch1.bi[b[0]]):
                return jcast('int', jcast('int', (Code04_MaximumMatch1.bi[a[0]] - Code04_MaximumMatch1.bi[b[0]])))
            if (jcast('int', (Code04_MaximumMatch1.bi[a[0]] & 1)) == 1):
                return jcast('int', jcast('int', (a[1] - b[1])))
            else:
                return jcast('int', jcast('int', (b[1] - a[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def up(i):
        i = jcast('int', i)
        l = jcast('int', jcast('int', (i << (1 & 31))))
        r = jcast('int', jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        newMatch = jcast('int', jstatic('Math', 'min', Code04_MaximumMatch1.resta[l], Code04_MaximumMatch1.overb[r]))
        Code04_MaximumMatch1.resta[i] = jcast('int', jcast('int', (jcast('int', jadd(Code04_MaximumMatch1.resta[l], Code04_MaximumMatch1.resta[r])) - newMatch)))
        Code04_MaximumMatch1.overb[i] = jcast('int', jcast('int', (jcast('int', jadd(Code04_MaximumMatch1.overb[l], Code04_MaximumMatch1.overb[r])) - newMatch)))
        Code04_MaximumMatch1.match[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code04_MaximumMatch1.match[l], Code04_MaximumMatch1.match[r])), newMatch)))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code04_MaximumMatch1.match[i] = jcast('int', 0)
            Code04_MaximumMatch1.resta[i] = jcast('int', 1)
            Code04_MaximumMatch1.overb[i] = jcast('int', 0)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code04_MaximumMatch1.build(l, mid, jcast('int', (i << (1 & 31))))
            Code04_MaximumMatch1.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code04_MaximumMatch1.up(i)

    @staticmethod
    def add(jobv, l, r, i):
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            if (Code04_MaximumMatch1.resta[i] == 1):
                Code04_MaximumMatch1.match[i] = jcast('int', 1)
                Code04_MaximumMatch1.resta[i] = jcast('int', 0)
            else:
                Code04_MaximumMatch1.overb[i] = jcast('int', (Code04_MaximumMatch1.overb[i] + 1))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jcast('int', jadd(jobv, Code04_MaximumMatch1.a[jcast('int', jadd(mid, 1))])) <= Code04_MaximumMatch1.z):
                Code04_MaximumMatch1.add(jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            else:
                if (jcast('int', jadd(jobv, Code04_MaximumMatch1.a[l])) <= Code04_MaximumMatch1.z):
                    Code04_MaximumMatch1.add(jobv, l, mid, jcast('int', (i << (1 & 31))))
            Code04_MaximumMatch1.up(i)

    @staticmethod
    def del_(jobv, l, r, i):
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            if (Code04_MaximumMatch1.overb[i] > 0):
                Code04_MaximumMatch1.overb[i] = jcast('int', (Code04_MaximumMatch1.overb[i] - 1))
            else:
                Code04_MaximumMatch1.match[i] = jcast('int', 0)
                Code04_MaximumMatch1.resta[i] = jcast('int', 1)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jcast('int', jadd(jobv, Code04_MaximumMatch1.a[jcast('int', jadd(mid, 1))])) <= Code04_MaximumMatch1.z):
                Code04_MaximumMatch1.del_(jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            else:
                if (jcast('int', jadd(jobv, Code04_MaximumMatch1.a[l])) <= Code04_MaximumMatch1.z):
                    Code04_MaximumMatch1.del_(jobv, l, mid, jcast('int', (i << (1 & 31))))
            Code04_MaximumMatch1.up(i)

    @staticmethod
    def prepare():
        jstatic('Arrays', 'sort', Code04_MaximumMatch1.a, 1, jcast('int', jadd(Code04_MaximumMatch1.n, 1)))
        blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code04_MaximumMatch1.m)))
        i = jcast('int', 1)
        while (i <= Code04_MaximumMatch1.m):
            Code04_MaximumMatch1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_MaximumMatch1.query, 1, jcast('int', jadd(Code04_MaximumMatch1.q, 1)), Code04_MaximumMatch1.QueryCmp())
        Code04_MaximumMatch1.build(1, Code04_MaximumMatch1.n, 1)

    @staticmethod
    def compute():
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_MaximumMatch1.q):
            jobl = jcast('int', Code04_MaximumMatch1.query[i][0])
            jobr = jcast('int', Code04_MaximumMatch1.query[i][1])
            id = jcast('int', Code04_MaximumMatch1.query[i][2])
            while (winl > jobl):
                Code04_MaximumMatch1.add(Code04_MaximumMatch1.b[(winl := jcast('int', (winl + (-1))))], 1, Code04_MaximumMatch1.n, 1)
            while (winr < jobr):
                Code04_MaximumMatch1.add(Code04_MaximumMatch1.b[(winr := jcast('int', (winr + (1))))], 1, Code04_MaximumMatch1.n, 1)
            while (winl < jobl):
                Code04_MaximumMatch1.del_(Code04_MaximumMatch1.b[((_java_old_1 := winl), (winl := jcast('int', (winl + (1)))), _java_old_1)[2]], 1, Code04_MaximumMatch1.n, 1)
            while (winr > jobr):
                Code04_MaximumMatch1.del_(Code04_MaximumMatch1.b[((_java_old_2 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_2)[2]], 1, Code04_MaximumMatch1.n, 1)
            Code04_MaximumMatch1.ans[id] = jcast('int', Code04_MaximumMatch1.match[1])
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code04_MaximumMatch1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_MaximumMatch1.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_MaximumMatch1.m = jcast('int', jcall(in_, 'nextInt'))
        Code04_MaximumMatch1.z = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_MaximumMatch1.n):
            jset(Code04_MaximumMatch1.a, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_MaximumMatch1.m):
            jset(Code04_MaximumMatch1.b, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code04_MaximumMatch1.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_MaximumMatch1.q):
            jset(Code04_MaximumMatch1.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code04_MaximumMatch1.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code04_MaximumMatch1.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code04_MaximumMatch1.prepare()
        Code04_MaximumMatch1.compute()
        i = jcast('int', 1)
        while (i <= Code04_MaximumMatch1.q):
            jcall(out, 'println', Code04_MaximumMatch1.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_3 := self), (_java_key_4 := 'ptr'), (_java_old_5 := jget(_java_obj_3, _java_key_4)), jset(_java_obj_3, _java_key_4, jcast('int', (_java_old_5 + (1)))), _java_old_5)[4]])

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
            raise TypeError("No matching overload for Code04_MaximumMatch1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_MaximumMatch1.MAXN = jcast('int', 152502)
Code04_MaximumMatch1.MAXM = jcast('int', 52502)
Code04_MaximumMatch1.MAXQ = jcast('int', 52502)
Code04_MaximumMatch1.n = jcast('int', 0)
Code04_MaximumMatch1.m = jcast('int', 0)
Code04_MaximumMatch1.z = jcast('int', 0)
Code04_MaximumMatch1.q = jcast('int', 0)
Code04_MaximumMatch1.a = jarray('int', [Code04_MaximumMatch1.MAXN])
Code04_MaximumMatch1.b = jarray('int', [Code04_MaximumMatch1.MAXM])
Code04_MaximumMatch1.query = jarray('int', [Code04_MaximumMatch1.MAXQ, 3])
Code04_MaximumMatch1.bi = jarray('int', [Code04_MaximumMatch1.MAXM])
Code04_MaximumMatch1.match = jarray('int', [jcast('int', (Code04_MaximumMatch1.MAXN << (2 & 31)))])
Code04_MaximumMatch1.resta = jarray('int', [jcast('int', (Code04_MaximumMatch1.MAXN << (2 & 31)))])
Code04_MaximumMatch1.overb = jarray('int', [jcast('int', (Code04_MaximumMatch1.MAXN << (2 & 31)))])
Code04_MaximumMatch1.ans = jarray('int', [Code04_MaximumMatch1.MAXQ])

if __name__ == '__main__':
    Code04_MaximumMatch1.main([])
