# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 大楼扔鸡蛋问题
# 一共有k枚相同的鸡蛋，一共有n层楼
# 已知一定存在楼层f(0<=f<=n)，从>f的楼层扔鸡蛋一定会碎，从<=f的楼层扔鸡蛋，扔几次都不会碎
# 鸡蛋一旦碎了就不能再使用，只能选择另外的鸡蛋
# 现在想确定f的值，返回最少扔几次鸡蛋，可以确保测出该值
# 1 <= k <= 100
# 1 <= n <= 10^4
# 测试链接 : https://leetcode.cn/problems/super-egg-drop/
class Code04_EggDrop:
    __java_fields__ = {}
    # 最优解
    @staticmethod
    def superEggDrop1(k, n):
        k = jcast('int', k)
        n = jcast('int', n)
        if (k == 1):
            return jcast('int', n)
        dp = jarray('int', [jcast('int', jadd(k, 1)), jcast('int', jadd(n, 1))])
        j = jcast('int', 1)
        while (j <= n):
            i = jcast('int', 1)
            while (i <= k):
                jset(dp[i], j, jcast('int', jadd(jcast('int', jadd(dp[jcast('int', (i - 1))][jcast('int', (j - 1))], dp[i][jcast('int', (j - 1))])), 1)))
                if (dp[i][j] >= n):
                    return jcast('int', j)
                i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        return jcast('int', jcast('int', (-1)))

    # 最优解空间压缩的版本
    @staticmethod
    def superEggDrop2(k, n):
        k = jcast('int', k)
        n = jcast('int', n)
        if (k == 1):
            return jcast('int', n)
        dp = jarray('int', [jcast('int', jadd(k, 1))])
        j = jcast('int', 1)
        while (j <= n):
            pre = jcast('int', 0)
            i = jcast('int', 1)
            while (i <= k):
                tmp = jcast('int', dp[i])
                dp[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(dp[i], pre)), 1)))
                pre = jcast('int', tmp)
                if (dp[i] >= n):
                    return jcast('int', j)
                i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        return jcast('int', jcast('int', (-1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


