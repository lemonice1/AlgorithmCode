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

# 二叉搜索子树的最大键值和
# 给你一棵以 root 为根的二叉树
# 请你返回 任意 二叉搜索子树的最大键值和
# 二叉搜索树的定义如下：
# 任意节点的左子树中的键值都 小于 此节点的键值
# 任意节点的右子树中的键值都 大于 此节点的键值
# 任意节点的左子树和右子树都是二叉搜索树
# 测试链接 : https://leetcode.cn/problems/maximum-sum-bst-in-binary-tree/
class Code02_MaximumSumBst:
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
    def maxSumBST(root):
        return jcast('int', jget(Code02_MaximumSumBst.f(root), 'maxBstSum'))

    class Info:
        __java_fields__ = {'max': 'max', 'min': 'min', 'sum': 'sum', 'isBst': 'isBst', 'maxBstSum': 'maxBstSum'}
        # 为什么这里的max和min是int类型？
        # 因为题目的数据量规定，
        # 节点值在[-4 * 10^4，4 * 10^4]范围
        # 所以int类型的最小值和最大值就够用了
        # 不需要用long类型
        # max：实例字段，在构造函数中初始化。
        # min：实例字段，在构造函数中初始化。
        # sum：实例字段，在构造函数中初始化。
        # isBst：实例字段，在构造函数中初始化。
        # maxBstSum：实例字段，在构造函数中初始化。
        def _java_init_0(self, a, b, c, d, e):
            a = jcast('int', a)
            b = jcast('int', b)
            c = jcast('int', c)
            d = jcast('boolean', d)
            e = jcast('int', e)
            self.max = jcast('int', a)
            self.min = jcast('int', b)
            self.sum = jcast('int', c)
            self.isBst = jcast('boolean', d)
            self.maxBstSum = jcast('int', e)

        def __init__(self, *args, _java_ctor=None):
            self.max = jcast('int', 0)
            self.min = jcast('int', 0)
            self.sum = jcast('int', 0)
            self.isBst = jcast('boolean', False)
            self.maxBstSum = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int', 'int', 'int', 'boolean', 'int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_MaximumSumBst.Info.Info")


    @staticmethod
    def f(x):
        if (x == None):
            return Code02_MaximumSumBst.Info(jget(Integer, 'MIN_VALUE'), jget(Integer, 'MAX_VALUE'), 0, True, 0, _java_ctor=0)
        infol = Code02_MaximumSumBst.f(jget(x, 'left'))
        infor = Code02_MaximumSumBst.f(jget(x, 'right'))
        max = jcast('int', jstatic('Math', 'max', jget(x, 'val'), jstatic('Math', 'max', jget(infol, 'max'), jget(infor, 'max'))))
        min = jcast('int', jstatic('Math', 'min', jget(x, 'val'), jstatic('Math', 'min', jget(infol, 'min'), jget(infor, 'min'))))
        sum = jcast('int', jcast('int', jadd(jcast('int', jadd(jget(infol, 'sum'), jget(infor, 'sum'))), jget(x, 'val'))))
        isBst = jcast('boolean', (((jget(infol, 'isBst') and jget(infor, 'isBst')) and (jget(infol, 'max') < jget(x, 'val'))) and (jget(x, 'val') < jget(infor, 'min'))))
        maxBstSum = jcast('int', jstatic('Math', 'max', jget(infol, 'maxBstSum'), jget(infor, 'maxBstSum')))
        if isBst:
            maxBstSum = jcast('int', jstatic('Math', 'max', maxBstSum, sum))
        return Code02_MaximumSumBst.Info(max, min, sum, isBst, maxBstSum, _java_ctor=0)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


