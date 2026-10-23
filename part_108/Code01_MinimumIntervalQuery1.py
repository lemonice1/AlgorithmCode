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
class Code01_MinimumIntervalQuery1:
    __java_fields__ = {}
    # 堆结构是现成结构
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
        # 0 : 长度
        # 1 : 影响到的位置
        heap = jnew('PriorityQueue', (lambda a, b: (a[0] - b[0])))
        ans = jarray('int', [m])
        i = jcast('int', 0)
        j = jcast('int', 0)
        while (i < m):
            while ((j < n) and (intervals[j][0] <= ques[i][0])):
                jcall(heap, 'add', jarray('int', [None], [jcast('int', jadd(jcast('int', (intervals[j][1] - intervals[j][0])), 1)), intervals[j][1]]))
                j = jcast('int', (j + 1))
            while ((not jcall(heap, 'isEmpty')) and (jcall(heap, 'peek')[1] < ques[i][0])):
                jcall(heap, 'poll')
            if (not jcall(heap, 'isEmpty')):
                jset(ans, ques[i][1], jcall(heap, 'peek')[0])
            else:
                jset(ans, ques[i][1], jcast('int', (-1)))
            i = jcast('int', (i + 1))
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


