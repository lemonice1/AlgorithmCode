# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# Morris遍历判断搜索二叉树
# 测试链接 : https://leetcode.cn/problems/validate-binary-search-tree/
class Code03_MorrisCheckBST:
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
    def isValidBST(head):
        cur = head
        mostRight = None
        # 前一个遍历的节点
        pre = None
        ans = jcast('boolean', True)
        while (cur != None):
            try:
                mostRight = jget(cur, 'left')
                if (mostRight != None):
                    while ((jget(mostRight, 'right') != None) and (jget(mostRight, 'right') != cur)):
                        mostRight = jget(mostRight, 'right')
                    if (jget(mostRight, 'right') == None):
                        mostRight.right = cur
                        cur = jget(cur, 'left')
                        raise JContinue(None)
                    else:
                        mostRight.right = None
                if ((pre != None) and (jget(pre, 'val') >= jget(cur, 'val'))):
                    ans = jcast('boolean', False)
                pre = cur
                cur = jget(cur, 'right')
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        return jcast('boolean', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


