# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 魔法卷轴
# 给定一个数组nums，其中可能有正、负、0
# 每个魔法卷轴可以把nums中连续的一段全变成0
# 你希望数组整体的累加和尽可能大
# 卷轴使不使用、使用多少随意，但一共只有2个魔法卷轴
# 请返回数组尽可能大的累加和
# 对数器验证
class Code03_MagicScrollProbelm:
    __java_fields__ = {}
    # 暴力方法
    # 为了测试
    @staticmethod
    def maxSum1(nums):
        p1 = jcast('int', 0)
        for num in nums:
            p1 = jcast('int', jcast('int', jadd(p1, num)))
        n = jcast('int', jget(nums, 'length'))
        p2 = jcast('int', Code03_MagicScrollProbelm.mustOneScroll(nums, 0, jcast('int', (n - 1))))
        p3 = jcast('int', jget(Integer, 'MIN_VALUE'))
        i = jcast('int', 1)
        while (i < n):
            p3 = jcast('int', jstatic('Math', 'max', p3, jcast('int', jadd(Code03_MagicScrollProbelm.mustOneScroll(nums, 0, jcast('int', (i - 1))), Code03_MagicScrollProbelm.mustOneScroll(nums, i, jcast('int', (n - 1)))))))
            i = jcast('int', (i + 1))
        return jcast('int', jstatic('Math', 'max', p1, jstatic('Math', 'max', p2, p3)))

    # 暴力方法
    # 为了测试
    # nums[l...r]范围上一定要用一次卷轴情况下的最大累加和
    @staticmethod
    def mustOneScroll(nums, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        # l...r范围上包含a...b范围
        # 如果a...b范围上的数字都变成0
        # 返回剩下数字的累加和
        # 所以枚举所有可能的a...b范围
        # 相当暴力，但是正确
        a = jcast('int', l)
        while (a <= r):
            b = jcast('int', a)
            while (b <= r):
                # l...a...b...r
                curAns = jcast('int', 0)
                i = jcast('int', l)
                while (i < a):
                    curAns = jcast('int', jcast('int', jadd(curAns, nums[i])))
                    i = jcast('int', (i + 1))
                i = jcast('int', jcast('int', jadd(b, 1)))
                while (i <= r):
                    curAns = jcast('int', jcast('int', jadd(curAns, nums[i])))
                    i = jcast('int', (i + 1))
                ans = jcast('int', jstatic('Math', 'max', ans, curAns))
                b = jcast('int', (b + 1))
            a = jcast('int', (a + 1))
        return jcast('int', ans)

    # 正式方法
    # 时间复杂度O(n)
    @staticmethod
    def maxSum2(nums):
        n = jcast('int', jget(nums, 'length'))
        if (n == 0):
            return jcast('int', 0)
        # 情况1 : 完全不使用卷轴
        p1 = jcast('int', 0)
        for num in nums:
            p1 = jcast('int', jcast('int', jadd(p1, num)))
        # prefix[i] : 0~i范围上一定要用1次卷轴的情况下，0~i范围上整体最大累加和多少
        prefix = jarray('int', [n])
        # 每一步的前缀和
        sum = jcast('int', nums[0])
        # maxPresum : 之前所有前缀和的最大值
        maxPresum = jcast('int', jstatic('Math', 'max', 0, nums[0]))
        i = jcast('int', 1)
        while (i < n):
            jset(prefix, i, jstatic('Math', 'max', jcast('int', jadd(prefix[jcast('int', (i - 1))], nums[i])), maxPresum))
            sum = jcast('int', jcast('int', jadd(sum, nums[i])))
            maxPresum = jcast('int', jstatic('Math', 'max', maxPresum, sum))
            i = jcast('int', (i + 1))
        # 情况二 : 必须用1次卷轴
        p2 = jcast('int', prefix[jcast('int', (n - 1))])
        # suffix[i] : i~n-1范围上一定要用1次卷轴的情况下，i~n-1范围上整体最大累加和多少
        suffix = jarray('int', [n])
        sum = jcast('int', nums[jcast('int', (n - 1))])
        maxPresum = jcast('int', jstatic('Math', 'max', 0, sum))
        i = jcast('int', jcast('int', (n - 2)))
        while (i >= 0):
            jset(suffix, i, jstatic('Math', 'max', jcast('int', jadd(nums[i], suffix[jcast('int', jadd(i, 1))])), maxPresum))
            sum = jcast('int', jcast('int', jadd(sum, nums[i])))
            maxPresum = jcast('int', jstatic('Math', 'max', maxPresum, sum))
            i = jcast('int', (i - 1))
        # 情况二 : 必须用2次卷轴
        p3 = jcast('int', jget(Integer, 'MIN_VALUE'))
        i = jcast('int', 1)
        while (i < n):
            # 枚举所有的划分点i
            # 0~i-1 左
            # i~n-1 右
            p3 = jcast('int', jstatic('Math', 'max', p3, jcast('int', jadd(prefix[jcast('int', (i - 1))], suffix[i]))))
            i = jcast('int', (i + 1))
        return jcast('int', jstatic('Math', 'max', p1, jstatic('Math', 'max', p2, p3)))

    # 为了测试
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        ans = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            jset(ans, i, jcast('int', (jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (v * 2)), 1)))) - v)))
            i = jcast('int', (i + 1))
        return ans

    # 为了测试
    @staticmethod
    def main(args):
        n = jcast('int', 50)
        v = jcast('int', 100)
        testTime = jcast('int', 10000)
        jprint('测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTime):
            len = jcast('int', jcast('int', (jstatic('Math', 'random') * n)))
            nums = Code03_MagicScrollProbelm.randomArray(len, v)
            ans1 = jcast('int', Code03_MagicScrollProbelm.maxSum1(nums))
            ans2 = jcast('int', Code03_MagicScrollProbelm.maxSum2(nums))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code03_MagicScrollProbelm.main([])
