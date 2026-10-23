# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 超级洗衣机
# 假设有n台超级洗衣机放在同一排上
# 开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的
# 在每一步操作中，你可以选择任意 m (1 <= m <= n) 台洗衣机
# 与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机
# 给定一个整数数组machines代表从左至右每台洗衣机中的衣物数量
# 请给出能让所有洗衣机中剩下的衣物的数量相等的最少的操作步数
# 如果不能使每台洗衣机中衣物的数量相等则返回-1
# 测试链接 : https://leetcode.cn/problems/super-washing-machines/
class Code05_SuperWashingMachines:
    __java_fields__ = {}
    @staticmethod
    def findMinMoves(arr):
        n = jcast('int', jget(arr, 'length'))
        sum = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            sum = jcast('int', jcast('int', jadd(sum, arr[i])))
            i = jcast('int', (i + 1))
        if (jcast('int', jmod(sum, n)) != 0):
            return jcast('int', jcast('int', (-1)))
        # 每台洗衣机最终要求的衣服数量一定是平均值
        avg = jcast('int', jcast('int', jdiv(sum, n)))
        # 左侧累加和
        leftSum = jcast('int', 0)
        # 左边还需要多少件衣服
        leftNeed = jcast('int', 0)
        # 右边还需要多少件衣服
        rightNeed = jcast('int', 0)
        # 每一步的瓶颈
        bottleNeck = jcast('int', 0)
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            leftNeed = jcast('int', jcast('int', (jcast('int', (i * avg)) - leftSum)))
            rightNeed = jcast('int', jcast('int', (jcast('int', (jcast('int', (jcast('int', (n - i)) - 1)) * avg)) - jcast('int', (jcast('int', (sum - leftSum)) - arr[i])))))
            if ((leftNeed > 0) and (rightNeed > 0)):
                bottleNeck = jcast('int', jcast('int', jadd(leftNeed, rightNeed)))
            else:
                bottleNeck = jcast('int', jstatic('Math', 'max', jstatic('Math', 'abs', leftNeed), jstatic('Math', 'abs', rightNeed)))
            ans = jcast('int', jstatic('Math', 'max', ans, bottleNeck))
            leftSum = jcast('int', jcast('int', jadd(leftSum, arr[i])))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


