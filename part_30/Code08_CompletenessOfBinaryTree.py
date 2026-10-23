# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 验证完全二叉树
# 测试链接 : https://leetcode.cn/problems/check-completeness-of-a-binary-tree/
class Code08_CompletenessOfBinaryTree:
    __java_fields__ = {'MAXN': 'MAXN', 'queue': 'queue', 'l': 'l', 'r': 'r'}
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
    # 如果测试数据量变大了就修改这个值
    MAXN = 0
    queue = None
    l = 0
    r = 0
    @staticmethod
    def isCompleteTree(h):
        if (h == None):
            return jcast('boolean', True)
        Code08_CompletenessOfBinaryTree.l = jcast('int', jset(Code08_CompletenessOfBinaryTree, 'r', 0))
        jset(Code08_CompletenessOfBinaryTree.queue, ((_java_obj_1 := Code08_CompletenessOfBinaryTree), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], h)
        # 是否遇到过左右两个孩子不双全的节点
        leaf = jcast('boolean', False)
        while (Code08_CompletenessOfBinaryTree.l < Code08_CompletenessOfBinaryTree.r):
            h = Code08_CompletenessOfBinaryTree.queue[((_java_obj_4 := Code08_CompletenessOfBinaryTree), (_java_key_5 := 'l'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]]
            if (((jget(h, 'left') == None) and (jget(h, 'right') != None)) or (leaf and ((jget(h, 'left') != None) or (jget(h, 'right') != None)))):
                return jcast('boolean', False)
            if (jget(h, 'left') != None):
                jset(Code08_CompletenessOfBinaryTree.queue, ((_java_obj_7 := Code08_CompletenessOfBinaryTree), (_java_key_8 := 'r'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4], jget(h, 'left'))
            if (jget(h, 'right') != None):
                jset(Code08_CompletenessOfBinaryTree.queue, ((_java_obj_10 := Code08_CompletenessOfBinaryTree), (_java_key_11 := 'r'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4], jget(h, 'right'))
            if ((jget(h, 'left') == None) or (jget(h, 'right') == None)):
                leaf = jcast('boolean', True)
        return jcast('boolean', True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code08_CompletenessOfBinaryTree.MAXN = jcast('int', 101)
Code08_CompletenessOfBinaryTree.queue = jarray('TreeNode', [Code08_CompletenessOfBinaryTree.MAXN])
Code08_CompletenessOfBinaryTree.l = jcast('int', 0)
Code08_CompletenessOfBinaryTree.r = jcast('int', 0)
