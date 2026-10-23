# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 异或序列，Python版
# 给定一个长度为n的数组arr，给定一个数字k，一共有m条查询，格式如下
# 查询 l r : arr[l..r]范围上，有多少子数组的异或和为k，打印其数量
# 0 <= n、m、k、arr[i] <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4462
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_XorSequence1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXS': 'MAXS', 'n': 'n', 'm': 'm', 'k': 'k', 'arr': 'arr', 'query': 'query', 'bi': 'bi', 'pre': 'pre', 'cnt': 'cnt', 'num': 'num', 'ans': 'ans'}
    MAXN = 0
    MAXS = 0
    n = 0
    m = 0
    k = 0
    arr = None
    query = None
    bi = None
    # pre[i] == x，表示前i个数字的前缀异或和为x
    pre = None
    # cnt[x] = a，表示窗口内，前缀异或和x，一共有a个
    cnt = None
    # num表示窗口内，异或和为k的子数组数量
    num = 0
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code05_XorSequence1.bi[a[0]] != Code05_XorSequence1.bi[b[0]]):
                return jcast('int', jcast('int', (Code05_XorSequence1.bi[a[0]] - Code05_XorSequence1.bi[b[0]])))
            return jcast('int', jcast('int', (a[1] - b[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    # 前缀异或和x要删除一次
    @staticmethod
    def del_(x):
        x = jcast('int', x)
        if (Code05_XorSequence1.k != 0):
            Code05_XorSequence1.num = jcast('long', jcast('long', (Code05_XorSequence1.num - jcast('long', (Code05_XorSequence1.cnt[x] * Code05_XorSequence1.cnt[jcast('int', (x ^ Code05_XorSequence1.k))])))))
        else:
            Code05_XorSequence1.num = jcast('long', jcast('long', (Code05_XorSequence1.num - jcast('long', (jcast('long', (Code05_XorSequence1.cnt[x] * jcast('long', (Code05_XorSequence1.cnt[x] - 1)))) >> (1 & 63))))))
        Code05_XorSequence1.cnt[x] = jcast('long', (Code05_XorSequence1.cnt[x] - 1))
        if (Code05_XorSequence1.k != 0):
            Code05_XorSequence1.num = jcast('long', jcast('long', jadd(Code05_XorSequence1.num, jcast('long', (Code05_XorSequence1.cnt[x] * Code05_XorSequence1.cnt[jcast('int', (x ^ Code05_XorSequence1.k))])))))
        else:
            Code05_XorSequence1.num = jcast('long', jcast('long', jadd(Code05_XorSequence1.num, jcast('long', (jcast('long', (Code05_XorSequence1.cnt[x] * jcast('long', (Code05_XorSequence1.cnt[x] - 1)))) >> (1 & 63))))))

    # 前缀异或和x要增加一次
    @staticmethod
    def add(x):
        x = jcast('int', x)
        if (Code05_XorSequence1.k != 0):
            Code05_XorSequence1.num = jcast('long', jcast('long', (Code05_XorSequence1.num - jcast('long', (Code05_XorSequence1.cnt[x] * Code05_XorSequence1.cnt[jcast('int', (x ^ Code05_XorSequence1.k))])))))
        else:
            Code05_XorSequence1.num = jcast('long', jcast('long', (Code05_XorSequence1.num - jcast('long', (jcast('long', (Code05_XorSequence1.cnt[x] * jcast('long', (Code05_XorSequence1.cnt[x] - 1)))) >> (1 & 63))))))
        Code05_XorSequence1.cnt[x] = jcast('long', (Code05_XorSequence1.cnt[x] + 1))
        if (Code05_XorSequence1.k != 0):
            Code05_XorSequence1.num = jcast('long', jcast('long', jadd(Code05_XorSequence1.num, jcast('long', (Code05_XorSequence1.cnt[x] * Code05_XorSequence1.cnt[jcast('int', (x ^ Code05_XorSequence1.k))])))))
        else:
            Code05_XorSequence1.num = jcast('long', jcast('long', jadd(Code05_XorSequence1.num, jcast('long', (jcast('long', (Code05_XorSequence1.cnt[x] * jcast('long', (Code05_XorSequence1.cnt[x] - 1)))) >> (1 & 63))))))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code05_XorSequence1.n):
            Code05_XorSequence1.pre[i] = jcast('int', jcast('int', (Code05_XorSequence1.pre[jcast('int', (i - 1))] ^ Code05_XorSequence1.arr[i])))
            i = jcast('int', (i + 1))
        blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code05_XorSequence1.n)))
        i = jcast('int', 1)
        while (i <= Code05_XorSequence1.n):
            Code05_XorSequence1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_XorSequence1.query, 1, jcast('int', jadd(Code05_XorSequence1.m, 1)), Code05_XorSequence1.QueryCmp())

    @staticmethod
    def compute():
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code05_XorSequence1.m):
            # 任务范围[jobl, jobr]，但是前缀可能性会多一种
            # 所以左边界-1
            jobl = jcast('int', jcast('int', (Code05_XorSequence1.query[i][0] - 1)))
            jobr = jcast('int', Code05_XorSequence1.query[i][1])
            while (winl > jobl):
                Code05_XorSequence1.add(Code05_XorSequence1.pre[(winl := jcast('int', (winl + (-1))))])
            while (winr < jobr):
                Code05_XorSequence1.add(Code05_XorSequence1.pre[(winr := jcast('int', (winr + (1))))])
            while (winl < jobl):
                Code05_XorSequence1.del_(Code05_XorSequence1.pre[((_java_old_1 := winl), (winl := jcast('int', (winl + (1)))), _java_old_1)[2]])
            while (winr > jobr):
                Code05_XorSequence1.del_(Code05_XorSequence1.pre[((_java_old_2 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_2)[2]])
            jset(Code05_XorSequence1.ans, Code05_XorSequence1.query[i][2], Code05_XorSequence1.num)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code05_XorSequence1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_XorSequence1.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_XorSequence1.m = jcast('int', jcall(in_, 'nextInt'))
        Code05_XorSequence1.k = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_XorSequence1.n):
            jset(Code05_XorSequence1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_XorSequence1.m):
            jset(Code05_XorSequence1.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code05_XorSequence1.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code05_XorSequence1.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code05_XorSequence1.prepare()
        Code05_XorSequence1.compute()
        i = jcast('int', 1)
        while (i <= Code05_XorSequence1.m):
            jcall(out, 'println', Code05_XorSequence1.ans[i])
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
            raise TypeError("No matching overload for Code05_XorSequence1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_XorSequence1.MAXN = jcast('int', 100001)
Code05_XorSequence1.MAXS = jcast('int', jcast('int', (1 << (20 & 31))))
Code05_XorSequence1.n = jcast('int', 0)
Code05_XorSequence1.m = jcast('int', 0)
Code05_XorSequence1.k = jcast('int', 0)
Code05_XorSequence1.arr = jarray('int', [Code05_XorSequence1.MAXN])
Code05_XorSequence1.query = jarray('int', [Code05_XorSequence1.MAXN, 3])
Code05_XorSequence1.bi = jarray('int', [Code05_XorSequence1.MAXN])
Code05_XorSequence1.pre = jarray('int', [Code05_XorSequence1.MAXN])
Code05_XorSequence1.cnt = jarray('long', [Code05_XorSequence1.MAXS])
Code05_XorSequence1.num = jcast('long', 0)
Code05_XorSequence1.ans = jarray('long', [Code05_XorSequence1.MAXN])

if __name__ == '__main__':
    Code05_XorSequence1.main([])
