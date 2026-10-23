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

# 无重复字符的最长子串
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
# 测试链接 : https://leetcode.cn/problems/longest-substring-without-repeating-characters/
class Code02_LongestSubstringWithoutRepeatingCharacters:
    __java_fields__ = {}
    @staticmethod
    def lengthOfLongestSubstring(str):
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        # char -> int -> 0 ~ 255
        # 每一种字符上次出现的位置
        last = jarray('int', [256])
        # 所有字符都没有上次出现的位置
        jstatic('Arrays', 'fill', last, jcast('int', (-1)))
        # 不含有重复字符的 最长子串 的长度
        ans = jcast('int', 0)
        l = jcast('int', 0)
        r = jcast('int', 0)
        while (r < n):
            l = jcast('int', jstatic('Math', 'max', l, jcast('int', jadd(last[s[r]], 1))))
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(jcast('int', (r - l)), 1))))
            # 更新当前字符上一次出现的位置
            jset(last, s[r], r)
            r = jcast('int', (r + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


