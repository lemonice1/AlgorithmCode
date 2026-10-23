# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 得到回文串的最少操作次数
# 给你一个只包含小写英文字母的字符串s
# 每一次操作可以选择s中两个相邻的字符进行交换
# 返回将s变成回文串的最少操作次数
# 输入数据会确保s一定能变成一个回文串
# 测试链接 : https://leetcode.cn/problems/minimum-number-of-moves-to-make-palindrome/
class Code05_MinimumNumberOfMovesToMakePalindrome:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'n': 'n', 's': 's', 'end': 'end', 'pre': 'pre', 'tree': 'tree', 'arr': 'arr', 'help': 'help'}
    MAXN = 0
    MAXV = 0
    n = 0
    s = None
    # 所有字符的位置列表
    end = None
    pre = None
    # 树状数组
    tree = None
    # 归并分治
    arr = None
    help = None
    @staticmethod
    def build():
        jstatic('Arrays', 'fill', Code05_MinimumNumberOfMovesToMakePalindrome.end, 0, Code05_MinimumNumberOfMovesToMakePalindrome.MAXV, 0)
        jstatic('Arrays', 'fill', Code05_MinimumNumberOfMovesToMakePalindrome.arr, 1, jcast('int', jadd(Code05_MinimumNumberOfMovesToMakePalindrome.n, 1)), 0)
        jstatic('Arrays', 'fill', Code05_MinimumNumberOfMovesToMakePalindrome.tree, 1, jcast('int', jadd(Code05_MinimumNumberOfMovesToMakePalindrome.n, 1)), 0)
        i = jcast('int', 1)
        while (i <= Code05_MinimumNumberOfMovesToMakePalindrome.n):
            Code05_MinimumNumberOfMovesToMakePalindrome.add(i, 1)
            i = jcast('int', (i + 1))

    # 字符v把下标j加入列表
    @staticmethod
    def push(v, j):
        v = jcast('int', v)
        j = jcast('int', j)
        Code05_MinimumNumberOfMovesToMakePalindrome.pre[j] = jcast('int', Code05_MinimumNumberOfMovesToMakePalindrome.end[v])
        Code05_MinimumNumberOfMovesToMakePalindrome.end[v] = jcast('int', j)

    # 弹出当前v字符最后的下标
    @staticmethod
    def pop(v):
        v = jcast('int', v)
        ans = jcast('int', Code05_MinimumNumberOfMovesToMakePalindrome.end[v])
        Code05_MinimumNumberOfMovesToMakePalindrome.end[v] = jcast('int', Code05_MinimumNumberOfMovesToMakePalindrome.pre[Code05_MinimumNumberOfMovesToMakePalindrome.end[v]])
        return jcast('int', ans)

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code05_MinimumNumberOfMovesToMakePalindrome.n):
            Code05_MinimumNumberOfMovesToMakePalindrome.tree[i] = jcast('int', jcast('int', jadd(Code05_MinimumNumberOfMovesToMakePalindrome.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code05_MinimumNumberOfMovesToMakePalindrome.lowbit(i))))

    @staticmethod
    def sum(i):
        i = jcast('int', i)
        ans = jcast('int', 0)
        while (i > 0):
            ans = jcast('int', jcast('int', jadd(ans, Code05_MinimumNumberOfMovesToMakePalindrome.tree[i])))
            i = jcast('int', jcast('int', (i - Code05_MinimumNumberOfMovesToMakePalindrome.lowbit(i))))
        return jcast('int', ans)

    # 时间复杂度O(n * logn)
    @staticmethod
    def minMovesToMakePalindrome(str):
        Code05_MinimumNumberOfMovesToMakePalindrome.s = jcall(str, 'toCharArray')
        Code05_MinimumNumberOfMovesToMakePalindrome.n = jcast('int', jget(Code05_MinimumNumberOfMovesToMakePalindrome.s, 'length'))
        Code05_MinimumNumberOfMovesToMakePalindrome.build()
        i = jcast('int', 0)
        j = jcast('int', 1)
        while (i < Code05_MinimumNumberOfMovesToMakePalindrome.n):
            Code05_MinimumNumberOfMovesToMakePalindrome.push(jcast('int', (Code05_MinimumNumberOfMovesToMakePalindrome.s[i] - jchar('a'))), j)
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        # arr[i]记录每个位置的字符最终要去哪
        i = jcast('int', 0)
        l = jcast('int', 1)
        r = 0
        k = 0
        while (i < Code05_MinimumNumberOfMovesToMakePalindrome.n):
            if (Code05_MinimumNumberOfMovesToMakePalindrome.arr[l] == 0):
                r = jcast('int', Code05_MinimumNumberOfMovesToMakePalindrome.pop(jcast('int', (Code05_MinimumNumberOfMovesToMakePalindrome.s[i] - jchar('a')))))
                if (l < r):
                    k = jcast('int', Code05_MinimumNumberOfMovesToMakePalindrome.sum(l))
                    Code05_MinimumNumberOfMovesToMakePalindrome.arr[l] = jcast('int', k)
                    Code05_MinimumNumberOfMovesToMakePalindrome.arr[r] = jcast('int', jcast('int', jadd(jcast('int', (Code05_MinimumNumberOfMovesToMakePalindrome.n - k)), 1)))
                else:
                    Code05_MinimumNumberOfMovesToMakePalindrome.arr[l] = jcast('int', jcast('int', jdiv(jcast('int', jadd(1, Code05_MinimumNumberOfMovesToMakePalindrome.n)), 2)))
                Code05_MinimumNumberOfMovesToMakePalindrome.add(r, jcast('int', (-1)))
            i = jcast('int', (i + 1))
            l = jcast('int', (l + 1))
        return jcast('int', Code05_MinimumNumberOfMovesToMakePalindrome.number(1, Code05_MinimumNumberOfMovesToMakePalindrome.n))

    @staticmethod
    def number(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return jcast('int', 0)
        m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        return jcast('int', jcast('int', jadd(jcast('int', jadd(Code05_MinimumNumberOfMovesToMakePalindrome.number(l, m), Code05_MinimumNumberOfMovesToMakePalindrome.number(jcast('int', jadd(m, 1)), r))), Code05_MinimumNumberOfMovesToMakePalindrome.merge(l, m, r))))

    @staticmethod
    def merge(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        ans = jcast('int', 0)
        i = jcast('int', m)
        j = jcast('int', r)
        while (i >= l):
            while ((j >= jcast('int', jadd(m, 1))) and (Code05_MinimumNumberOfMovesToMakePalindrome.arr[i] <= Code05_MinimumNumberOfMovesToMakePalindrome.arr[j])):
                j = jcast('int', (j - 1))
            ans = jcast('int', jcast('int', jadd(ans, jcast('int', (j - m)))))
            i = jcast('int', (i - 1))
        i = jcast('int', l)
        a = jcast('int', l)
        b = jcast('int', jcast('int', jadd(m, 1)))
        while ((a <= m) and (b <= r)):
            jset(Code05_MinimumNumberOfMovesToMakePalindrome.help, ((_java_old_3 := i), (i := jcast('int', (i + (1)))), _java_old_3)[2], (Code05_MinimumNumberOfMovesToMakePalindrome.arr[((_java_old_1 := a), (a := jcast('int', (a + (1)))), _java_old_1)[2]] if (Code05_MinimumNumberOfMovesToMakePalindrome.arr[a] <= Code05_MinimumNumberOfMovesToMakePalindrome.arr[b]) else Code05_MinimumNumberOfMovesToMakePalindrome.arr[((_java_old_2 := b), (b := jcast('int', (b + (1)))), _java_old_2)[2]]))
        while (a <= m):
            jset(Code05_MinimumNumberOfMovesToMakePalindrome.help, ((_java_old_5 := i), (i := jcast('int', (i + (1)))), _java_old_5)[2], Code05_MinimumNumberOfMovesToMakePalindrome.arr[((_java_old_4 := a), (a := jcast('int', (a + (1)))), _java_old_4)[2]])
        while (b <= r):
            jset(Code05_MinimumNumberOfMovesToMakePalindrome.help, ((_java_old_7 := i), (i := jcast('int', (i + (1)))), _java_old_7)[2], Code05_MinimumNumberOfMovesToMakePalindrome.arr[((_java_old_6 := b), (b := jcast('int', (b + (1)))), _java_old_6)[2]])
        i = jcast('int', l)
        while (i <= r):
            Code05_MinimumNumberOfMovesToMakePalindrome.arr[i] = jcast('int', Code05_MinimumNumberOfMovesToMakePalindrome.help[i])
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_MinimumNumberOfMovesToMakePalindrome.MAXN = jcast('int', 2001)
Code05_MinimumNumberOfMovesToMakePalindrome.MAXV = jcast('int', 26)
Code05_MinimumNumberOfMovesToMakePalindrome.n = jcast('int', 0)
Code05_MinimumNumberOfMovesToMakePalindrome.s = None
Code05_MinimumNumberOfMovesToMakePalindrome.end = jarray('int', [Code05_MinimumNumberOfMovesToMakePalindrome.MAXV])
Code05_MinimumNumberOfMovesToMakePalindrome.pre = jarray('int', [Code05_MinimumNumberOfMovesToMakePalindrome.MAXN])
Code05_MinimumNumberOfMovesToMakePalindrome.tree = jarray('int', [Code05_MinimumNumberOfMovesToMakePalindrome.MAXN])
Code05_MinimumNumberOfMovesToMakePalindrome.arr = jarray('int', [Code05_MinimumNumberOfMovesToMakePalindrome.MAXN])
Code05_MinimumNumberOfMovesToMakePalindrome.help = jarray('int', [Code05_MinimumNumberOfMovesToMakePalindrome.MAXN])
