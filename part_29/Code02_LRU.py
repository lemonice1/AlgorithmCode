# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 实现LRU结构
class Code02_LRU:
    __java_fields__ = {}
    # 测试链接 : https://leetcode.cn/problems/lru-cache/
    class LRUCache:
        __java_fields__ = {'keyNodeMap': 'keyNodeMap', 'nodeList': 'nodeList', 'capacity': 'capacity'}
        class DoubleNode:
            __java_fields__ = {'key': 'key', 'val': 'val', 'last': 'last', 'next': 'next'}
            # key：实例字段，在构造函数中初始化。
            # val：实例字段，在构造函数中初始化。
            # last：实例字段，在构造函数中初始化。
            # next：实例字段，在构造函数中初始化。
            def _java_init_0(self, k, v):
                k = jcast('int', k)
                v = jcast('int', v)
                self.key = jcast('int', k)
                self.val = jcast('int', v)

            def __init__(self, *args, _java_ctor=None):
                self.key = jcast('int', 0)
                self.val = jcast('int', 0)
                self.last = None
                self.next = None
                _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int', 'int']], [False])
                if _java_choice == 0:
                    return self._java_init_0(*args)
                raise TypeError("No matching overload for Code02_LRU.LRUCache.DoubleNode.DoubleNode")


        class DoubleList:
            __java_fields__ = {'head': 'head', 'tail': 'tail'}
            # head：实例字段，在构造函数中初始化。
            # tail：实例字段，在构造函数中初始化。
            def _java_init_0(self):
                self.head = None
                self.tail = None

            def addNode(self, newNode):
                if (newNode == None):
                    return
                if (self.head == None):
                    self.head = newNode
                    self.tail = newNode
                else:
                    jset(self.tail, 'next', newNode)
                    newNode.last = self.tail
                    self.tail = newNode

            def moveNodeToTail(self, node):
                if (self.tail == node):
                    return
                if (self.head == node):
                    self.head = jget(node, 'next')
                    jset(self.head, 'last', None)
                else:
                    jset(jget(node, 'last'), 'next', jget(node, 'next'))
                    jset(jget(node, 'next'), 'last', jget(node, 'last'))
                node.last = self.tail
                node.next = None
                jset(self.tail, 'next', node)
                self.tail = node

            def removeHead(self):
                if (self.head == None):
                    return None
                ans = self.head
                if (self.head == self.tail):
                    self.head = None
                    self.tail = None
                else:
                    self.head = jget(ans, 'next')
                    ans.next = None
                    jset(self.head, 'last', None)
                return ans

            def __init__(self, *args, _java_ctor=None):
                self.head = None
                self.tail = None
                _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
                if _java_choice == 0:
                    return self._java_init_0(*args)
                raise TypeError("No matching overload for Code02_LRU.LRUCache.DoubleList.DoubleList")


        # keyNodeMap：实例字段，在构造函数中初始化。
        # nodeList：实例字段，在构造函数中初始化。
        # capacity：实例字段，在构造函数中初始化。
        def _java_init_0(self, cap):
            cap = jcast('int', cap)
            self.keyNodeMap = jnew('HashMap')
            self.nodeList = Code02_LRU.LRUCache.DoubleList(_java_ctor=0)
            self.capacity = jcast('int', cap)

        def get(self, key):
            key = jcast('int', key)
            if jcall(self.keyNodeMap, 'containsKey', key):
                ans = jcall(self.keyNodeMap, 'get', key)
                jcall(self.nodeList, 'moveNodeToTail', ans)
                return jcast('int', jget(ans, 'val'))
            return jcast('int', jcast('int', (-1)))

        def put(self, key, value):
            key = jcast('int', key)
            value = jcast('int', value)
            if jcall(self.keyNodeMap, 'containsKey', key):
                node = jcall(self.keyNodeMap, 'get', key)
                node.val = jcast('int', value)
                jcall(self.nodeList, 'moveNodeToTail', node)
            else:
                if (jcall(self.keyNodeMap, 'size') == self.capacity):
                    jcall(self.keyNodeMap, 'remove', jget(jcall(self.nodeList, 'removeHead'), 'key'))
                newNode = Code02_LRU.LRUCache.DoubleNode(key, value, _java_ctor=0)
                jcall(self.keyNodeMap, 'put', key, newNode)
                jcall(self.nodeList, 'addNode', newNode)

        def __init__(self, *args, _java_ctor=None):
            self.keyNodeMap = None
            self.nodeList = None
            self.capacity = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_LRU.LRUCache.LRUCache")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


