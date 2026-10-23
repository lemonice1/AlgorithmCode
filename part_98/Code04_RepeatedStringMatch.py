# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 重复叠加字符串匹配
# 给定两个字符串a和b，寻找重复叠加字符串a的最小次数，使得字符串b成为叠加后的字符串a的子串
# 如果不存在则返回-1
# 字符串"abc"重复叠加0次是""
# 重复叠加1次是"abc"
# 重复叠加2次是"abcabc"
# 测试链接 : https://leetcode.cn/problems/repeated-string-match/
class Code04_RepeatedStringMatch:
    __java_fields__ = {'MAXN': 'MAXN', 's': 's', 'base': 'base', 'pow': 'pow', 'hash': 'hash_data'}
    @staticmethod
    def repeatedStringMatch(str1, str2):
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        m = jcast('int', jget(s2, 'length'))
        # m / n 向上取整
        k = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(m, n)) - 1)), n)))
        len = jcast('int', 0)
        cnt = jcast('int', 0)
        while (cnt <= k):
            i = jcast('int', 0)
            while (i < n):
                jset(Code04_RepeatedStringMatch.s, ((_java_old_1 := len), (len := jcast('int', (len + (1)))), _java_old_1)[2], s1[i])
                i = jcast('int', (i + 1))
            cnt = jcast('int', (cnt + 1))
        Code04_RepeatedStringMatch.build(len)
        h2 = jcast('long', jcast('int', jadd(jcast('int', (s2[0] - jchar('a'))), 1)))
        i = jcast('int', 1)
        while (i < m):
            h2 = jcast('long', jcast('long', jadd(jcast('long', (jcast('long', jadd(jcast('long', (h2 * Code04_RepeatedStringMatch.base)), s2[i])) - jchar('a'))), 1)))
            i = jcast('int', (i + 1))
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (m - 1)))
        while (r < len):
            if (Code04_RepeatedStringMatch.hash(l, r) == h2):
                return jcast('int', (k if (r < jcast('int', (n * k))) else jcast('int', jadd(k, 1))))
            l = jcast('int', (l + 1))
            r = jcast('int', (r + 1))
        return jcast('int', jcast('int', (-1)))

    MAXN = 0
    s = None
    base = 0
    pow = None
    hash_data = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code04_RepeatedStringMatch.pow[0] = jcast('long', 1)
        i = jcast('int', 1)
        while (i < n):
            Code04_RepeatedStringMatch.pow[i] = jcast('long', jcast('long', (Code04_RepeatedStringMatch.pow[jcast('int', (i - 1))] * Code04_RepeatedStringMatch.base)))
            i = jcast('int', (i + 1))
        Code04_RepeatedStringMatch.hash_data[0] = jcast('long', jcast('int', jadd(jcast('int', (Code04_RepeatedStringMatch.s[0] - jchar('a'))), 1)))
        i = jcast('int', 1)
        while (i < n):
            Code04_RepeatedStringMatch.hash_data[i] = jcast('long', jcast('long', jadd(jcast('long', (jcast('long', jadd(jcast('long', (Code04_RepeatedStringMatch.hash_data[jcast('int', (i - 1))] * Code04_RepeatedStringMatch.base)), Code04_RepeatedStringMatch.s[i])) - jchar('a'))), 1)))
            i = jcast('int', (i + 1))

    @staticmethod
    def hash(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        ans = jcast('long', Code04_RepeatedStringMatch.hash_data[r])
        ans = jcast('long', jcast('long', (ans - (0 if (l == 0) else jcast('long', (Code04_RepeatedStringMatch.hash_data[jcast('int', (l - 1))] * Code04_RepeatedStringMatch.pow[jcast('int', jadd(jcast('int', (r - l)), 1))]))))))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_RepeatedStringMatch.MAXN = jcast('int', 30001)
Code04_RepeatedStringMatch.s = jarray('char', [Code04_RepeatedStringMatch.MAXN])
Code04_RepeatedStringMatch.base = jcast('int', 499)
Code04_RepeatedStringMatch.pow = jarray('long', [Code04_RepeatedStringMatch.MAXN])
Code04_RepeatedStringMatch.hash_data = jarray('long', [Code04_RepeatedStringMatch.MAXN])
