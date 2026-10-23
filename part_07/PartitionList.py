# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 给你一个链表的头节点 head 和一个特定值 x
# 请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
# 你应当 保留 两个分区中每个节点的初始相对位置
# 测试链接 : https://leetcode.cn/problems/partition-list/
class PartitionList:
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
            raise TypeError("No matching overload for PartitionList.ListNode.ListNode")


    class Solution:
        __java_fields__ = {}
        @staticmethod
        def partition(head, x):
            x = jcast('int', x)
            # < x的区域
            leftHead = None
            leftTail = None
            # >=x的区域
            rightHead = None
            rightTail = None
            next = None
            while (head != None):
                next = jget(head, 'next')
                head.next = None
                if (jget(head, 'val') < x):
                    if (leftHead == None):
                        leftHead = head
                    else:
                        leftTail.next = head
                    leftTail = head
                else:
                    if (rightHead == None):
                        rightHead = head
                    else:
                        rightTail.next = head
                    rightTail = head
                head = next
            if (leftHead == None):
                return rightHead
            # < x的区域有内容！
            leftTail.next = rightHead
            return leftHead

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


