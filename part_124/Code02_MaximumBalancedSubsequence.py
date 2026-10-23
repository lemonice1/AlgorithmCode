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

# 平衡子序列的最大和
# 给定一个长度为n的数组nums，下面定义平衡子序列
# 如果下标i和下标j被选进了子序列，i在j的左边
# 那么必须有nums[j] - nums[i] >= j - i
# 如果一个子序列中任意的两个下标都满足上面的要求，那子序列就是平衡的
# 返回nums所有平衡子序列里，最大的累加和是多少
# 1 <= n <= 10^5
# -10^9 <= nums[i] <= +10^9
# 测试链接 : https://leetcode.cn/problems/maximum-balanced-subsequence-sum/
class Code02_MaximumBalancedSubsequence:
    __java_fields__ = {'MAXN': 'MAXN', 'sort': 'sort', 'tree': 'tree', 'n': 'n', 'm': 'm'}
    @staticmethod
    def maxBalancedSubsequenceSum(nums):
        Code02_MaximumBalancedSubsequence.build(nums)
        pre = 0
        i = jcast('int', 0)
        k = 0
        while (i < Code02_MaximumBalancedSubsequence.n):
            # k的含义为当前的指标是第几号指标
            k = jcast('int', Code02_MaximumBalancedSubsequence.rank(jcast('int', (nums[i] - i))))
            # dp[1号..k号指标]中的最大值是多少
            pre = jcast('long', Code02_MaximumBalancedSubsequence.max(k))
            if (pre < 0):
                # 如果之前的最好情况是负数，那么不要之前的数了
                # 当前数字自己单独形成平衡子序列
                # 去更新dp[k号指标]，看能不能变得更大
                Code02_MaximumBalancedSubsequence.update(k, nums[i])
            else:
                # 如果之前的最好情况不是负数，那么和当前数字一起形成更大的累加和
                # 去更新dp[k号指标]，看能不能变得更大
                Code02_MaximumBalancedSubsequence.update(k, jcast('long', jadd(pre, nums[i])))
            i = jcast('int', (i + 1))
        # 返回dp[1号..m号指标]中的最大值
        return jcast('long', Code02_MaximumBalancedSubsequence.max(Code02_MaximumBalancedSubsequence.m))

    MAXN = 0
    sort = None
    tree = None
    n = 0
    m = 0
    @staticmethod
    def build(nums):
        Code02_MaximumBalancedSubsequence.n = jcast('int', jget(nums, 'length'))
        i = jcast('int', 1)
        j = jcast('int', 0)
        while (i <= Code02_MaximumBalancedSubsequence.n):
            Code02_MaximumBalancedSubsequence.sort[i] = jcast('int', jcast('int', (nums[j] - j)))
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        jstatic('Arrays', 'sort', Code02_MaximumBalancedSubsequence.sort, 1, jcast('int', jadd(Code02_MaximumBalancedSubsequence.n, 1)))
        Code02_MaximumBalancedSubsequence.m = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code02_MaximumBalancedSubsequence.n):
            if (Code02_MaximumBalancedSubsequence.sort[Code02_MaximumBalancedSubsequence.m] != Code02_MaximumBalancedSubsequence.sort[i]):
                jset(Code02_MaximumBalancedSubsequence.sort, ((_java_obj_1 := Code02_MaximumBalancedSubsequence), (_java_key_2 := 'm'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_MaximumBalancedSubsequence.sort[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'fill', Code02_MaximumBalancedSubsequence.tree, 1, jcast('int', jadd(Code02_MaximumBalancedSubsequence.m, 1)), jget(Long, 'MIN_VALUE'))

    # 当前的指标值是v，返回这是第几号指标
    @staticmethod
    def rank(v):
        v = jcast('int', v)
        left = jcast('int', 1)
        right = jcast('int', Code02_MaximumBalancedSubsequence.m)
        mid = 0
        ans = jcast('int', 0)
        while (left <= right):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(left, right)), 2)))
            if (Code02_MaximumBalancedSubsequence.sort[mid] <= v):
                ans = jcast('int', mid)
                left = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ans)

    # dp[i号指标]，当前算出的值是v
    @staticmethod
    def update(i, v):
        i = jcast('int', i)
        v = jcast('long', v)
        while (i <= Code02_MaximumBalancedSubsequence.m):
            jset(Code02_MaximumBalancedSubsequence.tree, i, jstatic('Math', 'max', Code02_MaximumBalancedSubsequence.tree[i], v))
            i = jcast('int', jcast('int', jadd(i, jcast('int', (i & jcast('int', (-i)))))))

    # dp[1..i]，最大值多少返回
    @staticmethod
    def max(i):
        i = jcast('int', i)
        ans = jcast('long', jget(Long, 'MIN_VALUE'))
        while (i > 0):
            ans = jcast('long', jstatic('Math', 'max', ans, Code02_MaximumBalancedSubsequence.tree[i]))
            i = jcast('int', jcast('int', (i - jcast('int', (i & jcast('int', (-i)))))))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_MaximumBalancedSubsequence.MAXN = jcast('int', 100001)
Code02_MaximumBalancedSubsequence.sort = jarray('int', [Code02_MaximumBalancedSubsequence.MAXN])
Code02_MaximumBalancedSubsequence.tree = jarray('long', [Code02_MaximumBalancedSubsequence.MAXN])
Code02_MaximumBalancedSubsequence.n = jcast('int', 0)
Code02_MaximumBalancedSubsequence.m = jcast('int', 0)
