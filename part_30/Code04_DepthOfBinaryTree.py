# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 求二叉树的最大、最小深度
class Code04_DepthOfBinaryTree:
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


    # 测试链接 : https://leetcode.cn/problems/maximum-depth-of-binary-tree/
    @staticmethod
    def maxDepth(root):
        return jcast('int', (0 if (root == None) else jcast('int', jadd(jstatic('Math', 'max', Code04_DepthOfBinaryTree.maxDepth(jget(root, 'left')), Code04_DepthOfBinaryTree.maxDepth(jget(root, 'right'))), 1))))

    # 测试链接 : https://leetcode.cn/problems/minimum-depth-of-binary-tree/
    def minDepth(self, root):
        if (root == None):
            # 当前的树是空树
            return jcast('int', 0)
        if ((jget(root, 'left') == None) and (jget(root, 'right') == None)):
            # 当前root是叶节点
            return jcast('int', 1)
        ldeep = jcast('int', jget(Integer, 'MAX_VALUE'))
        rdeep = jcast('int', jget(Integer, 'MAX_VALUE'))
        if (jget(root, 'left') != None):
            ldeep = jcast('int', self.minDepth(jget(root, 'left')))
        if (jget(root, 'right') != None):
            rdeep = jcast('int', self.minDepth(jget(root, 'right')))
        return jcast('int', jcast('int', jadd(jstatic('Math', 'min', ldeep, rdeep), 1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


