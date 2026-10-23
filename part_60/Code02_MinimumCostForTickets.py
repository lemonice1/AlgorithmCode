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

# 最低票价
# 在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行
# 在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出
# 每一项是一个从 1 到 365 的整数
# 火车票有 三种不同的销售方式
# 一张 为期1天 的通行证售价为 costs[0] 美元
# 一张 为期7天 的通行证售价为 costs[1] 美元
# 一张 为期30天 的通行证售价为 costs[2] 美元
# 通行证允许数天无限制的旅行
# 例如，如果我们在第 2 天获得一张 为期 7 天 的通行证
# 那么我们可以连着旅行 7 天(第2~8天)
# 返回 你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费
# 测试链接 : https://leetcode.cn/problems/minimum-cost-for-tickets/
class Code02_MinimumCostForTickets:
    __java_fields__ = {'durations': 'durations', 'MAXN': 'MAXN', 'dp': 'dp'}
    # 无论提交什么方法都带着这个数组      0  1  2
    durations = None
    # 暴力尝试
    @staticmethod
    def mincostTickets1(days, costs):
        return jcast('int', Code02_MinimumCostForTickets.f1(days, costs, 0))

    # days[i..... 最少花费是多少
    @staticmethod
    def f1(days, costs, i):
        i = jcast('int', i)
        if (i == jget(days, 'length')):
            # 后续已经无旅行了
            return jcast('int', 0)
        # i下标 : 第days[i]天，有一场旅行
        # i.... 最少花费是多少
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        k = jcast('int', 0)
        j = jcast('int', i)
        while (k < 3):
            # k是方案编号 : 0 1 2
            while ((j < jget(days, 'length')) and (jcast('int', jadd(days[i], Code02_MinimumCostForTickets.durations[k])) > days[j])):
                # 因为方案2持续的天数最多，30天
                # 所以while循环最多执行30次
                # 枚举行为可以认为是O(1)
                j = jcast('int', (j + 1))
            ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(costs[k], Code02_MinimumCostForTickets.f1(days, costs, j)))))
            k = jcast('int', (k + 1))
        return jcast('int', ans)

    # 暴力尝试改记忆化搜索
    # 从顶到底的动态规划
    @staticmethod
    def mincostTickets2(days, costs):
        dp = jarray('int', [jget(days, 'length')])
        i = jcast('int', 0)
        while (i < jget(days, 'length')):
            dp[i] = jcast('int', jget(Integer, 'MAX_VALUE'))
            i = jcast('int', (i + 1))
        return jcast('int', Code02_MinimumCostForTickets.f2(days, costs, 0, dp))

    @staticmethod
    def f2(days, costs, i, dp):
        i = jcast('int', i)
        if (i == jget(days, 'length')):
            return jcast('int', 0)
        if (dp[i] != jget(Integer, 'MAX_VALUE')):
            return jcast('int', dp[i])
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        k = jcast('int', 0)
        j = jcast('int', i)
        while (k < 3):
            while ((j < jget(days, 'length')) and (jcast('int', jadd(days[i], Code02_MinimumCostForTickets.durations[k])) > days[j])):
                j = jcast('int', (j + 1))
            ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(costs[k], Code02_MinimumCostForTickets.f2(days, costs, j, dp)))))
            k = jcast('int', (k + 1))
        dp[i] = jcast('int', ans)
        return jcast('int', ans)

    # 严格位置依赖的动态规划
    # 从底到顶的动态规划
    MAXN = 0
    dp = None
    @staticmethod
    def mincostTickets3(days, costs):
        n = jcast('int', jget(days, 'length'))
        jstatic('Arrays', 'fill', Code02_MinimumCostForTickets.dp, 0, jcast('int', jadd(n, 1)), jget(Integer, 'MAX_VALUE'))
        Code02_MinimumCostForTickets.dp[n] = jcast('int', 0)
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            k = jcast('int', 0)
            j = jcast('int', i)
            while (k < 3):
                while ((j < jget(days, 'length')) and (jcast('int', jadd(days[i], Code02_MinimumCostForTickets.durations[k])) > days[j])):
                    j = jcast('int', (j + 1))
                jset(Code02_MinimumCostForTickets.dp, i, jstatic('Math', 'min', Code02_MinimumCostForTickets.dp[i], jcast('int', jadd(costs[k], Code02_MinimumCostForTickets.dp[j]))))
                k = jcast('int', (k + 1))
            i = jcast('int', (i - 1))
        return jcast('int', Code02_MinimumCostForTickets.dp[0])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_MinimumCostForTickets.durations = jarray('int', [None], [1, 7, 30])
Code02_MinimumCostForTickets.MAXN = jcast('int', 366)
Code02_MinimumCostForTickets.dp = jarray('int', [Code02_MinimumCostForTickets.MAXN])
