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

# 用这个例子讲解递归如何执行
class GetMaxValue:
    __java_fields__ = {}
    @staticmethod
    def maxValue(arr):
        return jcast('int', GetMaxValue.f(arr, 0, jcast('int', (jget(arr, 'length') - 1))))

    # arr[l....r]范围上的最大值
    @staticmethod
    def f(arr, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return jcast('int', arr[l])
        m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        lmax = jcast('int', GetMaxValue.f(arr, l, m))
        rmax = jcast('int', GetMaxValue.f(arr, jcast('int', jadd(m, 1)), r))
        return jcast('int', jstatic('Math', 'max', lmax, rmax))

    @staticmethod
    def main(args):
        arr = jarray('int', [None], [3, 8, 7, 6, 4, 5, 1, 2])
        jprint(jadd('数组最大值 : ', GetMaxValue.maxValue(arr)), newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    GetMaxValue.main([])
