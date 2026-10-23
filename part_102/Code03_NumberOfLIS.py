# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最长递增子序列的个数
# 给定一个未排序的整数数组nums，返回最长递增子序列的个数
# 测试链接 : https://leetcode.cn/problems/number-of-longest-increasing-subsequence/
# 本题在讲解072，最长递增子序列问题与扩展，就做出过预告
# 具体可以看讲解072视频最后的部分
# 用树状数组实现时间复杂度O(n * logn)
class Code03_NumberOfLIS:
    __java_fields__ = {'MAXN': 'MAXN', 'sort': 'sort', 'treeMaxLen': 'treeMaxLen', 'treeMaxLenCnt': 'treeMaxLenCnt', 'm': 'm', 'maxLen': 'maxLen', 'maxLenCnt': 'maxLenCnt'}
    MAXN = 0
    sort = None
    # 维护信息 : 以数值i结尾的最长递增子序列，长度是多少
    # 维护的信息以树状数组组织
    treeMaxLen = None
    # 维护信息 : 以数值i结尾的最长递增子序列，个数是多少
    # 维护的信息以树状数组组织
    treeMaxLenCnt = None
    m = 0
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    # 查询结尾数值<=i的最长递增子序列的长度，赋值给maxLen
    # 查询结尾数值<=i的最长递增子序列的个数，赋值给maxLenCnt
    maxLen = 0
    maxLenCnt = 0
    @staticmethod
    def query(i):
        i = jcast('int', i)
        Code03_NumberOfLIS.maxLen = jcast('int', jset(Code03_NumberOfLIS, 'maxLenCnt', 0))
        while (i > 0):
            if (Code03_NumberOfLIS.maxLen == Code03_NumberOfLIS.treeMaxLen[i]):
                Code03_NumberOfLIS.maxLenCnt = jcast('int', jcast('int', jadd(Code03_NumberOfLIS.maxLenCnt, Code03_NumberOfLIS.treeMaxLenCnt[i])))
            else:
                if (Code03_NumberOfLIS.maxLen < Code03_NumberOfLIS.treeMaxLen[i]):
                    Code03_NumberOfLIS.maxLen = jcast('int', Code03_NumberOfLIS.treeMaxLen[i])
                    Code03_NumberOfLIS.maxLenCnt = jcast('int', Code03_NumberOfLIS.treeMaxLenCnt[i])
            i = jcast('int', jcast('int', (i - Code03_NumberOfLIS.lowbit(i))))

    # 以数值i结尾的最长递增子序列，长度达到了len，个数增加了cnt
    # 更新树状数组
    @staticmethod
    def add(i, len, cnt):
        i = jcast('int', i)
        len = jcast('int', len)
        cnt = jcast('int', cnt)
        while (i <= Code03_NumberOfLIS.m):
            if (Code03_NumberOfLIS.treeMaxLen[i] == len):
                Code03_NumberOfLIS.treeMaxLenCnt[i] = jcast('int', jcast('int', jadd(Code03_NumberOfLIS.treeMaxLenCnt[i], cnt)))
            else:
                if (Code03_NumberOfLIS.treeMaxLen[i] < len):
                    Code03_NumberOfLIS.treeMaxLen[i] = jcast('int', len)
                    Code03_NumberOfLIS.treeMaxLenCnt[i] = jcast('int', cnt)
            i = jcast('int', jcast('int', jadd(i, Code03_NumberOfLIS.lowbit(i))))

    @staticmethod
    def findNumberOfLIS(nums):
        n = jcast('int', jget(nums, 'length'))
        i = jcast('int', 1)
        while (i <= n):
            Code03_NumberOfLIS.sort[i] = jcast('int', nums[jcast('int', (i - 1))])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code03_NumberOfLIS.sort, 1, jcast('int', jadd(n, 1)))
        Code03_NumberOfLIS.m = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= n):
            if (Code03_NumberOfLIS.sort[Code03_NumberOfLIS.m] != Code03_NumberOfLIS.sort[i]):
                jset(Code03_NumberOfLIS.sort, ((_java_obj_1 := Code03_NumberOfLIS), (_java_key_2 := 'm'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_NumberOfLIS.sort[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'fill', Code03_NumberOfLIS.treeMaxLen, 1, jcast('int', jadd(Code03_NumberOfLIS.m, 1)), 0)
        jstatic('Arrays', 'fill', Code03_NumberOfLIS.treeMaxLenCnt, 1, jcast('int', jadd(Code03_NumberOfLIS.m, 1)), 0)
        i = 0
        for num in nums:
            i = jcast('int', Code03_NumberOfLIS.rank(num))
            Code03_NumberOfLIS.query(jcast('int', (i - 1)))
            if (Code03_NumberOfLIS.maxLen == 0):
                # 如果查出数值<=i-1结尾的最长递增子序列长度为0
                # 那么说明，以值i结尾的最长递增子序列长度就是1，计数增加1
                Code03_NumberOfLIS.add(i, 1, 1)
            else:
                # 如果查出数值<=i-1结尾的最长递增子序列长度为maxLen != 0
                # 那么说明，以值i结尾的最长递增子序列长度就是maxLen + 1，计数增加maxLenCnt
                Code03_NumberOfLIS.add(i, jcast('int', jadd(Code03_NumberOfLIS.maxLen, 1)), Code03_NumberOfLIS.maxLenCnt)
        Code03_NumberOfLIS.query(Code03_NumberOfLIS.m)
        return jcast('int', Code03_NumberOfLIS.maxLenCnt)

    @staticmethod
    def rank(v):
        v = jcast('int', v)
        ans = jcast('int', 0)
        l = jcast('int', 1)
        r = jcast('int', Code03_NumberOfLIS.m)
        mid = 0
        while (l <= r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code03_NumberOfLIS.sort[mid] >= v):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_NumberOfLIS.MAXN = jcast('int', 2001)
Code03_NumberOfLIS.sort = jarray('int', [Code03_NumberOfLIS.MAXN])
Code03_NumberOfLIS.treeMaxLen = jarray('int', [Code03_NumberOfLIS.MAXN])
Code03_NumberOfLIS.treeMaxLenCnt = jarray('int', [Code03_NumberOfLIS.MAXN])
Code03_NumberOfLIS.m = jcast('int', 0)
Code03_NumberOfLIS.maxLen = jcast('int', 0)
Code03_NumberOfLIS.maxLenCnt = jcast('int', 0)
