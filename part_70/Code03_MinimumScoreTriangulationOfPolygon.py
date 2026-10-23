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

# 多边形三角剖分的最低得分
# 你有一个凸的 n 边形，其每个顶点都有一个整数值
# 给定一个整数数组values，其中values[i]是第i个顶点的值(顺时针顺序)
# 假设将多边形 剖分 为 n - 2 个三角形
# 对于每个三角形，该三角形的值是顶点标记的乘积
# 三角剖分的分数是进行三角剖分后所有 n - 2 个三角形的值之和
# 返回 多边形进行三角剖分后可以得到的最低分
# 测试链接 : https://leetcode.cn/problems/minimum-score-triangulation-of-polygon/
class Code03_MinimumScoreTriangulationOfPolygon:
    __java_fields__ = {}
    # 记忆化搜索
    @staticmethod
    def minScoreTriangulation1(arr):
        n = jcast('int', jget(arr, 'length'))
        dp = jarray('int', [n, n])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < n):
                jset(dp[i], j, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code03_MinimumScoreTriangulationOfPolygon.f(arr, 0, jcast('int', (n - 1)), dp))

    @staticmethod
    def f(arr, l, r, dp):
        l = jcast('int', l)
        r = jcast('int', r)
        if (dp[l][r] != jcast('int', (-1))):
            return jcast('int', dp[l][r])
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        if ((l == r) or (l == jcast('int', (r - 1)))):
            ans = jcast('int', 0)
        else:
            # l....r >=3
            # 0..1..2..3..4...5
            m = jcast('int', jcast('int', jadd(l, 1)))
            while (m < r):
                # l m r
                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(jcast('int', jadd(Code03_MinimumScoreTriangulationOfPolygon.f(arr, l, m, dp), Code03_MinimumScoreTriangulationOfPolygon.f(arr, m, r, dp))), jcast('int', (jcast('int', (arr[l] * arr[m])) * arr[r]))))))
                m = jcast('int', (m + 1))
        jset(dp[l], r, ans)
        return jcast('int', ans)

    # 严格位置依赖的动态规划
    @staticmethod
    def minScoreTriangulation2(arr):
        n = jcast('int', jget(arr, 'length'))
        dp = jarray('int', [n, n])
        l = jcast('int', jcast('int', (n - 3)))
        while (l >= 0):
            r = jcast('int', jcast('int', jadd(l, 2)))
            while (r < n):
                jset(dp[l], r, jget(Integer, 'MAX_VALUE'))
                m = jcast('int', jcast('int', jadd(l, 1)))
                while (m < r):
                    jset(dp[l], r, jstatic('Math', 'min', dp[l][r], jcast('int', jadd(jcast('int', jadd(dp[l][m], dp[m][r])), jcast('int', (jcast('int', (arr[l] * arr[m])) * arr[r]))))))
                    m = jcast('int', (m + 1))
                r = jcast('int', (r + 1))
            l = jcast('int', (l - 1))
        return jcast('int', dp[0][jcast('int', (n - 1))])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


