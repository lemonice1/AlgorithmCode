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

# 摆盘子的方法
# 一共有n个盘子k种菜，所有盘子排成一排，每个盘子只能放一种菜
# 要求最多连续两个盘子菜品一样，更长的重复出现是不允许的
# 返回摆盘的方法数，答案对 1000000007 取模
# 1 <= n <= 1000
# 1 <= k <= 1000
# 来自真实大厂笔试，对数器验证
class Code05_WaysOfArrangePlates:
    __java_fields__ = {'MOD': 'MOD'}
    MOD = 0
    # 正式方法的尝试思路
    @staticmethod
    def dp1(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        if (n == 1):
            return jcast('int', k)
        return jcast('int', jcast('int', jcast('long', jmod(jcast('long', (jcast('long', jadd(jcast('long', Code05_WaysOfArrangePlates.f1(jcast('int', (n - 1)), k)), Code05_WaysOfArrangePlates.f1(jcast('int', (n - 2)), k))) * k)), Code05_WaysOfArrangePlates.MOD))))

    @staticmethod
    def f1(i, k):
        i = jcast('int', i)
        k = jcast('int', k)
        if (i == 0):
            return jcast('int', 1)
        if (i == 1):
            return jcast('int', jcast('int', (k - 1)))
        p1 = jcast('long', Code05_WaysOfArrangePlates.f1(jcast('int', (i - 1)), k))
        p2 = jcast('long', Code05_WaysOfArrangePlates.f1(jcast('int', (i - 2)), k))
        return jcast('int', jcast('int', jcast('long', jmod(jcast('long', (jcast('long', jadd(p1, p2)) * jcast('int', (k - 1)))), Code05_WaysOfArrangePlates.MOD))))

    # 正式方法的普通动态规划版本
    # 时间复杂度O(n)
    @staticmethod
    def dp2(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        if (n == 1):
            return jcast('int', k)
        dp = jarray('int', [n])
        dp[0] = jcast('int', 1)
        dp[1] = jcast('int', jcast('int', (k - 1)))
        i = jcast('int', 2)
        while (i < n):
            p1 = jcast('long', dp[jcast('int', (i - 1))])
            p2 = jcast('long', dp[jcast('int', (i - 2))])
            dp[i] = jcast('int', jcast('int', jcast('long', jmod(jcast('long', (jcast('long', jadd(p1, p2)) * jcast('int', (k - 1)))), Code05_WaysOfArrangePlates.MOD))))
            i = jcast('int', (i + 1))
        return jcast('int', jcast('int', jcast('long', jmod(jcast('long', (jcast('long', jadd(jcast('long', dp[jcast('int', (n - 1))]), dp[jcast('int', (n - 2))])) * k)), Code05_WaysOfArrangePlates.MOD))))

    # 最优解的版本，动态规划 + 矩阵快速幂优化
    # 时间复杂度O(log n)
    # 不会的同学看讲解098
    @staticmethod
    def dp3(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        if (n == 1):
            return jcast('int', k)
        s = jcast('int', jcast('int', (k - 1)))
        start = jarray('int', [None, None], [[1, s]])
        base = jarray('int', [None, None], [[0, s], [1, s]])
        ans = Code05_WaysOfArrangePlates.multiply(start, Code05_WaysOfArrangePlates.power(base, jcast('int', (n - 2))))
        return jcast('int', jcast('int', jcast('long', jmod(jcast('long', (jcast('long', jadd(jcast('long', ans[0][0]), ans[0][1])) * k)), Code05_WaysOfArrangePlates.MOD))))

    @staticmethod
    def multiply(a, b):
        n = jcast('int', jget(a, 'length'))
        m = jcast('int', jget(b[0], 'length'))
        k = jcast('int', jget(a[0], 'length'))
        ans = jarray('int', [n, m])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < m):
                c = jcast('int', 0)
                while (c < k):
                    jset(ans[i], j, jcast('int', jcast('long', jmod(jcast('long', jadd(jcast('long', ans[i][j]), jcast('long', (jcast('long', a[i][c]) * b[c][j])))), Code05_WaysOfArrangePlates.MOD))))
                    c = jcast('int', (c + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return ans

    @staticmethod
    def power(m, p):
        p = jcast('int', p)
        n = jcast('int', jget(m, 'length'))
        ans = jarray('int', [n, n])
        i = jcast('int', 0)
        while (i < n):
            jset(ans[i], i, 1)
            i = jcast('int', (i + 1))
        while (p != 0):
            if (jcast('int', (p & 1)) != 0):
                ans = Code05_WaysOfArrangePlates.multiply(ans, m)
            m = Code05_WaysOfArrangePlates.multiply(m, m)
            p = jcast('int', jcast('int', (p >> (1 & 31))))
        return ans

    # 暴力方法
    # 为了验证
    @staticmethod
    def right(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        path = jarray('int', [n])
        return jcast('int', Code05_WaysOfArrangePlates.dfs(path, 0, k))

    # 暴力方法
    # 为了验证
    @staticmethod
    def dfs(path, i, k):
        i = jcast('int', i)
        k = jcast('int', k)
        if (i == jget(path, 'length')):
            len = jcast('int', 1)
            j = jcast('int', 1)
            while (j < jget(path, 'length')):
                if (path[jcast('int', (j - 1))] == path[j]):
                    len = jcast('int', (len + 1))
                else:
                    len = jcast('int', 1)
                if (len > 2):
                    return jcast('int', 0)
                j = jcast('int', (j + 1))
            return jcast('int', (0 if (len > 2) else 1))
        else:
            ans = jcast('int', 0)
            j = jcast('int', 0)
            while (j < k):
                path[i] = jcast('int', j)
                ans = jcast('int', jcast('int', jadd(ans, Code05_WaysOfArrangePlates.dfs(path, jcast('int', jadd(i, 1)), k))))
                j = jcast('int', (j + 1))
            return jcast('int', ans)

    # 对数器
    # 为了验证
    @staticmethod
    def main(args):
        jprint('功能测试开始', newline=True)
        n = jcast('int', 1)
        while (n <= 8):
            k = jcast('int', 1)
            while (k <= 8):
                ans1 = jcast('int', Code05_WaysOfArrangePlates.dp1(n, k))
                ans2 = jcast('int', Code05_WaysOfArrangePlates.dp2(n, k))
                ans3 = jcast('int', Code05_WaysOfArrangePlates.dp3(n, k))
                ans4 = jcast('int', Code05_WaysOfArrangePlates.right(n, k))
                if (((ans1 != ans2) or (ans1 != ans3)) or (ans1 != ans4)):
                    jprint('出错了!', newline=True)
                k = jcast('int', (k + 1))
            n = jcast('int', (n + 1))
        jprint('功能测试结束', newline=True)
        jprint(newline=True)
        jprint('性能测试开始', newline=True)
        n = jcast('int', 505060123)
        k = jcast('int', 303060123)
        jprint(jadd(jadd(jadd('数据量 : n = ', n), ', k = '), k), newline=True)
        start = 0
        end = 0
        start = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd('dp2方法结果(已经取模) : ', Code05_WaysOfArrangePlates.dp2(n, k)), newline=True)
        end = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd('dp2方法用时(毫秒) : ', jcast('long', (end - start))), newline=True)
        start = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd('dp3方法结果(已经取模) : ', Code05_WaysOfArrangePlates.dp3(n, k)), newline=True)
        end = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd('dp3方法用时(毫秒) : ', jcast('long', (end - start))), newline=True)
        jprint('性能测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_WaysOfArrangePlates.MOD = jcast('int', 1000000007)

if __name__ == '__main__':
    Code05_WaysOfArrangePlates.main([])
