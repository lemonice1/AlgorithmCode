# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 插入、删除和获取随机元素O(1)时间的结构
class Code03_InsertDeleteRandom:
    __java_fields__ = {}
    # 测试链接 : https://leetcode.cn/problems/insert-delete-getrandom-o1/
    class RandomizedSet:
        __java_fields__ = {'map': 'map', 'arr': 'arr'}
        # map：实例字段，在构造函数中初始化。
        # arr：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.map = jnew('HashMap')
            self.arr = jnew('ArrayList')

        def insert(self, val):
            val = jcast('int', val)
            if jcall(self.map, 'containsKey', val):
                return jcast('boolean', False)
            jcall(self.map, 'put', val, jcall(self.arr, 'size'))
            jcall(self.arr, 'add', val)
            return jcast('boolean', True)

        def remove(self, val):
            val = jcast('int', val)
            if (not jcall(self.map, 'containsKey', val)):
                return jcast('boolean', False)
            valIndex = jcast('int', jcall(self.map, 'get', val))
            endValue = jcast('int', jcall(self.arr, 'get', jcast('int', (jcall(self.arr, 'size') - 1))))
            jcall(self.map, 'put', endValue, valIndex)
            jcall(self.arr, 'set', valIndex, endValue)
            jcall(self.map, 'remove', val)
            jcall(self.arr, 'remove', jcast('int', (jcall(self.arr, 'size') - 1)))
            return jcast('boolean', True)

        def getRandom(self):
            return jcast('int', jcall(self.arr, 'get', jcast('int', (jstatic('Math', 'random') * jcall(self.arr, 'size')))))

        def __init__(self, *args, _java_ctor=None):
            self.map = None
            self.arr = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code03_InsertDeleteRandom.RandomizedSet.RandomizedSet")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


