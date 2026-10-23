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

# 掉落的方块
# 有一个二维平面，x轴是最底的边界
# 给定二维整数数组pos，pos[i] = [ lefti, leni ]
# 表示第i个方块边长为leni，左侧边缘在x = lefti位置，所在高度非常高
# 所有方块都是正方形，依次从高处垂直掉落，也就是左边界顺着x = lefti往下
# 如果掉落的方块碰到已经掉落正方形的顶边或者x轴就停止掉落
# 如果方块掉落时仅仅是擦过已经掉落正方形的左侧边或右侧边，并不会停止掉落
# 一旦停止，它就会固定在那里，无法再移动，俄罗斯方块游戏和本题意思一样
# 返回一个整数数组ans ，其中ans[i]表示在第i块方块掉落后整体的最大高度
# 1 <= pos数组长度 <= 1000，1 <= lefti <= 10^8，1 <= leni <= 10^6
# 测试链接 : https://leetcode.cn/problems/falling-squares
class Code01_FallingSquares:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'max': 'max', 'change': 'change', 'update': 'update_data'}
    MAXN = 0
    arr = None
    max = None
    change = None
    update_data = None
    @staticmethod
    def collect(poss):
        size = jcast('int', 1)
        for pos in poss:
            jset(Code01_FallingSquares.arr, ((_java_old_1 := size), (size := jcast('int', (size + (1)))), _java_old_1)[2], pos[0])
            jset(Code01_FallingSquares.arr, ((_java_old_2 := size), (size := jcast('int', (size + (1)))), _java_old_2)[2], jcast('int', (jcast('int', jadd(pos[0], pos[1])) - 1)))
        jstatic('Arrays', 'sort', Code01_FallingSquares.arr, 1, size)
        n = jcast('int', 1)
        i = jcast('int', 2)
        while (i < size):
            if (Code01_FallingSquares.arr[n] != Code01_FallingSquares.arr[i]):
                jset(Code01_FallingSquares.arr, (n := jcast('int', (n + (1)))), Code01_FallingSquares.arr[i])
            i = jcast('int', (i + 1))
        return jcast('int', n)

    @staticmethod
    def rank(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        ans = jcast('int', 0)
        l = jcast('int', 1)
        r = jcast('int', n)
        m = 0
        while (l <= r):
            m = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code01_FallingSquares.arr[m] >= v):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        jset(Code01_FallingSquares.max, i, jstatic('Math', 'max', Code01_FallingSquares.max[jcast('int', (i << (1 & 31)))], Code01_FallingSquares.max[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if Code01_FallingSquares.update_data[i]:
            Code01_FallingSquares.lazy(jcast('int', (i << (1 & 31))), Code01_FallingSquares.change[i])
            Code01_FallingSquares.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code01_FallingSquares.change[i])
            Code01_FallingSquares.update_data[i] = jcast('boolean', False)

    @staticmethod
    def lazy(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        Code01_FallingSquares.update_data[i] = jcast('boolean', True)
        Code01_FallingSquares.change[i] = jcast('int', v)
        Code01_FallingSquares.max[i] = jcast('int', v)

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code01_FallingSquares.build(l, mid, jcast('int', (i << (1 & 31))))
            Code01_FallingSquares.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code01_FallingSquares.max[i] = jcast('int', 0)
        Code01_FallingSquares.change[i] = jcast('int', 0)
        Code01_FallingSquares.update_data[i] = jcast('boolean', False)

    @staticmethod
    def update(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code01_FallingSquares.lazy(i, jobv)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code01_FallingSquares.down(i)
            if (jobl <= mid):
                Code01_FallingSquares.update(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code01_FallingSquares.update(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code01_FallingSquares.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code01_FallingSquares.max[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        Code01_FallingSquares.down(i)
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        if (jobl <= mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code01_FallingSquares.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code01_FallingSquares.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('int', ans)

    @staticmethod
    def fallingSquares(pos):
        n = jcast('int', Code01_FallingSquares.collect(pos))
        Code01_FallingSquares.build(1, n, 1)
        ans = jnew('ArrayList')
        max = jcast('int', 0)
        l = 0
        r = 0
        h = 0
        for square in pos:
            l = jcast('int', Code01_FallingSquares.rank(n, square[0]))
            r = jcast('int', Code01_FallingSquares.rank(n, jcast('int', (jcast('int', jadd(square[0], square[1])) - 1))))
            h = jcast('int', jcast('int', jadd(Code01_FallingSquares.query(l, r, 1, n, 1), square[1])))
            max = jcast('int', jstatic('Math', 'max', max, h))
            jcall(ans, 'add', max)
            Code01_FallingSquares.update(l, r, h, 1, n, 1)
        return ans

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_FallingSquares.MAXN = jcast('int', 2001)
Code01_FallingSquares.arr = jarray('int', [Code01_FallingSquares.MAXN])
Code01_FallingSquares.max = jarray('int', [jcast('int', (Code01_FallingSquares.MAXN << (2 & 31)))])
Code01_FallingSquares.change = jarray('int', [jcast('int', (Code01_FallingSquares.MAXN << (2 & 31)))])
Code01_FallingSquares.update_data = jarray('boolean', [jcast('int', (Code01_FallingSquares.MAXN << (2 & 31)))])
