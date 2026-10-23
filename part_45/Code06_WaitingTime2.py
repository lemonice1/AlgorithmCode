# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 完成旅途的最少时间(题目6的在线测试)
# 有同学找到了在线测试链接，和课上讲的题目6几乎是一个意思，但是有细微差别
# 实现的代码，除了一些变量需要改成long类型之外，仅有两处关键逻辑不同，都打上了注释
# 除此之外，和课上讲的题目6的实现，再无区别
# 可以仔细阅读如下测试链接里的题目，重点关注此题和题目6，在题意上的差别
# 测试链接 : https://leetcode.cn/problems/minimum-time-to-complete-trips/
class Code06_WaitingTime2:
    __java_fields__ = {}
    @staticmethod
    def minimumTime(arr, w):
        w = jcast('int', w)
        min = jcast('int', jget(Integer, 'MAX_VALUE'))
        for x in arr:
            min = jcast('int', jstatic('Math', 'min', min, x))
        ans = jcast('long', 0)
        l = jcast('long', 0)
        r = jcast('long', jcast('long', (jcast('long', min) * w)))
        m = 0
        while (l <= r):
            m = jcast('long', jcast('long', jadd(l, jcast('long', (jcast('long', (r - l)) >> (1 & 63))))))
            # 这里逻辑和课上讲的不同
            # 课上讲的题意，是需要等多少人才能获得服务，你是第w+1个
            # 在线测试的题意，是需要完成w趟旅行
            if (Code06_WaitingTime2.f(arr, m) >= w):
                ans = jcast('long', m)
                r = jcast('long', jcast('long', (m - 1)))
            else:
                l = jcast('long', jcast('long', jadd(m, 1)))
        return jcast('long', ans)

    @staticmethod
    def f(arr, time):
        time = jcast('long', time)
        ans = jcast('long', 0)
        for num in arr:
            # 这里逻辑和课上讲的不同
            # 课上讲的题意，计算time时间内，(完成 + 开始)服务的人数，需要+1
            # 在线测试的题意，计算time时间内，能完成多少旅行，不需要+1
            ans = jcast('long', jcast('long', jadd(ans, jcast('long', jdiv(time, num)))))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


