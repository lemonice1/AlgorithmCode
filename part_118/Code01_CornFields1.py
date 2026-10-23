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

# 种草的方法数(普通状压dp)
# 给定一个n*m的二维网格grid
# 网格里只有0、1两种值，0表示该田地不能种草，1表示该田地可以种草
# 种草的时候，任何两个种了草的田地不能相邻，相邻包括上、下、左、右四个方向
# 你可以随意决定种多少草，只要不破坏上面的规则即可
# 返回种草的方法数，答案对100000000取模
# 1 <= n, m <= 12
# 测试链接 : https://www.luogu.com.cn/problem/P1879
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 普通状压 DP 的状态规模较大，适合作为基础解法分析
# 有些测试样本会超时，这是dfs过程很费时导致的
class Code01_CornFields1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MOD': 'MOD', 'grid': 'grid', 'dp': 'dp', 'n': 'n', 'm': 'm', 'maxs': 'maxs'}
    MAXN = 0
    MAXM = 0
    MOD = 0
    grid = None
    dp = None
    n = 0
    m = 0
    maxs = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_CornFields1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code01_CornFields1.m = jcast('int', jcast('int', jget(in_, 'nval')))
        Code01_CornFields1.maxs = jcast('int', jcast('int', (1 << (Code01_CornFields1.m & 31))))
        i = jcast('int', 0)
        while (i < Code01_CornFields1.n):
            j = jcast('int', 0)
            while (j < Code01_CornFields1.m):
                jcall(in_, 'nextToken')
                jset(Code01_CornFields1.grid[i], j, jcast('int', jget(in_, 'nval')))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code01_CornFields1.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 时间复杂度O(n * 2的m次方 * 2的m次方)
    @staticmethod
    def compute():
        i = jcast('int', 0)
        while (i < Code01_CornFields1.n):
            s = jcast('int', 0)
            while (s < Code01_CornFields1.maxs):
                jset(Code01_CornFields1.dp[i], s, jcast('int', (-1)))
                s = jcast('int', (s + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code01_CornFields1.f(0, 0))

    @staticmethod
    def f(i, s):
        i = jcast('int', i)
        s = jcast('int', s)
        if (i == Code01_CornFields1.n):
            return jcast('int', 1)
        if (Code01_CornFields1.dp[i][s] != jcast('int', (-1))):
            return jcast('int', Code01_CornFields1.dp[i][s])
        ans = jcast('int', Code01_CornFields1.dfs(i, 0, s, 0))
        jset(Code01_CornFields1.dp[i], s, ans)
        return jcast('int', ans)

    # 当前来到i行j列
    # i-1行每列种草的状况s
    # i行每列种草的状况ss
    # 返回后续有几种方法
    @staticmethod
    def dfs(i, j, s, ss):
        i = jcast('int', i)
        j = jcast('int', j)
        s = jcast('int', s)
        ss = jcast('int', ss)
        if (j == Code01_CornFields1.m):
            return jcast('int', Code01_CornFields1.f(jcast('int', jadd(i, 1)), ss))
        ans = jcast('int', Code01_CornFields1.dfs(i, jcast('int', jadd(j, 1)), s, ss))
        if (((Code01_CornFields1.grid[i][j] == 1) and ((j == 0) or (Code01_CornFields1.get(ss, jcast('int', (j - 1))) == 0))) and (Code01_CornFields1.get(s, j) == 0)):
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code01_CornFields1.dfs(i, jcast('int', jadd(j, 1)), s, Code01_CornFields1.set(ss, j, 1)))), Code01_CornFields1.MOD)))
        return jcast('int', ans)

    # 得到状态s中j位的状态
    @staticmethod
    def get(s, j):
        s = jcast('int', s)
        j = jcast('int', j)
        return jcast('int', jcast('int', (jcast('int', (s >> (j & 31))) & 1)))

    # 状态s中j位的状态设置成v，然后把新的值返回
    @staticmethod
    def set(s, j, v):
        s = jcast('int', s)
        j = jcast('int', j)
        v = jcast('int', v)
        return jcast('int', (jcast('int', (s & jcast('int', (~jcast('int', (1 << (j & 31))))))) if (v == 0) else jcast('int', (s | jcast('int', (1 << (j & 31)))))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_CornFields1.MAXN = jcast('int', 12)
Code01_CornFields1.MAXM = jcast('int', 12)
Code01_CornFields1.MOD = jcast('int', 100000000)
Code01_CornFields1.grid = jarray('int', [Code01_CornFields1.MAXN, Code01_CornFields1.MAXM])
Code01_CornFields1.dp = jarray('int', [Code01_CornFields1.MAXN, jcast('int', (1 << (Code01_CornFields1.MAXM & 31)))])
Code01_CornFields1.n = jcast('int', 0)
Code01_CornFields1.m = jcast('int', 0)
Code01_CornFields1.maxs = jcast('int', 0)

if __name__ == '__main__':
    Code01_CornFields1.main([])
