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

# 巫师力量和
# 题目可以简化为如下的描述
# 给定一个长度为n的数组arr，下标从0开始
# 任何一个子数组的指标为，子数组累加和 * 子数组中最小值
# 返回arr中所有子数组指标的累加和，答案对 1000000007 取模
# 1 <= n <= 10^5
# 1 <= arr[i] <= 10^9
# 测试链接 : https://leetcode.cn/problems/sum-of-total-strength-of-wizards/
class Code06_SumOfTotalStrength:
    __java_fields__ = {'MOD': 'MOD'}
    MOD = 0
    @staticmethod
    def totalStrength(arr):
        n = jcast('int', jget(arr, 'length'))
        pre = jcast('int', jcast('int', jmod(arr[0], Code06_SumOfTotalStrength.MOD)))
        sumsum = jarray('int', [n])
        sumsum[0] = jcast('int', pre)
        i = jcast('int', 1)
        while (i < n):
            pre = jcast('int', jcast('int', jmod(jcast('int', jadd(pre, arr[i])), Code06_SumOfTotalStrength.MOD)))
            sumsum[i] = jcast('int', jcast('int', jmod(jcast('int', jadd(sumsum[jcast('int', (i - 1))], pre)), Code06_SumOfTotalStrength.MOD)))
            i = jcast('int', (i + 1))
        stack = jarray('int', [n])
        size = jcast('int', 0)
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            while ((size > 0) and (arr[stack[jcast('int', (size - 1))]] >= arr[i])):
                m = jcast('int', stack[(size := jcast('int', (size + (-1))))])
                l = jcast('int', (stack[jcast('int', (size - 1))] if (size > 0) else jcast('int', (-1))))
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code06_SumOfTotalStrength.sum(arr, sumsum, l, m, i))), Code06_SumOfTotalStrength.MOD)))
            jset(stack, ((_java_old_1 := size), (size := jcast('int', (size + (1)))), _java_old_1)[2], i)
            i = jcast('int', (i + 1))
        while (size > 0):
            m = jcast('int', stack[(size := jcast('int', (size + (-1))))])
            l = jcast('int', (stack[jcast('int', (size - 1))] if (size > 0) else jcast('int', (-1))))
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code06_SumOfTotalStrength.sum(arr, sumsum, l, m, n))), Code06_SumOfTotalStrength.MOD)))
        return jcast('int', ans)

    @staticmethod
    def sum(arr, sumsum, l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        left = jcast('long', sumsum[jcast('int', (r - 1))])
        if (jcast('int', (m - 1)) >= 0):
            left = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', (left - sumsum[jcast('int', (m - 1))])), Code06_SumOfTotalStrength.MOD)), Code06_SumOfTotalStrength.MOD)))
        left = jcast('long', jcast('long', jmod(jcast('long', (left * jcast('int', (m - l)))), Code06_SumOfTotalStrength.MOD)))
        right = jcast('long', 0)
        if (jcast('int', (m - 1)) >= 0):
            right = jcast('long', jcast('long', jmod(jcast('long', jadd(right, sumsum[jcast('int', (m - 1))])), Code06_SumOfTotalStrength.MOD)))
        if (jcast('int', (l - 1)) >= 0):
            right = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', (right - sumsum[jcast('int', (l - 1))])), Code06_SumOfTotalStrength.MOD)), Code06_SumOfTotalStrength.MOD)))
        right = jcast('long', jcast('long', jmod(jcast('long', (right * jcast('int', (r - m)))), Code06_SumOfTotalStrength.MOD)))
        return jcast('int', jcast('int', jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', jadd(jcast('long', (left - right)), Code06_SumOfTotalStrength.MOD)), Code06_SumOfTotalStrength.MOD)) * arr[m])), Code06_SumOfTotalStrength.MOD))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_SumOfTotalStrength.MOD = jcast('int', 1000000007)
