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

# 最优账单平衡
# 给你一个表示交易的数组 transactions
# 其中 transactions[i] = [fromi, toi, amounti]
# 表示 ID = fromi 的人给 ID = toi 的人共计 amounti
# 请你计算并返回还清所有债务的最小交易笔数
# 测试链接 : https://leetcode.cn/problems/optimal-account-balancing/
class Code02_OptimalAccountBalancing:
    __java_fields__ = {'MAXN': 'MAXN'}
    # 题目说了人员编号的最大范围：0 ~ 12
    MAXN = 0
    @staticmethod
    def minTransfers(transactions):
        # 加工出来的debt数组中一定不含有0
        debt = Code02_OptimalAccountBalancing.debts(transactions)
        n = jcast('int', jget(debt, 'length'))
        dp = jarray('int', [jcast('int', (1 << (n & 31)))])
        jstatic('Arrays', 'fill', dp, jcast('int', (-1)))
        return jcast('int', jcast('int', (n - Code02_OptimalAccountBalancing.f(debt, jcast('int', (jcast('int', (1 << (n & 31))) - 1)), 0, n, dp))))

    @staticmethod
    def debts(transactions):
        help = jarray('int', [Code02_OptimalAccountBalancing.MAXN])
        for tran in transactions:
            ((_java_obj_1 := help), (_java_key_2 := tran[0]), jset(_java_obj_1, _java_key_2, jcast('int', (jget(_java_obj_1, _java_key_2) - tran[2]))))[2]
            ((_java_obj_3 := help), (_java_key_4 := tran[1]), jset(_java_obj_3, _java_key_4, jcast('int', jadd(jget(_java_obj_3, _java_key_4), tran[2]))))[2]
        n = jcast('int', 0)
        for num in help:
            if (num != 0):
                n = jcast('int', (n + 1))
        debt = jarray('int', [n])
        index = jcast('int', 0)
        for num in help:
            if (num != 0):
                jset(debt, ((_java_old_5 := index), (index := jcast('int', (index + (1)))), _java_old_5)[2], num)
        return debt

    @staticmethod
    def f(debt, set, sum, n, dp):
        set = jcast('int', set)
        sum = jcast('int', sum)
        n = jcast('int', n)
        if (dp[set] != jcast('int', (-1))):
            return jcast('int', dp[set])
        ans = jcast('int', 0)
        # 集合中不只一个元素
        if (jcast('int', (set & jcast('int', (set - 1)))) != 0):
            if (sum == 0):
                i = jcast('int', 0)
                while (i < n):
                    try:
                        if (jcast('int', (set & jcast('int', (1 << (i & 31))))) != 0):
                            # 找到任何一个元素，去除这个元素
                            # 剩下的集合进行尝试，返回值 + 1
                            ans = jcast('int', jcast('int', jadd(Code02_OptimalAccountBalancing.f(debt, jcast('int', (set ^ jcast('int', (1 << (i & 31))))), jcast('int', (sum - debt[i])), n, dp), 1)))
                            # 然后不需要再尝试下一个元素了，因为答案一定是一样的
                            # 所以直接break
                            raise JBreak(None)
                    except JContinue as _java_control_6:
                        if _java_control_6.label not in (None,):
                            raise
                    except JBreak as _java_control_6:
                        if _java_control_6.label not in (None,):
                            raise
                        break
                    i = jcast('int', (i + 1))
            else:
                i = jcast('int', 0)
                while (i < n):
                    if (jcast('int', (set & jcast('int', (1 << (i & 31))))) != 0):
                        ans = jcast('int', jstatic('Math', 'max', ans, Code02_OptimalAccountBalancing.f(debt, jcast('int', (set ^ jcast('int', (1 << (i & 31))))), jcast('int', (sum - debt[i])), n, dp)))
                    i = jcast('int', (i + 1))
        dp[set] = jcast('int', ans)
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_OptimalAccountBalancing.MAXN = jcast('int', 13)
