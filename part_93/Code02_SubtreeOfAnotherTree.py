# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 另一棵树的子树
# 给你两棵二叉树root和subRoot
# 检验root中是否包含和subRoot具有相同结构和节点值的子树
# 如果存在，返回true
# 否则，返回false
# 测试链接 : https://leetcode.cn/problems/subtree-of-another-tree/
class Code02_SubtreeOfAnotherTree:
    __java_fields__ = {}
    # 不要提交这个类
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


    # 方法1
    # 暴力递归
    # 时间复杂度O(n * m)
    @staticmethod
    def isSubtree(t1, t2):
        if ((t1 != None) and (t2 != None)):
            return jcast('boolean', ((Code02_SubtreeOfAnotherTree.same(t1, t2) or Code02_SubtreeOfAnotherTree.isSubtree(jget(t1, 'left'), t2)) or Code02_SubtreeOfAnotherTree.isSubtree(jget(t1, 'right'), t2)))
        return jcast('boolean', (t2 == None))

    # 判断a和b这两棵树是否完全一样
    @staticmethod
    def same(a, b):
        if ((a == None) and (b == None)):
            return jcast('boolean', True)
        if ((a != None) and (b != None)):
            return jcast('boolean', (((jget(a, 'val') == jget(b, 'val')) and Code02_SubtreeOfAnotherTree.same(jget(a, 'left'), jget(b, 'left'))) and Code02_SubtreeOfAnotherTree.same(jget(a, 'right'), jget(b, 'right'))))
        return jcast('boolean', False)

    # 方法2
    # 二叉树先序序列化 + KMP算法匹配
    # 时间复杂度O(n + m)
    @staticmethod
    def isSubtree2(t1, t2):
        if ((t1 != None) and (t2 != None)):
            s1 = jnew('ArrayList')
            s2 = jnew('ArrayList')
            Code02_SubtreeOfAnotherTree.serial(t1, s1)
            Code02_SubtreeOfAnotherTree.serial(t2, s2)
            return jcast('boolean', (Code02_SubtreeOfAnotherTree.kmp(s1, s2) != jcast('int', (-1))))
        return jcast('boolean', (t2 == None))

    @staticmethod
    def serial(head, path):
        if (head == None):
            jcall(path, 'add', None)
        else:
            jcall(path, 'add', jstatic('String', 'valueOf', jget(head, 'val')))
            Code02_SubtreeOfAnotherTree.serial(jget(head, 'left'), path)
            Code02_SubtreeOfAnotherTree.serial(jget(head, 'right'), path)

    @staticmethod
    def kmp(s1, s2):
        n = jcast('int', jcall(s1, 'size'))
        m = jcast('int', jcall(s2, 'size'))
        x = jcast('int', 0)
        y = jcast('int', 0)
        next = Code02_SubtreeOfAnotherTree.nextArray(s2, m)
        while ((x < n) and (y < m)):
            if Code02_SubtreeOfAnotherTree.isEqual(jcall(s1, 'get', x), jcall(s2, 'get', y)):
                x = jcast('int', (x + 1))
                y = jcast('int', (y + 1))
            else:
                if (y == 0):
                    x = jcast('int', (x + 1))
                else:
                    y = jcast('int', next[y])
        return jcast('int', (jcast('int', (x - y)) if (y == m) else jcast('int', (-1))))

    @staticmethod
    def nextArray(s, m):
        m = jcast('int', m)
        if (m == 1):
            return jarray('int', [None], [jcast('int', (-1))])
        next = jarray('int', [m])
        next[0] = jcast('int', jcast('int', (-1)))
        next[1] = jcast('int', 0)
        i = jcast('int', 2)
        cn = jcast('int', 0)
        while (i < jget(next, 'length')):
            if Code02_SubtreeOfAnotherTree.isEqual(jcall(s, 'get', jcast('int', (i - 1))), jcall(s, 'get', cn)):
                jset(next, ((_java_old_1 := i), (i := jcast('int', (i + (1)))), _java_old_1)[2], (cn := jcast('int', (cn + (1)))))
            else:
                if (cn > 0):
                    cn = jcast('int', next[cn])
                else:
                    jset(next, ((_java_old_2 := i), (i := jcast('int', (i + (1)))), _java_old_2)[2], 0)
        return next

    # 比对两个字符串是否相等
    # a和b可能为null
    @staticmethod
    def isEqual(a, b):
        if ((a == None) and (b == None)):
            return jcast('boolean', True)
        if ((a != None) and (b != None)):
            return jcast('boolean', jcall(a, 'equals', b))
        return jcast('boolean', False)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


