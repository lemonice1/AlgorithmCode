# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 划分左右使其水王数相同
# 给定一个大小为n的数组nums
# 水王数是指在数组中出现次数大于n/2的数
# 返回其中的一个划分点下标，使得左侧水王数等于右侧水王数
# 如果数组不存在这样的划分返回-1
# 测试链接 : https://leetcode.cn/problems/minimum-index-of-a-valid-split/
class Code04_SplitSameWaterKing:
    __java_fields__ = {}
    @staticmethod
    def minimumIndex(nums):
        cand = jcast('int', 0)
        hp = jcast('int', 0)
        for num in nums:
            if (hp == 0):
                cand = jcast('int', num)
                hp = jcast('int', 1)
            else:
                if (cand == num):
                    hp = jcast('int', (hp + 1))
                else:
                    hp = jcast('int', (hp - 1))
        hp = jcast('int', 0)
        for num in nums:
            if (num == cand):
                hp = jcast('int', (hp + 1))
        n = jcast('int', jcall(nums, 'size'))
        # lc : 水王数左侧出现的词频
        # rc : 水王数右侧出现的词频
        i = jcast('int', 0)
        lc = jcast('int', 0)
        rc = jcast('int', hp)
        while (i < jcast('int', (n - 1))):
            if (jcall(nums, 'get', i) == cand):
                lc = jcast('int', (lc + 1))
                rc = jcast('int', (rc - 1))
            if ((lc > jcast('int', jdiv(jcast('int', jadd(i, 1)), 2))) and (rc > jcast('int', jdiv(jcast('int', (jcast('int', (n - i)) - 1)), 2)))):
                # 找到了划分点直接返回
                return jcast('int', i)
            i = jcast('int', (i + 1))
        # 不存在这样的划分点返回-1
        return jcast('int', jcast('int', (-1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


