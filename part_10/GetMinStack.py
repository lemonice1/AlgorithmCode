# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最小栈
# 测试链接 : https://leetcode.cn/problems/min-stack/
class GetMinStack:
    __java_fields__ = {}
    # 提交时把类名、构造方法改成MinStack
    class MinStack1:
        __java_fields__ = {'data': 'data', 'min': 'min'}
        # data：实例字段，在构造函数中初始化。
        # min：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.data = jnew('Stack')
            self.min = jnew('Stack')

        def push(self, val):
            val = jcast('int', val)
            jcall(self.data, 'push', val)
            if (jcall(self.min, 'isEmpty') or (val <= jcall(self.min, 'peek'))):
                jcall(self.min, 'push', val)
                # !min.isEmpty() && val > min.peek()
            else:
                jcall(self.min, 'push', jcall(self.min, 'peek'))

        def pop(self):
            jcall(self.data, 'pop')
            jcall(self.min, 'pop')

        def top(self):
            return jcast('int', jcall(self.data, 'peek'))

        def getMin(self):
            return jcast('int', jcall(self.min, 'peek'))

        def __init__(self, *args, _java_ctor=None):
            self.data = None
            self.min = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for GetMinStack.MinStack1.MinStack1")


    # 提交时把类名、构造方法改成MinStack
    class MinStack2:
        __java_fields__ = {'MAXN': 'MAXN', 'data': 'data', 'min': 'min', 'size': 'size'}
        # leetcode的数据在测试时，同时在栈里的数据不超过这个值
        # 这是几次提交实验出来的，哈哈
        # 如果leetcode补测试数据了，超过这个量导致出错，就调大
        # MAXN：实例字段，在构造函数中初始化。
        # data：实例字段，在构造函数中初始化。
        # min：实例字段，在构造函数中初始化。
        # size：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.data = jarray('int', [self.MAXN])
            self.min = jarray('int', [self.MAXN])
            self.size = jcast('int', 0)

        def push(self, val):
            val = jcast('int', val)
            self.data[self.size] = jcast('int', val)
            if ((self.size == 0) or (val <= self.min[jcast('int', (self.size - 1))])):
                self.min[self.size] = jcast('int', val)
            else:
                self.min[self.size] = jcast('int', self.min[jcast('int', (self.size - 1))])
            self.size = jcast('int', (self.size + 1))

        def pop(self):
            self.size = jcast('int', (self.size - 1))

        def top(self):
            return jcast('int', self.data[jcast('int', (self.size - 1))])

        def getMin(self):
            return jcast('int', self.min[jcast('int', (self.size - 1))])

        def __init__(self, *args, _java_ctor=None):
            self.MAXN = jcast('int', 8001)
            self.data = None
            self.min = None
            self.size = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for GetMinStack.MinStack2.MinStack2")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


