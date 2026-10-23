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

# 表现良好的最长时间段
# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数
# 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是 劳累的一天
# 所谓 表现良好的时间段 ，意味在这段时间内，「劳累的天数」是严格 大于 不劳累的天数
# 请你返回 表现良好时间段 的最大长度
# 测试链接 : https://leetcode.cn/problems/longest-well-performing-interval/
class Code05_LongestWellPerformingInterval:
    __java_fields__ = {}
    @staticmethod
    def longestWPI(hours):
        # 某个前缀和，最早出现的位置
        map = jnew('HashMap')
        # 0这个前缀和，最早出现在-1，一个数也没有的时候
        jcall(map, 'put', 0, jcast('int', (-1)))
        ans = jcast('int', 0)
        i = jcast('int', 0)
        sum = jcast('int', 0)
        while (i < jget(hours, 'length')):
            sum = jcast('int', jcast('int', jadd(sum, (1 if (hours[i] > 8) else jcast('int', (-1))))))
            if (sum > 0):
                ans = jcast('int', jcast('int', jadd(i, 1)))
            else:
                # sum <= 0
                if jcall(map, 'containsKey', jcast('int', (sum - 1))):
                    ans = jcast('int', jstatic('Math', 'max', ans, (i - jcall(map, 'get', jcast('int', (sum - 1))))))
            if (not jcall(map, 'containsKey', sum)):
                jcall(map, 'put', sum, i)
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


