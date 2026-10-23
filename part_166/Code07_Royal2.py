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

# 王室联邦，Python版
# 一共有n个城市，编号1~n，给定n-1条边，所有城市连成一棵树
# 给定数值b，请把树划分成若干个省，划分要求如下
# 每个省至少要有b个城市，最多有3 * b个城市，每个省必须有一个省会
# 省会可在省内也可在省外，一个城市可以是多个省的省会
# 一个省里，任何城市到达省会的路径上，除了省会之外的其他城市，必须都在省内
# 根据要求完成一种有效划分即可，先打印划分了多少个省，假设数量为k
# 然后打印n个数字，范围[1, k]，表示每个城市被划分给了哪个省
# 最后打印k个数字，表示每个省会的城市编号
# 1 <= n、b <= 10^3
# 测试链接 : https://www.luogu.com.cn/problem/P2325
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_Royal2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'b': 'b', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'capital': 'capital', 'belong': 'belong', 'cntb': 'cntb', 'stack': 'stack', 'siz': 'siz'}
    MAXN = 0
    n = 0
    b = 0
    head = None
    next = None
    to = None
    cntg = 0
    capital = None
    belong = None
    cntb = 0
    stack = None
    siz = 0
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_Royal2.next, ((_java_obj_1 := Code07_Royal2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_Royal2.head[u])
        Code07_Royal2.to[Code07_Royal2.cntg] = jcast('int', v)
        Code07_Royal2.head[u] = jcast('int', Code07_Royal2.cntg)

    @staticmethod
    def dfs(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        x = jcast('int', Code07_Royal2.siz)
        e = jcast('int', Code07_Royal2.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code07_Royal2.to[e])
            if (v != f):
                Code07_Royal2.dfs(v, u)
                if (jcast('int', (Code07_Royal2.siz - x)) >= Code07_Royal2.b):
                    jset(Code07_Royal2.capital, ((_java_obj_4 := Code07_Royal2), (_java_key_5 := 'cntb'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], u)
                    while (Code07_Royal2.siz != x):
                        jset(Code07_Royal2.belong, Code07_Royal2.stack[((_java_obj_7 := Code07_Royal2), (_java_key_8 := 'siz'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]], Code07_Royal2.cntb)
            e = jcast('int', Code07_Royal2.next[e])
        jset(Code07_Royal2.stack, ((_java_obj_10 := Code07_Royal2), (_java_key_11 := 'siz'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], u)

    @staticmethod
    def main(args):
        in_ = Code07_Royal2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_Royal2.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_Royal2.b = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code07_Royal2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code07_Royal2.addEdge(u, v)
            Code07_Royal2.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code07_Royal2.dfs(1, 0)
        if (Code07_Royal2.cntb == 0):
            jset(Code07_Royal2.capital, ((_java_obj_13 := Code07_Royal2), (_java_key_14 := 'cntb'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], 1)
        while (Code07_Royal2.siz > 0):
            jset(Code07_Royal2.belong, Code07_Royal2.stack[((_java_obj_16 := Code07_Royal2), (_java_key_17 := 'siz'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (-1)))), _java_old_18)[4]], Code07_Royal2.cntb)
        jcall(out, 'println', Code07_Royal2.cntb)
        i = jcast('int', 1)
        while (i <= Code07_Royal2.n):
            jcall(out, 'print', jadd(Code07_Royal2.belong[i], ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println')
        i = jcast('int', 1)
        while (i <= Code07_Royal2.cntb):
            jcall(out, 'print', jadd(Code07_Royal2.capital[i], ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println')
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
            return jcast('int', self.buffer[((_java_obj_19 := self), (_java_key_20 := 'ptr'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))), _java_old_21)[4]])

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
            self.buffer = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code07_Royal2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_Royal2.MAXN = jcast('int', 1001)
Code07_Royal2.n = jcast('int', 0)
Code07_Royal2.b = jcast('int', 0)
Code07_Royal2.head = jarray('int', [Code07_Royal2.MAXN])
Code07_Royal2.next = jarray('int', [jcast('int', (Code07_Royal2.MAXN << (1 & 31)))])
Code07_Royal2.to = jarray('int', [jcast('int', (Code07_Royal2.MAXN << (1 & 31)))])
Code07_Royal2.cntg = jcast('int', 0)
Code07_Royal2.capital = jarray('int', [Code07_Royal2.MAXN])
Code07_Royal2.belong = jarray('int', [Code07_Royal2.MAXN])
Code07_Royal2.cntb = jcast('int', 0)
Code07_Royal2.stack = jarray('int', [Code07_Royal2.MAXN])
Code07_Royal2.siz = jcast('int', 0)

if __name__ == '__main__':
    Code07_Royal2.main([])
