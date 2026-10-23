# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 预测赢家
# 给你一个整数数组 nums 。玩家 1 和玩家 2 基于这个数组设计了一个游戏
# 玩家 1 和玩家 2 轮流进行自己的回合，玩家 1 先手
# 开始时，两个玩家的初始分值都是 0
# 每一回合，玩家从数组的任意一端取一个数字
# 取到的数字将会从数组中移除，数组长度减1
# 玩家选中的数字将会加到他的得分上
# 当数组中没有剩余数字可取时游戏结束
# 如果玩家 1 能成为赢家，返回 true
# 如果两个玩家得分相等，同样认为玩家 1 是游戏的赢家，也返回 true
# 你可以假设每个玩家的玩法都会使他的分数最大化
# 测试链接 : https://leetcode.cn/problems/predict-the-winner/
class Code02_PredictTheWinner:
    __java_fields__ = {}
    # 暴力尝试
    @staticmethod
    def predictTheWinner1(nums):
        sum = jcast('int', 0)
        for num in nums:
            sum = jcast('int', jcast('int', jadd(sum, num)))
        n = jcast('int', jget(nums, 'length'))
        first = jcast('int', Code02_PredictTheWinner.f1(nums, 0, jcast('int', (n - 1))))
        second = jcast('int', jcast('int', (sum - first)))
        return jcast('boolean', (first >= second))

    # nums[l...r]范围上的数字进行游戏，轮到玩家1
    # 返回玩家1最终能获得多少分数，玩家1和玩家2都绝顶聪明
    @staticmethod
    def f1(nums, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return jcast('int', nums[l])
        if (l == jcast('int', (r - 1))):
            return jcast('int', jstatic('Math', 'max', nums[l], nums[r]))
        # l....r 不只两个数
        # 可能性1 ：玩家1拿走nums[l] l+1...r
        p1 = jcast('int', jcast('int', jadd(nums[l], jstatic('Math', 'min', Code02_PredictTheWinner.f1(nums, jcast('int', jadd(l, 2)), r), Code02_PredictTheWinner.f1(nums, jcast('int', jadd(l, 1)), jcast('int', (r - 1)))))))
        # 可能性2 ：玩家1拿走nums[r] l...r-1
        p2 = jcast('int', jcast('int', jadd(nums[r], jstatic('Math', 'min', Code02_PredictTheWinner.f1(nums, jcast('int', jadd(l, 1)), jcast('int', (r - 1))), Code02_PredictTheWinner.f1(nums, l, jcast('int', (r - 2)))))))
        return jcast('int', jstatic('Math', 'max', p1, p2))

    # 记忆化搜索
    @staticmethod
    def predictTheWinner2(nums):
        sum = jcast('int', 0)
        for num in nums:
            sum = jcast('int', jcast('int', jadd(sum, num)))
        n = jcast('int', jget(nums, 'length'))
        dp = jarray('int', [n, n])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', i)
            while (j < n):
                jset(dp[i], j, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        first = jcast('int', Code02_PredictTheWinner.f2(nums, 0, jcast('int', (n - 1)), dp))
        second = jcast('int', jcast('int', (sum - first)))
        return jcast('boolean', (first >= second))

    @staticmethod
    def f2(nums, l, r, dp):
        l = jcast('int', l)
        r = jcast('int', r)
        if (dp[l][r] != jcast('int', (-1))):
            return jcast('int', dp[l][r])
        ans = 0
        if (l == r):
            ans = jcast('int', nums[l])
        else:
            if (l == jcast('int', (r - 1))):
                ans = jcast('int', jstatic('Math', 'max', nums[l], nums[r]))
            else:
                p1 = jcast('int', jcast('int', jadd(nums[l], jstatic('Math', 'min', Code02_PredictTheWinner.f2(nums, jcast('int', jadd(l, 2)), r, dp), Code02_PredictTheWinner.f2(nums, jcast('int', jadd(l, 1)), jcast('int', (r - 1)), dp)))))
                p2 = jcast('int', jcast('int', jadd(nums[r], jstatic('Math', 'min', Code02_PredictTheWinner.f2(nums, jcast('int', jadd(l, 1)), jcast('int', (r - 1)), dp), Code02_PredictTheWinner.f2(nums, l, jcast('int', (r - 2)), dp)))))
                ans = jcast('int', jstatic('Math', 'max', p1, p2))
        jset(dp[l], r, ans)
        return jcast('int', ans)

    # 严格位置依赖的动态规划
    @staticmethod
    def predictTheWinner3(nums):
        sum = jcast('int', 0)
        for num in nums:
            sum = jcast('int', jcast('int', jadd(sum, num)))
        n = jcast('int', jget(nums, 'length'))
        dp = jarray('int', [n, n])
        i = jcast('int', 0)
        while (i < jcast('int', (n - 1))):
            jset(dp[i], i, nums[i])
            jset(dp[i], jcast('int', jadd(i, 1)), jstatic('Math', 'max', nums[i], nums[jcast('int', jadd(i, 1))]))
            i = jcast('int', (i + 1))
        jset(dp[jcast('int', (n - 1))], jcast('int', (n - 1)), nums[jcast('int', (n - 1))])
        l = jcast('int', jcast('int', (n - 3)))
        while (l >= 0):
            r = jcast('int', jcast('int', jadd(l, 2)))
            while (r < n):
                jset(dp[l], r, jstatic('Math', 'max', jcast('int', jadd(nums[l], jstatic('Math', 'min', dp[jcast('int', jadd(l, 2))][r], dp[jcast('int', jadd(l, 1))][jcast('int', (r - 1))]))), jcast('int', jadd(nums[r], jstatic('Math', 'min', dp[jcast('int', jadd(l, 1))][jcast('int', (r - 1))], dp[l][jcast('int', (r - 2))])))))
                r = jcast('int', (r + 1))
            l = jcast('int', (l - 1))
        first = jcast('int', dp[0][jcast('int', (n - 1))])
        second = jcast('int', jcast('int', (sum - first)))
        return jcast('boolean', (first >= second))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


