# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 自由之路
# 题目描述比较多，打开链接查看
# 测试链接 : https://leetcode.cn/problems/freedom-trail/
class Code03_FreedomTrail:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXC': 'MAXC', 'ring': 'ring', 'key': 'key', 'size': 'size', 'where': 'where', 'dp': 'dp', 'n': 'n', 'm': 'm'}
    # 为了让所有语言的同学都可以理解
    # 本算法自行维护所需数组和状态，不依赖额外容器接口
    # 只使用最简单的数组结构
    MAXN = 0
    MAXC = 0
    ring = None
    key = None
    size = None
    where = None
    dp = None
    n = 0
    m = 0
    @staticmethod
    def build(r, k):
        i = jcast('int', 0)
        while (i < Code03_FreedomTrail.MAXC):
            Code03_FreedomTrail.size[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        Code03_FreedomTrail.n = jcast('int', jcall(r, 'length'))
        Code03_FreedomTrail.m = jcast('int', jcall(k, 'length'))
        i = jcast('int', 0)
        v = 0
        while (i < Code03_FreedomTrail.n):
            v = jcast('int', jcast('int', (jcall(r, 'charAt', i) - jchar('a'))))
            jset(Code03_FreedomTrail.where[v], ((_java_obj_1 := Code03_FreedomTrail.size), (_java_key_2 := v), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], i)
            Code03_FreedomTrail.ring[i] = jcast('int', v)
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < Code03_FreedomTrail.m):
            jset(Code03_FreedomTrail.key, i, jcast('int', (jcall(k, 'charAt', i) - jchar('a'))))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < Code03_FreedomTrail.n):
            j = jcast('int', 0)
            while (j < Code03_FreedomTrail.m):
                jset(Code03_FreedomTrail.dp[i], j, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def findRotateSteps(r, k):
        Code03_FreedomTrail.build(r, k)
        return jcast('int', Code03_FreedomTrail.f(0, 0))

    # 指针当前指着轮盘i位置的字符，要搞定key[j....]所有字符，最小代价返回
    @staticmethod
    def f(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if (j == Code03_FreedomTrail.m):
            # key长度是m
            # 都搞定
            return jcast('int', 0)
        if (Code03_FreedomTrail.dp[i][j] != jcast('int', (-1))):
            return jcast('int', Code03_FreedomTrail.dp[i][j])
        ans = 0
        if (Code03_FreedomTrail.ring[i] == Code03_FreedomTrail.key[j]):
            # ring b
            # i
            # key  b
            # j
            ans = jcast('int', jcast('int', jadd(1, Code03_FreedomTrail.f(i, jcast('int', jadd(j, 1))))))
        else:
            # 轮盘处在i位置，ring[i] != key[j]
            # jump1 : 顺时针找到最近的key[j]字符在轮盘的什么位置
            # distance1 : 从i顺时针走向jump1有多远
            jump1 = jcast('int', Code03_FreedomTrail.clock(i, Code03_FreedomTrail.key[j]))
            distance1 = jcast('int', (jcast('int', (jump1 - i)) if (jump1 > i) else jcast('int', jadd(jcast('int', (Code03_FreedomTrail.n - i)), jump1))))
            # jump2 : 逆时针找到最近的key[j]字符在轮盘的什么位置
            # distance2 : 从i逆时针走向jump2有多远
            jump2 = jcast('int', Code03_FreedomTrail.counterClock(i, Code03_FreedomTrail.key[j]))
            distance2 = jcast('int', (jcast('int', (i - jump2)) if (i > jump2) else jcast('int', (jcast('int', jadd(i, Code03_FreedomTrail.n)) - jump2))))
            ans = jcast('int', jstatic('Math', 'min', jcast('int', jadd(distance1, Code03_FreedomTrail.f(jump1, j))), jcast('int', jadd(distance2, Code03_FreedomTrail.f(jump2, j)))))
        jset(Code03_FreedomTrail.dp[i], j, ans)
        return jcast('int', ans)

    # 从i开始，顺时针找到最近的v在轮盘的什么位置
    @staticmethod
    def clock(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        l = jcast('int', 0)
        # size[v] : 属于v这个字符的下标有几个
        r = jcast('int', jcast('int', (Code03_FreedomTrail.size[v] - 1)))
        m = 0
        # sorted[0...size[v]-1]收集了所有的下标，并且有序
        sorted = Code03_FreedomTrail.where[v]
        find = jcast('int', jcast('int', (-1)))
        # 有序数组中，找>i尽量靠左的下标
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (sorted[m] > i):
                find = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        # 找到了就返回
        # 没找到，那i顺指针一定先走到最小的下标
        return jcast('int', (sorted[find] if (find != jcast('int', (-1))) else sorted[0]))

    @staticmethod
    def counterClock(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (Code03_FreedomTrail.size[v] - 1)))
        m = 0
        sorted = Code03_FreedomTrail.where[v]
        find = jcast('int', jcast('int', (-1)))
        # 有序数组中，找<i尽量靠右的下标
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (sorted[m] < i):
                find = jcast('int', m)
                l = jcast('int', jcast('int', jadd(m, 1)))
            else:
                r = jcast('int', jcast('int', (m - 1)))
        # 找到了就返回
        # 没找到，那i逆指针一定先走到最大的下标
        return jcast('int', (sorted[find] if (find != jcast('int', (-1))) else sorted[jcast('int', (Code03_FreedomTrail.size[v] - 1))]))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_FreedomTrail.MAXN = jcast('int', 101)
Code03_FreedomTrail.MAXC = jcast('int', 26)
Code03_FreedomTrail.ring = jarray('int', [Code03_FreedomTrail.MAXN])
Code03_FreedomTrail.key = jarray('int', [Code03_FreedomTrail.MAXN])
Code03_FreedomTrail.size = jarray('int', [Code03_FreedomTrail.MAXC])
Code03_FreedomTrail.where = jarray('int', [Code03_FreedomTrail.MAXC, Code03_FreedomTrail.MAXN])
Code03_FreedomTrail.dp = jarray('int', [Code03_FreedomTrail.MAXN, Code03_FreedomTrail.MAXN])
Code03_FreedomTrail.n = jcast('int', 0)
Code03_FreedomTrail.m = jcast('int', 0)
