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

# 没有重复项数字的全排列
# 测试链接 : https://leetcode.cn/problems/permutations/
class Code03_Permutations:
    __java_fields__ = {}
    @staticmethod
    def permute(nums):
        ans = jnew('ArrayList')
        Code03_Permutations.f(nums, 0, ans)
        return ans

    @staticmethod
    def f(nums, i, ans):
        i = jcast('int', i)
        if (i == jget(nums, 'length')):
            cur = jnew('ArrayList')
            for num in nums:
                jcall(cur, 'add', num)
            jcall(ans, 'add', cur)
        else:
            j = jcast('int', i)
            while (j < jget(nums, 'length')):
                Code03_Permutations.swap(nums, i, j)
                Code03_Permutations.f(nums, jcast('int', jadd(i, 1)), ans)
                # 特别重要，课上进行了详细的图解
                Code03_Permutations.swap(nums, i, j)
                j = jcast('int', (j + 1))

    @staticmethod
    def swap(nums, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', nums[i])
        nums[i] = jcast('int', nums[j])
        nums[j] = jcast('int', tmp)

    @staticmethod
    def main(args):
        nums = jarray('int', [None], [1, 2, 3])
        ans = Code03_Permutations.permute(nums)
        for list in ans:
            for num in list:
                jprint(jadd(num, ' '), newline=False)
            jprint(newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code03_Permutations.main([])
