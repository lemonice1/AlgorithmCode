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

# Miller-Rabin 测试，Python 版本，不依赖 BigInteger 接口的实现
# 兼容层中的 long 按有符号 64 位整数处理；Python int 本身支持任意精度
# 两个 64 位整数相乘的中间结果最多需要 128 位；精确乘法可使用 Python int
# 但是
# 如果a和b都是long类型，其实 a * b 的过程，用位运算去实现，中间结果都 % mod 即可
# 这样就不需要使用BigInteger
# 讲解033，位运算实现乘法，增加 每一步 % mod 的逻辑即可
# 重点看一下本文件中的 multiply 方法，就是位运算实现乘法的改写
# Python int 支持任意精度，无需额外定义 128 位整数类型
# 测试链接 : https://www.luogu.com.cn/problem/U148828
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_LargeNumberIsPrime4:
    __java_fields__ = {'p': 'p'}
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        t = jcast('int', jstatic('Integer', 'valueOf', jcall(br, 'readLine')))
        i = jcast('int', 0)
        while (i < t):
            n = jcast('long', jstatic('Long', 'valueOf', jcall(br, 'readLine')))
            jcall(out, 'println', ('Yes' if Code02_LargeNumberIsPrime4.millerRabin(n) else 'No'))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    p = None
    @staticmethod
    def millerRabin(n):
        n = jcast('long', n)
        if (n <= 2):
            return jcast('boolean', (n == 2))
        if (jcast('long', (n & 1)) == 0):
            return jcast('boolean', False)
        i = jcast('int', 0)
        while ((i < jget(Code02_LargeNumberIsPrime4.p, 'length')) and (Code02_LargeNumberIsPrime4.p[i] < n)):
            if Code02_LargeNumberIsPrime4.witness(Code02_LargeNumberIsPrime4.p[i], n):
                return jcast('boolean', False)
            i = jcast('int', (i + 1))
        return jcast('boolean', True)

    @staticmethod
    def witness(a, n):
        a = jcast('long', a)
        n = jcast('long', n)
        u = jcast('long', jcast('long', (n - 1)))
        t = jcast('int', 0)
        while (jcast('long', (u & 1)) == 0):
            t = jcast('int', (t + 1))
            u = jcast('long', jcast('long', (u >> (1 & 63))))
        x1 = jcast('long', Code02_LargeNumberIsPrime4.power(a, u, n))
        x2 = 0
        i = jcast('int', 1)
        while (i <= t):
            x2 = jcast('long', Code02_LargeNumberIsPrime4.power(x1, 2, n))
            if (((x2 == 1) and (x1 != 1)) and (x1 != jcast('long', (n - 1)))):
                return jcast('boolean', True)
            x1 = jcast('long', x2)
            i = jcast('int', (i + 1))
        if (x1 != 1):
            return jcast('boolean', True)
        return jcast('boolean', False)

    # 返回，n的p次方 % mod
    # 乘的每一步都用multiply方法，不用语言自带的乘法
    @staticmethod
    def power(n, p, mod):
        n = jcast('long', n)
        p = jcast('long', p)
        mod = jcast('long', mod)
        ans = jcast('long', 1)
        while (p > 0):
            if (jcast('long', (p & 1)) == 1):
                ans = jcast('long', Code02_LargeNumberIsPrime4.multiply(ans, n, mod))
            n = jcast('long', Code02_LargeNumberIsPrime4.multiply(n, n, mod))
            p = jcast('long', jcast('long', (p >> (1 & 63))))
        return jcast('long', ans)

    # a * b的过程，用位运算实现，让每一个中间结果都 % mod
    # 这个原理来自，讲解033，位运算实现乘法
    # 这么写可以防止溢出，这也叫龟速乘
    @staticmethod
    def multiply(a, b, mod):
        a = jcast('long', a)
        b = jcast('long', b)
        mod = jcast('long', mod)
        a = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(a, mod)), mod)), mod)))
        b = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(b, mod)), mod)), mod)))
        ans = jcast('long', 0)
        while (b != 0):
            if (jcast('long', (b & 1)) != 0):
                ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, a)), mod)))
            a = jcast('long', jcast('long', jmod(jcast('long', jadd(a, a)), mod)))
            b = jcast('long', jcast('long', (b >> (1 & 63))))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_LargeNumberIsPrime4.p = jarray('long', [None], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])

if __name__ == '__main__':
    Code02_LargeNumberIsPrime4.main([])
