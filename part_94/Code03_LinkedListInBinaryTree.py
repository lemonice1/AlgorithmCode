# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 二叉树中的链表
# 给你一棵以root为根的二叉树、一个以head为头的链表
# 在二叉树中，有很多一直向下的路径
# 如果某个路径上的数值等于以head为头的整个链表
# 返回True，否则返回False
# 测试链接 : https://leetcode.cn/problems/linked-list-in-binary-tree/
class Code03_LinkedListInBinaryTree:
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


    # 不要提交这个类
    class TreeNode:
        __java_fields__ = {'val': 'val', 'left': 'left', 'right': 'right'}
        # val：实例字段，在构造函数中初始化。
        # left：实例字段，在构造函数中初始化。
        # right：实例字段，在构造函数中初始化。
        def __init__(self, *args, _java_ctor=None):
            self.val = jcast('int', 0)
            self.left = None
            self.right = None
            if args:
                raise TypeError('This class has a no-argument constructor')


    # 提交以下正式方法
    # 时间复杂度O(n + m)
    @staticmethod
    def isSubPath(head, root):
        m = jcast('int', 0)
        tmp = head
        while (tmp != None):
            m = jcast('int', (m + 1))
            tmp = jget(tmp, 'next')
        s2 = jarray('int', [m])
        m = jcast('int', 0)
        while (head != None):
            jset(s2, ((_java_old_1 := m), (m := jcast('int', (m + (1)))), _java_old_1)[2], jget(head, 'val'))
            head = jget(head, 'next')
        next = Code03_LinkedListInBinaryTree.nextArray(s2, m)
        return jcast('boolean', Code03_LinkedListInBinaryTree.find(s2, next, root, 0))

    # 二叉树来到cur节点了
    # 链表比对的位置来到i位置
    # 利用链表的next数组加速匹配
    # 返回是否能把链表整体匹配出来
    @staticmethod
    def find(s2, next, cur, i):
        i = jcast('int', i)
        if (i == jget(s2, 'length')):
            return jcast('boolean', True)
        if (cur == None):
            return jcast('boolean', False)
        # 当前来到cur节点, 一开始的i是父亲节点给的
        # 但是要修正，找到配成的位置
        # 均摊下来，时间复杂度O(1)
        while ((i >= 0) and (jget(cur, 'val') != s2[i])):
            i = jcast('int', next[i])
        return jcast('boolean', (Code03_LinkedListInBinaryTree.find(s2, next, jget(cur, 'left'), jcast('int', jadd(i, 1))) or Code03_LinkedListInBinaryTree.find(s2, next, jget(cur, 'right'), jcast('int', jadd(i, 1)))))

    @staticmethod
    def nextArray(s, m):
        m = jcast('int', m)
        if (m == 1):
            return jarray('int', [None], [jcast('int', (-1))])
        next = jarray('int', [m])
        next[0] = jcast('int', jcast('int', (-1)))
        next[1] = jcast('int', 0)
        i = jcast('int', 2)
        cn = jcast('int', 0)
        while (i < m):
            if (s[jcast('int', (i - 1))] == s[cn]):
                jset(next, ((_java_old_2 := i), (i := jcast('int', (i + (1)))), _java_old_2)[2], (cn := jcast('int', (cn + (1)))))
            else:
                if (cn > 0):
                    cn = jcast('int', next[cn])
                else:
                    jset(next, ((_java_old_3 := i), (i := jcast('int', (i + (1)))), _java_old_3)[2], 0)
        return next

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


