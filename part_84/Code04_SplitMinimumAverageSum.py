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

# 平均值最小累加和
# 给定一个数组arr，长度为n
# 再给定一个数字k，表示一定要将arr划分成k个集合
# 每个数字只能进一个集合
# 返回每个集合的平均值都累加起来的最小值
# 平均值向下取整
# 1 <= n <= 10^5
# 0 <= arr[i] <= 10^5
# 1 <= k <= n
# 来自真实大厂笔试，没有在线测试，对数器验证
class Code04_SplitMinimumAverageSum:
    __java_fields__ = {}
    # 暴力方法
    # 为了验证
    # 每个数字做出所有可能的选择
    # 时间复杂度O(k的n次方)
    @staticmethod
    def minAverageSum1(arr, k):
        k = jcast('int', k)
        sum = jarray('int', [k])
        cnt = jarray('int', [k])
        return jcast('int', Code04_SplitMinimumAverageSum.f(arr, 0, sum, cnt))

    # 暴力方法
    # 为了验证
    @staticmethod
    def f(arr, i, sum, cnt):
        i = jcast('int', i)
        if (i == jget(arr, 'length')):
            ans = jcast('int', 0)
            j = jcast('int', 0)
            while (j < jget(sum, 'length')):
                if (cnt[j] == 0):
                    return jcast('int', jget(Integer, 'MAX_VALUE'))
                ans = jcast('int', jcast('int', jadd(ans, jcast('int', jdiv(sum[j], cnt[j])))))
                j = jcast('int', (j + 1))
            return jcast('int', ans)
        else:
            ans = jcast('int', jget(Integer, 'MAX_VALUE'))
            j = jcast('int', 0)
            while (j < jget(sum, 'length')):
                sum[j] = jcast('int', jcast('int', jadd(sum[j], arr[i])))
                cnt[j] = jcast('int', (cnt[j] + 1))
                ans = jcast('int', jstatic('Math', 'min', ans, Code04_SplitMinimumAverageSum.f(arr, jcast('int', jadd(i, 1)), sum, cnt)))
                sum[j] = jcast('int', jcast('int', (sum[j] - arr[i])))
                cnt[j] = jcast('int', (cnt[j] - 1))
                j = jcast('int', (j + 1))
            return jcast('int', ans)

    # 正式方法
    # 时间复杂度O(n * logn)
    @staticmethod
    def minAverageSum2(arr, k):
        k = jcast('int', k)
        jstatic('Arrays', 'sort', arr)
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < jcast('int', (k - 1))):
            # 最小的k-1个数，每个数独自成一个集合
            ans = jcast('int', jcast('int', jadd(ans, arr[i])))
            i = jcast('int', (i + 1))
        sum = jcast('int', 0)
        i = jcast('int', jcast('int', (k - 1)))
        while (i < jget(arr, 'length')):
            sum = jcast('int', jcast('int', jadd(sum, arr[i])))
            i = jcast('int', (i + 1))
        ans = jcast('int', jcast('int', jadd(ans, jcast('int', jdiv(sum, jcast('int', jadd(jcast('int', (jget(arr, 'length') - k)), 1)))))))
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
        N = jcast('int', 8)
        V = jcast('int', 10000)
        testTimes = jcast('int', 2000)
        jprint('测试开始', newline=True)
        i = jcast('int', 1)
        while (i <= testTimes):
            n = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * N)), 1)))
            arr = Code04_SplitMinimumAverageSum.randomArray(n, V)
            k = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            ans1 = jcast('int', Code04_SplitMinimumAverageSum.minAverageSum1(arr, k))
            ans2 = jcast('int', Code04_SplitMinimumAverageSum.minAverageSum2(arr, k))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            if (jcast('int', jmod(i, 100)) == 0):
                jprint(jadd(jadd('测试到第', i), '组'), newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code04_SplitMinimumAverageSum.main([])
