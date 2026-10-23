# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 买卖股票的最佳时机含冷冻期
# 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格
# 设计一个算法计算出最大利润
# 在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）
# 测试链接 : https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/
class Code06_Stack6:
    __java_fields__ = {}
    @staticmethod
    def maxProfit1(prices):
        n = jcast('int', jget(prices, 'length'))
        if (n < 2):
            return jcast('int', 0)
        # prepare[i] : 0...i范围上，可以做无限次交易，获得收益的同时一定要扣掉一次购买，所有情况中的最好情况
        prepare = jarray('int', [n])
        # done[i] : 0...i范围上，可以做无限次交易，能获得的最大收益
        done = jarray('int', [n])
        jset(prepare, 1, jstatic('Math', 'max', jcast('int', (-prices[0])), jcast('int', (-prices[1]))))
        jset(done, 1, jstatic('Math', 'max', 0, jcast('int', (prices[1] - prices[0]))))
        i = jcast('int', 2)
        while (i < n):
            jset(done, i, jstatic('Math', 'max', done[jcast('int', (i - 1))], jcast('int', jadd(prepare[jcast('int', (i - 1))], prices[i]))))
            jset(prepare, i, jstatic('Math', 'max', prepare[jcast('int', (i - 1))], jcast('int', (done[jcast('int', (i - 2))] - prices[i]))))
            i = jcast('int', (i + 1))
        return jcast('int', done[jcast('int', (n - 1))])

    # 只是把方法1做了变量滚动更新(空间压缩)
    # 并没有新的东西
    @staticmethod
    def maxProfit2(prices):
        n = jcast('int', jget(prices, 'length'))
        if (n < 2):
            return jcast('int', 0)
        # prepare : prepare[i-1]
        prepare = jcast('int', jstatic('Math', 'max', jcast('int', (-prices[0])), jcast('int', (-prices[1]))))
        # done2 : done[i-2]
        done2 = jcast('int', 0)
        # done1 : done[i-1]
        done1 = jcast('int', jstatic('Math', 'max', 0, jcast('int', (prices[1] - prices[0]))))
        i = jcast('int', 2)
        curDone = 0
        while (i < n):
            # curDone : done[i]
            curDone = jcast('int', jstatic('Math', 'max', done1, jcast('int', jadd(prepare, prices[i]))))
            # prepare : prepare[i-1] -> prepare[i]
            prepare = jcast('int', jstatic('Math', 'max', prepare, jcast('int', (done2 - prices[i]))))
            done2 = jcast('int', done1)
            done1 = jcast('int', curDone)
            i = jcast('int', (i + 1))
        return jcast('int', done1)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


