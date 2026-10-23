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

# 修剪搜索二叉树
# 测试链接 : https://leetcode.cn/problems/trim-a-binary-search-tree/
class Code06_TrimBinarySearchTree:
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


    # 提交以下的方法
    # [low, high]
    @staticmethod
    def trimBST(cur, low, high):
        low = jcast('int', low)
        high = jcast('int', high)
        if (cur == None):
            return None
        if (jget(cur, 'val') < low):
            return Code06_TrimBinarySearchTree.trimBST(jget(cur, 'right'), low, high)
        if (jget(cur, 'val') > high):
            return Code06_TrimBinarySearchTree.trimBST(jget(cur, 'left'), low, high)
        # cur在范围中
        jset(cur, 'left', Code06_TrimBinarySearchTree.trimBST(jget(cur, 'left'), low, high))
        jset(cur, 'right', Code06_TrimBinarySearchTree.trimBST(jget(cur, 'right'), low, high))
        return cur

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


