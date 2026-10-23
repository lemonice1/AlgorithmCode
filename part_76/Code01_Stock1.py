# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 买卖股票的最佳时机
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票
# 设计一个算法来计算你所能获取的最大利润
# 返回你可以从这笔交易中获取的最大利润
# 如果你不能获取任何利润，返回 0
# 测试链接 : https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
class Code01_Stock1:
    __java_fields__ = {}
    @staticmethod
    def maxProfit(prices):
        ans = jcast('int', 0)
        i = jcast('int', 1)
        min = jcast('int', prices[0])
        while (i < jget(prices, 'length')):
            # min : 0...i范围上的最小值
            min = jcast('int', jstatic('Math', 'min', min, prices[i]))
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', (prices[i] - min))))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


