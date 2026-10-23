# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 二叉树的层序遍历
# 测试链接 : https://leetcode.cn/problems/binary-tree-level-order-traversal/
class Code01_LevelOrderTraversal:
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


    # 提交时把方法名改为levelOrder，此方法为普通bfs，此题不推荐
    @staticmethod
    def levelOrder1(root):
        ans = jnew('ArrayList')
        if (root != None):
            queue = jnew('LinkedList')
            levels = jnew('HashMap')
            jcall(queue, 'add', root)
            jcall(levels, 'put', root, 0)
            while (not jcall(queue, 'isEmpty')):
                cur = jcall(queue, 'poll')
                level = jcast('int', jcall(levels, 'get', cur))
                if (jcall(ans, 'size') == level):
                    jcall(ans, 'add', jnew('ArrayList'))
                jcall(jcall(ans, 'get', level), 'add', jget(cur, 'val'))
                if (jget(cur, 'left') != None):
                    jcall(queue, 'add', jget(cur, 'left'))
                    jcall(levels, 'put', jget(cur, 'left'), jcast('int', jadd(level, 1)))
                if (jget(cur, 'right') != None):
                    jcall(queue, 'add', jget(cur, 'right'))
                    jcall(levels, 'put', jget(cur, 'right'), jcast('int', jadd(level, 1)))
        return ans

    # 如果测试数据量变大了就修改这个值
    MAXN = 0
    queue = None
    l = 0
    r = 0
    # 提交时把方法名改为levelOrder，此方法为每次处理一层的优化bfs，此题推荐
    @staticmethod
    def levelOrder2(root):
        ans = jnew('ArrayList')
        if (root != None):
            Code01_LevelOrderTraversal.l = jcast('int', jset(Code01_LevelOrderTraversal, 'r', 0))
            jset(Code01_LevelOrderTraversal.queue, ((_java_obj_1 := Code01_LevelOrderTraversal), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], root)
            # 队列里还有东西
            while (Code01_LevelOrderTraversal.l < Code01_LevelOrderTraversal.r):
                size = jcast('int', jcast('int', (Code01_LevelOrderTraversal.r - Code01_LevelOrderTraversal.l)))
                list = jnew('ArrayList')
                i = jcast('int', 0)
                while (i < size):
                    cur = Code01_LevelOrderTraversal.queue[((_java_obj_4 := Code01_LevelOrderTraversal), (_java_key_5 := 'l'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]]
                    jcall(list, 'add', jget(cur, 'val'))
                    if (jget(cur, 'left') != None):
                        jset(Code01_LevelOrderTraversal.queue, ((_java_obj_7 := Code01_LevelOrderTraversal), (_java_key_8 := 'r'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4], jget(cur, 'left'))
                    if (jget(cur, 'right') != None):
                        jset(Code01_LevelOrderTraversal.queue, ((_java_obj_10 := Code01_LevelOrderTraversal), (_java_key_11 := 'r'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4], jget(cur, 'right'))
                    i = jcast('int', (i + 1))
                jcall(ans, 'add', list)
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_LevelOrderTraversal.MAXN = jcast('int', 2001)
Code01_LevelOrderTraversal.queue = jarray('TreeNode', [Code01_LevelOrderTraversal.MAXN])
Code01_LevelOrderTraversal.l = jcast('int', 0)
Code01_LevelOrderTraversal.r = jcast('int', 0)
