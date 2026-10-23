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

class TwoSmallQuestions:
    __java_fields__ = {}
    # 给定一个正数x
    # 已知用m个二进制位一定能表示x
    # 从高位到低位打印x每一位的状态
    @staticmethod
    def show1(x, m):
        x = jcast('int', x)
        m = jcast('int', m)
        p = jcast('int', jcast('int', (m - 1)))
        t = jcast('int', x)
        while (p >= 0):
            if (jcast('int', (1 << (p & 31))) <= t):
                t = jcast('int', jcast('int', (t - jcast('int', (1 << (p & 31))))))
                jprint(jadd(jadd(jadd(x, '的第'), p), '位是1'), newline=True)
            else:
                jprint(jadd(jadd(jadd(x, '的第'), p), '位是0'), newline=True)
            p = jcast('int', (p - 1))

    # 给定一个正数x
    # 打印<=x最大的2的幂
    # 到底是2的几次方
    @staticmethod
    def show2(x):
        x = jcast('int', x)
        power = jcast('int', 0)
        # 以下注释掉的写法不对，没有考虑溢出
        # while ((1 << power) <= x) {
        # power++;
        # }
        # power--;
        # 防止溢出的写法
        while (jcast('int', (1 << (power & 31))) <= jcast('int', (x >> (1 & 31)))):
            power = jcast('int', (power + 1))
        jprint(jadd(jadd(jadd(jadd('<=', x), '最大的2的幂，是2的'), power), '次方'), newline=True)

    @staticmethod
    def main(args):
        # 需要保证用m个二进制位一定能表示x
        x = jcast('int', 101)
        m = jcast('int', 10)
        TwoSmallQuestions.show1(x, m)
        x = jcast('int', 13)
        TwoSmallQuestions.show2(x)
        x = jcast('int', 16)
        TwoSmallQuestions.show2(x)
        x = jcast('int', 2000000000)
        TwoSmallQuestions.show2(x)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    TwoSmallQuestions.main([])
