# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 让字符串成为回文串的最少插入次数
# 给你一个字符串 s
# 每一次操作你都可以在字符串的任意位置插入任意字符
# 请你返回让s成为回文串的最少操作次数
# 测试链接 : https://leetcode.cn/problems/minimum-insertion-steps-to-make-a-string-palindrome/
class Code01_MinimumInsertionToPalindrome:
    __java_fields__ = {}
    # 暴力尝试
    @staticmethod
    def minInsertions1(str):
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        return jcast('int', Code01_MinimumInsertionToPalindrome.f1(s, 0, jcast('int', (n - 1))))

    # s[l....r]这个范围上的字符串，整体都变成回文串
    # 返回至少插入几个字符
    @staticmethod
    def f1(s, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        # l <= r
        if (l == r):
            return jcast('int', 0)
        if (jcast('int', jadd(l, 1)) == r):
            return jcast('int', (0 if (s[l] == s[r]) else 1))
        # l...r不只两个字符
        if (s[l] == s[r]):
            return jcast('int', Code01_MinimumInsertionToPalindrome.f1(s, jcast('int', jadd(l, 1)), jcast('int', (r - 1))))
        else:
            return jcast('int', jcast('int', jadd(jstatic('Math', 'min', Code01_MinimumInsertionToPalindrome.f1(s, l, jcast('int', (r - 1))), Code01_MinimumInsertionToPalindrome.f1(s, jcast('int', jadd(l, 1)), r)), 1)))

    # 记忆化搜索
    @staticmethod
    def minInsertions2(str):
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        dp = jarray('int', [n, n])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', i)
            while (j < n):
                jset(dp[i], j, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code01_MinimumInsertionToPalindrome.f2(s, 0, jcast('int', (n - 1)), dp))

    @staticmethod
    def f2(s, l, r, dp):
        l = jcast('int', l)
        r = jcast('int', r)
        if (dp[l][r] != jcast('int', (-1))):
            return jcast('int', dp[l][r])
        ans = 0
        if (l == r):
            ans = jcast('int', 0)
        else:
            if (jcast('int', jadd(l, 1)) == r):
                ans = jcast('int', (0 if (s[l] == s[jcast('int', jadd(l, 1))]) else 1))
            else:
                if (s[l] == s[r]):
                    ans = jcast('int', Code01_MinimumInsertionToPalindrome.f2(s, jcast('int', jadd(l, 1)), jcast('int', (r - 1)), dp))
                else:
                    ans = jcast('int', jcast('int', jadd(jstatic('Math', 'min', Code01_MinimumInsertionToPalindrome.f2(s, l, jcast('int', (r - 1)), dp), Code01_MinimumInsertionToPalindrome.f2(s, jcast('int', jadd(l, 1)), r, dp)), 1)))
        jset(dp[l], r, ans)
        return jcast('int', ans)

    # 严格位置依赖的动态规划
    @staticmethod
    def minInsertions3(str):
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        dp = jarray('int', [n, n])
        l = jcast('int', 0)
        while (l < jcast('int', (n - 1))):
            jset(dp[l], jcast('int', jadd(l, 1)), (0 if (s[l] == s[jcast('int', jadd(l, 1))]) else 1))
            l = jcast('int', (l + 1))
        l = jcast('int', jcast('int', (n - 3)))
        while (l >= 0):
            r = jcast('int', jcast('int', jadd(l, 2)))
            while (r < n):
                if (s[l] == s[r]):
                    jset(dp[l], r, dp[jcast('int', jadd(l, 1))][jcast('int', (r - 1))])
                else:
                    jset(dp[l], r, jcast('int', jadd(jstatic('Math', 'min', dp[l][jcast('int', (r - 1))], dp[jcast('int', jadd(l, 1))][r]), 1)))
                r = jcast('int', (r + 1))
            l = jcast('int', (l - 1))
        return jcast('int', dp[0][jcast('int', (n - 1))])

    # 空间压缩
    # 本题有关空间压缩的实现，可以参考讲解067，题目4，最长回文子序列问题的讲解
    # 这两个题空间压缩写法高度相似
    # 因为之前的课多次讲过空间压缩的内容，所以这里不再赘述
    @staticmethod
    def minInsertions4(str):
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        if (n < 2):
            return jcast('int', 0)
        dp = jarray('int', [n])
        dp[jcast('int', (n - 1))] = jcast('int', (0 if (s[jcast('int', (n - 2))] == s[jcast('int', (n - 1))]) else 1))
        l = jcast('int', jcast('int', (n - 3)))
        leftDown = 0
        backUp = 0
        while (l >= 0):
            leftDown = jcast('int', dp[jcast('int', jadd(l, 1))])
            dp[jcast('int', jadd(l, 1))] = jcast('int', (0 if (s[l] == s[jcast('int', jadd(l, 1))]) else 1))
            r = jcast('int', jcast('int', jadd(l, 2)))
            while (r < n):
                backUp = jcast('int', dp[r])
                if (s[l] == s[r]):
                    dp[r] = jcast('int', leftDown)
                else:
                    jset(dp, r, jcast('int', jadd(jstatic('Math', 'min', dp[jcast('int', (r - 1))], dp[r]), 1)))
                leftDown = jcast('int', backUp)
                r = jcast('int', (r + 1))
            l = jcast('int', (l - 1))
        return jcast('int', dp[jcast('int', (n - 1))])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


