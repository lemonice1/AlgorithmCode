# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 合并K个有序链表
# 测试链接：https://www.nowcoder.com/practice/65cfde9e5b9b4cf2b6bafa5f3ef33fa6
class Code01_MergeKSortedLists:
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


    # 提交以下的方法
    @staticmethod
    def mergeKLists(arr):
        # 小根堆
        heap = jnew('PriorityQueue', (lambda a, b: (jget(a, 'val') - jget(b, 'val'))))
        for h in arr:
            # 遍历所有的头！
            if (h != None):
                jcall(heap, 'add', h)
        if jcall(heap, 'isEmpty'):
            return None
        # 先弹出一个节点，做总头部
        h = jcall(heap, 'poll')
        pre = h
        if (jget(pre, 'next') != None):
            jcall(heap, 'add', jget(pre, 'next'))
        while (not jcall(heap, 'isEmpty')):
            cur = jcall(heap, 'poll')
            pre.next = cur
            pre = cur
            if (jget(cur, 'next') != None):
                jcall(heap, 'add', jget(cur, 'next'))
        return h

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


