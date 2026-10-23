# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 每日温度
# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer
# 其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后
# 如果气温在这之后都不会升高，请在该位置用 0 来代替。
# 测试链接 : https://leetcode.cn/problems/daily-temperatures/
class Code02_DailyTemperatures:
    __java_fields__ = {'MAXN': 'MAXN', 'stack': 'stack', 'r': 'r'}
    MAXN = 0
    stack = None
    r = 0
    @staticmethod
    def dailyTemperatures(nums):
        n = jcast('int', jget(nums, 'length'))
        ans = jarray('int', [n])
        Code02_DailyTemperatures.r = jcast('int', 0)
        i = jcast('int', 0)
        cur = 0
        while (i < n):
            # 相等时候的处理，相等也加入单调栈
            while ((Code02_DailyTemperatures.r > 0) and (nums[Code02_DailyTemperatures.stack[jcast('int', (Code02_DailyTemperatures.r - 1))]] < nums[i])):
                cur = jcast('int', Code02_DailyTemperatures.stack[((_java_obj_1 := Code02_DailyTemperatures), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))))[3]])
                ans[cur] = jcast('int', jcast('int', (i - cur)))
            jset(Code02_DailyTemperatures.stack, ((_java_obj_4 := Code02_DailyTemperatures), (_java_key_5 := 'r'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], i)
            i = jcast('int', (i + 1))
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_DailyTemperatures.MAXN = jcast('int', 100001)
Code02_DailyTemperatures.stack = jarray('int', [Code02_DailyTemperatures.MAXN])
Code02_DailyTemperatures.r = jcast('int', 0)
