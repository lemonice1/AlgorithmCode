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

# 打家劫舍 IV
# 沿街有一排连续的房屋。每间房屋内都藏有一定的现金
# 现在有一位小偷计划从这些房屋中窃取现金
# 由于相邻的房屋装有相互连通的防盗系统，所以小偷不会窃取相邻的房屋
# 小偷的 窃取能力 定义为他在窃取过程中能从单间房屋中窃取的 最大金额
# 给你一个整数数组 nums 表示每间房屋存放的现金金额
# 第i间房屋中放有nums[i]的钱数
# 另给你一个整数k，表示小偷需要窃取至少 k 间房屋
# 返回小偷需要的最小窃取能力值
# 测试链接 : https://leetcode.cn/problems/house-robber-iv/
class Code05_HouseRobberIV:
    __java_fields__ = {}
    @staticmethod
    def minCapability(nums, k):
        k = jcast('int', k)
        n = jcast('int', jget(nums, 'length'))
        l = jcast('int', nums[0])
        r = jcast('int', nums[0])
        i = jcast('int', 1)
        while (i < n):
            l = jcast('int', jstatic('Math', 'min', l, nums[i]))
            r = jcast('int', jstatic('Math', 'max', r, nums[i]))
            i = jcast('int', (i + 1))
        # l....r
        m = 0
        ans = jcast('int', 0)
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code05_HouseRobberIV.mostRob1(nums, n, m) >= k):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    # 盗贼能力为ability时
    # 返回盗贼最多能窃取多少间房屋
    # 注意限制 : 不能窃取相邻房屋
    @staticmethod
    def mostRob1(nums, n, ability):
        n = jcast('int', n)
        ability = jcast('int', ability)
        if (n == 1):
            return jcast('int', (1 if (nums[0] <= ability) else 0))
        if (n == 2):
            return jcast('int', (1 if ((nums[0] <= ability) or (nums[1] <= ability)) else 0))
        dp = jarray('int', [n])
        dp[0] = jcast('int', (1 if (nums[0] <= ability) else 0))
        dp[1] = jcast('int', (1 if ((nums[0] <= ability) or (nums[1] <= ability)) else 0))
        i = jcast('int', 2)
        while (i < n):
            jset(dp, i, jstatic('Math', 'max', dp[jcast('int', (i - 1))], jcast('int', jadd((1 if (nums[i] <= ability) else 0), dp[jcast('int', (i - 2))]))))
            i = jcast('int', (i + 1))
        return jcast('int', dp[jcast('int', (n - 1))])

    # 继续空间压缩优化
    @staticmethod
    def mostRob2(nums, n, ability):
        n = jcast('int', n)
        ability = jcast('int', ability)
        if (n == 1):
            return jcast('int', (1 if (nums[0] <= ability) else 0))
        if (n == 2):
            return jcast('int', (1 if ((nums[0] <= ability) or (nums[1] <= ability)) else 0))
        prepre = jcast('int', (1 if (nums[0] <= ability) else 0))
        pre = jcast('int', (1 if ((nums[0] <= ability) or (nums[1] <= ability)) else 0))
        i = jcast('int', 2)
        cur = 0
        while (i < n):
            cur = jcast('int', jstatic('Math', 'max', pre, jcast('int', jadd((1 if (nums[i] <= ability) else 0), prepre))))
            prepre = jcast('int', pre)
            pre = jcast('int', cur)
            i = jcast('int', (i + 1))
        return jcast('int', pre)

    # 继续贪心优化
    @staticmethod
    def mostRob3(nums, n, ability):
        n = jcast('int', n)
        ability = jcast('int', ability)
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            if (nums[i] <= ability):
                ans = jcast('int', (ans + 1))
                i = jcast('int', (i + 1))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


