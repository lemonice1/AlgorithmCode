# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 同时运行N台电脑的最长时间
# 你有 n 台电脑。给你整数 n 和一个下标从 0 开始的整数数组 batteries
# 其中第 i 个电池可以让一台电脑 运行 batteries[i] 分钟
# 你想使用这些电池让 全部 n 台电脑 同时 运行。
# 一开始，你可以给每台电脑连接 至多一个电池
# 然后在任意整数时刻，你都可以将一台电脑与它的电池断开连接，并连接另一个电池，你可以进行这个操作 任意次
# 新连接的电池可以是一个全新的电池，也可以是别的电脑用过的电池
# 断开连接和连接新的电池不会花费任何时间。
# 注意，你不能给电池充电。
# 请你返回你可以让 n 台电脑同时运行的 最长 分钟数。
# 测试链接 : https://leetcode.cn/problems/maximum-running-time-of-n-computers/
class Code05_MaximumRunningTimeOfNComputers:
    __java_fields__ = {}
    # 单纯的二分答案法
    # 提交时把函数名改为maxRunTime
    # 时间复杂度O(n * log(sum))，额外空间复杂度O(1)
    @staticmethod
    def maxRunTime1(num, arr):
        num = jcast('int', num)
        sum = jcast('long', 0)
        for x in arr:
            sum = jcast('long', jcast('long', jadd(sum, x)))
        ans = jcast('long', 0)
        # [0, sum]，不停二分
        l = jcast('long', 0)
        r = jcast('long', sum)
        m = 0
        while (l <= r):
            # m中点，让num台电脑共同运行m分钟，能不能做到
            m = jcast('long', jcast('long', jadd(l, jcast('long', (jcast('long', (r - l)) >> (1 & 63))))))
            if Code05_MaximumRunningTimeOfNComputers.f1(arr, num, m):
                ans = jcast('long', m)
                l = jcast('long', jcast('long', jadd(m, 1)))
            else:
                r = jcast('long', jcast('long', (m - 1)))
        return jcast('long', ans)

    # 让num台电脑共同运行time分钟，能不能做到
    @staticmethod
    def f1(arr, num, time):
        num = jcast('int', num)
        time = jcast('long', time)
        # 碎片电量总和
        sum = jcast('long', 0)
        for x in arr:
            if (x > time):
                num = jcast('int', (num - 1))
            else:
                # x <= time，是碎片电池
                sum = jcast('long', jcast('long', jadd(sum, x)))
            if (sum >= jcast('long', (jcast('long', num) * time))):
                # 碎片电量 >= 台数 * 要求
                return jcast('boolean', True)
        return jcast('boolean', False)

    # 二分答案法 + 增加分析(贪心)
    # 提交时把函数名改为maxRunTime
    # 时间复杂度O(n * log(max))，额外空间复杂度O(1)
    @staticmethod
    def maxRunTime2(num, arr):
        num = jcast('int', num)
        max = jcast('int', 0)
        sum = jcast('long', 0)
        for x in arr:
            max = jcast('int', jstatic('Math', 'max', max, x))
            sum = jcast('long', jcast('long', jadd(sum, x)))
        # 就是增加了这里的逻辑
        if (sum > jcast('long', (jcast('long', max) * num))):
            # 所有电池的最大电量是max
            # 如果此时sum > (long) max * num，
            # 说明 : 最终的供电时间一定在 >= max，而如果最终的供电时间 >= max
            # 说明 : 对于最终的答案X来说，所有电池都是课上讲的"碎片拼接"的概念
            # 那么寻找 ? * num <= sum 的情况中，尽量大的 ? 即可
            # 即sum / num
            return jcast('long', jcast('long', jdiv(sum, num)))
        # 最终的供电时间一定在 < max范围上
        # [0, sum]二分范围，可能定的比较粗，虽然不影响，但毕竟是有点慢
        # [0, max]二分范围！更精细的范围，二分次数会变少
        ans = jcast('int', 0)
        l = jcast('int', 0)
        r = jcast('int', max)
        m = 0
        while (l <= r):
            m = jcast('int', jcast('int', jadd(l, jcast('int', (jcast('int', (r - l)) >> (1 & 31))))))
            if Code05_MaximumRunningTimeOfNComputers.f2(arr, num, m):
                ans = jcast('int', m)
                l = jcast('int', jcast('int', jadd(m, 1)))
            else:
                r = jcast('int', jcast('int', (m - 1)))
        return jcast('long', ans)

    @staticmethod
    def f2(arr, num, time):
        num = jcast('int', num)
        time = jcast('int', time)
        # 碎片电量总和
        sum = jcast('long', 0)
        for x in arr:
            if (x > time):
                num = jcast('int', (num - 1))
            else:
                sum = jcast('long', jcast('long', jadd(sum, x)))
            if (sum >= jcast('long', (jcast('long', num) * time))):
                return jcast('boolean', True)
        return jcast('boolean', False)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


