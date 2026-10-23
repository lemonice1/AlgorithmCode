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

# 至少有K个重复字符的最长子串
# 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串
# 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度
# 如果不存在这样的子字符串，则返回 0。
# 测试链接 : https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/
class Code07_LongestSubstringWithAtLeastKRepeating:
    __java_fields__ = {}
    @staticmethod
    def longestSubstring(str, k):
        k = jcast('int', k)
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        cnts = jarray('int', [256])
        ans = jcast('int', 0)
        # 每次要求子串必须含有require种字符，每种字符都必须>=k次，这样的最长子串是多长
        require = jcast('int', 1)
        while (require <= 26):
            jstatic('Arrays', 'fill', cnts, 0)
            # collect : 窗口中一共收集到的种类数
            # satisfy : 窗口中达标的种类数(次数>=k)
            l = jcast('int', 0)
            r = jcast('int', 0)
            collect = jcast('int', 0)
            satisfy = jcast('int', 0)
            while (r < n):
                ((_java_obj_1 := cnts), (_java_key_2 := s[r]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
                if (cnts[s[r]] == 1):
                    collect = jcast('int', (collect + 1))
                if (cnts[s[r]] == k):
                    satisfy = jcast('int', (satisfy + 1))
                # l....r 种类超了！
                # l位置的字符，窗口中吐出来！
                while (collect > require):
                    if (cnts[s[l]] == 1):
                        collect = jcast('int', (collect - 1))
                    if (cnts[s[l]] == k):
                        satisfy = jcast('int', (satisfy - 1))
                    ((_java_obj_5 := cnts), (_java_key_6 := s[((_java_old_4 := l), (l := jcast('int', (l + (1)))), _java_old_4)[2]]), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4]
                # l.....r : 子串以r位置的字符结尾，且种类数不超的，最大长度！
                if (satisfy == require):
                    ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(jcast('int', (r - l)), 1))))
                r = jcast('int', (r + 1))
            require = jcast('int', (require + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


