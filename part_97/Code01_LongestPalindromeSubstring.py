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

# 最长回文子串
# 找到字符串s中最长的回文子串并返回
# 测试链接 : https://leetcode.cn/problems/longest-palindromic-substring/
class Code01_LongestPalindromeSubstring:
    __java_fields__ = {'MAXN': 'MAXN', 'ss': 'ss', 'p': 'p', 'n': 'n', 'max': 'max', 'end': 'end'}
    @staticmethod
    def longestPalindrome(s):
        Code01_LongestPalindromeSubstring.manacher(s)
        return jcall(s, 'substring', jcast('int', (Code01_LongestPalindromeSubstring.end - Code01_LongestPalindromeSubstring.max)), Code01_LongestPalindromeSubstring.end)

    MAXN = 0
    ss = None
    p = None
    n = 0
    max = 0
    end = 0
    @staticmethod
    def manacher(str):
        Code01_LongestPalindromeSubstring.manacherss(jcall(str, 'toCharArray'))
        Code01_LongestPalindromeSubstring.max = jcast('int', jset(Code01_LongestPalindromeSubstring, 'end', 0))
        i = jcast('int', 0)
        c = jcast('int', 0)
        r = jcast('int', 0)
        len = 0
        while (i < Code01_LongestPalindromeSubstring.n):
            len = jcast('int', (jstatic('Math', 'min', Code01_LongestPalindromeSubstring.p[jcast('int', (jcast('int', (2 * c)) - i))], jcast('int', (r - i))) if (r > i) else 1))
            while (((jcast('int', jadd(i, len)) < Code01_LongestPalindromeSubstring.n) and (jcast('int', (i - len)) >= 0)) and (Code01_LongestPalindromeSubstring.ss[jcast('int', jadd(i, len))] == Code01_LongestPalindromeSubstring.ss[jcast('int', (i - len))])):
                len = jcast('int', (len + 1))
            if (jcast('int', jadd(i, len)) > r):
                r = jcast('int', jcast('int', jadd(i, len)))
                c = jcast('int', i)
            if (len > Code01_LongestPalindromeSubstring.max):
                Code01_LongestPalindromeSubstring.max = jcast('int', jcast('int', (len - 1)))
                Code01_LongestPalindromeSubstring.end = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(i, len)) - 1)), 2)))
            Code01_LongestPalindromeSubstring.p[i] = jcast('int', len)
            i = jcast('int', (i + 1))

    @staticmethod
    def manacherss(a):
        Code01_LongestPalindromeSubstring.n = jcast('int', jcast('int', jadd(jcast('int', (jget(a, 'length') * 2)), 1)))
        i = jcast('int', 0)
        j = jcast('int', 0)
        while (i < Code01_LongestPalindromeSubstring.n):
            jset(Code01_LongestPalindromeSubstring.ss, i, (jchar('#') if (jcast('int', (i & 1)) == 0) else a[((_java_old_1 := j), (j := jcast('int', (j + (1)))), _java_old_1)[2]]))
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_LongestPalindromeSubstring.MAXN = jcast('int', 1001)
Code01_LongestPalindromeSubstring.ss = jarray('char', [jcast('int', (Code01_LongestPalindromeSubstring.MAXN << (1 & 31)))])
Code01_LongestPalindromeSubstring.p = jarray('int', [jcast('int', (Code01_LongestPalindromeSubstring.MAXN << (1 & 31)))])
Code01_LongestPalindromeSubstring.n = jcast('int', 0)
Code01_LongestPalindromeSubstring.max = jcast('int', 0)
Code01_LongestPalindromeSubstring.end = jcast('int', 0)
