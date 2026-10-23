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

# 会议室II
# 给你一个会议时间安排的数组 intervals
# 每个会议时间都会包括开始和结束的时间intervals[i]=[starti, endi]
# 返回所需会议室的最小数量
# 测试链接 : https://leetcode.cn/problems/meeting-rooms-ii/
class Code04_MeetingRoomsII:
    __java_fields__ = {}
    @staticmethod
    def minMeetingRooms(meeting):
        n = jcast('int', jget(meeting, 'length'))
        jstatic('Arrays', 'sort', meeting, (lambda a, b: (a[0] - b[0])))
        heap = jnew('PriorityQueue')
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            while ((not jcall(heap, 'isEmpty')) and (jcall(heap, 'peek') <= meeting[i][0])):
                jcall(heap, 'poll')
            jcall(heap, 'add', meeting[i][1])
            ans = jcast('int', jstatic('Math', 'max', ans, jcall(heap, 'size')))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


