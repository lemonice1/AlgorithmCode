# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 子序列累加和必须被7整除的最大累加和
# 给定一个非负数组nums，
# 可以任意选择数字组成子序列，但是子序列的累加和必须被7整除
# 返回最大累加和
# 对数器验证
class Code02_MaxSumDividedBy7:
    __java_fields__ = {}
    # 暴力方法
    # 为了验证
    @staticmethod
    def maxSum1(nums):
        # nums形成的所有子序列的累加和都求出来
        # 其中%7==0的那些累加和中，返回最大的
        # 就是如下f函数的功能
        return jcast('int', Code02_MaxSumDividedBy7.f(nums, 0, 0))

    @staticmethod
    def f(nums, i, s):
        i = jcast('int', i)
        s = jcast('int', s)
        if (i == jget(nums, 'length')):
            return jcast('int', (s if (jcast('int', jmod(s, 7)) == 0) else 0))
        return jcast('int', jstatic('Math', 'max', Code02_MaxSumDividedBy7.f(nums, jcast('int', jadd(i, 1)), s), Code02_MaxSumDividedBy7.f(nums, jcast('int', jadd(i, 1)), jcast('int', jadd(s, nums[i])))))

    # 正式方法
    # 时间复杂度O(n)
    @staticmethod
    def maxSum2(nums):
        n = jcast('int', jget(nums, 'length'))
        # dp[i][j] : nums[0...i-1]
        # nums前i个数形成的子序列一定要做到，子序列累加和%7 == j
        # 这样的子序列最大累加和是多少
        # 注意 : dp[i][j] == -1代表不存在这样的子序列
        dp = jarray('int', [jcast('int', jadd(n, 1)), 7])
        jset(dp[0], 0, 0)
        j = jcast('int', 1)
        while (j < 7):
            jset(dp[0], j, jcast('int', (-1)))
            j = jcast('int', (j + 1))
        i = jcast('int', 1)
        x = 0
        cur = 0
        need = 0
        while (i <= n):
            x = jcast('int', nums[jcast('int', (i - 1))])
            cur = jcast('int', jcast('int', jmod(nums[jcast('int', (i - 1))], 7)))
            j = jcast('int', 0)
            while (j < 7):
                jset(dp[i], j, dp[jcast('int', (i - 1))][j])
                # 这里求need是核心
                need = jcast('int', (jcast('int', (j - cur)) if (cur <= j) else jcast('int', jadd(jcast('int', (j - cur)), 7))))
                # 或者如下这种写法也对
                # need = (7 + j - cur) % 7;
                if (dp[jcast('int', (i - 1))][need] != jcast('int', (-1))):
                    jset(dp[i], j, jstatic('Math', 'max', dp[i][j], jcast('int', jadd(dp[jcast('int', (i - 1))][need], x))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[n][0])

    # 为了测试
    # 生成随机数组
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        ans = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            jset(ans, i, jcast('int', (jstatic('Math', 'random') * v)))
            i = jcast('int', (i + 1))
        return ans

    # 为了测试
    # 对数器
    @staticmethod
    def main(args):
        n = jcast('int', 15)
        v = jcast('int', 30)
        testTime = jcast('int', 20000)
        jprint('测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTime):
            len = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            nums = Code02_MaxSumDividedBy7.randomArray(len, v)
            ans1 = jcast('int', Code02_MaxSumDividedBy7.maxSum1(nums))
            ans2 = jcast('int', Code02_MaxSumDividedBy7.maxSum2(nums))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code02_MaxSumDividedBy7.main([])
