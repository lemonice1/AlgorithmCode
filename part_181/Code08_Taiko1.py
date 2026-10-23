# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 太鼓达人，Python版
# 给定一个正数n，所有长度为n的二进制状态一共有(2^n)个
# 构造一个字符串，字符串可以循环使用，其中的连续子串包含所有二进制状态
# 求出字符串的最小长度值，并且给出字典序最小的方案
# 比如n=3，字符串最小长度值为8，字典序最小的方案为00010111
# 注意到 000、001、010、101、011、111、110、100 都已包含
# 注意到 最后两个二进制状态 是字符串循环使用构造出来的
# 1 <= n <= 11
# 本题可以推广到k进制，代码就是按照推广来实现的
# 测试链接 : https://www.luogu.com.cn/problem/P10950
# 测试链接 : https://loj.ac/p/10110
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code08_Taiko1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'k': 'k', 'm': 'm', 'cur': 'cur', 'path': 'path', 'cntp': 'cntp'}
    MAXN = 0
    n = 0
    k = 0
    m = 0
    cur = None
    path = None
    cntp = 0
    @staticmethod
    def prepare(len, num):
        len = jcast('int', len)
        num = jcast('int', num)
        Code08_Taiko1.n = jcast('int', len)
        Code08_Taiko1.k = jcast('int', num)
        Code08_Taiko1.m = jcast('int', 1)
        i = jcast('int', 1)
        while (i <= jcast('int', (Code08_Taiko1.n - 1))):
            Code08_Taiko1.m = jcast('int', jcast('int', (Code08_Taiko1.m * Code08_Taiko1.k)))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < Code08_Taiko1.m):
            Code08_Taiko1.cur[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        Code08_Taiko1.cntp = jcast('int', 0)

    @staticmethod
    def euler(u, e):
        u = jcast('int', u)
        e = jcast('int', e)
        while (Code08_Taiko1.cur[u] < Code08_Taiko1.k):
            ne = jcast('int', ((_java_obj_1 := Code08_Taiko1.cur), (_java_key_2 := u), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])
            Code08_Taiko1.euler(jcast('int', jmod(jcast('int', jadd(jcast('int', (u * Code08_Taiko1.k)), ne)), Code08_Taiko1.m)), ne)
        jset(Code08_Taiko1.path, ((_java_obj_4 := Code08_Taiko1), (_java_key_5 := 'cntp'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], e)

    @staticmethod
    def main(args):
        in_ = Code08_Taiko1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        len = jcast('int', jcall(in_, 'nextInt'))
        num = jcast('int', 2)
        Code08_Taiko1.prepare(len, num)
        Code08_Taiko1.euler(0, jcast('int', (-1)))
        jcall(out, 'print', jadd(jcast('int', (Code08_Taiko1.m * Code08_Taiko1.k)), ' '))
        i = jcast('int', 1)
        while (i <= jcast('int', (Code08_Taiko1.n - 1))):
            jcall(out, 'print', '0')
            i = jcast('int', (i + 1))
        i = jcast('int', jcast('int', (Code08_Taiko1.cntp - 1)))
        while (i >= Code08_Taiko1.n):
            jcall(out, 'print', Code08_Taiko1.path[i])
            i = jcast('int', (i - 1))
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
            return jcast('int', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

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
            raise TypeError("No matching overload for Code08_Taiko1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code08_Taiko1.MAXN = jcast('int', 3001)
Code08_Taiko1.n = jcast('int', 0)
Code08_Taiko1.k = jcast('int', 0)
Code08_Taiko1.m = jcast('int', 0)
Code08_Taiko1.cur = jarray('int', [Code08_Taiko1.MAXN])
Code08_Taiko1.path = jarray('int', [Code08_Taiko1.MAXN])
Code08_Taiko1.cntp = jcast('int', 0)

if __name__ == '__main__':
    Code08_Taiko1.main([])
