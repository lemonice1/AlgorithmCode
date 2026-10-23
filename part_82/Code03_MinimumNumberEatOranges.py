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

# 吃掉N个橘子的最少天数
# 厨房里总共有 n 个橘子，你决定每一天选择如下方式之一吃这些橘子
# 1）吃掉一个橘子
# 2) 如果剩余橘子数 n 能被 2 整除，那么你可以吃掉 n/2 个橘子
# 3) 如果剩余橘子数 n 能被 3 整除，那么你可以吃掉 2*(n/3) 个橘子
# 每天你只能从以上 3 种方案中选择一种方案
# 请你返回吃掉所有 n 个橘子的最少天数
# 测试链接 : https://leetcode.cn/problems/minimum-number-of-days-to-eat-n-oranges/
class Code03_MinimumNumberEatOranges:
    __java_fields__ = {'dp': 'dp'}
    # 所有的答案都填在这个表里
    # 这个表对所有的过程共用
    dp = None
    @staticmethod
    def minDays(n):
        n = jcast('int', n)
        if (n <= 1):
            return jcast('int', n)
        if jcall(Code03_MinimumNumberEatOranges.dp, 'containsKey', n):
            return jcast('int', jcall(Code03_MinimumNumberEatOranges.dp, 'get', n))
        # 1) 吃掉一个橘子
        # 2) 如果n能被2整除，吃掉一半的橘子，剩下一半
        # 3) 如果n能被3正数，吃掉三分之二的橘子，剩下三分之一
        # 因为方法2）和3），是按比例吃橘子，所以必然会非常快
        # 所以，决策如下：
        # 可能性1：为了使用2）方法，先把橘子吃成2的整数倍，然后直接干掉一半，剩下的n/2调用递归
        # 即，n % 2 + 1 + minDays(n/2)
        # 可能性2：为了使用3）方法，先把橘子吃成3的整数倍，然后直接干掉三分之二，剩下的n/3调用递归
        # 即，n % 3 + 1 + minDays(n/3)
        # 至于方法1)，完全是为了这两种可能性服务的，因为能按比例吃，肯定比一个一个吃快(显而易见的贪心)
        ans = jcast('int', jstatic('Math', 'min', jcast('int', jadd(jcast('int', jadd(jcast('int', jmod(n, 2)), 1)), Code03_MinimumNumberEatOranges.minDays(jcast('int', jdiv(n, 2))))), jcast('int', jadd(jcast('int', jadd(jcast('int', jmod(n, 3)), 1)), Code03_MinimumNumberEatOranges.minDays(jcast('int', jdiv(n, 3)))))))
        jcall(Code03_MinimumNumberEatOranges.dp, 'put', n, ans)
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_MinimumNumberEatOranges.dp = jnew('HashMap')
