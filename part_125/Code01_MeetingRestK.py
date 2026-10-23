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

# 休息k分钟最大会议和
# 给定一个长度为n的数组arr，表示从早到晚发生的会议，各自召开的分钟数
# 当选择一个会议并参加之后，必须休息k分钟
# 返回能参加的会议时长最大累加和
# 比如，arr = { 200, 5, 6, 14, 7, 300 }，k = 15
# 最好的选择为，选择200分钟的会议，然后必须休息15分钟
# 那么接下来的5分钟、6分钟、14分钟的会议注定错过
# 然后放弃7分钟的会议，而选择参加300分钟的会议
# 最终返回500
# 1 <= n、arr[i]、k <= 10^6
# 来自真实大厂笔试，对数器验证
class Code01_MeetingRestK:
    __java_fields__ = {}
    # 不减少枚举的可能性
    # 时间复杂度O(n^2)
    @staticmethod
    def best1(arr, k):
        k = jcast('int', k)
        n = jcast('int', jget(arr, 'length'))
        dp = jarray('long', [jcast('int', jadd(n, 1))])
        i = jcast('int', jcast('int', (n - 1)))
        j = 0
        sum = 0
        while (i >= 0):
            j = jcast('int', jcast('int', jadd(i, 1)))
            sum = jcast('int', 0)
            while ((j < n) and (sum < k)):
                sum = jcast('int', jcast('int', jadd(sum, arr[j])))
                j = jcast('int', (j + 1))
            jset(dp, i, jstatic('Math', 'max', dp[jcast('int', jadd(i, 1))], jcast('long', jadd(dp[j], arr[i]))))
            i = jcast('int', (i - 1))
        return jcast('long', dp[0])

    # 利用预处理结构减少枚举的可能性
    # 时间复杂度O(n)
    @staticmethod
    def best2(arr, k):
        k = jcast('int', k)
        n = jcast('int', jget(arr, 'length'))
        jump = jarray('int', [n])
        # 窗口[l...r)，左闭右开，sum是窗口累加和
        i = jcast('int', 0)
        l = jcast('int', 1)
        r = jcast('int', 1)
        sum = jcast('int', 0)
        while (i < jcast('int', (n - 1))):
            while ((r < n) and (sum < k)):
                sum = jcast('int', jcast('int', jadd(sum, arr[((_java_old_1 := r), (r := jcast('int', (r + (1)))), _java_old_1)[2]])))
            jump[i] = jcast('int', r)
            sum = jcast('int', jcast('int', (sum - arr[l])))
            i = jcast('int', (i + 1))
            l = jcast('int', (l + 1))
        jump[jcast('int', (n - 1))] = jcast('int', n)
        dp = jarray('long', [jcast('int', jadd(n, 1))])
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            jset(dp, i, jstatic('Math', 'max', dp[jcast('int', jadd(i, 1))], jcast('long', jadd(dp[jump[i]], arr[i]))))
            i = jcast('int', (i - 1))
        return jcast('long', dp[0])

    # 为了测试
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

    # 为了测试
    @staticmethod
    def main(args):
        n = jcast('int', 1000)
        v = jcast('int', 3000)
        testTime = jcast('int', 10000)
        jprint('测试开始', newline=True)
        i = jcast('int', 1)
        while (i <= testTime):
            size = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            arr = Code01_MeetingRestK.randomArray(size, v)
            k = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * v)), 1)))
            ans1 = jcast('long', Code01_MeetingRestK.best1(arr, k))
            ans2 = jcast('long', Code01_MeetingRestK.best2(arr, k))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code01_MeetingRestK.main([])
