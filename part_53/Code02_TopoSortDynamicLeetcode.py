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

# 拓扑排序模版（Leetcode）
# 邻接表建图（动态方式）
# 课程表II
# 现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1
# 给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi]
# 表示在选修课程 ai 前 必须 先选修 bi
# 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1]
# 返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序
# 你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组
# 测试链接 : https://leetcode.cn/problems/course-schedule-ii/
class Code02_TopoSortDynamicLeetcode:
    __java_fields__ = {}
    @staticmethod
    def findOrder(numCourses, prerequisites):
        numCourses = jcast('int', numCourses)
        graph = jnew('ArrayList')
        # 0 ~ n-1
        i = jcast('int', 0)
        while (i < numCourses):
            jcall(graph, 'add', jnew('ArrayList'))
            i = jcast('int', (i + 1))
        # 入度表
        indegree = jarray('int', [numCourses])
        for edge in prerequisites:
            jcall(jcall(graph, 'get', edge[1]), 'add', edge[0])
            ((_java_obj_1 := indegree), (_java_key_2 := edge[0]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
        queue = jarray('int', [numCourses])
        l = jcast('int', 0)
        r = jcast('int', 0)
        i = jcast('int', 0)
        while (i < numCourses):
            if (indegree[i] == 0):
                jset(queue, ((_java_old_4 := r), (r := jcast('int', (r + (1)))), _java_old_4)[2], i)
            i = jcast('int', (i + 1))
        cnt = jcast('int', 0)
        while (l < r):
            cur = jcast('int', queue[((_java_old_5 := l), (l := jcast('int', (l + (1)))), _java_old_5)[2]])
            cnt = jcast('int', (cnt + 1))
            for next in jcall(graph, 'get', cur):
                if (((_java_obj_6 := indegree), (_java_key_7 := next), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (-1)))))[3] == 0):
                    jset(queue, ((_java_old_9 := r), (r := jcast('int', (r + (1)))), _java_old_9)[2], next)
        return (queue if (cnt == numCourses) else jarray('int', [0]))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


