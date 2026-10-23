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

# 分割的方法数
# 有同学找到了测试链接，题意几乎一样，而且数据量小很多
# 唯一的区别是：
# 课上讲的题意，单独的3可以分裂成(1, 2)、(2, 1)，一共两种方式
# 测试链接题意，单独的3可以分裂成(0, 3)、(1, 2)、(2, 1)、(3, 0)，一共四种方式
# 也就是对单独的v来说，课上讲的题意，分裂方式为v-1种。测试链接题意，分裂方式为v+1种
# 别的没有任何区别，实现代码中唯一有注释的那行，是仅有的改动
# 测试链接 : https://leetcode.cn/problems/find-the-count-of-monotonic-pairs-ii/
class Code04_SplitWays2:
    __java_fields__ = {'MOD': 'MOD'}
    MOD = 0
    @staticmethod
    def countOfPairs(arr):
        n = jcast('int', jget(arr, 'length'))
        # 原始题意，k = arr[0] - 1，这里改成，k = arr[0] + 1
        # 其他代码毫无区别
        k = jcast('int', jcast('int', jadd(arr[0], 1)))
        i = jcast('int', 1)
        while ((i < n) and (k > 0)):
            if (arr[jcast('int', (i - 1))] > arr[i]):
                k = jcast('int', jcast('int', (k - jcast('int', (arr[jcast('int', (i - 1))] - arr[i])))))
            i = jcast('int', (i + 1))
        if (k <= 0):
            return jcast('int', 0)
        return jcast('int', Code04_SplitWays2.c(jcast('int', (jcast('int', jadd(k, n)) - 1)), n))

    @staticmethod
    def c(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        fac = jcast('long', 1)
        inv1 = jcast('long', 1)
        inv2 = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= n):
            fac = jcast('long', jcast('long', jmod(jcast('long', (fac * i)), Code04_SplitWays2.MOD)))
            if (i == k):
                inv1 = jcast('long', Code04_SplitWays2.power(fac, jcast('int', (Code04_SplitWays2.MOD - 2))))
            if (i == jcast('int', (n - k))):
                inv2 = jcast('long', Code04_SplitWays2.power(fac, jcast('int', (Code04_SplitWays2.MOD - 2))))
            i = jcast('int', (i + 1))
        return jcast('int', jcast('int', jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (fac * inv1)), Code04_SplitWays2.MOD)) * inv2)), Code04_SplitWays2.MOD))))

    @staticmethod
    def power(x, p):
        x = jcast('long', x)
        p = jcast('long', p)
        ans = jcast('long', 1)
        while (p > 0):
            if (jcast('long', (p & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), Code04_SplitWays2.MOD)))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), Code04_SplitWays2.MOD)))
            p = jcast('long', jcast('long', (p >> (1 & 63))))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_SplitWays2.MOD = jcast('int', 1000000007)
