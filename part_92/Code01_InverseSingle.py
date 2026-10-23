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

# 单个除数求逆元
# 对数器验证
class Code01_InverseSingle:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        # 1) 必须保证a/b可以整除
        # 2) 必须保证mod是质数
        # 3) 必须保证b和mod的最大公约数为1
        mod = jcast('int', 41)
        b = jcast('long', 3671613)
        a = jcast('long', jcast('long', (67312 * b)))
        jprint(Code01_InverseSingle.compute1(a, b, mod), newline=True)
        jprint(Code01_InverseSingle.compute2(a, b, mod), newline=True)

    @staticmethod
    def compute1(a, b, mod):
        a = jcast('long', a)
        b = jcast('long', b)
        mod = jcast('int', mod)
        return jcast('int', jcast('int', jcast('long', jmod(jcast('long', jdiv(a, b)), mod))))

    @staticmethod
    def compute2(a, b, mod):
        a = jcast('long', a)
        b = jcast('long', b)
        mod = jcast('int', mod)
        inv = jcast('long', Code01_InverseSingle.power(b, jcast('int', (mod - 2)), mod))
        return jcast('int', jcast('int', jcast('long', jmod(jcast('long', (jcast('long', jmod(a, mod)) * inv)), mod))))

    # 乘法快速幂
    # 计算b的n次方的结果%mod
    @staticmethod
    def power(b, n, mod):
        b = jcast('long', b)
        n = jcast('int', n)
        mod = jcast('int', mod)
        ans = jcast('long', 1)
        while (n > 0):
            if (jcast('int', (n & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * b)), mod)))
            b = jcast('long', jcast('long', jmod(jcast('long', (b * b)), mod)))
            n = jcast('int', jcast('int', (n >> (1 & 31))))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code01_InverseSingle.main([])
