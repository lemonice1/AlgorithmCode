# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 俄罗斯套娃信封问题
# 给你一个二维整数数组envelopes ，其中envelopes[i]=[wi, hi]
# 表示第 i 个信封的宽度和高度
# 当另一个信封的宽度和高度都比这个信封大的时候
# 这个信封就可以放进另一个信封里，如同俄罗斯套娃一样
# 请计算 最多能有多少个信封能组成一组“俄罗斯套娃”信封
# 即可以把一个信封放到另一个信封里面，注意不允许旋转信封
# 测试链接 : https://leetcode.cn/problems/russian-doll-envelopes/
class Code02_RussianDollEnvelopes:
    __java_fields__ = {}
    @staticmethod
    def maxEnvelopes(envelopes):
        n = jcast('int', jget(envelopes, 'length'))
        # 排序策略:
        # 宽度从小到大
        # 宽度一样，高度从大到小
        jstatic('Arrays', 'sort', envelopes, (lambda a, b: ((a[0] - b[0]) if (a[0] != b[0]) else (b[1] - a[1]))))
        ends = jarray('int', [n])
        len = jcast('int', 0)
        i = jcast('int', 0)
        find = 0
        num = 0
        while (i < n):
            num = jcast('int', envelopes[i][1])
            find = jcast('int', Code02_RussianDollEnvelopes.bs(ends, len, num))
            if (find == jcast('int', (-1))):
                jset(ends, ((_java_old_1 := len), (len := jcast('int', (len + (1)))), _java_old_1)[2], num)
            else:
                ends[find] = jcast('int', num)
            i = jcast('int', (i + 1))
        return jcast('int', len)

    @staticmethod
    def bs(ends, len, num):
        len = jcast('int', len)
        num = jcast('int', num)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (len - 1)))
        m = 0
        ans = jcast('int', jcast('int', (-1)))
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (ends[m] >= num):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


