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

# 戳气球
# 有 n 个气球，编号为0到n-1，每个气球上都标有一个数字，这些数字存在数组nums中
# 现在要求你戳破所有的气球。戳破第 i 个气球
# 你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币
# 这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号
# 如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球
# 求所能获得硬币的最大数量
# 测试链接 : https://leetcode.cn/problems/burst-balloons/
class Code05_BurstBalloons:
    __java_fields__ = {}
    # 记忆化搜索
    @staticmethod
    def maxCoins1(nums):
        n = jcast('int', jget(nums, 'length'))
        # a b c d e
        # 1 a b c d e 1
        arr = jarray('int', [jcast('int', jadd(n, 2))])
        arr[0] = jcast('int', 1)
        arr[jcast('int', jadd(n, 1))] = jcast('int', 1)
        i = jcast('int', 0)
        while (i < n):
            arr[jcast('int', jadd(i, 1))] = jcast('int', nums[i])
            i = jcast('int', (i + 1))
        dp = jarray('int', [jcast('int', jadd(n, 2)), jcast('int', jadd(n, 2))])
        i = jcast('int', 1)
        while (i <= n):
            j = jcast('int', i)
            while (j <= n):
                jset(dp[i], j, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code05_BurstBalloons.f(arr, 1, n, dp))

    # arr[l...r]这些气球决定一个顺序，获得最大得分返回！
    # 一定有 : arr[l-1]一定没爆！
    # 一定有 : arr[r+1]一定没爆！
    # 尝试每个气球最后打爆
    @staticmethod
    def f(arr, l, r, dp):
        l = jcast('int', l)
        r = jcast('int', r)
        if (dp[l][r] != jcast('int', (-1))):
            return jcast('int', dp[l][r])
        ans = 0
        if (l == r):
            ans = jcast('int', jcast('int', (jcast('int', (arr[jcast('int', (l - 1))] * arr[l])) * arr[jcast('int', jadd(r, 1))])))
        else:
            # l   ....r
            # l +1 +2 .. r
            ans = jcast('int', jstatic('Math', 'max', jcast('int', jadd(jcast('int', (jcast('int', (arr[jcast('int', (l - 1))] * arr[l])) * arr[jcast('int', jadd(r, 1))])), Code05_BurstBalloons.f(arr, jcast('int', jadd(l, 1)), r, dp))), jcast('int', jadd(jcast('int', (jcast('int', (arr[jcast('int', (l - 1))] * arr[r])) * arr[jcast('int', jadd(r, 1))])), Code05_BurstBalloons.f(arr, l, jcast('int', (r - 1)), dp)))))
            # l位置的气球最后打爆
            # r位置的气球最后打爆
            k = jcast('int', jcast('int', jadd(l, 1)))
            while (k < r):
                # k位置的气球最后打爆
                # l...k-1  k  k+1...r
                ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(jcast('int', jadd(jcast('int', (jcast('int', (arr[jcast('int', (l - 1))] * arr[k])) * arr[jcast('int', jadd(r, 1))])), Code05_BurstBalloons.f(arr, l, jcast('int', (k - 1)), dp))), Code05_BurstBalloons.f(arr, jcast('int', jadd(k, 1)), r, dp)))))
                k = jcast('int', (k + 1))
        jset(dp[l], r, ans)
        return jcast('int', ans)

    # 严格位置依赖的动态规划
    @staticmethod
    def maxCoins2(nums):
        n = jcast('int', jget(nums, 'length'))
        arr = jarray('int', [jcast('int', jadd(n, 2))])
        arr[0] = jcast('int', 1)
        arr[jcast('int', jadd(n, 1))] = jcast('int', 1)
        i = jcast('int', 0)
        while (i < n):
            arr[jcast('int', jadd(i, 1))] = jcast('int', nums[i])
            i = jcast('int', (i + 1))
        dp = jarray('int', [jcast('int', jadd(n, 2)), jcast('int', jadd(n, 2))])
        i = jcast('int', 1)
        while (i <= n):
            jset(dp[i], i, jcast('int', (jcast('int', (arr[jcast('int', (i - 1))] * arr[i])) * arr[jcast('int', jadd(i, 1))])))
            i = jcast('int', (i + 1))
        l = jcast('int', n)
        ans = 0
        while (l >= 1):
            r = jcast('int', jcast('int', jadd(l, 1)))
            while (r <= n):
                ans = jcast('int', jstatic('Math', 'max', jcast('int', jadd(jcast('int', (jcast('int', (arr[jcast('int', (l - 1))] * arr[l])) * arr[jcast('int', jadd(r, 1))])), dp[jcast('int', jadd(l, 1))][r])), jcast('int', jadd(jcast('int', (jcast('int', (arr[jcast('int', (l - 1))] * arr[r])) * arr[jcast('int', jadd(r, 1))])), dp[l][jcast('int', (r - 1))]))))
                k = jcast('int', jcast('int', jadd(l, 1)))
                while (k < r):
                    ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(jcast('int', jadd(jcast('int', (jcast('int', (arr[jcast('int', (l - 1))] * arr[k])) * arr[jcast('int', jadd(r, 1))])), dp[l][jcast('int', (k - 1))])), dp[jcast('int', jadd(k, 1))][r]))))
                    k = jcast('int', (k + 1))
                jset(dp[l], r, ans)
                r = jcast('int', (r + 1))
            l = jcast('int', (l - 1))
        return jcast('int', dp[1][n])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


