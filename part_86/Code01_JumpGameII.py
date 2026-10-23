# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 跳跃游戏II
# 给定一个长度为n的整数数组nums
# 你初始在0下标，nums[i]表示你可以从i下标往右跳的最大距离
# 比如，nums[0] = 3
# 表示你可以从0下标去往：1下标、2下标、3下标
# 你达到i下标后，可以根据nums[i]的值继续往右跳
# 返回你到达n-1下标的最少跳跃次数
# 测试用例可以保证一定能到达
# 测试链接 : https://leetcode.cn/problems/jump-game-ii/
class Code01_JumpGameII:
    __java_fields__ = {}
    @staticmethod
    def jump(arr):
        n = jcast('int', jget(arr, 'length'))
        # 当前步以内，最右到哪
        cur = jcast('int', 0)
        # 如果再一步，(当前步+1)以内，最右到哪
        next = jcast('int', 0)
        # 一共需要跳几步
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            # 来到i下标
            # cur包括了i所在的位置，不用付出额外步数
            # cur没有包括i所在的位置，需要付出额外步数
            if (cur < i):
                ans = jcast('int', (ans + 1))
                cur = jcast('int', next)
            next = jcast('int', jstatic('Math', 'max', next, jcast('int', jadd(i, arr[i]))))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


