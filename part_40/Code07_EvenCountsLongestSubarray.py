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

# 每个元音包含偶数次的最长子字符串
# 给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度
# 每个元音字母，即 'a'，'e'，'i'，'o'，'u'
# 在子字符串中都恰好出现了偶数次。
# 测试链接 : https://leetcode.cn/problems/find-the-longest-substring-containing-vowels-in-even-counts/
class Code07_EvenCountsLongestSubarray:
    __java_fields__ = {}
    @staticmethod
    def findTheLongestSubstring(s):
        n = jcast('int', jcall(s, 'length'))
        # 只有5个元音字符，状态就5位
        map = jarray('int', [32])
        # map[0...31] = -2
        # map[01100] = -2, 这个状态之前没出现过
        jstatic('Arrays', 'fill', map, jcast('int', (-2)))
        map[0] = jcast('int', jcast('int', (-1)))
        ans = jcast('int', 0)
        i = jcast('int', 0)
        status = jcast('int', 0)
        m = 0
        while (i < n):
            # status : 0....i-1字符串上，aeiou的奇偶性
            # s[i] = 当前字符
            # 情况1 : 当前字符不是元音，status不变
            # 情况2 : 当前字符是元音，a~u(0~4)，修改相应的状态
            m = jcast('int', Code07_EvenCountsLongestSubarray.move(jcall(s, 'charAt', i)))
            if (m != jcast('int', (-1))):
                status = jcast('int', jcast('int', (status ^ jcast('int', (1 << (m & 31))))))
            # status:  0....i字符串上，aeiou的奇偶性
            # 同样的状态，之前最早出现在哪
            if (map[status] != jcast('int', (-2))):
                ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', (i - map[status]))))
            else:
                map[status] = jcast('int', i)
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def move(cha):
        cha = jcast('char', cha)
        _java_switch_1 = cha
        _java_case_2 = 5
        if _java_switch_1 == (jchar('a')):
            _java_case_2 = 0
        elif _java_switch_1 == (jchar('e')):
            _java_case_2 = 1
        elif _java_switch_1 == (jchar('i')):
            _java_case_2 = 2
        elif _java_switch_1 == (jchar('o')):
            _java_case_2 = 3
        elif _java_switch_1 == (jchar('u')):
            _java_case_2 = 4
        try:
            if _java_case_2 <= 0:
                return jcast('int', 0)
            if _java_case_2 <= 1:
                return jcast('int', 1)
            if _java_case_2 <= 2:
                return jcast('int', 2)
            if _java_case_2 <= 3:
                return jcast('int', 3)
            if _java_case_2 <= 4:
                return jcast('int', 4)
            if _java_case_2 <= 5:
                return jcast('int', jcast('int', (-1)))
        except JBreak as _java_break_3:
            if _java_break_3.label not in (None,):
                raise

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


