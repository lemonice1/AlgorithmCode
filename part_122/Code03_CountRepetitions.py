# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 统计重复个数
# 如果字符串x删除一些字符，可以得到字符串y，那么就说y可以从x中获得
# 给定s1和a，代表s1拼接a次，记为字符串x
# 给定s2和b，代表s2拼接b次，记为字符串y
# 现在把y拼接m次之后，得到的字符串依然可能从x中获得，返回尽可能大的m
# s1、s2只由小写字母组成
# 1 <= s1长度、s2长度 <= 100
# 1 <= a、b <= 10^6
# 测试链接 : https://leetcode.cn/problems/count-the-repetitions/
class Code03_CountRepetitions:
    __java_fields__ = {}
    # 该题的题解中有很多打败比例优异，但是时间复杂度不是最优的方法
    # 如果数据苛刻一些，就通过不了，所以一定要做到时间复杂度与a、b的值无关
    # 本方法时间复杂度O(s1长度 * s2长度)，一定是最优解，而且比其他方法更好理解
    @staticmethod
    def getMaxRepetitions(str1, a, str2, b):
        a = jcast('int', a)
        b = jcast('int', b)
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        # next[i][j] : 从i位置出发，至少需要多少长度，能找到j字符
        next = jarray('int', [n, 26])
        # 时间复杂度O(s1长度 + s2长度)
        if (not Code03_CountRepetitions.find(s1, n, next, s2)):
            return jcast('int', 0)
        # st[i][p] : 从i位置出发，至少需要多少长度，可以获得2^p个s2
        st = jarray('long', [n, 30])
        # 时间复杂度O(s1长度 * s2长度)
        i = jcast('int', 0)
        cur = 0
        len = 0
        while (i < n):
            cur = jcast('int', i)
            len = jcast('int', 0)
            for c in s2:
                len = jcast('int', jcast('int', jadd(len, next[cur][jcast('int', (c - jchar('a')))])))
                cur = jcast('int', jcast('int', jmod(jcast('int', jadd(cur, next[cur][jcast('int', (c - jchar('a')))])), n)))
            jset(st[i], 0, len)
            i = jcast('int', (i + 1))
        # 时间复杂度O(s1长度)
        p = jcast('int', 1)
        while (p <= 29):
            i = jcast('int', 0)
            while (i < n):
                jset(st[i], p, jcast('long', jadd(st[i][jcast('int', (p - 1))], st[jcast('int', jcast('long', jmod(jcast('long', jadd(st[i][jcast('int', (p - 1))], i)), n)))][jcast('int', (p - 1))])))
                i = jcast('int', (i + 1))
            p = jcast('int', (p + 1))
        ans = jcast('long', 0)
        # 时间复杂度O(1)
        p = jcast('int', 29)
        start = jcast('int', 0)
        while (p >= 0):
            if (jcast('long', jadd(st[jcast('int', jmod(start, n))][p], start)) <= jcast('int', (n * a))):
                ans = jcast('long', jcast('long', jadd(ans, jcast('int', (1 << (p & 31))))))
                start = jcast('int', jcast('long', jadd(start, st[jcast('int', jmod(start, n))][p])))
            p = jcast('int', (p - 1))
        return jcast('int', jcast('int', jcast('long', jdiv(ans, b))))

    # 时间复杂度O(s1长度 + s2长度)
    @staticmethod
    def find(s1, n, next, s2):
        n = jcast('int', n)
        right = jarray('int', [26])
        jstatic('Arrays', 'fill', right, jcast('int', (-1)))
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            jset(right, jcast('int', (s1[i] - jchar('a'))), jcast('int', jadd(i, n)))
            i = jcast('int', (i - 1))
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            jset(right, jcast('int', (s1[i] - jchar('a'))), i)
            j = jcast('int', 0)
            while (j < 26):
                if (right[j] != jcast('int', (-1))):
                    jset(next[i], j, jcast('int', jadd(jcast('int', (right[j] - i)), 1)))
                else:
                    jset(next[i], j, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i - 1))
        for c in s2:
            if (next[0][jcast('int', (c - jchar('a')))] == jcast('int', (-1))):
                return jcast('boolean', False)
        return jcast('boolean', True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


