# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 达标子数组的个数
# 给定一个长度为n的数组nums，给定两个整数lower和upper
# 子数组达标的条件是累加和在[lower, upper]范围上
# 返回nums中有多少个达标子数组
# 1 <= n <= 10^5
# nums[i]可能是任意整数
# -10^5 <= lower <= upper <= +10^5
# 测试链接 : https://leetcode.cn/problems/count-of-range-sum/
class Code01_CountOfRangeSum2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'sort': 'sort', 'tree': 'tree'}
    # 树状数组 + 离散化的解法，理解难度较低
    @staticmethod
    def countRangeSum(nums, lower, upper):
        lower = jcast('int', lower)
        upper = jcast('int', upper)
        Code01_CountOfRangeSum2.build(nums)
        sum = jcast('long', 0)
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < Code01_CountOfRangeSum2.n):
            sum = jcast('long', jcast('long', jadd(sum, nums[i])))
            ans = jcast('int', jcast('int', jadd(ans, jcast('int', (Code01_CountOfRangeSum2.sum(Code01_CountOfRangeSum2.rank(jcast('long', (sum - lower)))) - Code01_CountOfRangeSum2.sum(Code01_CountOfRangeSum2.rank(jcast('long', (jcast('long', (sum - upper)) - 1)))))))))
            if ((lower <= sum) and (sum <= upper)):
                ans = jcast('int', (ans + 1))
            Code01_CountOfRangeSum2.add(Code01_CountOfRangeSum2.rank(sum), 1)
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    MAXN = 0
    n = 0
    m = 0
    sort = None
    tree = None
    @staticmethod
    def build(nums):
        # 生成前缀和数组
        Code01_CountOfRangeSum2.n = jcast('int', jget(nums, 'length'))
        i = jcast('int', 1)
        j = jcast('int', 0)
        while (i <= Code01_CountOfRangeSum2.n):
            Code01_CountOfRangeSum2.sort[i] = jcast('long', jcast('long', jadd(Code01_CountOfRangeSum2.sort[jcast('int', (i - 1))], nums[j])))
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        # 前缀和数组排序和去重，最终有m个不同的前缀和
        jstatic('Arrays', 'sort', Code01_CountOfRangeSum2.sort, 1, jcast('int', jadd(Code01_CountOfRangeSum2.n, 1)))
        Code01_CountOfRangeSum2.m = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code01_CountOfRangeSum2.n):
            if (Code01_CountOfRangeSum2.sort[Code01_CountOfRangeSum2.m] != Code01_CountOfRangeSum2.sort[i]):
                jset(Code01_CountOfRangeSum2.sort, ((_java_obj_1 := Code01_CountOfRangeSum2), (_java_key_2 := 'm'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_CountOfRangeSum2.sort[i])
            i = jcast('int', (i + 1))
        # 初始化树状数组，下标1~m
        jstatic('Arrays', 'fill', Code01_CountOfRangeSum2.tree, 1, jcast('int', jadd(Code01_CountOfRangeSum2.m, 1)), 0)

    # 返回 <=v 并且尽量大的前缀和是第几号前缀和
    @staticmethod
    def rank(v):
        v = jcast('long', v)
        left = jcast('int', 1)
        right = jcast('int', Code01_CountOfRangeSum2.m)
        mid = 0
        ans = jcast('int', 0)
        while (left <= right):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(left, right)), 2)))
            if (Code01_CountOfRangeSum2.sort[mid] <= v):
                ans = jcast('int', mid)
                left = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ans)

    # 树状数组模版代码，没有任何修改
    # i号前缀和，个数增加c个
    @staticmethod
    def add(i, c):
        i = jcast('int', i)
        c = jcast('int', c)
        while (i <= Code01_CountOfRangeSum2.m):
            Code01_CountOfRangeSum2.tree[i] = jcast('int', jcast('int', jadd(Code01_CountOfRangeSum2.tree[i], c)))
            i = jcast('int', jcast('int', jadd(i, jcast('int', (i & jcast('int', (-i)))))))

    # 树状数组模版代码，没有任何修改
    # 查询1~i号前缀和一共有几个
    @staticmethod
    def sum(i):
        i = jcast('int', i)
        ans = jcast('int', 0)
        while (i > 0):
            ans = jcast('int', jcast('int', jadd(ans, Code01_CountOfRangeSum2.tree[i])))
            i = jcast('int', jcast('int', (i - jcast('int', (i & jcast('int', (-i)))))))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_CountOfRangeSum2.MAXN = jcast('int', 100002)
Code01_CountOfRangeSum2.n = jcast('int', 0)
Code01_CountOfRangeSum2.m = jcast('int', 0)
Code01_CountOfRangeSum2.sort = jarray('long', [Code01_CountOfRangeSum2.MAXN])
Code01_CountOfRangeSum2.tree = jarray('int', [Code01_CountOfRangeSum2.MAXN])
