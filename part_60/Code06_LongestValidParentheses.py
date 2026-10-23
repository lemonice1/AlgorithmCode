# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最长有效括号
# 给你一个只包含 '(' 和 ')' 的字符串
# 找出最长有效（格式正确且连续）括号子串的长度。
# 测试链接 : https://leetcode.cn/problems/longest-valid-parentheses/
class Code06_LongestValidParentheses:
    __java_fields__ = {}
    # 时间复杂度O(n)，n是str字符串的长度
    @staticmethod
    def longestValidParentheses(str):
        s = jcall(str, 'toCharArray')
        # dp[0...n-1]
        # dp[i] : 子串必须以i位置的字符结尾的情况下，往左整体有效的最大长度
        dp = jarray('int', [jget(s, 'length')])
        ans = jcast('int', 0)
        i = jcast('int', 1)
        p = 0
        while (i < jget(s, 'length')):
            if (s[i] == jchar(')')):
                p = jcast('int', jcast('int', (jcast('int', (i - dp[jcast('int', (i - 1))])) - 1)))
                # ?         )
                # p         i
                if ((p >= 0) and (s[p] == jchar('('))):
                    dp[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(dp[jcast('int', (i - 1))], 2)), (dp[jcast('int', (p - 1))] if (jcast('int', (p - 1)) >= 0) else 0))))
            ans = jcast('int', jstatic('Math', 'max', ans, dp[i]))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


