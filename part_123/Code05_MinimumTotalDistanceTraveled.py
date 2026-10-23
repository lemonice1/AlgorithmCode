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

# 最小移动总距离
# 所有工厂和机器人都分布在x轴上
# 给定长度为n的二维数组factory，factory[i][0]为i号工厂的位置，factory[i][1]为容量
# 给定长度为m的一维数组robot，robot[j]为第j个机器人的位置
# 每个工厂所在的位置都不同，每个机器人所在的位置都不同，机器人到工厂的距离为位置差的绝对值
# 所有机器人都是坏的，但是机器人可以去往任何工厂进行修理，但是不能超过某个工厂的容量
# 测试数据保证所有机器人都可以被维修，返回所有机器人移动的最小总距离
# 1 <= n、m <= 100
# -10^9 <= factory[i][0]、robot[j] <= +10^9
# 0 <= factory[i][1] <= m
# 测试链接 : https://leetcode.cn/problems/minimum-total-distance-traveled/
class Code05_MinimumTotalDistanceTraveled:
    __java_fields__ = {'NA': 'NA', 'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'fac': 'fac', 'rob': 'rob', 'dp': 'dp', 'sum': 'sum', 'queue': 'queue', 'l': 'l', 'r': 'r'}
    NA = 0
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    # 工厂下标从1开始，fac[i][0]表示位置，fac[i][1]表示容量
    fac = None
    # 机器人下标从1开始，rob[i]表示位置
    rob = None
    # dp[i][j] : 1...i工厂去修理1...j号机器人，最短总距离是多少
    dp = None
    # 前缀和数组
    sum = None
    # 单调队列
    queue = None
    l = 0
    r = 0
    @staticmethod
    def build(factory, robot):
        # 工厂和机器人都根据所在位置排序
        jstatic('Arrays', 'sort', factory, (lambda a, b: (a[0] - b[0])))
        jcall(robot, 'sort', (lambda a, b: (a - b)))
        Code05_MinimumTotalDistanceTraveled.n = jcast('int', jget(factory, 'length'))
        Code05_MinimumTotalDistanceTraveled.m = jcast('int', jcall(robot, 'size'))
        # 让工厂和机器人的下标都从1开始
        i = jcast('int', 1)
        while (i <= Code05_MinimumTotalDistanceTraveled.n):
            jset(Code05_MinimumTotalDistanceTraveled.fac[i], 0, factory[jcast('int', (i - 1))][0])
            jset(Code05_MinimumTotalDistanceTraveled.fac[i], 1, factory[jcast('int', (i - 1))][1])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_MinimumTotalDistanceTraveled.m):
            jset(Code05_MinimumTotalDistanceTraveled.rob, i, jcall(robot, 'get', jcast('int', (i - 1))))
            i = jcast('int', (i + 1))
        # dp初始化
        j = jcast('int', 1)
        while (j <= Code05_MinimumTotalDistanceTraveled.m):
            jset(Code05_MinimumTotalDistanceTraveled.dp[0], j, Code05_MinimumTotalDistanceTraveled.NA)
            j = jcast('int', (j + 1))

    # 最优解O(n * m)
    # 其他题解都没有达到这个最优复杂度
    @staticmethod
    def minimumTotalDistance(robot, factory):
        Code05_MinimumTotalDistanceTraveled.build(factory, robot)
        i = jcast('int', 1)
        cap = 0
        while (i <= Code05_MinimumTotalDistanceTraveled.n):
            # i号工厂的容量
            cap = jcast('int', Code05_MinimumTotalDistanceTraveled.fac[i][1])
            # sum[j]表示
            # 1号机器人去往i号工厂的距离
            # 2号机器人去往i号工厂的距离
            # ...
            # j号机器人去往i号工厂的距离
            # 上面全加起来，也就是前缀和的概念
            j = jcast('int', 1)
            while (j <= Code05_MinimumTotalDistanceTraveled.m):
                jset(Code05_MinimumTotalDistanceTraveled.sum, j, jcast('long', jadd(Code05_MinimumTotalDistanceTraveled.sum[jcast('int', (j - 1))], Code05_MinimumTotalDistanceTraveled.dist(i, j))))
                j = jcast('int', (j + 1))
            Code05_MinimumTotalDistanceTraveled.l = jcast('int', jset(Code05_MinimumTotalDistanceTraveled, 'r', 0))
            j = jcast('int', 1)
            while (j <= Code05_MinimumTotalDistanceTraveled.m):
                jset(Code05_MinimumTotalDistanceTraveled.dp[i], j, Code05_MinimumTotalDistanceTraveled.dp[jcast('int', (i - 1))][j])
                if (Code05_MinimumTotalDistanceTraveled.value(i, j) != Code05_MinimumTotalDistanceTraveled.NA):
                    while ((Code05_MinimumTotalDistanceTraveled.l < Code05_MinimumTotalDistanceTraveled.r) and (Code05_MinimumTotalDistanceTraveled.value(i, Code05_MinimumTotalDistanceTraveled.queue[jcast('int', (Code05_MinimumTotalDistanceTraveled.r - 1))]) >= Code05_MinimumTotalDistanceTraveled.value(i, j))):
                        Code05_MinimumTotalDistanceTraveled.r = jcast('int', (Code05_MinimumTotalDistanceTraveled.r - 1))
                    jset(Code05_MinimumTotalDistanceTraveled.queue, ((_java_obj_1 := Code05_MinimumTotalDistanceTraveled), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], j)
                if ((Code05_MinimumTotalDistanceTraveled.l < Code05_MinimumTotalDistanceTraveled.r) and (Code05_MinimumTotalDistanceTraveled.queue[Code05_MinimumTotalDistanceTraveled.l] == jcast('int', (j - cap)))):
                    Code05_MinimumTotalDistanceTraveled.l = jcast('int', (Code05_MinimumTotalDistanceTraveled.l + 1))
                if (Code05_MinimumTotalDistanceTraveled.l < Code05_MinimumTotalDistanceTraveled.r):
                    jset(Code05_MinimumTotalDistanceTraveled.dp[i], j, jstatic('Math', 'min', Code05_MinimumTotalDistanceTraveled.dp[i][j], jcast('long', jadd(Code05_MinimumTotalDistanceTraveled.value(i, Code05_MinimumTotalDistanceTraveled.queue[Code05_MinimumTotalDistanceTraveled.l]), Code05_MinimumTotalDistanceTraveled.sum[j]))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('long', Code05_MinimumTotalDistanceTraveled.dp[Code05_MinimumTotalDistanceTraveled.n][Code05_MinimumTotalDistanceTraveled.m])

    # i号工厂和j号机器人的距离
    @staticmethod
    def dist(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        return jcast('long', jstatic('Math', 'abs', jcast('long', (jcast('long', Code05_MinimumTotalDistanceTraveled.fac[i][0]) - Code05_MinimumTotalDistanceTraveled.rob[j]))))

    # i号工厂从j号机器人开始负责的指标
    # 真的可行，返回指标的值
    # 如果不可行，返回NA
    @staticmethod
    def value(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if (Code05_MinimumTotalDistanceTraveled.dp[jcast('int', (i - 1))][jcast('int', (j - 1))] == Code05_MinimumTotalDistanceTraveled.NA):
            return jcast('long', Code05_MinimumTotalDistanceTraveled.NA)
        return jcast('long', jcast('long', (Code05_MinimumTotalDistanceTraveled.dp[jcast('int', (i - 1))][jcast('int', (j - 1))] - Code05_MinimumTotalDistanceTraveled.sum[jcast('int', (j - 1))])))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_MinimumTotalDistanceTraveled.NA = jcast('long', jget(Long, 'MAX_VALUE'))
Code05_MinimumTotalDistanceTraveled.MAXN = jcast('int', 101)
Code05_MinimumTotalDistanceTraveled.MAXM = jcast('int', 101)
Code05_MinimumTotalDistanceTraveled.n = jcast('int', 0)
Code05_MinimumTotalDistanceTraveled.m = jcast('int', 0)
Code05_MinimumTotalDistanceTraveled.fac = jarray('int', [Code05_MinimumTotalDistanceTraveled.MAXN, 2])
Code05_MinimumTotalDistanceTraveled.rob = jarray('int', [Code05_MinimumTotalDistanceTraveled.MAXM])
Code05_MinimumTotalDistanceTraveled.dp = jarray('long', [Code05_MinimumTotalDistanceTraveled.MAXN, Code05_MinimumTotalDistanceTraveled.MAXM])
Code05_MinimumTotalDistanceTraveled.sum = jarray('long', [Code05_MinimumTotalDistanceTraveled.MAXM])
Code05_MinimumTotalDistanceTraveled.queue = jarray('int', [Code05_MinimumTotalDistanceTraveled.MAXM])
Code05_MinimumTotalDistanceTraveled.l = jcast('int', 0)
Code05_MinimumTotalDistanceTraveled.r = jcast('int', 0)
