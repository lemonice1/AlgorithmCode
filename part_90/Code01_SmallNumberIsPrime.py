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

# 判断较小的数字是否是质数
# 时间复杂度O(根号n)
class Code01_SmallNumberIsPrime:
    __java_fields__ = {}
    @staticmethod
    def isPrime(n):
        n = jcast('long', n)
        if (n <= 1):
            return jcast('boolean', False)
        # 2 ... 根号n
        i = jcast('long', 2)
        while (jcast('long', (i * i)) <= n):
            if (jcast('long', jmod(n, i)) == 0):
                return jcast('boolean', False)
            i = jcast('long', (i + 1))
        return jcast('boolean', True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


