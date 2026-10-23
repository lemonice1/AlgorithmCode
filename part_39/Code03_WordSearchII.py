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

# 在二维字符数组中搜索可能的单词
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words
# 返回所有二维网格上的单词。单词必须按照字母顺序，通过 相邻的单元格 内的字母构成
# 其中“相邻”单元格是那些水平相邻或垂直相邻的单元格
# 同一个单元格内的字母在一个单词中不允许被重复使用
# 1 <= m, n <= 12
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# 测试链接 : https://leetcode.cn/problems/word-search-ii/
class Code03_WordSearchII:
    __java_fields__ = {'MAXN': 'MAXN', 'tree': 'tree', 'pass': 'pass_', 'end': 'end', 'cnt': 'cnt'}
    @staticmethod
    def findWords(board, words):
        Code03_WordSearchII.build(words)
        ans = jnew('ArrayList')
        i = jcast('int', 0)
        while (i < jget(board, 'length')):
            j = jcast('int', 0)
            while (j < jget(board[0], 'length')):
                Code03_WordSearchII.dfs(board, i, j, 1, ans)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        Code03_WordSearchII.clear()
        return ans

    # board : 二维网格
    # i,j : 此时来到的格子位置，i行、j列
    # t : 前缀树的编号
    # List<String> ans : 收集到了哪些字符串，都放入ans
    # 返回值 : 收集到了几个字符串
    @staticmethod
    def dfs(board, i, j, t, ans):
        i = jcast('int', i)
        j = jcast('int', j)
        t = jcast('int', t)
        # 越界 或者 走了回头路，直接返回0
        if (((((i < 0) or (i == jget(board, 'length'))) or (j < 0)) or (j == jget(board[0], 'length'))) or (board[i][j] == 0)):
            return jcast('int', 0)
        # 不越界 且 不是回头路
        # 用tmp记录当前字符
        tmp = jcast('char', board[i][j])
        # 路的编号
        # a -> 0
        # b -> 1
        # ...
        # z -> 25
        road = jcast('int', jcast('int', (tmp - jchar('a'))))
        t = jcast('int', Code03_WordSearchII.tree[t][road])
        if (Code03_WordSearchII.pass_[t] == 0):
            return jcast('int', 0)
        # i，j位置有必要来
        # fix ：从当前i，j位置出发，一共收集到了几个字符串
        fix = jcast('int', 0)
        if (Code03_WordSearchII.end[t] != None):
            fix = jcast('int', (fix + 1))
            jcall(ans, 'add', Code03_WordSearchII.end[t])
            Code03_WordSearchII.end[t] = None
        # 把i，j位置的字符，改成0，后续的过程，是不可以再来到i，j位置的！
        jset(board[i], j, 0)
        fix = jcast('int', jcast('int', jadd(fix, Code03_WordSearchII.dfs(board, jcast('int', (i - 1)), j, t, ans))))
        fix = jcast('int', jcast('int', jadd(fix, Code03_WordSearchII.dfs(board, jcast('int', jadd(i, 1)), j, t, ans))))
        fix = jcast('int', jcast('int', jadd(fix, Code03_WordSearchII.dfs(board, i, jcast('int', (j - 1)), t, ans))))
        fix = jcast('int', jcast('int', jadd(fix, Code03_WordSearchII.dfs(board, i, jcast('int', jadd(j, 1)), t, ans))))
        Code03_WordSearchII.pass_[t] = jcast('int', jcast('int', (Code03_WordSearchII.pass_[t] - fix)))
        jset(board[i], j, tmp)
        return jcast('int', fix)

    MAXN = 0
    tree = None
    pass_ = None
    end = None
    cnt = 0
    @staticmethod
    def build(words):
        Code03_WordSearchII.cnt = jcast('int', 1)
        for word in words:
            cur = jcast('int', 1)
            Code03_WordSearchII.pass_[cur] = jcast('int', (Code03_WordSearchII.pass_[cur] + 1))
            i = jcast('int', 0)
            path = 0
            while (i < jcall(word, 'length')):
                path = jcast('int', jcast('int', (jcall(word, 'charAt', i) - jchar('a'))))
                if (Code03_WordSearchII.tree[cur][path] == 0):
                    jset(Code03_WordSearchII.tree[cur], path, ((_java_obj_1 := Code03_WordSearchII), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
                cur = jcast('int', Code03_WordSearchII.tree[cur][path])
                Code03_WordSearchII.pass_[cur] = jcast('int', (Code03_WordSearchII.pass_[cur] + 1))
                i = jcast('int', (i + 1))
            Code03_WordSearchII.end[cur] = word

    @staticmethod
    def clear():
        i = jcast('int', 1)
        while (i <= Code03_WordSearchII.cnt):
            jstatic('Arrays', 'fill', Code03_WordSearchII.tree[i], 0)
            Code03_WordSearchII.pass_[i] = jcast('int', 0)
            Code03_WordSearchII.end[i] = None
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_WordSearchII.MAXN = jcast('int', 10001)
Code03_WordSearchII.tree = jarray('int', [Code03_WordSearchII.MAXN, 26])
Code03_WordSearchII.pass_ = jarray('int', [Code03_WordSearchII.MAXN])
Code03_WordSearchII.end = jarray('String', [Code03_WordSearchII.MAXN])
Code03_WordSearchII.cnt = jcast('int', 0)
