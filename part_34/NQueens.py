# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# N皇后问题
# 测试链接 : https://leetcode.cn/problems/n-queens-ii/
class NQueens:
    __java_fields__ = {}
    # 用数组表示路径实现的N皇后问题，不推荐
    @staticmethod
    def totalNQueens1(n):
        n = jcast('int', n)
        if (n < 1):
            return jcast('int', 0)
        return jcast('int', NQueens.f1(0, jarray('int', [n]), n))

    # i : 当前来到的行
    # path : 0...i-1行的皇后，都摆在了哪些列
    # n : 是几皇后问题
    # 返回 : 0...i-1行已经摆完了，i....n-1行可以去尝试的情况下还能找到几种有效的方法
    @staticmethod
    def f1(i, path, n):
        i = jcast('int', i)
        n = jcast('int', n)
        if (i == n):
            return jcast('int', 1)
        ans = jcast('int', 0)
        # 0 1 2 3 .. n-1
        # i j
        j = jcast('int', 0)
        while (j < n):
            if NQueens.check(path, i, j):
                path[i] = jcast('int', j)
                ans = jcast('int', jcast('int', jadd(ans, NQueens.f1(jcast('int', jadd(i, 1)), path, n))))
            j = jcast('int', (j + 1))
        return jcast('int', ans)

    # 当前在i行、j列的位置，摆了一个皇后
    # 0...i-1行的皇后状况，path[0...i-1]
    # 返回会不会冲突，不会冲突，有效！true
    # 会冲突，无效，返回false
    @staticmethod
    def check(path, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        # 当前 i
        # 当列 j
        k = jcast('int', 0)
        while (k < i):
            # 0...i-1
            # 之前行 : k
            # 之前列 : path[k]
            if ((j == path[k]) or (jstatic('Math', 'abs', jcast('int', (i - k))) == jstatic('Math', 'abs', jcast('int', (j - path[k]))))):
                return jcast('boolean', False)
            k = jcast('int', (k + 1))
        return jcast('boolean', True)

    # 用位信息表示路径实现的N皇后问题，推荐
    @staticmethod
    def totalNQueens2(n):
        n = jcast('int', n)
        if (n < 1):
            return jcast('int', 0)
        # n = 5
        # 1 << 5 = 0...100000 - 1
        # limit  = 0...011111;
        # n = 7
        # limit  = 0...01111111;
        limit = jcast('int', jcast('int', (jcast('int', (1 << (n & 31))) - 1)))
        return jcast('int', NQueens.f2(limit, 0, 0, 0))

    # limit : 当前是几皇后问题
    # 之前皇后的列影响：col
    # 之前皇后的右上 -> 左下对角线影响：left
    # 之前皇后的左上 -> 右下对角线影响：right
    @staticmethod
    def f2(limit, col, left, right):
        limit = jcast('int', limit)
        col = jcast('int', col)
        left = jcast('int', left)
        right = jcast('int', right)
        if (col == limit):
            # 所有皇后放完了！
            return jcast('int', 1)
        # 总限制
        ban = jcast('int', jcast('int', (jcast('int', (col | left)) | right)))
        # ~ban : 1可放皇后，0不能放
        candidate = jcast('int', jcast('int', (limit & jcast('int', (~ban)))))
        # 放置皇后的尝试！
        place = jcast('int', 0)
        # 一共有多少有效的方法
        ans = jcast('int', 0)
        while (candidate != 0):
            # 提取出最右侧的1
            # 0 0 1 1 1 0
            # 5 4 3 2 1 0
            # place :
            # 0 0 0 0 1 0
            # candidate :
            # 0 0 1 1 0 0
            # 5 4 3 2 1 0
            # place :
            # 0 0 0 1 0 0
            # candidate :
            # 0 0 1 0 0 0
            # 5 4 3 2 1 0
            # place :
            # 0 0 1 0 0 0
            # candidate :
            # 0 0 0 0 0 0
            # 5 4 3 2 1 0
            place = jcast('int', jcast('int', (candidate & jcast('int', (-candidate)))))
            candidate = jcast('int', jcast('int', (candidate ^ place)))
            ans = jcast('int', jcast('int', jadd(ans, NQueens.f2(limit, jcast('int', (col | place)), jcast('int', (jcast('int', (left | place)) >> (1 & 31))), jcast('int', (jcast('int', (right | place)) << (1 & 31)))))))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        n = jcast('int', 14)
        start = 0
        end = 0
        jprint('测试开始', newline=True)
        jprint(jadd(jadd('解决', n), '皇后问题'), newline=True)
        start = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd('方法1答案 : ', NQueens.totalNQueens1(n)), newline=True)
        end = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd(jadd('方法1运行时间 : ', jcast('long', (end - start))), ' 毫秒'), newline=True)
        start = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd('方法2答案 : ', NQueens.totalNQueens2(n)), newline=True)
        end = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd(jadd('方法2运行时间 : ', jcast('long', (end - start))), ' 毫秒'), newline=True)
        jprint('测试结束', newline=True)
        jprint('=======', newline=True)
        jprint('只有位运算的版本，才能10秒内跑完16皇后问题的求解过程', newline=True)
        start = jcast('long', jstatic('System', 'currentTimeMillis'))
        ans = jcast('int', NQueens.totalNQueens2(16))
        end = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd('16皇后问题的答案 : ', ans), newline=True)
        jprint(jadd(jadd('运行时间 : ', jcast('long', (end - start))), ' 毫秒'), newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    NQueens.main([])
