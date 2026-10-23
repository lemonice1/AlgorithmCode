# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 随机快速排序，填函数练习风格
# 测试链接 : https://leetcode.cn/problems/sort-an-array/
class Code02_QuickSort:
    __java_fields__ = {'first': 'first', 'last': 'last'}
    @staticmethod
    def sortArray(nums):
        if (jget(nums, 'length') > 1):
            Code02_QuickSort.quickSort2(nums, 0, jcast('int', (jget(nums, 'length') - 1)))
        return nums

    # 随机快速排序经典版(不推荐)
    @staticmethod
    def quickSort1(arr, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        # 随机这一下，常数时间比较大
        # 但只有这一下随机，才能在概率上把快速排序的时间复杂度收敛到O(n * logn)
        x = jcast('int', arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
        mid = jcast('int', Code02_QuickSort.partition1(arr, l, r, x))
        Code02_QuickSort.quickSort1(arr, l, jcast('int', (mid - 1)))
        Code02_QuickSort.quickSort1(arr, jcast('int', jadd(mid, 1)), r)

    # 已知arr[l....r]范围上一定有x这个值
    # 划分数组 <=x放左边，>x放右边，并且确保划分完成后<=x区域的最后一个数字是x
    @staticmethod
    def partition1(arr, l, r, x):
        l = jcast('int', l)
        r = jcast('int', r)
        x = jcast('int', x)
        # a : arr[l....a-1]范围是<=x的区域
        # xi : 记录在<=x的区域上任何一个x的位置，哪一个都可以
        a = jcast('int', l)
        xi = jcast('int', 0)
        i = jcast('int', l)
        while (i <= r):
            if (arr[i] <= x):
                Code02_QuickSort.swap(arr, a, i)
                if (arr[a] == x):
                    xi = jcast('int', a)
                a = jcast('int', (a + 1))
            i = jcast('int', (i + 1))
        Code02_QuickSort.swap(arr, xi, jcast('int', (a - 1)))
        return jcast('int', jcast('int', (a - 1)))

    @staticmethod
    def swap(arr, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', arr[i])
        arr[i] = jcast('int', arr[j])
        arr[j] = jcast('int', tmp)

    # 随机快速排序改进版(推荐)
    @staticmethod
    def quickSort2(arr, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        # 随机这一下，常数时间比较大
        # 但只有这一下随机，才能在概率上把快速排序的时间复杂度收敛到O(n * logn)
        x = jcast('int', arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
        Code02_QuickSort.partition2(arr, l, r, x)
        # 为了防止底层的递归过程覆盖全局变量
        # 这里用临时变量记录first、last
        left = jcast('int', Code02_QuickSort.first)
        right = jcast('int', Code02_QuickSort.last)
        Code02_QuickSort.quickSort2(arr, l, jcast('int', (left - 1)))
        Code02_QuickSort.quickSort2(arr, jcast('int', jadd(right, 1)), r)

    # 荷兰国旗问题
    first = 0
    last = 0
    # 已知arr[l....r]范围上一定有x这个值
    # 划分数组 <x放左边，==x放中间，>x放右边
    # 把全局变量first, last，更新成==x区域的左右边界
    @staticmethod
    def partition2(arr, l, r, x):
        l = jcast('int', l)
        r = jcast('int', r)
        x = jcast('int', x)
        Code02_QuickSort.first = jcast('int', l)
        Code02_QuickSort.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= Code02_QuickSort.last):
            if (arr[i] == x):
                i = jcast('int', (i + 1))
            else:
                if (arr[i] < x):
                    Code02_QuickSort.swap(arr, ((_java_obj_1 := Code02_QuickSort), (_java_key_2 := 'first'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], ((_java_old_4 := i), (i := jcast('int', (i + (1)))), _java_old_4)[2])
                else:
                    Code02_QuickSort.swap(arr, i, ((_java_obj_5 := Code02_QuickSort), (_java_key_6 := 'last'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_QuickSort.first = jcast('int', 0)
Code02_QuickSort.last = jcast('int', 0)
