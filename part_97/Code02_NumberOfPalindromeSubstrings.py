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

# 回文子串数量
# 返回字符串s的回文子串数量
# 测试链接 : https://leetcode.cn/problems/palindromic-substrings/
class Code02_NumberOfPalindromeSubstrings:
    __java_fields__ = {'MAXN': 'MAXN', 'ss': 'ss', 'p': 'p', 'n': 'n'}
    @staticmethod
    def countSubstrings(s):
        Code02_NumberOfPalindromeSubstrings.manacher(s)
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < Code02_NumberOfPalindromeSubstrings.n):
            ans = jcast('int', jcast('int', jadd(ans, jcast('int', jdiv(Code02_NumberOfPalindromeSubstrings.p[i], 2)))))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    MAXN = 0
    ss = None
    p = None
    n = 0
    @staticmethod
    def manacher(str):
        Code02_NumberOfPalindromeSubstrings.manacherss(jcall(str, 'toCharArray'))
        i = jcast('int', 0)
        c = jcast('int', 0)
        r = jcast('int', 0)
        len = 0
        while (i < Code02_NumberOfPalindromeSubstrings.n):
            len = jcast('int', (jstatic('Math', 'min', Code02_NumberOfPalindromeSubstrings.p[jcast('int', (jcast('int', (2 * c)) - i))], jcast('int', (r - i))) if (r > i) else 1))
            while (((jcast('int', jadd(i, len)) < Code02_NumberOfPalindromeSubstrings.n) and (jcast('int', (i - len)) >= 0)) and (Code02_NumberOfPalindromeSubstrings.ss[jcast('int', jadd(i, len))] == Code02_NumberOfPalindromeSubstrings.ss[jcast('int', (i - len))])):
                len = jcast('int', (len + 1))
            if (jcast('int', jadd(i, len)) > r):
                r = jcast('int', jcast('int', jadd(i, len)))
                c = jcast('int', i)
            Code02_NumberOfPalindromeSubstrings.p[i] = jcast('int', len)
            i = jcast('int', (i + 1))

    @staticmethod
    def manacherss(a):
        Code02_NumberOfPalindromeSubstrings.n = jcast('int', jcast('int', jadd(jcast('int', (jget(a, 'length') * 2)), 1)))
        i = jcast('int', 0)
        j = jcast('int', 0)
        while (i < Code02_NumberOfPalindromeSubstrings.n):
            jset(Code02_NumberOfPalindromeSubstrings.ss, i, (jchar('#') if (jcast('int', (i & 1)) == 0) else a[((_java_old_1 := j), (j := jcast('int', (j + (1)))), _java_old_1)[2]]))
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_NumberOfPalindromeSubstrings.MAXN = jcast('int', 1001)
Code02_NumberOfPalindromeSubstrings.ss = jarray('char', [jcast('int', (Code02_NumberOfPalindromeSubstrings.MAXN << (1 & 31)))])
Code02_NumberOfPalindromeSubstrings.p = jarray('int', [jcast('int', (Code02_NumberOfPalindromeSubstrings.MAXN << (1 & 31)))])
Code02_NumberOfPalindromeSubstrings.n = jcast('int', 0)
