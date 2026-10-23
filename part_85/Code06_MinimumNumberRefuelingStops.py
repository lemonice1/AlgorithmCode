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

# 最低加油次数
# 汽车从起点出发驶向目的地，该目的地位于出发位置东面target英里处
# 沿途有加油站，用数组stations表示，其中 stations[i] = [positioni, fueli]
# 表示第i个加油站位于出发位置东面positioni英里处，并且有fueli升汽油
# 假设汽车油箱的容量是无限的，其中最初有startFuel升燃料
# 它每行驶1英里就会用掉1升汽油
# 当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中
# 为了到达目的地，汽车所必要的最低加油次数是多少？
# 如果无法到达目的地，则返回-1
# 注意：如果汽车到达加油站时剩余燃料为0，它仍然可以在那里加油
# 如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地
# 测试链接 : https://leetcode.cn/problems/minimum-number-of-refueling-stops/
class Code06_MinimumNumberRefuelingStops:
    __java_fields__ = {}
    @staticmethod
    def minRefuelStops(target, startFuel, stations):
        target = jcast('int', target)
        startFuel = jcast('int', startFuel)
        if (startFuel >= target):
            return jcast('int', 0)
        # 大根堆
        heap = jnew('PriorityQueue', (lambda a, b: (b - a)))
        # 包括初始油量 + 沿途加的油，能让你达到什么位置，to
        to = jcast('int', startFuel)
        cnt = jcast('int', 0)
        for station in stations:
            position = jcast('int', station[0])
            fuel = jcast('int', station[1])
            if (to < position):
                while ((not jcall(heap, 'isEmpty')) and (to < position)):
                    to = jcast('int', jadd(to, jcall(heap, 'poll')))
                    cnt = jcast('int', (cnt + 1))
                    if (to >= target):
                        return jcast('int', cnt)
                if (to < position):
                    return jcast('int', jcast('int', (-1)))
            jcall(heap, 'add', fuel)
        # 代码能走到这里，说明还没到达target
        # 如果还有油，看看能不能冲到target
        while (not jcall(heap, 'isEmpty')):
            to = jcast('int', jadd(to, jcall(heap, 'poll')))
            cnt = jcast('int', (cnt + 1))
            if (to >= target):
                return jcast('int', cnt)
        return jcast('int', jcast('int', (-1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


