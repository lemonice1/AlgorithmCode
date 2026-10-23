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

# DI序列的有效排列
# 给定一个长度为n的字符串s，其中s[i]是:
# "D"意味着减少，"I"意味着增加
# 有效排列是对有n+1个在[0,n]范围内的整数的一个排列perm，使得对所有的i：
# 如果 s[i] == 'D'，那么 perm[i] > perm[i+1]
# 如果 s[i] == 'I'，那么 perm[i] < perm[i+1]
# 返回有效排列的perm的数量
# 因为答案可能很大，答案对 1000000007 取模
# 测试链接 : https://leetcode.cn/problems/valid-permutations-for-di-sequence/
class Code07_DiSequence:
    __java_fields__ = {}
    @staticmethod
    def numPermsDISequence1(s):
        return jcast('int', Code07_DiSequence.f(jcall(s, 'toCharArray'), 0, jcast('int', jadd(jcall(s, 'length'), 1)), jcast('int', jadd(jcall(s, 'length'), 1))))

    # 猜法很妙！
    # 一共有n个数字，位置范围0~n-1
    # 当前来到i位置，i-1位置的数字已经确定，i位置的数字还没确定
    # i-1位置和i位置的关系，是s[i-1] : D、I
    # 0~i-1范围上是已经使用过的数字，i个
    # 还没有使用过的数字中，比i-1位置的数字小的，有less个
    # 还没有使用过的数字中，比i-1位置的数字大的，有n - i - less个
    # 返回后续还有多少种有效的排列
    @staticmethod
    def f(s, i, less, n):
        i = jcast('int', i)
        less = jcast('int', less)
        n = jcast('int', n)
        ans = jcast('int', 0)
        if (i == n):
            ans = jcast('int', 1)
        else:
            if ((i == 0) or (s[jcast('int', (i - 1))] == jchar('D'))):
                nextLess = jcast('int', 0)
                while (nextLess < less):
                    ans = jcast('int', jcast('int', jadd(ans, Code07_DiSequence.f(s, jcast('int', jadd(i, 1)), nextLess, n))))
                    nextLess = jcast('int', (nextLess + 1))
            else:
                nextLess = jcast('int', less)
                k = jcast('int', 1)
                while (k <= jcast('int', (jcast('int', (n - i)) - less))):
                    ans = jcast('int', jcast('int', jadd(ans, Code07_DiSequence.f(s, jcast('int', jadd(i, 1)), nextLess, n))))
                    k = jcast('int', (k + 1))
                    nextLess = jcast('int', (nextLess + 1))
        return jcast('int', ans)

    @staticmethod
    def numPermsDISequence2(str):
        mod = jcast('int', 1000000007)
        s = jcall(str, 'toCharArray')
        n = jcast('int', jcast('int', jadd(jget(s, 'length'), 1)))
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(n, 1))])
        less = jcast('int', 0)
        while (less <= n):
            jset(dp[n], less, 1)
            less = jcast('int', (less + 1))
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            less = jcast('int', 0)
            while (less <= n):
                if ((i == 0) or (s[jcast('int', (i - 1))] == jchar('D'))):
                    nextLess = jcast('int', 0)
                    while (nextLess < less):
                        jset(dp[i], less, jcast('int', jmod(jcast('int', jadd(dp[i][less], dp[jcast('int', jadd(i, 1))][nextLess])), mod)))
                        nextLess = jcast('int', (nextLess + 1))
                else:
                    nextLess = jcast('int', less)
                    k = jcast('int', 1)
                    while (k <= jcast('int', (jcast('int', (n - i)) - less))):
                        jset(dp[i], less, jcast('int', jmod(jcast('int', jadd(dp[i][less], dp[jcast('int', jadd(i, 1))][nextLess])), mod)))
                        k = jcast('int', (k + 1))
                        nextLess = jcast('int', (nextLess + 1))
                less = jcast('int', (less + 1))
            i = jcast('int', (i - 1))
        return jcast('int', dp[0][n])

    # 通过观察方法2，得到优化枚举的方法
    @staticmethod
    def numPermsDISequence3(str):
        mod = jcast('int', 1000000007)
        s = jcall(str, 'toCharArray')
        n = jcast('int', jcast('int', jadd(jget(s, 'length'), 1)))
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(n, 1))])
        less = jcast('int', 0)
        while (less <= n):
            jset(dp[n], less, 1)
            less = jcast('int', (less + 1))
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            if ((i == 0) or (s[jcast('int', (i - 1))] == jchar('D'))):
                jset(dp[i], 1, dp[jcast('int', jadd(i, 1))][0])
                less = jcast('int', 2)
                while (less <= n):
                    jset(dp[i], less, jcast('int', jmod(jcast('int', jadd(dp[i][jcast('int', (less - 1))], dp[jcast('int', jadd(i, 1))][jcast('int', (less - 1))])), mod)))
                    less = jcast('int', (less + 1))
            else:
                jset(dp[i], jcast('int', (jcast('int', (n - i)) - 1)), dp[jcast('int', jadd(i, 1))][jcast('int', (jcast('int', (n - i)) - 1))])
                less = jcast('int', jcast('int', (jcast('int', (n - i)) - 2)))
                while (less >= 0):
                    jset(dp[i], less, jcast('int', jmod(jcast('int', jadd(dp[i][jcast('int', jadd(less, 1))], dp[jcast('int', jadd(i, 1))][less])), mod)))
                    less = jcast('int', (less - 1))
            i = jcast('int', (i - 1))
        return jcast('int', dp[0][n])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


