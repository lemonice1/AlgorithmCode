# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 检查边长度限制的路径是否存在
# 给你一个 n 个点组成的无向图边集 edgeList
# 其中 edgeList[i] = [ui, vi, disi] 表示点 ui 和点 vi 之间有一条长度为 disi 的边
# 请注意，两个点之间可能有 超过一条边 。
# 给你一个查询数组queries ，其中 queries[j] = [pj, qj, limitj]
# 你的任务是对于每个查询 queries[j] ，判断是否存在从 pj 到 qj 的路径
# 且这条路径上的每一条边都 严格小于 limitj 。
# 请你返回一个 布尔数组 answer ，其中 answer.length == queries.length
# 当 queries[j] 的查询结果为 true 时， answer 第 j 个值为 true ，否则为 false
# 测试链接 : https://leetcode.cn/problems/checking-existence-of-edge-length-limited-paths/
class Code04_CheckingExistenceOfEdgeLengthLimit:
    __java_fields__ = {'MAXN': 'MAXN', 'questions': 'questions', 'father': 'father'}
    @staticmethod
    def distanceLimitedPathsExist(n, edges, queries):
        n = jcast('int', n)
        jstatic('Arrays', 'sort', edges, (lambda a, b: (a[2] - b[2])))
        m = jcast('int', jget(edges, 'length'))
        k = jcast('int', jget(queries, 'length'))
        i = jcast('int', 0)
        while (i < k):
            jset(Code04_CheckingExistenceOfEdgeLengthLimit.questions[i], 0, queries[i][0])
            jset(Code04_CheckingExistenceOfEdgeLengthLimit.questions[i], 1, queries[i][1])
            jset(Code04_CheckingExistenceOfEdgeLengthLimit.questions[i], 2, queries[i][2])
            jset(Code04_CheckingExistenceOfEdgeLengthLimit.questions[i], 3, i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_CheckingExistenceOfEdgeLengthLimit.questions, 0, k, (lambda a, b: (a[2] - b[2])))
        Code04_CheckingExistenceOfEdgeLengthLimit.build(n)
        ans = jarray('boolean', [k])
        i = jcast('int', 0)
        j = jcast('int', 0)
        while (i < k):
            # i : 问题编号
            # j : 边的编号
            while ((j < m) and (edges[j][2] < Code04_CheckingExistenceOfEdgeLengthLimit.questions[i][2])):
                Code04_CheckingExistenceOfEdgeLengthLimit.union(edges[j][0], edges[j][1])
                j = jcast('int', (j + 1))
            jset(ans, Code04_CheckingExistenceOfEdgeLengthLimit.questions[i][3], Code04_CheckingExistenceOfEdgeLengthLimit.isSameSet(Code04_CheckingExistenceOfEdgeLengthLimit.questions[i][0], Code04_CheckingExistenceOfEdgeLengthLimit.questions[i][1]))
            i = jcast('int', (i + 1))
        return ans

    MAXN = 0
    questions = None
    father = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        i = jcast('int', 0)
        while (i < n):
            Code04_CheckingExistenceOfEdgeLengthLimit.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code04_CheckingExistenceOfEdgeLengthLimit.father[i]):
            jset(Code04_CheckingExistenceOfEdgeLengthLimit.father, i, Code04_CheckingExistenceOfEdgeLengthLimit.find(Code04_CheckingExistenceOfEdgeLengthLimit.father[i]))
        return jcast('int', Code04_CheckingExistenceOfEdgeLengthLimit.father[i])

    @staticmethod
    def isSameSet(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('boolean', (Code04_CheckingExistenceOfEdgeLengthLimit.find(x) == Code04_CheckingExistenceOfEdgeLengthLimit.find(y)))

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        jset(Code04_CheckingExistenceOfEdgeLengthLimit.father, Code04_CheckingExistenceOfEdgeLengthLimit.find(x), Code04_CheckingExistenceOfEdgeLengthLimit.find(y))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_CheckingExistenceOfEdgeLengthLimit.MAXN = jcast('int', 100001)
Code04_CheckingExistenceOfEdgeLengthLimit.questions = jarray('int', [Code04_CheckingExistenceOfEdgeLengthLimit.MAXN, 4])
Code04_CheckingExistenceOfEdgeLengthLimit.father = jarray('int', [Code04_CheckingExistenceOfEdgeLengthLimit.MAXN])
