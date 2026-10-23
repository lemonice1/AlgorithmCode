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

# 将两个升序链表合并为一个新的 升序 链表并返回
# 新链表是通过拼接给定的两个链表的所有节点组成的
# 测试链接 : https://leetcode.cn/problems/merge-two-sorted-lists/
class MergeTwoLists:
    __java_fields__ = {}
    # 不要提交这个类
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
            raise TypeError("No matching overload for MergeTwoLists.ListNode.ListNode")


    class Solution:
        __java_fields__ = {}
        @staticmethod
        def mergeTwoLists(head1, head2):
            if ((head1 == None) or (head2 == None)):
                return (head2 if (head1 == None) else head1)
            head = (head1 if (jget(head1, 'val') <= jget(head2, 'val')) else head2)
            cur1 = jget(head, 'next')
            cur2 = (head2 if (head == head1) else head1)
            pre = head
            while ((cur1 != None) and (cur2 != None)):
                if (jget(cur1, 'val') <= jget(cur2, 'val')):
                    pre.next = cur1
                    cur1 = jget(cur1, 'next')
                else:
                    pre.next = cur2
                    cur2 = jget(cur2, 'next')
                pre = jget(pre, 'next')
            pre.next = (cur1 if (cur1 != None) else cur2)
            return head

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


