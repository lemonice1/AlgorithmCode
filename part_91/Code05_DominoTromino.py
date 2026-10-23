# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 多米诺和托米诺平铺
# 有两种形状的瓷砖，一种是2*1的多米诺形，另一种是形如"L"的托米诺形
# 两种形状都可以旋转，给定整数n，返回可以平铺2*n的面板的方法数量
# 返回对1000000007取模的值
# 测试链接 : https://leetcode.cn/problems/domino-and-tromino-tiling/
class Code05_DominoTromino:
    __java_fields__ = {'MOD': 'MOD'}
    # f(1) = 1
    # f(2) = 2
    # f(3) = 5
    # f(4) = 11
    # f(n) = 2 * f(n-1) + f(n-3)
    # 打表或者公式化简都可以发现规律，这里推荐打表找规律
    @staticmethod
    def main(args):
        i = jcast('int', 1)
        while (i <= 9):
            jprint(jadd(jadd(jadd('铺满 2 * ', i), ' 的区域方法数 : '), Code05_DominoTromino.f(i, 0)), newline=True)
            i = jcast('int', (i + 1))

    # 暴力方法
    # 为了找规律
    # 如果h==0，返回2*n的区域铺满的方法数
    # 如果h==1，返回1 + 2*n的区域铺满的方法数
    @staticmethod
    def f(n, h):
        n = jcast('int', n)
        h = jcast('int', h)
        if (n == 0):
            return jcast('int', (1 if (h == 0) else 0))
        if (n == 1):
            return jcast('int', 1)
        if (h == 1):
            return jcast('int', jcast('int', jadd(Code05_DominoTromino.f(jcast('int', (n - 1)), 0), Code05_DominoTromino.f(jcast('int', (n - 1)), 1))))
        else:
            return jcast('int', jcast('int', jadd(jcast('int', jadd(Code05_DominoTromino.f(jcast('int', (n - 1)), 0), Code05_DominoTromino.f(jcast('int', (n - 2)), 0))), jcast('int', (2 * Code05_DominoTromino.f(jcast('int', (n - 2)), 1))))))

    # 正式方法
    # 矩阵快速幂
    # 时间复杂度O(logn)
    @staticmethod
    def numTilings(n):
        n = jcast('int', n)
        return jcast('int', Code05_DominoTromino.f2(jcast('int', (n - 1))))

    MOD = 0
    @staticmethod
    def f2(n):
        n = jcast('int', n)
        if (n == 0):
            return jcast('int', 1)
        if (n == 1):
            return jcast('int', 2)
        if (n == 2):
            return jcast('int', 5)
        start = jarray('int', [None, None], [[5, 2, 1]])
        base = jarray('int', [None, None], [[2, 1, 0], [0, 0, 1], [1, 0, 0]])
        ans = Code05_DominoTromino.multiply(start, Code05_DominoTromino.power(base, jcast('int', (n - 2))))
        return jcast('int', ans[0][0])

    # 矩阵相乘 + 乘法取模
    # a的列数一定要等于b的行数
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
                    jset(ans[i], j, jcast('int', jcast('long', jmod(jcast('long', jadd(jcast('long', (jcast('long', a[i][c]) * b[c][j])), ans[i][j])), Code05_DominoTromino.MOD))))
                    c = jcast('int', (c + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return ans

    # 矩阵快速幂
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
                ans = Code05_DominoTromino.multiply(ans, m)
            m = Code05_DominoTromino.multiply(m, m)
            p = jcast('int', jcast('int', (p >> (1 & 31))))
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_DominoTromino.MOD = jcast('int', 1000000007)

if __name__ == '__main__':
    Code05_DominoTromino.main([])
