# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 每个人戴不同帽子的方案数
# 总共有 n 个人和 40 种不同的帽子，帽子编号从 1 到 40
# 给你一个整数列表的列表 hats ，其中 hats[i] 是第 i 个人所有喜欢帽子的列表
# 请你给每个人安排一顶他喜欢的帽子，确保每个人戴的帽子跟别人都不一样，并返回方案数
# 由于答案可能很大，答案对 1000000007 取模
# 测试链接 : https://leetcode.cn/problems/number-of-ways-to-wear-different-hats-to-each-other
class Code01_NumberOfWaysWearDifferentHats:
    __java_fields__ = {'MOD': 'MOD'}
    MOD = 0
    @staticmethod
    def numberWays(arr):
        # 帽子颜色的最大值
        m = jcast('int', 0)
        for person in arr:
            for hat in person:
                m = jcast('int', jstatic('Math', 'max', m, hat))
        n = jcast('int', jcall(arr, 'size'))
        # 1 ~ m 帽子，能满足哪些人，状态信息 -> int
        hats = jarray('int', [jcast('int', jadd(m, 1))])
        pi = jcast('int', 0)
        while (pi < n):
            for hat in jcall(arr, 'get', pi):
                hats[hat] = jcast('int', jcast('int', (hats[hat] | jcast('int', (1 << (pi & 31))))))
            pi = jcast('int', (pi + 1))
        dp = jarray('int', [jcast('int', jadd(m, 1)), jcast('int', (1 << (n & 31)))])
        i = jcast('int', 0)
        while (i <= m):
            jstatic('Arrays', 'fill', dp[i], jcast('int', (-1)))
            i = jcast('int', (i + 1))
        return jcast('int', Code01_NumberOfWaysWearDifferentHats.f2(hats, m, n, 1, 0, dp))

    # m : 帽子颜色的最大值, 1 ~ m
    # n : 人的数量，0 ~ n-1
    # i : 来到了什么颜色的帽子
    # s : n个人，谁没满足状态就是0，谁满足了状态就是1
    # dp : 记忆化搜索的表
    # 返回 : 有多少种方法
    @staticmethod
    def f1(hats, m, n, i, s, dp):
        m = jcast('int', m)
        n = jcast('int', n)
        i = jcast('int', i)
        s = jcast('int', s)
        if (s == jcast('int', (jcast('int', (1 << (n & 31))) - 1))):
            return jcast('int', 1)
        # 还有人没满足
        if (i == jcast('int', jadd(m, 1))):
            return jcast('int', 0)
        if (dp[i][s] != jcast('int', (-1))):
            return jcast('int', dp[i][s])
        # 可能性1 : i颜色的帽子，不分配给任何人
        ans = jcast('int', Code01_NumberOfWaysWearDifferentHats.f1(hats, m, n, jcast('int', jadd(i, 1)), s, dp))
        # 可能性2 : i颜色的帽子，分配给可能的每一个人
        cur = jcast('int', hats[i])
        # 用for循环从0 ~ n-1枚举每个人
        p = jcast('int', 0)
        while (p < n):
            if ((jcast('int', (cur & jcast('int', (1 << (p & 31))))) != 0) and (jcast('int', (s & jcast('int', (1 << (p & 31))))) == 0)):
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code01_NumberOfWaysWearDifferentHats.f1(hats, m, n, jcast('int', jadd(i, 1)), jcast('int', (s | jcast('int', (1 << (p & 31))))), dp))), Code01_NumberOfWaysWearDifferentHats.MOD)))
            p = jcast('int', (p + 1))
        jset(dp[i], s, ans)
        return jcast('int', ans)

    @staticmethod
    def f2(hats, m, n, i, s, dp):
        m = jcast('int', m)
        n = jcast('int', n)
        i = jcast('int', i)
        s = jcast('int', s)
        if (s == jcast('int', (jcast('int', (1 << (n & 31))) - 1))):
            return jcast('int', 1)
        if (i == jcast('int', jadd(m, 1))):
            return jcast('int', 0)
        if (dp[i][s] != jcast('int', (-1))):
            return jcast('int', dp[i][s])
        ans = jcast('int', Code01_NumberOfWaysWearDifferentHats.f2(hats, m, n, jcast('int', jadd(i, 1)), s, dp))
        cur = jcast('int', hats[i])
        # 不用for循环枚举
        # 从当前帽子中依次提取能满足的人
        # 提取出二进制状态中最右侧的1，讲解030-异或运算，题目5，Brian Kernighan算法
        # cur :
        # 0 0 0 1 1 0 1 0
        # -> 0 0 0 0 0 0 1 0
        # -> 0 0 0 0 1 0 0 0
        # -> 0 0 0 1 0 0 0 0
        rightOne = 0
        while (cur != 0):
            rightOne = jcast('int', jcast('int', (cur & jcast('int', (-cur)))))
            if (jcast('int', (s & rightOne)) == 0):
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code01_NumberOfWaysWearDifferentHats.f2(hats, m, n, jcast('int', jadd(i, 1)), jcast('int', (s | rightOne)), dp))), Code01_NumberOfWaysWearDifferentHats.MOD)))
            cur = jcast('int', jcast('int', (cur ^ rightOne)))
        jset(dp[i], s, ans)
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_NumberOfWaysWearDifferentHats.MOD = jcast('int', 1000000007)
