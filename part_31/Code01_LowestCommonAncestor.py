# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 普通二叉树上寻找两个节点的最近公共祖先
# 测试链接 : https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
class Code01_LowestCommonAncestor:
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
        if (((root == None) or (root == p)) or (root == q)):
            # 遇到空，或者p，或者q，直接返回
            return root
        l = Code01_LowestCommonAncestor.lowestCommonAncestor(jget(root, 'left'), p, q)
        r = Code01_LowestCommonAncestor.lowestCommonAncestor(jget(root, 'right'), p, q)
        if ((l != None) and (r != None)):
            # 左树也搜到，右树也搜到，返回root
            return root
        if ((l == None) and (r == None)):
            # 都没搜到返回空
            return None
        # l和r一个为空，一个不为空
        # 返回不空的那个
        return (l if (l != None) else r)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


