# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 编辑距离
# 给你两个单词 word1 和 word2
# 请返回将 word1 转换成 word2 所使用的最少代价
# 你可以对一个单词进行如下三种操作：
# 插入一个字符，代价a
# 删除一个字符，代价b
# 替换一个字符，代价c
# 测试链接 : https://leetcode.cn/problems/edit-distance/
class Code02_EditDistance:
    __java_fields__ = {}
    # 已经展示太多次从递归到动态规划了
    # 直接写动态规划吧
    def minDistance(self, word1, word2):
        return jcast('int', Code02_EditDistance.editDistance2(word1, word2, 1, 1, 1))

    # 原初尝试版
    # a : str1中插入1个字符的代价
    # b : str1中删除1个字符的代价
    # c : str1中改变1个字符的代价
    # 返回从str1转化成str2的最低代价
    @staticmethod
    def editDistance1(str1, str2, a, b, c):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        m = jcast('int', jget(s2, 'length'))
        # dp[i][j] :
        # s1[前缀长度为i]想变成s2[前缀长度为j]，至少付出多少代价
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(m, 1))])
        i = jcast('int', 1)
        while (i <= n):
            jset(dp[i], 0, jcast('int', (i * b)))
            i = jcast('int', (i + 1))
        j = jcast('int', 1)
        while (j <= m):
            jset(dp[0], j, jcast('int', (j * a)))
            j = jcast('int', (j + 1))
        i = jcast('int', 1)
        while (i <= n):
            j = jcast('int', 1)
            while (j <= m):
                p1 = jcast('int', jget(Integer, 'MAX_VALUE'))
                if (s1[jcast('int', (i - 1))] == s2[jcast('int', (j - 1))]):
                    p1 = jcast('int', dp[jcast('int', (i - 1))][jcast('int', (j - 1))])
                p2 = jcast('int', jget(Integer, 'MAX_VALUE'))
                if (s1[jcast('int', (i - 1))] != s2[jcast('int', (j - 1))]):
                    p2 = jcast('int', jcast('int', jadd(dp[jcast('int', (i - 1))][jcast('int', (j - 1))], c)))
                p3 = jcast('int', jcast('int', jadd(dp[i][jcast('int', (j - 1))], a)))
                p4 = jcast('int', jcast('int', jadd(dp[jcast('int', (i - 1))][j], b)))
                jset(dp[i], j, jstatic('Math', 'min', jstatic('Math', 'min', p1, p2), jstatic('Math', 'min', p3, p4)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[n][m])

    # 枚举小优化版
    # a : str1中插入1个字符的代价
    # b : str1中删除1个字符的代价
    # c : str1中改变1个字符的代价
    # 返回从str1转化成str2的最低代价
    @staticmethod
    def editDistance2(str1, str2, a, b, c):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        m = jcast('int', jget(s2, 'length'))
        # dp[i][j] :
        # s1[前缀长度为i]想变成s2[前缀长度为j]，至少付出多少代价
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(m, 1))])
        i = jcast('int', 1)
        while (i <= n):
            jset(dp[i], 0, jcast('int', (i * b)))
            i = jcast('int', (i + 1))
        j = jcast('int', 1)
        while (j <= m):
            jset(dp[0], j, jcast('int', (j * a)))
            j = jcast('int', (j + 1))
        i = jcast('int', 1)
        while (i <= n):
            j = jcast('int', 1)
            while (j <= m):
                if (s1[jcast('int', (i - 1))] == s2[jcast('int', (j - 1))]):
                    jset(dp[i], j, dp[jcast('int', (i - 1))][jcast('int', (j - 1))])
                else:
                    jset(dp[i], j, jstatic('Math', 'min', jstatic('Math', 'min', jcast('int', jadd(dp[jcast('int', (i - 1))][j], b)), jcast('int', jadd(dp[i][jcast('int', (j - 1))], a))), jcast('int', jadd(dp[jcast('int', (i - 1))][jcast('int', (j - 1))], c))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[n][m])

    # 空间压缩
    @staticmethod
    def editDistance3(str1, str2, a, b, c):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        m = jcast('int', jget(s2, 'length'))
        dp = jarray('int', [jcast('int', jadd(m, 1))])
        j = jcast('int', 1)
        while (j <= m):
            dp[j] = jcast('int', jcast('int', (j * a)))
            j = jcast('int', (j + 1))
        i = jcast('int', 1)
        leftUp = 0
        backUp = 0
        while (i <= n):
            leftUp = jcast('int', jcast('int', (jcast('int', (i - 1)) * b)))
            dp[0] = jcast('int', jcast('int', (i * b)))
            j = jcast('int', 1)
            while (j <= m):
                backUp = jcast('int', dp[j])
                if (s1[jcast('int', (i - 1))] == s2[jcast('int', (j - 1))]):
                    dp[j] = jcast('int', leftUp)
                else:
                    jset(dp, j, jstatic('Math', 'min', jstatic('Math', 'min', jcast('int', jadd(dp[j], b)), jcast('int', jadd(dp[jcast('int', (j - 1))], a))), jcast('int', jadd(leftUp, c))))
                leftUp = jcast('int', backUp)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[m])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


