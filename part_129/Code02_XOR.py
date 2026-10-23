# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 第k小的异或和，HDU的题目
# 这道题课上没有讲，核心逻辑和题目2一样，只是数据范围稍有不同
# 注意如下代码中，有注释的部分即可，其他代码都一样
# 给定一个长度为n的数组arr，arr中都是long类型的非负数，可能有重复值
# 在这些数中选取任意个，至少要选一个数字，可以得到很多异或和
# 假设异或和的结果去重，返回第k小的异或和
# 测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=3949
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_XOR:
    __java_fields__ = {'MAXN': 'MAXN', 'BIT': 'BIT', 'arr': 'arr', 'len': 'len', 'zero': 'zero', 't': 't', 'n': 'n'}
    MAXN = 0
    # 数字最大为10^18，需要更高的二进制位
    BIT = 0
    arr = None
    len = 0
    zero = False
    t = 0
    n = 0
    @staticmethod
    def compute():
        Code02_XOR.len = jcast('int', 1)
        i = jcast('long', Code02_XOR.BIT)
        while (i >= 0):
            try:
                j = jcast('int', Code02_XOR.len)
                while (j <= Code02_XOR.n):
                    try:
                        if (jcast('long', (Code02_XOR.arr[j] & jcast('long', (1 << (i & 63))))) != 0):
                            Code02_XOR.swap(j, Code02_XOR.len)
                            raise JBreak(None)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                if (jcast('long', (Code02_XOR.arr[Code02_XOR.len] & jcast('long', (1 << (i & 63))))) != 0):
                    j = jcast('int', 1)
                    while (j <= Code02_XOR.n):
                        if ((j != Code02_XOR.len) and (jcast('long', (Code02_XOR.arr[j] & jcast('long', (1 << (i & 63))))) != 0)):
                            Code02_XOR.arr[j] = jcast('long', jcast('long', (Code02_XOR.arr[j] ^ Code02_XOR.arr[Code02_XOR.len])))
                        j = jcast('int', (j + 1))
                    Code02_XOR.len = jcast('int', (Code02_XOR.len + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('long', (i - 1))
        Code02_XOR.len = jcast('int', (Code02_XOR.len - 1))
        Code02_XOR.zero = jcast('boolean', (Code02_XOR.len != Code02_XOR.n))

    @staticmethod
    def swap(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        tmp = jcast('long', Code02_XOR.arr[a])
        Code02_XOR.arr[a] = jcast('long', Code02_XOR.arr[b])
        Code02_XOR.arr[b] = jcast('long', tmp)

    @staticmethod
    def query(k):
        k = jcast('long', k)
        if (Code02_XOR.zero and (k == 1)):
            return jcast('long', 0)
        if Code02_XOR.zero:
            k = jcast('long', (k - 1))
        if (k >= jcast('long', (1 << (Code02_XOR.len & 63)))):
            return jcast('long', jcast('int', (-1)))
        ans = jcast('long', 0)
        i = jcast('int', Code02_XOR.len)
        j = jcast('int', 0)
        while (i >= 1):
            if (jcast('long', (k & jcast('long', (1 << (j & 63))))) != 0):
                ans = jcast('long', jcast('long', (ans ^ Code02_XOR.arr[i])))
            i = jcast('int', (i - 1))
            j = jcast('int', (j + 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code02_XOR.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        # 注意有多组测试
        Code02_XOR.t = jcast('int', jcall(in_, 'nextInt'))
        c = jcast('int', 1)
        while (c <= Code02_XOR.t):
            Code02_XOR.n = jcast('int', jcall(in_, 'nextInt'))
            i = jcast('int', 1)
            while (i <= Code02_XOR.n):
                jset(Code02_XOR.arr, i, jcall(in_, 'nextLong'))
                i = jcast('int', (i + 1))
            # 确保arr[n + 1]是0
            Code02_XOR.arr[jcast('int', jadd(Code02_XOR.n, 1))] = jcast('long', 0)
            Code02_XOR.compute()
            jcall(out, 'println', jadd(jadd('Case #', c), ':'))
            q = jcast('int', jcall(in_, 'nextInt'))
            i = jcast('int', 1)
            while (i <= q):
                k = jcast('long', jcall(in_, 'nextLong'))
                jcall(out, 'println', Code02_XOR.query(k))
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
            return jcast('int', self.buffer[((_java_obj_3 := self), (_java_key_4 := 'ptr'), (_java_old_5 := jget(_java_obj_3, _java_key_4)), jset(_java_obj_3, _java_key_4, jcast('int', (_java_old_5 + (1)))), _java_old_5)[4]])

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

        def nextLong(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('long', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('long', jcast('long', jadd(jcast('long', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('long', (jcast('long', (-val)) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_XOR.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_XOR.MAXN = jcast('int', 100001)
Code02_XOR.BIT = jcast('int', 60)
Code02_XOR.arr = jarray('long', [Code02_XOR.MAXN])
Code02_XOR.len = jcast('int', 0)
Code02_XOR.zero = jcast('boolean', False)
Code02_XOR.t = jcast('int', 0)
Code02_XOR.n = jcast('int', 0)

if __name__ == '__main__':
    Code02_XOR.main([])
