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

# 连续阶乘逆元的线性递推
# 实现组合公式C(n,m)的计算
# 最终结果 % 1000000007后返回
# 0 <= m <= n <= 1000
# 对数器验证
class Code03_InverseFactorial:
    __java_fields__ = {'MOD': 'MOD', 'LIMIT': 'LIMIT', 'fac': 'fac', 'inv': 'inv'}
    MOD = 0
    LIMIT = 0
    # 阶乘表
    # fac[i]代表 i! 在 %MOD 意义下的余数
    fac = None
    # 阶乘结果的逆元表
    # inv[i]代表i! 在 %MOD 意义下的逆元(1 / i!)
    inv = None
    @staticmethod
    def build():
        Code03_InverseFactorial.fac[1] = jcast('long', 1)
        i = jcast('int', 2)
        while (i <= Code03_InverseFactorial.LIMIT):
            Code03_InverseFactorial.fac[i] = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', i) * Code03_InverseFactorial.fac[jcast('int', (i - 1))])), Code03_InverseFactorial.MOD)))
            i = jcast('int', (i + 1))
        # 单个阶乘的逆元
        # inv[0] = 1;
        # for (int i = 1; i <= LIMIT; i++) {
        # inv[i] = power(fac[i], MOD - 2);
        # }
        # 利用线性递推优化
        jset(Code03_InverseFactorial.inv, Code03_InverseFactorial.LIMIT, Code03_InverseFactorial.power(Code03_InverseFactorial.fac[Code03_InverseFactorial.LIMIT], jcast('int', (Code03_InverseFactorial.MOD - 2))))
        i = jcast('int', jcast('int', (Code03_InverseFactorial.LIMIT - 1)))
        while (i >= 0):
            Code03_InverseFactorial.inv[i] = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', jcast('int', jadd(i, 1))) * Code03_InverseFactorial.inv[jcast('int', jadd(i, 1))])), Code03_InverseFactorial.MOD)))
            i = jcast('int', (i - 1))

    @staticmethod
    def power(x, n):
        x = jcast('long', x)
        n = jcast('int', n)
        ans = jcast('long', 1)
        while (n > 0):
            if (jcast('int', (n & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), Code03_InverseFactorial.MOD)))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), Code03_InverseFactorial.MOD)))
            n = jcast('int', jcast('int', (n >> (1 & 31))))
        return jcast('long', ans)

    # 组合公式
    # 得到的结果 % MOD
    # BigInteger保证中间计算结果完全正确
    @staticmethod
    def c1(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        a = jnew('BigInteger', '1')
        b = jnew('BigInteger', '1')
        c = jnew('BigInteger', '1')
        i = jcast('int', 1)
        while (i <= n):
            cur = jstatic('String', 'valueOf', i)
            a = jcall(a, 'multiply', jnew('BigInteger', cur))
            if (i <= m):
                b = jcall(b, 'multiply', jnew('BigInteger', cur))
            if (i <= jcast('int', (n - m))):
                c = jcall(c, 'multiply', jnew('BigInteger', cur))
            i = jcast('int', (i + 1))
        ans = jcall(jcall(a, 'divide', jcall(b, 'multiply', c)), 'mod', jnew('BigInteger', jstatic('String', 'valueOf', Code03_InverseFactorial.MOD)))
        return jcast('int', jcall(ans, 'intValue'))

    # 组合公式
    # 得到的结果 % MOD
    # 阶乘结果逆元表的线性递推
    @staticmethod
    def c2(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        ans = jcast('long', Code03_InverseFactorial.fac[n])
        ans = jcast('long', jcast('long', jmod(jcast('long', (ans * Code03_InverseFactorial.inv[m])), Code03_InverseFactorial.MOD)))
        ans = jcast('long', jcast('long', jmod(jcast('long', (ans * Code03_InverseFactorial.inv[jcast('int', (n - m))])), Code03_InverseFactorial.MOD)))
        return jcast('int', jcast('int', ans))

    @staticmethod
    def main(args):
        jprint('测试开始', newline=True)
        Code03_InverseFactorial.build()
        # 要保证 n <= LIMIT
        n = jcast('int', 500)
        m = jcast('int', 0)
        while (m <= n):
            ans1 = jcast('int', Code03_InverseFactorial.c1(n, m))
            ans2 = jcast('int', Code03_InverseFactorial.c2(n, m))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            m = jcast('int', (m + 1))
        jprint('测试结束', newline=True)
        # 要保证 b <= a <= LIMIT
        a = jcast('int', 537)
        b = jcast('int', 367)
        jprint(jadd(jadd(jadd(jadd(jadd('计算 C ( ', a), ' , '), b), ' ) % '), Code03_InverseFactorial.MOD), newline=True)
        jprint(jadd('方法1答案 : ', Code03_InverseFactorial.c1(a, b)), newline=True)
        jprint(jadd('方法2答案 : ', Code03_InverseFactorial.c2(a, b)), newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_InverseFactorial.MOD = jcast('int', 1000000007)
Code03_InverseFactorial.LIMIT = jcast('int', 1000)
Code03_InverseFactorial.fac = jarray('long', [jcast('int', jadd(Code03_InverseFactorial.LIMIT, 1))])
Code03_InverseFactorial.inv = jarray('long', [jcast('int', jadd(Code03_InverseFactorial.LIMIT, 1))])

if __name__ == '__main__':
    Code03_InverseFactorial.main([])
