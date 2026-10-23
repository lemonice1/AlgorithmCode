# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 判断链表是否是回文结构
# 测试链接 : https://leetcode.cn/problems/palindrome-linked-list/
class Code04_PalindromeLinkedList:
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
    def isPalindrome(head):
        if ((head == None) or (jget(head, 'next') == None)):
            return jcast('boolean', True)
        slow = head
        fast = head
        # 找中点
        while ((jget(fast, 'next') != None) and (jget(jget(fast, 'next'), 'next') != None)):
            slow = jget(slow, 'next')
            fast = jget(jget(fast, 'next'), 'next')
        # 现在中点就是slow，从中点开始往后的节点逆序
        pre = slow
        cur = jget(pre, 'next')
        next = None
        pre.next = None
        while (cur != None):
            next = jget(cur, 'next')
            cur.next = pre
            pre = cur
            cur = next
        # 上面的过程已经把链表调整成从左右两侧往中间指
        # head -> ... -> slow <- ... <- pre
        ans = jcast('boolean', True)
        left = head
        right = pre
        # left往右、right往左，每一步比对值是否一样，如果某一步不一样答案就是false
        while ((left != None) and (right != None)):
            try:
                if (jget(left, 'val') != jget(right, 'val')):
                    ans = jcast('boolean', False)
                    raise JBreak(None)
                left = jget(left, 'next')
                right = jget(right, 'next')
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        # 本着不坑的原则，把链表调整回原来的样子再返回判断结果
        cur = jget(pre, 'next')
        pre.next = None
        next = None
        while (cur != None):
            next = jget(cur, 'next')
            cur.next = pre
            pre = cur
            cur = next
        return jcast('boolean', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


