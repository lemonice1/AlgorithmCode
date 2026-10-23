# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 二叉树的锯齿形层序遍历
# 测试链接 : https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/
class Code02_ZigzagLevelOrderTraversal:
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
    # 用每次处理一层的优化bfs就非常容易实现
    # 如果测试数据量变大了就修改这个值
    MAXN = 0
    queue = None
    l = 0
    r = 0
    @staticmethod
    def zigzagLevelOrder(root):
        ans = jnew('ArrayList')
        if (root != None):
            Code02_ZigzagLevelOrderTraversal.l = jcast('int', jset(Code02_ZigzagLevelOrderTraversal, 'r', 0))
            jset(Code02_ZigzagLevelOrderTraversal.queue, ((_java_obj_1 := Code02_ZigzagLevelOrderTraversal), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], root)
            # false 代表从左往右
            # true 代表从右往左
            reverse = jcast('boolean', False)
            while (Code02_ZigzagLevelOrderTraversal.l < Code02_ZigzagLevelOrderTraversal.r):
                size = jcast('int', jcast('int', (Code02_ZigzagLevelOrderTraversal.r - Code02_ZigzagLevelOrderTraversal.l)))
                list = jnew('ArrayList')
                # reverse == false, 左 -> 右， l....r-1, 收集size个
                # reverse == true,  右 -> 左， r-1....l, 收集size个
                # 左 -> 右, i = i + 1
                # 右 -> 左, i = i - 1
                i = jcast('int', (jcast('int', (Code02_ZigzagLevelOrderTraversal.r - 1)) if reverse else Code02_ZigzagLevelOrderTraversal.l))
                j = jcast('int', (jcast('int', (-1)) if reverse else 1))
                k = jcast('int', 0)
                while (k < size):
                    cur = Code02_ZigzagLevelOrderTraversal.queue[i]
                    jcall(list, 'add', jget(cur, 'val'))
                    i = jcast('int', jcast('int', jadd(i, j)))
                    k = jcast('int', (k + 1))
                i = jcast('int', 0)
                while (i < size):
                    cur = Code02_ZigzagLevelOrderTraversal.queue[((_java_obj_4 := Code02_ZigzagLevelOrderTraversal), (_java_key_5 := 'l'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]]
                    if (jget(cur, 'left') != None):
                        jset(Code02_ZigzagLevelOrderTraversal.queue, ((_java_obj_7 := Code02_ZigzagLevelOrderTraversal), (_java_key_8 := 'r'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4], jget(cur, 'left'))
                    if (jget(cur, 'right') != None):
                        jset(Code02_ZigzagLevelOrderTraversal.queue, ((_java_obj_10 := Code02_ZigzagLevelOrderTraversal), (_java_key_11 := 'r'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4], jget(cur, 'right'))
                    i = jcast('int', (i + 1))
                jcall(ans, 'add', list)
                reverse = jcast('boolean', (not reverse))
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_ZigzagLevelOrderTraversal.MAXN = jcast('int', 2001)
Code02_ZigzagLevelOrderTraversal.queue = jarray('TreeNode', [Code02_ZigzagLevelOrderTraversal.MAXN])
Code02_ZigzagLevelOrderTraversal.l = jcast('int', 0)
Code02_ZigzagLevelOrderTraversal.r = jcast('int', 0)
