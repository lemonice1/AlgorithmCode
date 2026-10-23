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

# 单词接龙
# 字典 wordList 中从单词 beginWord 和 endWord 的 转换序列
# 是一个按下述规格形成的序列 beginWord -> s1 -> s2 -> ... -> sk ：
# 每一对相邻的单词只差一个字母。
# 对于 1 <= i <= k 时，每个 si 都在 wordList 中
# 注意， beginWord 不需要在 wordList 中。sk == endWord
# 给你两个单词 beginWord 和 endWord 和一个字典 wordList
# 返回 从 beginWord 到 endWord 的 最短转换序列 中的 单词数目
# 如果不存在这样的转换序列，返回 0 。
# 测试链接 : https://leetcode.cn/problems/word-ladder/
class Code01_WordLadder:
    __java_fields__ = {}
    @staticmethod
    def ladderLength(begin, end, wordList):
        # 总词表
        dict = jnew('HashSet', wordList)
        if (not jcall(dict, 'contains', end)):
            return jcast('int', 0)
        # 数量小的一侧
        smallLevel = jnew('HashSet')
        # 数量大的一侧
        bigLevel = jnew('HashSet')
        # 由数量小的一侧，所扩展出的下一层列表
        nextLevel = jnew('HashSet')
        jcall(smallLevel, 'add', begin)
        jcall(bigLevel, 'add', end)
        len = jcast('int', 2)
        while (not jcall(smallLevel, 'isEmpty')):
            for w in smallLevel:
                # 从小侧扩展
                word = jcall(w, 'toCharArray')
                j = jcast('int', 0)
                while (j < jget(word, 'length')):
                    # 每一位字符都试
                    old = jcast('char', word[j])
                    change = jcast('char', jchar('a'))
                    while (change <= jchar('z')):
                        # 每一位字符都从a到z换一遍
                        if (change != old):
                            word[j] = jcast('char', change)
                            next = jstatic('String', 'valueOf', word)
                            if jcall(bigLevel, 'contains', next):
                                return jcast('int', len)
                            if jcall(dict, 'contains', next):
                                jcall(dict, 'remove', next)
                                jcall(nextLevel, 'add', next)
                        change = jcast('char', (change + 1))
                    word[j] = jcast('char', old)
                    j = jcast('int', (j + 1))
            if (jcall(nextLevel, 'size') <= jcall(bigLevel, 'size')):
                tmp = smallLevel
                smallLevel = nextLevel
                nextLevel = tmp
            else:
                tmp = smallLevel
                smallLevel = bigLevel
                bigLevel = nextLevel
                nextLevel = tmp
            jcall(nextLevel, 'clear')
            len = jcast('int', (len + 1))
        return jcast('int', 0)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


