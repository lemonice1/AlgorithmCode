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

# 相乘为正或负的子数组数量
# 给定一个长度为n的数组arr，其中所有值都不是0
# 返回有多少个子数组相乘的结果是正
# 返回有多少个子数组相乘的结果是负
# 1 <= n <= 10^6
# -10^9 <= arr[i] <= +10^9，arr[i]一定不是0
# 来自真实大厂笔试，对数器验证
class Code03_MultiplyPositiveNegative1:
    __java_fields__ = {}
    # 正式方法
    @staticmethod
    def num(arr):
        # 0 : 正状态
        # 1 : 负状态
        # ^ : 乘法运算
        cnt = jarray('int', [2])
        cnt[0] = jcast('int', 1)
        cnt[1] = jcast('int', 0)
        ans1 = jcast('int', 0)
        ans2 = jcast('int', 0)
        i = jcast('int', 0)
        cur = jcast('int', 0)
        while (i < jget(arr, 'length')):
            cur = jcast('int', jcast('int', (cur ^ (0 if (arr[i] > 0) else 1))))
            ans1 = jcast('int', jcast('int', jadd(ans1, cnt[cur])))
            ans2 = jcast('int', jcast('int', jadd(ans2, cnt[jcast('int', (cur ^ 1))])))
            cnt[cur] = jcast('int', (cnt[cur] + 1))
            i = jcast('int', (i + 1))
        return jarray('int', [None], [ans1, ans2])

    # 暴力方法
    # 为了验证
    @staticmethod
    def right(arr):
        n = jcast('int', jget(arr, 'length'))
        ans1 = jcast('int', 0)
        ans2 = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            cur = jcast('long', 1)
            j = jcast('int', i)
            while (j < n):
                cur = jcast('long', jcast('long', (cur * arr[j])))
                if (cur > 0):
                    ans1 = jcast('int', (ans1 + 1))
                else:
                    ans2 = jcast('int', (ans2 + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jarray('int', [None], [ans1, ans2])

    # 为了验证
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        ans = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            while True:
                jset(ans, i, jcast('int', (jcast('int', ((jstatic('Math', 'random') * v) * 2)) - v)))
                if not ((ans[i] == 0)):
                    break
            i = jcast('int', (i + 1))
        return ans

    @staticmethod
    def main(args):
        # 正式方法无所谓，怎么都正确
        # 但是对数器方法是暴力乘起来，所以n和v不要太大，防止溢出
        n = jcast('int', 20)
        v = jcast('int', 10)
        testTime = jcast('int', 10000)
        jprint('测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTime):
            size = jcast('int', jcast('int', (jstatic('Math', 'random') * n)))
            arr = Code03_MultiplyPositiveNegative1.randomArray(size, v)
            ans1 = Code03_MultiplyPositiveNegative1.num(arr)
            ans2 = Code03_MultiplyPositiveNegative1.right(arr)
            if ((ans1[0] != ans2[0]) or (ans1[1] != ans2[1])):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code03_MultiplyPositiveNegative1.main([])
