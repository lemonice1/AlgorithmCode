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

# 达标子数组的个数
# 给定一个长度为n的数组nums，给定两个整数lower和upper
# 子数组达标的条件是累加和在[lower, upper]范围上
# 返回nums中有多少个达标子数组
# 1 <= n <= 10^5
# nums[i]可能是任意整数
# -10^5 <= lower <= upper <= +10^5
# 测试链接 : https://leetcode.cn/problems/count-of-range-sum/
class Code01_CountOfRangeSum1:
    __java_fields__ = {'MAXN': 'MAXN', 'sum': 'sum', 'help': 'help', 'low': 'low', 'up': 'up'}
    # 归并分治的解法，理解难度稍高，需要先掌握讲解022 - 归并分治
    @staticmethod
    def countRangeSum(nums, lower, upper):
        lower = jcast('int', lower)
        upper = jcast('int', upper)
        n = jcast('int', jget(nums, 'length'))
        Code01_CountOfRangeSum1.sum[0] = jcast('long', nums[0])
        i = jcast('int', 1)
        while (i < n):
            Code01_CountOfRangeSum1.sum[i] = jcast('long', jcast('long', jadd(Code01_CountOfRangeSum1.sum[jcast('int', (i - 1))], nums[i])))
            i = jcast('int', (i + 1))
        Code01_CountOfRangeSum1.low = jcast('int', lower)
        Code01_CountOfRangeSum1.up = jcast('int', upper)
        return jcast('int', Code01_CountOfRangeSum1.f(0, jcast('int', (n - 1))))

    MAXN = 0
    sum = None
    help = None
    low = 0
    up = 0
    @staticmethod
    def f(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return jcast('int', (1 if ((Code01_CountOfRangeSum1.low <= Code01_CountOfRangeSum1.sum[l]) and (Code01_CountOfRangeSum1.sum[l] <= Code01_CountOfRangeSum1.up)) else 0))
        m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        return jcast('int', jcast('int', jadd(jcast('int', jadd(Code01_CountOfRangeSum1.f(l, m), Code01_CountOfRangeSum1.f(jcast('int', jadd(m, 1)), r))), Code01_CountOfRangeSum1.merge(l, m, r))))

    @staticmethod
    def merge(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        # 归并分治的统计过程
        ans = jcast('int', 0)
        wl = jcast('int', l)
        wr = jcast('int', l)
        max = 0
        min = 0
        i = jcast('int', jcast('int', jadd(m, 1)))
        while (i <= r):
            max = jcast('long', jcast('long', (Code01_CountOfRangeSum1.sum[i] - Code01_CountOfRangeSum1.low)))
            min = jcast('long', jcast('long', (Code01_CountOfRangeSum1.sum[i] - Code01_CountOfRangeSum1.up)))
            # 有效窗口是[wl,wr)，左闭右开
            while ((wr <= m) and (Code01_CountOfRangeSum1.sum[wr] <= max)):
                wr = jcast('int', (wr + 1))
            while ((wl <= m) and (Code01_CountOfRangeSum1.sum[wl] < min)):
                wl = jcast('int', (wl + 1))
            ans = jcast('int', jcast('int', jadd(ans, jcast('int', (wr - wl)))))
            i = jcast('int', (i + 1))
        # 正常排序的合并过程
        p1 = jcast('int', l)
        p2 = jcast('int', jcast('int', jadd(m, 1)))
        i = jcast('int', l)
        while ((p1 <= m) and (p2 <= r)):
            jset(Code01_CountOfRangeSum1.help, ((_java_old_3 := i), (i := jcast('int', (i + (1)))), _java_old_3)[2], (Code01_CountOfRangeSum1.sum[((_java_old_1 := p1), (p1 := jcast('int', (p1 + (1)))), _java_old_1)[2]] if (Code01_CountOfRangeSum1.sum[p1] <= Code01_CountOfRangeSum1.sum[p2]) else Code01_CountOfRangeSum1.sum[((_java_old_2 := p2), (p2 := jcast('int', (p2 + (1)))), _java_old_2)[2]]))
        while (p1 <= m):
            jset(Code01_CountOfRangeSum1.help, ((_java_old_5 := i), (i := jcast('int', (i + (1)))), _java_old_5)[2], Code01_CountOfRangeSum1.sum[((_java_old_4 := p1), (p1 := jcast('int', (p1 + (1)))), _java_old_4)[2]])
        while (p2 <= r):
            jset(Code01_CountOfRangeSum1.help, ((_java_old_7 := i), (i := jcast('int', (i + (1)))), _java_old_7)[2], Code01_CountOfRangeSum1.sum[((_java_old_6 := p2), (p2 := jcast('int', (p2 + (1)))), _java_old_6)[2]])
        i = jcast('int', l)
        while (i <= r):
            Code01_CountOfRangeSum1.sum[i] = jcast('long', Code01_CountOfRangeSum1.help[i])
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_CountOfRangeSum1.MAXN = jcast('int', 100001)
Code01_CountOfRangeSum1.sum = jarray('long', [Code01_CountOfRangeSum1.MAXN])
Code01_CountOfRangeSum1.help = jarray('long', [Code01_CountOfRangeSum1.MAXN])
Code01_CountOfRangeSum1.low = jcast('int', 0)
Code01_CountOfRangeSum1.up = jcast('int', 0)
