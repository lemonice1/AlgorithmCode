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

# 相邻不同色的染色方法数(轮廓线dp)
# 给定两个参数n和m，表示n行m列的空白区域，一开始所有格子都没有颜色
# 给定参数k，表示有k种颜色，颜色编号0~k-1
# 你需要给每个格子染色，但是相邻的格子颜色不能相同
# 相邻包括上、下、左、右四个方向
# 并且给定了第0行和第n-1行的颜色状况，输入保证一定有效
# 那么你只能在1~n-2行上染色，返回染色的方法数，答案对376544743取模
# 2 <= k <= 4
# k = 2时，1 <= n <= 10^7，1 <= m <= 10^5
# 3 <= k <= 4时，1 <= n <= 100，1 <= m <= 8
# 测试链接 : https://www.luogu.com.cn/problem/P2435
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 空间会不达标，在线测试无法全部通过，但逻辑正确
# 我运行了所有可能的情况，结果是正确的
class Code03_AdjacentDifferent1:
    __java_fields__ = {'LIMIT1': 'LIMIT1', 'LIMIT2': 'LIMIT2', 'LIMIT3': 'LIMIT3', 'MOD': 'MOD', 'start': 'start', 'end': 'end', 'dp': 'dp', 'startStatus': 'startStatus', 'endStatus': 'endStatus', 'n': 'n', 'm': 'm', 'k': 'k', 'maxs': 'maxs'}
    LIMIT1 = 0
    LIMIT2 = 0
    LIMIT3 = 0
    MOD = 0
    start = None
    end = None
    dp = None
    startStatus = 0
    endStatus = 0
    n = 0
    m = 0
    k = 0
    maxs = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_AdjacentDifferent1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code03_AdjacentDifferent1.m = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code03_AdjacentDifferent1.k = jcast('int', jcast('int', jget(in_, 'nval')))
        Code03_AdjacentDifferent1.maxs = jcast('int', jcast('int', (1 << (jcast('int', (Code03_AdjacentDifferent1.m << (1 & 31))) & 31))))
        i = jcast('int', 0)
        while (i < Code03_AdjacentDifferent1.m):
            jcall(in_, 'nextToken')
            Code03_AdjacentDifferent1.start[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < Code03_AdjacentDifferent1.m):
            jcall(in_, 'nextToken')
            Code03_AdjacentDifferent1.end[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        if (Code03_AdjacentDifferent1.k == 2):
            jcall(out, 'println', Code03_AdjacentDifferent1.special())
        else:
            jcall(out, 'println', Code03_AdjacentDifferent1.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def special():
        if (jcast('int', (Code03_AdjacentDifferent1.n & 1)) == 0):
            i = jcast('int', 0)
            while (i < Code03_AdjacentDifferent1.m):
                if (Code03_AdjacentDifferent1.start[i] == Code03_AdjacentDifferent1.end[i]):
                    return jcast('int', 0)
                i = jcast('int', (i + 1))
        else:
            i = jcast('int', 0)
            while (i < Code03_AdjacentDifferent1.m):
                if (Code03_AdjacentDifferent1.start[i] != Code03_AdjacentDifferent1.end[i]):
                    return jcast('int', 0)
                i = jcast('int', (i + 1))
        return jcast('int', 1)

    @staticmethod
    def compute():
        Code03_AdjacentDifferent1.startStatus = jcast('int', jset(Code03_AdjacentDifferent1, 'endStatus', 0))
        j = jcast('int', 0)
        while (j < Code03_AdjacentDifferent1.m):
            Code03_AdjacentDifferent1.startStatus = jcast('int', Code03_AdjacentDifferent1.set(Code03_AdjacentDifferent1.startStatus, j, Code03_AdjacentDifferent1.start[j]))
            Code03_AdjacentDifferent1.endStatus = jcast('int', Code03_AdjacentDifferent1.set(Code03_AdjacentDifferent1.endStatus, j, Code03_AdjacentDifferent1.end[j]))
            j = jcast('int', (j + 1))
        i = jcast('int', 0)
        while (i < Code03_AdjacentDifferent1.n):
            j = jcast('int', 0)
            while (j < Code03_AdjacentDifferent1.m):
                s = jcast('int', 0)
                while (s < Code03_AdjacentDifferent1.maxs):
                    jset(Code03_AdjacentDifferent1.dp[i][j], s, jcast('int', (-1)))
                    s = jcast('int', (s + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code03_AdjacentDifferent1.f(1, 0, Code03_AdjacentDifferent1.startStatus))

    # 当前来到i行j列
    # i-1行中，[j..m-1]列的颜色状况，用s[j..m-1]号格子表示
    # i行中，[0..j-1]列的颜色状况，用s[0..j-1]号格子表示
    # s表示轮廓线的状况
    # 返回有几种染色方法
    @staticmethod
    def f(i, j, s):
        i = jcast('int', i)
        j = jcast('int', j)
        s = jcast('int', s)
        if (i == jcast('int', (Code03_AdjacentDifferent1.n - 1))):
            return jcast('int', (1 if Code03_AdjacentDifferent1.different(s, Code03_AdjacentDifferent1.endStatus) else 0))
        if (j == Code03_AdjacentDifferent1.m):
            return jcast('int', Code03_AdjacentDifferent1.f(jcast('int', jadd(i, 1)), 0, s))
        if (Code03_AdjacentDifferent1.dp[i][j][s] != jcast('int', (-1))):
            return jcast('int', Code03_AdjacentDifferent1.dp[i][j][s])
        ans = jcast('int', 0)
        color = jcast('int', 0)
        while (color < Code03_AdjacentDifferent1.k):
            if (((j == 0) or (Code03_AdjacentDifferent1.get(s, jcast('int', (j - 1))) != color)) and (Code03_AdjacentDifferent1.get(s, j) != color)):
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code03_AdjacentDifferent1.f(i, jcast('int', jadd(j, 1)), Code03_AdjacentDifferent1.set(s, j, color)))), Code03_AdjacentDifferent1.MOD)))
            color = jcast('int', (color + 1))
        jset(Code03_AdjacentDifferent1.dp[i][j], s, ans)
        return jcast('int', ans)

    # 颜色状况a和颜色状况b，是否每一格都不同
    @staticmethod
    def different(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        j = jcast('int', 0)
        while (j < Code03_AdjacentDifferent1.m):
            if (Code03_AdjacentDifferent1.get(a, j) == Code03_AdjacentDifferent1.get(b, j)):
                return jcast('boolean', False)
            j = jcast('int', (j + 1))
        return jcast('boolean', True)

    # 在颜色状况s里，取出j号格的颜色
    @staticmethod
    def get(s, j):
        s = jcast('int', s)
        j = jcast('int', j)
        return jcast('int', jcast('int', (jcast('int', (s >> (jcast('int', (j << (1 & 31))) & 31))) & 3)))

    # 颜色状况s中，把j号格的颜色设置成v，然后把新的s返回
    @staticmethod
    def set(s, j, v):
        s = jcast('int', s)
        j = jcast('int', j)
        v = jcast('int', v)
        return jcast('int', jcast('int', (jcast('int', (s & jcast('int', (~jcast('int', (3 << (jcast('int', (j << (1 & 31))) & 31))))))) | jcast('int', (v << (jcast('int', (j << (1 & 31))) & 31))))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_AdjacentDifferent1.LIMIT1 = jcast('int', 100001)
Code03_AdjacentDifferent1.LIMIT2 = jcast('int', 101)
Code03_AdjacentDifferent1.LIMIT3 = jcast('int', 8)
Code03_AdjacentDifferent1.MOD = jcast('int', 376544743)
Code03_AdjacentDifferent1.start = jarray('int', [Code03_AdjacentDifferent1.LIMIT1])
Code03_AdjacentDifferent1.end = jarray('int', [Code03_AdjacentDifferent1.LIMIT1])
Code03_AdjacentDifferent1.dp = jarray('int', [Code03_AdjacentDifferent1.LIMIT2, Code03_AdjacentDifferent1.LIMIT3, jcast('int', (1 << (jcast('int', (Code03_AdjacentDifferent1.LIMIT3 << (1 & 31))) & 31)))])
Code03_AdjacentDifferent1.startStatus = jcast('int', 0)
Code03_AdjacentDifferent1.endStatus = jcast('int', 0)
Code03_AdjacentDifferent1.n = jcast('int', 0)
Code03_AdjacentDifferent1.m = jcast('int', 0)
Code03_AdjacentDifferent1.k = jcast('int', 0)
Code03_AdjacentDifferent1.maxs = jcast('int', 0)

if __name__ == '__main__':
    Code03_AdjacentDifferent1.main([])
