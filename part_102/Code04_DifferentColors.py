# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# HH的项链
# 一共有n个位置，每个位置颜色给定，i位置的颜色是arr[i]
# 一共有m个查询，question[i] = {li, ri}
# 表示第i条查询想查arr[li..ri]范围上一共有多少种不同颜色
# 返回每条查询的答案
# 1 <= n、m、arr[i] <= 10^6
# 1 <= li <= ri <= n
# 测试链接 : https://www.luogu.com.cn/problem/P1972
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 代码逻辑和课上讲的完全一致，但是重写了读写工具类，增加了io效率
class Code04_DifferentColors:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'query': 'query', 'ans': 'ans', 'map': 'map', 'tree': 'tree', 'n': 'n', 'm': 'm'}
    MAXN = 0
    arr = None
    query = None
    ans = None
    map = None
    tree = None
    n = 0
    m = 0
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code04_DifferentColors.n):
            Code04_DifferentColors.tree[i] = jcast('int', jcast('int', jadd(Code04_DifferentColors.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code04_DifferentColors.lowbit(i))))

    @staticmethod
    def sum(i):
        i = jcast('int', i)
        ans = jcast('int', 0)
        while (i > 0):
            ans = jcast('int', jcast('int', jadd(ans, Code04_DifferentColors.tree[i])))
            i = jcast('int', jcast('int', (i - Code04_DifferentColors.lowbit(i))))
        return jcast('int', ans)

    @staticmethod
    def range(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        return jcast('int', jcast('int', (Code04_DifferentColors.sum(r) - Code04_DifferentColors.sum(jcast('int', (l - 1))))))

    @staticmethod
    def compute():
        jstatic('Arrays', 'sort', Code04_DifferentColors.query, 1, jcast('int', jadd(Code04_DifferentColors.m, 1)), (lambda a, b: (a[1] - b[1])))
        s = jcast('int', 1)
        q = jcast('int', 1)
        l = 0
        r = 0
        i = 0
        while (q <= Code04_DifferentColors.m):
            r = jcast('int', Code04_DifferentColors.query[q][1])
            while (s <= r):
                color = jcast('int', Code04_DifferentColors.arr[s])
                if (Code04_DifferentColors.map[color] != 0):
                    Code04_DifferentColors.add(Code04_DifferentColors.map[color], jcast('int', (-1)))
                Code04_DifferentColors.add(s, 1)
                Code04_DifferentColors.map[color] = jcast('int', s)
                s = jcast('int', (s + 1))
            l = jcast('int', Code04_DifferentColors.query[q][0])
            i = jcast('int', Code04_DifferentColors.query[q][2])
            jset(Code04_DifferentColors.ans, i, Code04_DifferentColors.range(l, r))
            q = jcast('int', (q + 1))

    @staticmethod
    def main(args):
        in_ = Code04_DifferentColors.FastReader(_java_ctor=0)
        out = jnew('BufferedWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_DifferentColors.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_DifferentColors.n):
            jset(Code04_DifferentColors.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code04_DifferentColors.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_DifferentColors.m):
            jset(Code04_DifferentColors.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code04_DifferentColors.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code04_DifferentColors.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code04_DifferentColors.compute()
        i = jcast('int', 1)
        while (i <= Code04_DifferentColors.m):
            jcall(out, 'write', jadd(Code04_DifferentColors.ans[i], '\n'))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'BUFFER_SIZE': 'BUFFER_SIZE', 'in': 'in_', 'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len'}
        # BUFFER_SIZE：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.in_ = jget(System, 'in')
            self.buffer = jarray('byte', [self.BUFFER_SIZE])
            self.ptr = jcast('int', jset(self, 'len', 0))

        def hasNextByte(self):
            if (self.ptr < self.len):
                return jcast('boolean', True)
            self.ptr = jcast('int', 0)
            self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
            return jcast('boolean', (self.len > 0))

        def readByte(self):
            if (not self.hasNextByte()):
                return jcast('byte', jcast('int', (-1)))
            return jcast('byte', self.buffer[((_java_obj_1 := self), (_java_key_2 := 'ptr'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]])

        def hasNext(self):
            while self.hasNextByte():
                b = jcast('byte', self.buffer[self.ptr])
                if (not self.isWhitespace(b)):
                    return jcast('boolean', True)
                self.ptr = jcast('int', (self.ptr + 1))
            return jcast('boolean', False)

        def next(self):
            c = 0
            while True:
                c = jcast('byte', self.readByte())
                if (c == jcast('int', (-1))):
                    return None
                if not ((c <= jchar(' '))):
                    break
            sb = jnew('StringBuilder')
            while (c > jchar(' ')):
                jcall(sb, 'append', jcast('char', c))
                c = jcast('byte', self.readByte())
            return jcall(sb, 'toString')

        def nextInt(self):
            num = jcast('int', 0)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                num = jcast('int', jcast('int', jadd(jcast('int', (num * 10)), jcast('int', (b - jchar('0'))))))
                b = jcast('byte', self.readByte())
            return jcast('int', (jcast('int', (-num)) if minus else num))

        def nextDouble(self):
            num = jcast('double', 0)
            div = jcast('double', 1)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while (((not self.isWhitespace(b)) and (b != jchar('.'))) and (b != jcast('int', (-1)))):
                num = jcast('double', jadd((num * 10), jcast('int', (b - jchar('0')))))
                b = jcast('byte', self.readByte())
            if (b == jchar('.')):
                b = jcast('byte', self.readByte())
                while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                    num = jcast('double', jadd(num, jdiv(jcast('int', (b - jchar('0'))), (div := (div * 10)))))
                    b = jcast('byte', self.readByte())
            return jcast('double', ((-num) if minus else num))

        def isWhitespace(self, b):
            b = jcast('byte', b)
            return jcast('boolean', ((((b == jchar(' ')) or (b == jchar('\n'))) or (b == jchar('\r'))) or (b == jchar('\t'))))

        def __init__(self, *args, _java_ctor=None):
            self.BUFFER_SIZE = jcast('int', jcast('int', (1 << (16 & 31))))
            self.in_ = None
            self.buffer = None
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_DifferentColors.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_DifferentColors.MAXN = jcast('int', 1000001)
Code04_DifferentColors.arr = jarray('int', [Code04_DifferentColors.MAXN])
Code04_DifferentColors.query = jarray('int', [Code04_DifferentColors.MAXN, 3])
Code04_DifferentColors.ans = jarray('int', [Code04_DifferentColors.MAXN])
Code04_DifferentColors.map = jarray('int', [Code04_DifferentColors.MAXN])
Code04_DifferentColors.tree = jarray('int', [Code04_DifferentColors.MAXN])
Code04_DifferentColors.n = jcast('int', 0)
Code04_DifferentColors.m = jcast('int', 0)

if __name__ == '__main__':
    Code04_DifferentColors.main([])
