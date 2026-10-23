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

# 线段树范围为1 ~ n时，需要几倍空间才够用？
class HowManySpace:
    __java_fields__ = {}
    # 范围l~r，信息存在独立数组的i位置
    # 返回递归展开的过程中出现的最大编号
    @staticmethod
    def maxi(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            return jcast('int', i)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            return jcast('int', jstatic('Math', 'max', HowManySpace.maxi(l, mid, jcast('int', (i << (1 & 31)))), HowManySpace.maxi(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))

    @staticmethod
    def main(args):
        n = jcast('int', 10000)
        a = jcast('int', 0)
        b = jcast('int', 0)
        t = jcast('double', 0)
        i = jcast('int', 1)
        while (i <= n):
            space = jcast('int', HowManySpace.maxi(1, i, 1))
            times = jcast('double', jdiv(jcast('double', space), jcast('double', i)))
            jprint(jadd(jadd(jadd(jadd(jadd(jadd('范围[1~', i), ']，'), '需要空间'), space), '，倍数='), times), newline=True)
            if (times > t):
                a = jcast('int', i)
                b = jcast('int', space)
                t = jcast('double', times)
            i = jcast('int', (i + 1))
        jprint(jadd(jadd(jadd(jadd(jadd(jadd('其中的最大倍数，范围[1~', a), ']，'), '需要空间'), b), '，倍数='), t), newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    HowManySpace.main([])
