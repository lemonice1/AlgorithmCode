# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 二叉树的直径
# 给你一棵二叉树的根节点，返回该树的直径
# 二叉树的 直径 是指树中任意两个节点之间最长路径的长度
# 这条路径可能经过也可能不经过根节点 root
# 两节点之间路径的 长度 由它们之间边数表示
# 测试链接 : https://leetcode.cn/problems/diameter-of-binary-tree/
class Code03_DiameterOfBinaryTree:
    __java_fields__ = {}
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


    # 提交如下的方法
    @staticmethod
    def diameterOfBinaryTree(root):
        return jcast('int', jget(Code03_DiameterOfBinaryTree.f(root), 'diameter'))

    class Info:
        __java_fields__ = {'diameter': 'diameter', 'height': 'height'}
        # diameter：实例字段，在构造函数中初始化。
        # height：实例字段，在构造函数中初始化。
        def _java_init_0(self, a, b):
            a = jcast('int', a)
            b = jcast('int', b)
            self.diameter = jcast('int', a)
            self.height = jcast('int', b)

        def __init__(self, *args, _java_ctor=None):
            self.diameter = jcast('int', 0)
            self.height = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int', 'int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code03_DiameterOfBinaryTree.Info.Info")


    @staticmethod
    def f(x):
        if (x == None):
            return Code03_DiameterOfBinaryTree.Info(0, 0, _java_ctor=0)
        leftInfo = Code03_DiameterOfBinaryTree.f(jget(x, 'left'))
        rightInfo = Code03_DiameterOfBinaryTree.f(jget(x, 'right'))
        height = jcast('int', jcast('int', jadd(jstatic('Math', 'max', jget(leftInfo, 'height'), jget(rightInfo, 'height')), 1)))
        diameter = jcast('int', jstatic('Math', 'max', jget(leftInfo, 'diameter'), jget(rightInfo, 'diameter')))
        diameter = jcast('int', jstatic('Math', 'max', diameter, jcast('int', jadd(jget(leftInfo, 'height'), jget(rightInfo, 'height')))))
        return Code03_DiameterOfBinaryTree.Info(diameter, height, _java_ctor=0)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


