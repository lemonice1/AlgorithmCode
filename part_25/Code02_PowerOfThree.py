# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 判断一个整数是不是3的幂
# 测试链接 : https://leetcode.cn/problems/power-of-three/
class Code02_PowerOfThree:
    __java_fields__ = {}
    # 如果一个数字是3的某次幂，那么这个数一定只含有3这个质数因子
    # 1162261467是int型范围内，最大的3的幂，它是3的19次方
    # 这个1162261467只含有3这个质数因子，如果n也是只含有3这个质数因子，那么
    # 1162261467 % n == 0
    # 反之如果1162261467 % n != 0 说明n一定含有其他因子
    @staticmethod
    def isPowerOfThree(n):
        n = jcast('int', n)
        return jcast('boolean', ((n > 0) and (jcast('int', jmod(1162261467, n)) == 0)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


