# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 统计不同回文子序列
# 给你一个字符串s，返回s中不同的非空回文子序列个数
# 由于答案可能很大，答案对 1000000007 取模
# 测试链接 : https://leetcode.cn/problems/count-different-palindromic-subsequences/
class Code06_CountDifferentPalindromicSubsequences:
    __java_fields__ = {}
    # 时间复杂度O(n^2)
    @staticmethod
    def countPalindromicSubsequences(str):
        mod = jcast('int', 1000000007)
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        last = jarray('int', [256])
        # left[i] : i位置的左边和s[i]字符相等且最近的位置在哪，不存在就是-1
        left = jarray('int', [n])
        jstatic('Arrays', 'fill', last, jcast('int', (-1)))
        i = jcast('int', 0)
        while (i < n):
            left[i] = jcast('int', last[s[i]])
            jset(last, s[i], i)
            i = jcast('int', (i + 1))
        # right[i] : i位置的右边和s[i]字符相等且最近的位置在哪，不存在就是n
        right = jarray('int', [n])
        jstatic('Arrays', 'fill', last, n)
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            right[i] = jcast('int', last[s[i]])
            jset(last, s[i], i)
            i = jcast('int', (i - 1))
        # dp[i][j] : i...j范围上有多少不同的回文子序列
        # 如果i>j，那么认为是无效范围dp[i][j] = 0
        dp = jarray('long', [n, n])
        i = jcast('int', 0)
        while (i < n):
            jset(dp[i], i, 1)
            i = jcast('int', (i + 1))
        i = jcast('int', jcast('int', (n - 2)))
        l = 0
        r = 0
        while (i >= 0):
            j = jcast('int', jcast('int', jadd(i, 1)))
            while (j < n):
                if (s[i] != s[j]):
                    # a ..... b
                    # i       j
                    # 因为要取模，所以只要发生减操作就+mod，讲解041同余原理
                    jset(dp[i], j, jcast('long', jadd(jcast('long', (jcast('long', jadd(dp[i][jcast('int', (j - 1))], dp[jcast('int', jadd(i, 1))][j])) - dp[jcast('int', jadd(i, 1))][jcast('int', (j - 1))])), mod)))
                else:
                    # s[i] == s[j]
                    # a......a
                    # i      j
                    l = jcast('int', right[i])
                    r = jcast('int', left[j])
                    if (l > r):
                        # i...j的内部没有s[i]字符
                        # a....a
                        # i    j
                        # (i+1..j-1) + a(i+1..j-1)a + a + aa
                        jset(dp[i], j, jcast('long', jadd(jcast('long', (dp[jcast('int', jadd(i, 1))][jcast('int', (j - 1))] * 2)), 2)))
                    else:
                        if (l == r):
                            # i...j的内部有一个s[i]字符
                            # a.....a......a
                            # i     lr     j
                            # (i+1..j-1) + a(i+1..j-1)a + aa
                            jset(dp[i], j, jcast('long', jadd(jcast('long', (dp[jcast('int', jadd(i, 1))][jcast('int', (j - 1))] * 2)), 1)))
                        else:
                            # i...j的内部不只一个s[i]字符
                            # a...a....这内部可能还有a但是不重要....a...a
                            # i   l                             r   j
                            # 因为要取模，所以只要发生减操作就+mod，讲解041同余原理
                            jset(dp[i], j, jcast('long', jadd(jcast('long', (jcast('long', (dp[jcast('int', jadd(i, 1))][jcast('int', (j - 1))] * 2)) - dp[jcast('int', jadd(l, 1))][jcast('int', (r - 1))])), mod)))
                ((_java_obj_1 := dp[i]), (_java_key_2 := j), jset(_java_obj_1, _java_key_2, jcast('long', jmod(jget(_java_obj_1, _java_key_2), mod))))[2]
                j = jcast('int', (j + 1))
            i = jcast('int', (i - 1))
        return jcast('int', jcast('int', dp[0][jcast('int', (n - 1))]))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


