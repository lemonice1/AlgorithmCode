# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 满足不等式的最大值
# 给你一个数组 points 和一个整数 k
# 数组中每个元素都表示二维平面上的点的坐标，并按照横坐标 x 的值从小到大排序
# 也就是说 points[i] = [xi, yi]
# 并且在 1 <= i < j <= points.length 的前提下，xi < xj 总成立
# 请你找出 yi + yj + |xi - xj| 的 最大值，
# 其中 |xi - xj| <= k 且 1 <= i < j <= points.length
# 题目测试数据保证至少存在一对能够满足 |xi - xj| <= k 的点。
# 测试链接 : https://leetcode.cn/problems/max-value-of-equation/
class Code02_MaxValueOfEquation:
    __java_fields__ = {'MAXN': 'MAXN', 'deque': 'deque', 'h': 'h', 't': 't'}
    MAXN = 0
    # [、i号点[x,y]、]
    # h、t
    deque = None
    h = 0
    t = 0
    # 已知所有的点都是根据x值排序的！
    # 任何两个点，组成指标，要求 : 后x - 前x <= k
    # 返回最大指标
    @staticmethod
    def findMaxValueOfEquation(points, k):
        k = jcast('int', k)
        Code02_MaxValueOfEquation.h = jcast('int', jset(Code02_MaxValueOfEquation, 't', 0))
        n = jcast('int', jget(points, 'length'))
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        i = jcast('int', 0)
        x = 0
        y = 0
        while (i < n):
            # i号点是此时的点，当前的后面点，看之前哪个点的y-x值最大，x距离又不能超过k
            x = jcast('int', points[i][0])
            y = jcast('int', points[i][1])
            while ((Code02_MaxValueOfEquation.h < Code02_MaxValueOfEquation.t) and (jcast('int', jadd(Code02_MaxValueOfEquation.deque[Code02_MaxValueOfEquation.h][0], k)) < x)):
                # 单调队列头部的可能性过期了，头部点的x与当前点x的距离超过了k
                Code02_MaxValueOfEquation.h = jcast('int', (Code02_MaxValueOfEquation.h + 1))
            if (Code02_MaxValueOfEquation.h < Code02_MaxValueOfEquation.t):
                ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', (jcast('int', jadd(jcast('int', jadd(x, y)), Code02_MaxValueOfEquation.deque[Code02_MaxValueOfEquation.h][1])) - Code02_MaxValueOfEquation.deque[Code02_MaxValueOfEquation.h][0]))))
            # i号点的x和y，该从尾部进入单调队列
            # 大 -> 小
            while ((Code02_MaxValueOfEquation.h < Code02_MaxValueOfEquation.t) and (jcast('int', (Code02_MaxValueOfEquation.deque[jcast('int', (Code02_MaxValueOfEquation.t - 1))][1] - Code02_MaxValueOfEquation.deque[jcast('int', (Code02_MaxValueOfEquation.t - 1))][0])) <= jcast('int', (y - x)))):
                Code02_MaxValueOfEquation.t = jcast('int', (Code02_MaxValueOfEquation.t - 1))
            jset(Code02_MaxValueOfEquation.deque[Code02_MaxValueOfEquation.t], 0, x)
            jset(Code02_MaxValueOfEquation.deque[((_java_obj_1 := Code02_MaxValueOfEquation), (_java_key_2 := 't'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]], 1, y)
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_MaxValueOfEquation.MAXN = jcast('int', 100001)
Code02_MaxValueOfEquation.deque = jarray('int', [Code02_MaxValueOfEquation.MAXN, 2])
Code02_MaxValueOfEquation.h = jcast('int', 0)
Code02_MaxValueOfEquation.t = jcast('int', 0)
