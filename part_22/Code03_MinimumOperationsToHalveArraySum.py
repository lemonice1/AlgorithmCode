# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 将数组和减半的最少操作次数
# 测试链接 : https://leetcode.cn/problems/minimum-operations-to-halve-array-sum/
class Code03_MinimumOperationsToHalveArraySum:
    __java_fields__ = {'MAXN': 'MAXN', 'heap': 'heap', 'size': 'size'}
    # 提交时把halveArray1改名为halveArray
    @staticmethod
    def halveArray1(nums):
        # 大根堆
        heap = jnew('PriorityQueue', (lambda a, b: jcall(b, 'compareTo', a)))
        sum = jcast('double', 0)
        for num in nums:
            jcall(heap, 'add', jcast('double', num))
            sum = jcast('double', jadd(sum, num))
        # sum，整体累加和，-> 要减少的目标！
        sum = jcast('double', jdiv(sum, 2))
        ans = jcast('int', 0)
        minus = jcast('double', 0)
        cur = 0.0
        while (minus < sum):
            cur = jcast('double', jdiv(jcall(heap, 'poll'), 2))
            jcall(heap, 'add', cur)
            ans = jcast('int', (ans + 1))
            minus = jcast('double', jadd(minus, cur))
        return jcast('int', ans)

    MAXN = 0
    heap = None
    size = 0
    # 提交时把halveArray2改名为halveArray
    @staticmethod
    def halveArray2(nums):
        Code03_MinimumOperationsToHalveArraySum.size = jcast('int', jget(nums, 'length'))
        sum = jcast('long', 0)
        i = jcast('int', jcast('int', (Code03_MinimumOperationsToHalveArraySum.size - 1)))
        while (i >= 0):
            Code03_MinimumOperationsToHalveArraySum.heap[i] = jcast('long', jcast('long', (jcast('long', nums[i]) << (20 & 63))))
            sum = jcast('long', jcast('long', jadd(sum, Code03_MinimumOperationsToHalveArraySum.heap[i])))
            Code03_MinimumOperationsToHalveArraySum.heapify(i)
            i = jcast('int', (i - 1))
        sum = jcast('long', jcast('long', jdiv(sum, 2)))
        ans = jcast('int', 0)
        minus = jcast('long', 0)
        while (minus < sum):
            Code03_MinimumOperationsToHalveArraySum.heap[0] = jcast('long', jcast('long', jdiv(Code03_MinimumOperationsToHalveArraySum.heap[0], 2)))
            minus = jcast('long', jcast('long', jadd(minus, Code03_MinimumOperationsToHalveArraySum.heap[0])))
            Code03_MinimumOperationsToHalveArraySum.heapify(0)
            ans = jcast('int', (ans + 1))
        return jcast('int', ans)

    @staticmethod
    def heapify(i):
        i = jcast('int', i)
        l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
        while (l < Code03_MinimumOperationsToHalveArraySum.size):
            try:
                best = jcast('int', (jcast('int', jadd(l, 1)) if ((jcast('int', jadd(l, 1)) < Code03_MinimumOperationsToHalveArraySum.size) and (Code03_MinimumOperationsToHalveArraySum.heap[jcast('int', jadd(l, 1))] > Code03_MinimumOperationsToHalveArraySum.heap[l])) else l))
                best = jcast('int', (best if (Code03_MinimumOperationsToHalveArraySum.heap[best] > Code03_MinimumOperationsToHalveArraySum.heap[i]) else i))
                if (best == i):
                    raise JBreak(None)
                Code03_MinimumOperationsToHalveArraySum.swap(best, i)
                i = jcast('int', best)
                l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('long', Code03_MinimumOperationsToHalveArraySum.heap[i])
        Code03_MinimumOperationsToHalveArraySum.heap[i] = jcast('long', Code03_MinimumOperationsToHalveArraySum.heap[j])
        Code03_MinimumOperationsToHalveArraySum.heap[j] = jcast('long', tmp)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_MinimumOperationsToHalveArraySum.MAXN = jcast('int', 100001)
Code03_MinimumOperationsToHalveArraySum.heap = jarray('long', [Code03_MinimumOperationsToHalveArraySum.MAXN])
Code03_MinimumOperationsToHalveArraySum.size = jcast('int', 0)
