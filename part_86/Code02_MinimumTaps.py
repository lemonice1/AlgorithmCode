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

# 灌溉花园的最少水龙头数目
# 在x轴上有一个一维的花园，花园长度为n，从点0开始，到点n结束
# 花园里总共有 n + 1 个水龙头，分别位于[0, 1, ... n]
# 给你一个整数n和一个长度为n+1的整数数组ranges
# 其中ranges[i]表示
# 如果打开点i处的水龙头，可以灌溉的区域为[i-ranges[i], i+ranges[i]]
# 请你返回可以灌溉整个花园的最少水龙头数目
# 如果花园始终存在无法灌溉到的地方请你返回-1
# 测试链接 : https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden/
class Code02_MinimumTaps:
    __java_fields__ = {}
    @staticmethod
    def minTaps(n, ranges):
        n = jcast('int', n)
        # right[i] = j
        # 所有左边界在i的水龙头里，影响到的最右右边界是j
        right = jarray('int', [jcast('int', jadd(n, 1))])
        i = jcast('int', 0)
        start = 0
        while (i <= n):
            start = jcast('int', jstatic('Math', 'max', 0, jcast('int', (i - ranges[i]))))
            jset(right, start, jstatic('Math', 'max', right[start], jcast('int', jadd(i, ranges[i]))))
            i = jcast('int', (i + 1))
        # 当前ans数量的水龙头打开，影响到的最右右边界
        cur = jcast('int', 0)
        # 如果再多打开一个水龙头，影响到的最右边界
        next = jcast('int', 0)
        # 打开水龙头的数量
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            # 来到i位置
            # 先更新下一步的next
            next = jcast('int', jstatic('Math', 'max', next, right[i]))
            if (i == cur):
                if (next > i):
                    cur = jcast('int', next)
                    ans = jcast('int', (ans + 1))
                else:
                    return jcast('int', jcast('int', (-1)))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


