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

# 归并排序，填函数练习风格
# 测试链接 : https://leetcode.cn/problems/sort-an-array/
class Code02_MergeSort:
    __java_fields__ = {'MAXN': 'MAXN', 'help': 'help'}
    @staticmethod
    def sortArray(nums):
        if (jget(nums, 'length') > 1):
            # mergeSort1为递归方法
            # mergeSort2为非递归方法
            # 用哪个都可以
            # mergeSort1(nums);
            Code02_MergeSort.mergeSort2(nums)
        return nums

    MAXN = 0
    help = None
    # 归并排序递归版
    @staticmethod
    def mergeSort1(arr):
        Code02_MergeSort.sort(arr, 0, jcast('int', (jget(arr, 'length') - 1)))

    @staticmethod
    def sort(arr, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return
        m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code02_MergeSort.sort(arr, l, m)
        Code02_MergeSort.sort(arr, jcast('int', jadd(m, 1)), r)
        Code02_MergeSort.merge(arr, l, m, r)

    # 归并排序非递归版
    @staticmethod
    def mergeSort2(arr):
        n = jcast('int', jget(arr, 'length'))
        l = 0
        m = 0
        r = 0
        step = jcast('int', 1)
        while (step < n):
            try:
                l = jcast('int', 0)
                while (l < n):
                    try:
                        m = jcast('int', jcast('int', (jcast('int', jadd(l, step)) - 1)))
                        if (jcast('int', jadd(m, 1)) >= n):
                            raise JBreak(None)
                        r = jcast('int', jstatic('Math', 'min', jcast('int', (jcast('int', jadd(l, jcast('int', (step << (1 & 31))))) - 1)), jcast('int', (n - 1))))
                        Code02_MergeSort.merge(arr, l, m, r)
                        l = jcast('int', jcast('int', jadd(r, 1)))
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            step = jcast('int', jcast('int', (step << (1 & 31))))

    @staticmethod
    def merge(arr, l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        i = jcast('int', l)
        a = jcast('int', l)
        b = jcast('int', jcast('int', jadd(m, 1)))
        while ((a <= m) and (b <= r)):
            jset(Code02_MergeSort.help, ((_java_old_5 := i), (i := jcast('int', (i + (1)))), _java_old_5)[2], (arr[((_java_old_3 := a), (a := jcast('int', (a + (1)))), _java_old_3)[2]] if (arr[a] <= arr[b]) else arr[((_java_old_4 := b), (b := jcast('int', (b + (1)))), _java_old_4)[2]]))
        while (a <= m):
            jset(Code02_MergeSort.help, ((_java_old_7 := i), (i := jcast('int', (i + (1)))), _java_old_7)[2], arr[((_java_old_6 := a), (a := jcast('int', (a + (1)))), _java_old_6)[2]])
        while (b <= r):
            jset(Code02_MergeSort.help, ((_java_old_9 := i), (i := jcast('int', (i + (1)))), _java_old_9)[2], arr[((_java_old_8 := b), (b := jcast('int', (b + (1)))), _java_old_8)[2]])
        i = jcast('int', l)
        while (i <= r):
            arr[i] = jcast('int', Code02_MergeSort.help[i])
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_MergeSort.MAXN = jcast('int', 50001)
Code02_MergeSort.help = jarray('int', [Code02_MergeSort.MAXN])
