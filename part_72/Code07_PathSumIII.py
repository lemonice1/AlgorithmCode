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

# 路径总和 III
# 给定一个二叉树的根节点 root ，和一个整数 targetSum
# 求该二叉树里节点值之和等于 targetSum 的 路径 的数目
# 路径 不需要从根节点开始，也不需要在叶子节点结束
# 但是路径方向必须是向下的（只能从父节点到子节点）
# 测试链接 : https://leetcode.cn/problems/path-sum-iii/
class Code07_PathSumIII:
    __java_fields__ = {'ans': 'ans'}
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
    def pathSum(root, sum):
        sum = jcast('int', sum)
        presum = jnew('HashMap')
        jcall(presum, 'put', 0, 1)
        Code07_PathSumIII.ans = jcast('int', 0)
        Code07_PathSumIII.f(root, sum, 0, presum)
        return jcast('int', Code07_PathSumIII.ans)

    ans = 0
    # sum : 从头节点出发，来到x的时候，上方累加和是多少
    # 路径必须以x作为结尾，路径累加和是target的路径数量，累加到全局变量ans上
    @staticmethod
    def f(x, target, sum, presum):
        target = jcast('int', target)
        sum = jcast('long', sum)
        if (x != None):
            # 从头节点出发一路走到x的整体累加和
            sum = jcast('long', jcast('long', jadd(sum, jget(x, 'val'))))
            Code07_PathSumIII.ans = jcast('int', jadd(Code07_PathSumIII.ans, jcall(presum, 'getOrDefault', jcast('long', (sum - target)), 0)))
            jcall(presum, 'put', sum, jadd(jcall(presum, 'getOrDefault', sum, 0), 1))
            Code07_PathSumIII.f(jget(x, 'left'), target, sum, presum)
            Code07_PathSumIII.f(jget(x, 'right'), target, sum, presum)
            jcall(presum, 'put', sum, (jcall(presum, 'get', sum) - 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_PathSumIII.ans = jcast('int', 0)
