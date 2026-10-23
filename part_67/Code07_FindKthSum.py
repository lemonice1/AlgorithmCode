# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 同学找到的在线测试，思路来自课上的题目6
# 找出数组的第K大和
# 给定一个数组nums和正数k
# 可以选择数组的任何子序列并对其元素求和
# 希望找到第k大的子序列和，子序列和允许出现重复
# 空子序列的和视作0，数组中的值可正、可负、可0
# 测试链接 : https://leetcode.cn/problems/find-the-k-sum-of-an-array/description/
#
# 转化逻辑如下 :
# 1，先把所有正数加起来，得到sum，这是nums第1大子序列和
# 2，nums第2大子序列和，要么sum中去掉一个最小的正数，要么sum + (选剩下的非正数字，拼出最大的累加和)
# 3，nums第2大子序列和 = (sum - 最小的正数) 或者 (sum - 选剩下的非正数字，拼出最小的绝对值)
# 4，原始数组记为nums，把每个数转成绝对值的数组记为a
# 5，nums第1大子序列和 = sum = sum - 0，其中0表示数组a取空集的累加和，认为是a的第1小子序列和
# 6，nums第1大子序列和 = sum - a的第1小子序列和
# 7，nums第2大子序列和 = sum - a的第2小子序列和
# 8，nums第k大子序列和 = sum - a的第k小子序列和
# 9，求a的第k小子序列和即可，注意，a的第1小子序列和，是空集的情况
class Code07_FindKthSum:
    __java_fields__ = {}
    class Solution:
        __java_fields__ = {}
        class Node:
            __java_fields__ = {'idx': 'idx', 'val': 'val'}
            # idx：实例字段，在构造函数中初始化。
            # val：实例字段，在构造函数中初始化。
            def _java_init_0(self, i, v):
                i = jcast('int', i)
                v = jcast('long', v)
                self.idx = jcast('int', i)
                self.val = jcast('long', v)

            def __init__(self, *args, _java_ctor=None):
                self.idx = jcast('int', 0)
                self.val = jcast('long', 0)
                _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int', 'long']], [False])
                if _java_choice == 0:
                    return self._java_init_0(*args)
                raise TypeError("No matching overload for Code07_FindKthSum.Solution.Node.Node")


        class NodeCmp:
            __java_fields__ = {}
            def compare(self, o1, o2):
                if (jget(o1, 'val') != jget(o2, 'val')):
                    return jcast('int', jstatic('Long', 'compare', jget(o1, 'val'), jget(o2, 'val')))
                else:
                    return jcast('int', jstatic('Integer', 'compare', jget(o1, 'idx'), jget(o2, 'idx')))

            def __init__(self, *args, _java_ctor=None):
                if args:
                    raise TypeError('This class has a no-argument constructor')


        def kSum(self, nums, k):
            k = jcast('int', k)
            n = jcast('int', jget(nums, 'length'))
            sum = jcast('long', 0)
            i = jcast('int', 0)
            while (i < n):
                if (nums[i] > 0):
                    sum = jcast('long', jcast('long', jadd(sum, nums[i])))
                else:
                    nums[i] = jcast('int', jcast('int', (-nums[i])))
                i = jcast('int', (i + 1))
            jstatic('Arrays', 'sort', nums)
            heap = jnew('PriorityQueue', Code07_FindKthSum.Solution.NodeCmp())
            # 空集，下标为-1，累加和为0，这是a的第1小子序列和
            jcall(heap, 'add', Code07_FindKthSum.Solution.Node(jcast('int', (-1)), 0, _java_ctor=0))
            # 弹出前k-1小
            i = jcast('int', 1)
            while (i < k):
                cur = jcall(heap, 'poll')
                idx = jcast('int', jget(cur, 'idx'))
                val = jcast('long', jget(cur, 'val'))
                if (jcast('int', jadd(idx, 1)) < n):
                    jcall(heap, 'add', Code07_FindKthSum.Solution.Node(jcast('int', jadd(idx, 1)), jcast('long', jadd(val, nums[jcast('int', jadd(idx, 1))])), _java_ctor=0))
                    if (idx >= 0):
                        jcall(heap, 'add', Code07_FindKthSum.Solution.Node(jcast('int', jadd(idx, 1)), jcast('long', jadd(jcast('long', (val - nums[idx])), nums[jcast('int', jadd(idx, 1))])), _java_ctor=0))
                i = jcast('int', (i + 1))
            # sum - a的第k小子序列和
            return jcast('long', (sum - jget(jcall(heap, 'poll'), 'val')))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


