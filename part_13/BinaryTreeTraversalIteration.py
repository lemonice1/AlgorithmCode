# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 不用递归，用迭代的方式实现二叉树的三序遍历
class BinaryTreeTraversalIteration:
    __java_fields__ = {}
    class TreeNode:
        __java_fields__ = {'val': 'val', 'left': 'left', 'right': 'right'}
        # val：实例字段，在构造函数中初始化。
        # left：实例字段，在构造函数中初始化。
        # right：实例字段，在构造函数中初始化。
        def _java_init_0(self, v):
            v = jcast('int', v)
            self.val = jcast('int', v)

        def __init__(self, *args, _java_ctor=None):
            self.val = jcast('int', 0)
            self.left = None
            self.right = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for BinaryTreeTraversalIteration.TreeNode.TreeNode")


    # 先序打印所有节点，非递归版
    @staticmethod
    def preOrder(head):
        if (head != None):
            stack = jnew('Stack')
            jcall(stack, 'push', head)
            while (not jcall(stack, 'isEmpty')):
                head = jcall(stack, 'pop')
                jprint(jadd(jget(head, 'val'), ' '), newline=False)
                if (jget(head, 'right') != None):
                    jcall(stack, 'push', jget(head, 'right'))
                if (jget(head, 'left') != None):
                    jcall(stack, 'push', jget(head, 'left'))
            jprint(newline=True)

    # 中序打印所有节点，非递归版
    @staticmethod
    def inOrder(head):
        if (head != None):
            stack = jnew('Stack')
            while ((not jcall(stack, 'isEmpty')) or (head != None)):
                if (head != None):
                    jcall(stack, 'push', head)
                    head = jget(head, 'left')
                else:
                    head = jcall(stack, 'pop')
                    jprint(jadd(jget(head, 'val'), ' '), newline=False)
                    head = jget(head, 'right')
            jprint(newline=True)

    # 后序打印所有节点，非递归版
    # 这是用两个栈的方法
    @staticmethod
    def posOrderTwoStacks(head):
        if (head != None):
            stack = jnew('Stack')
            collect = jnew('Stack')
            jcall(stack, 'push', head)
            while (not jcall(stack, 'isEmpty')):
                head = jcall(stack, 'pop')
                jcall(collect, 'push', head)
                if (jget(head, 'left') != None):
                    jcall(stack, 'push', jget(head, 'left'))
                if (jget(head, 'right') != None):
                    jcall(stack, 'push', jget(head, 'right'))
            while (not jcall(collect, 'isEmpty')):
                jprint(jadd(jget(jcall(collect, 'pop'), 'val'), ' '), newline=False)
            jprint(newline=True)

    # 后序打印所有节点，非递归版
    # 这是用一个栈的方法
    @staticmethod
    def posOrderOneStack(h):
        if (h != None):
            stack = jnew('Stack')
            jcall(stack, 'push', h)
            # 如果始终没有打印过节点，h就一直是头节点
            # 一旦打印过节点，h就变成打印节点
            # 之后h的含义 : 上一次打印的节点
            while (not jcall(stack, 'isEmpty')):
                cur = jcall(stack, 'peek')
                if (((jget(cur, 'left') != None) and (h != jget(cur, 'left'))) and (h != jget(cur, 'right'))):
                    # 有左树且左树没处理过
                    jcall(stack, 'push', jget(cur, 'left'))
                else:
                    if ((jget(cur, 'right') != None) and (h != jget(cur, 'right'))):
                        # 有右树且右树没处理过
                        jcall(stack, 'push', jget(cur, 'right'))
                    else:
                        # 左树、右树 没有 或者 都处理过了
                        jprint(jadd(jget(cur, 'val'), ' '), newline=False)
                        h = jcall(stack, 'pop')
            jprint(newline=True)

    @staticmethod
    def main(args):
        head = BinaryTreeTraversalIteration.TreeNode(1, _java_ctor=0)
        jset(head, 'left', BinaryTreeTraversalIteration.TreeNode(2, _java_ctor=0))
        jset(head, 'right', BinaryTreeTraversalIteration.TreeNode(3, _java_ctor=0))
        jset(jget(head, 'left'), 'left', BinaryTreeTraversalIteration.TreeNode(4, _java_ctor=0))
        jset(jget(head, 'left'), 'right', BinaryTreeTraversalIteration.TreeNode(5, _java_ctor=0))
        jset(jget(head, 'right'), 'left', BinaryTreeTraversalIteration.TreeNode(6, _java_ctor=0))
        jset(jget(head, 'right'), 'right', BinaryTreeTraversalIteration.TreeNode(7, _java_ctor=0))
        BinaryTreeTraversalIteration.preOrder(head)
        jprint('先序遍历非递归版', newline=True)
        BinaryTreeTraversalIteration.inOrder(head)
        jprint('中序遍历非递归版', newline=True)
        BinaryTreeTraversalIteration.posOrderTwoStacks(head)
        jprint('后序遍历非递归版 - 2个栈实现', newline=True)
        BinaryTreeTraversalIteration.posOrderOneStack(head)
        jprint('后序遍历非递归版 - 1个栈实现', newline=True)

    # 用一个栈完成先序遍历
    # 测试链接 : https://leetcode.cn/problems/binary-tree-preorder-traversal/
    @staticmethod
    def preorderTraversal(head):
        ans = jnew('ArrayList')
        if (head != None):
            stack = jnew('Stack')
            jcall(stack, 'push', head)
            while (not jcall(stack, 'isEmpty')):
                head = jcall(stack, 'pop')
                jcall(ans, 'add', jget(head, 'val'))
                if (jget(head, 'right') != None):
                    jcall(stack, 'push', jget(head, 'right'))
                if (jget(head, 'left') != None):
                    jcall(stack, 'push', jget(head, 'left'))
        return ans

    # 用一个栈完成中序遍历
    # 测试链接 : https://leetcode.cn/problems/binary-tree-inorder-traversal/
    @staticmethod
    def inorderTraversal(head):
        ans = jnew('ArrayList')
        if (head != None):
            stack = jnew('Stack')
            while ((not jcall(stack, 'isEmpty')) or (head != None)):
                if (head != None):
                    jcall(stack, 'push', head)
                    head = jget(head, 'left')
                else:
                    head = jcall(stack, 'pop')
                    jcall(ans, 'add', jget(head, 'val'))
                    head = jget(head, 'right')
        return ans

    # 用两个栈完成后序遍历
    # 提交时函数名改为postorderTraversal
    # 测试链接 : https://leetcode.cn/problems/binary-tree-postorder-traversal/
    @staticmethod
    def postorderTraversalTwoStacks(head):
        ans = jnew('ArrayList')
        if (head != None):
            stack = jnew('Stack')
            collect = jnew('Stack')
            jcall(stack, 'push', head)
            while (not jcall(stack, 'isEmpty')):
                head = jcall(stack, 'pop')
                jcall(collect, 'push', head)
                if (jget(head, 'left') != None):
                    jcall(stack, 'push', jget(head, 'left'))
                if (jget(head, 'right') != None):
                    jcall(stack, 'push', jget(head, 'right'))
            while (not jcall(collect, 'isEmpty')):
                jcall(ans, 'add', jget(jcall(collect, 'pop'), 'val'))
        return ans

    # 用一个栈完成后序遍历
    # 提交时函数名改为postorderTraversal
    # 测试链接 : https://leetcode.cn/problems/binary-tree-postorder-traversal/
    @staticmethod
    def postorderTraversalOneStack(h):
        ans = jnew('ArrayList')
        if (h != None):
            stack = jnew('Stack')
            jcall(stack, 'push', h)
            while (not jcall(stack, 'isEmpty')):
                cur = jcall(stack, 'peek')
                if (((jget(cur, 'left') != None) and (h != jget(cur, 'left'))) and (h != jget(cur, 'right'))):
                    jcall(stack, 'push', jget(cur, 'left'))
                else:
                    if ((jget(cur, 'right') != None) and (h != jget(cur, 'right'))):
                        jcall(stack, 'push', jget(cur, 'right'))
                    else:
                        jcall(ans, 'add', jget(cur, 'val'))
                        h = jcall(stack, 'pop')
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    BinaryTreeTraversalIteration.main([])
