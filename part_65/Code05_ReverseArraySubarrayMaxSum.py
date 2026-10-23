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

# 可以翻转1次的情况下子数组最大累加和
# 给定一个数组nums，
# 现在允许你随意选择数组连续一段进行翻转，也就是子数组逆序的调整
# 比如翻转[1,2,3,4,5,6]的[2~4]范围，得到的是[1,2,5,4,3,6]
# 返回必须随意翻转1次之后，子数组的最大累加和
# 对数器验证
class Code05_ReverseArraySubarrayMaxSum:
    __java_fields__ = {}
    # 暴力方法
    # 为了验证
    @staticmethod
    def maxSumReverse1(nums):
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        l = jcast('int', 0)
        while (l < jget(nums, 'length')):
            r = jcast('int', l)
            while (r < jget(nums, 'length')):
                Code05_ReverseArraySubarrayMaxSum.reverse(nums, l, r)
                ans = jcast('int', jstatic('Math', 'max', ans, Code05_ReverseArraySubarrayMaxSum.maxSum(nums)))
                Code05_ReverseArraySubarrayMaxSum.reverse(nums, l, r)
                r = jcast('int', (r + 1))
            l = jcast('int', (l + 1))
        return jcast('int', ans)

    # nums[l...r]范围上的数字进行逆序调整
    @staticmethod
    def reverse(nums, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        while (l < r):
            tmp = jcast('int', nums[l])
            jset(nums, ((_java_old_1 := l), (l := jcast('int', (l + (1)))), _java_old_1)[2], nums[r])
            jset(nums, ((_java_old_2 := r), (r := jcast('int', (r + (-1)))), _java_old_2)[2], tmp)

    # 返回子数组最大累加和
    @staticmethod
    def maxSum(nums):
        n = jcast('int', jget(nums, 'length'))
        ans = jcast('int', nums[0])
        i = jcast('int', 1)
        pre = jcast('int', nums[0])
        while (i < n):
            pre = jcast('int', jstatic('Math', 'max', nums[i], jcast('int', jadd(pre, nums[i]))))
            ans = jcast('int', jstatic('Math', 'max', ans, pre))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 正式方法
    # 时间复杂度O(n)
    @staticmethod
    def maxSumReverse2(nums):
        n = jcast('int', jget(nums, 'length'))
        # start[i] : 所有必须以i开头的子数组中，最大累加和是多少
        start = jarray('int', [n])
        start[jcast('int', (n - 1))] = jcast('int', nums[jcast('int', (n - 1))])
        i = jcast('int', jcast('int', (n - 2)))
        while (i >= 0):
            # nums[i]
            # nums[i] + start[i+1]
            jset(start, i, jstatic('Math', 'max', nums[i], jcast('int', jadd(nums[i], start[jcast('int', jadd(i, 1))]))))
            i = jcast('int', (i - 1))
        ans = jcast('int', start[0])
        # end : 子数组必须以i-1结尾，其中的最大累加和
        end = jcast('int', nums[0])
        # maxEnd :
        # 0~i-1范围上，
        # 子数组必须以0结尾，其中的最大累加和
        # 子数组必须以1结尾，其中的最大累加和
        # ...
        # 子数组必须以i-1结尾，其中的最大累加和
        # 所有情况中，最大的那个累加和就是maxEnd
        maxEnd = jcast('int', nums[0])
        i = jcast('int', 1)
        while (i < n):
            # maxend   i....
            # 枚举划分点 i...
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(maxEnd, start[i]))))
            # 子数组必须以i结尾，其中的最大累加和
            end = jcast('int', jstatic('Math', 'max', nums[i], jcast('int', jadd(end, nums[i]))))
            maxEnd = jcast('int', jstatic('Math', 'max', maxEnd, end))
            i = jcast('int', (i + 1))
        ans = jcast('int', jstatic('Math', 'max', ans, maxEnd))
        return jcast('int', ans)

    # 为了测试
    # 生成随机数组
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
    # 对数器
    @staticmethod
    def main(args):
        n = jcast('int', 50)
        v = jcast('int', 200)
        testTime = jcast('int', 20000)
        jprint('测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTime):
            len = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            arr = Code05_ReverseArraySubarrayMaxSum.randomArray(len, v)
            ans1 = jcast('int', Code05_ReverseArraySubarrayMaxSum.maxSumReverse1(arr))
            ans2 = jcast('int', Code05_ReverseArraySubarrayMaxSum.maxSumReverse2(arr))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code05_ReverseArraySubarrayMaxSum.main([])
