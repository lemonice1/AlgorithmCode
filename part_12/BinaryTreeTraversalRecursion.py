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

# 递归序的解释
# 用递归实现二叉树的三序遍历
class BinaryTreeTraversalRecursion:
    __java_fields__ = {}
    class TreeNode:
        __java_fields__ = {'val': 'val', 'left': 'left', 'right': 'right'}
        # val：实例字段，在构造函数中初始化。
        # left：实例字段，在构造函数中初始化。
        # right：实例字段，在构造函数中初始化。
        def _java_init_0(self, v):
            v = jcast('int', v)
            self.val = jcast('int', v)

        def __init__(self, *args, _java_ctor=None):
            self.val = jcast('int', 0)
            self.left = None
            self.right = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for BinaryTreeTraversalRecursion.TreeNode.TreeNode")


    # 递归基本样子，用来理解递归序
    @staticmethod
    def f(head):
        if (head == None):
            return
        # 1
        BinaryTreeTraversalRecursion.f(jget(head, 'left'))
        # 2
        BinaryTreeTraversalRecursion.f(jget(head, 'right'))
        # 3

    # 先序打印所有节点，递归版
    @staticmethod
    def preOrder(head):
        if (head == None):
            return
        jprint(jadd(jget(head, 'val'), ' '), newline=False)
        BinaryTreeTraversalRecursion.preOrder(jget(head, 'left'))
        BinaryTreeTraversalRecursion.preOrder(jget(head, 'right'))

    # 中序打印所有节点，递归版
    @staticmethod
    def inOrder(head):
        if (head == None):
            return
        BinaryTreeTraversalRecursion.inOrder(jget(head, 'left'))
        jprint(jadd(jget(head, 'val'), ' '), newline=False)
        BinaryTreeTraversalRecursion.inOrder(jget(head, 'right'))

    # 后序打印所有节点，递归版
    @staticmethod
    def posOrder(head):
        if (head == None):
            return
        BinaryTreeTraversalRecursion.posOrder(jget(head, 'left'))
        BinaryTreeTraversalRecursion.posOrder(jget(head, 'right'))
        jprint(jadd(jget(head, 'val'), ' '), newline=False)

    @staticmethod
    def main(args):
        head = BinaryTreeTraversalRecursion.TreeNode(1, _java_ctor=0)
        jset(head, 'left', BinaryTreeTraversalRecursion.TreeNode(2, _java_ctor=0))
        jset(head, 'right', BinaryTreeTraversalRecursion.TreeNode(3, _java_ctor=0))
        jset(jget(head, 'left'), 'left', BinaryTreeTraversalRecursion.TreeNode(4, _java_ctor=0))
        jset(jget(head, 'left'), 'right', BinaryTreeTraversalRecursion.TreeNode(5, _java_ctor=0))
        jset(jget(head, 'right'), 'left', BinaryTreeTraversalRecursion.TreeNode(6, _java_ctor=0))
        jset(jget(head, 'right'), 'right', BinaryTreeTraversalRecursion.TreeNode(7, _java_ctor=0))
        BinaryTreeTraversalRecursion.preOrder(head)
        jprint(newline=True)
        jprint('先序遍历递归版', newline=True)
        BinaryTreeTraversalRecursion.inOrder(head)
        jprint(newline=True)
        jprint('中序遍历递归版', newline=True)
        BinaryTreeTraversalRecursion.posOrder(head)
        jprint(newline=True)
        jprint('后序遍历递归版', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    BinaryTreeTraversalRecursion.main([])
