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

# 最长理想子序列
# 给定一个长度为n，只由小写字母组成的字符串s，给定一个非负整数k
# 字符串s可以生成很多子序列，下面给出理想子序列的定义
# 子序列中任意相邻的两个字符，在字母表中位次的差值绝对值<=k
# 返回最长理想子序列
# 1 <= n <= 10^5
# 0 <= k <= 25
# s只由小写字母组成
# 测试链接 : https://leetcode.cn/problems/longest-ideal-subsequence/
class Code04_LongestIdealString:
    __java_fields__ = {'n': 'n', 'max': 'max_data'}
    # 数据量太小，线段树的优势不明显
    # 时间复杂度O(n * log e)，n为字符串长度，e为字符集大小
    @staticmethod
    def longestIdealString(s, k):
        k = jcast('int', k)
        jstatic('Arrays', 'fill', Code04_LongestIdealString.max_data, 0)
        v = 0
        p = 0
        ans = jcast('int', 0)
        for cha in jcall(s, 'toCharArray'):
            v = jcast('int', jcast('int', jadd(jcast('int', (cha - jchar('a'))), 1)))
            p = jcast('int', Code04_LongestIdealString.max(jstatic('Math', 'max', jcast('int', (v - k)), 1), jstatic('Math', 'min', jcast('int', jadd(v, k)), Code04_LongestIdealString.n), 1, Code04_LongestIdealString.n, 1))
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(p, 1))))
            Code04_LongestIdealString.update(v, jcast('int', jadd(p, 1)), 1, Code04_LongestIdealString.n, 1)
        return jcast('int', ans)

    n = 0
    max_data = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        jset(Code04_LongestIdealString.max_data, i, jstatic('Math', 'max', Code04_LongestIdealString.max_data[jcast('int', (i << (1 & 31)))], Code04_LongestIdealString.max_data[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))

    # 只有单点更新不需要定义down方法
    # 因为单点更新的任务一定会从线段树头节点直插到某个叶节点
    # 根本没有懒更新这回事
    @staticmethod
    def update(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((l == r) and (jobi == l)):
            Code04_LongestIdealString.max_data[i] = jcast('int', jobv)
        else:
            m = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= m):
                Code04_LongestIdealString.update(jobi, jobv, l, m, jcast('int', (i << (1 & 31))))
            else:
                Code04_LongestIdealString.update(jobi, jobv, jcast('int', jadd(m, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code04_LongestIdealString.up(i)

    @staticmethod
    def max(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code04_LongestIdealString.max_data[i])
        m = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('int', 0)
        if (jobl <= m):
            ans = jcast('int', jstatic('Math', 'max', ans, Code04_LongestIdealString.max(jobl, jobr, l, m, jcast('int', (i << (1 & 31))))))
        if (jobr > m):
            ans = jcast('int', jstatic('Math', 'max', ans, Code04_LongestIdealString.max(jobl, jobr, jcast('int', jadd(m, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_LongestIdealString.n = jcast('int', 26)
Code04_LongestIdealString.max_data = jarray('int', [jcast('int', (jcast('int', jadd(Code04_LongestIdealString.n, 1)) << (2 & 31)))])
