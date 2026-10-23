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

# 切棍子的最小成本
# 有一根长度为n个单位的木棍，棍上从0到n标记了若干位置
# 给你一个整数数组cuts，其中cuts[i]表示你需要将棍子切开的位置
# 你可以按顺序完成切割，也可以根据需要更改切割的顺序
# 每次切割的成本都是当前要切割的棍子的长度，切棍子的总成本是历次切割成本的总和
# 对棍子进行切割将会把一根木棍分成两根较小的木棍
# 这两根木棍的长度和就是切割前木棍的长度
# 返回切棍子的最小总成本
# 测试链接 : https://leetcode.cn/problems/minimum-cost-to-cut-a-stick/
class Code04_MinimumCostToCutAStick:
    __java_fields__ = {}
    # 记忆化搜索
    @staticmethod
    def minCost1(n, cuts):
        n = jcast('int', n)
        m = jcast('int', jget(cuts, 'length'))
        jstatic('Arrays', 'sort', cuts)
        arr = jarray('int', [jcast('int', jadd(m, 2))])
        arr[0] = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= m):
            arr[i] = jcast('int', cuts[jcast('int', (i - 1))])
            i = jcast('int', (i + 1))
        arr[jcast('int', jadd(m, 1))] = jcast('int', n)
        dp = jarray('int', [jcast('int', jadd(m, 2)), jcast('int', jadd(m, 2))])
        i = jcast('int', 1)
        while (i <= m):
            j = jcast('int', 1)
            while (j <= m):
                jset(dp[i], j, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code04_MinimumCostToCutAStick.f(arr, 1, m, dp))

    # 切点[l....r]，决定一个顺序
    # 让切点都切完，总代价最小
    @staticmethod
    def f(arr, l, r, dp):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l > r):
            return jcast('int', 0)
        if (l == r):
            return jcast('int', jcast('int', (arr[jcast('int', jadd(r, 1))] - arr[jcast('int', (l - 1))])))
        if (dp[l][r] != jcast('int', (-1))):
            return jcast('int', dp[l][r])
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        k = jcast('int', l)
        while (k <= r):
            ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(Code04_MinimumCostToCutAStick.f(arr, l, jcast('int', (k - 1)), dp), Code04_MinimumCostToCutAStick.f(arr, jcast('int', jadd(k, 1)), r, dp)))))
            k = jcast('int', (k + 1))
        ans = jcast('int', jcast('int', jadd(ans, jcast('int', (arr[jcast('int', jadd(r, 1))] - arr[jcast('int', (l - 1))])))))
        jset(dp[l], r, ans)
        return jcast('int', ans)

    # 严格位置依赖的动态规划
    @staticmethod
    def minCost2(n, cuts):
        n = jcast('int', n)
        m = jcast('int', jget(cuts, 'length'))
        jstatic('Arrays', 'sort', cuts)
        arr = jarray('int', [jcast('int', jadd(m, 2))])
        arr[0] = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= m):
            arr[i] = jcast('int', cuts[jcast('int', (i - 1))])
            i = jcast('int', (i + 1))
        arr[jcast('int', jadd(m, 1))] = jcast('int', n)
        dp = jarray('int', [jcast('int', jadd(m, 2)), jcast('int', jadd(m, 2))])
        i = jcast('int', 1)
        while (i <= m):
            jset(dp[i], i, jcast('int', (arr[jcast('int', jadd(i, 1))] - arr[jcast('int', (i - 1))])))
            i = jcast('int', (i + 1))
        l = jcast('int', jcast('int', (m - 1)))
        next = 0
        while (l >= 1):
            r = jcast('int', jcast('int', jadd(l, 1)))
            while (r <= m):
                next = jcast('int', jget(Integer, 'MAX_VALUE'))
                k = jcast('int', l)
                while (k <= r):
                    next = jcast('int', jstatic('Math', 'min', next, jcast('int', jadd(dp[l][jcast('int', (k - 1))], dp[jcast('int', jadd(k, 1))][r]))))
                    k = jcast('int', (k + 1))
                jset(dp[l], r, jcast('int', jadd(jcast('int', (arr[jcast('int', jadd(r, 1))] - arr[jcast('int', (l - 1))])), next)))
                r = jcast('int', (r + 1))
            l = jcast('int', (l - 1))
        return jcast('int', dp[1][m])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


