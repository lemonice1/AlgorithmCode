# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 单词搜索（无法改成动态规划）
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word
# 如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成
# 其中"相邻"单元格是那些水平相邻或垂直相邻的单元格
# 同一个单元格内的字母不允许被重复使用
# 测试链接 : https://leetcode.cn/problems/word-search/
class Code02_WordSearch:
    __java_fields__ = {}
    @staticmethod
    def exist(board, word):
        w = jcall(word, 'toCharArray')
        i = jcast('int', 0)
        while (i < jget(board, 'length')):
            j = jcast('int', 0)
            while (j < jget(board[0], 'length')):
                if Code02_WordSearch.f(board, i, j, w, 0):
                    return jcast('boolean', True)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('boolean', False)

    # 因为board会改其中的字符
    # 用来标记哪些字符无法再用
    # 带路径的递归无法改成动态规划或者说没必要
    # 从(i,j)出发，来到w[k]，请问后续能不能把word走出来w[k...]
    @staticmethod
    def f(b, i, j, w, k):
        i = jcast('int', i)
        j = jcast('int', j)
        k = jcast('int', k)
        if (k == jget(w, 'length')):
            return jcast('boolean', True)
        if (((((i < 0) or (i == jget(b, 'length'))) or (j < 0)) or (j == jget(b[0], 'length'))) or (b[i][j] != w[k])):
            return jcast('boolean', False)
        # 不越界，b[i][j] == w[k]
        tmp = jcast('char', b[i][j])
        jset(b[i], j, 0)
        ans = jcast('boolean', (((Code02_WordSearch.f(b, jcast('int', (i - 1)), j, w, jcast('int', jadd(k, 1))) or Code02_WordSearch.f(b, jcast('int', jadd(i, 1)), j, w, jcast('int', jadd(k, 1)))) or Code02_WordSearch.f(b, i, jcast('int', (j - 1)), w, jcast('int', jadd(k, 1)))) or Code02_WordSearch.f(b, i, jcast('int', jadd(j, 1)), w, jcast('int', jadd(k, 1)))))
        jset(b[i], j, tmp)
        return jcast('boolean', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


