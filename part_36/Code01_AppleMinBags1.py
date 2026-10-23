# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 买苹果使用最少袋子
# 本题已经找到了在线测试，就是本节课Code01_AppleMinBags2文件
# 有装下8个苹果的袋子、装下6个苹果的袋子，一定要保证买苹果时所有使用的袋子都装满
# 对于无法装满所有袋子的方案不予考虑，给定n个苹果，返回至少要多少个袋子
# 如果不存在每个袋子都装满的方案返回-1
class Code01_AppleMinBags1:
    __java_fields__ = {}
    @staticmethod
    def bags1(apple):
        apple = jcast('int', apple)
        ans = jcast('int', Code01_AppleMinBags1.f(apple))
        return jcast('int', (jcast('int', (-1)) if (ans == jget(Integer, 'MAX_VALUE')) else ans))

    # 当前还有rest个苹果，使用的每个袋子必须装满，返回至少几个袋子
    @staticmethod
    def f(rest):
        rest = jcast('int', rest)
        if (rest < 0):
            return jcast('int', jget(Integer, 'MAX_VALUE'))
        if (rest == 0):
            return jcast('int', 0)
        # 使用8规格的袋子，剩余的苹果还需要几个袋子，有可能返回无效解
        p1 = jcast('int', Code01_AppleMinBags1.f(jcast('int', (rest - 8))))
        # 使用6规格的袋子，剩余的苹果还需要几个袋子，有可能返回无效解
        p2 = jcast('int', Code01_AppleMinBags1.f(jcast('int', (rest - 6))))
        p1 = jcast('int', jcast('int', jadd(p1, (1 if (p1 != jget(Integer, 'MAX_VALUE')) else 0))))
        p2 = jcast('int', jcast('int', jadd(p2, (1 if (p2 != jget(Integer, 'MAX_VALUE')) else 0))))
        return jcast('int', jstatic('Math', 'min', p1, p2))

    @staticmethod
    def bags2(apple):
        apple = jcast('int', apple)
        if (jcast('int', (apple & 1)) != 0):
            return jcast('int', jcast('int', (-1)))
        if (apple < 18):
            if (apple == 0):
                return jcast('int', 0)
            if ((apple == 6) or (apple == 8)):
                return jcast('int', 1)
            if (((apple == 12) or (apple == 14)) or (apple == 16)):
                return jcast('int', 2)
            return jcast('int', jcast('int', (-1)))
        return jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (apple - 18)), 8)), 3)))

    @staticmethod
    def main(args):
        apple = jcast('int', 0)
        while (apple < 100):
            jprint(jadd(jadd(apple, ' : '), Code01_AppleMinBags1.bags1(apple)), newline=True)
            apple = jcast('int', (apple + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code01_AppleMinBags1.main([])
