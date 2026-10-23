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

# 字符串哈希得到子串哈希
# 利用字符串哈希的便利性替代KMP算法
# 测试链接 : https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Code03_SubstringHash:
    __java_fields__ = {'MAXN': 'MAXN', 'base': 'base', 'pow': 'pow', 'hash': 'hash_data'}
    @staticmethod
    def strStr(str1, str2):
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        m = jcast('int', jget(s2, 'length'))
        Code03_SubstringHash.build(s1, n)
        h2 = jcast('long', jcast('int', jadd(jcast('int', (s2[0] - jchar('a'))), 1)))
        i = jcast('int', 1)
        while (i < m):
            h2 = jcast('long', jcast('long', jadd(jcast('long', (jcast('long', jadd(jcast('long', (h2 * Code03_SubstringHash.base)), s2[i])) - jchar('a'))), 1)))
            i = jcast('int', (i + 1))
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (m - 1)))
        while (r < n):
            if (Code03_SubstringHash.hash(l, r) == h2):
                return jcast('int', l)
            l = jcast('int', (l + 1))
            r = jcast('int', (r + 1))
        return jcast('int', jcast('int', (-1)))

    # 如下代码是字符串哈希的原理和模版
    # 比如，base = 499, 也就是课上说的选择的质数进制
    # 再比如字符串s如下
    # " c a b e f "
    # 0 1 2 3 4
    # hash[0] = 3 * base的0次方
    # hash[1] = 3 * base的1次方 + 1 * base的0次方
    # hash[2] = 3 * base的2次方 + 1 * base的1次方 + 2 * base的0次方
    # hash[3] = 3 * base的3次方 + 1 * base的2次方 + 2 * base的1次方 + 5 * base的0次方
    # hash[4] = 3 * base的4次方 + 1 * base的3次方 + 2 * base的2次方 + 5 * base的1次方 + 6 *
    # base的0次方
    # hash[i] = hash[i-1] * base + s[i] - 'a' + 1，就是上面说的意思
    # 想计算子串"be"的哈希值 -> 2 * base的1次方 + 5 * base的0次方
    # 子串"be"的哈希值 = hash[3] - hash[1] * base的2次方(子串"be"的长度次方)
    # hash[1] = 3 * base的1次方 + 1 * base的0次方
    # hash[1] * base的2次方 = 3 * base的3次方 + 1 * base的2次方
    # hash[3] = 3 * base的3次方 + 1 * base的2次方 + 2 * base的1次方 + 5 * base的0次方
    # hash[3] - hash[1] * base的2次方 = 2 * base的1次方 + 5 * base的0次方
    # 这样就得到子串"be"的哈希值了
    # 子串s[l...r]的哈希值 = hash[r] - hash[l-1] * base的(r-l+1)次方，就是上面说的意思
    MAXN = 0
    base = 0
    pow = None
    hash_data = None
    @staticmethod
    def build(s, n):
        n = jcast('int', n)
        Code03_SubstringHash.pow[0] = jcast('long', 1)
        i = jcast('int', 1)
        while (i < n):
            Code03_SubstringHash.pow[i] = jcast('long', jcast('long', (Code03_SubstringHash.pow[jcast('int', (i - 1))] * Code03_SubstringHash.base)))
            i = jcast('int', (i + 1))
        Code03_SubstringHash.hash_data[0] = jcast('long', jcast('int', jadd(jcast('int', (s[0] - jchar('a'))), 1)))
        i = jcast('int', 1)
        while (i < n):
            Code03_SubstringHash.hash_data[i] = jcast('long', jcast('long', jadd(jcast('long', (jcast('long', jadd(jcast('long', (Code03_SubstringHash.hash_data[jcast('int', (i - 1))] * Code03_SubstringHash.base)), s[i])) - jchar('a'))), 1)))
            i = jcast('int', (i + 1))

    # 返回s[l...r]的哈希值
    @staticmethod
    def hash(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        ans = jcast('long', Code03_SubstringHash.hash_data[r])
        if (l > 0):
            ans = jcast('long', jcast('long', (ans - jcast('long', (Code03_SubstringHash.hash_data[jcast('int', (l - 1))] * Code03_SubstringHash.pow[jcast('int', jadd(jcast('int', (r - l)), 1))])))))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_SubstringHash.MAXN = jcast('int', 100005)
Code03_SubstringHash.base = jcast('int', 499)
Code03_SubstringHash.pow = jarray('long', [Code03_SubstringHash.MAXN])
Code03_SubstringHash.hash_data = jarray('long', [Code03_SubstringHash.MAXN])
