# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 不同的子序列
# 给你两个字符串s和t ，统计并返回在s的子序列中t出现的个数
# 答案对 1000000007 取模
# 测试链接 : https://leetcode.cn/problems/distinct-subsequences/
class Code01_DistinctSubsequences:
    __java_fields__ = {}
    # 已经展示太多次从递归到动态规划了
    # 直接写动态规划吧
    @staticmethod
    def numDistinct1(str, target):
        s = jcall(str, 'toCharArray')
        t = jcall(target, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        m = jcast('int', jget(t, 'length'))
        # dp[i][j] :
        # s[前缀长度为i]的所有子序列中，有多少个子序列等于t[前缀长度为j]
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(m, 1))])
        i = jcast('int', 0)
        while (i <= n):
            jset(dp[i], 0, 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= n):
            j = jcast('int', 1)
            while (j <= m):
                jset(dp[i], j, dp[jcast('int', (i - 1))][j])
                if (s[jcast('int', (i - 1))] == t[jcast('int', (j - 1))]):
                    ((_java_obj_1 := dp[i]), (_java_key_2 := j), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), dp[jcast('int', (i - 1))][jcast('int', (j - 1))]))))[2]
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[n][m])

    # 空间压缩
    @staticmethod
    def numDistinct2(str, target):
        s = jcall(str, 'toCharArray')
        t = jcall(target, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        m = jcast('int', jget(t, 'length'))
        dp = jarray('int', [jcast('int', jadd(m, 1))])
        dp[0] = jcast('int', 1)
        i = jcast('int', 1)
        while (i <= n):
            j = jcast('int', m)
            while (j >= 1):
                if (s[jcast('int', (i - 1))] == t[jcast('int', (j - 1))]):
                    dp[j] = jcast('int', jcast('int', jadd(dp[j], dp[jcast('int', (j - 1))])))
                j = jcast('int', (j - 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[m])

    # 本题说了要取模，所以增加取模的逻辑
    @staticmethod
    def numDistinct3(str, target):
        mod = jcast('int', 1000000007)
        s = jcall(str, 'toCharArray')
        t = jcall(target, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        m = jcast('int', jget(t, 'length'))
        dp = jarray('int', [jcast('int', jadd(m, 1))])
        dp[0] = jcast('int', 1)
        i = jcast('int', 1)
        while (i <= n):
            j = jcast('int', m)
            while (j >= 1):
                if (s[jcast('int', (i - 1))] == t[jcast('int', (j - 1))]):
                    dp[j] = jcast('int', jcast('int', jmod(jcast('int', jadd(dp[j], dp[jcast('int', (j - 1))])), mod)))
                j = jcast('int', (j - 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[m])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


