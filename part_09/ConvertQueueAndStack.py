# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 用栈实现队列
# 用队列实现栈
class ConvertQueueAndStack:
    __java_fields__ = {}
    # 测试链接 : https://leetcode.cn/problems/implement-queue-using-stacks/
    class MyQueue:
        __java_fields__ = {'in': 'in_', 'out': 'out'}
        # in_：实例字段，在构造函数中初始化。
        # out：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.in_ = jnew('Stack')
            self.out = jnew('Stack')

        # 倒数据
        # 从in栈，把数据倒入out栈
        # 1) out空了，才能倒数据
        # 2) 如果倒数据，in必须倒完
        def inToOut(self):
            if jcall(self.out, 'empty'):
                while (not jcall(self.in_, 'empty')):
                    jcall(self.out, 'push', jcall(self.in_, 'pop'))

        def push(self, x):
            x = jcast('int', x)
            jcall(self.in_, 'push', x)
            self.inToOut()

        def pop(self):
            self.inToOut()
            return jcast('int', jcall(self.out, 'pop'))

        def peek(self):
            self.inToOut()
            return jcast('int', jcall(self.out, 'peek'))

        def empty(self):
            return jcast('boolean', (jcall(self.in_, 'isEmpty') and jcall(self.out, 'isEmpty')))

        def __init__(self, *args, _java_ctor=None):
            self.in_ = None
            self.out = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for ConvertQueueAndStack.MyQueue.MyQueue")


    # 测试链接 : https://leetcode.cn/problems/implement-stack-using-queues/
    class MyStack:
        __java_fields__ = {'queue': 'queue'}
        # queue：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.queue = jnew('LinkedList')

        # O(n)
        def push(self, x):
            x = jcast('int', x)
            n = jcast('int', jcall(self.queue, 'size'))
            jcall(self.queue, 'offer', x)
            i = jcast('int', 0)
            while (i < n):
                jcall(self.queue, 'offer', jcall(self.queue, 'poll'))
                i = jcast('int', (i + 1))

        def pop(self):
            return jcast('int', jcall(self.queue, 'poll'))

        def top(self):
            return jcast('int', jcall(self.queue, 'peek'))

        def empty(self):
            return jcast('boolean', jcall(self.queue, 'isEmpty'))

        def __init__(self, *args, _java_ctor=None):
            self.queue = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for ConvertQueueAndStack.MyStack.MyStack")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


