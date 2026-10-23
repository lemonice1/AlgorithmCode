# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 非负数组前k个最小的子序列累加和
# 给定一个数组nums，含有n个数字，都是非负数
# 给定一个正数k，返回所有子序列中累加和最小的前k个累加和
# 子序列是包含空集的
# 1 <= n <= 10^5
# 1 <= nums[i] <= 10^6
# 1 <= k <= 10^5
# 注意这个数据量，用01背包的解法是不行的，时间复杂度太高了
# 对数器验证
class Code06_TopKMinimumSubsequenceSum:
    __java_fields__ = {}
    # 暴力方法
    # 为了验证
    @staticmethod
    def topKSum1(nums, k):
        k = jcast('int', k)
        allSubsequences = jnew('ArrayList')
        Code06_TopKMinimumSubsequenceSum.f1(nums, 0, 0, allSubsequences)
        jcall(allSubsequences, 'sort', (lambda a, b: jcall(a, 'compareTo', b)))
        ans = jarray('int', [k])
        i = jcast('int', 0)
        while (i < k):
            jset(ans, i, jcall(allSubsequences, 'get', i))
            i = jcast('int', (i + 1))
        return ans

    # 暴力方法
    # 得到所有子序列的和
    @staticmethod
    def f1(nums, index, sum, ans):
        index = jcast('int', index)
        sum = jcast('int', sum)
        if (index == jget(nums, 'length')):
            jcall(ans, 'add', sum)
        else:
            Code06_TopKMinimumSubsequenceSum.f1(nums, jcast('int', jadd(index, 1)), sum, ans)
            Code06_TopKMinimumSubsequenceSum.f1(nums, jcast('int', jadd(index, 1)), jcast('int', jadd(sum, nums[index])), ans)

    # 01背包来实现
    # 这种方法此时不是最优解
    # 因为n很大，数值也很大，那么可能的累加和就更大
    # 时间复杂度太差
    @staticmethod
    def topKSum2(nums, k):
        k = jcast('int', k)
        sum = jcast('int', 0)
        for num in nums:
            sum = jcast('int', jcast('int', jadd(sum, num)))
        # dp[i][j]
        # 1) dp[i-1][j]
        # 2) dp[i-1][j-nums[i]
        dp = jarray('int', [jcast('int', jadd(sum, 1))])
        dp[0] = jcast('int', 1)
        for num in nums:
            j = jcast('int', sum)
            while (j >= num):
                dp[j] = jcast('int', jcast('int', jadd(dp[j], dp[jcast('int', (j - num))])))
                j = jcast('int', (j - 1))
        ans = jarray('int', [k])
        index = jcast('int', 0)
        j = jcast('int', 0)
        while ((j <= sum) and (index < k)):
            i = jcast('int', 0)
            while ((i < dp[j]) and (index < k)):
                jset(ans, ((_java_old_1 := index), (index := jcast('int', (index + (1)))), _java_old_1)[2], j)
                i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        return ans

    # 正式方法
    # 用堆来做是最优解，时间复杂度O(n * log n) + O(k * log k)
    @staticmethod
    def topKSum3(nums, k):
        k = jcast('int', k)
        jstatic('Arrays', 'sort', nums)
        # (子序列的最右下标，子序列的累加和)
        heap = jnew('PriorityQueue', (lambda a, b: (a[1] - b[1])))
        jcall(heap, 'add', jarray('int', [None], [0, nums[0]]))
        ans = jarray('int', [k])
        i = jcast('int', 1)
        while (i < k):
            cur = jcall(heap, 'poll')
            right = jcast('int', cur[0])
            sum = jcast('int', cur[1])
            ans[i] = jcast('int', sum)
            if (jcast('int', jadd(right, 1)) < jget(nums, 'length')):
                jcall(heap, 'add', jarray('int', [None], [jcast('int', jadd(right, 1)), jcast('int', jadd(jcast('int', (sum - nums[right])), nums[jcast('int', jadd(right, 1))]))]))
                jcall(heap, 'add', jarray('int', [None], [jcast('int', jadd(right, 1)), jcast('int', jadd(sum, nums[jcast('int', jadd(right, 1))]))]))
            i = jcast('int', (i + 1))
        return ans

    # 为了测试
    @staticmethod
    def randomArray(len, value):
        len = jcast('int', len)
        value = jcast('int', value)
        ans = jarray('int', [len])
        i = jcast('int', 0)
        while (i < len):
            jset(ans, i, jcast('int', (jstatic('Math', 'random') * value)))
            i = jcast('int', (i + 1))
        return ans

    # 为了测试
    @staticmethod
    def equals(ans1, ans2):
        if (jget(ans1, 'length') != jget(ans2, 'length')):
            return jcast('boolean', False)
        i = jcast('int', 0)
        while (i < jget(ans1, 'length')):
            if (ans1[i] != ans2[i]):
                return jcast('boolean', False)
            i = jcast('int', (i + 1))
        return jcast('boolean', True)

    # 为了测试
    # 对数器
    @staticmethod
    def main(args):
        n = jcast('int', 15)
        v = jcast('int', 40)
        testTime = jcast('int', 5000)
        jprint('测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTime):
            len = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            nums = Code06_TopKMinimumSubsequenceSum.randomArray(len, v)
            k = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * jcast('int', (jcast('int', (1 << (len & 31))) - 1)))), 1)))
            ans1 = Code06_TopKMinimumSubsequenceSum.topKSum1(nums, k)
            ans2 = Code06_TopKMinimumSubsequenceSum.topKSum2(nums, k)
            ans3 = Code06_TopKMinimumSubsequenceSum.topKSum3(nums, k)
            if ((not Code06_TopKMinimumSubsequenceSum.equals(ans1, ans2)) or (not Code06_TopKMinimumSubsequenceSum.equals(ans1, ans3))):
                jprint('出错了！', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code06_TopKMinimumSubsequenceSum.main([])
