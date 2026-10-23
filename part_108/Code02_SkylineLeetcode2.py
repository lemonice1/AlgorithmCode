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

# 天际线问题(Leetcode测试)
# 测试链接 : https://leetcode.cn/problems/the-skyline-problem/
class Code02_SkylineLeetcode2:
    __java_fields__ = {'MAXN': 'MAXN', 'xsort': 'xsort', 'height': 'height', 'heap': 'heap', 'heapSize': 'heapSize'}
    # 堆结构由自己实现
    @staticmethod
    def getSkyline(arr):
        n = jcast('int', jget(arr, 'length'))
        m = jcast('int', Code02_SkylineLeetcode2.prepare(arr, n))
        i = jcast('int', 1)
        j = jcast('int', 0)
        while (i <= m):
            while ((j < n) and (arr[j][0] <= i)):
                Code02_SkylineLeetcode2.push(arr[j][2], arr[j][1])
                j = jcast('int', (j + 1))
            while ((not Code02_SkylineLeetcode2.isEmpty()) and (Code02_SkylineLeetcode2.peekEnd() < i)):
                Code02_SkylineLeetcode2.poll()
            if (not Code02_SkylineLeetcode2.isEmpty()):
                jset(Code02_SkylineLeetcode2.height, i, Code02_SkylineLeetcode2.peekHeight())
            i = jcast('int', (i + 1))
        ans = jnew('ArrayList')
        i = jcast('int', 1)
        pre = jcast('int', 0)
        while (i <= m):
            if (pre != Code02_SkylineLeetcode2.height[i]):
                jcall(ans, 'add', jstatic('Arrays', 'asList', Code02_SkylineLeetcode2.xsort[i], Code02_SkylineLeetcode2.height[i]))
            pre = jcast('int', Code02_SkylineLeetcode2.height[i])
            i = jcast('int', (i + 1))
        return ans

    MAXN = 0
    xsort = None
    height = None
    heap = None
    heapSize = 0
    @staticmethod
    def prepare(arr, n):
        n = jcast('int', n)
        size = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            jset(Code02_SkylineLeetcode2.xsort, (size := jcast('int', (size + (1)))), arr[i][0])
            jset(Code02_SkylineLeetcode2.xsort, (size := jcast('int', (size + (1)))), jcast('int', (arr[i][1] - 1)))
            jset(Code02_SkylineLeetcode2.xsort, (size := jcast('int', (size + (1)))), arr[i][1])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_SkylineLeetcode2.xsort, 1, jcast('int', jadd(size, 1)))
        m = jcast('int', 1)
        i = jcast('int', 1)
        while (i <= size):
            if (Code02_SkylineLeetcode2.xsort[m] != Code02_SkylineLeetcode2.xsort[i]):
                jset(Code02_SkylineLeetcode2.xsort, (m := jcast('int', (m + (1)))), Code02_SkylineLeetcode2.xsort[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < n):
            jset(arr[i], 0, Code02_SkylineLeetcode2.rank(m, arr[i][0]))
            jset(arr[i], 1, Code02_SkylineLeetcode2.rank(m, jcast('int', (arr[i][1] - 1))))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', arr, 0, n, (lambda a, b: (a[0] - b[0])))
        jstatic('Arrays', 'fill', Code02_SkylineLeetcode2.height, 1, jcast('int', jadd(m, 1)), 0)
        return jcast('int', m)

    @staticmethod
    def rank(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        ans = jcast('int', 0)
        l = jcast('int', 1)
        r = jcast('int', n)
        mid = 0
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code02_SkylineLeetcode2.xsort[mid] >= v):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    @staticmethod
    def isEmpty():
        return jcast('boolean', (Code02_SkylineLeetcode2.heapSize == 0))

    @staticmethod
    def peekHeight():
        return jcast('int', Code02_SkylineLeetcode2.heap[0][0])

    @staticmethod
    def peekEnd():
        return jcast('int', Code02_SkylineLeetcode2.heap[0][1])

    @staticmethod
    def push(h, e):
        h = jcast('int', h)
        e = jcast('int', e)
        jset(Code02_SkylineLeetcode2.heap[Code02_SkylineLeetcode2.heapSize], 0, h)
        jset(Code02_SkylineLeetcode2.heap[Code02_SkylineLeetcode2.heapSize], 1, e)
        Code02_SkylineLeetcode2.heapInsert(((_java_obj_1 := Code02_SkylineLeetcode2), (_java_key_2 := 'heapSize'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def poll():
        Code02_SkylineLeetcode2.swap(0, ((_java_obj_4 := Code02_SkylineLeetcode2), (_java_key_5 := 'heapSize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))))[3])
        Code02_SkylineLeetcode2.heapify(0)

    @staticmethod
    def heapInsert(i):
        i = jcast('int', i)
        while (Code02_SkylineLeetcode2.heap[i][0] > Code02_SkylineLeetcode2.heap[jcast('int', jdiv(jcast('int', (i - 1)), 2))][0]):
            Code02_SkylineLeetcode2.swap(i, jcast('int', jdiv(jcast('int', (i - 1)), 2)))
            i = jcast('int', jcast('int', jdiv(jcast('int', (i - 1)), 2)))

    @staticmethod
    def heapify(i):
        i = jcast('int', i)
        l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
        while (l < Code02_SkylineLeetcode2.heapSize):
            try:
                best = jcast('int', (jcast('int', jadd(l, 1)) if ((jcast('int', jadd(l, 1)) < Code02_SkylineLeetcode2.heapSize) and (Code02_SkylineLeetcode2.heap[jcast('int', jadd(l, 1))][0] > Code02_SkylineLeetcode2.heap[l][0])) else l))
                best = jcast('int', (best if (Code02_SkylineLeetcode2.heap[best][0] > Code02_SkylineLeetcode2.heap[i][0]) else i))
                if (best == i):
                    raise JBreak(None)
                Code02_SkylineLeetcode2.swap(best, i)
                i = jcast('int', best)
                l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = Code02_SkylineLeetcode2.heap[i]
        Code02_SkylineLeetcode2.heap[i] = Code02_SkylineLeetcode2.heap[j]
        Code02_SkylineLeetcode2.heap[j] = tmp

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_SkylineLeetcode2.MAXN = jcast('int', 100001)
Code02_SkylineLeetcode2.xsort = jarray('int', [Code02_SkylineLeetcode2.MAXN])
Code02_SkylineLeetcode2.height = jarray('int', [Code02_SkylineLeetcode2.MAXN])
Code02_SkylineLeetcode2.heap = jarray('int', [Code02_SkylineLeetcode2.MAXN, 2])
Code02_SkylineLeetcode2.heapSize = jcast('int', 0)
