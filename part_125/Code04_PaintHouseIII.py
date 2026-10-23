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

# 粉刷房子III
# 房子有n个，从左到右排列，编号1..n，颜色有c种，编号1..c
# 给定数组house，house[i]表示房子的颜色，如果house[i]为0说明房子没有涂色
# 你必须给每个没有涂色的房子涂上颜色，如果有颜色的房子不能改变颜色
# 给定二维数组cost，cost[i][v]表示如果i号房涂成v号颜色，需要花费多少钱
# 相邻的、拥有同一种颜色的房子为1个街区
# 比如如果所有房子的颜色为: {1, 1, 2, 3, 2, 2}，那么一共4个街区
# 最终所有的房子涂完颜色，一定要形成t个街区，返回最少的花费
# 1 <= t <= n <= 100
# 1 <= c <= 20
# 0 <= house[i] <= c
# 1 <= cost[i][v] <= 10^4
# 测试链接 : https://leetcode.cn/problems/paint-house-iii/
class Code04_PaintHouseIII:
    __java_fields__ = {'NA': 'NA', 'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXC': 'MAXC', 'house': 'house', 'cost': 'cost', 'n': 'n', 't': 't', 'c': 'c'}
    NA = 0
    MAXN = 0
    MAXT = 0
    MAXC = 0
    house = None
    cost = None
    n = 0
    t = 0
    c = 0
    # 原始测试页面的数据描述非常绕，一律转化成课上描述的形式
    # 房子编号从1开始，颜色编号从1开始，颜色0代表没有涂色
    # build方法就是转化逻辑
    @staticmethod
    def build(houses, costs, hsize, csize, tsize):
        hsize = jcast('int', hsize)
        csize = jcast('int', csize)
        tsize = jcast('int', tsize)
        Code04_PaintHouseIII.n = jcast('int', hsize)
        Code04_PaintHouseIII.t = jcast('int', tsize)
        Code04_PaintHouseIII.c = jcast('int', csize)
        i = jcast('int', 1)
        while (i <= Code04_PaintHouseIII.n):
            Code04_PaintHouseIII.house[i] = jcast('int', houses[jcast('int', (i - 1))])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_PaintHouseIII.n):
            j = jcast('int', 1)
            while (j <= Code04_PaintHouseIII.c):
                jset(Code04_PaintHouseIII.cost[i], j, costs[jcast('int', (i - 1))][jcast('int', (j - 1))])
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    # 递归 + 记忆化搜索，不优化枚举
    # 时间复杂度O(n * t * c平方)
    @staticmethod
    def minCost1(houses, costs, hsize, csize, tsize):
        hsize = jcast('int', hsize)
        csize = jcast('int', csize)
        tsize = jcast('int', tsize)
        Code04_PaintHouseIII.build(houses, costs, hsize, csize, tsize)
        Code04_PaintHouseIII.t = jcast('int', (Code04_PaintHouseIII.t + 1))
        dp = jarray('int', [jcast('int', jadd(Code04_PaintHouseIII.n, 1)), jcast('int', jadd(Code04_PaintHouseIII.t, 1)), jcast('int', jadd(Code04_PaintHouseIII.c, 1))])
        i = jcast('int', 0)
        while (i <= Code04_PaintHouseIII.n):
            j = jcast('int', 0)
            while (j <= Code04_PaintHouseIII.t):
                v = jcast('int', 0)
                while (v <= Code04_PaintHouseIII.c):
                    jset(dp[i][j], v, jcast('int', (-1)))
                    v = jcast('int', (v + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', Code04_PaintHouseIII.f1(Code04_PaintHouseIII.n, Code04_PaintHouseIII.t, 0, dp))
        return jcast('int', (jcast('int', (-1)) if (ans == Code04_PaintHouseIII.NA) else ans))

    # 1...i范围的房子去确定颜色，i+1号房子的颜色已经涂成了v
    # 1...i+1范围的房子必须凑齐j个街区，返回最少的花费
    # 如果做不到返回NA
    @staticmethod
    def f1(i, j, v, dp):
        i = jcast('int', i)
        j = jcast('int', j)
        v = jcast('int', v)
        if (j == 0):
            return jcast('int', Code04_PaintHouseIII.NA)
        if (i == 0):
            return jcast('int', (0 if (j == 1) else Code04_PaintHouseIII.NA))
        if (dp[i][j][v] != jcast('int', (-1))):
            return jcast('int', dp[i][j][v])
        ans = jcast('int', Code04_PaintHouseIII.NA)
        if (Code04_PaintHouseIII.house[i] != 0):
            if (Code04_PaintHouseIII.house[i] == v):
                ans = jcast('int', Code04_PaintHouseIII.f1(jcast('int', (i - 1)), j, Code04_PaintHouseIII.house[i], dp))
            else:
                ans = jcast('int', Code04_PaintHouseIII.f1(jcast('int', (i - 1)), jcast('int', (j - 1)), Code04_PaintHouseIII.house[i], dp))
        else:
            color = jcast('int', 1)
            next = 0
            while (color <= Code04_PaintHouseIII.c):
                if (color == v):
                    next = jcast('int', Code04_PaintHouseIII.f1(jcast('int', (i - 1)), j, color, dp))
                else:
                    next = jcast('int', Code04_PaintHouseIII.f1(jcast('int', (i - 1)), jcast('int', (j - 1)), color, dp))
                if (next != Code04_PaintHouseIII.NA):
                    ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(next, Code04_PaintHouseIII.cost[i][color]))))
                color = jcast('int', (color + 1))
        jset(dp[i][j], v, ans)
        return jcast('int', ans)

    # 严格位置依赖的动态规划，不优化枚举
    # 时间复杂度O(n * t * c平方)
    @staticmethod
    def minCost2(houses, costs, hsize, csize, tsize):
        hsize = jcast('int', hsize)
        csize = jcast('int', csize)
        tsize = jcast('int', tsize)
        Code04_PaintHouseIII.build(houses, costs, hsize, csize, tsize)
        Code04_PaintHouseIII.t = jcast('int', (Code04_PaintHouseIII.t + 1))
        dp = jarray('int', [jcast('int', jadd(Code04_PaintHouseIII.n, 1)), jcast('int', jadd(Code04_PaintHouseIII.t, 1)), jcast('int', jadd(Code04_PaintHouseIII.c, 1))])
        i = jcast('int', 0)
        while (i <= Code04_PaintHouseIII.n):
            v = jcast('int', 0)
            while (v <= Code04_PaintHouseIII.c):
                jset(dp[i][0], v, Code04_PaintHouseIII.NA)
                v = jcast('int', (v + 1))
            i = jcast('int', (i + 1))
        j = jcast('int', 1)
        while (j <= Code04_PaintHouseIII.t):
            v = jcast('int', 0)
            while (v <= Code04_PaintHouseIII.c):
                jset(dp[0][j], v, (0 if (j == 1) else Code04_PaintHouseIII.NA))
                v = jcast('int', (v + 1))
            j = jcast('int', (j + 1))
        i = jcast('int', 1)
        while (i <= Code04_PaintHouseIII.n):
            j = jcast('int', 1)
            while (j <= Code04_PaintHouseIII.t):
                v = jcast('int', 0)
                while (v <= Code04_PaintHouseIII.c):
                    ans = jcast('int', Code04_PaintHouseIII.NA)
                    if (Code04_PaintHouseIII.house[i] != 0):
                        if (Code04_PaintHouseIII.house[i] == v):
                            ans = jcast('int', dp[jcast('int', (i - 1))][j][Code04_PaintHouseIII.house[i]])
                        else:
                            ans = jcast('int', dp[jcast('int', (i - 1))][jcast('int', (j - 1))][Code04_PaintHouseIII.house[i]])
                    else:
                        color = jcast('int', 1)
                        next = 0
                        while (color <= Code04_PaintHouseIII.c):
                            if (color == v):
                                next = jcast('int', dp[jcast('int', (i - 1))][j][color])
                            else:
                                next = jcast('int', dp[jcast('int', (i - 1))][jcast('int', (j - 1))][color])
                            if (next != Code04_PaintHouseIII.NA):
                                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(next, Code04_PaintHouseIII.cost[i][color]))))
                            color = jcast('int', (color + 1))
                    jset(dp[i][j], v, ans)
                    v = jcast('int', (v + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', dp[Code04_PaintHouseIII.n][Code04_PaintHouseIII.t][0])
        return jcast('int', (jcast('int', (-1)) if (ans == Code04_PaintHouseIII.NA) else ans))

    # 空间压缩版本，不优化枚举
    # 时间复杂度O(n * t * c平方)
    @staticmethod
    def minCost3(houses, costs, hsize, csize, tsize):
        hsize = jcast('int', hsize)
        csize = jcast('int', csize)
        tsize = jcast('int', tsize)
        Code04_PaintHouseIII.build(houses, costs, hsize, csize, tsize)
        Code04_PaintHouseIII.t = jcast('int', (Code04_PaintHouseIII.t + 1))
        memo = jarray('int', [jcast('int', jadd(Code04_PaintHouseIII.t, 1)), jcast('int', jadd(Code04_PaintHouseIII.c, 1))])
        dp = jarray('int', [jcast('int', jadd(Code04_PaintHouseIII.t, 1)), jcast('int', jadd(Code04_PaintHouseIII.c, 1))])
        # 因为此时只有memo、dp两份空间
        # 所以让memo[0][v] = dp[0][v] = NA
        # 这样一来，在滚动更新时，不管i是多少，只要j==0，那么结果都是NA
        v = jcast('int', 0)
        while (v <= Code04_PaintHouseIII.c):
            jset(memo[0], v, jset(dp[0], v, Code04_PaintHouseIII.NA))
            v = jcast('int', (v + 1))
        # i == 0时，结果填入memo表
        j = jcast('int', 1)
        while (j <= Code04_PaintHouseIII.t):
            v = jcast('int', 0)
            while (v <= Code04_PaintHouseIII.c):
                jset(memo[j], v, (0 if (j == 1) else Code04_PaintHouseIII.NA))
                v = jcast('int', (v + 1))
            j = jcast('int', (j + 1))
        # 滚动更新
        i = jcast('int', 1)
        while (i <= Code04_PaintHouseIII.n):
            j = jcast('int', 1)
            while (j <= Code04_PaintHouseIII.t):
                v = jcast('int', 0)
                while (v <= Code04_PaintHouseIII.c):
                    ans = jcast('int', Code04_PaintHouseIII.NA)
                    if (Code04_PaintHouseIII.house[i] != 0):
                        if (Code04_PaintHouseIII.house[i] == v):
                            ans = jcast('int', memo[j][Code04_PaintHouseIII.house[i]])
                        else:
                            ans = jcast('int', memo[jcast('int', (j - 1))][Code04_PaintHouseIII.house[i]])
                    else:
                        color = jcast('int', 1)
                        next = 0
                        while (color <= Code04_PaintHouseIII.c):
                            if (color == v):
                                next = jcast('int', memo[j][color])
                            else:
                                next = jcast('int', memo[jcast('int', (j - 1))][color])
                            if (next != Code04_PaintHouseIII.NA):
                                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(next, Code04_PaintHouseIII.cost[i][color]))))
                            color = jcast('int', (color + 1))
                    jset(dp[j], v, ans)
                    v = jcast('int', (v + 1))
                j = jcast('int', (j + 1))
            tmp = memo
            memo = dp
            dp = tmp
            i = jcast('int', (i + 1))
        ans = jcast('int', memo[Code04_PaintHouseIII.t][0])
        return jcast('int', (jcast('int', (-1)) if (ans == Code04_PaintHouseIII.NA) else ans))

    # 最优解
    # 优化枚举 + 空间压缩
    # 时间复杂度O(n * t * c)
    @staticmethod
    def minCost4(houses, costs, hsize, csize, tsize):
        hsize = jcast('int', hsize)
        csize = jcast('int', csize)
        tsize = jcast('int', tsize)
        Code04_PaintHouseIII.build(houses, costs, hsize, csize, tsize)
        Code04_PaintHouseIII.t = jcast('int', (Code04_PaintHouseIII.t + 1))
        memo = jarray('int', [jcast('int', jadd(Code04_PaintHouseIII.t, 1)), jcast('int', jadd(Code04_PaintHouseIII.c, 1))])
        dp = jarray('int', [jcast('int', jadd(Code04_PaintHouseIII.t, 1)), jcast('int', jadd(Code04_PaintHouseIII.c, 1))])
        v = jcast('int', 0)
        while (v <= Code04_PaintHouseIII.c):
            jset(memo[0], v, jset(dp[0], v, Code04_PaintHouseIII.NA))
            v = jcast('int', (v + 1))
        j = jcast('int', 1)
        while (j <= Code04_PaintHouseIII.t):
            v = jcast('int', 0)
            while (v <= Code04_PaintHouseIII.c):
                jset(memo[j], v, (0 if (j == 1) else Code04_PaintHouseIII.NA))
                v = jcast('int', (v + 1))
            j = jcast('int', (j + 1))
        # pre[s] : dp[i-1][j][1...s] + cost[i][1...s]中的最小值
        # suf[s] : dp[i-1][j][s...c] + cost[i][s...c]中的最小值
        pre = jarray('int', [jcast('int', jadd(Code04_PaintHouseIII.c, 2))])
        suf = jarray('int', [jcast('int', jadd(Code04_PaintHouseIII.c, 2))])
        jset(pre, 0, jset(suf, jcast('int', jadd(Code04_PaintHouseIII.c, 1)), Code04_PaintHouseIII.NA))
        i = jcast('int', 1)
        while (i <= Code04_PaintHouseIII.n):
            j = jcast('int', 1)
            while (j <= Code04_PaintHouseIII.t):
                # 预处理结构优化前缀枚举
                v = jcast('int', 1)
                while (v <= Code04_PaintHouseIII.c):
                    pre[v] = jcast('int', pre[jcast('int', (v - 1))])
                    if (memo[jcast('int', (j - 1))][v] != Code04_PaintHouseIII.NA):
                        jset(pre, v, jstatic('Math', 'min', pre[v], jcast('int', jadd(memo[jcast('int', (j - 1))][v], Code04_PaintHouseIII.cost[i][v]))))
                    v = jcast('int', (v + 1))
                # 预处理结构优化后缀枚举
                v = jcast('int', Code04_PaintHouseIII.c)
                while (v >= 1):
                    suf[v] = jcast('int', suf[jcast('int', jadd(v, 1))])
                    if (memo[jcast('int', (j - 1))][v] != Code04_PaintHouseIII.NA):
                        jset(suf, v, jstatic('Math', 'min', suf[v], jcast('int', jadd(memo[jcast('int', (j - 1))][v], Code04_PaintHouseIII.cost[i][v]))))
                    v = jcast('int', (v - 1))
                # 填写dp表
                v = jcast('int', 0)
                while (v <= Code04_PaintHouseIII.c):
                    ans = jcast('int', Code04_PaintHouseIII.NA)
                    if (Code04_PaintHouseIII.house[i] != 0):
                        if (Code04_PaintHouseIII.house[i] == v):
                            ans = jcast('int', memo[j][Code04_PaintHouseIII.house[i]])
                        else:
                            ans = jcast('int', memo[jcast('int', (j - 1))][Code04_PaintHouseIII.house[i]])
                    else:
                        if (v == 0):
                            ans = jcast('int', suf[1])
                        else:
                            ans = jcast('int', jstatic('Math', 'min', pre[jcast('int', (v - 1))], suf[jcast('int', jadd(v, 1))]))
                            if (memo[j][v] != Code04_PaintHouseIII.NA):
                                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(memo[j][v], Code04_PaintHouseIII.cost[i][v]))))
                    jset(dp[j], v, ans)
                    v = jcast('int', (v + 1))
                j = jcast('int', (j + 1))
            tmp = memo
            memo = dp
            dp = tmp
            i = jcast('int', (i + 1))
        ans = jcast('int', memo[Code04_PaintHouseIII.t][0])
        return jcast('int', (jcast('int', (-1)) if (ans == Code04_PaintHouseIII.NA) else ans))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_PaintHouseIII.NA = jcast('int', jget(Integer, 'MAX_VALUE'))
Code04_PaintHouseIII.MAXN = jcast('int', 101)
Code04_PaintHouseIII.MAXT = jcast('int', 101)
Code04_PaintHouseIII.MAXC = jcast('int', 21)
Code04_PaintHouseIII.house = jarray('int', [Code04_PaintHouseIII.MAXN])
Code04_PaintHouseIII.cost = jarray('int', [Code04_PaintHouseIII.MAXN, Code04_PaintHouseIII.MAXC])
Code04_PaintHouseIII.n = jcast('int', 0)
Code04_PaintHouseIII.t = jcast('int', 0)
Code04_PaintHouseIII.c = jcast('int', 0)
