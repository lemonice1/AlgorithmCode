# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 分割的方法数
# 给定一个长度为n的数组A, 将其分割成数组B和数组C，满足A[i] = B[i] + C[i]
# 也就是一个数字分成两份，然后各自进入B和C，要求B[i], C[i] >= 1
# 同时要求，B数组从左到右不能降序，C数组从左到右不能升序
# 比如，A = { 5, 4, 5 }，一种有效的划分，B = { 2, 2, 3 }，C = { 3, 2, 2 }
# 返回有多少种有效的划分方式
# 1 <= n <= 10^7
# 1 <= A[i] <= 10^7
# 最终结果可能很大，答案对 1000000007 取模
# 来自真实大厂笔试题，该实现为对数器版本
# 有同学找到了测试链接，就是Code04_SplitWays2文件
class Code04_SplitWays1:
    __java_fields__ = {'MOD': 'MOD'}
    # 暴力方法
    # 为了验证
    @staticmethod
    def ways1(arr):
        ans = jcast('int', 0)
        b = jcast('int', 1)
        c = jcast('int', jcast('int', (arr[0] - 1)))
        while (b < arr[0]):
            ans = jcast('int', jcast('int', jadd(ans, Code04_SplitWays1.f(arr, 1, b, c))))
            b = jcast('int', (b + 1))
            c = jcast('int', (c - 1))
        return jcast('int', ans)

    @staticmethod
    def f(arr, i, preb, prec):
        i = jcast('int', i)
        preb = jcast('int', preb)
        prec = jcast('int', prec)
        if (i == jget(arr, 'length')):
            return jcast('int', 1)
        ans = jcast('int', 0)
        b = jcast('int', 1)
        c = jcast('int', jcast('int', (arr[i] - 1)))
        while (b < arr[i]):
            if ((preb <= b) and (prec >= c)):
                ans = jcast('int', jcast('int', jadd(ans, Code04_SplitWays1.f(arr, jcast('int', jadd(i, 1)), b, c))))
            b = jcast('int', (b + 1))
            c = jcast('int', (c - 1))
        return jcast('int', ans)

    # 正式方法
    # 转化成杨辉三角
    MOD = 0
    @staticmethod
    def ways2(arr):
        n = jcast('int', jget(arr, 'length'))
        k = jcast('int', jcast('int', (arr[0] - 1)))
        i = jcast('int', 1)
        while ((i < n) and (k > 0)):
            if (arr[jcast('int', (i - 1))] > arr[i]):
                k = jcast('int', jcast('int', (k - jcast('int', (arr[jcast('int', (i - 1))] - arr[i])))))
            i = jcast('int', (i + 1))
        if (k <= 0):
            return jcast('int', 0)
        return jcast('int', Code04_SplitWays1.c(jcast('int', (jcast('int', jadd(k, n)) - 1)), n))

    # 组合公式
    @staticmethod
    def c(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        fac = jcast('long', 1)
        inv1 = jcast('long', 1)
        inv2 = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= n):
            fac = jcast('long', jcast('long', jmod(jcast('long', (fac * i)), Code04_SplitWays1.MOD)))
            if (i == k):
                # 费马小定理求逆元
                inv1 = jcast('long', Code04_SplitWays1.power(fac, jcast('int', (Code04_SplitWays1.MOD - 2))))
            if (i == jcast('int', (n - k))):
                # 费马小定理求逆元
                inv2 = jcast('long', Code04_SplitWays1.power(fac, jcast('int', (Code04_SplitWays1.MOD - 2))))
            i = jcast('int', (i + 1))
        return jcast('int', jcast('int', jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (fac * inv1)), Code04_SplitWays1.MOD)) * inv2)), Code04_SplitWays1.MOD))))

    # 乘法快速幂
    @staticmethod
    def power(x, p):
        x = jcast('long', x)
        p = jcast('long', p)
        ans = jcast('long', 1)
        while (p > 0):
            if (jcast('long', (p & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), Code04_SplitWays1.MOD)))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), Code04_SplitWays1.MOD)))
            p = jcast('long', jcast('long', (p >> (1 & 63))))
        return jcast('long', ans)

    # 为了测试
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        ans = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            jset(ans, i, jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * v)), 1)))
            i = jcast('int', (i + 1))
        return ans

    # 为了测试
    @staticmethod
    def main(args):
        jprint('功能测试开始', newline=True)
        N = jcast('int', 10)
        V = jcast('int', 20)
        test = jcast('int', 20000)
        i = jcast('int', 0)
        while (i < test):
            n = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * N)), 1)))
            arr = Code04_SplitWays1.randomArray(n, V)
            ans1 = jcast('int', Code04_SplitWays1.ways1(arr))
            ans2 = jcast('int', Code04_SplitWays1.ways2(arr))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('功能测试结束', newline=True)
        jprint('==========', newline=True)
        jprint('性能测试开始', newline=True)
        n = jcast('int', 10000000)
        v = jcast('int', 10000000)
        start = 0
        end = 0
        arr = jarray('int', [n])
        jprint('随机生成的数据测试', newline=True)
        jprint(jadd('数组长度 : ', n), newline=True)
        jprint(jadd(jadd(jadd(jadd('数值范围 : [', 1), ','), v), ']'), newline=True)
        i = jcast('int', 0)
        while (i < n):
            jset(arr, i, jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * v)), 1)))
            i = jcast('int', (i + 1))
        start = jcast('long', jstatic('System', 'currentTimeMillis'))
        Code04_SplitWays1.ways2(arr)
        end = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd(jadd('运行时间 : ', jcast('long', (end - start))), ' 毫秒'), newline=True)
        jprint(newline=True)
        jprint('运行最慢的数据测试', newline=True)
        jprint(jadd('数组长度 : ', n), newline=True)
        jprint(jadd('数值都是 : ', v), newline=True)
        jprint('这种情况其实是复杂度最高的情况', newline=True)
        i = jcast('int', 0)
        while (i < n):
            arr[i] = jcast('int', v)
            i = jcast('int', (i + 1))
        start = jcast('long', jstatic('System', 'currentTimeMillis'))
        Code04_SplitWays1.ways2(arr)
        end = jcast('long', jstatic('System', 'currentTimeMillis'))
        jprint(jadd(jadd('运行时间 : ', jcast('long', (end - start))), ' 毫秒'), newline=True)
        jprint('性能测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_SplitWays1.MOD = jcast('int', 1000000007)

if __name__ == '__main__':
    Code04_SplitWays1.main([])
