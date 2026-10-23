# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 三个无重叠子数组的最大和
# 给你一个整数数组 nums 和一个整数 k
# 找出三个长度为 k 、互不重叠、且全部数字和（3 * k 项）最大的子数组
# 并返回这三个子数组
# 以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置
# 如果有多个结果，返回字典序最小的一个
# 测试链接 : https://leetcode.cn/problems/maximum-sum-of-3-non-overlapping-subarrays/
class Code04_MaximumSum3UnoverlappingSubarrays:
    __java_fields__ = {}
    @staticmethod
    def maxSumOfThreeSubarrays(nums, k):
        k = jcast('int', k)
        n = jcast('int', jget(nums, 'length'))
        # sums[i] : 以i开头并且长度为k的子数组的累加和
        sums = jarray('int', [n])
        l = jcast('int', 0)
        r = jcast('int', 0)
        sum = jcast('int', 0)
        while (r < n):
            # l....r
            sum = jcast('int', jcast('int', jadd(sum, nums[r])))
            if (jcast('int', jadd(jcast('int', (r - l)), 1)) == k):
                sums[l] = jcast('int', sum)
                sum = jcast('int', jcast('int', (sum - nums[l])))
                l = jcast('int', (l + 1))
            r = jcast('int', (r + 1))
        # prefix[i] :
        # 0~i范围上所有长度为k的子数组中，拥有最大累加和的子数组，是以什么位置开头的
        prefix = jarray('int', [n])
        l = jcast('int', 1)
        r = jcast('int', k)
        while (r < n):
            if (sums[l] > sums[prefix[jcast('int', (r - 1))]]):
                # 注意>，为了同样最大累加和的情况下，最小的字典序
                prefix[r] = jcast('int', l)
            else:
                prefix[r] = jcast('int', prefix[jcast('int', (r - 1))])
            l = jcast('int', (l + 1))
            r = jcast('int', (r + 1))
        # suffix[i] :
        # i~n-1范围上所有长度为k的子数组中，拥有最大累加和的子数组，是以什么位置开头的
        suffix = jarray('int', [n])
        suffix[jcast('int', (n - k))] = jcast('int', jcast('int', (n - k)))
        l = jcast('int', jcast('int', (jcast('int', (n - k)) - 1)))
        while (l >= 0):
            if (sums[l] >= sums[suffix[jcast('int', jadd(l, 1))]]):
                # 注意>=，为了同样最大累加和的情况下，最小的字典序
                suffix[l] = jcast('int', l)
            else:
                suffix[l] = jcast('int', suffix[jcast('int', jadd(l, 1))])
            l = jcast('int', (l - 1))
        a = jcast('int', 0)
        b = jcast('int', 0)
        c = jcast('int', 0)
        max = jcast('int', 0)
        # 0...i-1    i...j    j+1...n-1
        # 左     中(长度为k)     右
        p = 0
        s = 0
        i = jcast('int', k)
        j = jcast('int', jcast('int', (jcast('int', (2 * k)) - 1)))
        sum = 0
        while (j < jcast('int', (n - k))):
            # 0.....i-1   i.....j  j+1.....n-1
            # 最好开头p      i开头     最好开头s
            p = jcast('int', prefix[jcast('int', (i - 1))])
            s = jcast('int', suffix[jcast('int', jadd(j, 1))])
            sum = jcast('int', jcast('int', jadd(jcast('int', jadd(sums[p], sums[i])), sums[s])))
            if (sum > max):
                # 注意>，为了同样最大累加和的情况下，最小的字典序
                max = jcast('int', sum)
                a = jcast('int', p)
                b = jcast('int', i)
                c = jcast('int', s)
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        return jarray('int', [None], [a, b, c])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


