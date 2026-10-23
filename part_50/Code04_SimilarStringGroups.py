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

# 相似字符串组
# 如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等
# 那么称 X 和 Y 两个字符串相似
# 如果这两个字符串本身是相等的，那它们也是相似的
# 例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)；
# "rats" 和 "arts" 也是相似的，但是 "star" 不与 "tars"，"rats"，或 "arts" 相似
# 总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}
# 注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似
# 形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。
# 给你一个字符串列表 strs列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。
# 返回 strs 中有多少字符串组
# 测试链接 : https://leetcode.cn/problems/similar-string-groups/
class Code04_SimilarStringGroups:
    __java_fields__ = {'MAXN': 'MAXN', 'father': 'father', 'sets': 'sets'}
    MAXN = 0
    father = None
    sets = 0
    @staticmethod
    def build(n):
        n = jcast('int', n)
        i = jcast('int', 0)
        while (i < n):
            Code04_SimilarStringGroups.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        Code04_SimilarStringGroups.sets = jcast('int', n)

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code04_SimilarStringGroups.father[i]):
            jset(Code04_SimilarStringGroups.father, i, Code04_SimilarStringGroups.find(Code04_SimilarStringGroups.father[i]))
        return jcast('int', Code04_SimilarStringGroups.father[i])

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code04_SimilarStringGroups.find(x))
        fy = jcast('int', Code04_SimilarStringGroups.find(y))
        if (fx != fy):
            Code04_SimilarStringGroups.father[fx] = jcast('int', fy)
            Code04_SimilarStringGroups.sets = jcast('int', (Code04_SimilarStringGroups.sets - 1))

    @staticmethod
    def numSimilarGroups(strs):
        n = jcast('int', jget(strs, 'length'))
        m = jcast('int', jcall(strs[0], 'length'))
        Code04_SimilarStringGroups.build(n)
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', jcast('int', jadd(i, 1)))
            while (j < n):
                if (Code04_SimilarStringGroups.find(i) != Code04_SimilarStringGroups.find(j)):
                    diff = jcast('int', 0)
                    k = jcast('int', 0)
                    while ((k < m) and (diff < 3)):
                        if (jcall(strs[i], 'charAt', k) != jcall(strs[j], 'charAt', k)):
                            diff = jcast('int', (diff + 1))
                        k = jcast('int', (k + 1))
                    if ((diff == 0) or (diff == 2)):
                        Code04_SimilarStringGroups.union(i, j)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code04_SimilarStringGroups.sets)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_SimilarStringGroups.MAXN = jcast('int', 301)
Code04_SimilarStringGroups.father = jarray('int', [Code04_SimilarStringGroups.MAXN])
Code04_SimilarStringGroups.sets = jcast('int', 0)
