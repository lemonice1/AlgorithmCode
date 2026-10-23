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

# 爱吃香蕉的珂珂
# 珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉
# 警卫已经离开了，将在 h 小时后回来。
# 珂珂可以决定她吃香蕉的速度 k （单位：根/小时)
# 每个小时，她将会选择一堆香蕉，从中吃掉 k 根
# 如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉
# 珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
# 返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）
# 测试链接 : https://leetcode.cn/problems/koko-eating-bananas/
class Code01_KokoEatingBananas:
    __java_fields__ = {}
    # 时间复杂度O(n * log(max))，额外空间复杂度O(1)
    @staticmethod
    def minEatingSpeed(piles, h):
        h = jcast('int', h)
        # 最小且达标的速度，范围[l,r]
        l = jcast('int', 1)
        r = jcast('int', 0)
        for pile in piles:
            r = jcast('int', jstatic('Math', 'max', r, pile))
        # [l,r]不停二分
        ans = jcast('int', 0)
        m = jcast('int', 0)
        while (l <= r):
            # m = (l + r) / 2
            m = jcast('int', jcast('int', jadd(l, jcast('int', (jcast('int', (r - l)) >> (1 & 31))))))
            if (Code01_KokoEatingBananas.f(piles, m) <= h):
                # 达标！
                # 记录答案，去左侧二分
                ans = jcast('int', m)
                # l....m....r
                # l..m-1
                r = jcast('int', jcast('int', (m - 1)))
            else:
                # 不达标
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    # 香蕉重量都在piles
    # 速度就定成speed
    # 返回吃完所有的香蕉，耗费的小时数量
    @staticmethod
    def f(piles, speed):
        speed = jcast('int', speed)
        ans = jcast('long', 0)
        for pile in piles:
            # (a/b)结果向上取整，如果a和b都是非负数，可以写成(a+b-1)/b
            # "讲解032-位图"讲了这种写法，不会的同学可以去看看
            # 这里不再赘述
            ans = jcast('long', jcast('long', jadd(ans, jcast('int', jdiv(jcast('int', (jcast('int', jadd(pile, speed)) - 1)), speed)))))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


