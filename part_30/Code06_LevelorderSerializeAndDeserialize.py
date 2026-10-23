# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 二叉树按层序列化和反序列化
# 测试链接 : https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/
class Code06_LevelorderSerializeAndDeserialize:
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
            raise TypeError("No matching overload for Code06_LevelorderSerializeAndDeserialize.TreeNode.TreeNode")


    # 提交这个类
    # 按层序列化
    class Codec:
        __java_fields__ = {}
        def serialize(self, root):
            builder = jnew('StringBuilder')
            if (root != None):
                jcall(builder, 'append', jadd(jget(root, 'val'), ','))
                # 修改了课上代码，改用自带的队列结构
                que = jnew('LinkedList')
                jcall(que, 'offer', root)
                while (not jcall(que, 'isEmpty')):
                    root = jcall(que, 'poll')
                    if (jget(root, 'left') != None):
                        jcall(builder, 'append', jadd(jget(jget(root, 'left'), 'val'), ','))
                        jcall(que, 'offer', jget(root, 'left'))
                    else:
                        jcall(builder, 'append', '#,')
                    if (jget(root, 'right') != None):
                        jcall(builder, 'append', jadd(jget(jget(root, 'right'), 'val'), ','))
                        jcall(que, 'offer', jget(root, 'right'))
                    else:
                        jcall(builder, 'append', '#,')
            return jcall(builder, 'toString')

        def deserialize(self, data):
            if jcall(data, 'equals', ''):
                return None
            nodes = jcall(data, 'split', ',')
            index = jcast('int', 0)
            root = self.generate(nodes[((_java_old_1 := index), (index := jcast('int', (index + (1)))), _java_old_1)[2]])
            # 修改了课上代码，改用自带的队列结构
            que = jnew('LinkedList')
            jcall(que, 'offer', root)
            while (not jcall(que, 'isEmpty')):
                cur = jcall(que, 'poll')
                jset(cur, 'left', self.generate(nodes[((_java_old_2 := index), (index := jcast('int', (index + (1)))), _java_old_2)[2]]))
                jset(cur, 'right', self.generate(nodes[((_java_old_3 := index), (index := jcast('int', (index + (1)))), _java_old_3)[2]]))
                if (jget(cur, 'left') != None):
                    jcall(que, 'offer', jget(cur, 'left'))
                if (jget(cur, 'right') != None):
                    jcall(que, 'offer', jget(cur, 'right'))
            return root

        def generate(self, val):
            return (None if jcall(val, 'equals', '#') else Code06_LevelorderSerializeAndDeserialize.TreeNode(jstatic('Integer', 'valueOf', val)))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


