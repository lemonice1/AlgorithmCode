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

# 供暖器
# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
# 在加热器的加热半径范围内的每个房屋都可以获得供暖。
# 现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置
# 请你找出并返回可以覆盖所有房屋的最小加热半径。
# 说明：所有供暖器都遵循你的半径标准，加热的半径也一样。
# 测试链接 : https://leetcode.cn/problems/heaters/
class Code06_Heaters:
    __java_fields__ = {}
    # 时间复杂度O(n * logn)，因为有排序，额外空间复杂度O(1)
    @staticmethod
    def findRadius(houses, heaters):
        jstatic('Arrays', 'sort', houses)
        jstatic('Arrays', 'sort', heaters)
        ans = jcast('int', 0)
        i = jcast('int', 0)
        j = jcast('int', 0)
        while (i < jget(houses, 'length')):
            # i号房屋
            # j号供暖器
            while (not Code06_Heaters.best(houses, heaters, i, j)):
                j = jcast('int', (j + 1))
            ans = jcast('int', jstatic('Math', 'max', ans, jstatic('Math', 'abs', jcast('int', (heaters[j] - houses[i])))))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 这个函数含义：
    # 当前的地点houses[i]由heaters[j]来供暖是最优的吗？
    # 当前的地点houses[i]由heaters[j]来供暖，产生的半径是a
    # 当前的地点houses[i]由heaters[j + 1]来供暖，产生的半径是b
    # 如果a < b, 说明是最优，供暖不应该跳下一个位置
    # 如果a >= b, 说明不是最优，应该跳下一个位置
    @staticmethod
    def best(houses, heaters, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        return jcast('boolean', ((j == jcast('int', (jget(heaters, 'length') - 1))) or (jstatic('Math', 'abs', jcast('int', (heaters[j] - houses[i]))) < jstatic('Math', 'abs', jcast('int', (heaters[jcast('int', jadd(j, 1))] - houses[i]))))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


