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

# 合法排列数对，Python版
# 给定n个数对，每个数对(a, b)，其中 a != b，并且不存在相同的数对
# 希望所有数对形成首尾相接的样子，叫做合法排列，比如以下的数对
# [5,1] [4,5] [11,9] [9,4] 合法排列为 [11,9] [9,4] [4,5] [5,1]
# 注意每个数对必须使用且仅用1次，数据保证存在合法排列，返回任何一个都可以
# 1 <= n <= 10^5
# 0 <= 数字 <= 10^9
# 测试链接 : https://leetcode.cn/problems/valid-arrangement-of-pairs/
# 在线评测时提交题目要求的方法接口，并一并提供使用到的公共辅助模块
class Code03_Arrangement1:
    __java_fields__ = {}
    class Solution:
        __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'pair': 'pair', 'sortv': 'sortv', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'cur': 'cur', 'outDeg': 'outDeg', 'inDeg': 'inDeg', 'path': 'path', 'cntp': 'cntp'}
        MAXN = 0
        n = 0
        m = 0
        pair = None
        sortv = None
        head = None
        nxt = None
        to = None
        cntg = 0
        cur = None
        outDeg = None
        inDeg = None
        path = None
        cntp = 0
        @staticmethod
        def addEdge(u, v):
            u = jcast('int', u)
            v = jcast('int', v)
            jset(Code03_Arrangement1.Solution.nxt, ((_java_obj_1 := Code03_Arrangement1.Solution), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_Arrangement1.Solution.head[u])
            jset(Code03_Arrangement1.Solution.to, Code03_Arrangement1.Solution.cntg, v)
            jset(Code03_Arrangement1.Solution.head, u, Code03_Arrangement1.Solution.cntg)

        @staticmethod
        def kth(num):
            num = jcast('int', num)
            l = jcast('int', 1)
            r = jcast('int', Code03_Arrangement1.Solution.n)
            ans = jcast('int', 0)
            while (l <= r):
                mid = jcast('int', jcast('int', jushr(jcast('int', jadd(l, r)), 1, 32)))
                if (Code03_Arrangement1.Solution.sortv[mid] >= num):
                    ans = jcast('int', mid)
                    r = jcast('int', jcast('int', (mid - 1)))
                else:
                    l = jcast('int', jcast('int', jadd(mid, 1)))
            return jcast('int', ans)

        @staticmethod
        def prepare():
            len = jcast('int', 0)
            i = jcast('int', 0)
            while (i < Code03_Arrangement1.Solution.m):
                jset(Code03_Arrangement1.Solution.sortv, (len := jcast('int', (len + (1)))), Code03_Arrangement1.Solution.pair[i][0])
                jset(Code03_Arrangement1.Solution.sortv, (len := jcast('int', (len + (1)))), Code03_Arrangement1.Solution.pair[i][1])
                i = jcast('int', (i + 1))
            jstatic('Arrays', 'sort', Code03_Arrangement1.Solution.sortv, 1, jcast('int', jadd(len, 1)))
            jset(Code03_Arrangement1.Solution, 'n', 1)
            i = jcast('int', 2)
            while (i <= len):
                if (Code03_Arrangement1.Solution.sortv[Code03_Arrangement1.Solution.n] != Code03_Arrangement1.Solution.sortv[i]):
                    jset(Code03_Arrangement1.Solution.sortv, ((_java_obj_4 := Code03_Arrangement1.Solution), (_java_key_5 := 'n'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code03_Arrangement1.Solution.sortv[i])
                i = jcast('int', (i + 1))
            jset(Code03_Arrangement1.Solution, 'cntg', jset(Code03_Arrangement1.Solution, 'cntp', 0))
            i = jcast('int', 1)
            while (i <= Code03_Arrangement1.Solution.n):
                jset(Code03_Arrangement1.Solution.head, i, jset(Code03_Arrangement1.Solution.outDeg, i, jset(Code03_Arrangement1.Solution.inDeg, i, 0)))
                i = jcast('int', (i + 1))

        @staticmethod
        def connect():
            i = jcast('int', 0)
            u = 0
            v = 0
            while (i < Code03_Arrangement1.Solution.m):
                u = jcast('int', Code03_Arrangement1.Solution.kth(Code03_Arrangement1.Solution.pair[i][0]))
                v = jcast('int', Code03_Arrangement1.Solution.kth(Code03_Arrangement1.Solution.pair[i][1]))
                ((_java_obj_7 := Code03_Arrangement1.Solution.outDeg), (_java_key_8 := u), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]
                ((_java_obj_10 := Code03_Arrangement1.Solution.inDeg), (_java_key_11 := v), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]
                Code03_Arrangement1.Solution.addEdge(u, v)
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code03_Arrangement1.Solution.n):
                jset(Code03_Arrangement1.Solution.cur, i, Code03_Arrangement1.Solution.head[i])
                i = jcast('int', (i + 1))

        @staticmethod
        def directedStart():
            start = jcast('int', jcast('int', (-1)))
            end = jcast('int', jcast('int', (-1)))
            i = jcast('int', 1)
            while (i <= Code03_Arrangement1.Solution.n):
                v = jcast('int', jcast('int', (Code03_Arrangement1.Solution.outDeg[i] - Code03_Arrangement1.Solution.inDeg[i])))
                if ((((v < jcast('int', (-1))) or (v > 1)) or ((v == 1) and (start != jcast('int', (-1))))) or ((v == jcast('int', (-1))) and (end != jcast('int', (-1))))):
                    return jcast('int', jcast('int', (-1)))
                if (v == 1):
                    start = jcast('int', i)
                if (v == jcast('int', (-1))):
                    end = jcast('int', i)
                i = jcast('int', (i + 1))
            if ((start == jcast('int', (-1))) ^ (end == jcast('int', (-1)))):
                return jcast('int', jcast('int', (-1)))
            if (start != jcast('int', (-1))):
                return jcast('int', start)
            i = jcast('int', 1)
            while (i <= Code03_Arrangement1.Solution.n):
                if (Code03_Arrangement1.Solution.outDeg[i] > 0):
                    return jcast('int', i)
                i = jcast('int', (i + 1))
            return jcast('int', jcast('int', (-1)))

        @staticmethod
        def euler(u):
            u = jcast('int', u)
            e = jcast('int', Code03_Arrangement1.Solution.cur[u])
            while (e > 0):
                jset(Code03_Arrangement1.Solution.cur, u, Code03_Arrangement1.Solution.nxt[e])
                Code03_Arrangement1.Solution.euler(Code03_Arrangement1.Solution.to[e])
                e = jcast('int', Code03_Arrangement1.Solution.cur[u])
            jset(Code03_Arrangement1.Solution.path, ((_java_obj_13 := Code03_Arrangement1.Solution), (_java_key_14 := 'cntp'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], u)

        def validArrangement(self, pairs):
            jset(Code03_Arrangement1.Solution, 'm', jget(pairs, 'length'))
            jset(Code03_Arrangement1.Solution, 'pair', pairs)
            Code03_Arrangement1.Solution.prepare()
            Code03_Arrangement1.Solution.connect()
            start = jcast('int', Code03_Arrangement1.Solution.directedStart())
            if (start == jcast('int', (-1))):
                return None
            Code03_Arrangement1.Solution.euler(start)
            if (Code03_Arrangement1.Solution.cntp != jcast('int', jadd(Code03_Arrangement1.Solution.m, 1))):
                return None
            ans = jarray('int', [Code03_Arrangement1.Solution.m, 2])
            i = jcast('int', 0)
            j = jcast('int', Code03_Arrangement1.Solution.cntp)
            while (i < Code03_Arrangement1.Solution.m):
                jset(ans[i], 0, Code03_Arrangement1.Solution.sortv[Code03_Arrangement1.Solution.path[j]])
                jset(ans[i], 1, Code03_Arrangement1.Solution.sortv[Code03_Arrangement1.Solution.path[jcast('int', (j - 1))]])
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
            return ans

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Arrangement1.Solution.MAXN = jcast('int', 200001)
Code03_Arrangement1.Solution.n = jcast('int', 0)
Code03_Arrangement1.Solution.m = jcast('int', 0)
Code03_Arrangement1.Solution.pair = None
Code03_Arrangement1.Solution.sortv = jarray('int', [Code03_Arrangement1.Solution.MAXN])
Code03_Arrangement1.Solution.head = jarray('int', [Code03_Arrangement1.Solution.MAXN])
Code03_Arrangement1.Solution.nxt = jarray('int', [Code03_Arrangement1.Solution.MAXN])
Code03_Arrangement1.Solution.to = jarray('int', [Code03_Arrangement1.Solution.MAXN])
Code03_Arrangement1.Solution.cntg = jcast('int', 0)
Code03_Arrangement1.Solution.cur = jarray('int', [Code03_Arrangement1.Solution.MAXN])
Code03_Arrangement1.Solution.outDeg = jarray('int', [Code03_Arrangement1.Solution.MAXN])
Code03_Arrangement1.Solution.inDeg = jarray('int', [Code03_Arrangement1.Solution.MAXN])
Code03_Arrangement1.Solution.path = jarray('int', [Code03_Arrangement1.Solution.MAXN])
Code03_Arrangement1.Solution.cntp = jcast('int', 0)
