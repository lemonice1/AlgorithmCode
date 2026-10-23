# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 连接棒材的最低费用(leetcode测试)
# 你有一些长度为正整数的棍子
# 这些长度以数组sticks的形式给出
# sticks[i]是第i个木棍的长度
# 你可以通过支付x+y的成本将任意两个长度为x和y的棍子连接成一个棍子
# 你必须连接所有的棍子，直到剩下一个棍子
# 返回以这种方式将所有给定的棍子连接成一个棍子的最小成本
# 测试链接 : https://leetcode.cn/problems/minimum-cost-to-connect-sticks/
class Code06_MinimumCostToConnectSticks1:
    __java_fields__ = {}
    @staticmethod
    def connectSticks(arr):
        # 小根堆
        heap = jnew('PriorityQueue')
        i = jcast('int', 0)
        while (i < jget(arr, 'length')):
            jcall(heap, 'add', arr[i])
            i = jcast('int', (i + 1))
        sum = jcast('int', 0)
        cur = jcast('int', 0)
        while (jcall(heap, 'size') > 1):
            cur = jcast('int', jadd(jcall(heap, 'poll'), jcall(heap, 'poll')))
            sum = jcast('int', jcast('int', jadd(sum, cur)))
            jcall(heap, 'add', cur)
        return jcast('int', sum)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


