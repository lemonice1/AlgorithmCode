# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 串联所有单词的子串
# 给定一个字符串s和一个字符串数组words
# words中所有字符串长度相同
# s中的串联子串是指一个包含 words中所有字符串以任意顺序排列连接起来的子串
# 例如words = { "ab","cd","ef" }
# 那么"abcdef"、"abefcd"、"cdabef"、"cdefab"、"efabcd"、"efcdab"都是串联子串。
# "acdbef"不是串联子串，因为他不是任何words排列的连接
# 返回所有串联子串在s中的开始索引
# 你可以以任意顺序返回答案
# 测试链接 : https://leetcode.cn/problems/substring-with-concatenation-of-all-words/
class Code05_ConcatenationAllWords:
    __java_fields__ = {'MAXN': 'MAXN', 'base': 'base', 'pow': 'pow', 'hash': 'hash_data'}
    # 如果s的长度为n，words里所有单词的总长度为m
    # 时间复杂度O(n + m)，最优解的时间复杂度与单词个数、单词长度是无关的
    # 所有题解都没有做到这个复杂度的
    # 虽然这个做法打败比例没有到100%，但那是因为测试数据量不够大
    # 所以最优解的时间复杂度优势没有体现出来
    # 这个方法绝对是最优解，只有同余分组 + 字符串哈希，时间复杂度才能到最优
    @staticmethod
    def findSubstring(s, words):
        ans = jnew('ArrayList')
        if ((((s == None) or (jcall(s, 'length') == 0)) or (words == None)) or (jget(words, 'length') == 0)):
            return ans
        # words的词频表
        map = jnew('HashMap')
        for key in words:
            v = jcast('long', Code05_ConcatenationAllWords._java_hash_1(key))
            jcall(map, 'put', v, jadd(jcall(map, 'getOrDefault', v, 0), 1))
        Code05_ConcatenationAllWords.build(s)
        n = jcast('int', jcall(s, 'length'))
        wordLen = jcast('int', jcall(words[0], 'length'))
        wordNum = jcast('int', jget(words, 'length'))
        allLen = jcast('int', jcast('int', (wordLen * wordNum)))
        # 窗口的词频表
        window = jnew('HashMap')
        # 同余分组
        init = jcast('int', 0)
        while ((init < wordLen) and (jcast('int', jadd(init, allLen)) <= n)):
            # init是当前组的首个开头
            debt = jcast('int', wordNum)
            # 建立起窗口
            l = jcast('int', init)
            r = jcast('int', jcast('int', jadd(init, wordLen)))
            part = jcast('int', 0)
            while (part < wordNum):
                cur = jcast('long', Code05_ConcatenationAllWords._java_hash_0(l, r))
                jcall(window, 'put', cur, jadd(jcall(window, 'getOrDefault', cur, 0), 1))
                if (jcall(window, 'get', cur) <= jcall(map, 'getOrDefault', cur, 0)):
                    debt = jcast('int', (debt - 1))
                l = jcast('int', jcast('int', jadd(l, wordLen)))
                r = jcast('int', jcast('int', jadd(r, wordLen)))
                part = jcast('int', (part + 1))
            if (debt == 0):
                jcall(ans, 'add', init)
            # 接下来窗口进一个、出一个
            l1 = jcast('int', init)
            r1 = jcast('int', jcast('int', jadd(init, wordLen)))
            l2 = jcast('int', jcast('int', jadd(init, allLen)))
            r2 = jcast('int', jcast('int', jadd(jcast('int', jadd(init, allLen)), wordLen)))
            while (r2 <= n):
                out = jcast('long', Code05_ConcatenationAllWords._java_hash_0(l1, r1))
                in_ = jcast('long', Code05_ConcatenationAllWords._java_hash_0(l2, r2))
                jcall(window, 'put', out, (jcall(window, 'get', out) - 1))
                if (jcall(window, 'get', out) < jcall(map, 'getOrDefault', out, 0)):
                    debt = jcast('int', (debt + 1))
                jcall(window, 'put', in_, jadd(jcall(window, 'getOrDefault', in_, 0), 1))
                if (jcall(window, 'get', in_) <= jcall(map, 'getOrDefault', in_, 0)):
                    debt = jcast('int', (debt - 1))
                if (debt == 0):
                    jcall(ans, 'add', r1)
                l1 = jcast('int', jcast('int', jadd(l1, wordLen)))
                r1 = jcast('int', jcast('int', jadd(r1, wordLen)))
                l2 = jcast('int', jcast('int', jadd(l2, wordLen)))
                r2 = jcast('int', jcast('int', jadd(r2, wordLen)))
            jcall(window, 'clear')
            init = jcast('int', (init + 1))
        return ans

    MAXN = 0
    base = 0
    pow = None
    hash_data = None
    @staticmethod
    def build(str):
        Code05_ConcatenationAllWords.pow[0] = jcast('long', 1)
        j = jcast('int', 1)
        while (j < Code05_ConcatenationAllWords.MAXN):
            Code05_ConcatenationAllWords.pow[j] = jcast('long', jcast('long', (Code05_ConcatenationAllWords.pow[jcast('int', (j - 1))] * Code05_ConcatenationAllWords.base)))
            j = jcast('int', (j + 1))
        jset(Code05_ConcatenationAllWords.hash_data, 0, jcast('int', jadd(jcast('int', (jcall(str, 'charAt', 0) - jchar('a'))), 1)))
        j = jcast('int', 1)
        while (j < jcall(str, 'length')):
            jset(Code05_ConcatenationAllWords.hash_data, j, jcast('long', jadd(jcast('long', (jcast('long', jadd(jcast('long', (Code05_ConcatenationAllWords.hash_data[jcast('int', (j - 1))] * Code05_ConcatenationAllWords.base)), jcall(str, 'charAt', j))) - jchar('a'))), 1)))
            j = jcast('int', (j + 1))

    # 范围是s[l,r)，左闭右开
    @staticmethod
    def _java_hash_0(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        ans = jcast('long', Code05_ConcatenationAllWords.hash_data[jcast('int', (r - 1))])
        ans = jcast('long', jcast('long', (ans - (0 if (l == 0) else jcast('long', (Code05_ConcatenationAllWords.hash_data[jcast('int', (l - 1))] * Code05_ConcatenationAllWords.pow[jcast('int', (r - l))]))))))
        return jcast('long', ans)

    # 计算一个字符串的哈希值
    @staticmethod
    def _java_hash_1(str):
        if jcall(str, 'equals', ''):
            return jcast('long', 0)
        n = jcast('int', jcall(str, 'length'))
        ans = jcast('long', jcast('int', jadd(jcast('int', (jcall(str, 'charAt', 0) - jchar('a'))), 1)))
        j = jcast('int', 1)
        while (j < n):
            ans = jcast('long', jcast('long', jadd(jcast('long', (jcast('long', jadd(jcast('long', (ans * Code05_ConcatenationAllWords.base)), jcall(str, 'charAt', j))) - jchar('a'))), 1)))
            j = jcast('int', (j + 1))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def hash(*args):
        _java_choice = jselect(args, [['int', 'int'], ['String']], [False, False])
        if _java_choice == 0:
            return Code05_ConcatenationAllWords._java_hash_0(*args)
        if _java_choice == 1:
            return Code05_ConcatenationAllWords._java_hash_1(*args)
        raise TypeError("No matching overload for Code05_ConcatenationAllWords.hash")


Code05_ConcatenationAllWords.MAXN = jcast('int', 10001)
Code05_ConcatenationAllWords.base = jcast('int', 499)
Code05_ConcatenationAllWords.pow = jarray('long', [Code05_ConcatenationAllWords.MAXN])
Code05_ConcatenationAllWords.hash_data = jarray('long', [Code05_ConcatenationAllWords.MAXN])
