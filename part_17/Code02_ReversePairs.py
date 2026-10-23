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

# 翻转对数量
# 测试链接 : https://leetcode.cn/problems/reverse-pairs/
class Code02_ReversePairs:
    __java_fields__ = {'MAXN': 'MAXN', 'help': 'help'}
    MAXN = 0
    help = None
    @staticmethod
    def reversePairs(arr):
        return jcast('int', Code02_ReversePairs.counts(arr, 0, jcast('int', (jget(arr, 'length') - 1))))

    # 统计l...r范围上，翻转对的数量，同时l...r范围统计完后变有序
    # 时间复杂度O(n * logn)
    @staticmethod
    def counts(arr, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return jcast('int', 0)
        m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        return jcast('int', jcast('int', jadd(jcast('int', jadd(Code02_ReversePairs.counts(arr, l, m), Code02_ReversePairs.counts(arr, jcast('int', jadd(m, 1)), r))), Code02_ReversePairs.merge(arr, l, m, r))))

    @staticmethod
    def merge(arr, l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        # 统计部分
        ans = jcast('int', 0)
        i = jcast('int', l)
        j = jcast('int', jcast('int', jadd(m, 1)))
        while (i <= m):
            while ((j <= r) and (jcast('long', arr[i]) > jcast('long', (jcast('long', arr[j]) * 2)))):
                j = jcast('int', (j + 1))
            ans = jcast('int', jcast('int', jadd(ans, jcast('int', (jcast('int', (j - m)) - 1)))))
            i = jcast('int', (i + 1))
        # 正常merge
        i = jcast('int', l)
        a = jcast('int', l)
        b = jcast('int', jcast('int', jadd(m, 1)))
        while ((a <= m) and (b <= r)):
            jset(Code02_ReversePairs.help, ((_java_old_3 := i), (i := jcast('int', (i + (1)))), _java_old_3)[2], (arr[((_java_old_1 := a), (a := jcast('int', (a + (1)))), _java_old_1)[2]] if (arr[a] <= arr[b]) else arr[((_java_old_2 := b), (b := jcast('int', (b + (1)))), _java_old_2)[2]]))
        while (a <= m):
            jset(Code02_ReversePairs.help, ((_java_old_5 := i), (i := jcast('int', (i + (1)))), _java_old_5)[2], arr[((_java_old_4 := a), (a := jcast('int', (a + (1)))), _java_old_4)[2]])
        while (b <= r):
            jset(Code02_ReversePairs.help, ((_java_old_7 := i), (i := jcast('int', (i + (1)))), _java_old_7)[2], arr[((_java_old_6 := b), (b := jcast('int', (b + (1)))), _java_old_6)[2]])
        i = jcast('int', l)
        while (i <= r):
            arr[i] = jcast('int', Code02_ReversePairs.help[i])
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_ReversePairs.MAXN = jcast('int', 50001)
Code02_ReversePairs.help = jarray('int', [Code02_ReversePairs.MAXN])
