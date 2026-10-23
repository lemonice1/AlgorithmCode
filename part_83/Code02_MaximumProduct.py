# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 分成k份的最大乘积
# 一个数字n一定要分成k份，得到的乘积尽量大是多少
# 数字n和k，可能非常大，到达10^12规模
# 结果可能更大，所以返回结果对 1000000007 取模
# 来自真实大厂笔试，没有在线测试，对数器验证
class Code02_MaximumProduct:
    __java_fields__ = {}
    # 暴力递归
    # 为了验证
    @staticmethod
    def maxValue1(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        return jcast('int', Code02_MaximumProduct.f1(n, k))

    # 剩余的数字rest拆成k份
    # 返回最大乘积
    # 暴力尝试一定能得到最优解
    @staticmethod
    def f1(rest, k):
        rest = jcast('int', rest)
        k = jcast('int', k)
        if (k == 1):
            return jcast('int', rest)
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        cur = jcast('int', 1)
        while ((cur <= rest) and (jcast('int', (rest - cur)) >= jcast('int', (k - 1)))):
            curAns = jcast('int', jcast('int', (cur * Code02_MaximumProduct.f1(jcast('int', (rest - cur)), jcast('int', (k - 1))))))
            ans = jcast('int', jstatic('Math', 'max', ans, curAns))
            cur = jcast('int', (cur + 1))
        return jcast('int', ans)

    # 贪心的解
    # 这是最优解
    # 如果结果很大，那么求余数
    @staticmethod
    def maxValue2(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        mod = jcast('int', 1000000007)
        a = jcast('long', jcast('int', jdiv(n, k)))
        b = jcast('int', jcast('int', jmod(n, k)))
        part1 = jcast('long', Code02_MaximumProduct.power(jcast('long', jadd(a, 1)), b, mod))
        part2 = jcast('long', Code02_MaximumProduct.power(a, jcast('int', (k - b)), mod))
        return jcast('int', jcast('int', jmod(jcast('int', jcast('long', (part1 * part2))), mod)))

    @staticmethod
    def power(x, n, mod):
        x = jcast('long', x)
        n = jcast('int', n)
        mod = jcast('int', mod)
        ans = jcast('long', 1)
        while (n > 0):
            if (jcast('int', (n & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), mod)))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), mod)))
            n = jcast('int', jcast('int', (n >> (1 & 31))))
        return jcast('long', ans)

    # 对数器
    # 为了验证
    @staticmethod
    def main(args):
        N = jcast('int', 30)
        testTimes = jcast('int', 2000)
        jprint('测试开始', newline=True)
        i = jcast('int', 1)
        while (i <= testTimes):
            n = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * N)), 1)))
            k = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            ans1 = jcast('int', Code02_MaximumProduct.maxValue1(n, k))
            ans2 = jcast('int', Code02_MaximumProduct.maxValue2(n, k))
            if (ans1 != ans2):
                # 如果出错了
                # 可以增加打印行为找到一组出错的例子
                # 然后去debug
                jprint('出错了！', newline=True)
            if (jcast('int', jmod(i, 100)) == 0):
                jprint(jadd(jadd('测试到第', i), '组'), newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code02_MaximumProduct.main([])
