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

# 哈希冲突，Python版
# 给定一个长度为n的数组arr，接下来有m条操作，操作格式如下
# 操作 A x y : 下标 % x == y，符合要求的下标，把对应的值累加起来，打印结果
# 操作 C x y : arr[x]的值改成y
# 1 <= n、m <= 1.5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3396
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_HashCollision2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'blen': 'blen', 'arr': 'arr', 'dp': 'dp'}
    MAXN = 0
    MAXB = 0
    n = 0
    m = 0
    blen = 0
    arr = None
    dp = None
    @staticmethod
    def query(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        if (x <= Code01_HashCollision2.blen):
            return jcast('long', Code01_HashCollision2.dp[x][y])
        ans = jcast('long', 0)
        i = jcast('int', y)
        while (i <= Code01_HashCollision2.n):
            ans = jcast('long', jcast('long', jadd(ans, Code01_HashCollision2.arr[i])))
            i = jcast('int', jcast('int', jadd(i, x)))
        return jcast('long', ans)

    @staticmethod
    def update(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        delta = jcast('int', jcast('int', (v - Code01_HashCollision2.arr[i])))
        Code01_HashCollision2.arr[i] = jcast('int', v)
        x = jcast('int', 1)
        while (x <= Code01_HashCollision2.blen):
            ((_java_obj_1 := Code01_HashCollision2.dp[x]), (_java_key_2 := jcast('int', jmod(i, x))), jset(_java_obj_1, _java_key_2, jcast('long', jadd(jget(_java_obj_1, _java_key_2), delta))))[2]
            x = jcast('int', (x + 1))

    @staticmethod
    def prepare():
        Code01_HashCollision2.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code01_HashCollision2.n)))
        x = jcast('int', 1)
        while (x <= Code01_HashCollision2.blen):
            i = jcast('int', 1)
            while (i <= Code01_HashCollision2.n):
                ((_java_obj_3 := Code01_HashCollision2.dp[x]), (_java_key_4 := jcast('int', jmod(i, x))), jset(_java_obj_3, _java_key_4, jcast('long', jadd(jget(_java_obj_3, _java_key_4), Code01_HashCollision2.arr[i]))))[2]
                i = jcast('int', (i + 1))
            x = jcast('int', (x + 1))

    @staticmethod
    def main(args):
        in_ = Code01_HashCollision2.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_HashCollision2.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_HashCollision2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_HashCollision2.n):
            jset(Code01_HashCollision2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code01_HashCollision2.prepare()
        op = jchar(0)
        x = 0
        y = 0
        i = jcast('int', 1)
        while (i <= Code01_HashCollision2.m):
            op = jcast('char', jcall(in_, 'nextChar'))
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            if (op == jchar('A')):
                jcall(out, 'println', Code01_HashCollision2.query(x, y))
            else:
                Code01_HashCollision2.update(x, y)
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
            return jcast('byte', self.buffer[((_java_obj_5 := self), (_java_key_6 := 'ptr'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))), _java_old_7)[4]])

        def nextChar(self):
            c = 0
            while True:
                c = jcast('byte', self.readByte())
                if (c == jcast('int', (-1))):
                    return jcast('char', 0)
                if not ((c <= jchar(' '))):
                    break
            ans = jcast('char', 0)
            while (c > jchar(' ')):
                ans = jcast('char', jcast('char', c))
                c = jcast('byte', self.readByte())
            return jcast('char', ans)

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
            raise TypeError("No matching overload for Code01_HashCollision2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_HashCollision2.MAXN = jcast('int', 150001)
Code01_HashCollision2.MAXB = jcast('int', 401)
Code01_HashCollision2.n = jcast('int', 0)
Code01_HashCollision2.m = jcast('int', 0)
Code01_HashCollision2.blen = jcast('int', 0)
Code01_HashCollision2.arr = jarray('int', [Code01_HashCollision2.MAXN])
Code01_HashCollision2.dp = jarray('long', [Code01_HashCollision2.MAXB, Code01_HashCollision2.MAXB])

if __name__ == '__main__':
    Code01_HashCollision2.main([])
