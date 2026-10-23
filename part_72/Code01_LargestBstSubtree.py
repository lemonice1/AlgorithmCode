# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最大BST子树
# 给定一个二叉树，找到其中最大的二叉搜索树（BST）子树，并返回该子树的大小
# 其中，最大指的是子树节点数最多的
# 二叉搜索树（BST）中的所有节点都具备以下属性：
# 左子树的值小于其父（根）节点的值
# 右子树的值大于其父（根）节点的值
# 注意：子树必须包含其所有后代
# 测试链接 : https://leetcode.cn/problems/largest-bst-subtree/
class Code01_LargestBstSubtree:
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
    def largestBSTSubtree(root):
        return jcast('int', jget(Code01_LargestBstSubtree.f(root), 'maxBstSize'))

    class Info:
        __java_fields__ = {'max': 'max', 'min': 'min', 'isBst': 'isBst', 'maxBstSize': 'maxBstSize'}
        # max：实例字段，在构造函数中初始化。
        # min：实例字段，在构造函数中初始化。
        # isBst：实例字段，在构造函数中初始化。
        # maxBstSize：实例字段，在构造函数中初始化。
        def _java_init_0(self, a, b, c, d):
            a = jcast('long', a)
            b = jcast('long', b)
            c = jcast('boolean', c)
            d = jcast('int', d)
            self.max = jcast('long', a)
            self.min = jcast('long', b)
            self.isBst = jcast('boolean', c)
            self.maxBstSize = jcast('int', d)

        def __init__(self, *args, _java_ctor=None):
            self.max = jcast('long', 0)
            self.min = jcast('long', 0)
            self.isBst = jcast('boolean', False)
            self.maxBstSize = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['long', 'long', 'boolean', 'int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_LargestBstSubtree.Info.Info")


    @staticmethod
    def f(x):
        if (x == None):
            return Code01_LargestBstSubtree.Info(jget(Long, 'MIN_VALUE'), jget(Long, 'MAX_VALUE'), True, 0, _java_ctor=0)
        infol = Code01_LargestBstSubtree.f(jget(x, 'left'))
        infor = Code01_LargestBstSubtree.f(jget(x, 'right'))
        # 左 4信息
        # 右 4信息
        # x 整合出4信息返回
        max = jcast('long', jstatic('Math', 'max', jget(x, 'val'), jstatic('Math', 'max', jget(infol, 'max'), jget(infor, 'max'))))
        min = jcast('long', jstatic('Math', 'min', jget(x, 'val'), jstatic('Math', 'min', jget(infol, 'min'), jget(infor, 'min'))))
        isBst = jcast('boolean', (((jget(infol, 'isBst') and jget(infor, 'isBst')) and (jget(infol, 'max') < jget(x, 'val'))) and (jget(x, 'val') < jget(infor, 'min'))))
        maxBSTSize = 0
        if isBst:
            maxBSTSize = jcast('int', jcast('int', jadd(jcast('int', jadd(jget(infol, 'maxBstSize'), jget(infor, 'maxBstSize'))), 1)))
        else:
            maxBSTSize = jcast('int', jstatic('Math', 'max', jget(infol, 'maxBstSize'), jget(infor, 'maxBstSize')))
        return Code01_LargestBstSubtree.Info(max, min, isBst, maxBSTSize, _java_ctor=0)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


