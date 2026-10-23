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

# 你可以安排的最多任务数目
# 给你 n 个任务和 m 个工人。每个任务需要一定的力量值才能完成
# 需要的力量值保存在下标从 0 开始的整数数组 tasks 中，
# 第i个任务需要 tasks[i] 的力量才能完成
# 每个工人的力量值保存在下标从 0 开始的整数数组workers中，
# 第j个工人的力量值为 workers[j]
# 每个工人只能完成一个任务，且力量值需要大于等于该任务的力量要求值，即workers[j]>=tasks[i]
# 除此以外，你还有 pills 个神奇药丸，可以给 一个工人的力量值 增加 strength
# 你可以决定给哪些工人使用药丸，但每个工人 最多 只能使用 一片 药丸
# 给你下标从 0 开始的整数数组tasks 和 workers 以及两个整数 pills 和 strength
# 请你返回 最多 有多少个任务可以被完成。
# 测试链接 : https://leetcode.cn/problems/maximum-number-of-tasks-you-can-assign/
class Code03_MaximumNumberOfTasksYouCanAssign:
    __java_fields__ = {'tasks': 'tasks', 'workers': 'workers', 'MAXN': 'MAXN', 'deque': 'deque', 'h': 'h', 't': 't'}
    tasks = None
    workers = None
    MAXN = 0
    deque = None
    h = 0
    t = 0
    # 两个数组排序 : O(n * logn) + O(m * logm)
    # 二分答案的过程，每次二分都用一下双端队列 : O((n和m最小值)*log(n和m最小值))
    # 最复杂的反而是排序的过程了，所以时间复杂度O(n * logn) + O(m * logm)
    @staticmethod
    def maxTaskAssign(ts, ws, pills, strength):
        pills = jcast('int', pills)
        strength = jcast('int', strength)
        Code03_MaximumNumberOfTasksYouCanAssign.tasks = ts
        Code03_MaximumNumberOfTasksYouCanAssign.workers = ws
        jstatic('Arrays', 'sort', Code03_MaximumNumberOfTasksYouCanAssign.tasks)
        jstatic('Arrays', 'sort', Code03_MaximumNumberOfTasksYouCanAssign.workers)
        tsize = jcast('int', jget(Code03_MaximumNumberOfTasksYouCanAssign.tasks, 'length'))
        wsize = jcast('int', jget(Code03_MaximumNumberOfTasksYouCanAssign.workers, 'length'))
        ans = jcast('int', 0)
        # [0, Math.min(tsize, wsize)]
        l = jcast('int', 0)
        r = jcast('int', jstatic('Math', 'min', tsize, wsize))
        m = 0
        while (l <= r):
            # m中点，一定要完成的任务数量
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if Code03_MaximumNumberOfTasksYouCanAssign.f(0, jcast('int', (m - 1)), jcast('int', (wsize - m)), jcast('int', (wsize - 1)), strength, pills):
                ans = jcast('int', m)
                l = jcast('int', jcast('int', jadd(m, 1)))
            else:
                r = jcast('int', jcast('int', (m - 1)))
        return jcast('int', ans)

    # tasks[tl....tr]需要力量最小的几个任务
    # workers[wl....wr]力量值最大的几个工人
    # 药效是s，一共有的药pills个
    # 在药的数量不超情况下，能不能每个工人都做一个任务
    @staticmethod
    def f(tl, tr, wl, wr, s, pills):
        tl = jcast('int', tl)
        tr = jcast('int', tr)
        wl = jcast('int', wl)
        wr = jcast('int', wr)
        s = jcast('int', s)
        pills = jcast('int', pills)
        Code03_MaximumNumberOfTasksYouCanAssign.h = jcast('int', jset(Code03_MaximumNumberOfTasksYouCanAssign, 't', 0))
        # 已经使用的药的数量
        cnt = jcast('int', 0)
        i = jcast('int', wl)
        j = jcast('int', tl)
        while (i <= wr):
            # i : 工人的编号
            # j : 任务的编号
            while ((j <= tr) and (Code03_MaximumNumberOfTasksYouCanAssign.tasks[j] <= Code03_MaximumNumberOfTasksYouCanAssign.workers[i])):
                # 工人不吃药的情况下，去解锁任务
                jset(Code03_MaximumNumberOfTasksYouCanAssign.deque, ((_java_obj_1 := Code03_MaximumNumberOfTasksYouCanAssign), (_java_key_2 := 't'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], j)
                j = jcast('int', (j + 1))
            if ((Code03_MaximumNumberOfTasksYouCanAssign.h < Code03_MaximumNumberOfTasksYouCanAssign.t) and (Code03_MaximumNumberOfTasksYouCanAssign.tasks[Code03_MaximumNumberOfTasksYouCanAssign.deque[Code03_MaximumNumberOfTasksYouCanAssign.h]] <= Code03_MaximumNumberOfTasksYouCanAssign.workers[i])):
                Code03_MaximumNumberOfTasksYouCanAssign.h = jcast('int', (Code03_MaximumNumberOfTasksYouCanAssign.h + 1))
            else:
                # 吃药之后的逻辑
                while ((j <= tr) and (Code03_MaximumNumberOfTasksYouCanAssign.tasks[j] <= jcast('int', jadd(Code03_MaximumNumberOfTasksYouCanAssign.workers[i], s)))):
                    jset(Code03_MaximumNumberOfTasksYouCanAssign.deque, ((_java_obj_4 := Code03_MaximumNumberOfTasksYouCanAssign), (_java_key_5 := 't'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], j)
                    j = jcast('int', (j + 1))
                if (Code03_MaximumNumberOfTasksYouCanAssign.h < Code03_MaximumNumberOfTasksYouCanAssign.t):
                    cnt = jcast('int', (cnt + 1))
                    Code03_MaximumNumberOfTasksYouCanAssign.t = jcast('int', (Code03_MaximumNumberOfTasksYouCanAssign.t - 1))
                else:
                    return jcast('boolean', False)
            i = jcast('int', (i + 1))
        return jcast('boolean', (cnt <= pills))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_MaximumNumberOfTasksYouCanAssign.tasks = None
Code03_MaximumNumberOfTasksYouCanAssign.workers = None
Code03_MaximumNumberOfTasksYouCanAssign.MAXN = jcast('int', 50001)
Code03_MaximumNumberOfTasksYouCanAssign.deque = jarray('int', [Code03_MaximumNumberOfTasksYouCanAssign.MAXN])
Code03_MaximumNumberOfTasksYouCanAssign.h = jcast('int', 0)
Code03_MaximumNumberOfTasksYouCanAssign.t = jcast('int', 0)
