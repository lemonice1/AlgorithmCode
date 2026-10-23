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

# 二叉树打家劫舍问题
# 测试链接 : https://leetcode.cn/problems/house-robber-iii/
class Code07_HouseRobberIII:
    __java_fields__ = {'yes': 'yes', 'no': 'no'}
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
    def rob(root):
        Code07_HouseRobberIII.f(root)
        return jcast('int', jstatic('Math', 'max', Code07_HouseRobberIII.yes, Code07_HouseRobberIII.no))

    # 全局变量，完成了X子树的遍历，返回之后
    # yes变成，X子树在偷头节点的情况下，最大的收益
    yes = 0
    # 全局变量，完成了X子树的遍历，返回之后
    # no变成，X子树在不偷头节点的情况下，最大的收益
    no = 0
    @staticmethod
    def f(root):
        if (root == None):
            Code07_HouseRobberIII.yes = jcast('int', 0)
            Code07_HouseRobberIII.no = jcast('int', 0)
        else:
            y = jcast('int', jget(root, 'val'))
            n = jcast('int', 0)
            Code07_HouseRobberIII.f(jget(root, 'left'))
            y = jcast('int', jcast('int', jadd(y, Code07_HouseRobberIII.no)))
            n = jcast('int', jcast('int', jadd(n, jstatic('Math', 'max', Code07_HouseRobberIII.yes, Code07_HouseRobberIII.no))))
            Code07_HouseRobberIII.f(jget(root, 'right'))
            y = jcast('int', jcast('int', jadd(y, Code07_HouseRobberIII.no)))
            n = jcast('int', jcast('int', jadd(n, jstatic('Math', 'max', Code07_HouseRobberIII.yes, Code07_HouseRobberIII.no))))
            Code07_HouseRobberIII.yes = jcast('int', y)
            Code07_HouseRobberIII.no = jcast('int', n)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_HouseRobberIII.yes = jcast('int', 0)
Code07_HouseRobberIII.no = jcast('int', 0)
