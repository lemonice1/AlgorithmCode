# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 将珠子放进背包中
# 给定一个长度为n的数组weights，背包一共有k个
# 其中weights[i]是第i个珠子的重量
# 请你按照如下规则将所有的珠子放进k个背包
# 1，没有背包是空的
# 2，如果第i个珠子和第j个珠子在同一个背包里，那么i到j所有珠子都要在这个背包里
# 一个背包如果包含i到j的所有珠子，这个背包的价格是weights[i]+weights[j]
# 一个珠子分配方案的分数，是所有k个背包的价格之和
# 请返回所有分配方案中，最大分数与最小分数的差值为多少
# 1 <= n, k <= 10^5
# 测试链接 : https://leetcode.cn/problems/put-marbles-in-bags/
class Code06_MarblesInBags:
    __java_fields__ = {}
    @staticmethod
    def putMarbles(weights, k):
        k = jcast('int', k)
        n = jcast('int', jget(weights, 'length'))
        split = jarray('long', [jcast('int', (n - 1))])
        i = jcast('int', 1)
        while (i < n):
            split[jcast('int', (i - 1))] = jcast('long', jcast('long', jadd(jcast('long', weights[jcast('int', (i - 1))]), weights[i])))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', split)
        small = jcast('long', 0)
        big = jcast('long', 0)
        i = jcast('int', 0)
        j = jcast('int', jcast('int', (n - 2)))
        p = jcast('int', 1)
        while (p < k):
            small = jcast('long', jcast('long', jadd(small, split[i])))
            big = jcast('long', jcast('long', jadd(big, split[j])))
            i = jcast('int', (i + 1))
            j = jcast('int', (j - 1))
            p = jcast('int', (p + 1))
        return jcast('long', jcast('long', (big - small)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


