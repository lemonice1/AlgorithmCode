# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 参加会议II
# 给定n个会议，每个会议有开始时间、结束时间、收益三个值
# 参加会议就能得到收益，但是同一时间只能参加一个会议
# 一共能参加k个会议，如果选择参加某个会议，那么必须完整的参加完这个会议
# 会议结束日期是包含在会议内的，一个会议的结束时间等于另一个会议的开始时间，不能两个会议都参加
# 返回能得到的会议价值最大和
# 1 <= n * k <= 10^6
# 1 <= 开始时间、结束时间 <= 10^9
# 1 <= 收益 <= 10^6
# 测试链接 : https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended-ii/
class Code01_MaximumNumberOfEvents:
    __java_fields__ = {}
    # events[i][0] : 开始时间
    # events[i][1] : 结束时间
    # events[i][2] : 收益
    @staticmethod
    def maxValue(events, k):
        k = jcast('int', k)
        n = jcast('int', jget(events, 'length'))
        jstatic('Arrays', 'sort', events, (lambda a, b: (a[1] - b[1])))
        # dp[i][j] : 0..i范围上最多选j个会议召开，最大收益是多少
        dp = jarray('int', [n, jcast('int', jadd(k, 1))])
        j = jcast('int', 1)
        while (j <= k):
            jset(dp[0], j, events[0][2])
            j = jcast('int', (j + 1))
        i = jcast('int', 1)
        pre = 0
        while (i < n):
            pre = jcast('int', Code01_MaximumNumberOfEvents.find(events, jcast('int', (i - 1)), events[i][0]))
            j = jcast('int', 1)
            while (j <= k):
                jset(dp[i], j, jstatic('Math', 'max', dp[jcast('int', (i - 1))][j], jcast('int', jadd((0 if (pre == jcast('int', (-1))) else dp[pre][jcast('int', (j - 1))]), events[i][2]))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[jcast('int', (n - 1))][k])

    # 0...i范围上的会议，根据结束日期排序了
    # 找到结束时间<s，最右的会议编号
    # 如果不存在这样的会议返回-1
    @staticmethod
    def find(events, i, s):
        i = jcast('int', i)
        s = jcast('int', s)
        l = jcast('int', 0)
        r = jcast('int', i)
        mid = 0
        ans = jcast('int', jcast('int', (-1)))
        while (l <= r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (events[mid][1] < s):
                ans = jcast('int', mid)
                l = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                r = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


