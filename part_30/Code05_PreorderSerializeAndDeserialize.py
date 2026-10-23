# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 二叉树先序序列化和反序列化
# 测试链接 : https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/
class Code05_PreorderSerializeAndDeserialize:
    __java_fields__ = {}
    # 不提交这个类
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
            raise TypeError("No matching overload for Code05_PreorderSerializeAndDeserialize.TreeNode.TreeNode")


    # 二叉树可以通过先序、后序或者按层遍历的方式序列化和反序列化
    # 但是，二叉树无法通过中序遍历的方式实现序列化和反序列化
    # 因为不同的两棵树，可能得到同样的中序序列，即便补了空位置也可能一样。
    # 比如如下两棵树
    # __2
    # /
    # 1
    # 和
    # 1__
    # \
    # 2
    # 补足空位置的中序遍历结果都是{ null, 1, null, 2, null}
    # 提交这个类
    class Codec:
        __java_fields__ = {}
        def serialize(self, root):
            builder = jnew('StringBuilder')
            self.f(root, builder)
            return jcall(builder, 'toString')

        def f(self, root, builder):
            if (root == None):
                jcall(builder, 'append', '#,')
            else:
                jcall(builder, 'append', jadd(jget(root, 'val'), ','))
                self.f(jget(root, 'left'), builder)
                self.f(jget(root, 'right'), builder)

        # leetcode增加了本题的限制
        # 不允许使用外部变量传递信息
        # 所以改用自带的队列结构
        # 消费队列中的字符串
        def deserialize(self, data):
            vals = jnew('LinkedList')
            for v in jcall(data, 'split', ','):
                jcall(vals, 'offer', v)
            return self.g(vals)

        def g(self, vals):
            cur = jcall(vals, 'poll')
            if jcall(cur, 'equals', '#'):
                return None
            else:
                head = Code05_PreorderSerializeAndDeserialize.TreeNode(jstatic('Integer', 'valueOf', cur))
                jset(head, 'left', self.g(vals))
                jset(head, 'right', self.g(vals))
                return head

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


