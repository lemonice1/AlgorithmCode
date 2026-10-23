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

# 买卖股票的最佳时机含手续费
# 给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格
# 整数 fee 代表了交易股票的手续费用
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费
# 如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
# 返回获得利润的最大值
# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费
# 测试链接 : https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
class Code05_Stack5:
    __java_fields__ = {}
    @staticmethod
    def maxProfit(prices, fee):
        fee = jcast('int', fee)
        # prepare : 交易次数无限制情况下，获得收益的同时扣掉了一次购买和手续费之后，最好的情况
        prepare = jcast('int', jcast('int', (jcast('int', (-prices[0])) - fee)))
        # done : 交易次数无限制情况下，能获得的最大收益
        done = jcast('int', 0)
        i = jcast('int', 1)
        while (i < jget(prices, 'length')):
            done = jcast('int', jstatic('Math', 'max', done, jcast('int', jadd(prepare, prices[i]))))
            prepare = jcast('int', jstatic('Math', 'max', prepare, jcast('int', (jcast('int', (done - prices[i])) - fee))))
            i = jcast('int', (i + 1))
        return jcast('int', done)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


