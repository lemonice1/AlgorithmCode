# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 插入、删除和获取随机元素O(1)时间且允许有重复数字的结构
class Code04_InsertDeleteRandomDuplicatesAllowed:
    __java_fields__ = {}
    # 测试链接 :
    # https://leetcode.cn/problems/insert-delete-getrandom-o1-duplicates-allowed/
    class RandomizedCollection:
        __java_fields__ = {'map': 'map', 'arr': 'arr'}
        # map：实例字段，在构造函数中初始化。
        # arr：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.map = jnew('HashMap')
            self.arr = jnew('ArrayList')

        def insert(self, val):
            val = jcast('int', val)
            jcall(self.arr, 'add', val)
            set = jcall(self.map, 'getOrDefault', val, jnew('HashSet'))
            jcall(set, 'add', jcast('int', (jcall(self.arr, 'size') - 1)))
            jcall(self.map, 'put', val, set)
            return jcast('boolean', (jcall(set, 'size') == 1))

        def remove(self, val):
            val = jcast('int', val)
            if (not jcall(self.map, 'containsKey', val)):
                return jcast('boolean', False)
            valSet = jcall(self.map, 'get', val)
            valAnyIndex = jcast('int', jcall(jcall(valSet, 'iterator'), 'next'))
            endValue = jcast('int', jcall(self.arr, 'get', jcast('int', (jcall(self.arr, 'size') - 1))))
            if (val == endValue):
                jcall(valSet, 'remove', jcast('int', (jcall(self.arr, 'size') - 1)))
            else:
                endValueSet = jcall(self.map, 'get', endValue)
                jcall(endValueSet, 'add', valAnyIndex)
                jcall(self.arr, 'set', valAnyIndex, endValue)
                jcall(endValueSet, 'remove', jcast('int', (jcall(self.arr, 'size') - 1)))
                jcall(valSet, 'remove', valAnyIndex)
            jcall(self.arr, 'remove', jcast('int', (jcall(self.arr, 'size') - 1)))
            if jcall(valSet, 'isEmpty'):
                jcall(self.map, 'remove', val)
            return jcast('boolean', True)

        def getRandom(self):
            return jcast('int', jcall(self.arr, 'get', jcast('int', (jstatic('Math', 'random') * jcall(self.arr, 'size')))))

        def __init__(self, *args, _java_ctor=None):
            self.map = None
            self.arr = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_InsertDeleteRandomDuplicatesAllowed.RandomizedCollection.RandomizedCollection")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


