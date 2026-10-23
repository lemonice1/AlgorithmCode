# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 小Z的袜子，Python版
# 给定一个长度为n的数组arr，一共有m条查询，格式如下
# 查询 l r : arr[l..r]范围上，随机选不同位置的两个数，打印数值相同的概率
# 概率用分数的形式表达，并且约分到最简的形式
# 1 <= n、m、arr[i] <= 5 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P1494
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 对应实现可参考 Code03_SockFromZ2.py
# 两个版本保留相同的算法逻辑
class Code03_SockFromZ1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'arr': 'arr', 'query': 'query', 'bi': 'bi', 'cnt': 'cnt', 'sum': 'sum', 'ans1': 'ans1', 'ans2': 'ans2'}
    MAXN = 0
    n = 0
    m = 0
    arr = None
    query = None
    bi = None
    cnt = None
    sum = 0
    # 每个查询的分子的值
    ans1 = None
    # 每个查询的分母的值
    ans2 = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code03_SockFromZ1.bi[a[0]] != Code03_SockFromZ1.bi[b[0]]):
                return jcast('int', jcast('int', (Code03_SockFromZ1.bi[a[0]] - Code03_SockFromZ1.bi[b[0]])))
            return jcast('int', jcast('int', (a[1] - b[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def gcd(a, b):
        a = jcast('long', a)
        b = jcast('long', b)
        return jcast('long', (a if (b == 0) else Code03_SockFromZ1.gcd(b, jcast('long', jmod(a, b)))))

    @staticmethod
    def del_(num):
        num = jcast('int', num)
        Code03_SockFromZ1.sum = jcast('long', jcast('long', (Code03_SockFromZ1.sum - jcast('int', (Code03_SockFromZ1.cnt[num] * Code03_SockFromZ1.cnt[num])))))
        Code03_SockFromZ1.cnt[num] = jcast('int', (Code03_SockFromZ1.cnt[num] - 1))
        Code03_SockFromZ1.sum = jcast('long', jcast('long', jadd(Code03_SockFromZ1.sum, jcast('int', (Code03_SockFromZ1.cnt[num] * Code03_SockFromZ1.cnt[num])))))

    @staticmethod
    def add(num):
        num = jcast('int', num)
        Code03_SockFromZ1.sum = jcast('long', jcast('long', (Code03_SockFromZ1.sum - jcast('int', (Code03_SockFromZ1.cnt[num] * Code03_SockFromZ1.cnt[num])))))
        Code03_SockFromZ1.cnt[num] = jcast('int', (Code03_SockFromZ1.cnt[num] + 1))
        Code03_SockFromZ1.sum = jcast('long', jcast('long', jadd(Code03_SockFromZ1.sum, jcast('int', (Code03_SockFromZ1.cnt[num] * Code03_SockFromZ1.cnt[num])))))

    @staticmethod
    def prepare():
        blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code03_SockFromZ1.n)))
        i = jcast('int', 1)
        while (i <= Code03_SockFromZ1.n):
            Code03_SockFromZ1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code03_SockFromZ1.query, 1, jcast('int', jadd(Code03_SockFromZ1.m, 1)), Code03_SockFromZ1.QueryCmp())

    @staticmethod
    def compute():
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code03_SockFromZ1.m):
            jobl = jcast('int', Code03_SockFromZ1.query[i][0])
            jobr = jcast('int', Code03_SockFromZ1.query[i][1])
            id = jcast('int', Code03_SockFromZ1.query[i][2])
            while (winl > jobl):
                Code03_SockFromZ1.add(Code03_SockFromZ1.arr[(winl := jcast('int', (winl + (-1))))])
            while (winr < jobr):
                Code03_SockFromZ1.add(Code03_SockFromZ1.arr[(winr := jcast('int', (winr + (1))))])
            while (winl < jobl):
                Code03_SockFromZ1.del_(Code03_SockFromZ1.arr[((_java_old_1 := winl), (winl := jcast('int', (winl + (1)))), _java_old_1)[2]])
            while (winr > jobr):
                Code03_SockFromZ1.del_(Code03_SockFromZ1.arr[((_java_old_2 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_2)[2]])
            if (jobl == jobr):
                Code03_SockFromZ1.ans1[id] = jcast('long', 0)
                Code03_SockFromZ1.ans2[id] = jcast('long', 1)
            else:
                Code03_SockFromZ1.ans1[id] = jcast('long', jcast('long', (Code03_SockFromZ1.sum - jcast('int', jadd(jcast('int', (jobr - jobl)), 1)))))
                Code03_SockFromZ1.ans2[id] = jcast('long', jcast('long', (jcast('long', (1 * jcast('int', jadd(jcast('int', (jobr - jobl)), 1)))) * jcast('int', (jobr - jobl)))))
                g = jcast('long', Code03_SockFromZ1.gcd(Code03_SockFromZ1.ans1[id], Code03_SockFromZ1.ans2[id]))
                Code03_SockFromZ1.ans1[id] = jcast('long', jcast('long', jdiv(Code03_SockFromZ1.ans1[id], g)))
                Code03_SockFromZ1.ans2[id] = jcast('long', jcast('long', jdiv(Code03_SockFromZ1.ans2[id], g)))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code03_SockFromZ1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_SockFromZ1.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_SockFromZ1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_SockFromZ1.n):
            jset(Code03_SockFromZ1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_SockFromZ1.m):
            jset(Code03_SockFromZ1.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code03_SockFromZ1.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code03_SockFromZ1.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code03_SockFromZ1.prepare()
        Code03_SockFromZ1.compute()
        i = jcast('int', 1)
        while (i <= Code03_SockFromZ1.m):
            jcall(out, 'println', jadd(jadd(Code03_SockFromZ1.ans1[i], '/'), Code03_SockFromZ1.ans2[i]))
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
            raise TypeError("No matching overload for Code03_SockFromZ1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_SockFromZ1.MAXN = jcast('int', 50001)
Code03_SockFromZ1.n = jcast('int', 0)
Code03_SockFromZ1.m = jcast('int', 0)
Code03_SockFromZ1.arr = jarray('int', [Code03_SockFromZ1.MAXN])
Code03_SockFromZ1.query = jarray('int', [Code03_SockFromZ1.MAXN, 3])
Code03_SockFromZ1.bi = jarray('int', [Code03_SockFromZ1.MAXN])
Code03_SockFromZ1.cnt = jarray('int', [Code03_SockFromZ1.MAXN])
Code03_SockFromZ1.sum = jcast('long', 0)
Code03_SockFromZ1.ans1 = jarray('long', [Code03_SockFromZ1.MAXN])
Code03_SockFromZ1.ans2 = jarray('long', [Code03_SockFromZ1.MAXN])

if __name__ == '__main__':
    Code03_SockFromZ1.main([])
