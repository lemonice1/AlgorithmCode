# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 返回两个无环链表相交的第一个节点
# 测试链接 : https://leetcode.cn/problems/intersection-of-two-linked-lists/
class Code01_IntersectionOfTwoLinkedLists:
    __java_fields__ = {}
    # 提交时不要提交这个类
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
    def getIntersectionNode(h1, h2):
        if ((h1 == None) or (h2 == None)):
            return None
        a = h1
        b = h2
        diff = jcast('int', 0)
        while (jget(a, 'next') != None):
            a = jget(a, 'next')
            diff = jcast('int', (diff + 1))
        while (jget(b, 'next') != None):
            b = jget(b, 'next')
            diff = jcast('int', (diff - 1))
        if (a != b):
            return None
        if (diff >= 0):
            a = h1
            b = h2
        else:
            a = h2
            b = h1
        diff = jcast('int', jstatic('Math', 'abs', diff))
        while (((_java_old_1 := diff), (diff := jcast('int', (diff + (-1)))), _java_old_1)[2] != 0):
            a = jget(a, 'next')
        while (a != b):
            a = jget(a, 'next')
            b = jget(b, 'next')
        return a

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


