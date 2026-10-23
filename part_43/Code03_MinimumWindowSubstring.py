# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最小覆盖子串
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串
# 如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
# 测试链接 : https://leetcode.cn/problems/minimum-window-substring/
class Code03_MinimumWindowSubstring:
    __java_fields__ = {}
    @staticmethod
    def minWindow(str, tar):
        s = jcall(str, 'toCharArray')
        t = jcall(tar, 'toCharArray')
        # 每种字符的欠债情况
        # cnts[i] = 负数，代表字符i有负债
        # cnts[i] = 正数，代表字符i有盈余
        cnts = jarray('int', [256])
        for cha in t:
            cnts[cha] = jcast('int', (cnts[cha] - 1))
        # 最小覆盖子串的长度
        len = jcast('int', jget(Integer, 'MAX_VALUE'))
        # 从哪个位置开头，发现的最小覆盖子串
        start = jcast('int', 0)
        # 总债务
        debt = jcast('int', jget(t, 'length'))
        l = jcast('int', 0)
        r = jcast('int', 0)
        while (r < jget(s, 'length')):
            # 窗口右边界向右，给出字符
            if (((_java_obj_1 := cnts), (_java_key_2 := s[r]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4] < 0):
                debt = jcast('int', (debt - 1))
            if (debt == 0):
                # 窗口左边界向右，拿回字符
                while (cnts[s[l]] > 0):
                    ((_java_obj_5 := cnts), (_java_key_6 := s[((_java_old_4 := l), (l := jcast('int', (l + (1)))), _java_old_4)[2]]), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4]
                # 以r位置结尾的达标窗口，更新答案
                if (jcast('int', jadd(jcast('int', (r - l)), 1)) < len):
                    len = jcast('int', jcast('int', jadd(jcast('int', (r - l)), 1)))
                    start = jcast('int', l)
            r = jcast('int', (r + 1))
        return ('' if (len == jget(Integer, 'MAX_VALUE')) else jcall(str, 'substring', start, jcast('int', jadd(start, len))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


