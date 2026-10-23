# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 所有可能的密码串，Python版
# 给定正数n，表示密码有n位，每一位可能的数字是[0..9]
# 密码有(10^n)个可能性，构造一个字符串，其中的连续子串包含所有可能的密码
# 先保证字符串的长度最短，然后保证字典序尽量的小，返回这个字符串
# 1 <= n <= 6
# 测试链接 : http://poj.org/problem?id=1780
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_Password2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'k': 'k', 'm': 'm', 'cur': 'cur', 'path': 'path', 'cntp': 'cntp', 'sta': 'sta', 'u': 'u', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    n = 0
    k = 0
    m = 0
    cur = None
    path = None
    cntp = 0
    sta = None
    u = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, e):
        u = jcast('int', u)
        e = jcast('int', e)
        jset(Code07_Password2.sta[Code07_Password2.stacksize], 0, u)
        jset(Code07_Password2.sta[Code07_Password2.stacksize], 1, e)
        Code07_Password2.stacksize = jcast('int', (Code07_Password2.stacksize + 1))

    @staticmethod
    def pop():
        Code07_Password2.stacksize = jcast('int', (Code07_Password2.stacksize - 1))
        Code07_Password2.u = jcast('int', Code07_Password2.sta[Code07_Password2.stacksize][0])
        Code07_Password2.e = jcast('int', Code07_Password2.sta[Code07_Password2.stacksize][1])

    @staticmethod
    def prepare(len, num):
        len = jcast('int', len)
        num = jcast('int', num)
        Code07_Password2.n = jcast('int', len)
        Code07_Password2.k = jcast('int', num)
        Code07_Password2.m = jcast('int', 1)
        i = jcast('int', 1)
        while (i <= jcast('int', (Code07_Password2.n - 1))):
            Code07_Password2.m = jcast('int', jcast('int', (Code07_Password2.m * Code07_Password2.k)))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < Code07_Password2.m):
            Code07_Password2.cur[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        Code07_Password2.cntp = jcast('int', 0)

    # 本题的递归深度很大：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def euler(node, edge):
        node = jcast('int', node)
        edge = jcast('int', edge)
        Code07_Password2.stacksize = jcast('int', 0)
        Code07_Password2.push(node, edge)
        while (Code07_Password2.stacksize > 0):
            Code07_Password2.pop()
            if (Code07_Password2.cur[Code07_Password2.u] < Code07_Password2.k):
                ne = jcast('int', ((_java_obj_1 := Code07_Password2.cur), (_java_key_2 := Code07_Password2.u), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])
                Code07_Password2.push(Code07_Password2.u, Code07_Password2.e)
                Code07_Password2.push(jcast('int', jmod(jcast('int', jadd(jcast('int', (Code07_Password2.u * Code07_Password2.k)), ne)), Code07_Password2.m)), ne)
            else:
                jset(Code07_Password2.path, ((_java_obj_4 := Code07_Password2), (_java_key_5 := 'cntp'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code07_Password2.e)

    @staticmethod
    def main(args):
        in_ = Code07_Password2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        len = jcast('int', jcall(in_, 'nextInt'))
        num = jcast('int', 10)
        while (len != 0):
            Code07_Password2.prepare(len, num)
            Code07_Password2.euler(0, jcast('int', (-1)))
            i = jcast('int', 1)
            while (i <= jcast('int', (Code07_Password2.n - 1))):
                jcall(out, 'print', '0')
                i = jcast('int', (i + 1))
            i = jcast('int', jcast('int', (Code07_Password2.cntp - 1)))
            while (i >= 1):
                jcall(out, 'print', Code07_Password2.path[i])
                i = jcast('int', (i - 1))
            jcall(out, 'println')
            len = jcast('int', jcall(in_, 'nextInt'))
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
            raise TypeError("No matching overload for Code07_Password2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_Password2.MAXN = jcast('int', 1000002)
Code07_Password2.n = jcast('int', 0)
Code07_Password2.k = jcast('int', 0)
Code07_Password2.m = jcast('int', 0)
Code07_Password2.cur = jarray('int', [Code07_Password2.MAXN])
Code07_Password2.path = jarray('int', [Code07_Password2.MAXN])
Code07_Password2.cntp = jcast('int', 0)
Code07_Password2.sta = jarray('int', [Code07_Password2.MAXN, 2])
Code07_Password2.u = jcast('int', 0)
Code07_Password2.e = jcast('int', 0)
Code07_Password2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code07_Password2.main([])
