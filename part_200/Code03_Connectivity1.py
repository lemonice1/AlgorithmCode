# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 连通数，Python版
# 一共n个点，给定有向图的邻接矩阵a
# 如果 a[i][j] == 1，表示存在从i到j的有向边
# 如果 a[i][j] == 0，表示不存在从i到j的有向边
# 如果i可以直接或间接到达j，则有序点对(i, j)计入答案
# 每个点都认为可以到达自己，因此(i, i)也计入答案
# 求所有可达有序点对的数量，打印这个数量
# 1 <= n <= 2000
# 测试链接 : https://www.luogu.com.cn/problem/P4306
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Connectivity1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'dp': 'dp'}
    MAXN = 0
    n = 0
    dp = None
    @staticmethod
    def floyd():
        bridge = jcast('int', 1)
        while (bridge <= Code03_Connectivity1.n):
            i = jcast('int', 1)
            while (i <= Code03_Connectivity1.n):
                if jcall(Code03_Connectivity1.dp[i], 'get', bridge):
                    jcall(Code03_Connectivity1.dp[i], 'or', Code03_Connectivity1.dp[bridge])
                i = jcast('int', (i + 1))
            bridge = jcast('int', (bridge + 1))

    @staticmethod
    def main(args):
        in_ = Code03_Connectivity1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_Connectivity1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_Connectivity1.n):
            jset(Code03_Connectivity1.dp, i, jnew('BitSet', jcast('int', jadd(Code03_Connectivity1.n, 1))))
            i = jcast('int', (i + 1))
        s = jchar(0)
        i = jcast('int', 1)
        while (i <= Code03_Connectivity1.n):
            j = jcast('int', 1)
            while (j <= Code03_Connectivity1.n):
                s = jcast('char', jcall(in_, 'nextChar'))
                jcall(Code03_Connectivity1.dp[i], 'set', j, (s == jchar('1')))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        # 主动设置对角线
        i = jcast('int', 1)
        while (i <= Code03_Connectivity1.n):
            jcall(Code03_Connectivity1.dp[i], 'set', i)
            i = jcast('int', (i + 1))
        Code03_Connectivity1.floyd()
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code03_Connectivity1.n):
            ans = jcast('int', jadd(ans, jcall(Code03_Connectivity1.dp[i], 'cardinality')))
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

        def nextChar(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            return jcast('char', jcast('char', c))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code03_Connectivity1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Connectivity1.MAXN = jcast('int', 2001)
Code03_Connectivity1.n = jcast('int', 0)
Code03_Connectivity1.dp = jarray('BitSet', [Code03_Connectivity1.MAXN])

if __name__ == '__main__':
    Code03_Connectivity1.main([])
