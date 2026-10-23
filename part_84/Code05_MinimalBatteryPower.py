# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 执行所有任务的最少初始电量
# 每一个任务有两个参数，需要耗费的电量、至少多少电量才能开始这个任务
# 返回手机至少需要多少的初始电量，才能执行完所有的任务
# 测试链接 : https://leetcode.cn/problems/minimum-initial-energy-to-finish-tasks/
class Code05_MinimalBatteryPower:
    __java_fields__ = {}
    # 在线评测入口对应 minimumEffort 方法，提交时需保留相应的接口
    # 测试链接 : https://leetcode.cn/problems/minimum-initial-energy-to-finish-tasks/
    @staticmethod
    def minimumEffort(tasks):
        jstatic('Arrays', 'sort', tasks, (lambda a, b: ((b[0] - b[1]) - (a[0] - a[1]))))
        ans = jcast('int', 0)
        for job in tasks:
            ans = jcast('int', jstatic('Math', 'max', jcast('int', jadd(ans, job[0])), job[1]))
        return jcast('int', ans)

    # 暴力递归
    # 为了验证
    # 时间复杂度O(n!)
    # 得到所有排列
    # 其中一定有返还电量最小的排列
    @staticmethod
    def atLeast1(jobs):
        return jcast('int', Code05_MinimalBatteryPower.f1(jobs, jget(jobs, 'length'), 0))

    @staticmethod
    def f1(jobs, n, i):
        n = jcast('int', n)
        i = jcast('int', i)
        if (i == n):
            ans = jcast('int', 0)
            for job in jobs:
                ans = jcast('int', jstatic('Math', 'max', job[1], jcast('int', jadd(ans, job[0]))))
            return jcast('int', ans)
        else:
            ans = jcast('int', jget(Integer, 'MAX_VALUE'))
            j = jcast('int', i)
            while (j < n):
                Code05_MinimalBatteryPower.swap(jobs, i, j)
                ans = jcast('int', jstatic('Math', 'min', ans, Code05_MinimalBatteryPower.f1(jobs, n, jcast('int', jadd(i, 1)))))
                Code05_MinimalBatteryPower.swap(jobs, i, j)
                j = jcast('int', (j + 1))
            return jcast('int', ans)

    @staticmethod
    def swap(jobs, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jobs[i]
        jobs[i] = jobs[j]
        jobs[j] = tmp

    # 正式方法
    # 贪心
    # 时间复杂度O(n * logn)
    @staticmethod
    def atLeast2(jobs):
        # jobs[i][0] : 耗费
        # jobs[i][1] : 至少电量
        # 消耗电量 - 至少电量，越大的任务，越先倒推
        jstatic('Arrays', 'sort', jobs, (lambda a, b: ((b[0] - b[1]) - (a[0] - a[1]))))
        ans = jcast('int', 0)
        for job in jobs:
            ans = jcast('int', jstatic('Math', 'max', jcast('int', jadd(ans, job[0])), job[1]))
        return jcast('int', ans)

    # 为了验证
    @staticmethod
    def randomJobs(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        jobs = jarray('int', [n, 2])
        i = jcast('int', 0)
        while (i < n):
            jset(jobs[i], 0, jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * v)), 1)))
            jset(jobs[i], 1, jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * v)), 1)))
            i = jcast('int', (i + 1))
        return jobs

    # 为了验证
    @staticmethod
    def main(args):
        N = jcast('int', 10)
        V = jcast('int', 20)
        testTimes = jcast('int', 2000)
        jprint('测试开始', newline=True)
        i = jcast('int', 1)
        while (i <= testTimes):
            n = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * N)), 1)))
            jobs = Code05_MinimalBatteryPower.randomJobs(n, V)
            ans1 = jcast('int', Code05_MinimalBatteryPower.atLeast1(jobs))
            ans2 = jcast('int', Code05_MinimalBatteryPower.atLeast2(jobs))
            if (ans1 != ans2):
                jprint('出错了！', newline=True)
            if (jcast('int', jmod(i, 100)) == 0):
                jprint(jadd(jadd('测试到第', i), '组'), newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code05_MinimalBatteryPower.main([])
