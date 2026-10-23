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

# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的组合
# 答案 不能 包含重复的组合。返回的答案中，组合可以按 任意顺序 排列
# 注意其实要求返回的不是子集，因为子集一定是不包含相同元素的，要返回的其实是不重复的组合
# 比如输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
# 测试链接 : https://leetcode.cn/problems/subsets-ii/
class Code02_Combinations:
    __java_fields__ = {}
    @staticmethod
    def subsetsWithDup(nums):
        ans = jnew('ArrayList')
        jstatic('Arrays', 'sort', nums)
        Code02_Combinations.f(nums, 0, jarray('int', [jget(nums, 'length')]), 0, ans)
        return ans

    @staticmethod
    def f(nums, i, path, size, ans):
        i = jcast('int', i)
        size = jcast('int', size)
        if (i == jget(nums, 'length')):
            cur = jnew('ArrayList')
            j = jcast('int', 0)
            while (j < size):
                jcall(cur, 'add', path[j])
                j = jcast('int', (j + 1))
            jcall(ans, 'add', cur)
        else:
            # 下一组的第一个数的位置
            j = jcast('int', jcast('int', jadd(i, 1)))
            while ((j < jget(nums, 'length')) and (nums[i] == nums[j])):
                j = jcast('int', (j + 1))
            # 当前数x，要0个
            Code02_Combinations.f(nums, j, path, size, ans)
            # 当前数x，要1个、要2个、要3个...都尝试
            while (i < j):
                jset(path, ((_java_old_1 := size), (size := jcast('int', (size + (1)))), _java_old_1)[2], nums[i])
                Code02_Combinations.f(nums, j, path, size, ans)
                i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


