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

# 有序数组中是否存在一个数字
class Code01_FindNumber:
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
            arr = Code01_FindNumber.randomArray(n, V)
            jstatic('Arrays', 'sort', arr)
            num = jcast('int', jcast('int', (jstatic('Math', 'random') * V)))
            if (Code01_FindNumber.right(arr, num) != Code01_FindNumber.exist(arr, num)):
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
    def right(sortedArr, num):
        num = jcast('int', num)
        for cur in sortedArr:
            if (cur == num):
                return jcast('boolean', True)
        return jcast('boolean', False)

    # 保证arr有序，才能用这个方法
    @staticmethod
    def exist(arr, num):
        num = jcast('int', num)
        if ((arr == None) or (jget(arr, 'length') == 0)):
            return jcast('boolean', False)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (jget(arr, 'length') - 1)))
        m = jcast('int', 0)
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (arr[m] == num):
                return jcast('boolean', True)
            else:
                if (arr[m] > num):
                    r = jcast('int', jcast('int', (m - 1)))
                else:
                    l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('boolean', False)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code01_FindNumber.main([])
