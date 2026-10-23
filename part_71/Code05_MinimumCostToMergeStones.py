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

# 合并石头的最低成本
# 有 n 堆石头排成一排，第 i 堆中有 stones[i] 块石头
# 每次 移动 需要将 连续的 k 堆石头合并为一堆，而这次移动的成本为这 k 堆中石头的总数
# 返回把所有石头合并成一堆的最低成本
# 如果无法合并成一堆返回-1
# 测试链接 : https://leetcode.cn/problems/minimum-cost-to-merge-stones/
class Code05_MinimumCostToMergeStones:
    __java_fields__ = {}
    # 时间复杂度O(n^3)
    # 优化策略来自于观察
    # l.....r最终会变成几份其实是注定的，根本就无法改变
    # 那么也就知道，满足(n - 1) % (k - 1) == 0的情况下，
    # 0....n-1最终一定是1份，也无法改变
    # 如果l.....r最终一定是1份
    # 那么要保证l.....m最终一定是1份，m+1...r最终一定是k-1份
    # 如果l.....r最终一定是p份（p>1）
    # 那么要保证l.....m最终一定是1份，那么m+1...r最终一定是p-1份
    # 怎么保证的？枚举行为中，m += k-1很重要！
    # m每次跳k-1！
    # 如果l.....r最终一定是1份
    # 就一定能保证l.....m最终一定是1份
    # 也一定能保证m+1...r最终一定是k-1份
    # 不要忘了，加上最后合并成1份的代价
    # 如果l.....r最终一定是p份
    # 就一定能保证l.....m最终一定是1份
    # 也一定能保证m+1...r最终一定是p-1份
    # 不用加上最后合并成1份的代价
    @staticmethod
    def mergeStones(stones, k):
        k = jcast('int', k)
        n = jcast('int', jget(stones, 'length'))
        if (jcast('int', jmod(jcast('int', (n - 1)), jcast('int', (k - 1)))) != 0):
            return jcast('int', jcast('int', (-1)))
        presum = jarray('int', [jcast('int', jadd(n, 1))])
        # 多补了一个0位置，l...r累加和 : presum[r+1] - presum[l]
        i = jcast('int', 0)
        j = jcast('int', 1)
        sum = jcast('int', 0)
        while (i < n):
            sum = jcast('int', jcast('int', jadd(sum, stones[i])))
            presum[j] = jcast('int', sum)
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        # dp[l][r] : l...r范围上的石头，合并到不能再合并（份数是确定的），最小代价是多少
        dp = jarray('int', [n, n])
        l = jcast('int', jcast('int', (n - 2)))
        ans = 0
        while (l >= 0):
            r = jcast('int', jcast('int', jadd(l, 1)))
            while (r < n):
                ans = jcast('int', jget(Integer, 'MAX_VALUE'))
                m = jcast('int', l)
                while (m < r):
                    ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(dp[l][m], dp[jcast('int', jadd(m, 1))][r]))))
                    m = jcast('int', jcast('int', jadd(m, jcast('int', (k - 1)))))
                if (jcast('int', jmod(jcast('int', (r - l)), jcast('int', (k - 1)))) == 0):
                    # 最终一定能划分成一份，那么就再加合并代价
                    ans = jcast('int', jcast('int', jadd(ans, jcast('int', (presum[jcast('int', jadd(r, 1))] - presum[l])))))
                jset(dp[l], r, ans)
                r = jcast('int', (r + 1))
            l = jcast('int', (l - 1))
        return jcast('int', dp[0][jcast('int', (n - 1))])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


