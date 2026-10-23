# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 环绕字符串中唯一的子字符串
# 定义字符串 base 为一个 "abcdefghijklmnopqrstuvwxyz" 无限环绕的字符串
# 所以 base 看起来是这样的：
# "..zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd.."
# 给你一个字符串 s ，请你统计并返回 s 中有多少 不同非空子串 也在 base 中出现
# 测试链接 : https://leetcode.cn/problems/unique-substrings-in-wraparound-string/
class Code07_UniqueSubstringsWraparoundString:
    __java_fields__ = {}
    # 时间复杂度O(n)，n是字符串s的长度，字符串base长度为正无穷
    @staticmethod
    def findSubstringInWraproundString(str):
        n = jcast('int', jcall(str, 'length'))
        s = jarray('int', [n])
        # abcde...z -> 0, 1, 2, 3, 4....25
        i = jcast('int', 0)
        while (i < n):
            jset(s, i, jcast('int', (jcall(str, 'charAt', i) - jchar('a'))))
            i = jcast('int', (i + 1))
        # dp[0] : s中必须以'a'的子串，最大延伸长度是多少，延伸一定要跟据base串的规则
        dp = jarray('int', [26])
        # s : c d e....
        # 2 3 4
        jset(dp, s[0], 1)
        i = jcast('int', 1)
        cur = 0
        pre = 0
        len = jcast('int', 1)
        while (i < n):
            cur = jcast('int', s[i])
            pre = jcast('int', s[jcast('int', (i - 1))])
            # pre cur
            if (((pre == 25) and (cur == 0)) or (jcast('int', jadd(pre, 1)) == cur)):
                # (前一个字符是'z' && 当前字符是'a') || 前一个字符比当前字符的ascii码少1
                len = jcast('int', (len + 1))
            else:
                len = jcast('int', 1)
            jset(dp, cur, jstatic('Math', 'max', dp[cur], len))
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < 26):
            ans = jcast('int', jcast('int', jadd(ans, dp[i])))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


