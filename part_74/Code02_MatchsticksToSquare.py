# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 火柴拼正方形
# 你将得到一个整数数组 matchsticks
# 其中 matchsticks[i] 是第 i 个火柴棒的长度
# 你要用 所有的火柴棍 拼成一个正方形
# 你 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次
# 如果你能拼出正方形，则返回 true ，否则返回 false
# 测试链接 : https://leetcode.cn/problems/matchsticks-to-square/
class Code02_MatchsticksToSquare:
    __java_fields__ = {}
    @staticmethod
    def makesquare(nums):
        sum = jcast('int', 0)
        for num in nums:
            sum = jcast('int', jcast('int', jadd(sum, num)))
        if (jcast('int', jmod(sum, 4)) != 0):
            return jcast('boolean', False)
        n = jcast('int', jget(nums, 'length'))
        dp = jarray('int', [jcast('int', (1 << (n & 31)))])
        return jcast('boolean', Code02_MatchsticksToSquare.f(nums, jcast('int', jdiv(sum, 4)), jcast('int', (jcast('int', (1 << (n & 31))) - 1)), 0, 4, dp))

    # limit : 每条边规定的长度
    # status : 表示哪些数字还可以选
    # cur : 当前要解决的这条边已经形成的长度
    # rest : 一共还有几条边没有解决
    # 返回 : 能否用光所有火柴去解决剩下的所有边
    # 因为调用子过程之前，一定保证每条边累加起来都不超过limit
    # 所以status是决定cur和rest的，关键可变参数只有status
    @staticmethod
    def f(nums, limit, status, cur, rest, dp):
        limit = jcast('int', limit)
        status = jcast('int', status)
        cur = jcast('int', cur)
        rest = jcast('int', rest)
        if (rest == 0):
            return jcast('boolean', (status == 0))
        if (dp[status] != 0):
            return jcast('boolean', (dp[status] == 1))
        ans = jcast('boolean', False)
        i = jcast('int', 0)
        while (i < jget(nums, 'length')):
            try:
                # 考察每一根火柴，只能使用状态为1的火柴
                if ((jcast('int', (status & jcast('int', (1 << (i & 31))))) != 0) and (jcast('int', jadd(cur, nums[i])) <= limit)):
                    if (jcast('int', jadd(cur, nums[i])) == limit):
                        ans = jcast('boolean', Code02_MatchsticksToSquare.f(nums, limit, jcast('int', (status ^ jcast('int', (1 << (i & 31))))), 0, jcast('int', (rest - 1)), dp))
                    else:
                        ans = jcast('boolean', Code02_MatchsticksToSquare.f(nums, limit, jcast('int', (status ^ jcast('int', (1 << (i & 31))))), jcast('int', jadd(cur, nums[i])), rest, dp))
                    if ans:
                        raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        dp[status] = jcast('int', (1 if ans else jcast('int', (-1))))
        return jcast('boolean', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


