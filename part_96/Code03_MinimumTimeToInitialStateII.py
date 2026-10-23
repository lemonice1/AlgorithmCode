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

# 将单词恢复初始状态所需的最短时间II
# 给你一个下标从0开始的字符串word和一个整数k
# 在每一秒，必须执行以下操作
# 移除word的前k个字符
# 在word的末尾添加k个任意字符
# 添加的字符不必和移除的字符相同
# 返回将word恢复到初始状态所需的最短时间
# 该时间必须大于零
# 测试链接 : https://leetcode.cn/problems/minimum-time-to-revert-word-to-initial-state-ii/
class Code03_MinimumTimeToInitialStateII:
    __java_fields__ = {'MAXN': 'MAXN', 'z': 'z'}
    @staticmethod
    def minimumTimeToInitialState(word, k):
        k = jcast('int', k)
        s = jcall(word, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        Code03_MinimumTimeToInitialStateII.zArray(s, n)
        i = jcast('int', k)
        while (i < n):
            if (Code03_MinimumTimeToInitialStateII.z[i] == jcast('int', (n - i))):
                return jcast('int', jcast('int', jdiv(i, k)))
            i = jcast('int', jcast('int', jadd(i, k)))
        return jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(n, k)) - 1)), k)))

    # leetcode增加了数据量
    # 所以把这个值改成10^6规模
    MAXN = 0
    z = None
    @staticmethod
    def zArray(s, n):
        n = jcast('int', n)
        Code03_MinimumTimeToInitialStateII.z[0] = jcast('int', n)
        i = jcast('int', 1)
        c = jcast('int', 1)
        r = jcast('int', 1)
        len = 0
        while (i < n):
            len = jcast('int', (jstatic('Math', 'min', jcast('int', (r - i)), Code03_MinimumTimeToInitialStateII.z[jcast('int', (i - c))]) if (r > i) else 0))
            while ((jcast('int', jadd(i, len)) < n) and (s[jcast('int', jadd(i, len))] == s[len])):
                len = jcast('int', (len + 1))
            if (jcast('int', jadd(i, len)) > r):
                r = jcast('int', jcast('int', jadd(i, len)))
                c = jcast('int', i)
            Code03_MinimumTimeToInitialStateII.z[i] = jcast('int', len)
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_MinimumTimeToInitialStateII.MAXN = jcast('int', 1000001)
Code03_MinimumTimeToInitialStateII.z = jarray('int', [Code03_MinimumTimeToInitialStateII.MAXN])
