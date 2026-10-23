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

# 数组查询，Python版
# 给定一个长度为n的数组arr，接下来有q条查询，查询格式如下
# 查询 p k : p 不断变成 p + arr[p] + k，直到 p > n 停止，打印操作次数
# 1 <= n、q <= 10 ^ 5
# 1 <= arr[i] <= n
# 测试链接 : https://www.luogu.com.cn/problem/CF797E
# 测试链接 : https://codeforces.com/problemset/problem/797/E
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_ArrayQueries1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'q': 'q', 'blen': 'blen', 'arr': 'arr', 'dp': 'dp'}
    MAXN = 0
    MAXB = 0
    n = 0
    q = 0
    blen = 0
    arr = None
    dp = None
    @staticmethod
    def query(p, k):
        p = jcast('int', p)
        k = jcast('int', k)
        if (k <= Code02_ArrayQueries1.blen):
            return jcast('int', Code02_ArrayQueries1.dp[p][k])
        ans = jcast('int', 0)
        while (p <= Code02_ArrayQueries1.n):
            ans = jcast('int', (ans + 1))
            p = jcast('int', jcast('int', jadd(p, jcast('int', jadd(Code02_ArrayQueries1.arr[p], k)))))
        return jcast('int', ans)

    @staticmethod
    def prepare():
        Code02_ArrayQueries1.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code02_ArrayQueries1.n)))
        p = jcast('int', Code02_ArrayQueries1.n)
        while (p >= 1):
            k = jcast('int', 1)
            while (k <= Code02_ArrayQueries1.blen):
                jset(Code02_ArrayQueries1.dp[p], k, jcast('int', jadd(1, (0 if (jcast('int', jadd(jcast('int', jadd(p, Code02_ArrayQueries1.arr[p])), k)) > Code02_ArrayQueries1.n) else Code02_ArrayQueries1.dp[jcast('int', jadd(jcast('int', jadd(p, Code02_ArrayQueries1.arr[p])), k))][k]))))
                k = jcast('int', (k + 1))
            p = jcast('int', (p - 1))

    @staticmethod
    def main(args):
        in_ = Code02_ArrayQueries1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_ArrayQueries1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_ArrayQueries1.n):
            jset(Code02_ArrayQueries1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code02_ArrayQueries1.prepare()
        Code02_ArrayQueries1.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        p = 0
        k = 0
        while (i <= Code02_ArrayQueries1.q):
            p = jcast('int', jcall(in_, 'nextInt'))
            k = jcast('int', jcall(in_, 'nextInt'))
            jcall(out, 'println', Code02_ArrayQueries1.query(p, k))
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
            raise TypeError("No matching overload for Code02_ArrayQueries1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_ArrayQueries1.MAXN = jcast('int', 100001)
Code02_ArrayQueries1.MAXB = jcast('int', 401)
Code02_ArrayQueries1.n = jcast('int', 0)
Code02_ArrayQueries1.q = jcast('int', 0)
Code02_ArrayQueries1.blen = jcast('int', 0)
Code02_ArrayQueries1.arr = jarray('int', [Code02_ArrayQueries1.MAXN])
Code02_ArrayQueries1.dp = jarray('int', [Code02_ArrayQueries1.MAXN, Code02_ArrayQueries1.MAXB])

if __name__ == '__main__':
    Code02_ArrayQueries1.main([])
