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

# 利用先序与中序遍历序列构造二叉树
# 测试链接 : https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
class Code07_PreorderInorderBuildBinaryTree:
    __java_fields__ = {}
    # 不提交这个类
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
            raise TypeError("No matching overload for Code07_PreorderInorderBuildBinaryTree.TreeNode.TreeNode")


    # 提交如下的方法
    @staticmethod
    def buildTree(pre, in_):
        if (((pre == None) or (in_ == None)) or (jget(pre, 'length') != jget(in_, 'length'))):
            return None
        map = jnew('HashMap')
        i = jcast('int', 0)
        while (i < jget(in_, 'length')):
            jcall(map, 'put', in_[i], i)
            i = jcast('int', (i + 1))
        return Code07_PreorderInorderBuildBinaryTree.f(pre, 0, jcast('int', (jget(pre, 'length') - 1)), in_, 0, jcast('int', (jget(in_, 'length') - 1)), map)

    @staticmethod
    def f(pre, l1, r1, in_, l2, r2, map):
        l1 = jcast('int', l1)
        r1 = jcast('int', r1)
        l2 = jcast('int', l2)
        r2 = jcast('int', r2)
        if (l1 > r1):
            return None
        head = Code07_PreorderInorderBuildBinaryTree.TreeNode(pre[l1], _java_ctor=0)
        if (l1 == r1):
            return head
        k = jcast('int', jcall(map, 'get', pre[l1]))
        # pre : l1(........)[.......r1]
        # in  : (l2......)k[........r2]
        # (...)是左树对应，[...]是右树的对应
        jset(head, 'left', Code07_PreorderInorderBuildBinaryTree.f(pre, jcast('int', jadd(l1, 1)), jcast('int', (jcast('int', jadd(l1, k)) - l2)), in_, l2, jcast('int', (k - 1)), map))
        jset(head, 'right', Code07_PreorderInorderBuildBinaryTree.f(pre, jcast('int', jadd(jcast('int', (jcast('int', jadd(l1, k)) - l2)), 1)), r1, in_, jcast('int', jadd(k, 1)), r2, map))
        return head

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


