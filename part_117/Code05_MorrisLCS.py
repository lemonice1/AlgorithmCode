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

# Morris遍历求两个节点的最低公共祖先
# 测试链接 : https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
class Code05_MorrisLCS:
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


    # 提交以下的方法
    @staticmethod
    def lowestCommonAncestor(head, o1, o2):
        if ((Code05_MorrisLCS.preOrder(jget(o1, 'left'), o1, o2) != None) or (Code05_MorrisLCS.preOrder(jget(o1, 'right'), o1, o2) != None)):
            return o1
        if ((Code05_MorrisLCS.preOrder(jget(o2, 'left'), o1, o2) != None) or (Code05_MorrisLCS.preOrder(jget(o2, 'right'), o1, o2) != None)):
            return o2
        left = Code05_MorrisLCS.preOrder(head, o1, o2)
        cur = head
        mostRight = None
        lca = None
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
                        # 第二次来到cur
                    else:
                        mostRight.right = None
                        if (lca == None):
                            # 检查left是否在cur左树的右边界上
                            if Code05_MorrisLCS.rightCheck(jget(cur, 'left'), left):
                                # 检查left看看右树里是否有o2
                                if (Code05_MorrisLCS.preOrder(jget(left, 'right'), o1, o2) != None):
                                    lca = left
                                left = cur
                                # 为什么此时检查的是left而不是cur
                                # 因为cur右树上的某些右指针可能没有恢复回来
                                # 需要等右指针恢复回来之后检查才不出错
                                # 所以此时检查的是left而不是cur
                                # 课上已经重点图解了
                cur = jget(cur, 'right')
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        # 如果morris遍历结束了还没有收集到答案
        # 此时最后一个left还没有验证，它一定是答案
        return (lca if (lca != None) else left)

    # 以head为头的树进行先序遍历，o1和o2谁先被找到就返回谁
    @staticmethod
    def preOrder(head, o1, o2):
        cur = head
        mostRight = None
        ans = None
        while (cur != None):
            try:
                mostRight = jget(cur, 'left')
                if (mostRight != None):
                    while ((jget(mostRight, 'right') != None) and (jget(mostRight, 'right') != cur)):
                        mostRight = jget(mostRight, 'right')
                    if (jget(mostRight, 'right') == None):
                        if ((ans == None) and ((cur == o1) or (cur == o2))):
                            ans = cur
                        mostRight.right = cur
                        cur = jget(cur, 'left')
                        raise JContinue(None)
                    else:
                        mostRight.right = None
                else:
                    if ((ans == None) and ((cur == o1) or (cur == o2))):
                        ans = cur
                cur = jget(cur, 'right')
            except JContinue as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
            except JBreak as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
                break
        return ans

    # 以head为头的树遍历右边界，返回是否找到了target
    @staticmethod
    def rightCheck(head, target):
        while (head != None):
            if (head == target):
                return jcast('boolean', True)
            head = jget(head, 'right')
        return jcast('boolean', False)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


