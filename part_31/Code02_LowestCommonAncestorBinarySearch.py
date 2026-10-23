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

# 搜索二叉树上寻找两个节点的最近公共祖先
# 测试链接 : https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/
class Code02_LowestCommonAncestorBinarySearch:
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
    def lowestCommonAncestor(root, p, q):
        # root从上到下
        # 如果先遇到了p，说明p是答案
        # 如果先遇到了q，说明q是答案
        # 如果root在p~q的值之间，不用管p和q谁大谁小，只要root在中间，那么此时的root就是答案
        # 如果root在p~q的值的左侧，那么root往右移动
        # 如果root在p~q的值的右侧，那么root往左移动
        while ((jget(root, 'val') != jget(p, 'val')) and (jget(root, 'val') != jget(q, 'val'))):
            try:
                if ((jstatic('Math', 'min', jget(p, 'val'), jget(q, 'val')) < jget(root, 'val')) and (jget(root, 'val') < jstatic('Math', 'max', jget(p, 'val'), jget(q, 'val')))):
                    raise JBreak(None)
                root = (jget(root, 'right') if (jget(root, 'val') < jstatic('Math', 'min', jget(p, 'val'), jget(q, 'val'))) else jget(root, 'left'))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        return root

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


