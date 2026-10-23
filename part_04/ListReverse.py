# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 按值传递、按引用传递
# 从堆栈角度解释链表节点
# 以堆栈视角来看链表反转
class ListReverse:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        # int、long、byte、short
        # char、float、double、boolean
        # 还有String
        # 都是按值传递
        a = jcast('int', 10)
        ListReverse.f(a)
        jprint(a, newline=True)
        # 其他类型按引用传递
        # 比如下面的Number是自定义的类
        b = ListReverse.Number(5, _java_ctor=0)
        ListReverse.g1(b)
        jprint(jget(b, 'val'), newline=True)
        ListReverse.g2(b)
        jprint(jget(b, 'val'), newline=True)
        # 比如下面的一维数组
        c = jarray('int', [None], [1, 2, 3, 4])
        ListReverse.g3(c)
        jprint(c[0], newline=True)
        ListReverse.g4(c)
        jprint(c[0], newline=True)

    @staticmethod
    def f(a):
        a = jcast('int', a)
        a = jcast('int', 0)

    class Number:
        __java_fields__ = {'val': 'val'}
        # val：实例字段，在构造函数中初始化。
        def _java_init_0(self, v):
            v = jcast('int', v)
            self.val = jcast('int', v)

        def __init__(self, *args, _java_ctor=None):
            self.val = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for ListReverse.Number.Number")


    @staticmethod
    def g1(b):
        b = None

    @staticmethod
    def g2(b):
        b.val = jcast('int', 6)

    @staticmethod
    def g3(c):
        c = None

    @staticmethod
    def g4(c):
        c[0] = jcast('int', 100)

    # 单链表节点
    class ListNode:
        __java_fields__ = {'val': 'val', 'next': 'next'}
        # val：实例字段，在构造函数中初始化。
        # next：实例字段，在构造函数中初始化。
        def _java_init_0(self, val):
            val = jcast('int', val)
            self.val = jcast('int', val)

        def _java_init_1(self, val, next):
            val = jcast('int', val)
            self.val = jcast('int', val)
            self.next = next

        def __init__(self, *args, _java_ctor=None):
            self.val = jcast('int', 0)
            self.next = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int'], ['int', 'ListNode']], [False, False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            if _java_choice == 1:
                return self._java_init_1(*args)
            raise TypeError("No matching overload for ListReverse.ListNode.ListNode")


    # 反转单链表测试链接 : https://leetcode.cn/problems/reverse-linked-list/
    class Solution:
        __java_fields__ = {}
        @staticmethod
        def reverseList(head):
            pre = None
            next = None
            while (head != None):
                next = jget(head, 'next')
                head.next = pre
                pre = head
                head = next
            return pre

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    # 双链表节点
    class DoubleListNode:
        __java_fields__ = {'value': 'value', 'last': 'last', 'next': 'next'}
        # value：实例字段，在构造函数中初始化。
        # last：实例字段，在构造函数中初始化。
        # next：实例字段，在构造函数中初始化。
        def _java_init_0(self, v):
            v = jcast('int', v)
            self.value = jcast('int', v)

        def __init__(self, *args, _java_ctor=None):
            self.value = jcast('int', 0)
            self.last = None
            self.next = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for ListReverse.DoubleListNode.DoubleListNode")


    # 反转双链表
    # 没有找到测试链接
    # 如下方法是对的
    @staticmethod
    def reverseDoubleList(head):
        pre = None
        next = None
        while (head != None):
            next = jget(head, 'next')
            head.next = pre
            head.last = next
            pre = head
            head = next
        return pre

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    ListReverse.main([])
