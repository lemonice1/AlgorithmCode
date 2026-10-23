# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# Morris遍历实现后序遍历
# 测试链接 : https://leetcode.cn/problems/binary-tree-postorder-traversal/
class Code02_MorrisPostorder:
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
    def postorderTraversal(head):
        ans = jnew('ArrayList')
        Code02_MorrisPostorder.morrisPostorder(head, ans)
        return ans

    @staticmethod
    def morrisPostorder(head, ans):
        cur = head
        mostRight = None
        while (cur != None):
            try:
                mostRight = jget(cur, 'left')
                # cur有左树
                if (mostRight != None):
                    # 找到左树最右节点
                    # 注意左树最右节点的右指针可能指向空，也可能指向cur
                    while ((jget(mostRight, 'right') != None) and (jget(mostRight, 'right') != cur)):
                        mostRight = jget(mostRight, 'right')
                    # 判断左树最右节点的右指针状态
                    # 第一次到达
                    if (jget(mostRight, 'right') == None):
                        mostRight.right = cur
                        cur = jget(cur, 'left')
                        raise JContinue(None)
                        # 第二次到达
                    else:
                        mostRight.right = None
                        Code02_MorrisPostorder.collect(jget(cur, 'left'), ans)
                cur = jget(cur, 'right')
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        Code02_MorrisPostorder.collect(head, ans)

    # 以head为头的子树，树的右边界逆序收集
    @staticmethod
    def collect(head, ans):
        tail = Code02_MorrisPostorder.reverse(head)
        cur = tail
        while (cur != None):
            jcall(ans, 'add', jget(cur, 'val'))
            cur = jget(cur, 'right')
        Code02_MorrisPostorder.reverse(tail)

    # 从from出发，类似单链表翻转，去翻转right指针的方向
    @staticmethod
    def reverse(from_):
        pre = None
        next = None
        while (from_ != None):
            next = jget(from_, 'right')
            from_.right = pre
            pre = from_
            from_ = next
        return pre

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


