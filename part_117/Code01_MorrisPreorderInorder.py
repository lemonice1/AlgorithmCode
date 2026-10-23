# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# Morris遍历实现先序和中序遍历
# 测试链接 : https://leetcode.cn/problems/binary-tree-preorder-traversal/
# 测试链接 : https://leetcode.cn/problems/binary-tree-inorder-traversal/
class Code01_MorrisPreorderInorder:
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


    # Morris遍历
    @staticmethod
    def morris(head):
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
                cur = jget(cur, 'right')
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break

    # Morris遍历实现先序遍历
    # 测试链接 : https://leetcode.cn/problems/binary-tree-preorder-traversal/
    # 在线评测入口对应 preorderTraversal 方法，提交时需保留相应的接口
    @staticmethod
    def preorderTraversal(head):
        ans = jnew('ArrayList')
        Code01_MorrisPreorderInorder.morrisPreorder(head, ans)
        return ans

    @staticmethod
    def morrisPreorder(head, ans):
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
                        jcall(ans, 'add', jget(cur, 'val'))
                        mostRight.right = cur
                        cur = jget(cur, 'left')
                        raise JContinue(None)
                        # 第二次到达
                    else:
                        mostRight.right = None
                    # cur无左树
                else:
                    jcall(ans, 'add', jget(cur, 'val'))
                cur = jget(cur, 'right')
            except JContinue as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
            except JBreak as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
                break

    # Morris遍历实现中序遍历
    # 测试链接 : https://leetcode.cn/problems/binary-tree-inorder-traversal/
    # 在线评测入口对应 inorderTraversal 方法，提交时需保留相应的接口
    @staticmethod
    def inorderTraversal(head):
        ans = jnew('ArrayList')
        Code01_MorrisPreorderInorder.morrisInorder(head, ans)
        return ans

    @staticmethod
    def morrisInorder(head, ans):
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
                jcall(ans, 'add', jget(cur, 'val'))
                cur = jget(cur, 'right')
            except JContinue as _java_control_3:
                if _java_control_3.label not in (None,):
                    raise
            except JBreak as _java_control_3:
                if _java_control_3.label not in (None,):
                    raise
                break

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


