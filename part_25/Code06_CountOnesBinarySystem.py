# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 返回n的二进制中有几个1
# 两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
# 给你两个整数 x 和 y，计算并返回它们之间的汉明距离
# 测试链接 : https://leetcode.cn/problems/hamming-distance/
class Code06_CountOnesBinarySystem:
    __java_fields__ = {}
    @staticmethod
    def hammingDistance(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('int', Code06_CountOnesBinarySystem.cntOnes(jcast('int', (x ^ y))))

    # 返回n的二进制中有几个1
    # 这个实现脑洞太大了
    @staticmethod
    def cntOnes(n):
        n = jcast('int', n)
        n = jcast('int', jcast('int', jadd(jcast('int', (n & 1431655765)), jcast('int', (jcast('int', jushr(n, 1, 32)) & 1431655765)))))
        n = jcast('int', jcast('int', jadd(jcast('int', (n & 858993459)), jcast('int', (jcast('int', jushr(n, 2, 32)) & 858993459)))))
        n = jcast('int', jcast('int', jadd(jcast('int', (n & 252645135)), jcast('int', (jcast('int', jushr(n, 4, 32)) & 252645135)))))
        n = jcast('int', jcast('int', jadd(jcast('int', (n & 16711935)), jcast('int', (jcast('int', jushr(n, 8, 32)) & 16711935)))))
        n = jcast('int', jcast('int', jadd(jcast('int', (n & 65535)), jcast('int', (jcast('int', jushr(n, 16, 32)) & 65535)))))
        return jcast('int', n)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


