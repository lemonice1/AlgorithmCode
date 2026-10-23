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

# 买卖股票的最佳时机 II
# 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格
# 在每一天，你可以决定是否购买和/或出售股票
# 你在任何时候 最多 只能持有 一股 股票
# 你也可以先购买，然后在 同一天 出售
# 返回 你能获得的 最大 利润
# 测试链接 : https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/
class Code02_Stock2:
    __java_fields__ = {}
    @staticmethod
    def maxProfit(prices):
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i < jget(prices, 'length')):
            ans = jcast('int', jcast('int', jadd(ans, jstatic('Math', 'max', jcast('int', (prices[i] - prices[jcast('int', (i - 1))])), 0))))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


