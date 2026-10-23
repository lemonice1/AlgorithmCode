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

# 草一共有n的重量，两只牛轮流吃草，A牛先吃，B牛后吃
# 每只牛在自己的回合，吃草的重量必须是4的幂，1、4、16、64....
# 谁在自己的回合正好把草吃完谁赢，根据输入的n，返回谁赢
class Code02_EatGrass:
    __java_fields__ = {}
    # "A"  "B"
    @staticmethod
    def win1(n):
        n = jcast('int', n)
        return Code02_EatGrass.f(n, 'A')

    # rest : 还剩多少草
    # cur  : 当前选手的名字
    # 返回  : 还剩rest份草，当前选手是cur，按照题目说的，返回最终谁赢
    @staticmethod
    def f(rest, cur):
        rest = jcast('int', rest)
        enemy = ('B' if jcall(cur, 'equals', 'A') else 'A')
        if (rest < 5):
            return (enemy if ((rest == 0) or (rest == 2)) else cur)
        # rest >= 5
        # rest == 100
        # cur :
        # 1) 1 ->99,enemy ....
        # 2) 4 ->96,enemy ....
        # 3) 16 -> 84,enemy ....
        # 4) 64 -> 36,enemy ...
        # 没有cur赢的分支，enemy赢
        pick = jcast('int', 1)
        while (pick <= rest):
            if jcall(Code02_EatGrass.f(jcast('int', (rest - pick)), enemy), 'equals', cur):
                return cur
            pick = jcast('int', jcast('int', (pick * 4)))
        return enemy

    @staticmethod
    def win2(n):
        n = jcast('int', n)
        if ((jcast('int', jmod(n, 5)) == 0) or (jcast('int', jmod(n, 5)) == 2)):
            return 'B'
        else:
            return 'A'

    @staticmethod
    def main(args):
        i = jcast('int', 0)
        while (i <= 50):
            jprint(jadd(jadd(i, ' : '), Code02_EatGrass.win1(i)), newline=True)
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code02_EatGrass.main([])
