# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 二叉树的最大特殊宽度，Python版
# 测试链接 : https://leetcode.cn/problems/maximum-width-of-binary-tree/
class Code03_WidthOfBinaryTree1:
    __java_fields__ = {'MAXN': 'MAXN', 'nq': 'nq', 'iq': 'iq', 'l': 'l', 'r': 'r'}
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
    # 用每次处理一层的优化bfs就非常容易实现
    # 如果测试数据量变大了就修改这个值
    MAXN = 0
    nq = None
    iq = None
    l = 0
    r = 0
    @staticmethod
    def widthOfBinaryTree(root):
        ans = jcast('int', 1)
        Code03_WidthOfBinaryTree1.l = jcast('int', jset(Code03_WidthOfBinaryTree1, 'r', 0))
        Code03_WidthOfBinaryTree1.nq[Code03_WidthOfBinaryTree1.r] = root
        jset(Code03_WidthOfBinaryTree1.iq, ((_java_obj_1 := Code03_WidthOfBinaryTree1), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], 1)
        while (Code03_WidthOfBinaryTree1.l < Code03_WidthOfBinaryTree1.r):
            size = jcast('int', jcast('int', (Code03_WidthOfBinaryTree1.r - Code03_WidthOfBinaryTree1.l)))
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jcast('long', jadd(jcast('long', (Code03_WidthOfBinaryTree1.iq[jcast('int', (Code03_WidthOfBinaryTree1.r - 1))] - Code03_WidthOfBinaryTree1.iq[Code03_WidthOfBinaryTree1.l])), 1)))))
            i = jcast('int', 0)
            while (i < size):
                node = Code03_WidthOfBinaryTree1.nq[Code03_WidthOfBinaryTree1.l]
                id = jcast('long', Code03_WidthOfBinaryTree1.iq[((_java_obj_4 := Code03_WidthOfBinaryTree1), (_java_key_5 := 'l'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]])
                if (jget(node, 'left') != None):
                    Code03_WidthOfBinaryTree1.nq[Code03_WidthOfBinaryTree1.r] = jget(node, 'left')
                    jset(Code03_WidthOfBinaryTree1.iq, ((_java_obj_7 := Code03_WidthOfBinaryTree1), (_java_key_8 := 'r'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4], jcast('long', (id * 2)))
                if (jget(node, 'right') != None):
                    Code03_WidthOfBinaryTree1.nq[Code03_WidthOfBinaryTree1.r] = jget(node, 'right')
                    jset(Code03_WidthOfBinaryTree1.iq, ((_java_obj_10 := Code03_WidthOfBinaryTree1), (_java_key_11 := 'r'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4], jcast('long', jadd(jcast('long', (id * 2)), 1)))
                i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_WidthOfBinaryTree1.MAXN = jcast('int', 3001)
Code03_WidthOfBinaryTree1.nq = jarray('TreeNode', [Code03_WidthOfBinaryTree1.MAXN])
Code03_WidthOfBinaryTree1.iq = jarray('long', [Code03_WidthOfBinaryTree1.MAXN])
Code03_WidthOfBinaryTree1.l = jcast('int', 0)
Code03_WidthOfBinaryTree1.r = jcast('int', 0)
