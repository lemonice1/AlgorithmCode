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

# 两地调度
# 公司计划面试2n个人，给定一个数组 costs
# 其中costs[i]=[aCosti, bCosti]
# 表示第i人飞往a市的费用为aCosti，飞往b市的费用为bCosti
# 返回将每个人都飞到a、b中某座城市的最低费用
# 要求每个城市都有n人抵达
# 测试链接 : https://leetcode.cn/problems/two-city-scheduling/
class Code02_TwoCityScheduling:
    __java_fields__ = {}
    @staticmethod
    def twoCitySchedCost(costs):
        n = jcast('int', jget(costs, 'length'))
        arr = jarray('int', [n])
        sum = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            arr[i] = jcast('int', jcast('int', (costs[i][1] - costs[i][0])))
            sum = jcast('int', jcast('int', jadd(sum, costs[i][0])))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', arr)
        m = jcast('int', jcast('int', jdiv(n, 2)))
        i = jcast('int', 0)
        while (i < m):
            sum = jcast('int', jcast('int', jadd(sum, arr[i])))
            i = jcast('int', (i + 1))
        return jcast('int', sum)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


