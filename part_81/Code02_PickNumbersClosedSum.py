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

# 选择k个数字使得两集合累加和相差不超过1
# 给定一个正数n，表示1~n这些数字都可以选择
# 给定一个正数k，表示要从1~n中选择k个数字组成集合A，剩下数字组成集合B
# 希望做到集合A和集合B的累加和相差不超过1
# 如果能做到，返回集合A选择了哪些数字，任何一种方案都可以
# 如果不能做到，返回长度为0的数组
# 2 <= n <= 10^6
# 1 <= k <= n
# 来自真实大厂笔试，没有测试链接，用对数器验证
class Code02_PickNumbersClosedSum:
    __java_fields__ = {}
    # 正式方法
    # 最优解
    @staticmethod
    def pick(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        sum = jcast('long', jcast('int', jdiv(jcast('int', (jcast('int', jadd(n, 1)) * n)), 2)))
        ans = Code02_PickNumbersClosedSum.generate(jcast('long', jdiv(sum, 2)), n, k)
        if ((jget(ans, 'length') == 0) and (jcast('long', (sum & 1)) == 1)):
            ans = Code02_PickNumbersClosedSum.generate(jcast('long', jadd(jcast('long', jdiv(sum, 2)), 1)), n, k)
        return ans

    # 1 ~ n这些数字挑选k个
    # 能不能凑够累加和sum
    # 能的话，返回挑选了哪些数字
    # 不能的话，返回长度为0的数组
    @staticmethod
    def generate(sum, n, k):
        sum = jcast('long', sum)
        n = jcast('int', n)
        k = jcast('int', k)
        minKSum = jcast('long', jcast('int', jdiv(jcast('int', (jcast('int', jadd(k, 1)) * k)), 2)))
        range = jcast('int', jcast('int', (n - k)))
        if ((sum < minKSum) or (sum > jcast('long', jadd(minKSum, jcast('long', (jcast('long', range) * k)))))):
            return jarray('int', [0])
        # 100 15 -> 85
        need = jcast('long', jcast('long', (sum - minKSum)))
        rightSize = jcast('int', jcast('int', jcast('long', jdiv(need, range))))
        midIndex = jcast('int', jcast('int', jadd(jcast('int', (k - rightSize)), jcast('int', jcast('long', jmod(need, range))))))
        leftSize = jcast('int', jcast('int', (jcast('int', (k - rightSize)) - (0 if (jcast('long', jmod(need, range)) == 0) else 1))))
        ans = jarray('int', [k])
        i = jcast('int', 0)
        while (i < leftSize):
            ans[i] = jcast('int', jcast('int', jadd(i, 1)))
            i = jcast('int', (i + 1))
        if (jcast('long', jmod(need, range)) != 0):
            ans[leftSize] = jcast('int', midIndex)
        i = jcast('int', jcast('int', (k - 1)))
        j = jcast('int', 0)
        while (j < rightSize):
            ans[i] = jcast('int', jcast('int', (n - j)))
            i = jcast('int', (i - 1))
            j = jcast('int', (j + 1))
        return ans

    # 为了验证
    # 检验得到的结果是否正确
    @staticmethod
    def pass_(n, k, ans):
        n = jcast('int', n)
        k = jcast('int', k)
        if (jget(ans, 'length') == 0):
            if Code02_PickNumbersClosedSum.canSplit(n, k):
                return jcast('boolean', False)
            else:
                return jcast('boolean', True)
        else:
            if (jget(ans, 'length') != k):
                return jcast('boolean', False)
            sum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(n, 1)) * n)), 2)))
            pickSum = jcast('int', 0)
            for num in ans:
                pickSum = jcast('int', jcast('int', jadd(pickSum, num)))
            return jcast('boolean', (jstatic('Math', 'abs', jcast('int', (pickSum - jcast('int', (sum - pickSum))))) <= 1))

    # 记忆化搜索
    # 不是最优解，只是为了验证
    # 返回能不能做到
    @staticmethod
    def canSplit(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        sum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(n, 1)) * n)), 2)))
        wantSum = jcast('int', jcast('int', jadd(jcast('int', jdiv(sum, 2)), (0 if (jcast('int', (sum & 1)) == 0) else 1))))
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(k, 1)), jcast('int', jadd(wantSum, 1))])
        return jcast('boolean', Code02_PickNumbersClosedSum.f(n, 1, k, wantSum, dp))

    @staticmethod
    def f(n, i, k, s, dp):
        n = jcast('int', n)
        i = jcast('int', i)
        k = jcast('int', k)
        s = jcast('int', s)
        if ((k < 0) or (s < 0)):
            return jcast('boolean', False)
        if (i == jcast('int', jadd(n, 1))):
            return jcast('boolean', ((k == 0) and (s == 0)))
        if (dp[i][k][s] != 0):
            return jcast('boolean', (dp[i][k][s] == 1))
        ans = jcast('boolean', (Code02_PickNumbersClosedSum.f(n, jcast('int', jadd(i, 1)), k, s, dp) or Code02_PickNumbersClosedSum.f(n, jcast('int', jadd(i, 1)), jcast('int', (k - 1)), jcast('int', (s - i)), dp)))
        jset(dp[i][k], s, (1 if ans else jcast('int', (-1))))
        return jcast('boolean', ans)

    # 为了验证
    # 对数器
    @staticmethod
    def main(args):
        N = jcast('int', 60)
        testTime = jcast('int', 5000)
        jprint('测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTime):
            n = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * N)), 2)))
            k = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            ans = Code02_PickNumbersClosedSum.pick(n, k)
            if (not Code02_PickNumbersClosedSum.pass_(n, k, ans)):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code02_PickNumbersClosedSum.main([])
