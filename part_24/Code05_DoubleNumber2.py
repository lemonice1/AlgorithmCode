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

# 数组中有2种数出现了奇数次，其他的数都出现了偶数次
# 返回这2种出现了奇数次的数
# 测试链接 : https://leetcode.cn/problems/single-number-iii/
# 下面为对应算法的 Python 实现，保留原算法逻辑
class Code05_DoubleNumber2:
    __java_fields__ = {}
    @staticmethod
    def singleNumber(nums):
        eor1 = jcast('int', 0)
        for num in nums:
            # nums中有2种数a、b出现了奇数次，其他的数都出现了偶数次
            eor1 = jcast('int', jcast('int', (eor1 ^ num)))
        # eor1 : a ^ b
        # Brian Kernighan算法
        # 提取出二进制里最右侧的1
        rightOne = jcast('int', jcast('int', (eor1 & jcast('int', (-eor1)))))
        eor2 = jcast('int', 0)
        for num in nums:
            if (jcast('int', (num & rightOne)) == 0):
                eor2 = jcast('int', jcast('int', (eor2 ^ num)))
        return jarray('int', [None], [eor2, jcast('int', (eor1 ^ eor2))])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


