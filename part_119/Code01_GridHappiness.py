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

# 最大化网格幸福感
# 给定四个整数m、n、in、ex，表示m*n的网格，以及in个内向的人，ex个外向的人
# 你来决定网格中应当居住多少人，并为每个人分配一个网格单元，不必让所有人都生活在网格中
# 每个人的幸福感计算如下：
# 内向的人开始时有120幸福感，但每存在一个邻居，他都会失去30幸福感
# 外向的人开始时有40幸福感，但每存在一个邻居，他都会得到20幸福感
# 邻居只包含上、下、左、右四个方向
# 网格幸福感是每个人幸福感的总和，返回最大可能的网格幸福感
# 1 <= m、n <= 5
# 1 <= in、ex <= 6
# 测试链接 : https://leetcode.cn/problems/maximize-grid-happiness/
# 有兴趣的同学可以自己改一下空间压缩的版本
class Code01_GridHappiness:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 'MAXS': 'MAXS', 'n': 'n', 'm': 'm', 'maxs': 'maxs', 'dp': 'dp'}
    MAXN = 0
    MAXM = 0
    MAXP = 0
    MAXS = 0
    n = 0
    m = 0
    maxs = 0
    dp = None
    @staticmethod
    def getMaxGridHappiness(rows, cols, in_, ex):
        rows = jcast('int', rows)
        cols = jcast('int', cols)
        in_ = jcast('int', in_)
        ex = jcast('int', ex)
        Code01_GridHappiness.n = jcast('int', jstatic('Math', 'max', rows, cols))
        Code01_GridHappiness.m = jcast('int', jstatic('Math', 'min', rows, cols))
        Code01_GridHappiness.maxs = jcast('int', jcast('int', jstatic('Math', 'pow', 3, Code01_GridHappiness.m)))
        i = jcast('int', 0)
        while (i < Code01_GridHappiness.n):
            j = jcast('int', 0)
            while (j < Code01_GridHappiness.m):
                s = jcast('int', 0)
                while (s < Code01_GridHappiness.maxs):
                    a = jcast('int', 0)
                    while (a <= in_):
                        b = jcast('int', 0)
                        while (b <= ex):
                            jset(Code01_GridHappiness.dp[i][j][s][a], b, jcast('int', (-1)))
                            b = jcast('int', (b + 1))
                        a = jcast('int', (a + 1))
                    s = jcast('int', (s + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code01_GridHappiness.f(0, 0, 0, in_, ex, 1))

    # 当前来到i行j列的格子
    # s表示轮廓线的状态，可以得到左侧格子放了什么人，上侧格子放了什么人
    # 内向的人还有a个，外向的人还有b个
    # 返回最大的幸福感
    # 注意 : bit等于3的j次方，bit不是关键可变参数，因为bit的值被j的值决定
    @staticmethod
    def f(i, j, s, a, b, bit):
        i = jcast('int', i)
        j = jcast('int', j)
        s = jcast('int', s)
        a = jcast('int', a)
        b = jcast('int', b)
        bit = jcast('int', bit)
        if (i == Code01_GridHappiness.n):
            return jcast('int', 0)
        if (j == Code01_GridHappiness.m):
            return jcast('int', Code01_GridHappiness.f(jcast('int', jadd(i, 1)), 0, s, a, b, 1))
        if (Code01_GridHappiness.dp[i][j][s][a][b] != jcast('int', (-1))):
            return jcast('int', Code01_GridHappiness.dp[i][j][s][a][b])
        # 当前格子不安置人
        ans = jcast('int', Code01_GridHappiness.f(i, jcast('int', jadd(j, 1)), Code01_GridHappiness.set(s, bit, 0), a, b, jcast('int', (bit * 3))))
        # 上方邻居的状态
        up = jcast('int', Code01_GridHappiness.get(s, bit))
        # 左方邻居的状态
        left = jcast('int', (0 if (j == 0) else Code01_GridHappiness.get(s, jcast('int', jdiv(bit, 3)))))
        # 邻居人数
        neighbor = jcast('int', 0)
        # 如果放置人，之前得到的幸福感要如何变化
        pre = jcast('int', 0)
        if (up != 0):
            neighbor = jcast('int', (neighbor + 1))
            # 上邻居是内向的人，幸福感要减30；是外向的人，幸福感要加20
            pre = jcast('int', jcast('int', jadd(pre, (jcast('int', (-30)) if (up == 1) else 20))))
        if (left != 0):
            neighbor = jcast('int', (neighbor + 1))
            # 左邻居是内向的人，幸福感要减30；是外向的人，幸福感要加20
            pre = jcast('int', jcast('int', jadd(pre, (jcast('int', (-30)) if (left == 1) else 20))))
        if (a > 0):
            # 当前格子决定放内向的人
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(jcast('int', (jcast('int', jadd(pre, 120)) - jcast('int', (neighbor * 30)))), Code01_GridHappiness.f(i, jcast('int', jadd(j, 1)), Code01_GridHappiness.set(s, bit, 1), jcast('int', (a - 1)), b, jcast('int', (bit * 3)))))))
        if (b > 0):
            # 当前格子决定放外向的人
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(jcast('int', jadd(jcast('int', jadd(pre, 40)), jcast('int', (neighbor * 20)))), Code01_GridHappiness.f(i, jcast('int', jadd(j, 1)), Code01_GridHappiness.set(s, bit, 2), a, jcast('int', (b - 1)), jcast('int', (bit * 3)))))))
        jset(Code01_GridHappiness.dp[i][j][s][a], b, ans)
        return jcast('int', ans)

    # s表示当前状态，按照3进制来理解
    # 当前来到第j号格，3的j次方是bit
    # 返回s第j号格的值
    @staticmethod
    def get(s, bit):
        s = jcast('int', s)
        bit = jcast('int', bit)
        return jcast('int', jcast('int', jmod(jcast('int', jdiv(s, bit)), 3)))

    # s表示当前状态，按照3进制来理解
    # 当前来到第j号格，3的j次方是bit
    # 把s第j号格的值设置成v，返回新状态
    @staticmethod
    def set(s, bit, v):
        s = jcast('int', s)
        bit = jcast('int', bit)
        v = jcast('int', v)
        return jcast('int', jcast('int', jadd(jcast('int', (s - jcast('int', (Code01_GridHappiness.get(s, bit) * bit)))), jcast('int', (v * bit)))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_GridHappiness.MAXN = jcast('int', 5)
Code01_GridHappiness.MAXM = jcast('int', 5)
Code01_GridHappiness.MAXP = jcast('int', 7)
Code01_GridHappiness.MAXS = jcast('int', jcast('int', jstatic('Math', 'pow', 3, Code01_GridHappiness.MAXM)))
Code01_GridHappiness.n = jcast('int', 0)
Code01_GridHappiness.m = jcast('int', 0)
Code01_GridHappiness.maxs = jcast('int', 0)
Code01_GridHappiness.dp = jarray('int', [Code01_GridHappiness.MAXN, Code01_GridHappiness.MAXM, Code01_GridHappiness.MAXS, Code01_GridHappiness.MAXP, Code01_GridHappiness.MAXP])
