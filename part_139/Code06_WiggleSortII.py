# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 摇摆排序ii(满足全部进阶要求)
# 给定一个数组arr，重新排列数组，确保满足：arr[0] < arr[1] > arr[2] < arr[3] > ...
# 题目保证输入的数组一定有解，要求时间复杂度O(n)，额外空间复杂度O(1)
# 测试链接 : https://leetcode.cn/problems/wiggle-sort-ii/
class Code06_WiggleSortII:
    __java_fields__ = {'first': 'first', 'last': 'last', 'MAXN': 'MAXN', 'start': 'start', 'split': 'split', 'size': 'size'}
    # 最优解
    # 时间复杂度O(n)，额外空间复杂度O(1)
    @staticmethod
    def wiggleSort(arr):
        n = jcast('int', jget(arr, 'length'))
        Code06_WiggleSortII.randomizedSelect(arr, n, jcast('int', jdiv(n, 2)))
        if (jcast('int', (n & 1)) == 0):
            Code06_WiggleSortII.shuffle(arr, 0, jcast('int', (n - 1)))
            Code06_WiggleSortII.reverse(arr, 0, jcast('int', (n - 1)))
        else:
            Code06_WiggleSortII.shuffle(arr, 1, jcast('int', (n - 1)))

    # 随机选择算法，不会去看讲解024
    # 无序数组中找到，如果排序之后，在i位置的数x，顺便把数组调整为
    # 左边是小于x的部分    中间是等于x的部分    右边是大于x的部分
    # 时间复杂度O(n)，额外空间复杂度O(1)
    @staticmethod
    def randomizedSelect(arr, n, i):
        n = jcast('int', n)
        i = jcast('int', i)
        ans = jcast('int', 0)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (n - 1)))
        while (l <= r):
            try:
                Code06_WiggleSortII.partition(arr, l, r, arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
                if (i < Code06_WiggleSortII.first):
                    r = jcast('int', jcast('int', (Code06_WiggleSortII.first - 1)))
                else:
                    if (i > Code06_WiggleSortII.last):
                        l = jcast('int', jcast('int', jadd(Code06_WiggleSortII.last, 1)))
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

    first = 0
    last = 0
    @staticmethod
    def partition(arr, l, r, x):
        l = jcast('int', l)
        r = jcast('int', r)
        x = jcast('int', x)
        Code06_WiggleSortII.first = jcast('int', l)
        Code06_WiggleSortII.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= Code06_WiggleSortII.last):
            if (arr[i] == x):
                i = jcast('int', (i + 1))
            else:
                if (arr[i] < x):
                    Code06_WiggleSortII.swap(arr, ((_java_obj_2 := Code06_WiggleSortII), (_java_key_3 := 'first'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))), _java_old_4)[4], ((_java_old_5 := i), (i := jcast('int', (i + (1)))), _java_old_5)[2])
                else:
                    Code06_WiggleSortII.swap(arr, i, ((_java_obj_6 := Code06_WiggleSortII), (_java_key_7 := 'last'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (-1)))), _java_old_8)[4])

    # 完美洗牌算法
    # 时间复杂度O(n)，额外空间复杂度O(1)
    MAXN = 0
    start = None
    split = None
    size = 0
    @staticmethod
    def shuffle(arr, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        n = jcast('int', jcast('int', jadd(jcast('int', (r - l)), 1)))
        Code06_WiggleSortII.build(n)
        i = jcast('int', Code06_WiggleSortII.size)
        m = 0
        while (n > 0):
            if (Code06_WiggleSortII.split[i] <= n):
                m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
                Code06_WiggleSortII.rotate(arr, jcast('int', jadd(l, jcast('int', jdiv(Code06_WiggleSortII.split[i], 2)))), m, jcast('int', jadd(m, jcast('int', jdiv(Code06_WiggleSortII.split[i], 2)))))
                Code06_WiggleSortII.circle(arr, l, jcast('int', (jcast('int', jadd(l, Code06_WiggleSortII.split[i])) - 1)), i)
                l = jcast('int', jcast('int', jadd(l, Code06_WiggleSortII.split[i])))
                n = jcast('int', jcast('int', (n - Code06_WiggleSortII.split[i])))
            else:
                i = jcast('int', (i - 1))

    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code06_WiggleSortII.size = jcast('int', 0)
        s = jcast('int', 1)
        p = jcast('int', 2)
        while (p <= n):
            jset(Code06_WiggleSortII.start, ((_java_obj_9 := Code06_WiggleSortII), (_java_key_10 := 'size'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))))[3], s)
            Code06_WiggleSortII.split[Code06_WiggleSortII.size] = jcast('int', p)
            s = jcast('int', jcast('int', (s * 3)))
            p = jcast('int', jcast('int', (jcast('int', (s * 3)) - 1)))

    @staticmethod
    def rotate(arr, l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        Code06_WiggleSortII.reverse(arr, l, m)
        Code06_WiggleSortII.reverse(arr, jcast('int', jadd(m, 1)), r)
        Code06_WiggleSortII.reverse(arr, l, r)

    @staticmethod
    def reverse(arr, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        while (l < r):
            Code06_WiggleSortII.swap(arr, ((_java_old_12 := l), (l := jcast('int', (l + (1)))), _java_old_12)[2], ((_java_old_13 := r), (r := jcast('int', (r + (-1)))), _java_old_13)[2])

    @staticmethod
    def swap(arr, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', arr[i])
        arr[i] = jcast('int', arr[j])
        arr[j] = jcast('int', tmp)

    @staticmethod
    def circle(arr, l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        j = jcast('int', 1)
        init = 0
        cur = 0
        next = 0
        curv = 0
        nextv = 0
        while (j <= i):
            init = jcast('int', (cur := jcast('int', (jcast('int', jadd(l, Code06_WiggleSortII.start[j])) - 1))))
            next = jcast('int', Code06_WiggleSortII.to(cur, l, r))
            curv = jcast('int', arr[cur])
            while (next != init):
                nextv = jcast('int', arr[next])
                arr[next] = jcast('int', curv)
                curv = jcast('int', nextv)
                cur = jcast('int', next)
                next = jcast('int', Code06_WiggleSortII.to(cur, l, r))
            arr[init] = jcast('int', curv)
            j = jcast('int', (j + 1))

    @staticmethod
    def to(i, l, r):
        i = jcast('int', i)
        l = jcast('int', l)
        r = jcast('int', r)
        if (i <= jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))):
            return jcast('int', jcast('int', jadd(i, jcast('int', jadd(jcast('int', (i - l)), 1)))))
        else:
            return jcast('int', jcast('int', (i - jcast('int', jadd(jcast('int', (r - i)), 1)))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_WiggleSortII.first = jcast('int', 0)
Code06_WiggleSortII.last = jcast('int', 0)
Code06_WiggleSortII.MAXN = jcast('int', 20)
Code06_WiggleSortII.start = jarray('int', [Code06_WiggleSortII.MAXN])
Code06_WiggleSortII.split = jarray('int', [Code06_WiggleSortII.MAXN])
Code06_WiggleSortII.size = jcast('int', 0)
