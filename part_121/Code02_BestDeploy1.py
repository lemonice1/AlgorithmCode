# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 注意查看Code02_BestDeploy2文件，找到了题目2的在线测试
# 最好的部署
# 一共有n台机器，编号1 ~ n，所有机器排成一排
# 你只能一台一台的部署机器，你可以决定部署的顺序，最终所有机器都要部署
# 给定三个数组no[]、one[]、both[]
# no[i] : 如果i号机器部署时，相邻没有机器部署，此时能获得的收益
# one[i] : 如果i号机器部署时，相邻有一台机器部署，此时能获得的收益
# both[i] : 如果i号机器部署时，相邻有两台机器部署，此时能获得的收益
# 第1号机器、第n号机器当然不会有两台相邻的机器
# 返回部署的最大收益
# 1 <= n <= 10^5
# 0 <= no[i]、one[i]、both[i]
# 来自真实大厂笔试，对数器验证
class Code02_BestDeploy1:
    __java_fields__ = {'MAXN': 'MAXN', 'no': 'no', 'one': 'one', 'both': 'both', 'n': 'n'}
    MAXN = 0
    no = None
    one = None
    both = None
    n = 0
    # 区间dp的尝试
    # 时间复杂度O(n^3)
    # 正确但是并不推荐
    @staticmethod
    def best1():
        dp = jarray('int', [jcast('int', jadd(Code02_BestDeploy1.n, 1)), jcast('int', jadd(Code02_BestDeploy1.n, 1))])
        l = jcast('int', 1)
        while (l <= Code02_BestDeploy1.n):
            r = jcast('int', l)
            while (r <= Code02_BestDeploy1.n):
                jset(dp[l], r, jcast('int', (-1)))
                r = jcast('int', (r + 1))
            l = jcast('int', (l + 1))
        return jcast('int', Code02_BestDeploy1.f(1, Code02_BestDeploy1.n, dp))

    # 部署l...r范围上的机器
    # 并且l-1和r+1的机器一定都没有部署
    # 返回部署的最大收益
    @staticmethod
    def f(l, r, dp):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return jcast('int', Code02_BestDeploy1.no[l])
        if (dp[l][r] != jcast('int', (-1))):
            return jcast('int', dp[l][r])
        ans = jcast('int', jcast('int', jadd(Code02_BestDeploy1.f(jcast('int', jadd(l, 1)), r, dp), Code02_BestDeploy1.one[l])))
        ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(Code02_BestDeploy1.f(l, jcast('int', (r - 1)), dp), Code02_BestDeploy1.one[r]))))
        i = jcast('int', jcast('int', jadd(l, 1)))
        while (i < r):
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(jcast('int', jadd(Code02_BestDeploy1.f(l, jcast('int', (i - 1)), dp), Code02_BestDeploy1.f(jcast('int', jadd(i, 1)), r, dp))), Code02_BestDeploy1.both[i]))))
            i = jcast('int', (i + 1))
        jset(dp[l], r, ans)
        return jcast('int', ans)

    # 线性dp的尝试
    # 时间复杂度O(n)
    # 推荐
    @staticmethod
    def best2():
        # dp[i][0] : i号机器的前一台机器没有部署的情况下，部署i...的机器获得的最大收益
        # dp[i][1] : i号机器的前一台机器已经部署的情况下，部署i...的机器获得的最大收益
        dp = jarray('int', [jcast('int', jadd(Code02_BestDeploy1.n, 1)), 2])
        jset(dp[Code02_BestDeploy1.n], 0, Code02_BestDeploy1.no[Code02_BestDeploy1.n])
        jset(dp[Code02_BestDeploy1.n], 1, Code02_BestDeploy1.one[Code02_BestDeploy1.n])
        i = jcast('int', jcast('int', (Code02_BestDeploy1.n - 1)))
        while (i >= 1):
            jset(dp[i], 0, jstatic('Math', 'max', jcast('int', jadd(Code02_BestDeploy1.no[i], dp[jcast('int', jadd(i, 1))][1])), jcast('int', jadd(Code02_BestDeploy1.one[i], dp[jcast('int', jadd(i, 1))][0]))))
            jset(dp[i], 1, jstatic('Math', 'max', jcast('int', jadd(Code02_BestDeploy1.one[i], dp[jcast('int', jadd(i, 1))][1])), jcast('int', jadd(Code02_BestDeploy1.both[i], dp[jcast('int', jadd(i, 1))][0]))))
            i = jcast('int', (i - 1))
        return jcast('int', dp[1][0])

    # 为了测试
    @staticmethod
    def random(size, v):
        size = jcast('int', size)
        v = jcast('int', v)
        Code02_BestDeploy1.n = jcast('int', size)
        i = jcast('int', 1)
        while (i <= Code02_BestDeploy1.n):
            jset(Code02_BestDeploy1.no, i, jcast('int', (jstatic('Math', 'random') * v)))
            jset(Code02_BestDeploy1.one, i, jcast('int', (jstatic('Math', 'random') * v)))
            jset(Code02_BestDeploy1.both, i, jcast('int', (jstatic('Math', 'random') * v)))
            i = jcast('int', (i + 1))

    # 为了测试
    @staticmethod
    def main(args):
        maxn = jcast('int', 100)
        maxv = jcast('int', 100)
        testTime = jcast('int', 10000)
        jprint('测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTime):
            size = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * maxn)), 1)))
            Code02_BestDeploy1.random(size, maxv)
            ans1 = jcast('int', Code02_BestDeploy1.best1())
            ans2 = jcast('int', Code02_BestDeploy1.best2())
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_BestDeploy1.MAXN = jcast('int', 1001)
Code02_BestDeploy1.no = jarray('int', [Code02_BestDeploy1.MAXN])
Code02_BestDeploy1.one = jarray('int', [Code02_BestDeploy1.MAXN])
Code02_BestDeploy1.both = jarray('int', [Code02_BestDeploy1.MAXN])
Code02_BestDeploy1.n = jcast('int', 0)

if __name__ == '__main__':
    Code02_BestDeploy1.main([])
