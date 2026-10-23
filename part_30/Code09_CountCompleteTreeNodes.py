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

# 求完全二叉树的节点个数
# 测试链接 : https://leetcode.cn/problems/count-complete-tree-nodes/
class Code09_CountCompleteTreeNodes:
    __java_fields__ = {}
    # 不提交这个类
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


    # 提交如下的方法
    @staticmethod
    def countNodes(head):
        if (head == None):
            return jcast('int', 0)
        return jcast('int', Code09_CountCompleteTreeNodes.f(head, 1, Code09_CountCompleteTreeNodes.mostLeft(head, 1)))

    # cur : 当前来到的节点
    # level :  当前来到的节点在第几层
    # h : 整棵树的高度，不是cur这棵子树的高度
    # 求 : cur这棵子树上有多少节点
    @staticmethod
    def f(cur, level, h):
        level = jcast('int', level)
        h = jcast('int', h)
        if (level == h):
            return jcast('int', 1)
        if (Code09_CountCompleteTreeNodes.mostLeft(jget(cur, 'right'), jcast('int', jadd(level, 1))) == h):
            # cur右树上的最左节点，扎到了最深层
            return jcast('int', jcast('int', jadd(jcast('int', (1 << (jcast('int', (h - level)) & 31))), Code09_CountCompleteTreeNodes.f(jget(cur, 'right'), jcast('int', jadd(level, 1)), h))))
        else:
            # cur右树上的最左节点，没扎到最深层
            return jcast('int', jcast('int', jadd(jcast('int', (1 << (jcast('int', (jcast('int', (h - level)) - 1)) & 31))), Code09_CountCompleteTreeNodes.f(jget(cur, 'left'), jcast('int', jadd(level, 1)), h))))

    # 当前节点是cur，并且它在level层
    # 返回从cur开始不停往左，能扎到几层
    @staticmethod
    def mostLeft(cur, level):
        level = jcast('int', level)
        while (cur != None):
            level = jcast('int', (level + 1))
            cur = jget(cur, 'left')
        return jcast('int', jcast('int', (level - 1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


