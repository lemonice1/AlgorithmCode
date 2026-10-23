# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 等差数列求和，Python版
# 一共有t组测试，每组测试遵循同样的设定
# 给定一个长度为n的数组arr，接下来有q条查询，查询格式如下
# 查询 s d k : arr[s]作为第1项、arr[s + 1d]作为第2项、arr[s + 2d]作为第3项...
# 每项的值 * 项的编号，一共k项都累加起来，打印累加和
# 1 <= n <= 10^5
# 1 <= q <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF1921F
# 测试链接 : https://codeforces.com/problemset/problem/1921/F
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_SumOfProgression2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 't': 't', 'n': 'n', 'q': 'q', 'blen': 'blen', 'arr': 'arr', 'f': 'f', 'g': 'g'}
    MAXN = 0
    MAXB = 0
    t = 0
    n = 0
    q = 0
    blen = 0
    arr = None
    f = None
    g = None
    @staticmethod
    def query(s, d, k):
        s = jcast('int', s)
        d = jcast('int', d)
        k = jcast('int', k)
        ans = jcast('long', 0)
        if (d <= Code03_SumOfProgression2.blen):
            ans = jcast('long', Code03_SumOfProgression2.g[d][s])
            if (jcast('int', jadd(s, jcast('int', (d * k)))) <= Code03_SumOfProgression2.n):
                ans = jcast('long', jcast('long', (jcast('long', (ans - Code03_SumOfProgression2.g[d][jcast('int', jadd(s, jcast('int', (d * k))))])) - jcast('long', (Code03_SumOfProgression2.f[d][jcast('int', jadd(s, jcast('int', (d * k))))] * k)))))
        else:
            i = jcast('int', 1)
            while (i <= k):
                ans = jcast('long', jcast('long', jadd(ans, jcast('long', (jcast('long', (1 * Code03_SumOfProgression2.arr[jcast('int', jadd(s, jcast('int', (jcast('int', (i - 1)) * d))))])) * i)))))
                i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def prepare():
        Code03_SumOfProgression2.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code03_SumOfProgression2.n)))
        d = jcast('int', 1)
        while (d <= Code03_SumOfProgression2.blen):
            i = jcast('int', Code03_SumOfProgression2.n)
            while (i >= 1):
                jset(Code03_SumOfProgression2.f[d], i, jcast('int', jadd(Code03_SumOfProgression2.arr[i], (0 if (jcast('int', jadd(i, d)) > Code03_SumOfProgression2.n) else Code03_SumOfProgression2.f[d][jcast('int', jadd(i, d))]))))
                i = jcast('int', (i - 1))
            d = jcast('int', (d + 1))
        d = jcast('int', 1)
        while (d <= Code03_SumOfProgression2.blen):
            i = jcast('int', Code03_SumOfProgression2.n)
            while (i >= 1):
                jset(Code03_SumOfProgression2.g[d], i, jcast('long', jadd(Code03_SumOfProgression2.f[d][i], (0 if (jcast('int', jadd(i, d)) > Code03_SumOfProgression2.n) else Code03_SumOfProgression2.g[d][jcast('int', jadd(i, d))]))))
                i = jcast('int', (i - 1))
            d = jcast('int', (d + 1))

    @staticmethod
    def main(args):
        in_ = Code03_SumOfProgression2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_SumOfProgression2.t = jcast('int', jcall(in_, 'nextInt'))
        c = jcast('int', 1)
        while (c <= Code03_SumOfProgression2.t):
            Code03_SumOfProgression2.n = jcast('int', jcall(in_, 'nextInt'))
            Code03_SumOfProgression2.q = jcast('int', jcall(in_, 'nextInt'))
            i = jcast('int', 1)
            while (i <= Code03_SumOfProgression2.n):
                jset(Code03_SumOfProgression2.arr, i, jcall(in_, 'nextInt'))
                i = jcast('int', (i + 1))
            Code03_SumOfProgression2.prepare()
            i = jcast('int', 1)
            s = 0
            d = 0
            k = 0
            while (i <= Code03_SumOfProgression2.q):
                s = jcast('int', jcall(in_, 'nextInt'))
                d = jcast('int', jcall(in_, 'nextInt'))
                k = jcast('int', jcall(in_, 'nextInt'))
                jcall(out, 'println', Code03_SumOfProgression2.query(s, d, k))
                i = jcast('int', (i + 1))
            c = jcast('int', (c + 1))
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
            return jcast('int', self.buffer[((_java_obj_1 := self), (_java_key_2 := 'ptr'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]])

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
            raise TypeError("No matching overload for Code03_SumOfProgression2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_SumOfProgression2.MAXN = jcast('int', 100001)
Code03_SumOfProgression2.MAXB = jcast('int', 401)
Code03_SumOfProgression2.t = jcast('int', 0)
Code03_SumOfProgression2.n = jcast('int', 0)
Code03_SumOfProgression2.q = jcast('int', 0)
Code03_SumOfProgression2.blen = jcast('int', 0)
Code03_SumOfProgression2.arr = jarray('int', [Code03_SumOfProgression2.MAXN])
Code03_SumOfProgression2.f = jarray('long', [Code03_SumOfProgression2.MAXB, Code03_SumOfProgression2.MAXN])
Code03_SumOfProgression2.g = jarray('long', [Code03_SumOfProgression2.MAXB, Code03_SumOfProgression2.MAXN])

if __name__ == '__main__':
    Code03_SumOfProgression2.main([])
