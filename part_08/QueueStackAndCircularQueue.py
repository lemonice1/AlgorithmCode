# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

class QueueStackAndCircularQueue:
    __java_fields__ = {}
    # 使用 Python 对应容器，兼容层保留原容器接口
    # 其实内部就是双向链表，常数操作慢
    class Queue1:
        __java_fields__ = {'queue': 'queue'}
        # LinkedList 接口由基于 collections.deque 的 JDeque 兼容
        # 单向链表就足够了
        # queue：实例字段，在构造函数中初始化。
        # 调用任何方法之前，先调用这个方法来判断队列内是否有东西
        def isEmpty(self):
            return jcast('boolean', jcall(self.queue, 'isEmpty'))

        # 向队列中加入num，加到尾巴
        def offer(self, num):
            num = jcast('int', num)
            jcall(self.queue, 'offer', num)

        # 从队列拿，从头拿
        def poll(self):
            return jcast('int', jcall(self.queue, 'poll'))

        # 返回队列头的元素但是不弹出
        def peek(self):
            return jcast('int', jcall(self.queue, 'peek'))

        # 返回目前队列里有几个数
        def size(self):
            return jcast('int', jcall(self.queue, 'size'))

        def __init__(self, *args, _java_ctor=None):
            self.queue = jnew('LinkedList')
            if args:
                raise TypeError('This class has a no-argument constructor')


    # 实际刷题时更常见的写法，常数时间好
    # 如果可以确定加入操作的总次数不超过n，那么可以用
    # 一般笔试、面试都会有一个明确数据量，所以这是最常用的方式
    class Queue2:
        __java_fields__ = {'queue': 'queue', 'l': 'l', 'r': 'r'}
        # queue：实例字段，在构造函数中初始化。
        # l：实例字段，在构造函数中初始化。
        # r：实例字段，在构造函数中初始化。
        # 加入操作的总次数上限是多少，一定要明确
        def _java_init_0(self, n):
            n = jcast('int', n)
            self.queue = jarray('int', [n])
            self.l = jcast('int', 0)
            self.r = jcast('int', 0)

        # 调用任何方法之前，先调用这个方法来判断队列内是否有东西
        def isEmpty(self):
            return jcast('boolean', (self.l == self.r))

        def offer(self, num):
            num = jcast('int', num)
            jset(self.queue, ((_java_obj_1 := self), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], num)

        def poll(self):
            return jcast('int', self.queue[((_java_obj_4 := self), (_java_key_5 := 'l'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]])

        # ?
        # l...r-1 r
        # [l..r)
        def head(self):
            return jcast('int', self.queue[self.l])

        def tail(self):
            return jcast('int', self.queue[jcast('int', (self.r - 1))])

        def size(self):
            return jcast('int', jcast('int', (self.r - self.l)))

        def __init__(self, *args, _java_ctor=None):
            self.queue = None
            self.l = jcast('int', 0)
            self.r = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for QueueStackAndCircularQueue.Queue2.Queue2")


    # 使用 Python 对应容器，兼容层保留原容器接口
    # 其实就是动态数组，不过常数时间并不好
    class Stack1:
        __java_fields__ = {'stack': 'stack'}
        # stack：实例字段，在构造函数中初始化。
        # 调用任何方法之前，先调用这个方法来判断栈内是否有东西
        def isEmpty(self):
            return jcast('boolean', jcall(self.stack, 'isEmpty'))

        def push(self, num):
            num = jcast('int', num)
            jcall(self.stack, 'push', num)

        def pop(self):
            return jcast('int', jcall(self.stack, 'pop'))

        def peek(self):
            return jcast('int', jcall(self.stack, 'peek'))

        def size(self):
            return jcast('int', jcall(self.stack, 'size'))

        def __init__(self, *args, _java_ctor=None):
            self.stack = jnew('Stack')
            if args:
                raise TypeError('This class has a no-argument constructor')


    # 实际刷题时更常见的写法，常数时间好
    # 如果可以保证同时在栈里的元素个数不会超过n，那么可以用
    # 也就是发生弹出操作之后，空间可以复用
    # 一般笔试、面试都会有一个明确数据量，所以这是最常用的方式
    class Stack2:
        __java_fields__ = {'stack': 'stack', 'size': 'size_data'}
        # stack：实例字段，在构造函数中初始化。
        # size：实例字段，在构造函数中初始化。
        # 同时在栈里的元素个数不会超过n
        def _java_init_0(self, n):
            n = jcast('int', n)
            self.stack = jarray('int', [n])
            self.size_data = jcast('int', 0)

        # 调用任何方法之前，先调用这个方法来判断栈内是否有东西
        def isEmpty(self):
            return jcast('boolean', (self.size_data == 0))

        def push(self, num):
            num = jcast('int', num)
            jset(self.stack, ((_java_obj_7 := self), (_java_key_8 := 'size_data'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4], num)

        def pop(self):
            return jcast('int', self.stack[((_java_obj_10 := self), (_java_key_11 := 'size_data'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))))[3]])

        def peek(self):
            return jcast('int', self.stack[jcast('int', (self.size_data - 1))])

        def size(self):
            return jcast('int', self.size_data)

        def __init__(self, *args, _java_ctor=None):
            self.stack = None
            self.size_data = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for QueueStackAndCircularQueue.Stack2.Stack2")


    # 设计循环队列
    # 测试链接 : https://leetcode.cn/problems/design-circular-queue/
    class MyCircularQueue:
        __java_fields__ = {'queue': 'queue', 'l': 'l', 'r': 'r', 'size': 'size', 'limit': 'limit'}
        # queue：实例字段，在构造函数中初始化。
        # l：实例字段，在构造函数中初始化。
        # r：实例字段，在构造函数中初始化。
        # size：实例字段，在构造函数中初始化。
        # limit：实例字段，在构造函数中初始化。
        # 同时在队列里的数字个数，不要超过k
        def _java_init_0(self, k):
            k = jcast('int', k)
            self.queue = jarray('int', [k])
            self.l = jcast('int', jset(self, 'r', jset(self, 'size', 0)))
            self.limit = jcast('int', k)

        # 如果队列满了，什么也不做，返回false
        # 如果队列没满，加入value，返回true
        def enQueue(self, value):
            value = jcast('int', value)
            if self.isFull():
                return jcast('boolean', False)
            else:
                self.queue[self.r] = jcast('int', value)
                # r++, 结束了，跳回0
                self.r = jcast('int', (0 if (self.r == jcast('int', (self.limit - 1))) else jcast('int', jadd(self.r, 1))))
                self.size = jcast('int', (self.size + 1))
                return jcast('boolean', True)

        # 如果队列空了，什么也不做，返回false
        # 如果队列没空，弹出头部的数字，返回true
        def deQueue(self):
            if self.isEmpty():
                return jcast('boolean', False)
            else:
                # l++, 结束了，跳回0
                self.l = jcast('int', (0 if (self.l == jcast('int', (self.limit - 1))) else jcast('int', jadd(self.l, 1))))
                self.size = jcast('int', (self.size - 1))
                return jcast('boolean', True)

        # 返回队列头部的数字（不弹出），如果没有数返回-1
        def Front(self):
            if self.isEmpty():
                return jcast('int', jcast('int', (-1)))
            else:
                return jcast('int', self.queue[self.l])

        def Rear(self):
            if self.isEmpty():
                return jcast('int', jcast('int', (-1)))
            else:
                last = jcast('int', (jcast('int', (self.limit - 1)) if (self.r == 0) else jcast('int', (self.r - 1))))
                return jcast('int', self.queue[last])

        def isEmpty(self):
            return jcast('boolean', (self.size == 0))

        def isFull(self):
            return jcast('boolean', (self.size == self.limit))

        def __init__(self, *args, _java_ctor=None):
            self.queue = None
            self.l = jcast('int', 0)
            self.r = jcast('int', 0)
            self.size = jcast('int', 0)
            self.limit = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for QueueStackAndCircularQueue.MyCircularQueue.MyCircularQueue")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


