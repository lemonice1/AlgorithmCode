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

# 最长数对链
# 给你一个由n个数对组成的数对数组pairs
# 其中 pairs[i] = [lefti, righti] 且 lefti < righti
# 现在，我们定义一种 跟随 关系，当且仅当 b < c 时
# 数对 p2 = [c, d] 才可以跟在 p1 = [a, b] 后面
# 我们用这种形式来构造 数对链
# 找出并返回能够形成的最长数对链的长度
# 测试链接 : https://leetcode.cn/problems/maximum-length-of-pair-chain/
class Code04_MaximumLengthOfPairChain:
    __java_fields__ = {}
    @staticmethod
    def findLongestChain(pairs):
        n = jcast('int', jget(pairs, 'length'))
        # 数对根据开始位置排序，从小到大
        # 结束位置无所谓！
        jstatic('Arrays', 'sort', pairs, (lambda a, b: (a[0] - b[0])))
        # 结尾的数值
        ends = jarray('int', [n])
        len = jcast('int', 0)
        for pair in pairs:
            find = jcast('int', Code04_MaximumLengthOfPairChain.bs(ends, len, pair[0]))
            if (find == jcast('int', (-1))):
                jset(ends, ((_java_old_1 := len), (len := jcast('int', (len + (1)))), _java_old_1)[2], pair[1])
            else:
                jset(ends, find, jstatic('Math', 'min', ends[find], pair[1]))
        return jcast('int', len)

    # >= num最左位置
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

    # 最优解利用贪心
    @staticmethod
    def findLongestChain2(pairs):
        pre = jcast('int', jget(Integer, 'MIN_VALUE'))
        ans = jcast('int', 0)
        jstatic('Arrays', 'sort', pairs, (lambda a, b: (a[1] - b[1])))
        for pair in pairs:
            if (pre < pair[0]):
                pre = jcast('int', pair[1])
                ans = jcast('int', (ans + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


