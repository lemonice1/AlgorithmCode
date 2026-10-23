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

# 统计元音字母序列的数目
# 给你一个整数n，请你帮忙统计一下我们可以按下述规则形成多少个长度为n的字符串：
# 字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
# 每个元音 'a' 后面都只能跟着 'e'
# 每个元音 'e' 后面只能跟着 'a' 或者是 'i'
# 每个元音 'i' 后面 不能 再跟着另一个 'i'
# 每个元音 'o' 后面只能跟着 'i' 或者是 'u'
# 每个元音 'u' 后面只能跟着 'a'
# 由于答案可能会很大，结果对1000000007取模
# 测试链接 : https://leetcode.cn/problems/count-vowels-permutation/
class Code06_CountVowelsPermutation:
    __java_fields__ = {'MOD': 'MOD'}
    # 正式方法
    # 矩阵快速幂
    # 时间复杂度O(logn)
    MOD = 0
    @staticmethod
    def countVowelPermutation(n):
        n = jcast('int', n)
        # 长度为1的时候，以a、e、i、o、u结尾的合法数量
        start = jarray('int', [None, None], [[1, 1, 1, 1, 1]])
        base = jarray('int', [None, None], [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [1, 1, 0, 1, 1], [0, 0, 1, 0, 1], [1, 0, 0, 0, 0]])
        ans = Code06_CountVowelsPermutation.multiply(start, Code06_CountVowelsPermutation.power(base, jcast('int', (n - 1))))
        ret = jcast('int', 0)
        for a in ans[0]:
            ret = jcast('int', jcast('int', jmod(jcast('int', jadd(ret, a)), Code06_CountVowelsPermutation.MOD)))
        return jcast('int', ret)

    # 矩阵相乘 + 乘法取模
    # a的列数一定要等于b的行数
    @staticmethod
    def multiply(a, b):
        n = jcast('int', jget(a, 'length'))
        m = jcast('int', jget(b[0], 'length'))
        k = jcast('int', jget(a[0], 'length'))
        ans = jarray('int', [n, m])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                c = jcast('int', 0)
                while (c < k):
                    jset(ans[i], j, jcast('int', jcast('long', jmod(jcast('long', jadd(jcast('long', (jcast('long', a[i][c]) * b[c][j])), ans[i][j])), Code06_CountVowelsPermutation.MOD))))
                    c = jcast('int', (c + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return ans

    # 矩阵快速幂
    @staticmethod
    def power(m, p):
        p = jcast('int', p)
        n = jcast('int', jget(m, 'length'))
        ans = jarray('int', [n, n])
        i = jcast('int', 0)
        while (i < n):
            jset(ans[i], i, 1)
            i = jcast('int', (i + 1))
        while (p != 0):
            if (jcast('int', (p & 1)) != 0):
                ans = Code06_CountVowelsPermutation.multiply(ans, m)
            m = Code06_CountVowelsPermutation.multiply(m, m)
            p = jcast('int', jcast('int', (p >> (1 & 31))))
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_CountVowelsPermutation.MOD = jcast('int', 1000000007)
