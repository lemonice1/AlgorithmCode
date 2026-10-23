# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

class Complexity:
    __java_fields__ = {}
    # 只用一个循环完成冒泡排序
    # 但这是时间复杂度O(N^2)的！
    @staticmethod
    def bubbleSort(arr):
        if ((arr == None) or (jget(arr, 'length') < 2)):
            return
        n = jcast('int', jget(arr, 'length'))
        end = jcast('int', jcast('int', (n - 1)))
        i = jcast('int', 0)
        while (end > 0):
            if (arr[i] > arr[jcast('int', jadd(i, 1))]):
                Complexity.swap(arr, i, jcast('int', jadd(i, 1)))
            if (i < jcast('int', (end - 1))):
                i = jcast('int', (i + 1))
            else:
                end = jcast('int', (end - 1))
                i = jcast('int', 0)

    @staticmethod
    def swap(arr, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', arr[i])
        arr[i] = jcast('int', arr[j])
        arr[j] = jcast('int', tmp)

    @staticmethod
    def main(args):
        # 随机生成长度为n
        # 值在0~v-1之间
        # 且任意相邻两数不相等的数组
        n = jcast('int', 10)
        v = jcast('int', 4)
        arr1 = jarray('int', [n])
        jset(arr1, 0, jcast('int', (jstatic('Math', 'random') * v)))
        i = jcast('int', 1)
        while (i < n):
            while True:
                jset(arr1, i, jcast('int', (jstatic('Math', 'random') * v)))
                if not ((arr1[i] == arr1[jcast('int', (i - 1))])):
                    break
            i = jcast('int', (i + 1))
        for num in arr1:
            jprint(jadd(num, ' '), newline=False)
        jprint(newline=True)
        jprint('=========', newline=True)
        # 动态数组使用 Python list；ArrayList 接口由 JList 兼容
        # 各个语言中的动态数组的初始大小和实际扩容因子可能会变化，但是均摊都是O(1)
        # 课上用2作为扩容因子只是举例而已
        arr2 = jnew('ArrayList')
        # 0
        jcall(arr2, 'add', 5)
        # 1
        jcall(arr2, 'add', 4)
        # 2
        jcall(arr2, 'add', 9)
        # arr[1]由4改成了6
        jcall(arr2, 'set', 1, 6)
        jprint(jcall(arr2, 'get', 1), newline=True)
        jprint('=========', newline=True)
        arr = jarray('int', [None], [64, 31, 78, 0, 5, 7, 103])
        Complexity.bubbleSort(arr)
        for num in arr:
            jprint(jadd(num, ' '), newline=False)
        jprint(newline=True)
        jprint('=========', newline=True)
        N = jcast('int', 200000)
        start = 0
        end = 0
        jprint('测试开始', newline=True)
        start = jcast('long', jstatic('System', 'currentTimeMillis'))
        i = jcast('int', 1)
        while (i <= N):
            j = jcast('int', i)
            while (j <= N):
                None
                # 这两个嵌套for循环的流程，时间复杂度为O(N * logN)
                # 1/1 + 1/2 + 1/3 + 1/4 + 1/5 + ... + 1/n，也叫"调和级数"，收敛于O(logN)
                # 所以如果一个流程的表达式 : n/1 + n/2 + n/3 + ... + n/n
                # 那么这个流程时间复杂度O(N * logN)
                j = jcast('int', jcast('int', jadd(j, i)))
            i = jcast('int', (i + 1))
        end = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd(jadd('测试结束，运行时间 : ', jcast('long', (end - start))), ' 毫秒'), newline=True)
        jprint('测试开始', newline=True)
        start = jcast('long', jstatic('System', 'currentTimeMillis'))
        i = jcast('int', 1)
        while (i <= N):
            j = jcast('int', i)
            while (j <= N):
                None
                # 这两个嵌套for循环的流程，时间复杂度为O(N^2)
                # 很明显等差数列
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        end = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd(jadd('测试结束，运行时间 : ', jcast('long', (end - start))), ' 毫秒'), newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Complexity.main([])
