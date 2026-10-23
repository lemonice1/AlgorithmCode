# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 绝对差不超过限制的最长连续子数组
# 给你一个整数数组 nums ，和一个表示限制的整数 limit
# 请你返回最长连续子数组的长度
# 该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit
# 如果不存在满足条件的子数组，则返回 0
# 测试链接 : https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
class Code02_LongestSubarrayAbsoluteLimit:
    __java_fields__ = {'MAXN': 'MAXN', 'maxDeque': 'maxDeque', 'minDeque': 'minDeque', 'maxh': 'maxh', 'maxt': 'maxt', 'minh': 'minh', 'mint': 'mint', 'arr': 'arr'}
    MAXN = 0
    # 窗口内最大值的更新结构（单调队列）
    maxDeque = None
    # 窗口内最小值的更新结构（单调队列）
    minDeque = None
    maxh = 0
    maxt = 0
    minh = 0
    mint = 0
    arr = None
    @staticmethod
    def longestSubarray(nums, limit):
        limit = jcast('int', limit)
        Code02_LongestSubarrayAbsoluteLimit.maxh = jcast('int', jset(Code02_LongestSubarrayAbsoluteLimit, 'maxt', jset(Code02_LongestSubarrayAbsoluteLimit, 'minh', jset(Code02_LongestSubarrayAbsoluteLimit, 'mint', 0))))
        Code02_LongestSubarrayAbsoluteLimit.arr = nums
        n = jcast('int', jget(Code02_LongestSubarrayAbsoluteLimit.arr, 'length'))
        ans = jcast('int', 0)
        l = jcast('int', 0)
        r = jcast('int', 0)
        while (l < n):
            # [l,r)，r永远是没有进入窗口的、下一个数所在的位置
            while ((r < n) and Code02_LongestSubarrayAbsoluteLimit.ok(limit, nums[r])):
                Code02_LongestSubarrayAbsoluteLimit.push(((_java_old_1 := r), (r := jcast('int', (r + (1)))), _java_old_1)[2])
            # 从while出来的时候，[l,r)是l开头的子数组能向右延伸的最大范围
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', (r - l))))
            Code02_LongestSubarrayAbsoluteLimit.pop(l)
            l = jcast('int', (l + 1))
        return jcast('int', ans)

    # 判断如果加入数字number，窗口最大值 - 窗口最小值是否依然 <= limit
    # 依然 <= limit，返回true
    # 不再 <= limit，返回false
    @staticmethod
    def ok(limit, number):
        limit = jcast('int', limit)
        number = jcast('int', number)
        # max : 如果number进来，新窗口的最大值
        max = jcast('int', (jstatic('Math', 'max', Code02_LongestSubarrayAbsoluteLimit.arr[Code02_LongestSubarrayAbsoluteLimit.maxDeque[Code02_LongestSubarrayAbsoluteLimit.maxh]], number) if (Code02_LongestSubarrayAbsoluteLimit.maxh < Code02_LongestSubarrayAbsoluteLimit.maxt) else number))
        # min : 如果number进来，新窗口的最小值
        min = jcast('int', (jstatic('Math', 'min', Code02_LongestSubarrayAbsoluteLimit.arr[Code02_LongestSubarrayAbsoluteLimit.minDeque[Code02_LongestSubarrayAbsoluteLimit.minh]], number) if (Code02_LongestSubarrayAbsoluteLimit.minh < Code02_LongestSubarrayAbsoluteLimit.mint) else number))
        return jcast('boolean', (jcast('int', (max - min)) <= limit))

    # r位置的数字进入窗口，修改窗口内最大值的更新结构、修改窗口内最小值的更新结构
    @staticmethod
    def push(r):
        r = jcast('int', r)
        while ((Code02_LongestSubarrayAbsoluteLimit.maxh < Code02_LongestSubarrayAbsoluteLimit.maxt) and (Code02_LongestSubarrayAbsoluteLimit.arr[Code02_LongestSubarrayAbsoluteLimit.maxDeque[jcast('int', (Code02_LongestSubarrayAbsoluteLimit.maxt - 1))]] <= Code02_LongestSubarrayAbsoluteLimit.arr[r])):
            Code02_LongestSubarrayAbsoluteLimit.maxt = jcast('int', (Code02_LongestSubarrayAbsoluteLimit.maxt - 1))
        jset(Code02_LongestSubarrayAbsoluteLimit.maxDeque, ((_java_obj_2 := Code02_LongestSubarrayAbsoluteLimit), (_java_key_3 := 'maxt'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))), _java_old_4)[4], r)
        while ((Code02_LongestSubarrayAbsoluteLimit.minh < Code02_LongestSubarrayAbsoluteLimit.mint) and (Code02_LongestSubarrayAbsoluteLimit.arr[Code02_LongestSubarrayAbsoluteLimit.minDeque[jcast('int', (Code02_LongestSubarrayAbsoluteLimit.mint - 1))]] >= Code02_LongestSubarrayAbsoluteLimit.arr[r])):
            Code02_LongestSubarrayAbsoluteLimit.mint = jcast('int', (Code02_LongestSubarrayAbsoluteLimit.mint - 1))
        jset(Code02_LongestSubarrayAbsoluteLimit.minDeque, ((_java_obj_5 := Code02_LongestSubarrayAbsoluteLimit), (_java_key_6 := 'mint'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))), _java_old_7)[4], r)

    # 窗口要吐出l位置的数了！检查过期！
    @staticmethod
    def pop(l):
        l = jcast('int', l)
        if ((Code02_LongestSubarrayAbsoluteLimit.maxh < Code02_LongestSubarrayAbsoluteLimit.maxt) and (Code02_LongestSubarrayAbsoluteLimit.maxDeque[Code02_LongestSubarrayAbsoluteLimit.maxh] == l)):
            Code02_LongestSubarrayAbsoluteLimit.maxh = jcast('int', (Code02_LongestSubarrayAbsoluteLimit.maxh + 1))
        if ((Code02_LongestSubarrayAbsoluteLimit.minh < Code02_LongestSubarrayAbsoluteLimit.mint) and (Code02_LongestSubarrayAbsoluteLimit.minDeque[Code02_LongestSubarrayAbsoluteLimit.minh] == l)):
            Code02_LongestSubarrayAbsoluteLimit.minh = jcast('int', (Code02_LongestSubarrayAbsoluteLimit.minh + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_LongestSubarrayAbsoluteLimit.MAXN = jcast('int', 100001)
Code02_LongestSubarrayAbsoluteLimit.maxDeque = jarray('int', [Code02_LongestSubarrayAbsoluteLimit.MAXN])
Code02_LongestSubarrayAbsoluteLimit.minDeque = jarray('int', [Code02_LongestSubarrayAbsoluteLimit.MAXN])
Code02_LongestSubarrayAbsoluteLimit.maxh = jcast('int', 0)
Code02_LongestSubarrayAbsoluteLimit.maxt = jcast('int', 0)
Code02_LongestSubarrayAbsoluteLimit.minh = jcast('int', 0)
Code02_LongestSubarrayAbsoluteLimit.mint = jcast('int', 0)
Code02_LongestSubarrayAbsoluteLimit.arr = None
