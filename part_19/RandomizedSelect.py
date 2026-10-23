# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 无序数组中第K大的元素
# 测试链接 : https://leetcode.cn/problems/kth-largest-element-in-an-array/
class RandomizedSelect:
    __java_fields__ = {'first': 'first', 'last': 'last'}
    # 随机选择算法，时间复杂度O(n)
    @staticmethod
    def findKthLargest(nums, k):
        k = jcast('int', k)
        return jcast('int', RandomizedSelect.randomizedSelect(nums, jcast('int', (jget(nums, 'length') - k))))

    # 如果arr排序的话，在i位置的数字是什么
    @staticmethod
    def randomizedSelect(arr, i):
        i = jcast('int', i)
        ans = jcast('int', 0)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (jget(arr, 'length') - 1)))
        while (l <= r):
            try:
                # 随机这一下，常数时间比较大
                # 但只有这一下随机，才能在概率上把时间复杂度收敛到O(n)
                RandomizedSelect.partition(arr, l, r, arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
                # 因为左右两侧只需要走一侧
                # 所以不需要临时变量记录全局的first、last
                # 直接用即可
                if (i < RandomizedSelect.first):
                    r = jcast('int', jcast('int', (RandomizedSelect.first - 1)))
                else:
                    if (i > RandomizedSelect.last):
                        l = jcast('int', jcast('int', jadd(RandomizedSelect.last, 1)))
                    else:
                        ans = jcast('int', arr[i])
                        raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        return jcast('int', ans)

    # 荷兰国旗问题
    first = 0
    last = 0
    @staticmethod
    def partition(arr, l, r, x):
        l = jcast('int', l)
        r = jcast('int', r)
        x = jcast('int', x)
        RandomizedSelect.first = jcast('int', l)
        RandomizedSelect.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= RandomizedSelect.last):
            if (arr[i] == x):
                i = jcast('int', (i + 1))
            else:
                if (arr[i] < x):
                    RandomizedSelect.swap(arr, ((_java_obj_2 := RandomizedSelect), (_java_key_3 := 'first'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))), _java_old_4)[4], ((_java_old_5 := i), (i := jcast('int', (i + (1)))), _java_old_5)[2])
                else:
                    RandomizedSelect.swap(arr, i, ((_java_obj_6 := RandomizedSelect), (_java_key_7 := 'last'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (-1)))), _java_old_8)[4])

    @staticmethod
    def swap(arr, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', arr[i])
        arr[i] = jcast('int', arr[j])
        arr[j] = jcast('int', tmp)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


RandomizedSelect.first = jcast('int', 0)
RandomizedSelect.last = jcast('int', 0)
