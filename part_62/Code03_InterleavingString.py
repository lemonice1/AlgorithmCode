# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 交错字符串
# 给定三个字符串 s1、s2、s3
# 请帮忙验证s3是否由s1和s2交错组成
# 测试链接 : https://leetcode.cn/problems/interleaving-string/
class Code03_InterleavingString:
    __java_fields__ = {}
    # 已经展示太多次从递归到动态规划了
    # 直接写动态规划吧
    @staticmethod
    def isInterleave1(str1, str2, str3):
        if (jcast('int', jadd(jcall(str1, 'length'), jcall(str2, 'length'))) != jcall(str3, 'length')):
            return jcast('boolean', False)
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        s3 = jcall(str3, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        m = jcast('int', jget(s2, 'length'))
        # dp[i][j]:
        # s1[前缀长度为i]和s2[前缀长度为j]，能否交错组成出s3[前缀长度为i+j]
        dp = jarray('boolean', [jcast('int', jadd(n, 1)), jcast('int', jadd(m, 1))])
        jset(dp[0], 0, True)
        i = jcast('int', 1)
        while (i <= n):
            try:
                if (s1[jcast('int', (i - 1))] != s3[jcast('int', (i - 1))]):
                    raise JBreak(None)
                jset(dp[i], 0, True)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        j = jcast('int', 1)
        while (j <= m):
            try:
                if (s2[jcast('int', (j - 1))] != s3[jcast('int', (j - 1))]):
                    raise JBreak(None)
                jset(dp[0], j, True)
            except JContinue as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
            except JBreak as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
                break
            j = jcast('int', (j + 1))
        i = jcast('int', 1)
        while (i <= n):
            j = jcast('int', 1)
            while (j <= m):
                jset(dp[i], j, (((s1[jcast('int', (i - 1))] == s3[jcast('int', (jcast('int', jadd(i, j)) - 1))]) and dp[jcast('int', (i - 1))][j]) or ((s2[jcast('int', (j - 1))] == s3[jcast('int', (jcast('int', jadd(i, j)) - 1))]) and dp[i][jcast('int', (j - 1))])))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('boolean', dp[n][m])

    # 空间压缩
    @staticmethod
    def isInterleave2(str1, str2, str3):
        if (jcast('int', jadd(jcall(str1, 'length'), jcall(str2, 'length'))) != jcall(str3, 'length')):
            return jcast('boolean', False)
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        s3 = jcall(str3, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        m = jcast('int', jget(s2, 'length'))
        dp = jarray('boolean', [jcast('int', jadd(m, 1))])
        dp[0] = jcast('boolean', True)
        j = jcast('int', 1)
        while (j <= m):
            try:
                if (s2[jcast('int', (j - 1))] != s3[jcast('int', (j - 1))]):
                    raise JBreak(None)
                dp[j] = jcast('boolean', True)
            except JContinue as _java_control_3:
                if _java_control_3.label not in (None,):
                    raise
            except JBreak as _java_control_3:
                if _java_control_3.label not in (None,):
                    raise
                break
            j = jcast('int', (j + 1))
        i = jcast('int', 1)
        while (i <= n):
            dp[0] = jcast('boolean', ((s1[jcast('int', (i - 1))] == s3[jcast('int', (i - 1))]) and dp[0]))
            j = jcast('int', 1)
            while (j <= m):
                dp[j] = jcast('boolean', (((s1[jcast('int', (i - 1))] == s3[jcast('int', (jcast('int', jadd(i, j)) - 1))]) and dp[j]) or ((s2[jcast('int', (j - 1))] == s3[jcast('int', (jcast('int', jadd(i, j)) - 1))]) and dp[jcast('int', (j - 1))])))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('boolean', dp[m])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


