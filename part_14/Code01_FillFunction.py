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

# 展示填函数风格的测试方式
# 子矩阵的最大累加和问题，不要求会解题思路，后面的课会讲
# 测试链接 : https://www.nowcoder.com/practice/840eee05dccd4ffd8f9433ce8085946b
class Code01_FillFunction:
    __java_fields__ = {}
    def sumOfSubMatrix(self, mat, n):
        n = jcast('int', n)
        return jcast('int', Code01_FillFunction.maxSumSubmatrix(mat, n, n))

    # 求子矩阵的最大累加和，后面的课会讲
    @staticmethod
    def maxSumSubmatrix(mat, n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        max = jcast('int', jget(Integer, 'MIN_VALUE'))
        i = jcast('int', 0)
        while (i < n):
            # 需要的辅助数组，临时动态生成就可以
            arr = jarray('int', [m])
            j = jcast('int', i)
            while (j < n):
                k = jcast('int', 0)
                while (k < m):
                    arr[k] = jcast('int', jcast('int', jadd(arr[k], mat[j][k])))
                    k = jcast('int', (k + 1))
                max = jcast('int', jstatic('Math', 'max', max, Code01_FillFunction.maxSumSubarray(arr, m)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', max)

    # 求子数组的最大累加和，后面的课会讲
    @staticmethod
    def maxSumSubarray(arr, m):
        m = jcast('int', m)
        max = jcast('int', jget(Integer, 'MIN_VALUE'))
        cur = jcast('int', 0)
        i = jcast('int', 0)
        while (i < m):
            cur = jcast('int', jcast('int', jadd(cur, arr[i])))
            max = jcast('int', jstatic('Math', 'max', max, cur))
            cur = jcast('int', (0 if (cur < 0) else cur))
            i = jcast('int', (i + 1))
        return jcast('int', max)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


