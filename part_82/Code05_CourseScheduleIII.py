# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 课程表III
# 这里有n门不同的在线课程，按从1到n编号
# 给你一个数组courses
# 其中courses[i]=[durationi, lastDayi]表示第i门课将会持续上durationi天课
# 并且必须在不晚于lastDayi的时候完成
# 你的学期从第 1 天开始
# 且不能同时修读两门及两门以上的课程
# 返回你最多可以修读的课程数目
# 测试链接 : https://leetcode.cn/problems/course-schedule-iii/
class Code05_CourseScheduleIII:
    __java_fields__ = {}
    @staticmethod
    def scheduleCourse(courses):
        # 0 : 代价
        # 1 : 截止
        jstatic('Arrays', 'sort', courses, (lambda a, b: (a[1] - b[1])))
        # 大根堆
        heap = jnew('PriorityQueue', (lambda a, b: (b - a)))
        time = jcast('int', 0)
        for c in courses:
            if (jcast('int', jadd(time, c[0])) <= c[1]):
                jcall(heap, 'add', c[0])
                time = jcast('int', jcast('int', jadd(time, c[0])))
            else:
                # time + c[0] > c[1]
                if ((not jcall(heap, 'isEmpty')) and (jcall(heap, 'peek') > c[0])):
                    time = jcast('int', jadd(time, (c[0] - jcall(heap, 'poll'))))
                    jcall(heap, 'add', c[0])
        return jcast('int', jcall(heap, 'size'))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


