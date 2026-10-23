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

# 最长回文子序列
# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度
# 测试链接 : https://leetcode.cn/problems/longest-palindromic-subsequence/
class Code04_LongestPalindromicSubsequence:
    __java_fields__ = {}
    # 最长回文子序列问题可以转化成最长公共子序列问题
    # 不过这里讲述区间动态规划的思路
    # 区间dp还会有单独的视频做详细讲述
    @staticmethod
    def longestPalindromeSubseq1(str):
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        return jcast('int', Code04_LongestPalindromicSubsequence.f1(s, 0, jcast('int', (n - 1))))

    # s[l...r]最长回文子序列长度
    # l <= r
    @staticmethod
    def f1(s, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return jcast('int', 1)
        if (jcast('int', jadd(l, 1)) == r):
            return jcast('int', (2 if (s[l] == s[r]) else 1))
        if (s[l] == s[r]):
            return jcast('int', jcast('int', jadd(2, Code04_LongestPalindromicSubsequence.f1(s, jcast('int', jadd(l, 1)), jcast('int', (r - 1))))))
        else:
            return jcast('int', jstatic('Math', 'max', Code04_LongestPalindromicSubsequence.f1(s, jcast('int', jadd(l, 1)), r), Code04_LongestPalindromicSubsequence.f1(s, l, jcast('int', (r - 1)))))

    @staticmethod
    def longestPalindromeSubseq2(str):
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        dp = jarray('int', [n, n])
        return jcast('int', Code04_LongestPalindromicSubsequence.f2(s, 0, jcast('int', (n - 1)), dp))

    @staticmethod
    def f2(s, l, r, dp):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return jcast('int', 1)
        if (jcast('int', jadd(l, 1)) == r):
            return jcast('int', (2 if (s[l] == s[r]) else 1))
        if (dp[l][r] != 0):
            return jcast('int', dp[l][r])
        ans = 0
        if (s[l] == s[r]):
            ans = jcast('int', jcast('int', jadd(2, Code04_LongestPalindromicSubsequence.f2(s, jcast('int', jadd(l, 1)), jcast('int', (r - 1)), dp))))
        else:
            ans = jcast('int', jstatic('Math', 'max', Code04_LongestPalindromicSubsequence.f2(s, jcast('int', jadd(l, 1)), r, dp), Code04_LongestPalindromicSubsequence.f2(s, l, jcast('int', (r - 1)), dp)))
        jset(dp[l], r, ans)
        return jcast('int', ans)

    @staticmethod
    def longestPalindromeSubseq3(str):
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        dp = jarray('int', [n, n])
        l = jcast('int', jcast('int', (n - 1)))
        while (l >= 0):
            jset(dp[l], l, 1)
            if (jcast('int', jadd(l, 1)) < n):
                jset(dp[l], jcast('int', jadd(l, 1)), (2 if (s[l] == s[jcast('int', jadd(l, 1))]) else 1))
            r = jcast('int', jcast('int', jadd(l, 2)))
            while (r < n):
                if (s[l] == s[r]):
                    jset(dp[l], r, jcast('int', jadd(2, dp[jcast('int', jadd(l, 1))][jcast('int', (r - 1))])))
                else:
                    jset(dp[l], r, jstatic('Math', 'max', dp[jcast('int', jadd(l, 1))][r], dp[l][jcast('int', (r - 1))]))
                r = jcast('int', (r + 1))
            l = jcast('int', (l - 1))
        return jcast('int', dp[0][jcast('int', (n - 1))])

    @staticmethod
    def longestPalindromeSubseq4(str):
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        dp = jarray('int', [n])
        l = jcast('int', jcast('int', (n - 1)))
        leftDown = jcast('int', 0)
        backup = 0
        while (l >= 0):
            # dp[l] : 想象中的dp[l][l]
            dp[l] = jcast('int', 1)
            if (jcast('int', jadd(l, 1)) < n):
                leftDown = jcast('int', dp[jcast('int', jadd(l, 1))])
                # dp[l+1] : 想象中的dp[l][l+1]
                dp[jcast('int', jadd(l, 1))] = jcast('int', (2 if (s[l] == s[jcast('int', jadd(l, 1))]) else 1))
            r = jcast('int', jcast('int', jadd(l, 2)))
            while (r < n):
                backup = jcast('int', dp[r])
                if (s[l] == s[r]):
                    dp[r] = jcast('int', jcast('int', jadd(2, leftDown)))
                else:
                    jset(dp, r, jstatic('Math', 'max', dp[r], dp[jcast('int', (r - 1))]))
                leftDown = jcast('int', backup)
                r = jcast('int', (r + 1))
            l = jcast('int', (l - 1))
        return jcast('int', dp[jcast('int', (n - 1))])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


