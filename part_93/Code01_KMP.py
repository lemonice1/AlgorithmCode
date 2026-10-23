# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# KMP算法模版
# 测试链接 : https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Code01_KMP:
    __java_fields__ = {}
    @staticmethod
    def strStr(s1, s2):
        # return s1.indexOf(s2);
        return jcast('int', Code01_KMP.kmp(jcall(s1, 'toCharArray'), jcall(s2, 'toCharArray')))

    # KMP算法
    @staticmethod
    def kmp(s1, s2):
        # s1中当前比对的位置是x
        # s2中当前比对的位置是y
        n = jcast('int', jget(s1, 'length'))
        m = jcast('int', jget(s2, 'length'))
        x = jcast('int', 0)
        y = jcast('int', 0)
        # O(m)
        next = Code01_KMP.nextArray(s2, m)
        # O(n)
        while ((x < n) and (y < m)):
            if (s1[x] == s2[y]):
                x = jcast('int', (x + 1))
                y = jcast('int', (y + 1))
            else:
                if (y == 0):
                    x = jcast('int', (x + 1))
                else:
                    y = jcast('int', next[y])
        return jcast('int', (jcast('int', (x - y)) if (y == m) else jcast('int', (-1))))

    # 得到next数组
    @staticmethod
    def nextArray(s, m):
        m = jcast('int', m)
        if (m == 1):
            return jarray('int', [None], [jcast('int', (-1))])
        next = jarray('int', [m])
        next[0] = jcast('int', jcast('int', (-1)))
        next[1] = jcast('int', 0)
        # i表示当前要求next值的位置
        # cn表示当前要和前一个字符比对的下标
        i = jcast('int', 2)
        cn = jcast('int', 0)
        while (i < m):
            if (s[jcast('int', (i - 1))] == s[cn]):
                jset(next, ((_java_old_1 := i), (i := jcast('int', (i + (1)))), _java_old_1)[2], (cn := jcast('int', (cn + (1)))))
            else:
                if (cn > 0):
                    cn = jcast('int', next[cn])
                else:
                    jset(next, ((_java_old_2 := i), (i := jcast('int', (i + (1)))), _java_old_2)[2], 0)
        return next

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


