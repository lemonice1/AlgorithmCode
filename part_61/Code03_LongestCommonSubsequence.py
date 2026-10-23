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

# 最长公共子序列
# 给定两个字符串text1和text2
# 返回这两个字符串的最长 公共子序列 的长度
# 如果不存在公共子序列，返回0
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列
# 测试链接 : https://leetcode.cn/problems/longest-common-subsequence/
class Code03_LongestCommonSubsequence:
    __java_fields__ = {}
    @staticmethod
    def longestCommonSubsequence1(str1, str2):
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        m = jcast('int', jget(s2, 'length'))
        return jcast('int', Code03_LongestCommonSubsequence.f1(s1, s2, jcast('int', (n - 1)), jcast('int', (m - 1))))

    # s1[0....i1]与s2[0....i2]最长公共子序列长度
    @staticmethod
    def f1(s1, s2, i1, i2):
        i1 = jcast('int', i1)
        i2 = jcast('int', i2)
        if ((i1 < 0) or (i2 < 0)):
            return jcast('int', 0)
        p1 = jcast('int', Code03_LongestCommonSubsequence.f1(s1, s2, jcast('int', (i1 - 1)), jcast('int', (i2 - 1))))
        p2 = jcast('int', Code03_LongestCommonSubsequence.f1(s1, s2, jcast('int', (i1 - 1)), i2))
        p3 = jcast('int', Code03_LongestCommonSubsequence.f1(s1, s2, i1, jcast('int', (i2 - 1))))
        p4 = jcast('int', (jcast('int', jadd(p1, 1)) if (s1[i1] == s2[i2]) else 0))
        return jcast('int', jstatic('Math', 'max', jstatic('Math', 'max', p1, p2), jstatic('Math', 'max', p3, p4)))

    # 为了避免很多边界讨论
    # 很多时候往往不用下标来定义尝试，而是用长度来定义尝试
    # 因为长度最短是0，而下标越界的话讨论起来就比较麻烦
    @staticmethod
    def longestCommonSubsequence2(str1, str2):
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        m = jcast('int', jget(s2, 'length'))
        return jcast('int', Code03_LongestCommonSubsequence.f2(s1, s2, n, m))

    # s1[前缀长度为len1]对应s2[前缀长度为len2]
    # 最长公共子序列长度
    @staticmethod
    def f2(s1, s2, len1, len2):
        len1 = jcast('int', len1)
        len2 = jcast('int', len2)
        if ((len1 == 0) or (len2 == 0)):
            return jcast('int', 0)
        ans = 0
        if (s1[jcast('int', (len1 - 1))] == s2[jcast('int', (len2 - 1))]):
            ans = jcast('int', jcast('int', jadd(Code03_LongestCommonSubsequence.f2(s1, s2, jcast('int', (len1 - 1)), jcast('int', (len2 - 1))), 1)))
        else:
            ans = jcast('int', jstatic('Math', 'max', Code03_LongestCommonSubsequence.f2(s1, s2, jcast('int', (len1 - 1)), len2), Code03_LongestCommonSubsequence.f2(s1, s2, len1, jcast('int', (len2 - 1)))))
        return jcast('int', ans)

    # 记忆化搜索
    @staticmethod
    def longestCommonSubsequence3(str1, str2):
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        m = jcast('int', jget(s2, 'length'))
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(m, 1))])
        i = jcast('int', 0)
        while (i <= n):
            j = jcast('int', 0)
            while (j <= m):
                jset(dp[i], j, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code03_LongestCommonSubsequence.f3(s1, s2, n, m, dp))

    @staticmethod
    def f3(s1, s2, len1, len2, dp):
        len1 = jcast('int', len1)
        len2 = jcast('int', len2)
        if ((len1 == 0) or (len2 == 0)):
            return jcast('int', 0)
        if (dp[len1][len2] != jcast('int', (-1))):
            return jcast('int', dp[len1][len2])
        ans = 0
        if (s1[jcast('int', (len1 - 1))] == s2[jcast('int', (len2 - 1))]):
            ans = jcast('int', jcast('int', jadd(Code03_LongestCommonSubsequence.f3(s1, s2, jcast('int', (len1 - 1)), jcast('int', (len2 - 1)), dp), 1)))
        else:
            ans = jcast('int', jstatic('Math', 'max', Code03_LongestCommonSubsequence.f3(s1, s2, jcast('int', (len1 - 1)), len2, dp), Code03_LongestCommonSubsequence.f3(s1, s2, len1, jcast('int', (len2 - 1)), dp)))
        jset(dp[len1], len2, ans)
        return jcast('int', ans)

    # 严格位置依赖的动态规划
    @staticmethod
    def longestCommonSubsequence4(str1, str2):
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        m = jcast('int', jget(s2, 'length'))
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(m, 1))])
        len1 = jcast('int', 1)
        while (len1 <= n):
            len2 = jcast('int', 1)
            while (len2 <= m):
                if (s1[jcast('int', (len1 - 1))] == s2[jcast('int', (len2 - 1))]):
                    jset(dp[len1], len2, jcast('int', jadd(1, dp[jcast('int', (len1 - 1))][jcast('int', (len2 - 1))])))
                else:
                    jset(dp[len1], len2, jstatic('Math', 'max', dp[jcast('int', (len1 - 1))][len2], dp[len1][jcast('int', (len2 - 1))]))
                len2 = jcast('int', (len2 + 1))
            len1 = jcast('int', (len1 + 1))
        return jcast('int', dp[n][m])

    # 严格位置依赖的动态规划 + 空间压缩
    @staticmethod
    def longestCommonSubsequence5(str1, str2):
        s1 = None
        s2 = None
        if (jcall(str1, 'length') >= jcall(str2, 'length')):
            s1 = jcall(str1, 'toCharArray')
            s2 = jcall(str2, 'toCharArray')
        else:
            s1 = jcall(str2, 'toCharArray')
            s2 = jcall(str1, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        m = jcast('int', jget(s2, 'length'))
        dp = jarray('int', [jcast('int', jadd(m, 1))])
        len1 = jcast('int', 1)
        while (len1 <= n):
            leftUp = jcast('int', 0)
            backup = 0
            len2 = jcast('int', 1)
            while (len2 <= m):
                backup = jcast('int', dp[len2])
                if (s1[jcast('int', (len1 - 1))] == s2[jcast('int', (len2 - 1))]):
                    dp[len2] = jcast('int', jcast('int', jadd(1, leftUp)))
                else:
                    jset(dp, len2, jstatic('Math', 'max', dp[len2], dp[jcast('int', (len2 - 1))]))
                leftUp = jcast('int', backup)
                len2 = jcast('int', (len2 + 1))
            len1 = jcast('int', (len1 + 1))
        return jcast('int', dp[m])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


