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

# 出现次数大于n/k的数
# 给定一个大小为n的数组nums，给定一个较小的正数k
# 水王数是指在数组中出现次数大于n/k的数
# 返回所有的水王数，如果没有水王数返回空列表
# 测试链接 : https://leetcode.cn/problems/majority-element-ii/
class Code05_MoreThanNK:
    __java_fields__ = {}
    @staticmethod
    def majorityElement(nums):
        return Code05_MoreThanNK.majority(nums, 3)

    @staticmethod
    def majority(nums, k):
        k = jcast('int', k)
        cands = jarray('int', [(k := jcast('int', (k + (-1)))), 2])
        for num in nums:
            Code05_MoreThanNK.update(cands, k, num)
        ans = jnew('ArrayList')
        Code05_MoreThanNK.collect(cands, k, nums, jget(nums, 'length'), ans)
        return ans

    @staticmethod
    def update(cands, k, num):
        k = jcast('int', k)
        num = jcast('int', num)
        i = jcast('int', 0)
        while (i < k):
            if ((cands[i][0] == num) and (cands[i][1] > 0)):
                ((_java_obj_1 := cands[i]), (_java_key_2 := 1), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
                return
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < k):
            if (cands[i][1] == 0):
                jset(cands[i], 0, num)
                jset(cands[i], 1, 1)
                return
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < k):
            if (cands[i][1] > 0):
                ((_java_obj_4 := cands[i]), (_java_key_5 := 1), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))), _java_old_6)[4]
            i = jcast('int', (i + 1))

    @staticmethod
    def collect(cands, k, nums, n, ans):
        k = jcast('int', k)
        n = jcast('int', n)
        i = jcast('int', 0)
        cur = 0
        real = 0
        while (i < k):
            if (cands[i][1] > 0):
                cur = jcast('int', cands[i][0])
                real = jcast('int', 0)
                for num in nums:
                    if (cur == num):
                        real = jcast('int', (real + 1))
                if (real > jcast('int', jdiv(n, jcast('int', jadd(k, 1))))):
                    jcall(ans, 'add', cur)
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


