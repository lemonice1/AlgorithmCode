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

# 分配重复整数
# 给你一个长度为n的整数数组nums，这个数组中至多有50个不同的值
# 同时你有m个顾客的订单quantity，其中整数quantity[i]是第i位顾客订单的数目
# 请你判断是否能将nums中的整数分配给这些顾客，且满足：
# 第i位顾客恰好有quantity[i]个整数、第i位顾客拿到的整数都是相同的
# 每位顾客都要满足上述两个要求，返回是否能都满足
# 测试链接 : https://leetcode.cn/problems/distribute-repeating-integers/
class Code04_DistributeRepeatingIntegers:
    __java_fields__ = {}
    # 时间复杂度O(n * 3的m次方)，空间复杂度O(n * 2的m次方)
    # ppt上有时间复杂度解析
    @staticmethod
    def canDistribute(nums, quantity):
        jstatic('Arrays', 'sort', nums)
        n = jcast('int', 1)
        i = jcast('int', 1)
        while (i < jget(nums, 'length')):
            if (nums[jcast('int', (i - 1))] != nums[i]):
                n = jcast('int', (n + 1))
            i = jcast('int', (i + 1))
        cnt = jarray('int', [n])
        c = jcast('int', 1)
        i = jcast('int', 1)
        j = jcast('int', 0)
        while (i < jget(nums, 'length')):
            if (nums[jcast('int', (i - 1))] != nums[i]):
                jset(cnt, ((_java_old_1 := j), (j := jcast('int', (j + (1)))), _java_old_1)[2], c)
                c = jcast('int', 1)
            else:
                c = jcast('int', (c + 1))
            i = jcast('int', (i + 1))
        cnt[jcast('int', (n - 1))] = jcast('int', c)
        m = jcast('int', jget(quantity, 'length'))
        sum = jarray('int', [jcast('int', (1 << (m & 31)))])
        # 下面这个枚举是生成quantity中的每个子集，所需要数字的个数
        i = jcast('int', 0)
        v = 0
        h = 0
        while (i < jget(quantity, 'length')):
            v = jcast('int', quantity[i])
            h = jcast('int', jcast('int', (1 << (i & 31))))
            j = jcast('int', 0)
            while (j < h):
                sum[jcast('int', (h | j))] = jcast('int', jcast('int', jadd(sum[j], v)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        dp = jarray('int', [jcast('int', (1 << (m & 31))), n])
        return jcast('boolean', Code04_DistributeRepeatingIntegers.f(cnt, sum, jcast('int', (jcast('int', (1 << (m & 31))) - 1)), 0, dp))

    # 当前来到的数字，编号index，个数cnt[index]
    # status : 订单状态，1还需要去满足，0已经满足过了
    @staticmethod
    def f(cnt, sum, status, index, dp):
        status = jcast('int', status)
        index = jcast('int', index)
        if (status == 0):
            return jcast('boolean', True)
        # status != 0
        if (index == jget(cnt, 'length')):
            return jcast('boolean', False)
        if (dp[status][index] != 0):
            return jcast('boolean', (dp[status][index] == 1))
        ans = jcast('boolean', False)
        k = jcast('int', cnt[index])
        # 这是整个实现最核心的枚举
        # j枚举了status的所有子集状态
        # 建议记住
        j = jcast('int', status)
        while (j > 0):
            try:
                if ((sum[j] <= k) and Code04_DistributeRepeatingIntegers.f(cnt, sum, jcast('int', (status ^ j)), jcast('int', jadd(index, 1)), dp)):
                    ans = jcast('boolean', True)
                    raise JBreak(None)
            except JContinue as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
            except JBreak as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
                break
            j = jcast('int', jcast('int', (jcast('int', (j - 1)) & status)))
        if (not ans):
            ans = jcast('boolean', Code04_DistributeRepeatingIntegers.f(cnt, sum, status, jcast('int', jadd(index, 1)), dp))
        jset(dp[status], index, (1 if ans else jcast('int', (-1))))
        return jcast('boolean', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


