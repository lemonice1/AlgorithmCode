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

# 有向图与查询，Python版
# 一共n个点，编号1~n，给定m条有向边，没有重边和自环
# 每条边的格式 a b，表示存在从a到b的有向边
# 定义有向路径的代价，路径上所有点的编号最大值，包括起点和终点
# 一共q条查询，每条查询的格式 s t，保证 s != t
# 求从s到t的所有有向路径中，最小的路径代价，不存在路径输出-1
# 2 <= n <= 2000
# 0 <= m <= n * (n - 1)
# 1 <= q <= 10000
# 测试链接 : https://www.luogu.com.cn/problem/AT_abc287_h
# 测试链接 : https://atcoder.jp/contests/abc287/tasks/abc287_h
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_DirectedGraphAndQuery1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXQ': 'MAXQ', 'n': 'n', 'm': 'm', 'q': 'q', 's': 's', 't': 't', 'dp': 'dp', 'ans': 'ans'}
    MAXN = 0
    MAXQ = 0
    n = 0
    m = 0
    q = 0
    s = None
    t = None
    dp = None
    ans = None
    @staticmethod
    def floyd():
        i = jcast('int', 1)
        while (i <= Code06_DirectedGraphAndQuery1.q):
            Code06_DirectedGraphAndQuery1.ans[i] = jcast('int', jcast('int', (-1)))
            i = jcast('int', (i + 1))
        bridge = jcast('int', 1)
        while (bridge <= Code06_DirectedGraphAndQuery1.n):
            i = jcast('int', 1)
            while (i <= Code06_DirectedGraphAndQuery1.n):
                if jcall(Code06_DirectedGraphAndQuery1.dp[i], 'get', bridge):
                    jcall(Code06_DirectedGraphAndQuery1.dp[i], 'or', Code06_DirectedGraphAndQuery1.dp[bridge])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code06_DirectedGraphAndQuery1.q):
                if ((Code06_DirectedGraphAndQuery1.ans[i] == jcast('int', (-1))) and jcall(Code06_DirectedGraphAndQuery1.dp[Code06_DirectedGraphAndQuery1.s[i]], 'get', Code06_DirectedGraphAndQuery1.t[i])):
                    jset(Code06_DirectedGraphAndQuery1.ans, i, jstatic('Math', 'max', bridge, jstatic('Math', 'max', Code06_DirectedGraphAndQuery1.s[i], Code06_DirectedGraphAndQuery1.t[i])))
                i = jcast('int', (i + 1))
            bridge = jcast('int', (bridge + 1))

    @staticmethod
    def main(args):
        in_ = Code06_DirectedGraphAndQuery1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_DirectedGraphAndQuery1.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_DirectedGraphAndQuery1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_DirectedGraphAndQuery1.n):
            jset(Code06_DirectedGraphAndQuery1.dp, i, jnew('BitSet', jcast('int', jadd(Code06_DirectedGraphAndQuery1.n, 1))))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        a = 0
        b = 0
        while (i <= Code06_DirectedGraphAndQuery1.m):
            a = jcast('int', jcall(in_, 'nextInt'))
            b = jcast('int', jcall(in_, 'nextInt'))
            jcall(Code06_DirectedGraphAndQuery1.dp[a], 'set', b)
            i = jcast('int', (i + 1))
        Code06_DirectedGraphAndQuery1.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_DirectedGraphAndQuery1.q):
            jset(Code06_DirectedGraphAndQuery1.s, i, jcall(in_, 'nextInt'))
            jset(Code06_DirectedGraphAndQuery1.t, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code06_DirectedGraphAndQuery1.floyd()
        i = jcast('int', 1)
        while (i <= Code06_DirectedGraphAndQuery1.q):
            jcall(out, 'println', Code06_DirectedGraphAndQuery1.ans[i])
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
            raise TypeError("No matching overload for Code06_DirectedGraphAndQuery1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_DirectedGraphAndQuery1.MAXN = jcast('int', 2001)
Code06_DirectedGraphAndQuery1.MAXQ = jcast('int', 10001)
Code06_DirectedGraphAndQuery1.n = jcast('int', 0)
Code06_DirectedGraphAndQuery1.m = jcast('int', 0)
Code06_DirectedGraphAndQuery1.q = jcast('int', 0)
Code06_DirectedGraphAndQuery1.s = jarray('int', [Code06_DirectedGraphAndQuery1.MAXQ])
Code06_DirectedGraphAndQuery1.t = jarray('int', [Code06_DirectedGraphAndQuery1.MAXQ])
Code06_DirectedGraphAndQuery1.dp = jarray('BitSet', [Code06_DirectedGraphAndQuery1.MAXN])
Code06_DirectedGraphAndQuery1.ans = jarray('int', [Code06_DirectedGraphAndQuery1.MAXQ])

if __name__ == '__main__':
    Code06_DirectedGraphAndQuery1.main([])
