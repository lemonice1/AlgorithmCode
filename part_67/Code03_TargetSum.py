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

# 目标和
# 给你一个非负整数数组 nums 和一个整数 target 。
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数
# 可以构造一个表达式
# 例如nums=[2, 1]，可以在2之前添加'+' ，在1之前添加'-'
# 然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的，运算结果等于 target 的不同表达式的数目
# 测试链接 : https://leetcode.cn/problems/target-sum/
class Code03_TargetSum:
    __java_fields__ = {}
    # 普通尝试，暴力递归版
    @staticmethod
    def findTargetSumWays1(nums, target):
        target = jcast('int', target)
        return jcast('int', Code03_TargetSum.f1(nums, target, 0, 0))

    # nums[0...i-1]范围上，已经形成的累加和是sum
    # nums[i...]范围上，每个数字可以标记+或者-
    # 最终形成累加和为target的不同表达式数目
    @staticmethod
    def f1(nums, target, i, sum):
        target = jcast('int', target)
        i = jcast('int', i)
        sum = jcast('int', sum)
        if (i == jget(nums, 'length')):
            return jcast('int', (1 if (sum == target) else 0))
        return jcast('int', jcast('int', jadd(Code03_TargetSum.f1(nums, target, jcast('int', jadd(i, 1)), jcast('int', jadd(sum, nums[i]))), Code03_TargetSum.f1(nums, target, jcast('int', jadd(i, 1)), jcast('int', (sum - nums[i]))))))

    # 普通尝试，记忆化搜索版
    @staticmethod
    def findTargetSumWays2(nums, target):
        target = jcast('int', target)
        # i, sum -> value（返回值 ）
        dp = jnew('HashMap')
        return jcast('int', Code03_TargetSum.f2(nums, target, 0, 0, dp))

    # 因为累加和可以为负数
    # 所以缓存动态规划表用哈希表
    @staticmethod
    def f2(nums, target, i, j, dp):
        target = jcast('int', target)
        i = jcast('int', i)
        j = jcast('int', j)
        if (i == jget(nums, 'length')):
            return jcast('int', (1 if (j == target) else 0))
        if (jcall(dp, 'containsKey', i) and jcall(jcall(dp, 'get', i), 'containsKey', j)):
            return jcast('int', jcall(jcall(dp, 'get', i), 'get', j))
        ans = jcast('int', jcast('int', jadd(Code03_TargetSum.f2(nums, target, jcast('int', jadd(i, 1)), jcast('int', jadd(j, nums[i])), dp), Code03_TargetSum.f2(nums, target, jcast('int', jadd(i, 1)), jcast('int', (j - nums[i])), dp))))
        jcall(dp, 'putIfAbsent', i, jnew('HashMap'))
        jcall(jcall(dp, 'get', i), 'put', j, ans)
        return jcast('int', ans)

    # 普通尝试
    # 严格位置依赖的动态规划
    # 平移技巧
    @staticmethod
    def findTargetSumWays3(nums, target):
        target = jcast('int', target)
        s = jcast('int', 0)
        for num in nums:
            s = jcast('int', jcast('int', jadd(s, num)))
        if ((target < jcast('int', (-s))) or (target > s)):
            return jcast('int', 0)
        n = jcast('int', jget(nums, 'length'))
        # -s ~ +s -> 2 * s + 1
        m = jcast('int', jcast('int', jadd(jcast('int', (2 * s)), 1)))
        # 原本的dp[i][j]含义:
        # nums[0...i-1]范围上，已经形成的累加和是sum
        # nums[i...]范围上，每个数字可以标记+或者-
        # 最终形成累加和为target的不同表达式数目
        # 因为sum可能为负数，为了下标不出现负数，
        # "原本的dp[i][j]"由dp表中的dp[i][j + s]来表示
        # 也就是平移操作！
        # 一切"原本的dp[i][j]"一律平移到dp表中的dp[i][j + s]
        dp = jarray('int', [jcast('int', jadd(n, 1)), m])
        # 原本的dp[n][target] = 1，平移！
        jset(dp[n], jcast('int', jadd(target, s)), 1)
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            j = jcast('int', jcast('int', (-s)))
            while (j <= s):
                if (jcast('int', jadd(jcast('int', jadd(j, nums[i])), s)) < m):
                    # 原本是 : dp[i][j] = dp[i + 1][j + nums[i]]
                    # 平移！
                    jset(dp[i], jcast('int', jadd(j, s)), dp[jcast('int', jadd(i, 1))][jcast('int', jadd(jcast('int', jadd(j, nums[i])), s))])
                if (jcast('int', jadd(jcast('int', (j - nums[i])), s)) >= 0):
                    # 原本是 : dp[i][j] += dp[i + 1][j - nums[i]]
                    # 平移！
                    ((_java_obj_1 := dp[i]), (_java_key_2 := jcast('int', jadd(j, s))), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), dp[jcast('int', jadd(i, 1))][jcast('int', jadd(jcast('int', (j - nums[i])), s))]))))[2]
                j = jcast('int', (j + 1))
            i = jcast('int', (i - 1))
        # 原本应该返回dp[0][0]
        # 平移！
        # 返回dp[0][0 + s]
        return jcast('int', dp[0][s])

    # 新思路，转化为01背包问题
    # 思考1:
    # 虽然题目说nums是非负数组，但即使nums中有负数比如[3,-4,2]
    # 因为能在每个数前面用+或者-号
    # 所以[3,-4,2]其实和[3,4,2]会达成一样的结果
    # 所以即使nums中有负数，也可以把负数直接变成正数，也不会影响结果
    # 思考2:
    # 如果nums都是非负数，并且所有数的累加和是sum
    # 那么如果target>sum，很明显没有任何方法可以达到target，可以直接返回0
    # 思考3:
    # nums内部的数组，不管怎么+和-，最终的结果都一定不会改变奇偶性
    # 所以，如果所有数的累加和是sum，并且与target的奇偶性不一样
    # 那么没有任何方法可以达到target，可以直接返回0
    # 思考4(最重要):
    # 比如说给定一个数组, nums = [1, 2, 3, 4, 5] 并且 target = 3
    # 其中一个方案是 : +1 -2 +3 -4 +5 = 3
    # 该方案中取了正的集合为A = {1，3，5}
    # 该方案中取了负的集合为B = {2，4}
    # 所以任何一种方案，都一定有 sum(A) - sum(B) = target
    # 现在我们来处理一下这个等式，把左右两边都加上sum(A) + sum(B)，那么就会变成如下：
    # sum(A) - sum(B) + sum(A) + sum(B) = target + sum(A) + sum(B)
    # 2 * sum(A) = target + 数组所有数的累加和
    # sum(A) = (target + 数组所有数的累加和) / 2
    # 也就是说，任何一个集合，只要累加和是(target + 数组所有数的累加和) / 2
    # 那么就一定对应一种target的方式
    # 比如非负数组nums，target = 1, nums所有数累加和是11
    # 求有多少方法组成1，其实就是求，有多少种子集累加和达到6的方法，(1+11)/2=6
    # 因为，子集累加和6 - 另一半的子集累加和5 = 1(target)
    # 所以有多少个累加和为6的不同集合，就代表有多少个target==1的表达式数量
    # 至此已经转化为01背包问题了
    @staticmethod
    def findTargetSumWays4(nums, target):
        target = jcast('int', target)
        sum = jcast('int', 0)
        for n in nums:
            sum = jcast('int', jcast('int', jadd(sum, n)))
        if ((sum < target) or (jcast('int', (jcast('int', (target & 1)) ^ jcast('int', (sum & 1)))) == 1)):
            return jcast('int', 0)
        return jcast('int', Code03_TargetSum.subsets(nums, jcast('int', (jcast('int', jadd(target, sum)) >> (1 & 31)))))

    # 求非负数组nums有多少个子序列累加和是t
    # 01背包问题(子集累加和严格是t) + 空间压缩
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
    @staticmethod
    def subsets(nums, t):
        t = jcast('int', t)
        if (t < 0):
            return jcast('int', 0)
        dp = jarray('int', [jcast('int', jadd(t, 1))])
        dp[0] = jcast('int', 1)
        # i省略了
        for num in nums:
            j = jcast('int', t)
            while (j >= num):
                dp[j] = jcast('int', jcast('int', jadd(dp[j], dp[jcast('int', (j - num))])))
                j = jcast('int', (j - 1))
        return jcast('int', dp[t])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


