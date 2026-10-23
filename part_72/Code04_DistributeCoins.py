# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 在二叉树中分配硬币
# 给你一个有 n 个结点的二叉树的根结点 root
# 其中树中每个结点 node 都对应有 node.val 枚硬币
# 整棵树上一共有 n 枚硬币
# 在一次移动中，我们可以选择两个相邻的结点，然后将一枚硬币从其中一个结点移动到另一个结点
# 移动可以是从父结点到子结点，或者从子结点移动到父结点
# 返回使每个结点上 只有 一枚硬币所需的 最少 移动次数
# 测试链接 : https://leetcode.cn/problems/distribute-coins-in-binary-tree/
class Code04_DistributeCoins:
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
    def distributeCoins(root):
        return jcast('int', jget(Code04_DistributeCoins.f(root), 'move'))

    class Info:
        __java_fields__ = {'cnt': 'cnt', 'sum': 'sum', 'move': 'move'}
        # cnt：实例字段，在构造函数中初始化。
        # sum：实例字段，在构造函数中初始化。
        # move：实例字段，在构造函数中初始化。
        def _java_init_0(self, a, b, c):
            a = jcast('int', a)
            b = jcast('int', b)
            c = jcast('int', c)
            self.cnt = jcast('int', a)
            self.sum = jcast('int', b)
            self.move = jcast('int', c)

        def __init__(self, *args, _java_ctor=None):
            self.cnt = jcast('int', 0)
            self.sum = jcast('int', 0)
            self.move = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int', 'int', 'int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_DistributeCoins.Info.Info")


    @staticmethod
    def f(x):
        if (x == None):
            return Code04_DistributeCoins.Info(0, 0, 0, _java_ctor=0)
        infol = Code04_DistributeCoins.f(jget(x, 'left'))
        infor = Code04_DistributeCoins.f(jget(x, 'right'))
        cnts = jcast('int', jcast('int', jadd(jcast('int', jadd(jget(infol, 'cnt'), jget(infor, 'cnt'))), 1)))
        sums = jcast('int', jcast('int', jadd(jcast('int', jadd(jget(infol, 'sum'), jget(infor, 'sum'))), jget(x, 'val'))))
        moves = jcast('int', jcast('int', jadd(jcast('int', jadd(jcast('int', jadd(jget(infol, 'move'), jget(infor, 'move'))), jstatic('Math', 'abs', jcast('int', (jget(infol, 'cnt') - jget(infol, 'sum')))))), jstatic('Math', 'abs', jcast('int', (jget(infor, 'cnt') - jget(infor, 'sum')))))))
        return Code04_DistributeCoins.Info(cnts, sums, moves, _java_ctor=0)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


