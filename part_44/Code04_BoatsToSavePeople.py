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

# 救生艇
# 给定数组 people
# people[i]表示第 i 个人的体重 ，船的数量不限，每艘船可以承载的最大重量为 limit
# 每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit
# 返回 承载所有人所需的最小船数
# 测试链接 : https://leetcode.cn/problems/boats-to-save-people/
class Code04_BoatsToSavePeople:
    __java_fields__ = {}
    # 时间复杂度O(n * logn)，因为有排序，额外空间复杂度O(1)
    @staticmethod
    def numRescueBoats(people, limit):
        limit = jcast('int', limit)
        jstatic('Arrays', 'sort', people)
        ans = jcast('int', 0)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (jget(people, 'length') - 1)))
        sum = jcast('int', 0)
        while (l <= r):
            sum = jcast('int', (people[l] if (l == r) else jcast('int', jadd(people[l], people[r]))))
            if (sum > limit):
                r = jcast('int', (r - 1))
            else:
                l = jcast('int', (l + 1))
                r = jcast('int', (r - 1))
            ans = jcast('int', (ans + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


