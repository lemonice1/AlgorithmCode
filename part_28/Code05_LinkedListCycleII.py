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

# 返回链表的第一个入环节点
# 测试链接 : https://leetcode.cn/problems/linked-list-cycle-ii/
class Code05_LinkedListCycleII:
    __java_fields__ = {}
    # 不要提交这个类
    class ListNode:
        __java_fields__ = {'val': 'val', 'next': 'next'}
        # val：实例字段，在构造函数中初始化。
        # next：实例字段，在构造函数中初始化。
        def __init__(self, *args, _java_ctor=None):
            self.val = jcast('int', 0)
            self.next = None
            if args:
                raise TypeError('This class has a no-argument constructor')


    # 提交如下的方法
    @staticmethod
    def detectCycle(head):
        if (((head == None) or (jget(head, 'next') == None)) or (jget(jget(head, 'next'), 'next') == None)):
            return None
        slow = jget(head, 'next')
        fast = jget(jget(head, 'next'), 'next')
        while (slow != fast):
            if ((jget(fast, 'next') == None) or (jget(jget(fast, 'next'), 'next') == None)):
                return None
            slow = jget(slow, 'next')
            fast = jget(jget(fast, 'next'), 'next')
        fast = head
        while (slow != fast):
            slow = jget(slow, 'next')
            fast = jget(fast, 'next')
        return slow

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


