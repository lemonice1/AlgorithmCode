# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 滑动窗口最大值（单调队列经典用法模版）
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧
# 你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# 返回 滑动窗口中的最大值 。
# 测试链接 : https://leetcode.cn/problems/sliding-window-maximum/
class Code01_SlidingWindowMaximum:
    __java_fields__ = {'MAXN': 'MAXN', 'deque': 'deque', 'h': 'h', 't': 't'}
    MAXN = 0
    deque = None
    h = 0
    t = 0
    @staticmethod
    def maxSlidingWindow(arr, k):
        k = jcast('int', k)
        Code01_SlidingWindowMaximum.h = jcast('int', jset(Code01_SlidingWindowMaximum, 't', 0))
        n = jcast('int', jget(arr, 'length'))
        # 先形成长度为k-1的窗口
        i = jcast('int', 0)
        while (i < jcast('int', (k - 1))):
            # 大 -> 小
            while ((Code01_SlidingWindowMaximum.h < Code01_SlidingWindowMaximum.t) and (arr[Code01_SlidingWindowMaximum.deque[jcast('int', (Code01_SlidingWindowMaximum.t - 1))]] <= arr[i])):
                Code01_SlidingWindowMaximum.t = jcast('int', (Code01_SlidingWindowMaximum.t - 1))
            jset(Code01_SlidingWindowMaximum.deque, ((_java_obj_1 := Code01_SlidingWindowMaximum), (_java_key_2 := 't'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], i)
            i = jcast('int', (i + 1))
        m = jcast('int', jcast('int', jadd(jcast('int', (n - k)), 1)))
        ans = jarray('int', [m])
        # 当前窗口k-1长度
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (k - 1)))
        while (l < m):
            # 少一个，要让r位置的数进来
            while ((Code01_SlidingWindowMaximum.h < Code01_SlidingWindowMaximum.t) and (arr[Code01_SlidingWindowMaximum.deque[jcast('int', (Code01_SlidingWindowMaximum.t - 1))]] <= arr[r])):
                Code01_SlidingWindowMaximum.t = jcast('int', (Code01_SlidingWindowMaximum.t - 1))
            jset(Code01_SlidingWindowMaximum.deque, ((_java_obj_4 := Code01_SlidingWindowMaximum), (_java_key_5 := 't'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], r)
            # 收集答案
            ans[l] = jcast('int', arr[Code01_SlidingWindowMaximum.deque[Code01_SlidingWindowMaximum.h]])
            # l位置的数出去
            if (Code01_SlidingWindowMaximum.deque[Code01_SlidingWindowMaximum.h] == l):
                Code01_SlidingWindowMaximum.h = jcast('int', (Code01_SlidingWindowMaximum.h + 1))
            l = jcast('int', (l + 1))
            r = jcast('int', (r + 1))
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_SlidingWindowMaximum.MAXN = jcast('int', 100001)
Code01_SlidingWindowMaximum.deque = jarray('int', [Code01_SlidingWindowMaximum.MAXN])
Code01_SlidingWindowMaximum.h = jcast('int', 0)
Code01_SlidingWindowMaximum.t = jcast('int', 0)
