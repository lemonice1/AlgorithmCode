# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 加油站
# 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升
# 你从其中的一个加油站出发，开始时油箱为空。
# 给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周
# 则返回出发时加油站的编号，否则返回 -1
# 如果存在解，则 保证 它是 唯一 的。
# 测试链接 : https://leetcode.cn/problems/gas-station/
class Code04_GasStation:
    __java_fields__ = {}
    @staticmethod
    def canCompleteCircuit(gas, cost):
        n = jcast('int', jget(gas, 'length'))
        # 本来下标是0..n-1，但是扩充到0..2*n-1，i位置的余量信息在(r%n)位置
        # 窗口范围是[l, r)，左闭右开，也就是说窗口是[l..r-1]，r是到不了的位置
        l = jcast('int', 0)
        r = jcast('int', 0)
        sum = 0
        while (l < n):
            sum = jcast('int', 0)
            while (jcast('int', (jcast('int', jadd(sum, gas[jcast('int', jmod(r, n))])) - cost[jcast('int', jmod(r, n))])) >= 0):
                # r位置即将右扩，窗口会变大
                # 此时检查是否已经转了一圈
                if (jcast('int', jadd(jcast('int', (r - l)), 1)) == n):
                    return jcast('int', l)
                # r位置进入窗口，累加和加上r位置的余量
                sum = jcast('int', jcast('int', jadd(sum, jcast('int', (gas[jcast('int', jmod(r, n))] - cost[jcast('int', jmod(r, n))])))))
                # r右扩，窗口变大了
                r = jcast('int', (r + 1))
            l = jcast('int', jcast('int', jadd(r, 1)))
            r = jcast('int', l)
        return jcast('int', jcast('int', (-1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


