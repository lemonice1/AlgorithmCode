# -*- coding: utf-8 -*-
# Python 3 算法实现；中文题意、算法说明与原课程顺序对应。
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 用类描述实现前缀树。不推荐！
# 测试链接 : https://leetcode.cn/problems/implement-trie-ii-prefix-tree/
class Code01_TrieTree:
    __java_fields__ = {}
    # 路是数组实现的
    # 提交时把类名、构造方法改为Trie
    class Trie1:
        __java_fields__ = {'root': 'root'}
        class TrieNode:
            __java_fields__ = {'pass': 'pass_', 'end': 'end', 'nexts': 'nexts'}
            # pass_：实例字段，在构造函数中初始化。
            # end：实例字段，在构造函数中初始化。
            # nexts：实例字段，在构造函数中初始化。
            def _java_init_0(self):
                self.pass_ = jcast('int', 0)
                self.end = jcast('int', 0)
                self.nexts = jarray('TrieNode', [26])

            def __init__(self, *args, _java_ctor=None):
                self.pass_ = jcast('int', 0)
                self.end = jcast('int', 0)
                self.nexts = None
                _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
                if _java_choice == 0:
                    return self._java_init_0(*args)
                raise TypeError("No matching overload for Code01_TrieTree.Trie1.TrieNode.TrieNode")


        # root：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.root = Code01_TrieTree.Trie1.TrieNode(_java_ctor=0)

        def insert(self, word):
            node = self.root
            node.pass_ = jcast('int', (node.pass_ + 1))
            # 从左往右遍历字符
            i = jcast('int', 0)
            path = 0
            while (i < jcall(word, 'length')):
                # 由字符，对应成走向哪条路
                path = jcast('int', jcast('int', (jcall(word, 'charAt', i) - jchar('a'))))
                if (jget(node, 'nexts')[path] == None):
                    jset(jget(node, 'nexts'), path, Code01_TrieTree.Trie1.TrieNode(_java_ctor=0))
                node = jget(node, 'nexts')[path]
                node.pass_ = jcast('int', (node.pass_ + 1))
                i = jcast('int', (i + 1))
            node.end = jcast('int', (node.end + 1))

        # 如果之前word插入过前缀树，那么此时删掉一次
        # 如果之前word没有插入过前缀树，那么什么也不做
        def erase(self, word):
            if (self.countWordsEqualTo(word) > 0):
                node = self.root
                node.pass_ = jcast('int', (node.pass_ - 1))
                i = jcast('int', 0)
                path = 0
                while (i < jcall(word, 'length')):
                    path = jcast('int', jcast('int', (jcall(word, 'charAt', i) - jchar('a'))))
                    if (((_java_obj_1 := jget(node, 'nexts')[path]), (_java_key_2 := 'pass'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))))[3] == 0):
                        jset(jget(node, 'nexts'), path, None)
                        return
                    node = jget(node, 'nexts')[path]
                    i = jcast('int', (i + 1))
                node.end = jcast('int', (node.end - 1))

        # 查询前缀树里，word单词出现了几次
        def countWordsEqualTo(self, word):
            node = self.root
            i = jcast('int', 0)
            path = 0
            while (i < jcall(word, 'length')):
                path = jcast('int', jcast('int', (jcall(word, 'charAt', i) - jchar('a'))))
                if (jget(node, 'nexts')[path] == None):
                    return jcast('int', 0)
                node = jget(node, 'nexts')[path]
                i = jcast('int', (i + 1))
            return jcast('int', jget(node, 'end'))

        # 查询前缀树里，有多少单词以pre做前缀
        def countWordsStartingWith(self, pre):
            node = self.root
            i = jcast('int', 0)
            path = 0
            while (i < jcall(pre, 'length')):
                path = jcast('int', jcast('int', (jcall(pre, 'charAt', i) - jchar('a'))))
                if (jget(node, 'nexts')[path] == None):
                    return jcast('int', 0)
                node = jget(node, 'nexts')[path]
                i = jcast('int', (i + 1))
            return jcast('int', jget(node, 'pass'))

        def __init__(self, *args, _java_ctor=None):
            self.root = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_TrieTree.Trie1.Trie1")


    # 路是哈希表实现的
    # 提交时把类名、构造方法改为Trie
    class Trie2:
        __java_fields__ = {'root': 'root'}
        class TrieNode:
            __java_fields__ = {'pass': 'pass_', 'end': 'end', 'nexts': 'nexts'}
            # pass_：实例字段，在构造函数中初始化。
            # end：实例字段，在构造函数中初始化。
            # nexts：实例字段，在构造函数中初始化。
            def _java_init_0(self):
                self.pass_ = jcast('int', 0)
                self.end = jcast('int', 0)
                self.nexts = jnew('HashMap')

            def __init__(self, *args, _java_ctor=None):
                self.pass_ = jcast('int', 0)
                self.end = jcast('int', 0)
                self.nexts = None
                _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
                if _java_choice == 0:
                    return self._java_init_0(*args)
                raise TypeError("No matching overload for Code01_TrieTree.Trie2.TrieNode.TrieNode")


        # root：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.root = Code01_TrieTree.Trie2.TrieNode(_java_ctor=0)

        def insert(self, word):
            node = self.root
            node.pass_ = jcast('int', (node.pass_ + 1))
            # 从左往右遍历字符
            i = jcast('int', 0)
            path = 0
            while (i < jcall(word, 'length')):
                path = jcast('int', jcall(word, 'charAt', i))
                if (not jcall(jget(node, 'nexts'), 'containsKey', path)):
                    jcall(jget(node, 'nexts'), 'put', path, Code01_TrieTree.Trie2.TrieNode(_java_ctor=0))
                node = jcall(jget(node, 'nexts'), 'get', path)
                node.pass_ = jcast('int', (node.pass_ + 1))
                i = jcast('int', (i + 1))
            node.end = jcast('int', (node.end + 1))

        def erase(self, word):
            if (self.countWordsEqualTo(word) > 0):
                node = self.root
                next = None
                node.pass_ = jcast('int', (node.pass_ - 1))
                i = jcast('int', 0)
                path = 0
                while (i < jcall(word, 'length')):
                    path = jcast('int', jcall(word, 'charAt', i))
                    next = jcall(jget(node, 'nexts'), 'get', path)
                    if (((_java_obj_4 := next), (_java_key_5 := 'pass'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))))[3] == 0):
                        jcall(jget(node, 'nexts'), 'remove', path)
                        return
                    node = next
                    i = jcast('int', (i + 1))
                node.end = jcast('int', (node.end - 1))

        def countWordsEqualTo(self, word):
            node = self.root
            i = jcast('int', 0)
            path = 0
            while (i < jcall(word, 'length')):
                path = jcast('int', jcall(word, 'charAt', i))
                if (not jcall(jget(node, 'nexts'), 'containsKey', path)):
                    return jcast('int', 0)
                node = jcall(jget(node, 'nexts'), 'get', path)
                i = jcast('int', (i + 1))
            return jcast('int', jget(node, 'end'))

        def countWordsStartingWith(self, pre):
            node = self.root
            i = jcast('int', 0)
            path = 0
            while (i < jcall(pre, 'length')):
                path = jcast('int', jcall(pre, 'charAt', i))
                if (not jcall(jget(node, 'nexts'), 'containsKey', path)):
                    return jcast('int', 0)
                node = jcall(jget(node, 'nexts'), 'get', path)
                i = jcast('int', (i + 1))
            return jcast('int', jget(node, 'pass'))

        def __init__(self, *args, _java_ctor=None):
            self.root = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_TrieTree.Trie2.Trie2")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


