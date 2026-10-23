# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 判断较大的数字是否是质数(Miller-Rabin测试)
# 测试链接 : https://www.luogu.com.cn/problem/U148828
# 此实现用于展示算法思路，性能需结合题目规模评估
# 本文件可以解决10^9范围内数字的质数检查
# 时间复杂度O(s * (logn)的三次方)，很快
# 为什么不能搞定所有long类型的数字检查
# 原因在于long类型位数不够，乘法同余的时候会溢出，课上已经做了说明
class Code02_LargeNumberIsPrime1:
    __java_fields__ = {'p': 'p'}
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        t = jcast('int', jstatic('Integer', 'valueOf', jcall(br, 'readLine')))
        i = jcast('int', 0)
        while (i < t):
            # 这里要注意
            # 如果读入long类型的数字，数字本身很大的话
            # 先读出字符串str，然后用Long.valueOf(str)
            n = jcast('long', jstatic('Long', 'valueOf', jcall(br, 'readLine')))
            jcall(out, 'println', ('Yes' if Code02_LargeNumberIsPrime1.millerRabin(n) else 'No'))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 质数的个数代表测试次数
    # 如果想增加测试次数就继续增加更大的质数
    p = None
    @staticmethod
    def millerRabin(n):
        n = jcast('long', n)
        if (n <= 2):
            return jcast('boolean', (n == 2))
        if (jcast('long', (n & 1)) == 0):
            return jcast('boolean', False)
        i = jcast('int', 0)
        while ((i < jget(Code02_LargeNumberIsPrime1.p, 'length')) and (Code02_LargeNumberIsPrime1.p[i] < n)):
            if Code02_LargeNumberIsPrime1.witness(Code02_LargeNumberIsPrime1.p[i], n):
                return jcast('boolean', False)
            i = jcast('int', (i + 1))
        return jcast('boolean', True)

    # 单次测试的函数，不用纠结原理
    # 返回n是不是合数
    @staticmethod
    def witness(a, n):
        a = jcast('long', a)
        n = jcast('long', n)
        u = jcast('long', jcast('long', (n - 1)))
        t = jcast('int', 0)
        while (jcast('long', (u & 1)) == 0):
            t = jcast('int', (t + 1))
            u = jcast('long', jcast('long', (u >> (1 & 63))))
        x1 = jcast('long', Code02_LargeNumberIsPrime1.power(a, u, n))
        x2 = 0
        i = jcast('int', 1)
        while (i <= t):
            x2 = jcast('long', Code02_LargeNumberIsPrime1.power(x1, 2, n))
            if (((x2 == 1) and (x1 != 1)) and (x1 != jcast('long', (n - 1)))):
                return jcast('boolean', True)
            x1 = jcast('long', x2)
            i = jcast('int', (i + 1))
        if (x1 != 1):
            return jcast('boolean', True)
        return jcast('boolean', False)

    # 返回 : n的p次方 % mod
    # 快速幂，讲解098会重点讲述，此时直接用即可
    @staticmethod
    def power(n, p, mod):
        n = jcast('long', n)
        p = jcast('long', p)
        mod = jcast('long', mod)
        ans = jcast('long', 1)
        while (p > 0):
            if (jcast('long', (p & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * n)), mod)))
            n = jcast('long', jcast('long', jmod(jcast('long', (n * n)), mod)))
            p = jcast('long', jcast('long', (p >> (1 & 63))))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_LargeNumberIsPrime1.p = jarray('long', [None], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])

if __name__ == '__main__':
    Code02_LargeNumberIsPrime1.main([])
