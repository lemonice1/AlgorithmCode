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

# 并行课程 III
# 给你一个整数 n ，表示有 n 节课，课程编号从 1 到 n
# 同时给你一个二维整数数组 relations ，
# 其中 relations[j] = [prevCoursej, nextCoursej]
# 表示课程 prevCoursej 必须在课程 nextCoursej 之前 完成（先修课的关系）
# 同时给你一个下标从 0 开始的整数数组 time
# 其中 time[i] 表示完成第 (i+1) 门课程需要花费的 月份 数。
# 请你根据以下规则算出完成所有课程所需要的 最少 月份数：
# 如果一门课的所有先修课都已经完成，你可以在 任意 时间开始这门课程。
# 你可以 同时 上 任意门课程 。请你返回完成所有课程所需要的 最少 月份数。
# 注意：测试数据保证一定可以完成所有课程（也就是先修课的关系构成一个有向无环图）
# 测试链接 : https://leetcode.cn/problems/parallel-courses-iii/
class Code03_ParallelCoursesIII:
    __java_fields__ = {}
    @staticmethod
    def minimumTime(n, relations, time):
        n = jcast('int', n)
        # 点 : 1....n
        graph = jnew('ArrayList')
        i = jcast('int', 0)
        while (i <= n):
            jcall(graph, 'add', jnew('ArrayList'))
            i = jcast('int', (i + 1))
        indegree = jarray('int', [jcast('int', jadd(n, 1))])
        for edge in relations:
            jcall(jcall(graph, 'get', edge[0]), 'add', edge[1])
            ((_java_obj_1 := indegree), (_java_key_2 := edge[1]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
        queue = jarray('int', [n])
        l = jcast('int', 0)
        r = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= n):
            if (indegree[i] == 0):
                jset(queue, ((_java_old_4 := r), (r := jcast('int', (r + (1)))), _java_old_4)[2], i)
            i = jcast('int', (i + 1))
        cost = jarray('int', [jcast('int', jadd(n, 1))])
        ans = jcast('int', 0)
        while (l < r):
            cur = jcast('int', queue[((_java_old_5 := l), (l := jcast('int', (l + (1)))), _java_old_5)[2]])
            # 1 : time[0]
            # x : time[x-1]
            cost[cur] = jcast('int', jcast('int', jadd(cost[cur], time[jcast('int', (cur - 1))])))
            ans = jcast('int', jstatic('Math', 'max', ans, cost[cur]))
            for next in jcall(graph, 'get', cur):
                jset(cost, next, jstatic('Math', 'max', cost[next], cost[cur]))
                if (((_java_obj_6 := indegree), (_java_key_7 := next), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (-1)))))[3] == 0):
                    jset(queue, ((_java_old_9 := r), (r := jcast('int', (r + (1)))), _java_old_9)[2], next)
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


