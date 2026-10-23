# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# K个不同整数的子数组
# 给定一个正整数数组 nums和一个整数 k，返回 nums 中 「好子数组」 的数目。
# 如果 nums 的某个子数组中不同整数的个数恰好为 k
# 则称 nums 的这个连续、不一定不同的子数组为 「好子数组 」。
# 例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。
# 子数组 是数组的 连续 部分。
# 测试链接 : https://leetcode.cn/problems/subarrays-with-k-different-integers/
class Code06_SubarraysWithKDifferentIntegers:
    __java_fields__ = {'MAXN': 'MAXN', 'cnts': 'cnts'}
    @staticmethod
    def subarraysWithKDistinct(arr, k):
        k = jcast('int', k)
        return jcast('int', jcast('int', (Code06_SubarraysWithKDifferentIntegers.numsOfMostKinds(arr, k) - Code06_SubarraysWithKDifferentIntegers.numsOfMostKinds(arr, jcast('int', (k - 1))))))

    MAXN = 0
    cnts = None
    # arr中有多少子数组，数字种类不超过k
    # arr的长度是n，arr里的数值1~n之间
    @staticmethod
    def numsOfMostKinds(arr, k):
        k = jcast('int', k)
        jstatic('Arrays', 'fill', Code06_SubarraysWithKDifferentIntegers.cnts, 1, jcast('int', jadd(jget(arr, 'length'), 1)), 0)
        ans = jcast('int', 0)
        l = jcast('int', 0)
        r = jcast('int', 0)
        collect = jcast('int', 0)
        while (r < jget(arr, 'length')):
            if (((_java_obj_1 := Code06_SubarraysWithKDifferentIntegers.cnts), (_java_key_2 := arr[r]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3] == 1):
                collect = jcast('int', (collect + 1))
            while (collect > k):
                if (((_java_obj_6 := Code06_SubarraysWithKDifferentIntegers.cnts), (_java_key_7 := arr[((_java_old_5 := l), (l := jcast('int', (l + (1)))), _java_old_5)[2]]), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (-1)))))[3] == 0):
                    collect = jcast('int', (collect - 1))
            ans = jcast('int', jcast('int', jadd(ans, jcast('int', jadd(jcast('int', (r - l)), 1)))))
            r = jcast('int', (r + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_SubarraysWithKDifferentIntegers.MAXN = jcast('int', 20001)
Code06_SubarraysWithKDifferentIntegers.cnts = jarray('int', [Code06_SubarraysWithKDifferentIntegers.MAXN])
