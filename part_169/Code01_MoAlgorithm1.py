# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 普通莫队入门题，Python版
# 给定一个长度为n的数组arr，一共有q条查询，格式如下
# 查询 l r : 打印arr[l..r]范围上有几种不同的数字
# 1 <= n <= 3 * 10^4
# 1 <= arr[i] <= 10^6
# 1 <= q <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/SP3267
# 测试链接 : https://www.spoj.com/problems/DQUERY/
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_MoAlgorithm1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'MAXQ': 'MAXQ', 'n': 'n', 'q': 'q', 'arr': 'arr', 'query': 'query', 'bi': 'bi', 'cnt': 'cnt', 'kind': 'kind', 'ans': 'ans'}
    MAXN = 0
    MAXV = 0
    MAXQ = 0
    n = 0
    q = 0
    arr = None
    # jobl, jobr, 问题id
    query = None
    bi = None
    cnt = None
    kind = 0
    ans = None
    # 普通莫队经典排序
    class QueryCmp1:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code01_MoAlgorithm1.bi[a[0]] != Code01_MoAlgorithm1.bi[b[0]]):
                return jcast('int', jcast('int', (Code01_MoAlgorithm1.bi[a[0]] - Code01_MoAlgorithm1.bi[b[0]])))
            return jcast('int', jcast('int', (a[1] - b[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    # 普通莫队奇偶排序
    class QueryCmp2:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code01_MoAlgorithm1.bi[a[0]] != Code01_MoAlgorithm1.bi[b[0]]):
                return jcast('int', jcast('int', (Code01_MoAlgorithm1.bi[a[0]] - Code01_MoAlgorithm1.bi[b[0]])))
            if (jcast('int', (Code01_MoAlgorithm1.bi[a[0]] & 1)) == 1):
                return jcast('int', jcast('int', (a[1] - b[1])))
            else:
                return jcast('int', jcast('int', (b[1] - a[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def del_(num):
        num = jcast('int', num)
        if (((_java_obj_1 := Code01_MoAlgorithm1.cnt), (_java_key_2 := num), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))))[3] == 0):
            Code01_MoAlgorithm1.kind = jcast('int', (Code01_MoAlgorithm1.kind - 1))

    @staticmethod
    def add(num):
        num = jcast('int', num)
        if (((_java_obj_4 := Code01_MoAlgorithm1.cnt), (_java_key_5 := num), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3] == 1):
            Code01_MoAlgorithm1.kind = jcast('int', (Code01_MoAlgorithm1.kind + 1))

    @staticmethod
    def prepare():
        blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code01_MoAlgorithm1.n)))
        i = jcast('int', 1)
        while (i <= Code01_MoAlgorithm1.n):
            Code01_MoAlgorithm1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        # Arrays.sort(query, 1, q + 1, new QueryCmp1());
        jstatic('Arrays', 'sort', Code01_MoAlgorithm1.query, 1, jcast('int', jadd(Code01_MoAlgorithm1.q, 1)), Code01_MoAlgorithm1.QueryCmp2())

    @staticmethod
    def compute():
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code01_MoAlgorithm1.q):
            jobl = jcast('int', Code01_MoAlgorithm1.query[i][0])
            jobr = jcast('int', Code01_MoAlgorithm1.query[i][1])
            while (winl > jobl):
                Code01_MoAlgorithm1.add(Code01_MoAlgorithm1.arr[(winl := jcast('int', (winl + (-1))))])
            while (winr < jobr):
                Code01_MoAlgorithm1.add(Code01_MoAlgorithm1.arr[(winr := jcast('int', (winr + (1))))])
            while (winl < jobl):
                Code01_MoAlgorithm1.del_(Code01_MoAlgorithm1.arr[((_java_old_7 := winl), (winl := jcast('int', (winl + (1)))), _java_old_7)[2]])
            while (winr > jobr):
                Code01_MoAlgorithm1.del_(Code01_MoAlgorithm1.arr[((_java_old_8 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_8)[2]])
            jset(Code01_MoAlgorithm1.ans, Code01_MoAlgorithm1.query[i][2], Code01_MoAlgorithm1.kind)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code01_MoAlgorithm1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_MoAlgorithm1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_MoAlgorithm1.n):
            jset(Code01_MoAlgorithm1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code01_MoAlgorithm1.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_MoAlgorithm1.q):
            jset(Code01_MoAlgorithm1.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code01_MoAlgorithm1.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code01_MoAlgorithm1.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code01_MoAlgorithm1.prepare()
        Code01_MoAlgorithm1.compute()
        i = jcast('int', 1)
        while (i <= Code01_MoAlgorithm1.q):
            jcall(out, 'println', Code01_MoAlgorithm1.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_9 := self), (_java_key_10 := 'ptr'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))), _java_old_11)[4]])

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
            raise TypeError("No matching overload for Code01_MoAlgorithm1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_MoAlgorithm1.MAXN = jcast('int', 30001)
Code01_MoAlgorithm1.MAXV = jcast('int', 1000001)
Code01_MoAlgorithm1.MAXQ = jcast('int', 200001)
Code01_MoAlgorithm1.n = jcast('int', 0)
Code01_MoAlgorithm1.q = jcast('int', 0)
Code01_MoAlgorithm1.arr = jarray('int', [Code01_MoAlgorithm1.MAXN])
Code01_MoAlgorithm1.query = jarray('int', [Code01_MoAlgorithm1.MAXQ, 3])
Code01_MoAlgorithm1.bi = jarray('int', [Code01_MoAlgorithm1.MAXN])
Code01_MoAlgorithm1.cnt = jarray('int', [Code01_MoAlgorithm1.MAXV])
Code01_MoAlgorithm1.kind = jcast('int', 0)
Code01_MoAlgorithm1.ans = jarray('int', [Code01_MoAlgorithm1.MAXQ])

if __name__ == '__main__':
    Code01_MoAlgorithm1.main([])
