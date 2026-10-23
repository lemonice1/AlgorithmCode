# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 单词接龙 II
# 按字典 wordList 完成从单词 beginWord 到单词 endWord 转化
# 一个表示此过程的 转换序列 是形式上像
# beginWord -> s1 -> s2 -> ... -> sk 这样的单词序列，并满足：
# 每对相邻的单词之间仅有单个字母不同
# 转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词
# 注意，beginWord 不必是字典 wordList 中的单词
# sk == endWord
# 给你两个单词 beginWord 和 endWord ，以及一个字典 wordList
# 请你找出并返回所有从 beginWord 到 endWord 的 最短转换序列
# 如果不存在这样的转换序列，返回一个空列表
# 每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk] 的形式返回
# 测试链接 : https://leetcode.cn/problems/word-ladder-ii/
class Code06_WordLadderII:
    __java_fields__ = {'dict': 'dict', 'curLevel': 'curLevel', 'nextLevel': 'nextLevel', 'graph': 'graph', 'path': 'path', 'ans': 'ans'}
    # 单词表 ： list -> hashSet
    dict = None
    curLevel = None
    nextLevel = None
    # 反向图
    graph = None
    # 记录路径，当生成一条有效路的时候，拷贝进ans！
    path = None
    ans = None
    @staticmethod
    def build(wordList):
        Code06_WordLadderII.dict = jnew('HashSet', wordList)
        jcall(Code06_WordLadderII.graph, 'clear')
        jcall(Code06_WordLadderII.ans, 'clear')
        jcall(Code06_WordLadderII.curLevel, 'clear')
        jcall(Code06_WordLadderII.nextLevel, 'clear')

    @staticmethod
    def findLadders(beginWord, endWord, wordList):
        Code06_WordLadderII.build(wordList)
        if (not jcall(Code06_WordLadderII.dict, 'contains', endWord)):
            return Code06_WordLadderII.ans
        if Code06_WordLadderII.bfs(beginWord, endWord):
            Code06_WordLadderII.dfs(endWord, beginWord)
        return Code06_WordLadderII.ans

    # begin -> end ，一层层bfs去，建图
    # 返回值：真的能找到end，返回true；false
    @staticmethod
    def bfs(begin, end):
        find = jcast('boolean', False)
        jcall(Code06_WordLadderII.curLevel, 'add', begin)
        while (not jcall(Code06_WordLadderII.curLevel, 'isEmpty')):
            jcall(Code06_WordLadderII.dict, 'removeAll', Code06_WordLadderII.curLevel)
            for word in Code06_WordLadderII.curLevel:
                # word : 去扩
                # 每个位置，字符a~z，换一遍！检查在词表中是否存在
                # 避免，加工出自己
                w = jcall(word, 'toCharArray')
                i = jcast('int', 0)
                while (i < jget(w, 'length')):
                    old = jcast('char', w[i])
                    ch = jcast('char', jchar('a'))
                    while (ch <= jchar('z')):
                        w[i] = jcast('char', ch)
                        str = jstatic('String', 'valueOf', w)
                        if (jcall(Code06_WordLadderII.dict, 'contains', str) and (not jcall(str, 'equals', word))):
                            if jcall(str, 'equals', end):
                                find = jcast('boolean', True)
                            jcall(Code06_WordLadderII.graph, 'putIfAbsent', str, jnew('ArrayList'))
                            jcall(jcall(Code06_WordLadderII.graph, 'get', str), 'add', word)
                            jcall(Code06_WordLadderII.nextLevel, 'add', str)
                        ch = jcast('char', (ch + 1))
                    w[i] = jcast('char', old)
                    i = jcast('int', (i + 1))
            if find:
                return jcast('boolean', True)
            else:
                tmp = Code06_WordLadderII.curLevel
                Code06_WordLadderII.curLevel = Code06_WordLadderII.nextLevel
                Code06_WordLadderII.nextLevel = tmp
                jcall(Code06_WordLadderII.nextLevel, 'clear')
        return jcast('boolean', False)

    @staticmethod
    def dfs(word, aim):
        jcall(Code06_WordLadderII.path, 'addFirst', word)
        if jcall(word, 'equals', aim):
            jcall(Code06_WordLadderII.ans, 'add', jnew('ArrayList', Code06_WordLadderII.path))
        else:
            if jcall(Code06_WordLadderII.graph, 'containsKey', word):
                for next in jcall(Code06_WordLadderII.graph, 'get', word):
                    Code06_WordLadderII.dfs(next, aim)
        jcall(Code06_WordLadderII.path, 'removeFirst')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_WordLadderII.dict = None
Code06_WordLadderII.curLevel = jnew('HashSet')
Code06_WordLadderII.nextLevel = jnew('HashSet')
Code06_WordLadderII.graph = jnew('HashMap')
Code06_WordLadderII.path = jnew('LinkedList')
Code06_WordLadderII.ans = jnew('ArrayList')
