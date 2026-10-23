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

# 利用二维前缀和信息迅速得到二维区域和
# 测试链接 : https://leetcode.cn/problems/range-sum-query-2d-immutable/
class Code01_PrefixSumMatrix:
    __java_fields__ = {}
    class NumMatrix:
        __java_fields__ = {'sum': 'sum'}
        # sum：实例字段，在构造函数中初始化。
        def _java_init_0(self, matrix):
            n = jcast('int', jget(matrix, 'length'))
            m = jcast('int', jget(matrix[0], 'length'))
            self.sum = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(m, 1))])
            a = jcast('int', 1)
            c = jcast('int', 0)
            while (c < n):
                b = jcast('int', 1)
                d = jcast('int', 0)
                while (d < m):
                    jset(self.sum[a], b, matrix[c][d])
                    b = jcast('int', (b + 1))
                    d = jcast('int', (d + 1))
                a = jcast('int', (a + 1))
                c = jcast('int', (c + 1))
            i = jcast('int', 1)
            while (i <= n):
                j = jcast('int', 1)
                while (j <= m):
                    ((_java_obj_1 := self.sum[i]), (_java_key_2 := j), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), jcast('int', (jcast('int', jadd(self.sum[i][jcast('int', (j - 1))], self.sum[jcast('int', (i - 1))][j])) - self.sum[jcast('int', (i - 1))][jcast('int', (j - 1))]))))))[2]
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))

        def sumRegion(self, a, b, c, d):
            a = jcast('int', a)
            b = jcast('int', b)
            c = jcast('int', c)
            d = jcast('int', d)
            c = jcast('int', (c + 1))
            d = jcast('int', (d + 1))
            return jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (self.sum[c][d] - self.sum[c][b])) - self.sum[a][d])), self.sum[a][b])))

        def __init__(self, *args, _java_ctor=None):
            self.sum = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int[][]']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_PrefixSumMatrix.NumMatrix.NumMatrix")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


