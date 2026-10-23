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

# 买卖股票的最佳时机 IV
# 给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易
# 也就是说，你最多可以买 k 次，卖 k 次
# 注意：你不能同时参与多笔交易，你必须在再次购买前出售掉之前的股票
# 测试链接 : https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/
class Code04_Stock4:
    __java_fields__ = {}
    # 就是股票问题2
    @staticmethod
    def free(prices):
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i < jget(prices, 'length')):
            ans = jcast('int', jcast('int', jadd(ans, jstatic('Math', 'max', jcast('int', (prices[i] - prices[jcast('int', (i - 1))])), 0))))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def maxProfit1(k, prices):
        k = jcast('int', k)
        n = jcast('int', jget(prices, 'length'))
        if (k >= jcast('int', jdiv(n, 2))):
            # 这是一个剪枝
            # 如果k >= n / 2，那么代表所有上坡都可以抓到
            # 所有上坡都可以抓到 == 交易次数无限，所以回到股票问题2
            return jcast('int', Code04_Stock4.free(prices))
        dp = jarray('int', [jcast('int', jadd(k, 1)), n])
        i = jcast('int', 1)
        while (i <= k):
            j = jcast('int', 1)
            while (j < n):
                jset(dp[i], j, dp[i][jcast('int', (j - 1))])
                p = jcast('int', 0)
                while (p < j):
                    jset(dp[i], j, jstatic('Math', 'max', dp[i][j], jcast('int', (jcast('int', jadd(dp[jcast('int', (i - 1))][p], prices[j])) - prices[p]))))
                    p = jcast('int', (p + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[k][jcast('int', (n - 1))])

    @staticmethod
    def maxProfit2(k, prices):
        k = jcast('int', k)
        n = jcast('int', jget(prices, 'length'))
        if (k >= jcast('int', jdiv(n, 2))):
            # 这是一个剪枝
            # 如果k >= n / 2，那么代表所有上坡都可以抓到
            # 所有上坡都可以抓到 == 交易次数无限，所以回到股票问题2
            return jcast('int', Code04_Stock4.free(prices))
        dp = jarray('int', [jcast('int', jadd(k, 1)), n])
        i = jcast('int', 1)
        best = 0
        while (i <= k):
            best = jcast('int', jcast('int', (dp[jcast('int', (i - 1))][0] - prices[0])))
            j = jcast('int', 1)
            while (j < n):
                # 用best变量替代了枚举行为
                jset(dp[i], j, jstatic('Math', 'max', dp[i][jcast('int', (j - 1))], jcast('int', jadd(best, prices[j]))))
                best = jcast('int', jstatic('Math', 'max', best, jcast('int', (dp[jcast('int', (i - 1))][j] - prices[j]))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[k][jcast('int', (n - 1))])

    # 对方法2进行空间压缩的版本
    @staticmethod
    def maxProfit3(k, prices):
        k = jcast('int', k)
        n = jcast('int', jget(prices, 'length'))
        if (k >= jcast('int', jdiv(n, 2))):
            # 这是一个剪枝
            # 如果k >= n / 2，那么代表所有上坡都可以抓到
            # 所有上坡都可以抓到 == 交易次数无限，所以回到股票问题2
            return jcast('int', Code04_Stock4.free(prices))
        dp = jarray('int', [n])
        i = jcast('int', 1)
        best = 0
        tmp = 0
        while (i <= k):
            best = jcast('int', jcast('int', (dp[0] - prices[0])))
            j = jcast('int', 1)
            while (j < n):
                tmp = jcast('int', dp[j])
                jset(dp, j, jstatic('Math', 'max', dp[jcast('int', (j - 1))], jcast('int', jadd(best, prices[j]))))
                best = jcast('int', jstatic('Math', 'max', best, jcast('int', (tmp - prices[j]))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[jcast('int', (n - 1))])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


