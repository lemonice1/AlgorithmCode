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

# 设计循环双端队列
# 测试链接 : https://leetcode.cn/problems/design-circular-deque/
class CircularDeque:
    __java_fields__ = {}
    # 提交时把类名、构造方法改成 : MyCircularDeque
    # 其实内部就是双向链表
    # 常数操作慢，但是leetcode数据量太小了，所以看不出劣势
    class MyCircularDeque1:
        __java_fields__ = {'deque': 'deque', 'size': 'size', 'limit': 'limit'}
        # deque：实例字段，在构造函数中初始化。
        # size：实例字段，在构造函数中初始化。
        # limit：实例字段，在构造函数中初始化。
        def _java_init_0(self, k):
            k = jcast('int', k)
            self.size = jcast('int', 0)
            self.limit = jcast('int', k)

        def insertFront(self, value):
            value = jcast('int', value)
            if self.isFull():
                return jcast('boolean', False)
            else:
                jcall(self.deque, 'offerFirst', value)
                self.size = jcast('int', (self.size + 1))
                return jcast('boolean', True)

        def insertLast(self, value):
            value = jcast('int', value)
            if self.isFull():
                return jcast('boolean', False)
            else:
                jcall(self.deque, 'offerLast', value)
                self.size = jcast('int', (self.size + 1))
                return jcast('boolean', True)

        def deleteFront(self):
            if self.isEmpty():
                return jcast('boolean', False)
            else:
                self.size = jcast('int', (self.size - 1))
                jcall(self.deque, 'pollFirst')
                return jcast('boolean', True)

        def deleteLast(self):
            if self.isEmpty():
                return jcast('boolean', False)
            else:
                self.size = jcast('int', (self.size - 1))
                jcall(self.deque, 'pollLast')
                return jcast('boolean', True)

        def getFront(self):
            if self.isEmpty():
                return jcast('int', jcast('int', (-1)))
            else:
                return jcast('int', jcall(self.deque, 'peekFirst'))

        def getRear(self):
            if self.isEmpty():
                return jcast('int', jcast('int', (-1)))
            else:
                return jcast('int', jcall(self.deque, 'peekLast'))

        def isEmpty(self):
            return jcast('boolean', (self.size == 0))

        def isFull(self):
            return jcast('boolean', (self.size == self.limit))

        def __init__(self, *args, _java_ctor=None):
            self.deque = jnew('LinkedList')
            self.size = jcast('int', 0)
            self.limit = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for CircularDeque.MyCircularDeque1.MyCircularDeque1")


    # 提交时把类名、构造方法改成 : MyCircularDeque
    # 自己用数组实现，常数操作快，但是leetcode数据量太小了，看不出优势
    class MyCircularDeque2:
        __java_fields__ = {'deque': 'deque', 'l': 'l', 'r': 'r', 'size': 'size', 'limit': 'limit'}
        # deque：实例字段，在构造函数中初始化。
        # l：实例字段，在构造函数中初始化。
        # r：实例字段，在构造函数中初始化。
        # size：实例字段，在构造函数中初始化。
        # limit：实例字段，在构造函数中初始化。
        def _java_init_0(self, k):
            k = jcast('int', k)
            self.deque = jarray('int', [k])
            self.l = jcast('int', jset(self, 'r', jset(self, 'size', 0)))
            self.limit = jcast('int', k)

        def insertFront(self, value):
            value = jcast('int', value)
            if self.isFull():
                return jcast('boolean', False)
            else:
                if self.isEmpty():
                    self.l = jcast('int', jset(self, 'r', 0))
                    self.deque[0] = jcast('int', value)
                else:
                    self.l = jcast('int', (jcast('int', (self.limit - 1)) if (self.l == 0) else jcast('int', (self.l - 1))))
                    self.deque[self.l] = jcast('int', value)
                self.size = jcast('int', (self.size + 1))
                return jcast('boolean', True)

        def insertLast(self, value):
            value = jcast('int', value)
            if self.isFull():
                return jcast('boolean', False)
            else:
                if self.isEmpty():
                    self.l = jcast('int', jset(self, 'r', 0))
                    self.deque[0] = jcast('int', value)
                else:
                    self.r = jcast('int', (0 if (self.r == jcast('int', (self.limit - 1))) else jcast('int', jadd(self.r, 1))))
                    self.deque[self.r] = jcast('int', value)
                self.size = jcast('int', (self.size + 1))
                return jcast('boolean', True)

        def deleteFront(self):
            if self.isEmpty():
                return jcast('boolean', False)
            else:
                self.l = jcast('int', (0 if (self.l == jcast('int', (self.limit - 1))) else jcast('int', jadd(self.l, 1))))
                self.size = jcast('int', (self.size - 1))
                return jcast('boolean', True)

        def deleteLast(self):
            if self.isEmpty():
                return jcast('boolean', False)
            else:
                self.r = jcast('int', (jcast('int', (self.limit - 1)) if (self.r == 0) else jcast('int', (self.r - 1))))
                self.size = jcast('int', (self.size - 1))
                return jcast('boolean', True)

        def getFront(self):
            if self.isEmpty():
                return jcast('int', jcast('int', (-1)))
            else:
                return jcast('int', self.deque[self.l])

        def getRear(self):
            if self.isEmpty():
                return jcast('int', jcast('int', (-1)))
            else:
                return jcast('int', self.deque[self.r])

        def isEmpty(self):
            return jcast('boolean', (self.size == 0))

        def isFull(self):
            return jcast('boolean', (self.size == self.limit))

        def __init__(self, *args, _java_ctor=None):
            self.deque = None
            self.l = jcast('int', 0)
            self.r = jcast('int', 0)
            self.size = jcast('int', 0)
            self.limit = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for CircularDeque.MyCircularDeque2.MyCircularDeque2")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


