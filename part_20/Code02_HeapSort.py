# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 堆结构和堆排序，填函数练习风格
# 测试链接 : https://leetcode.cn/problems/sort-an-array/
class Code02_HeapSort:
    __java_fields__ = {}
    @staticmethod
    def sortArray(nums):
        if (jget(nums, 'length') > 1):
            # heapSort1为从顶到底建堆然后排序
            # heapSort2为从底到顶建堆然后排序
            # 用哪个都可以
            # heapSort1(nums);
            Code02_HeapSort.heapSort2(nums)
        return nums

    # i位置的数，向上调整大根堆
    # arr[i] = x，x是新来的！往上看，直到不比父亲大，或者来到0位置(顶)
    @staticmethod
    def heapInsert(arr, i):
        i = jcast('int', i)
        while (arr[i] > arr[jcast('int', jdiv(jcast('int', (i - 1)), 2))]):
            Code02_HeapSort.swap(arr, i, jcast('int', jdiv(jcast('int', (i - 1)), 2)))
            i = jcast('int', jcast('int', jdiv(jcast('int', (i - 1)), 2)))

    # i位置的数，变小了，又想维持大根堆结构
    # 向下调整大根堆
    # 当前堆的大小为size
    @staticmethod
    def heapify(arr, i, size):
        i = jcast('int', i)
        size = jcast('int', size)
        l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
        while (l < size):
            try:
                # 有左孩子，l
                # 右孩子，l+1
                # 评选，最强的孩子，是哪个下标的孩子
                best = jcast('int', (jcast('int', jadd(l, 1)) if ((jcast('int', jadd(l, 1)) < size) and (arr[jcast('int', jadd(l, 1))] > arr[l])) else l))
                # 上面已经评选了最强的孩子，接下来，当前的数和最强的孩子之前，最强下标是谁
                best = jcast('int', (best if (arr[best] > arr[i]) else i))
                if (best == i):
                    raise JBreak(None)
                Code02_HeapSort.swap(arr, best, i)
                i = jcast('int', best)
                l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break

    @staticmethod
    def swap(arr, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', arr[i])
        arr[i] = jcast('int', arr[j])
        arr[j] = jcast('int', tmp)

    # 从顶到底建立大根堆，O(n * logn)
    # 依次弹出堆内最大值并排好序，O(n * logn)
    # 整体时间复杂度O(n * logn)
    @staticmethod
    def heapSort1(arr):
        n = jcast('int', jget(arr, 'length'))
        i = jcast('int', 0)
        while (i < n):
            Code02_HeapSort.heapInsert(arr, i)
            i = jcast('int', (i + 1))
        size = jcast('int', n)
        while (size > 1):
            Code02_HeapSort.swap(arr, 0, (size := jcast('int', (size + (-1)))))
            Code02_HeapSort.heapify(arr, 0, size)

    # 从底到顶建立大根堆，O(n)
    # 依次弹出堆内最大值并排好序，O(n * logn)
    # 整体时间复杂度O(n * logn)
    @staticmethod
    def heapSort2(arr):
        n = jcast('int', jget(arr, 'length'))
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            Code02_HeapSort.heapify(arr, i, n)
            i = jcast('int', (i - 1))
        size = jcast('int', n)
        while (size > 1):
            Code02_HeapSort.swap(arr, 0, (size := jcast('int', (size + (-1)))))
            Code02_HeapSort.heapify(arr, 0, size)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


