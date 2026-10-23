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

# 有效涂色问题
# 给定n、m两个参数
# 一共有n个格子，每个格子可以涂上一种颜色，颜色在m种里选
# 当涂满n个格子，并且m种颜色都使用了，叫一种有效方法
# 求一共有多少种有效的涂色方法
# 1 <= n, m <= 5000
# 结果比较大请 % 1000000007 之后返回
# 对数器验证
class Code04_FillCellsUseAllColorsWays:
    __java_fields__ = {'MAXN': 'MAXN', 'dp': 'dp', 'mod': 'mod'}
    # 暴力方法
    # 为了验证
    @staticmethod
    def ways1(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        return jcast('int', Code04_FillCellsUseAllColorsWays.f(jarray('int', [n]), jarray('boolean', [jcast('int', jadd(m, 1))]), 0, n, m))

    # 把所有填色的方法暴力枚举
    # 然后一个一个验证是否有效
    # 这是一个带路径的递归
    # 无法改成动态规划
    @staticmethod
    def f(path, set, i, n, m):
        i = jcast('int', i)
        n = jcast('int', n)
        m = jcast('int', m)
        if (i == n):
            jstatic('Arrays', 'fill', set, False)
            colors = jcast('int', 0)
            for c in path:
                if (not set[c]):
                    set[c] = jcast('boolean', True)
                    colors = jcast('int', (colors + 1))
            return jcast('int', (1 if (colors == m) else 0))
        else:
            ans = jcast('int', 0)
            j = jcast('int', 1)
            while (j <= m):
                path[i] = jcast('int', j)
                ans = jcast('int', jcast('int', jadd(ans, Code04_FillCellsUseAllColorsWays.f(path, set, jcast('int', jadd(i, 1)), n, m))))
                j = jcast('int', (j + 1))
            return jcast('int', ans)

    # 正式方法
    # 时间复杂度O(n * m)
    # 已经展示太多次从递归到动态规划了
    # 直接写动态规划吧
    # 也不做空间压缩了，因为千篇一律
    # 有兴趣的同学自己试试
    MAXN = 0
    dp = None
    mod = 0
    @staticmethod
    def ways2(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        # dp[i][j]:
        # 一共有m种颜色
        # 前i个格子涂满j种颜色的方法数
        i = jcast('int', 1)
        while (i <= n):
            jset(Code04_FillCellsUseAllColorsWays.dp[i], 1, m)
            i = jcast('int', (i + 1))
        i = jcast('int', 2)
        while (i <= n):
            j = jcast('int', 2)
            while (j <= m):
                jset(Code04_FillCellsUseAllColorsWays.dp[i], j, jcast('int', jcast('long', jmod(jcast('long', (jcast('long', Code04_FillCellsUseAllColorsWays.dp[jcast('int', (i - 1))][j]) * j)), Code04_FillCellsUseAllColorsWays.mod))))
                jset(Code04_FillCellsUseAllColorsWays.dp[i], j, jcast('int', jcast('long', jmod(jcast('long', jadd(jcast('long', (jcast('long', Code04_FillCellsUseAllColorsWays.dp[jcast('int', (i - 1))][jcast('int', (j - 1))]) * jcast('int', jadd(jcast('int', (m - j)), 1)))), Code04_FillCellsUseAllColorsWays.dp[i][j])), Code04_FillCellsUseAllColorsWays.mod))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code04_FillCellsUseAllColorsWays.dp[n][m])

    @staticmethod
    def main(args):
        # 测试的数据量比较小
        # 那是因为数据量大了，暴力方法过不了
        # 但是这个数据量足够说明正式方法是正确的
        N = jcast('int', 9)
        M = jcast('int', 9)
        jprint('功能测试开始', newline=True)
        n = jcast('int', 1)
        while (n <= N):
            m = jcast('int', 1)
            while (m <= M):
                ans1 = jcast('int', Code04_FillCellsUseAllColorsWays.ways1(n, m))
                ans2 = jcast('int', Code04_FillCellsUseAllColorsWays.ways2(n, m))
                if (ans1 != ans2):
                    jprint('出错了!', newline=True)
                m = jcast('int', (m + 1))
            n = jcast('int', (n + 1))
        jprint('功能测试结束', newline=True)
        jprint('性能测试开始', newline=True)
        n = jcast('int', 5000)
        m = jcast('int', 4877)
        jprint(jadd('n : ', n), newline=True)
        jprint(jadd('m : ', m), newline=True)
        start = jcast('long', jstatic('System', 'currentTimeMillis'))
        ans = jcast('int', Code04_FillCellsUseAllColorsWays.ways2(n, m))
        end = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd('取模之后的结果 : ', ans), newline=True)
        jprint(jadd(jadd('运行时间 : ', jcast('long', (end - start))), ' 毫秒'), newline=True)
        jprint('性能测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_FillCellsUseAllColorsWays.MAXN = jcast('int', 5001)
Code04_FillCellsUseAllColorsWays.dp = jarray('int', [Code04_FillCellsUseAllColorsWays.MAXN, Code04_FillCellsUseAllColorsWays.MAXN])
Code04_FillCellsUseAllColorsWays.mod = jcast('int', 1000000007)

if __name__ == '__main__':
    Code04_FillCellsUseAllColorsWays.main([])
