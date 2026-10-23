# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 计算等位时间
# 给定一个数组arr长度为n，表示n个服务员，每服务一个人的时间
# 给定一个正数m，表示有m个人等位，如果你是刚来的人，请问你需要等多久？
# 假设m远远大于n，比如n <= 10^3, m <= 10^9，该怎么做是最优解？
# 谷歌的面试，这个题连考了2个月
# 找不到测试链接，所以用对数器验证
class Code06_WaitingTime:
    __java_fields__ = {}
    # 堆模拟
    # 验证方法，不是重点
    # 如果m很大，该方法会超时
    # 时间复杂度O(m * log(n))，额外空间复杂度O(n)
    @staticmethod
    def waitingTime1(arr, m):
        m = jcast('int', m)
        # 一个一个对象int[]
        # [醒来时间，服务一个客人要多久]
        heap = jnew('PriorityQueue', (lambda a, b: (a[0] - b[0])))
        n = jcast('int', jget(arr, 'length'))
        i = jcast('int', 0)
        while (i < n):
            jcall(heap, 'add', jarray('int', [None], [0, arr[i]]))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < m):
            cur = jcall(heap, 'poll')
            cur[0] = jcast('int', jcast('int', jadd(cur[0], cur[1])))
            jcall(heap, 'add', cur)
            i = jcast('int', (i + 1))
        return jcast('int', jcall(heap, 'peek')[0])

    # 二分答案法
    # 最优解
    # 时间复杂度O(n * log(min * w))，额外空间复杂度O(1)
    @staticmethod
    def waitingTime2(arr, w):
        w = jcast('int', w)
        min = jcast('int', jget(Integer, 'MAX_VALUE'))
        for x in arr:
            min = jcast('int', jstatic('Math', 'min', min, x))
        ans = jcast('int', 0)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (min * w)))
        m = 0
        while (l <= r):
            # m中点，表示一定要让服务员工作的时间！
            m = jcast('int', jcast('int', jadd(l, jcast('int', (jcast('int', (r - l)) >> (1 & 31))))))
            # 能够给几个客人提供服务
            if (Code06_WaitingTime.f(arr, m) >= jcast('int', jadd(w, 1))):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    # 如果每个服务员工作time，可以接待几位客人（结束的、开始的客人都算）
    @staticmethod
    def f(arr, time):
        time = jcast('int', time)
        ans = jcast('int', 0)
        for num in arr:
            ans = jcast('int', jcast('int', jadd(ans, jcast('int', jadd(jcast('int', jdiv(time, num)), 1)))))
        return jcast('int', ans)

    # 对数器测试
    @staticmethod
    def main(args):
        jprint('测试开始', newline=True)
        N = jcast('int', 50)
        V = jcast('int', 30)
        M = jcast('int', 3000)
        testTime = jcast('int', 20000)
        i = jcast('int', 0)
        while (i < testTime):
            n = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * N)), 1)))
            arr = Code06_WaitingTime.randomArray(n, V)
            m = jcast('int', jcast('int', (jstatic('Math', 'random') * M)))
            ans1 = jcast('int', Code06_WaitingTime.waitingTime1(arr, m))
            ans2 = jcast('int', Code06_WaitingTime.waitingTime2(arr, m))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    # 对数器测试
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        arr = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            jset(arr, i, jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * v)), 1)))
            i = jcast('int', (i + 1))
        return arr

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code06_WaitingTime.main([])
