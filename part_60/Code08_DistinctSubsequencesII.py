# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 不同的子序列 II
# 给定一个字符串 s，计算 s 的 不同非空子序列 的个数
# 因为结果可能很大，答案对 1000000007 取模
# 字符串的 子序列 是经由原字符串删除一些（也可能不删除）
# 字符但不改变剩余字符相对位置的一个新字符串
# 例如，"ace" 是 "abcde" 的一个子序列，但 "aec" 不是
# 测试链接 : https://leetcode.cn/problems/distinct-subsequences-ii/
class Code08_DistinctSubsequencesII:
    __java_fields__ = {}
    # 时间复杂度O(n)，n是字符串s的长度
    @staticmethod
    def distinctSubseqII(s):
        mod = jcast('int', 1000000007)
        str = jcall(s, 'toCharArray')
        cnt = jarray('int', [26])
        all = jcast('int', 1)
        newAdd = 0
        for x in str:
            newAdd = jcast('int', jcast('int', jmod(jcast('int', jadd(jcast('int', (all - cnt[jcast('int', (x - jchar('a')))])), mod)), mod)))
            cnt[jcast('int', (x - jchar('a')))] = jcast('int', jcast('int', jmod(jcast('int', jadd(cnt[jcast('int', (x - jchar('a')))], newAdd)), mod)))
            all = jcast('int', jcast('int', jmod(jcast('int', jadd(all, newAdd)), mod)))
        return jcast('int', jcast('int', jmod(jcast('int', jadd(jcast('int', (all - 1)), mod)), mod)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


