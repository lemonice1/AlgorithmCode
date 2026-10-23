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

# 包含每个查询的最小区间
# 给你一个二维整数数组intervals，其中intervals[i] = [l, r]
# 表示第i个区间开始于l，结束于r，区间的长度是r-l+1
# 给你一个整数数组queries，queries[i]表示要查询的位置
# 答案是所有包含queries[i]的区间中，最小长度的区间是多长
# 返回数组对应查询的所有答案，如果不存在这样的区间那么答案是-1
# 测试链接 : https://leetcode.cn/problems/minimum-interval-to-include-each-query/
class Code01_MinimumIntervalQuery2:
    __java_fields__ = {'MAXN': 'MAXN', 'heap': 'heap', 'heapSize': 'heapSize'}
    # 堆结构由自己实现
    @staticmethod
    def minInterval(intervals, queries):
        n = jcast('int', jget(intervals, 'length'))
        m = jcast('int', jget(queries, 'length'))
        jstatic('Arrays', 'sort', intervals, (lambda a, b: (a[0] - b[0])))
        ques = jarray('int', [m, 2])
        i = jcast('int', 0)
        while (i < m):
            jset(ques[i], 0, queries[i])
            jset(ques[i], 1, i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', ques, (lambda a, b: (a[0] - b[0])))
        Code01_MinimumIntervalQuery2.heapSize = jcast('int', 0)
        ans = jarray('int', [m])
        i = jcast('int', 0)
        j = jcast('int', 0)
        while (i < m):
            while ((j < n) and (intervals[j][0] <= ques[i][0])):
                Code01_MinimumIntervalQuery2.push(jcast('int', jadd(jcast('int', (intervals[j][1] - intervals[j][0])), 1)), intervals[j][1])
                j = jcast('int', (j + 1))
            while ((not Code01_MinimumIntervalQuery2.isEmpty()) and (Code01_MinimumIntervalQuery2.peekEnd() < ques[i][0])):
                Code01_MinimumIntervalQuery2.poll()
            if (not Code01_MinimumIntervalQuery2.isEmpty()):
                jset(ans, ques[i][1], Code01_MinimumIntervalQuery2.peekLength())
            else:
                jset(ans, ques[i][1], jcast('int', (-1)))
            i = jcast('int', (i + 1))
        return ans

    MAXN = 0
    heap = None
    heapSize = 0
    @staticmethod
    def isEmpty():
        return jcast('boolean', (Code01_MinimumIntervalQuery2.heapSize == 0))

    @staticmethod
    def peekLength():
        return jcast('int', Code01_MinimumIntervalQuery2.heap[0][0])

    @staticmethod
    def peekEnd():
        return jcast('int', Code01_MinimumIntervalQuery2.heap[0][1])

    @staticmethod
    def push(h, e):
        h = jcast('int', h)
        e = jcast('int', e)
        jset(Code01_MinimumIntervalQuery2.heap[Code01_MinimumIntervalQuery2.heapSize], 0, h)
        jset(Code01_MinimumIntervalQuery2.heap[Code01_MinimumIntervalQuery2.heapSize], 1, e)
        Code01_MinimumIntervalQuery2.heapInsert(((_java_obj_1 := Code01_MinimumIntervalQuery2), (_java_key_2 := 'heapSize'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def poll():
        Code01_MinimumIntervalQuery2.swap(0, ((_java_obj_4 := Code01_MinimumIntervalQuery2), (_java_key_5 := 'heapSize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))))[3])
        Code01_MinimumIntervalQuery2.heapify(0)

    @staticmethod
    def heapInsert(i):
        i = jcast('int', i)
        while (Code01_MinimumIntervalQuery2.heap[i][0] < Code01_MinimumIntervalQuery2.heap[jcast('int', jdiv(jcast('int', (i - 1)), 2))][0]):
            Code01_MinimumIntervalQuery2.swap(i, jcast('int', jdiv(jcast('int', (i - 1)), 2)))
            i = jcast('int', jcast('int', jdiv(jcast('int', (i - 1)), 2)))

    @staticmethod
    def heapify(i):
        i = jcast('int', i)
        l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
        while (l < Code01_MinimumIntervalQuery2.heapSize):
            try:
                best = jcast('int', (jcast('int', jadd(l, 1)) if ((jcast('int', jadd(l, 1)) < Code01_MinimumIntervalQuery2.heapSize) and (Code01_MinimumIntervalQuery2.heap[jcast('int', jadd(l, 1))][0] < Code01_MinimumIntervalQuery2.heap[l][0])) else l))
                best = jcast('int', (best if (Code01_MinimumIntervalQuery2.heap[best][0] < Code01_MinimumIntervalQuery2.heap[i][0]) else i))
                if (best == i):
                    raise JBreak(None)
                Code01_MinimumIntervalQuery2.swap(best, i)
                i = jcast('int', best)
                l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = Code01_MinimumIntervalQuery2.heap[i]
        Code01_MinimumIntervalQuery2.heap[i] = Code01_MinimumIntervalQuery2.heap[j]
        Code01_MinimumIntervalQuery2.heap[j] = tmp

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_MinimumIntervalQuery2.MAXN = jcast('int', 100001)
Code01_MinimumIntervalQuery2.heap = jarray('int', [Code01_MinimumIntervalQuery2.MAXN, 2])
Code01_MinimumIntervalQuery2.heapSize = jcast('int', 0)
