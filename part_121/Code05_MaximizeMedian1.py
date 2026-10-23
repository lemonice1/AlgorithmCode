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

# 相邻必选的子序列最大中位数
# 给定一个长度为n的数组arr
# 合法子序列定义为，任意相邻的两个数至少要有一个被挑选所组成的子序列
# 求所有合法子序列中，最大中位数是多少
# 中位数的定义为上中位数
# [1, 2, 3, 4]的上中位数是2
# [1, 2, 3, 4, 5]的上中位数是3
# 2 <=  n <= 10^5
# 1 <= arr[i] <= 10^9
# 来自真实大厂笔试，对数器验证
class Code05_MaximizeMedian1:
    __java_fields__ = {}
    # 正式方法
    # 时间复杂度O(n * log n)
    @staticmethod
    def maximizeMedian(arr):
        n = jcast('int', jget(arr, 'length'))
        sort = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            sort[i] = jcast('int', arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', sort)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (n - 1)))
        m = jcast('int', 0)
        ans = jcast('int', jcast('int', (-1)))
        help = jarray('int', [n])
        dp = jarray('int', [jcast('int', jadd(n, 1)), 2])
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if Code05_MaximizeMedian1.check(arr, help, dp, sort[m], n):
                ans = jcast('int', sort[m])
                l = jcast('int', jcast('int', jadd(m, 1)))
            else:
                r = jcast('int', jcast('int', (m - 1)))
        return jcast('int', ans)

    # 任意相邻的两数至少选一个来生成子序列
    # 到底有没有一个合法子序列，能让其中>=x的数达到一半以上
    @staticmethod
    def check(arr, help, dp, x, n):
        x = jcast('int', x)
        n = jcast('int', n)
        i = jcast('int', 0)
        while (i < n):
            help[i] = jcast('int', (1 if (arr[i] >= x) else jcast('int', (-1))))
            i = jcast('int', (i + 1))
        return jcast('boolean', (Code05_MaximizeMedian1.dp(help, dp, n) > 0))

    # 任意相邻的两数至少选一个来生成子序列
    # 返回合法子序列的最大累加和
    @staticmethod
    def dp(arr, dp, n):
        n = jcast('int', n)
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            # dp[i][0] : i位置的数字，选和不选皆可，i...范围上形成合法子序列的最大累加和
            # dp[i][1] : i位置的数字，一定要选，i...范围上形成合法子序列的最大累加和
            jset(dp[i], 0, jstatic('Math', 'max', jcast('int', jadd(arr[i], dp[jcast('int', jadd(i, 1))][0])), dp[jcast('int', jadd(i, 1))][1]))
            jset(dp[i], 1, jcast('int', jadd(arr[i], dp[jcast('int', jadd(i, 1))][0])))
            i = jcast('int', (i - 1))
        return jcast('int', dp[0][0])

    # 暴力方法
    # 为了验证
    @staticmethod
    def right(arr):
        path = jarray('int', [jget(arr, 'length')])
        return jcast('int', Code05_MaximizeMedian1.dfs(arr, 0, True, path, 0))

    # 暴力方法
    # 为了验证
    @staticmethod
    def dfs(arr, i, pre, path, size):
        i = jcast('int', i)
        pre = jcast('boolean', pre)
        size = jcast('int', size)
        if (i == jget(arr, 'length')):
            if (size == 0):
                return jcast('int', 0)
            sort = jarray('int', [size])
            j = jcast('int', 0)
            while (j < size):
                sort[j] = jcast('int', path[j])
                j = jcast('int', (j + 1))
            jstatic('Arrays', 'sort', sort)
            return jcast('int', sort[jcast('int', jdiv(jcast('int', (jget(sort, 'length') - 1)), 2))])
        else:
            path[size] = jcast('int', arr[i])
            ans = jcast('int', Code05_MaximizeMedian1.dfs(arr, jcast('int', jadd(i, 1)), True, path, jcast('int', jadd(size, 1))))
            if pre:
                ans = jcast('int', jstatic('Math', 'max', ans, Code05_MaximizeMedian1.dfs(arr, jcast('int', jadd(i, 1)), False, path, size)))
            return jcast('int', ans)

    # 为了测试
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        ans = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            jset(ans, i, jcast('int', (jstatic('Math', 'random') * v)))
            i = jcast('int', (i + 1))
        return ans

    # 为了测试
    @staticmethod
    def main(args):
        n = jcast('int', 20)
        v = jcast('int', 1000)
        testTime = jcast('int', 10000)
        jprint('功能测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTime):
            size = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            arr = Code05_MaximizeMedian1.randomArray(size, v)
            ans1 = jcast('int', Code05_MaximizeMedian1.right(arr))
            ans2 = jcast('int', Code05_MaximizeMedian1.maximizeMedian(arr))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('功能测试结束', newline=True)
        jprint(newline=True)
        jprint('性能测试开始', newline=True)
        n = jcast('int', 100000)
        v = jcast('int', 50000000)
        jprint(jadd('数组长度 : ', n), newline=True)
        jprint(jadd('数值范围 : ', v), newline=True)
        arr = Code05_MaximizeMedian1.randomArray(n, v)
        start = jcast('long', jstatic('System', 'currentTimeMillis'))
        Code05_MaximizeMedian1.maximizeMedian(arr)
        end = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd(jadd('正式方法的运行时间 : ', jcast('long', (end - start))), ' 毫秒'), newline=True)
        jprint('性能测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code05_MaximizeMedian1.main([])
