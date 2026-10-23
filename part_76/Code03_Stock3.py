# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 买卖股票的最佳时机 III
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易
# 注意：你不能同时参与多笔交易，你必须在再次购买前出售掉之前的股票
# 测试链接 : https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii
class Code03_Stock3:
    __java_fields__ = {}
    # 完全不优化枚举的方法
    # 通过不了，会超时
    @staticmethod
    def maxProfit1(prices):
        n = jcast('int', jget(prices, 'length'))
        # dp1[i] : 0...i范围上发生一次交易，不要求在i的时刻卖出，最大利润是多少
        dp1 = jarray('int', [n])
        i = jcast('int', 1)
        min = jcast('int', prices[0])
        while (i < n):
            min = jcast('int', jstatic('Math', 'min', min, prices[i]))
            jset(dp1, i, jstatic('Math', 'max', dp1[jcast('int', (i - 1))], jcast('int', (prices[i] - min))))
            i = jcast('int', (i + 1))
        # dp2[i] : 0...i范围上发生两次交易，并且第二次交易在i时刻卖出，最大利润是多少
        dp2 = jarray('int', [n])
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i < n):
            # 第二次交易一定要在i时刻卖出
            j = jcast('int', 0)
            while (j <= i):
                # 枚举第二次交易的买入时机j <= i
                jset(dp2, i, jstatic('Math', 'max', dp2[i], jcast('int', (jcast('int', jadd(dp1[j], prices[i])) - prices[j]))))
                j = jcast('int', (j + 1))
            ans = jcast('int', jstatic('Math', 'max', ans, dp2[i]))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 观察出优化枚举的方法
    # 引入best数组，需要分析能力
    @staticmethod
    def maxProfit2(prices):
        n = jcast('int', jget(prices, 'length'))
        # dp1[i] : 0...i范围上发生一次交易，不要求在i的时刻卖出，最大利润是多少
        dp1 = jarray('int', [n])
        i = jcast('int', 1)
        min = jcast('int', prices[0])
        while (i < n):
            min = jcast('int', jstatic('Math', 'min', min, prices[i]))
            jset(dp1, i, jstatic('Math', 'max', dp1[jcast('int', (i - 1))], jcast('int', (prices[i] - min))))
            i = jcast('int', (i + 1))
        # best[i] : 0...i范围上，所有的dp1[i]-prices[i]，最大值是多少
        # 这是数组的设置完全是为了替代最后for循环的枚举行为
        best = jarray('int', [n])
        best[0] = jcast('int', jcast('int', (dp1[0] - prices[0])))
        i = jcast('int', 1)
        while (i < n):
            jset(best, i, jstatic('Math', 'max', best[jcast('int', (i - 1))], jcast('int', (dp1[i] - prices[i]))))
            i = jcast('int', (i + 1))
        # dp2[i] : 0...i范围上发生两次交易，并且第二次交易在i时刻卖出，最大利润是多少
        dp2 = jarray('int', [n])
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i < n):
            # 不需要枚举了
            # 因为，best[i]已经揭示了，0...i范围上，所有的dp1[i]-prices[i]，最大值是多少
            dp2[i] = jcast('int', jcast('int', jadd(best[i], prices[i])))
            ans = jcast('int', jstatic('Math', 'max', ans, dp2[i]))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 发现所有更新行为都可以放在一起
    # 并不需要写多个并列的for循环
    # 就是等义改写，不需要分析能力
    @staticmethod
    def maxProfit3(prices):
        n = jcast('int', jget(prices, 'length'))
        dp1 = jarray('int', [n])
        best = jarray('int', [n])
        best[0] = jcast('int', jcast('int', (-prices[0])))
        dp2 = jarray('int', [n])
        ans = jcast('int', 0)
        i = jcast('int', 1)
        min = jcast('int', prices[0])
        while (i < n):
            min = jcast('int', jstatic('Math', 'min', min, prices[i]))
            jset(dp1, i, jstatic('Math', 'max', dp1[jcast('int', (i - 1))], jcast('int', (prices[i] - min))))
            jset(best, i, jstatic('Math', 'max', best[jcast('int', (i - 1))], jcast('int', (dp1[i] - prices[i]))))
            dp2[i] = jcast('int', jcast('int', jadd(best[i], prices[i])))
            ans = jcast('int', jstatic('Math', 'max', ans, dp2[i]))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 发现只需要有限几个变量滚动更新下去就可以了
    # 空间压缩的版本
    # 就是等义改写，不需要分析能力
    @staticmethod
    def maxProfit4(prices):
        dp1 = jcast('int', 0)
        best = jcast('int', jcast('int', (-prices[0])))
        ans = jcast('int', 0)
        i = jcast('int', 1)
        min = jcast('int', prices[0])
        while (i < jget(prices, 'length')):
            min = jcast('int', jstatic('Math', 'min', min, prices[i]))
            dp1 = jcast('int', jstatic('Math', 'max', dp1, jcast('int', (prices[i] - min))))
            best = jcast('int', jstatic('Math', 'max', best, jcast('int', (dp1 - prices[i]))))
            # ans = Math.max(ans, dp2);
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(best, prices[i]))))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


