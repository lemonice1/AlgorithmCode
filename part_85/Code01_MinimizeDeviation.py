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

# 数组的最小偏移量
# 给你一个由n个正整数组成的数组nums
# 你可以对数组的任意元素执行任意次数的两类操作：
# 如果元素是偶数，除以2
# 例如如果数组是[1,2,3,4]
# 那么你可以对最后一个元素执行此操作，使其变成[1,2,3,2]
# 如果元素是奇数，乘上2
# 例如如果数组是[1,2,3,4]
# 那么你可以对第一个元素执行此操作，使其变成[2,2,3,4]
# 数组的偏移量是数组中任意两个元素之间的最大差值
# 返回数组在执行某些操作之后可以拥有的最小偏移量
# 测试链接 : https://leetcode.cn/problems/minimize-deviation-in-array/
class Code01_MinimizeDeviation:
    __java_fields__ = {}
    @staticmethod
    def minimumDeviation(nums):
        # 有序表可以查询最大值、最小值
        set = jnew('TreeSet')
        for num in nums:
            if (jcast('int', jmod(num, 2)) == 0):
                jcall(set, 'add', num)
            else:
                jcall(set, 'add', jcast('int', (num * 2)))
        ans = jcast('int', (jcall(set, 'last') - jcall(set, 'first')))
        while ((ans > 0) and (jmod(jcall(set, 'last'), 2) == 0)):
            max = jcast('int', jcall(set, 'last'))
            jcall(set, 'remove', max)
            jcall(set, 'add', jcast('int', jdiv(max, 2)))
            ans = jcast('int', jstatic('Math', 'min', ans, (jcall(set, 'last') - jcall(set, 'first'))))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


