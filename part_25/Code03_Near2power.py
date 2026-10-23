# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 已知n是非负数
# 返回大于等于n的最小的2某次方
# 如果int范围内不存在这样的数，返回整数最小值
class Code03_Near2power:
    __java_fields__ = {}
    @staticmethod
    def near2power(n):
        n = jcast('int', n)
        if (n <= 0):
            return jcast('int', 1)
        n = jcast('int', (n - 1))
        n = jcast('int', jcast('int', (n | jcast('int', jushr(n, 1, 32)))))
        n = jcast('int', jcast('int', (n | jcast('int', jushr(n, 2, 32)))))
        n = jcast('int', jcast('int', (n | jcast('int', jushr(n, 4, 32)))))
        n = jcast('int', jcast('int', (n | jcast('int', jushr(n, 8, 32)))))
        n = jcast('int', jcast('int', (n | jcast('int', jushr(n, 16, 32)))))
        return jcast('int', jcast('int', jadd(n, 1)))

    @staticmethod
    def main(args):
        number = jcast('int', 100)
        jprint(Code03_Near2power.near2power(number), newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code03_Near2power.main([])
