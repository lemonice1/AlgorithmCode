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

# 用异或运算交换两数的值
class Code01_SwapExclusiveOr:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        a = jcast('int', jcast('int', (-2323)))
        b = jcast('int', 10)
        a = jcast('int', jcast('int', (a ^ b)))
        b = jcast('int', jcast('int', (a ^ b)))
        a = jcast('int', jcast('int', (a ^ b)))
        jprint(a, newline=True)
        jprint(b, newline=True)
        arr = jarray('int', [None], [3, 5])
        Code01_SwapExclusiveOr.swap(arr, 0, 1)
        jprint(arr[0], newline=True)
        jprint(arr[1], newline=True)
        Code01_SwapExclusiveOr.swap(arr, 0, 0)
        jprint(arr[0], newline=True)

    # 当i!=j，没问题，会完成交换功能
    # 当i==j，会出错
    # 所以知道这种写法即可，并不推荐
    @staticmethod
    def swap(arr, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        arr[i] = jcast('int', jcast('int', (arr[i] ^ arr[j])))
        arr[j] = jcast('int', jcast('int', (arr[i] ^ arr[j])))
        arr[i] = jcast('int', jcast('int', (arr[i] ^ arr[j])))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code01_SwapExclusiveOr.main([])
