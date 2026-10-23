# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 复制带随机指针的链表
# 测试链接 : https://leetcode.cn/problems/copy-list-with-random-pointer/
class Code03_CopyListWithRandomPointer:
    __java_fields__ = {}
    # 不要提交这个类
    class Node:
        __java_fields__ = {'val': 'val', 'next': 'next', 'random': 'random'}
        # val：实例字段，在构造函数中初始化。
        # next：实例字段，在构造函数中初始化。
        # random：实例字段，在构造函数中初始化。
        def _java_init_0(self, v):
            v = jcast('int', v)
            self.val = jcast('int', v)

        def __init__(self, *args, _java_ctor=None):
            self.val = jcast('int', 0)
            self.next = None
            self.random = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code03_CopyListWithRandomPointer.Node.Node")


    # 提交如下的方法
    @staticmethod
    def copyRandomList(head):
        if (head == None):
            return None
        cur = head
        next = None
        # 1 -> 2 -> 3 -> ...
        # 变成 : 1 -> 1' -> 2 -> 2' -> 3 -> 3' -> ...
        while (cur != None):
            next = jget(cur, 'next')
            jset(cur, 'next', Code03_CopyListWithRandomPointer.Node(jget(cur, 'val'), _java_ctor=0))
            jset(jget(cur, 'next'), 'next', next)
            cur = next
        cur = head
        copy = None
        # 利用上面新老节点的结构关系，设置每一个新节点的random指针
        while (cur != None):
            next = jget(jget(cur, 'next'), 'next')
            copy = jget(cur, 'next')
            copy.random = (jget(jget(cur, 'random'), 'next') if (jget(cur, 'random') != None) else None)
            cur = next
        ans = jget(head, 'next')
        cur = head
        # 新老链表分离 : 老链表重新连在一起，新链表重新连在一起
        while (cur != None):
            next = jget(jget(cur, 'next'), 'next')
            copy = jget(cur, 'next')
            cur.next = next
            copy.next = (jget(next, 'next') if (next != None) else None)
            cur = next
        # 返回新链表的头节点
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


