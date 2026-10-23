# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 盈利计划(多维费用背包)
# 集团里有 n 名员工，他们可以完成各种各样的工作创造利润
# 第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与
# 如果成员参与了其中一项工作，就不能参与另一项工作
# 工作的任何至少产生 minProfit 利润的子集称为 盈利计划
# 并且工作的成员总数最多为 n
# 有多少种计划可以选择？因为答案很大，答案对 1000000007 取模
# 测试链接 : https://leetcode.cn/problems/profitable-schemes/
class Code02_ProfitableSchemes:
    __java_fields__ = {'mod': 'mod'}
    # n : 员工的额度，不能超
    # p : 利润的额度，不能少
    # group[i] : i号项目需要几个人
    # profit[i] : i号项目产生的利润
    # 返回能做到员工不能超过n，利润不能少于p的计划有多少个
    @staticmethod
    def profitableSchemes1(n, minProfit, group, profit):
        n = jcast('int', n)
        minProfit = jcast('int', minProfit)
        return jcast('int', Code02_ProfitableSchemes.f1(group, profit, 0, n, minProfit))

    # i : 来到i号工作
    # r : 员工额度还有r人，如果r<=0说明已经没法再选择工作了
    # s : 利润还有s才能达标，如果s<=0说明之前的选择已经让利润达标了
    # 返回 : i.... r、s，有多少种方案
    @staticmethod
    def f1(g, p, i, r, s):
        i = jcast('int', i)
        r = jcast('int', r)
        s = jcast('int', s)
        if (r <= 0):
            # 人已经耗尽了，之前可能选了一些工作
            return jcast('int', (1 if (s <= 0) else 0))
        # r > 0
        if (i == jget(g, 'length')):
            # 工作耗尽了，之前可能选了一些工作
            return jcast('int', (1 if (s <= 0) else 0))
        # 不要当前工作
        p1 = jcast('int', Code02_ProfitableSchemes.f1(g, p, jcast('int', jadd(i, 1)), r, s))
        # 要做当前工作
        p2 = jcast('int', 0)
        if (g[i] <= r):
            p2 = jcast('int', Code02_ProfitableSchemes.f1(g, p, jcast('int', jadd(i, 1)), jcast('int', (r - g[i])), jcast('int', (s - p[i]))))
        return jcast('int', jcast('int', jadd(p1, p2)))

    mod = 0
    @staticmethod
    def profitableSchemes2(n, minProfit, group, profit):
        n = jcast('int', n)
        minProfit = jcast('int', minProfit)
        m = jcast('int', jget(group, 'length'))
        dp = jarray('int', [m, jcast('int', jadd(n, 1)), jcast('int', jadd(minProfit, 1))])
        a = jcast('int', 0)
        while (a < m):
            b = jcast('int', 0)
            while (b <= n):
                c = jcast('int', 0)
                while (c <= minProfit):
                    jset(dp[a][b], c, jcast('int', (-1)))
                    c = jcast('int', (c + 1))
                b = jcast('int', (b + 1))
            a = jcast('int', (a + 1))
        return jcast('int', Code02_ProfitableSchemes.f2(group, profit, 0, n, minProfit, dp))

    @staticmethod
    def f2(g, p, i, r, s, dp):
        i = jcast('int', i)
        r = jcast('int', r)
        s = jcast('int', s)
        if (r <= 0):
            return jcast('int', (1 if (s == 0) else 0))
        if (i == jget(g, 'length')):
            return jcast('int', (1 if (s == 0) else 0))
        if (dp[i][r][s] != jcast('int', (-1))):
            return jcast('int', dp[i][r][s])
        p1 = jcast('int', Code02_ProfitableSchemes.f2(g, p, jcast('int', jadd(i, 1)), r, s, dp))
        p2 = jcast('int', 0)
        if (g[i] <= r):
            p2 = jcast('int', Code02_ProfitableSchemes.f2(g, p, jcast('int', jadd(i, 1)), jcast('int', (r - g[i])), jstatic('Math', 'max', 0, jcast('int', (s - p[i]))), dp))
        ans = jcast('int', jcast('int', jmod(jcast('int', jadd(p1, p2)), Code02_ProfitableSchemes.mod)))
        jset(dp[i][r], s, ans)
        return jcast('int', ans)

    @staticmethod
    def profitableSchemes3(n, minProfit, group, profit):
        n = jcast('int', n)
        minProfit = jcast('int', minProfit)
        # i = 没有工作的时候，i == g.length
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(minProfit, 1))])
        r = jcast('int', 0)
        while (r <= n):
            jset(dp[r], 0, 1)
            r = jcast('int', (r + 1))
        m = jcast('int', jget(group, 'length'))
        i = jcast('int', jcast('int', (m - 1)))
        while (i >= 0):
            r = jcast('int', n)
            while (r >= 0):
                s = jcast('int', minProfit)
                while (s >= 0):
                    p1 = jcast('int', dp[r][s])
                    p2 = jcast('int', (dp[jcast('int', (r - group[i]))][jstatic('Math', 'max', 0, jcast('int', (s - profit[i])))] if (group[i] <= r) else 0))
                    jset(dp[r], s, jcast('int', jmod(jcast('int', jadd(p1, p2)), Code02_ProfitableSchemes.mod)))
                    s = jcast('int', (s - 1))
                r = jcast('int', (r - 1))
            i = jcast('int', (i - 1))
        return jcast('int', dp[n][minProfit])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_ProfitableSchemes.mod = jcast('int', 1000000007)
