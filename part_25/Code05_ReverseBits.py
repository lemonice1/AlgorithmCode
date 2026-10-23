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

# 逆序二进制的状态
# 测试链接 : https://leetcode.cn/problems/reverse-bits/
class Code05_ReverseBits:
    __java_fields__ = {}
    # 逆序二进制的状态
    # 是不是看着头皮发麻啊？代码看着很魔幻吧？别慌
    @staticmethod
    def reverseBits(n):
        n = jcast('int', n)
        n = jcast('int', jcast('int', (jcast('int', jushr(jcast('int', (n & -1431655766)), 1, 32)) | jcast('int', (jcast('int', (n & 1431655765)) << (1 & 31))))))
        n = jcast('int', jcast('int', (jcast('int', jushr(jcast('int', (n & -858993460)), 2, 32)) | jcast('int', (jcast('int', (n & 858993459)) << (2 & 31))))))
        n = jcast('int', jcast('int', (jcast('int', jushr(jcast('int', (n & -252645136)), 4, 32)) | jcast('int', (jcast('int', (n & 252645135)) << (4 & 31))))))
        n = jcast('int', jcast('int', (jcast('int', jushr(jcast('int', (n & -16711936)), 8, 32)) | jcast('int', (jcast('int', (n & 16711935)) << (8 & 31))))))
        n = jcast('int', jcast('int', (jcast('int', jushr(n, 16, 32)) | jcast('int', (n << (16 & 31))))))
        return jcast('int', n)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


