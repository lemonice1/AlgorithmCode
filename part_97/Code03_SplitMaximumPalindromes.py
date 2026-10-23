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

# 不重叠回文子串的最多数目
# 给定一个字符串str和一个正数k
# 你可以随意把str切分成多个子串
# 目的是找到某一种划分方案，有尽可能多的回文子串
# 并且每个回文子串都要求长度>=k、且彼此没有重合的部分
# 返回最多能划分出几个这样的回文子串
# 测试链接 : https://leetcode.cn/problems/maximum-number-of-non-overlapping-palindrome-substrings/
class Code03_SplitMaximumPalindromes:
    __java_fields__ = {'MAXN': 'MAXN', 'ss': 'ss', 'p': 'p', 'n': 'n'}
    # 时间复杂度O(n)
    @staticmethod
    def maxPalindromes(str, k):
        k = jcast('int', k)
        Code03_SplitMaximumPalindromes.manacherss(jcall(str, 'toCharArray'))
        ans = jcast('int', 0)
        next = jcast('int', 0)
        while ((next := Code03_SplitMaximumPalindromes.find(next, k)) != jcast('int', (-1))):
            ans = jcast('int', (ans + 1))
        return jcast('int', ans)

    MAXN = 0
    ss = None
    p = None
    n = 0
    @staticmethod
    def manacherss(a):
        Code03_SplitMaximumPalindromes.n = jcast('int', jcast('int', jadd(jcast('int', (jget(a, 'length') * 2)), 1)))
        i = jcast('int', 0)
        j = jcast('int', 0)
        while (i < Code03_SplitMaximumPalindromes.n):
            jset(Code03_SplitMaximumPalindromes.ss, i, (jchar('#') if (jcast('int', (i & 1)) == 0) else a[((_java_old_1 := j), (j := jcast('int', (j + (1)))), _java_old_1)[2]]))
            i = jcast('int', (i + 1))

    # 扩展串ss从l位置开始往右寻找回文，且ss[l]一定是'#'
    # 一旦有某个中心的回文半径>k，马上返回最右下标
    # 表示找到了距离l最近且长度>=k的回文串
    # 返回的这个最右下标一定要命中'#'
    # 如果没有命中返回(最右下标+1)，让其一定命中'#'
    # 如果不存在距离l最近且长度>=k的回文串，返回-1
    @staticmethod
    def find(l, k):
        l = jcast('int', l)
        k = jcast('int', k)
        i = jcast('int', l)
        c = jcast('int', l)
        r = jcast('int', l)
        len = 0
        while (i < Code03_SplitMaximumPalindromes.n):
            len = jcast('int', (jstatic('Math', 'min', Code03_SplitMaximumPalindromes.p[jcast('int', (jcast('int', (2 * c)) - i))], jcast('int', (r - i))) if (r > i) else 1))
            while (((jcast('int', jadd(i, len)) < Code03_SplitMaximumPalindromes.n) and (jcast('int', (i - len)) >= l)) and (Code03_SplitMaximumPalindromes.ss[jcast('int', jadd(i, len))] == Code03_SplitMaximumPalindromes.ss[jcast('int', (i - len))])):
                if ((len := jcast('int', (len + (1)))) > k):
                    return jcast('int', jcast('int', jadd(jcast('int', jadd(i, k)), (1 if (Code03_SplitMaximumPalindromes.ss[jcast('int', jadd(i, k))] != jchar('#')) else 0))))
            if (jcast('int', jadd(i, len)) > r):
                r = jcast('int', jcast('int', jadd(i, len)))
                c = jcast('int', i)
            Code03_SplitMaximumPalindromes.p[i] = jcast('int', len)
            i = jcast('int', (i + 1))
        return jcast('int', jcast('int', (-1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_SplitMaximumPalindromes.MAXN = jcast('int', 2001)
Code03_SplitMaximumPalindromes.ss = jarray('char', [jcast('int', (Code03_SplitMaximumPalindromes.MAXN << (1 & 31)))])
Code03_SplitMaximumPalindromes.p = jarray('int', [jcast('int', (Code03_SplitMaximumPalindromes.MAXN << (1 & 31)))])
Code03_SplitMaximumPalindromes.n = jcast('int', 0)
