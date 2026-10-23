# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 传递闭包，Python版
# 一共n个点，给定有向图的邻接矩阵a，原图没有自环
# 如果 a[i][j] == 1，表示存在从i到j的有向边
# 如果 a[i][j] == 0，表示不存在从i到j的有向边
# 求有向图的传递闭包，输出关系矩阵b
# 如果i经过至少一条有向边可以到达j，那么b[i][j]为1，否则为0
# 1 <= n <= 100
# 测试链接 : https://www.luogu.com.cn/problem/B3611
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_TransitiveClosure1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'dp': 'dp'}
    MAXN = 0
    n = 0
    dp = None
    @staticmethod
    def floyd():
        bridge = jcast('int', 1)
        while (bridge <= Code02_TransitiveClosure1.n):
            i = jcast('int', 1)
            while (i <= Code02_TransitiveClosure1.n):
                if jcall(Code02_TransitiveClosure1.dp[i], 'get', bridge):
                    jcall(Code02_TransitiveClosure1.dp[i], 'or', Code02_TransitiveClosure1.dp[bridge])
                i = jcast('int', (i + 1))
            bridge = jcast('int', (bridge + 1))

    @staticmethod
    def main(args):
        in_ = Code02_TransitiveClosure1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_TransitiveClosure1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_TransitiveClosure1.n):
            jset(Code02_TransitiveClosure1.dp, i, jnew('BitSet', jcast('int', jadd(Code02_TransitiveClosure1.n, 1))))
            i = jcast('int', (i + 1))
        s = 0
        i = jcast('int', 1)
        while (i <= Code02_TransitiveClosure1.n):
            j = jcast('int', 1)
            while (j <= Code02_TransitiveClosure1.n):
                s = jcast('int', jcall(in_, 'nextInt'))
                jcall(Code02_TransitiveClosure1.dp[i], 'set', j, (s == 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        Code02_TransitiveClosure1.floyd()
        i = jcast('int', 1)
        while (i <= Code02_TransitiveClosure1.n):
            j = jcast('int', 1)
            while (j <= Code02_TransitiveClosure1.n):
                if jcall(Code02_TransitiveClosure1.dp[i], 'get', j):
                    jcall(out, 'print', '1 ')
                else:
                    jcall(out, 'print', '0 ')
                j = jcast('int', (j + 1))
            jcall(out, 'println')
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
            raise TypeError("No matching overload for Code02_TransitiveClosure1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_TransitiveClosure1.MAXN = jcast('int', 101)
Code02_TransitiveClosure1.n = jcast('int', 0)
Code02_TransitiveClosure1.dp = jarray('BitSet', [Code02_TransitiveClosure1.MAXN])

if __name__ == '__main__':
    Code02_TransitiveClosure1.main([])
