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

# 判断一个数字是否是若干数量(数量>1)的连续正整数的和
class Code03_IsSumOfConsecutiveNumbers:
    __java_fields__ = {}
    @staticmethod
    def is1(num):
        num = jcast('int', num)
        start = jcast('int', 1)
        sum = 0
        while (start <= num):
            try:
                sum = jcast('int', start)
                j = jcast('int', jcast('int', jadd(start, 1)))
                while (j <= num):
                    try:
                        if (jcast('int', jadd(sum, j)) > num):
                            raise JBreak(None)
                        if (jcast('int', jadd(sum, j)) == num):
                            return jcast('boolean', True)
                        sum = jcast('int', jcast('int', jadd(sum, j)))
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            start = jcast('int', (start + 1))
        return jcast('boolean', False)

    @staticmethod
    def is2(num):
        num = jcast('int', num)
        return jcast('boolean', (jcast('int', (num & jcast('int', (num - 1)))) != 0))

    @staticmethod
    def main(args):
        num = jcast('int', 1)
        while (num < 200):
            jprint(jadd(jadd(num, ' : '), ('T' if Code03_IsSumOfConsecutiveNumbers.is1(num) else 'F')), newline=True)
            num = jcast('int', (num + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code03_IsSumOfConsecutiveNumbers.main([])
