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

# 森林中的兔子
# 森林中有未知数量的兔子
# 你问兔子们一个问题: "还有多少只兔子与你颜色相同?"
# 你将答案收集到了一个数组answers中
# 你可能没有收集到所有兔子的回答，可能只是一部分兔子的回答
# 其中answers[i]是第i只兔子的答案
# 所有兔子都不会说错，返回森林中兔子的最少数量
# 测试链接 : https://leetcode.cn/problems/rabbits-in-forest/
class Code02_RabbitsInForest:
    __java_fields__ = {}
    @staticmethod
    def numRabbits(arr):
        # a / b 向上取整 -> (a + b - 1) / b
        jstatic('Arrays', 'sort', arr)
        n = jcast('int', jget(arr, 'length'))
        ans = jcast('int', 0)
        i = jcast('int', 0)
        j = jcast('int', 1)
        x = 0
        while (i < n):
            x = jcast('int', arr[i])
            while ((j < n) and (x == arr[j])):
                j = jcast('int', (j + 1))
            # i...j-1 都是同一种答案，当前组有j-i个回答
            ans = jcast('int', jcast('int', jadd(ans, jcast('int', (jcast('int', jdiv(jcast('int', jadd(jcast('int', (j - i)), x)), jcast('int', jadd(x, 1)))) * jcast('int', jadd(x, 1)))))))
            i = jcast('int', j)
            j = jcast('int', (j + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


