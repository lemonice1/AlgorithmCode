# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 求最大公约数、最小公倍数
class Code01_GcdAndLcm:
    __java_fields__ = {}
    # 证明辗转相除法就是证明如下关系：
    # gcd(a, b) = gcd(b, a % b)
    # 假设a % b = r，即需要证明的关系为：gcd(a, b) = gcd(b, r)
    # 证明过程：
    # 因为a % b = r，所以如下两个等式必然成立
    # 1) a = b * q + r，q为0、1、2、3....中的一个整数
    # 2) r = a − b * q，q为0、1、2、3....中的一个整数
    # 假设u是a和b的公因子，则有: a = s * u, b = t * u
    # 把a和b带入2)得到，r = s * u - t * u * q = (s - t * q) * u
    # 这说明 : u如果是a和b的公因子，那么u也是r的因子
    # 假设v是b和r的公因子，则有: b = x * v, r = y * v
    # 把b和r带入1)得到，a = x * v * q + y * v = (x * q + y) * v
    # 这说明 : v如果是b和r的公因子，那么v也是a的公因子
    # 综上，a和b的每一个公因子 也是 b和r的一个公因子，反之亦然
    # 所以，a和b的全体公因子集合 = b和r的全体公因子集合
    # 即gcd(a, b) = gcd(b, r)
    # 证明结束
    @staticmethod
    def gcd(a, b):
        a = jcast('long', a)
        b = jcast('long', b)
        return jcast('long', (a if (b == 0) else Code01_GcdAndLcm.gcd(b, jcast('long', jmod(a, b)))))

    @staticmethod
    def lcm(a, b):
        a = jcast('long', a)
        b = jcast('long', b)
        return jcast('long', jcast('long', (jcast('long', jdiv(jcast('long', a), Code01_GcdAndLcm.gcd(a, b))) * b)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


