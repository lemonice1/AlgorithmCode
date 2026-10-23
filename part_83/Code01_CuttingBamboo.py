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

# 砍竹子II
# 现需要将一根长为正整数bamboo_len的竹子砍为若干段
# 每段长度均为正整数
# 请返回每段竹子长度的最大乘积是多少
# 答案需要对 1000000007 取模
# 测试链接 : https://leetcode.cn/problems/jian-sheng-zi-ii-lcof/
class Code01_CuttingBamboo:
    __java_fields__ = {}
    # 快速幂，求余数
    # 求x的n次方，最终得到的结果 % mod
    @staticmethod
    def power(x, n, mod):
        x = jcast('long', x)
        n = jcast('int', n)
        mod = jcast('int', mod)
        ans = jcast('long', 1)
        while (n > 0):
            if (jcast('int', (n & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), mod)))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), mod)))
            n = jcast('int', jcast('int', (n >> (1 & 31))))
        return jcast('long', ans)

    @staticmethod
    def cuttingBamboo(n):
        n = jcast('int', n)
        if (n == 2):
            return jcast('int', 1)
        if (n == 3):
            return jcast('int', 2)
        mod = jcast('int', 1000000007)
        # n = 4  -> 2 * 2
        # n = 5  -> 3 * 2
        # n = 6  -> 3 * 3
        # n = 7  -> 3 * 2 * 2
        # n = 8  -> 3 * 3 * 2
        # n = 9  -> 3 * 3 * 3
        # n = 10 -> 3 * 3 * 2 * 2
        # n = 11 -> 3 * 3 * 3 * 2
        # n = 12 -> 3 * 3 * 3 * 3
        tail = jcast('int', (1 if (jcast('int', jmod(n, 3)) == 0) else (4 if (jcast('int', jmod(n, 3)) == 1) else 2)))
        power = jcast('int', jcast('int', jdiv((n if (tail == 1) else jcast('int', (n - tail))), 3)))
        return jcast('int', jcast('int', jcast('long', jmod(jcast('long', (Code01_CuttingBamboo.power(3, power, mod) * tail)), mod))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


