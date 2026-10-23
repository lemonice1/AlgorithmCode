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

class Exgcd:
    __java_fields__ = {'d': 'd', 'x': 'x', 'y': 'y', 'px': 'px', 'py': 'py'}
    # 扩展欧几里得算法
    # 对于方程ax + by = gcd(a,b)
    # 当a和b确定，那么gcd(a,b)也确定
    # 扩展欧几里得算法可以给出a和b的最大公约数d、以及其中一个特解x、y
    # 特别注意要保证入参a和b没有负数
    d = 0
    x = 0
    y = 0
    px = 0
    py = 0
    @staticmethod
    def exgcd(a, b):
        a = jcast('long', a)
        b = jcast('long', b)
        if (b == 0):
            Exgcd.d = jcast('long', a)
            Exgcd.x = jcast('long', 1)
            Exgcd.y = jcast('long', 0)
        else:
            Exgcd.exgcd(b, jcast('long', jmod(a, b)))
            Exgcd.px = jcast('long', Exgcd.x)
            Exgcd.py = jcast('long', Exgcd.y)
            Exgcd.x = jcast('long', Exgcd.py)
            Exgcd.y = jcast('long', jcast('long', (Exgcd.px - jcast('long', (Exgcd.py * jcast('long', jdiv(a, b)))))))

    # 讲解099，费马小定理计算逆元
    @staticmethod
    def fermat(num, mod):
        num = jcast('long', num)
        mod = jcast('long', mod)
        return jcast('long', Exgcd.power(num, jcast('long', (mod - 2)), mod))

    @staticmethod
    def power(num, pow, mod):
        num = jcast('long', num)
        pow = jcast('long', pow)
        mod = jcast('long', mod)
        ans = jcast('long', 1)
        while (pow > 0):
            if (jcast('long', (pow & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * num)), mod)))
            num = jcast('long', jcast('long', jmod(jcast('long', (num * num)), mod)))
            pow = jcast('long', jcast('long', (pow >> (1 & 63))))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        # 扩展欧几里得算法例子
        a = jcast('int', 220)
        b = jcast('int', 170)
        Exgcd.exgcd(a, b)
        jprint(jadd(jadd(jadd(jadd(jadd(jadd('gcd(', a), ', '), b), ')'), ' = '), Exgcd.d), newline=True)
        jprint(jadd(jadd(jadd(jadd('x = ', Exgcd.x), ', '), ' y = '), Exgcd.y), newline=True)
        # 扩展欧几里得算法可以去求逆元
        jprint('求逆元测试开始', newline=True)
        mod = jcast('long', 1000000007)
        test = jcast('long', 10000000)
        num = jcast('long', 1)
        while (num <= test):
            Exgcd.exgcd(num, mod)
            Exgcd.x = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(Exgcd.x, mod)), mod)), mod)))
            if (Exgcd.x != Exgcd.fermat(num, mod)):
                jprint('出错了!', newline=True)
            num = jcast('long', (num + 1))
        jprint('求逆元测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Exgcd.d = jcast('long', 0)
Exgcd.x = jcast('long', 0)
Exgcd.y = jcast('long', 0)
Exgcd.px = jcast('long', 0)
Exgcd.py = jcast('long', 0)

if __name__ == '__main__':
    Exgcd.main([])
