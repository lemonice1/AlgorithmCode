# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 监控二叉树
# 给定一个二叉树，我们在树的节点上安装摄像头
# 节点上的每个摄影头都可以监视其父对象、自身及其直接子对象
# 计算监控树的所有节点所需的最小摄像头数量
# 测试链接 : https://leetcode.cn/problems/binary-tree-cameras/
class Code06_BinaryTreeCameras:
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
    def minCameraCover(self, root):
        Code06_BinaryTreeCameras.ans = jcast('int', 0)
        if (self.f(root) == 0):
            Code06_BinaryTreeCameras.ans = jcast('int', (Code06_BinaryTreeCameras.ans + 1))
        return jcast('int', Code06_BinaryTreeCameras.ans)

    # 遍历过程中一旦需要放置相机，ans++
    ans = 0
    # 递归含义
    # 假设x上方一定有父亲的情况下，这个假设很重要
    # x为头的整棵树，最终想都覆盖，
    # 并且想使用最少的摄像头，x应该是什么样的状态
    # 返回值含义
    # 0: x是无覆盖的状态，x下方的节点都已经被覆盖
    # 1: x是覆盖状态，x上没摄像头，x下方的节点都已经被覆盖
    # 2: x是覆盖状态，x上有摄像头，x下方的节点都已经被覆盖
    def f(self, x):
        if (x == None):
            return jcast('int', 1)
        left = jcast('int', self.f(jget(x, 'left')))
        right = jcast('int', self.f(jget(x, 'right')))
        if ((left == 0) or (right == 0)):
            Code06_BinaryTreeCameras.ans = jcast('int', (Code06_BinaryTreeCameras.ans + 1))
            return jcast('int', 2)
        if ((left == 1) and (right == 1)):
            return jcast('int', 0)
        return jcast('int', 1)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_BinaryTreeCameras.ans = jcast('int', 0)
