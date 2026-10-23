# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 独特子串的数量
# 给你一个由数字组成的字符串s
# 返回s中独特子字符串数量
# 其中的每一个数字出现的频率都相同
# 测试链接 : https://leetcode.cn/problems/unique-substrings-with-equal-digit-frequency/
class Code02_NumberOfUniqueString:
    __java_fields__ = {}
    @staticmethod
    def equalDigitFrequency(str):
        base = jcast('long', 499)
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        set = jnew('HashSet')
        cnt = jarray('int', [10])
        i = jcast('int', 0)
        while (i < n):
            jstatic('Arrays', 'fill', cnt, 0)
            hashCode = jcast('long', 0)
            curVal = jcast('int', 0)
            maxCnt = jcast('int', 0)
            maxCntKinds = jcast('int', 0)
            allKinds = jcast('int', 0)
            j = jcast('int', i)
            while (j < n):
                curVal = jcast('int', jcast('int', (s[j] - jchar('0'))))
                hashCode = jcast('long', jcast('long', jadd(jcast('long', jadd(jcast('long', (hashCode * base)), curVal)), 1)))
                cnt[curVal] = jcast('int', (cnt[curVal] + 1))
                if (cnt[curVal] == 1):
                    allKinds = jcast('int', (allKinds + 1))
                if (cnt[curVal] > maxCnt):
                    maxCnt = jcast('int', cnt[curVal])
                    maxCntKinds = jcast('int', 1)
                else:
                    if (cnt[curVal] == maxCnt):
                        maxCntKinds = jcast('int', (maxCntKinds + 1))
                if (maxCntKinds == allKinds):
                    jcall(set, 'add', hashCode)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', jcall(set, 'size'))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


