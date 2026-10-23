# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 会议只占一天的最大会议数量
# 给定若干会议的开始、结束时间
# 任何会议的召开期间，你只需要抽出1天来参加
# 但是你安排的那一天，只能参加这个会议，不能同时参加其他会议
# 返回你能参加的最大会议数量
# 测试链接 : https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/
class Code04_MeetingOneDay:
    __java_fields__ = {}
    @staticmethod
    def maxEvents(events):
        n = jcast('int', jget(events, 'length'))
        # events[i][0] : i号会议开始时间
        # events[i][1] : i号会议结束时间
        jstatic('Arrays', 'sort', events, (lambda a, b: (a[0] - b[0])))
        min = jcast('int', events[0][0])
        max = jcast('int', events[0][1])
        i = jcast('int', 1)
        while (i < n):
            max = jcast('int', jstatic('Math', 'max', max, events[i][1]))
            i = jcast('int', (i + 1))
        # 小根堆 : 会议的结束时间
        heap = jnew('PriorityQueue')
        i = jcast('int', 0)
        ans = jcast('int', 0)
        day = jcast('int', min)
        while (day <= max):
            while ((i < n) and (events[i][0] == day)):
                jcall(heap, 'add', events[((_java_old_1 := i), (i := jcast('int', (i + (1)))), _java_old_1)[2]][1])
            while ((not jcall(heap, 'isEmpty')) and (jcall(heap, 'peek') < day)):
                jcall(heap, 'poll')
            if (not jcall(heap, 'isEmpty')):
                jcall(heap, 'poll')
                ans = jcast('int', (ans + 1))
            day = jcast('int', (day + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


