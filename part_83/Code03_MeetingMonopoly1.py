# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 会议必须独占时间段的最大会议数量
# 给定若干会议的开始、结束时间
# 你参加某个会议的期间，不能参加其他会议
# 返回你能参加的最大会议数量
# 同学找到了Leetcode的在线测试，题意类似
# 测试链接 :https://leetcode.cn/problems/non-overlapping-intervals/
class Code03_MeetingMonopoly1:
    __java_fields__ = {}
    # 测试链接 :https://leetcode.cn/problems/non-overlapping-intervals/
    # 测试链接中，问至少删除多少会议，可以让剩下的会议都不重合
    # 那么求出，最多能不重合的参加多少会议，然后 n - 这个数量，就是答案
    # 同时注意，测试链接中，会议的时间点范围[- 5 * 10 ^ 4 ~ + 5 * 10 ^ 4]
    # 其实就是课上讲的方法，稍微改动一下即可，改动的地方已经加上注释
    @staticmethod
    def eraseOverlapIntervals(meeting):
        jstatic('Arrays', 'sort', meeting, (lambda a, b: (a[1] - b[1])))
        n = jcast('int', jget(meeting, 'length'))
        ans = jcast('int', 0)
        # cur初始设置为-50001，因为题目数据状况如此
        i = jcast('int', 0)
        cur = jcast('int', jcast('int', (-50001)))
        while (i < n):
            if (cur <= meeting[i][0]):
                ans = jcast('int', (ans + 1))
                cur = jcast('int', meeting[i][1])
            i = jcast('int', (i + 1))
        # 会议总数 - 参加的最大会议数量
        return jcast('int', jcast('int', (n - ans)))

    # 暴力方法
    # 为了验证
    # 时间复杂度O(n!)
    @staticmethod
    def maxMeeting1(meeting):
        return jcast('int', Code03_MeetingMonopoly1.f(meeting, jget(meeting, 'length'), 0))

    # 把所有会议全排列
    # 其中一定有安排会议次数最多的排列
    @staticmethod
    def f(meeting, n, i):
        n = jcast('int', n)
        i = jcast('int', i)
        ans = jcast('int', 0)
        if (i == n):
            j = jcast('int', 0)
            cur = jcast('int', jcast('int', (-1)))
            while (j < n):
                if (cur <= meeting[j][0]):
                    ans = jcast('int', (ans + 1))
                    cur = jcast('int', meeting[j][1])
                j = jcast('int', (j + 1))
        else:
            j = jcast('int', i)
            while (j < n):
                Code03_MeetingMonopoly1.swap(meeting, i, j)
                ans = jcast('int', jstatic('Math', 'max', ans, Code03_MeetingMonopoly1.f(meeting, n, jcast('int', jadd(i, 1)))))
                Code03_MeetingMonopoly1.swap(meeting, i, j)
                j = jcast('int', (j + 1))
        return jcast('int', ans)

    @staticmethod
    def swap(meeting, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = meeting[i]
        meeting[i] = meeting[j]
        meeting[j] = tmp

    # 正式方法
    # 时间复杂度O(n*logn)
    @staticmethod
    def maxMeeting2(meeting):
        # meeting[i][0] : i号会议开始时间
        # meeting[i][1] : i号会议结束时间
        jstatic('Arrays', 'sort', meeting, (lambda a, b: (a[1] - b[1])))
        n = jcast('int', jget(meeting, 'length'))
        ans = jcast('int', 0)
        i = jcast('int', 0)
        cur = jcast('int', jcast('int', (-1)))
        while (i < n):
            if (cur <= meeting[i][0]):
                ans = jcast('int', (ans + 1))
                cur = jcast('int', meeting[i][1])
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 为了验证
    # 生成随机会议
    @staticmethod
    def randomMeeting(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        ans = jarray('int', [n, 2])
        i = jcast('int', 0)
        a = 0
        b = 0
        while (i < n):
            a = jcast('int', jcast('int', (jstatic('Math', 'random') * m)))
            b = jcast('int', jcast('int', (jstatic('Math', 'random') * m)))
            if (a == b):
                jset(ans[i], 0, a)
                jset(ans[i], 1, jcast('int', jadd(a, 1)))
            else:
                jset(ans[i], 0, jstatic('Math', 'min', a, b))
                jset(ans[i], 1, jstatic('Math', 'max', a, b))
            i = jcast('int', (i + 1))
        return ans

    # 对数器
    # 为了验证
    @staticmethod
    def main(args):
        N = jcast('int', 10)
        M = jcast('int', 12)
        testTimes = jcast('int', 2000)
        jprint('测试开始', newline=True)
        i = jcast('int', 1)
        while (i <= testTimes):
            n = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * N)), 1)))
            meeting = Code03_MeetingMonopoly1.randomMeeting(n, M)
            ans1 = jcast('int', Code03_MeetingMonopoly1.maxMeeting1(meeting))
            ans2 = jcast('int', Code03_MeetingMonopoly1.maxMeeting2(meeting))
            if (ans1 != ans2):
                # 如果出错了
                # 可以增加打印行为找到一组出错的例子
                # 然后去debug
                jprint('出错了！', newline=True)
            if (jcast('int', jmod(i, 100)) == 0):
                jprint(jadd(jadd('测试到第', i), '组'), newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code03_MeetingMonopoly1.main([])
