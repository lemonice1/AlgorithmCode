# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 打印n层汉诺塔问题的最优移动轨迹
class Code07_TowerOfHanoi:
    __java_fields__ = {}
    @staticmethod
    def hanoi(n):
        n = jcast('int', n)
        if (n > 0):
            Code07_TowerOfHanoi.f(n, '左', '右', '中')

    @staticmethod
    def f(i, from_, to, other):
        i = jcast('int', i)
        if (i == 1):
            jprint(jadd(jadd(jadd('移动圆盘 1 从 ', from_), ' 到 '), to), newline=True)
        else:
            Code07_TowerOfHanoi.f(jcast('int', (i - 1)), from_, other, to)
            jprint(jadd(jadd(jadd(jadd(jadd('移动圆盘 ', i), ' 从 '), from_), ' 到 '), to), newline=True)
            Code07_TowerOfHanoi.f(jcast('int', (i - 1)), other, to, from_)

    @staticmethod
    def main(args):
        n = jcast('int', 3)
        Code07_TowerOfHanoi.hanoi(n)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code07_TowerOfHanoi.main([])
