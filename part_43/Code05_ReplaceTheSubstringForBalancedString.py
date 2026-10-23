# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 替换子串得到平衡字符串
# 有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。
# 假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。
# 给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。
# 你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。
# 请返回待替换子串的最小可能长度。
# 如果原字符串自身就是一个平衡字符串，则返回 0。
# 测试链接 : https://leetcode.cn/problems/replace-the-substring-for-balanced-string/
class Code05_ReplaceTheSubstringForBalancedString:
    __java_fields__ = {}
    @staticmethod
    def balancedString(str):
        n = jcast('int', jcall(str, 'length'))
        s = jarray('int', [n])
        cnts = jarray('int', [4])
        i = jcast('int', 0)
        while (i < n):
            c = jcast('char', jcall(str, 'charAt', i))
            s[i] = jcast('int', (1 if (c == jchar('W')) else (2 if (c == jchar('E')) else (3 if (c == jchar('R')) else 0))))
            ((_java_obj_1 := cnts), (_java_key_2 := s[i]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
            i = jcast('int', (i + 1))
        debt = jcast('int', 0)
        i = jcast('int', 0)
        while (i < 4):
            if (cnts[i] < jcast('int', jdiv(n, 4))):
                cnts[i] = jcast('int', 0)
            else:
                cnts[i] = jcast('int', jcast('int', (jcast('int', jdiv(n, 4)) - cnts[i])))
                debt = jcast('int', jcast('int', (debt - cnts[i])))
            i = jcast('int', (i + 1))
        if (debt == 0):
            return jcast('int', 0)
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        l = jcast('int', 0)
        r = jcast('int', 0)
        while (r < n):
            if (((_java_obj_4 := cnts), (_java_key_5 := s[r]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4] < 0):
                debt = jcast('int', (debt - 1))
            if (debt == 0):
                while (cnts[s[l]] > 0):
                    ((_java_obj_8 := cnts), (_java_key_9 := s[((_java_old_7 := l), (l := jcast('int', (l + (1)))), _java_old_7)[2]]), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (-1)))), _java_old_10)[4]
                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(jcast('int', (r - l)), 1))))
            r = jcast('int', (r + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


