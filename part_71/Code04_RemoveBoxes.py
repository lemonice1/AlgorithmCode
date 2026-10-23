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

# 移除盒子
# 给出一些不同颜色的盒子boxes，盒子的颜色由不同的正数表示
# 你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止
# 每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1）
# 这样一轮之后你将得到 k * k 个积分
# 返回你能获得的最大积分总和
# 测试链接 : https://leetcode.cn/problems/remove-boxes/
class Code04_RemoveBoxes:
    __java_fields__ = {}
    # 时间复杂度O(n^4)
    @staticmethod
    def removeBoxes(boxes):
        n = jcast('int', jget(boxes, 'length'))
        dp = jarray('int', [n, n, n])
        return jcast('int', Code04_RemoveBoxes.f(boxes, 0, jcast('int', (n - 1)), 0, dp))

    # boxes[l....r]范围上要去消除，前面跟着k个连续的和boxes[l]颜色一样的盒子
    # 这种情况下，返回最大得分
    @staticmethod
    def f(boxes, l, r, k, dp):
        l = jcast('int', l)
        r = jcast('int', r)
        k = jcast('int', k)
        if (l > r):
            return jcast('int', 0)
        # l <= r
        if (dp[l][r][k] > 0):
            return jcast('int', dp[l][r][k])
        s = jcast('int', l)
        while ((jcast('int', jadd(s, 1)) <= r) and (boxes[l] == boxes[jcast('int', jadd(s, 1))])):
            s = jcast('int', (s + 1))
        # boxes[l...s]都是一种颜色，boxes[s+1]就不是同一种颜色了
        # cnt是总前缀数量 : 之前的相同前缀(k个) + l...s这个颜色相同的部分(s-l+1个)
        cnt = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', jadd(k, s)) - l)), 1)))
        # 可能性1 : 前缀先消
        ans = jcast('int', jcast('int', jadd(jcast('int', (cnt * cnt)), Code04_RemoveBoxes.f(boxes, jcast('int', jadd(s, 1)), r, 0, dp))))
        # 可能性2 : 讨论前缀跟着哪个后，一起消掉
        m = jcast('int', jcast('int', jadd(s, 2)))
        while (m <= r):
            if ((boxes[l] == boxes[m]) and (boxes[jcast('int', (m - 1))] != boxes[m])):
                # boxes[l] == boxes[m]是必须条件
                # boxes[m - 1] != boxes[m]是剪枝条件，避免不必要的调用
                ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(Code04_RemoveBoxes.f(boxes, jcast('int', jadd(s, 1)), jcast('int', (m - 1)), 0, dp), Code04_RemoveBoxes.f(boxes, m, r, cnt, dp)))))
            m = jcast('int', (m + 1))
        jset(dp[l][r], k, ans)
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


