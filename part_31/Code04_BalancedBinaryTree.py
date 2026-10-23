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

# 验证平衡二叉树
# 测试链接 : https://leetcode.cn/problems/balanced-binary-tree/
class Code04_BalancedBinaryTree:
    __java_fields__ = {'balance': 'balance'}
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
    balance = False
    @staticmethod
    def isBalanced(root):
        # balance是全局变量，所有调用过程共享
        # 所以每次判断开始时，设置为true
        Code04_BalancedBinaryTree.balance = jcast('boolean', True)
        Code04_BalancedBinaryTree.height(root)
        return jcast('boolean', Code04_BalancedBinaryTree.balance)

    # 一旦发现不平衡，返回什么高度已经不重要了
    @staticmethod
    def height(cur):
        if ((not Code04_BalancedBinaryTree.balance) or (cur == None)):
            return jcast('int', 0)
        lh = jcast('int', Code04_BalancedBinaryTree.height(jget(cur, 'left')))
        rh = jcast('int', Code04_BalancedBinaryTree.height(jget(cur, 'right')))
        if (jstatic('Math', 'abs', jcast('int', (lh - rh))) > 1):
            Code04_BalancedBinaryTree.balance = jcast('boolean', False)
        return jcast('int', jcast('int', jadd(jstatic('Math', 'max', lh, rh), 1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_BalancedBinaryTree.balance = jcast('boolean', False)
