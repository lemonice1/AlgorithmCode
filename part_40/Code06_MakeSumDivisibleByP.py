# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 使数组和能被P整除
# 给你一个正整数数组 nums，请你移除 最短 子数组（可以为 空）
# 使得剩余元素的 和 能被 p 整除。 不允许 将整个数组都移除。
# 请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 -1 。
# 子数组 定义为原数组中连续的一组元素。
# 测试链接 : https://leetcode.cn/problems/make-sum-divisible-by-p/
class Code06_MakeSumDivisibleByP:
    __java_fields__ = {}
    @staticmethod
    def minSubarray(nums, p):
        p = jcast('int', p)
        # 整体余数
        mod = jcast('int', 0)
        for num in nums:
            mod = jcast('int', jcast('int', jmod(jcast('int', jadd(mod, num)), p)))
        if (mod == 0):
            return jcast('int', 0)
        # key : 前缀和%p的余数
        # value : 最晚出现的位置
        map = jnew('HashMap')
        jcall(map, 'put', 0, jcast('int', (-1)))
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        i = jcast('int', 0)
        cur = jcast('int', 0)
        find = 0
        while (i < jget(nums, 'length')):
            # 0...i这部分的余数
            cur = jcast('int', jcast('int', jmod(jcast('int', jadd(cur, nums[i])), p)))
            find = jcast('int', (jcast('int', (cur - mod)) if (cur >= mod) else jcast('int', (jcast('int', jadd(cur, p)) - mod))))
            # find = (cur + p - mod) % p;
            if jcall(map, 'containsKey', find):
                ans = jcast('int', jstatic('Math', 'min', ans, (i - jcall(map, 'get', find))))
            jcall(map, 'put', cur, i)
            i = jcast('int', (i + 1))
        return jcast('int', (jcast('int', (-1)) if (ans == jget(nums, 'length')) else ans))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


