# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 给你两个 非空 的链表，表示两个非负的整数
# 它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头
# 测试链接：https://leetcode.cn/problems/add-two-numbers/
class AddTwoNumbers:
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
            raise TypeError("No matching overload for AddTwoNumbers.ListNode.ListNode")


    class Solution:
        __java_fields__ = {}
        # 也可以复用老链表
        # 不过这个实现没有这么做，都是生成的新节点(为了教学好懂)
        @staticmethod
        def addTwoNumbers(h1, h2):
            ans = None
            cur = None
            carry = jcast('int', 0)
            # 声明变量
            sum = 0
            val = 0
            while ((h1 != None) or (h2 != None)):
                # 终止条件
                # 每一步h1的跳转
                # 每一步h2的跳转
                sum = jcast('int', jcast('int', jadd(jcast('int', jadd((0 if (h1 == None) else jget(h1, 'val')), (0 if (h2 == None) else jget(h2, 'val')))), carry)))
                val = jcast('int', jcast('int', jmod(sum, 10)))
                carry = jcast('int', jcast('int', jdiv(sum, 10)))
                if (ans == None):
                    ans = AddTwoNumbers.ListNode(val, _java_ctor=0)
                    cur = ans
                else:
                    jset(cur, 'next', AddTwoNumbers.ListNode(val, _java_ctor=0))
                    cur = jget(cur, 'next')
                h1 = (None if (h1 == None) else jget(h1, 'next'))
                h2 = (None if (h2 == None) else jget(h2, 'next'))
            if (carry == 1):
                jset(cur, 'next', AddTwoNumbers.ListNode(1, _java_ctor=0))
            return ans

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


