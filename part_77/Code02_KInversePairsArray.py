# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# K个逆序对数组
# 逆序对的定义如下：
# 对于数组nums的第i个和第j个元素
# 如果满足0<=i<j<nums.length 且 nums[i]>nums[j]，则为一个逆序对
# 给你两个整数n和k，找出所有包含从1到n的数字
# 且恰好拥有k个逆序对的不同的数组的个数
# 由于答案可能很大，答案对 1000000007 取模
# 测试链接 : https://leetcode.cn/problems/k-inverse-pairs-array/
class Code02_KInversePairsArray:
    __java_fields__ = {}
    # 最普通的动态规划
    # 不优化枚举
    @staticmethod
    def kInversePairs1(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        mod = jcast('int', 1000000007)
        # dp[i][j] : 1、2、3...i这些数字，形成的排列一定要有j个逆序对，请问这样的排列有几种
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(k, 1))])
        jset(dp[0], 0, 1)
        i = jcast('int', 1)
        while (i <= n):
            jset(dp[i], 0, 1)
            j = jcast('int', 1)
            while (j <= k):
                if (i > j):
                    p = jcast('int', 0)
                    while (p <= j):
                        jset(dp[i], j, jcast('int', jmod(jcast('int', jadd(dp[i][j], dp[jcast('int', (i - 1))][p])), mod)))
                        p = jcast('int', (p + 1))
                else:
                    # i <= j
                    p = jcast('int', jcast('int', jadd(jcast('int', (j - i)), 1)))
                    while (p <= j):
                        jset(dp[i], j, jcast('int', jmod(jcast('int', jadd(dp[i][j], dp[jcast('int', (i - 1))][p])), mod)))
                        p = jcast('int', (p + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[n][k])

    # 根据观察方法1优化枚举
    # 最优解
    # 其实可以进一步空间压缩
    # 有兴趣的同学自己试试吧
    @staticmethod
    def kInversePairs2(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        mod = jcast('int', 1000000007)
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(k, 1))])
        jset(dp[0], 0, 1)
        # window : 窗口的累加和
        i = jcast('int', 1)
        window = 0
        while (i <= n):
            jset(dp[i], 0, 1)
            window = jcast('int', 1)
            j = jcast('int', 1)
            while (j <= k):
                if (i > j):
                    window = jcast('int', jcast('int', jmod(jcast('int', jadd(window, dp[jcast('int', (i - 1))][j])), mod)))
                else:
                    # i <= j
                    window = jcast('int', jcast('int', jmod(jcast('int', jadd(jcast('int', (jcast('int', jmod(jcast('int', jadd(window, dp[jcast('int', (i - 1))][j])), mod)) - dp[jcast('int', (i - 1))][jcast('int', (j - i))])), mod)), mod)))
                jset(dp[i], j, window)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[n][k])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


