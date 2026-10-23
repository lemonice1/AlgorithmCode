# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最大宽度坡
# 给定一个整数数组 A，坡是元组 (i, j)，其中  i < j 且 A[i] <= A[j]
# 这样的坡的宽度为 j - i，找出 A 中的坡的最大宽度，如果不存在，返回 0
# 测试链接 : https://leetcode.cn/problems/maximum-width-ramp/
class Code01_MaximumWidthRamp:
    __java_fields__ = {'MAXN': 'MAXN', 'stack': 'stack', 'r': 'r'}
    MAXN = 0
    stack = None
    r = 0
    @staticmethod
    def maxWidthRamp(arr):
        # 令r=1相当于0位置进栈了
        # stack[0] = 0，然后栈的大小变成1
        Code01_MaximumWidthRamp.r = jcast('int', 1)
        n = jcast('int', jget(arr, 'length'))
        i = jcast('int', 1)
        while (i < n):
            if (arr[Code01_MaximumWidthRamp.stack[jcast('int', (Code01_MaximumWidthRamp.r - 1))]] > arr[i]):
                jset(Code01_MaximumWidthRamp.stack, ((_java_obj_1 := Code01_MaximumWidthRamp), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], i)
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        j = jcast('int', jcast('int', (n - 1)))
        while (j >= 0):
            while ((Code01_MaximumWidthRamp.r > 0) and (arr[Code01_MaximumWidthRamp.stack[jcast('int', (Code01_MaximumWidthRamp.r - 1))]] <= arr[j])):
                ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', (j - Code01_MaximumWidthRamp.stack[((_java_obj_4 := Code01_MaximumWidthRamp), (_java_key_5 := 'r'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))))[3]]))))
            j = jcast('int', (j - 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_MaximumWidthRamp.MAXN = jcast('int', 50001)
Code01_MaximumWidthRamp.stack = jarray('int', [Code01_MaximumWidthRamp.MAXN])
Code01_MaximumWidthRamp.r = jcast('int', 0)
