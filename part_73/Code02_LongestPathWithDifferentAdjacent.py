# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 相邻字符不同的最长路径
# 给你一棵 树（即一个连通、无向、无环图），根节点是节点 0
# 这棵树由编号从 0 到 n - 1 的 n 个节点组成
# 用下标从 0 开始、长度为 n 的数组 parent 来表示这棵树
# 其中 parent[i] 是节点 i 的父节点
# 由于节点 0 是根节点，所以 parent[0] == -1
# 另给你一个字符串 s ，长度也是 n ，其中 s[i] 表示分配给节点 i 的字符
# 请你找出路径上任意一对相邻节点都没有分配到相同字符的 最长路径
# 并返回该路径的长度
# 测试链接 : https://leetcode.cn/problems/longest-path-with-different-adjacent-characters/
class Code02_LongestPathWithDifferentAdjacent:
    __java_fields__ = {}
    @staticmethod
    def longestPath(parent, str):
        n = jcast('int', jget(parent, 'length'))
        s = jcall(str, 'toCharArray')
        graph = jnew('ArrayList')
        i = jcast('int', 0)
        while (i < n):
            jcall(graph, 'add', jnew('ArrayList'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < n):
            jcall(jcall(graph, 'get', parent[i]), 'add', i)
            i = jcast('int', (i + 1))
        return jcast('int', jget(Code02_LongestPathWithDifferentAdjacent.f(s, graph, 0), 'maxPath'))

    class Info:
        __java_fields__ = {'maxPathFromHead': 'maxPathFromHead', 'maxPath': 'maxPath'}
        # 一定要从头节点出发的情况下，相邻字符不等的最长路径长度
        # maxPathFromHead：实例字段，在构造函数中初始化。
        # 整棵树上，相邻字符不等的最长路径长度
        # maxPath：实例字段，在构造函数中初始化。
        def _java_init_0(self, a, b):
            a = jcast('int', a)
            b = jcast('int', b)
            self.maxPathFromHead = jcast('int', a)
            self.maxPath = jcast('int', b)

        def __init__(self, *args, _java_ctor=None):
            self.maxPathFromHead = jcast('int', 0)
            self.maxPath = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int', 'int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_LongestPathWithDifferentAdjacent.Info.Info")


    @staticmethod
    def f(s, graph, u):
        u = jcast('int', u)
        if jcall(jcall(graph, 'get', u), 'isEmpty'):
            # u节点是叶
            return Code02_LongestPathWithDifferentAdjacent.Info(1, 1, _java_ctor=0)
        # 下方最长链
        max1 = jcast('int', 0)
        # 下方次长链
        max2 = jcast('int', 0)
        maxPath = jcast('int', 1)
        for v in jcall(graph, 'get', u):
            nextInfo = Code02_LongestPathWithDifferentAdjacent.f(s, graph, v)
            maxPath = jcast('int', jstatic('Math', 'max', maxPath, jget(nextInfo, 'maxPath')))
            if (s[u] != s[v]):
                if (jget(nextInfo, 'maxPathFromHead') > max1):
                    max2 = jcast('int', max1)
                    max1 = jcast('int', jget(nextInfo, 'maxPathFromHead'))
                else:
                    if (jget(nextInfo, 'maxPathFromHead') > max2):
                        max2 = jcast('int', jget(nextInfo, 'maxPathFromHead'))
        maxPathFromHead = jcast('int', jcast('int', jadd(max1, 1)))
        maxPath = jcast('int', jstatic('Math', 'max', maxPath, jcast('int', jadd(jcast('int', jadd(max1, max2)), 1))))
        return Code02_LongestPathWithDifferentAdjacent.Info(maxPathFromHead, maxPath, _java_ctor=0)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


