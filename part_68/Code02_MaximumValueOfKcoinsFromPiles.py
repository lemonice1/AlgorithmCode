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

# 从栈中取出K个硬币的最大面值和
# 一张桌子上总共有 n 个硬币 栈 。每个栈有 正整数 个带面值的硬币
# 每一次操作中，你可以从任意一个栈的 顶部 取出 1 个硬币，从栈中移除它，并放入你的钱包里
# 给你一个列表 piles ，其中 piles[i] 是一个整数数组
# 分别表示第 i 个栈里 从顶到底 的硬币面值。同时给你一个正整数 k
# 请你返回在 恰好 进行 k 次操作的前提下，你钱包里硬币面值之和 最大为多少
# 测试链接 : https://leetcode.cn/problems/maximum-value-of-k-coins-from-piles/
class Code02_MaximumValueOfKcoinsFromPiles:
    __java_fields__ = {}
    # piles是一组一组的硬币
    # m是容量，表示一定要进行m次操作
    # dp[i][j] : 1~i组上，一共拿走j个硬币的情况下，获得的最大价值
    # 1) 不要i组的硬币 : dp[i-1][j]
    # 2) i组里尝试每一种方案
    # 比如，i组里拿走前k个硬币的方案 : dp[i-1][j-k] + 从顶部开始前k个硬币的价值和
    # 枚举每一个k，选出最大值
    @staticmethod
    def maxValueOfCoins1(piles, m):
        m = jcast('int', m)
        n = jcast('int', jcall(piles, 'size'))
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(m, 1))])
        i = jcast('int', 1)
        while (i <= n):
            # i从1组开始（我们的设定），但是题目中的piles是从下标0开始的
            # 所以来到i的时候，piles.get(i-1)是当前组
            team = jcall(piles, 'get', jcast('int', (i - 1)))
            t = jcast('int', jstatic('Math', 'min', jcall(team, 'size'), m))
            # 预处理前缀和，为了加速计算
            preSum = jarray('int', [jcast('int', jadd(t, 1))])
            j = jcast('int', 0)
            sum = jcast('int', 0)
            while (j < t):
                sum = jcast('int', jadd(sum, jcall(team, 'get', j)))
                preSum[jcast('int', jadd(j, 1))] = jcast('int', sum)
                j = jcast('int', (j + 1))
            # 更新动态规划表
            j = jcast('int', 0)
            while (j <= m):
                # 当前组一个硬币也不拿的方案
                jset(dp[i], j, dp[jcast('int', (i - 1))][j])
                k = jcast('int', 1)
                while (k <= jstatic('Math', 'min', t, j)):
                    jset(dp[i], j, jstatic('Math', 'max', dp[i][j], jcast('int', jadd(dp[jcast('int', (i - 1))][jcast('int', (j - k))], preSum[k]))))
                    k = jcast('int', (k + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[n][m])

    # 空间压缩
    @staticmethod
    def maxValueOfCoins2(piles, m):
        m = jcast('int', m)
        dp = jarray('int', [jcast('int', jadd(m, 1))])
        for team in piles:
            t = jcast('int', jstatic('Math', 'min', jcall(team, 'size'), m))
            preSum = jarray('int', [jcast('int', jadd(t, 1))])
            j = jcast('int', 0)
            sum = jcast('int', 0)
            while (j < t):
                sum = jcast('int', jadd(sum, jcall(team, 'get', j)))
                preSum[jcast('int', jadd(j, 1))] = jcast('int', sum)
                j = jcast('int', (j + 1))
            j = jcast('int', m)
            while (j > 0):
                k = jcast('int', 1)
                while (k <= jstatic('Math', 'min', t, j)):
                    jset(dp, j, jstatic('Math', 'max', dp[j], jcast('int', jadd(dp[jcast('int', (j - k))], preSum[k]))))
                    k = jcast('int', (k + 1))
                j = jcast('int', (j - 1))
        return jcast('int', dp[m])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


