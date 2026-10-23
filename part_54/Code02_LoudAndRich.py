# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 喧闹和富有
# 从 0 到 n - 1 编号，其中每个人都有不同数目的钱，以及不同程度的安静值
# 给你一个数组richer，其中richer[i] = [ai, bi] 表示
# person ai 比 person bi 更有钱
# 还有一个整数数组 quiet ，其中 quiet[i] 是 person i 的安静值
# richer 中所给出的数据 逻辑自洽
# 也就是说，在 person x 比 person y 更有钱的同时，不会出现
# person y 比 person x 更有钱的情况
# 现在，返回一个整数数组 answer 作为答案，其中 answer[x] = y 的前提是,
# 在所有拥有的钱肯定不少于 person x 的人中，
# person y 是最安静的人（也就是安静值 quiet[y] 最小的人）。
# 测试链接 : https://leetcode.cn/problems/loud-and-rich/
class Code02_LoudAndRich:
    __java_fields__ = {}
    @staticmethod
    def loudAndRich(richer, quiet):
        n = jcast('int', jget(quiet, 'length'))
        graph = jnew('ArrayList')
        i = jcast('int', 0)
        while (i < n):
            jcall(graph, 'add', jnew('ArrayList'))
            i = jcast('int', (i + 1))
        indegree = jarray('int', [n])
        for r in richer:
            jcall(jcall(graph, 'get', r[0]), 'add', r[1])
            ((_java_obj_1 := indegree), (_java_key_2 := r[1]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
        queue = jarray('int', [n])
        l = jcast('int', 0)
        r = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            if (indegree[i] == 0):
                jset(queue, ((_java_old_4 := r), (r := jcast('int', (r + (1)))), _java_old_4)[2], i)
            i = jcast('int', (i + 1))
        ans = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            ans[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        while (l < r):
            cur = jcast('int', queue[((_java_old_5 := l), (l := jcast('int', (l + (1)))), _java_old_5)[2]])
            for next in jcall(graph, 'get', cur):
                if (quiet[ans[cur]] < quiet[ans[next]]):
                    ans[next] = jcast('int', ans[cur])
                if (((_java_obj_6 := indegree), (_java_key_7 := next), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (-1)))))[3] == 0):
                    jset(queue, ((_java_old_9 := r), (r := jcast('int', (r + (1)))), _java_old_9)[2], next)
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


