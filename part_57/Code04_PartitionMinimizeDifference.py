# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 将数组分成两个数组并最小化数组和的差
# 这道题课上没讲，其实就是题目3加上了选取数字个数的限制
# 比如一共30个数，分配到两个部分
# 要求每个部分都是15个数，并且做到累加和差值最小
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 测试链接 : https://leetcode.cn/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
class Code04_PartitionMinimizeDifference:
    __java_fields__ = {}
    class Solution:
        __java_fields__ = {'MAXK': 'MAXK', 'MAXS': 'MAXS', 'lsiz': 'lsiz', 'rsiz': 'rsiz', 'lsum': 'lsum', 'rsum': 'rsum'}
        MAXK = 0
        MAXS = 0
        # siz[k] : 选了k个数的情况下，一共有多少个累加和
        lsiz = None
        rsiz = None
        # sum[k][...] : 选了k个数的情况下，收集的每个累加和都是什么
        # 到底有几个累加和？就是siz[k]的数量
        lsum = None
        rsum = None
        @staticmethod
        def minimumDifference(nums):
            m = jcast('int', jget(nums, 'length'))
            n = jcast('int', jcast('int', (m >> (1 & 31))))
            sum = jcast('int', 0)
            for num in nums:
                sum = jcast('int', jcast('int', jadd(sum, num)))
            # 排序只是为了递归收集时压缩相同数字，常数优化
            jstatic('Arrays', 'sort', nums)
            jstatic('Arrays', 'fill', Code04_PartitionMinimizeDifference.Solution.lsiz, 0, jcast('int', jadd(n, 1)), 0)
            jstatic('Arrays', 'fill', Code04_PartitionMinimizeDifference.Solution.rsiz, 0, jcast('int', jadd(n, 1)), 0)
            Code04_PartitionMinimizeDifference.Solution.collect(nums, 0, n, 0, 0, Code04_PartitionMinimizeDifference.Solution.lsum, Code04_PartitionMinimizeDifference.Solution.lsiz)
            Code04_PartitionMinimizeDifference.Solution.collect(nums, n, m, 0, 0, Code04_PartitionMinimizeDifference.Solution.rsum, Code04_PartitionMinimizeDifference.Solution.rsiz)
            i = jcast('int', 0)
            while (i <= n):
                jstatic('Arrays', 'sort', Code04_PartitionMinimizeDifference.Solution.lsum[i], 0, Code04_PartitionMinimizeDifference.Solution.lsiz[i])
                jstatic('Arrays', 'sort', Code04_PartitionMinimizeDifference.Solution.rsum[i], 0, Code04_PartitionMinimizeDifference.Solution.rsiz[i])
                i = jcast('int', (i + 1))
            ans = jcast('long', jget(Long, 'MAX_VALUE'))
            k = jcast('int', 0)
            while (k <= n):
                need = jcast('int', jcast('int', (n - k)))
                i = jcast('int', 0)
                j = jcast('int', jcast('int', (Code04_PartitionMinimizeDifference.Solution.rsiz[need] - 1)))
                while (i < Code04_PartitionMinimizeDifference.Solution.lsiz[k]):
                    while ((j > 0) and (jstatic('Math', 'abs', jcast('long', (jcast('long', sum) - jcast('long', (2 * jcast('int', jadd(Code04_PartitionMinimizeDifference.Solution.lsum[k][i], Code04_PartitionMinimizeDifference.Solution.rsum[need][jcast('int', (j - 1))]))))))) <= jstatic('Math', 'abs', jcast('long', (jcast('long', sum) - jcast('long', (2 * jcast('int', jadd(Code04_PartitionMinimizeDifference.Solution.lsum[k][i], Code04_PartitionMinimizeDifference.Solution.rsum[need][j]))))))))):
                        j = jcast('int', (j - 1))
                    ans = jcast('long', jstatic('Math', 'min', ans, jstatic('Math', 'abs', jcast('long', (jcast('long', sum) - jcast('long', (2 * jcast('int', jadd(Code04_PartitionMinimizeDifference.Solution.lsum[k][i], Code04_PartitionMinimizeDifference.Solution.rsum[need][j])))))))))
                    i = jcast('int', (i + 1))
                k = jcast('int', (k + 1))
            return jcast('int', jcast('int', ans))

        @staticmethod
        def collect(nums, i, end, s, c, sum, siz):
            i = jcast('int', i)
            end = jcast('int', end)
            s = jcast('int', s)
            c = jcast('int', c)
            if (i == end):
                jset(sum[c], ((_java_obj_1 := siz), (_java_key_2 := c), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], s)
            else:
                j = jcast('int', jcast('int', jadd(i, 1)))
                while ((j < end) and (nums[j] == nums[i])):
                    j = jcast('int', (j + 1))
                k = jcast('int', 0)
                while (k <= jcast('int', (j - i))):
                    Code04_PartitionMinimizeDifference.Solution.collect(nums, j, end, jcast('int', jadd(s, jcast('int', (k * nums[i])))), jcast('int', jadd(c, k)), sum, siz)
                    k = jcast('int', (k + 1))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_PartitionMinimizeDifference.Solution.MAXK = jcast('int', 16)
Code04_PartitionMinimizeDifference.Solution.MAXS = jcast('int', jcast('int', (1 << (15 & 31))))
Code04_PartitionMinimizeDifference.Solution.lsiz = jarray('int', [Code04_PartitionMinimizeDifference.Solution.MAXK])
Code04_PartitionMinimizeDifference.Solution.rsiz = jarray('int', [Code04_PartitionMinimizeDifference.Solution.MAXK])
Code04_PartitionMinimizeDifference.Solution.lsum = jarray('int', [Code04_PartitionMinimizeDifference.Solution.MAXK, Code04_PartitionMinimizeDifference.Solution.MAXS])
Code04_PartitionMinimizeDifference.Solution.rsum = jarray('int', [Code04_PartitionMinimizeDifference.Solution.MAXK, Code04_PartitionMinimizeDifference.Solution.MAXS])
