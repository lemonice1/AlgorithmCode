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

# 贴纸拼词
# 我们有 n 种不同的贴纸。每个贴纸上都有一个小写的英文单词。
# 您想要拼写出给定的字符串 target ，方法是从收集的贴纸中切割单个字母并重新排列它们
# 如果你愿意，你可以多次使用每个贴纸，每个贴纸的数量是无限的。
# 返回你需要拼出 target 的最小贴纸数量。如果任务不可能，则返回 -1
# 注意：在所有的测试用例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选择的
# 并且 target 被选择为两个随机单词的连接。
# 测试链接 : https://leetcode.cn/problems/stickers-to-spell-word/
class Code02_StickersToSpellWord:
    __java_fields__ = {'MAXN': 'MAXN', 'queue': 'queue', 'l': 'l', 'r': 'r', 'graph': 'graph', 'visited': 'visited'}
    MAXN = 0
    queue = None
    l = 0
    r = 0
    # 下标0 -> a
    # 下标1 -> b
    # 下标2 -> c
    # ...
    # 下标25 -> z
    graph = None
    visited = None
    # 宽度优先遍历的解法
    # 也可以使用动态规划
    # 后续课程会有动态规划专题讲解
    @staticmethod
    def minStickers(stickers, target):
        i = jcast('int', 0)
        while (i < 26):
            jcall(jcall(Code02_StickersToSpellWord.graph, 'get', i), 'clear')
            i = jcast('int', (i + 1))
        jcall(Code02_StickersToSpellWord.visited, 'clear')
        for str in stickers:
            str = Code02_StickersToSpellWord.sort(str)
            i = jcast('int', 0)
            while (i < jcall(str, 'length')):
                if ((i == 0) or (jcall(str, 'charAt', i) != jcall(str, 'charAt', jcast('int', (i - 1))))):
                    jcall(jcall(Code02_StickersToSpellWord.graph, 'get', jcast('int', (jcall(str, 'charAt', i) - jchar('a')))), 'add', str)
                i = jcast('int', (i + 1))
        target = Code02_StickersToSpellWord.sort(target)
        jcall(Code02_StickersToSpellWord.visited, 'add', target)
        Code02_StickersToSpellWord.l = jcast('int', jset(Code02_StickersToSpellWord, 'r', 0))
        jset(Code02_StickersToSpellWord.queue, ((_java_obj_1 := Code02_StickersToSpellWord), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], target)
        level = jcast('int', 1)
        # 使用队列的形式是整层弹出
        while (Code02_StickersToSpellWord.l < Code02_StickersToSpellWord.r):
            size = jcast('int', jcast('int', (Code02_StickersToSpellWord.r - Code02_StickersToSpellWord.l)))
            i = jcast('int', 0)
            while (i < size):
                cur = Code02_StickersToSpellWord.queue[((_java_obj_4 := Code02_StickersToSpellWord), (_java_key_5 := 'l'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]]
                for s in jcall(Code02_StickersToSpellWord.graph, 'get', jcast('int', (jcall(cur, 'charAt', 0) - jchar('a')))):
                    next = Code02_StickersToSpellWord.next(cur, s)
                    if jcall(next, 'equals', ''):
                        return jcast('int', level)
                    else:
                        if (not jcall(Code02_StickersToSpellWord.visited, 'contains', next)):
                            jcall(Code02_StickersToSpellWord.visited, 'add', next)
                            jset(Code02_StickersToSpellWord.queue, ((_java_obj_7 := Code02_StickersToSpellWord), (_java_key_8 := 'r'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4], next)
                i = jcast('int', (i + 1))
            level = jcast('int', (level + 1))
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def sort(str):
        s = jcall(str, 'toCharArray')
        jstatic('Arrays', 'sort', s)
        return jstatic('String', 'valueOf', s)

    @staticmethod
    def next(t, s):
        builder = jnew('StringBuilder')
        i = jcast('int', 0)
        j = jcast('int', 0)
        while (i < jcall(t, 'length')):
            if (j == jcall(s, 'length')):
                jcall(builder, 'append', jcall(t, 'charAt', ((_java_old_10 := i), (i := jcast('int', (i + (1)))), _java_old_10)[2]))
            else:
                if (jcall(t, 'charAt', i) < jcall(s, 'charAt', j)):
                    jcall(builder, 'append', jcall(t, 'charAt', ((_java_old_11 := i), (i := jcast('int', (i + (1)))), _java_old_11)[2]))
                else:
                    if (jcall(t, 'charAt', i) > jcall(s, 'charAt', j)):
                        j = jcast('int', (j + 1))
                    else:
                        i = jcast('int', (i + 1))
                        j = jcast('int', (j + 1))
        return jcall(builder, 'toString')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_StickersToSpellWord.MAXN = jcast('int', 401)
Code02_StickersToSpellWord.queue = jarray('String', [Code02_StickersToSpellWord.MAXN])
Code02_StickersToSpellWord.l = jcast('int', 0)
Code02_StickersToSpellWord.r = jcast('int', 0)
Code02_StickersToSpellWord.graph = jnew('ArrayList')
i = jcast('int', 0)
while (i < 26):
    jcall(Code02_StickersToSpellWord.graph, 'add', jnew('ArrayList'))
    i = jcast('int', (i + 1))
Code02_StickersToSpellWord.visited = jnew('HashSet')
