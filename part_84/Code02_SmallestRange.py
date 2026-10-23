# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最小区间
# 你有k个非递减排列的整数列表
# 找到一个最小区间，使得k个列表中的每个列表至少有一个数包含在其中
# 测试链接 : https://leetcode.cn/problems/smallest-range-covering-elements-from-k-lists/
class Code02_SmallestRange:
    __java_fields__ = {}
    class Node:
        __java_fields__ = {'v': 'v', 'i': 'i', 'j': 'j'}
        # 值
        # v：实例字段，在构造函数中初始化。
        # 当前值来自哪个数组
        # i：实例字段，在构造函数中初始化。
        # 当前值来自i号数组的什么位置
        # j：实例字段，在构造函数中初始化。
        def _java_init_0(self, a, b, c):
            a = jcast('int', a)
            b = jcast('int', b)
            c = jcast('int', c)
            self.v = jcast('int', a)
            self.i = jcast('int', b)
            self.j = jcast('int', c)

        def __init__(self, *args, _java_ctor=None):
            self.v = jcast('int', 0)
            self.i = jcast('int', 0)
            self.j = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int', 'int', 'int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_SmallestRange.Node.Node")


    # 时间复杂度O(n*logk)
    # n是数字总数，k是数组数量
    @staticmethod
    def smallestRange(nums):
        k = jcast('int', jcall(nums, 'size'))
        # 根据值排序
        # 为什么排序的时候i要参与
        # 因为有序表中比较相等的样本只会保留一个
        # 为了值一样的元素都保留，于是i要参与排序
        # 在有序表中的所有元素i必然都不同
        set = jnew('TreeSet', (lambda a, b: ((jget(a, 'v') - jget(b, 'v')) if (jget(a, 'v') != jget(b, 'v')) else (jget(a, 'i') - jget(b, 'i')))))
        i = jcast('int', 0)
        while (i < k):
            jcall(set, 'add', Code02_SmallestRange.Node(jcall(jcall(nums, 'get', i), 'get', 0), i, 0))
            i = jcast('int', (i + 1))
        # 记录最窄区间的宽度
        r = jcast('int', jget(Integer, 'MAX_VALUE'))
        # 记录最窄区间的开头
        a = jcast('int', 0)
        # 记录最窄区间的结尾
        b = jcast('int', 0)
        max = None
        min = None
        while (jcall(set, 'size') == k):
            # 在有序表中，值最大的记录
            max = jcall(set, 'last')
            # 在有序表中，值最小的记录，并弹出
            min = jcall(set, 'pollFirst')
            if (jcast('int', (jget(max, 'v') - jget(min, 'v'))) < r):
                r = jcast('int', jcast('int', (jget(max, 'v') - jget(min, 'v'))))
                a = jcast('int', jget(min, 'v'))
                b = jcast('int', jget(max, 'v'))
            if (jcast('int', jadd(jget(min, 'j'), 1)) < jcall(jcall(nums, 'get', jget(min, 'i')), 'size')):
                jcall(set, 'add', Code02_SmallestRange.Node(jcall(jcall(nums, 'get', jget(min, 'i')), 'get', jcast('int', jadd(jget(min, 'j'), 1))), jget(min, 'i'), jcast('int', jadd(jget(min, 'j'), 1))))
        return jarray('int', [None], [a, b])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


