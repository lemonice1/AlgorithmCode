# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 有序数组中找<=num的最右位置
class Code03_FindRight:
    __java_fields__ = {}
    # 为了验证
    @staticmethod
    def main(args):
        N = jcast('int', 100)
        V = jcast('int', 1000)
        testTime = jcast('int', 500000)
        jprint('测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTime):
            n = jcast('int', jcast('int', (jstatic('Math', 'random') * N)))
            arr = Code03_FindRight.randomArray(n, V)
            jstatic('Arrays', 'sort', arr)
            num = jcast('int', jcast('int', (jstatic('Math', 'random') * V)))
            if (Code03_FindRight.right(arr, num) != Code03_FindRight.findRight(arr, num)):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    # 为了验证
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        arr = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            jset(arr, i, jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * v)), 1)))
            i = jcast('int', (i + 1))
        return arr

    # 为了验证
    # 保证arr有序，才能用这个方法
    @staticmethod
    def right(arr, num):
        num = jcast('int', num)
        i = jcast('int', jcast('int', (jget(arr, 'length') - 1)))
        while (i >= 0):
            if (arr[i] <= num):
                return jcast('int', i)
            i = jcast('int', (i - 1))
        return jcast('int', jcast('int', (-1)))

    # 保证arr有序，才能用这个方法
    # 有序数组中找<=num的最右位置
    @staticmethod
    def findRight(arr, num):
        num = jcast('int', num)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (jget(arr, 'length') - 1)))
        m = jcast('int', 0)
        ans = jcast('int', jcast('int', (-1)))
        while (l <= r):
            m = jcast('int', jcast('int', jadd(l, jcast('int', (jcast('int', (r - l)) >> (1 & 31))))))
            if (arr[m] <= num):
                ans = jcast('int', m)
                l = jcast('int', jcast('int', jadd(m, 1)))
            else:
                r = jcast('int', jcast('int', (m - 1)))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code03_FindRight.main([])
