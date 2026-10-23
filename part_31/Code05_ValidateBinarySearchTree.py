# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 验证搜索二叉树
# 测试链接 : https://leetcode.cn/problems/validate-binary-search-tree/
class Code05_ValidateBinarySearchTree:
    __java_fields__ = {'MAXN': 'MAXN', 'stack': 'stack', 'r': 'r', 'min': 'min', 'max': 'max'}
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
    MAXN = 0
    stack = None
    r = 0
    # 提交时改名为isValidBST
    @staticmethod
    def isValidBST1(head):
        if (head == None):
            return jcast('boolean', True)
        pre = None
        Code05_ValidateBinarySearchTree.r = jcast('int', 0)
        while ((Code05_ValidateBinarySearchTree.r > 0) or (head != None)):
            if (head != None):
                jset(Code05_ValidateBinarySearchTree.stack, ((_java_obj_1 := Code05_ValidateBinarySearchTree), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], head)
                head = jget(head, 'left')
            else:
                head = Code05_ValidateBinarySearchTree.stack[((_java_obj_4 := Code05_ValidateBinarySearchTree), (_java_key_5 := 'r'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))))[3]]
                if ((pre != None) and (jget(pre, 'val') >= jget(head, 'val'))):
                    return jcast('boolean', False)
                pre = head
                head = jget(head, 'right')
        return jcast('boolean', True)

    min = 0
    max = 0
    # 提交时改名为isValidBST
    @staticmethod
    def isValidBST2(head):
        if (head == None):
            Code05_ValidateBinarySearchTree.min = jcast('long', jget(Long, 'MAX_VALUE'))
            Code05_ValidateBinarySearchTree.max = jcast('long', jget(Long, 'MIN_VALUE'))
            return jcast('boolean', True)
        lok = jcast('boolean', Code05_ValidateBinarySearchTree.isValidBST2(jget(head, 'left')))
        lmin = jcast('long', Code05_ValidateBinarySearchTree.min)
        lmax = jcast('long', Code05_ValidateBinarySearchTree.max)
        rok = jcast('boolean', Code05_ValidateBinarySearchTree.isValidBST2(jget(head, 'right')))
        rmin = jcast('long', Code05_ValidateBinarySearchTree.min)
        rmax = jcast('long', Code05_ValidateBinarySearchTree.max)
        Code05_ValidateBinarySearchTree.min = jcast('long', jstatic('Math', 'min', jstatic('Math', 'min', lmin, rmin), jget(head, 'val')))
        Code05_ValidateBinarySearchTree.max = jcast('long', jstatic('Math', 'max', jstatic('Math', 'max', lmax, rmax), jget(head, 'val')))
        return jcast('boolean', (((lok and rok) and (lmax < jget(head, 'val'))) and (jget(head, 'val') < rmin)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_ValidateBinarySearchTree.MAXN = jcast('int', 10001)
Code05_ValidateBinarySearchTree.stack = jarray('TreeNode', [Code05_ValidateBinarySearchTree.MAXN])
Code05_ValidateBinarySearchTree.r = jcast('int', 0)
Code05_ValidateBinarySearchTree.min = jcast('long', 0)
Code05_ValidateBinarySearchTree.max = jcast('long', 0)
