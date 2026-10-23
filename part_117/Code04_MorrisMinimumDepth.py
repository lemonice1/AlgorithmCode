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

# Morris遍历求二叉树最小高度
# 测试链接 : https://leetcode.cn/problems/minimum-depth-of-binary-tree/
class Code04_MorrisMinimumDepth:
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
    def minDepth(head):
        if (head == None):
            return jcast('int', 0)
        cur = head
        mostRight = None
        # morris遍历中，上一个节点所在的层数
        preLevel = jcast('int', 0)
        # 树的右边界长度
        rightLen = 0
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        while (cur != None):
            try:
                mostRight = jget(cur, 'left')
                if (mostRight != None):
                    rightLen = jcast('int', 1)
                    while ((jget(mostRight, 'right') != None) and (jget(mostRight, 'right') != cur)):
                        rightLen = jcast('int', (rightLen + 1))
                        mostRight = jget(mostRight, 'right')
                    if (jget(mostRight, 'right') == None):
                        preLevel = jcast('int', (preLevel + 1))
                        mostRight.right = cur
                        cur = jget(cur, 'left')
                        raise JContinue(None)
                    else:
                        if (jget(mostRight, 'left') == None):
                            ans = jcast('int', jstatic('Math', 'min', ans, preLevel))
                        preLevel = jcast('int', jcast('int', (preLevel - rightLen)))
                        mostRight.right = None
                else:
                    preLevel = jcast('int', (preLevel + 1))
                cur = jget(cur, 'right')
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        # 不要忘了整棵树的最右节点
        rightLen = jcast('int', 1)
        cur = head
        while (jget(cur, 'right') != None):
            rightLen = jcast('int', (rightLen + 1))
            cur = jget(cur, 'right')
        # 整棵树的最右节点是叶节点才纳入统计
        if (jget(cur, 'left') == None):
            ans = jcast('int', jstatic('Math', 'min', ans, rightLen))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


