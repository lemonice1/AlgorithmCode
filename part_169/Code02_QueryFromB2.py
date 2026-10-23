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

# 小B的询问，Python版
# 给定一个长度为n的数组arr，所有数字在[1..k]范围上
# 定义f(i) = i这种数的出现次数的平方
# 一共有m条查询，格式如下
# 查询 l r : arr[l..r]范围上，打印 f(1) + f(2) + .. + f(k) 的值
# 1 <= n、m、k <= 5 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P2709
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_QueryFromB2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'k': 'k', 'arr': 'arr', 'query': 'query', 'bi': 'bi', 'cnt': 'cnt', 'sum': 'sum', 'ans': 'ans'}
    MAXN = 0
    n = 0
    m = 0
    k = 0
    arr = None
    # jobl, jobr, 问题id
    query = None
    bi = None
    cnt = None
    sum = 0
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code02_QueryFromB2.bi[a[0]] != Code02_QueryFromB2.bi[b[0]]):
                return jcast('int', jcast('int', (Code02_QueryFromB2.bi[a[0]] - Code02_QueryFromB2.bi[b[0]])))
            return jcast('int', jcast('int', (a[1] - b[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def del_(num):
        num = jcast('int', num)
        Code02_QueryFromB2.sum = jcast('int', jcast('int', (Code02_QueryFromB2.sum - jcast('int', (Code02_QueryFromB2.cnt[num] * Code02_QueryFromB2.cnt[num])))))
        Code02_QueryFromB2.cnt[num] = jcast('int', (Code02_QueryFromB2.cnt[num] - 1))
        Code02_QueryFromB2.sum = jcast('int', jcast('int', jadd(Code02_QueryFromB2.sum, jcast('int', (Code02_QueryFromB2.cnt[num] * Code02_QueryFromB2.cnt[num])))))

    @staticmethod
    def add(num):
        num = jcast('int', num)
        Code02_QueryFromB2.sum = jcast('int', jcast('int', (Code02_QueryFromB2.sum - jcast('int', (Code02_QueryFromB2.cnt[num] * Code02_QueryFromB2.cnt[num])))))
        Code02_QueryFromB2.cnt[num] = jcast('int', (Code02_QueryFromB2.cnt[num] + 1))
        Code02_QueryFromB2.sum = jcast('int', jcast('int', jadd(Code02_QueryFromB2.sum, jcast('int', (Code02_QueryFromB2.cnt[num] * Code02_QueryFromB2.cnt[num])))))

    @staticmethod
    def prepare():
        blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code02_QueryFromB2.n)))
        i = jcast('int', 1)
        while (i <= Code02_QueryFromB2.n):
            Code02_QueryFromB2.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_QueryFromB2.query, 1, jcast('int', jadd(Code02_QueryFromB2.m, 1)), Code02_QueryFromB2.QueryCmp())

    @staticmethod
    def compute():
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code02_QueryFromB2.m):
            jobl = jcast('int', Code02_QueryFromB2.query[i][0])
            jobr = jcast('int', Code02_QueryFromB2.query[i][1])
            while (winl > jobl):
                Code02_QueryFromB2.add(Code02_QueryFromB2.arr[(winl := jcast('int', (winl + (-1))))])
            while (winr < jobr):
                Code02_QueryFromB2.add(Code02_QueryFromB2.arr[(winr := jcast('int', (winr + (1))))])
            while (winl < jobl):
                Code02_QueryFromB2.del_(Code02_QueryFromB2.arr[((_java_old_1 := winl), (winl := jcast('int', (winl + (1)))), _java_old_1)[2]])
            while (winr > jobr):
                Code02_QueryFromB2.del_(Code02_QueryFromB2.arr[((_java_old_2 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_2)[2]])
            jset(Code02_QueryFromB2.ans, Code02_QueryFromB2.query[i][2], Code02_QueryFromB2.sum)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code02_QueryFromB2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_QueryFromB2.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_QueryFromB2.m = jcast('int', jcall(in_, 'nextInt'))
        Code02_QueryFromB2.k = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_QueryFromB2.n):
            jset(Code02_QueryFromB2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_QueryFromB2.m):
            jset(Code02_QueryFromB2.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code02_QueryFromB2.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code02_QueryFromB2.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code02_QueryFromB2.prepare()
        Code02_QueryFromB2.compute()
        i = jcast('int', 1)
        while (i <= Code02_QueryFromB2.m):
            jcall(out, 'println', Code02_QueryFromB2.ans[i])
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
            raise TypeError("No matching overload for Code02_QueryFromB2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_QueryFromB2.MAXN = jcast('int', 50001)
Code02_QueryFromB2.n = jcast('int', 0)
Code02_QueryFromB2.m = jcast('int', 0)
Code02_QueryFromB2.k = jcast('int', 0)
Code02_QueryFromB2.arr = jarray('int', [Code02_QueryFromB2.MAXN])
Code02_QueryFromB2.query = jarray('int', [Code02_QueryFromB2.MAXN, 3])
Code02_QueryFromB2.bi = jarray('int', [Code02_QueryFromB2.MAXN])
Code02_QueryFromB2.cnt = jarray('int', [Code02_QueryFromB2.MAXN])
Code02_QueryFromB2.sum = jcast('int', 0)
Code02_QueryFromB2.ans = jarray('int', [Code02_QueryFromB2.MAXN])

if __name__ == '__main__':
    Code02_QueryFromB2.main([])
