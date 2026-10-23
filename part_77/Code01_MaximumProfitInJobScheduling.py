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

# 规划兼职工作
# 你打算利用空闲时间来做兼职工作赚些零花钱，这里有n份兼职工作
# 每份工作预计从startTime[i]开始、endTime[i]结束，报酬为profit[i]
# 返回可以获得的最大报酬
# 注意，时间上出现重叠的 2 份工作不能同时进行
# 如果你选择的工作在时间X结束，那么你可以立刻进行在时间X开始的下一份工作
# 测试链接 : https://leetcode.cn/problems/maximum-profit-in-job-scheduling/
class Code01_MaximumProfitInJobScheduling:
    __java_fields__ = {'MAXN': 'MAXN', 'jobs': 'jobs', 'dp': 'dp'}
    MAXN = 0
    jobs = None
    dp = None
    @staticmethod
    def jobScheduling(startTime, endTime, profit):
        n = jcast('int', jget(startTime, 'length'))
        i = jcast('int', 0)
        while (i < n):
            jset(Code01_MaximumProfitInJobScheduling.jobs[i], 0, startTime[i])
            jset(Code01_MaximumProfitInJobScheduling.jobs[i], 1, endTime[i])
            jset(Code01_MaximumProfitInJobScheduling.jobs[i], 2, profit[i])
            i = jcast('int', (i + 1))
        # 工作按照结束时间从小到大排序
        jstatic('Arrays', 'sort', Code01_MaximumProfitInJobScheduling.jobs, 0, n, (lambda a, b: (a[1] - b[1])))
        Code01_MaximumProfitInJobScheduling.dp[0] = jcast('int', Code01_MaximumProfitInJobScheduling.jobs[0][2])
        i = jcast('int', 1)
        start = 0
        while (i < n):
            start = jcast('int', Code01_MaximumProfitInJobScheduling.jobs[i][0])
            Code01_MaximumProfitInJobScheduling.dp[i] = jcast('int', Code01_MaximumProfitInJobScheduling.jobs[i][2])
            if (Code01_MaximumProfitInJobScheduling.jobs[0][1] <= start):
                ((_java_obj_1 := Code01_MaximumProfitInJobScheduling.dp), (_java_key_2 := i), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), Code01_MaximumProfitInJobScheduling.dp[Code01_MaximumProfitInJobScheduling.find(jcast('int', (i - 1)), start)]))))[2]
            jset(Code01_MaximumProfitInJobScheduling.dp, i, jstatic('Math', 'max', Code01_MaximumProfitInJobScheduling.dp[i], Code01_MaximumProfitInJobScheduling.dp[jcast('int', (i - 1))]))
            i = jcast('int', (i + 1))
        return jcast('int', Code01_MaximumProfitInJobScheduling.dp[jcast('int', (n - 1))])

    # job[0...i]范围上，找到结束时间 <= start，最右的下标
    @staticmethod
    def find(i, start):
        i = jcast('int', i)
        start = jcast('int', start)
        ans = jcast('int', 0)
        l = jcast('int', 0)
        r = jcast('int', i)
        m = 0
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code01_MaximumProfitInJobScheduling.jobs[m][1] <= start):
                ans = jcast('int', m)
                l = jcast('int', jcast('int', jadd(m, 1)))
            else:
                r = jcast('int', jcast('int', (m - 1)))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_MaximumProfitInJobScheduling.MAXN = jcast('int', 50001)
Code01_MaximumProfitInJobScheduling.jobs = jarray('int', [Code01_MaximumProfitInJobScheduling.MAXN, 3])
Code01_MaximumProfitInJobScheduling.dp = jarray('int', [Code01_MaximumProfitInJobScheduling.MAXN])
