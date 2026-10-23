# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 加法、减法、乘法的同余原理
# 不包括除法，因为除法必须求逆元，后续课讲述
class Code03_SameMod:
    __java_fields__ = {}
    # 为了测试
    @staticmethod
    def random():
        return jcast('long', jcast('long', (jstatic('Math', 'random') * jget(Long, 'MAX_VALUE'))))

    # 计算 ((a + b) * (c - d) + (a * c - b * d)) % mod 的非负结果
    @staticmethod
    def f1(a, b, c, d, mod):
        a = jcast('long', a)
        b = jcast('long', b)
        c = jcast('long', c)
        d = jcast('long', d)
        mod = jcast('int', mod)
        # a
        o1 = jnew('BigInteger', jstatic('String', 'valueOf', a))
        # b
        o2 = jnew('BigInteger', jstatic('String', 'valueOf', b))
        # c
        o3 = jnew('BigInteger', jstatic('String', 'valueOf', c))
        # d
        o4 = jnew('BigInteger', jstatic('String', 'valueOf', d))
        # a + b
        o5 = jcall(o1, 'add', o2)
        # c - d
        o6 = jcall(o3, 'subtract', o4)
        # a * c
        o7 = jcall(o1, 'multiply', o3)
        # b * d
        o8 = jcall(o2, 'multiply', o4)
        # (a + b) * (c - d)
        o9 = jcall(o5, 'multiply', o6)
        # (a * c - b * d)
        o10 = jcall(o7, 'subtract', o8)
        # ((a + b) * (c - d) + (a * c - b * d))
        o11 = jcall(o9, 'add', o10)
        # ((a + b) * (c - d) + (a * c - b * d)) % mod
        o12 = jcall(o11, 'mod', jnew('BigInteger', jstatic('String', 'valueOf', mod)))
        if (jcall(o12, 'signum') == jcast('int', (-1))):
            # 如果是负数那么+mod返回
            return jcast('int', jcall(jcall(o12, 'add', jnew('BigInteger', jstatic('String', 'valueOf', mod))), 'intValue'))
        else:
            # 如果不是负数直接返回
            return jcast('int', jcall(o12, 'intValue'))

    # 计算 ((a + b) * (c - d) + (a * c - b * d)) % mod 的非负结果
    @staticmethod
    def f2(a, b, c, d, mod):
        a = jcast('long', a)
        b = jcast('long', b)
        c = jcast('long', c)
        d = jcast('long', d)
        mod = jcast('int', mod)
        # a
        o1 = jcast('int', jcast('int', jcast('long', jmod(a, mod))))
        # b
        o2 = jcast('int', jcast('int', jcast('long', jmod(b, mod))))
        # c
        o3 = jcast('int', jcast('int', jcast('long', jmod(c, mod))))
        # d
        o4 = jcast('int', jcast('int', jcast('long', jmod(d, mod))))
        # a + b
        o5 = jcast('int', jcast('int', jmod(jcast('int', jadd(o1, o2)), mod)))
        # c - d
        o6 = jcast('int', jcast('int', jmod(jcast('int', jadd(jcast('int', (o3 - o4)), mod)), mod)))
        # a * c
        o7 = jcast('int', jcast('int', jcast('long', jmod(jcast('long', (jcast('long', o1) * o3)), mod))))
        # b * d
        o8 = jcast('int', jcast('int', jcast('long', jmod(jcast('long', (jcast('long', o2) * o4)), mod))))
        # (a + b) * (c - d)
        o9 = jcast('int', jcast('int', jcast('long', jmod(jcast('long', (jcast('long', o5) * o6)), mod))))
        # (a * c - b * d)
        o10 = jcast('int', jcast('int', jmod(jcast('int', jadd(jcast('int', (o7 - o8)), mod)), mod)))
        # ((a + b) * (c - d) + (a * c - b * d)) % mod
        ans = jcast('int', jcast('int', jmod(jcast('int', jadd(o9, o10)), mod)))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        jprint('测试开始', newline=True)
        testTime = jcast('int', 100000)
        mod = jcast('int', 1000000007)
        i = jcast('int', 0)
        while (i < testTime):
            a = jcast('long', Code03_SameMod.random())
            b = jcast('long', Code03_SameMod.random())
            c = jcast('long', Code03_SameMod.random())
            d = jcast('long', Code03_SameMod.random())
            if (Code03_SameMod.f1(a, b, c, d, mod) != Code03_SameMod.f2(a, b, c, d, mod)):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)
        jprint('===', newline=True)
        a = jcast('long', Code03_SameMod.random())
        b = jcast('long', Code03_SameMod.random())
        c = jcast('long', Code03_SameMod.random())
        d = jcast('long', Code03_SameMod.random())
        jprint(jadd('a : ', a), newline=True)
        jprint(jadd('b : ', b), newline=True)
        jprint(jadd('c : ', c), newline=True)
        jprint(jadd('d : ', d), newline=True)
        jprint('===', newline=True)
        jprint(jadd('f1 : ', Code03_SameMod.f1(a, b, c, d, mod)), newline=True)
        jprint(jadd('f2 : ', Code03_SameMod.f2(a, b, c, d, mod)), newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code03_SameMod.main([])
