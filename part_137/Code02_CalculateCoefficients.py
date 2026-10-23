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

# 计算系数
# 多项式为，(ax + by)的k次方，其中a、b、k为常数
# 计算这个多项式展开后，x的n次方 * y的m次方，这一项的系数
# 0 <= k <= 1000
# 0 <= a、b <= 10^6
# n + m == k
# 测试链接 : https://www.luogu.com.cn/problem/P1313
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_CalculateCoefficients:
    __java_fields__ = {'MAXK': 'MAXK', 'MOD': 'MOD', 'fac': 'fac', 'inv': 'inv', 'a': 'a', 'b': 'b', 'k': 'k', 'n': 'n', 'm': 'm'}
    MAXK = 0
    MOD = 0
    # fac[i]代表 i! 在 %MOD 意义下的余数
    fac = None
    # inv[i]代表 i! 在 %MOD 意义下的逆元
    inv = None
    a = 0
    b = 0
    k = 0
    n = 0
    m = 0
    # 来自讲解098，乘法快速幂，x的p次方 % MOD
    @staticmethod
    def power(x, p):
        x = jcast('long', x)
        p = jcast('int', p)
        ans = jcast('long', 1)
        while (p > 0):
            if (jcast('int', (p & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), Code02_CalculateCoefficients.MOD)))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), Code02_CalculateCoefficients.MOD)))
            p = jcast('int', jcast('int', (p >> (1 & 31))))
        return jcast('long', ans)

    # 来自讲解099，生成阶乘表和逆元表
    @staticmethod
    def build():
        # 阶乘表线性递推
        Code02_CalculateCoefficients.fac[1] = jcast('long', 1)
        i = jcast('int', 2)
        while (i <= Code02_CalculateCoefficients.MAXK):
            Code02_CalculateCoefficients.fac[i] = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', i) * Code02_CalculateCoefficients.fac[jcast('int', (i - 1))])), Code02_CalculateCoefficients.MOD)))
            i = jcast('int', (i + 1))
        # 逆元表线性递推
        jset(Code02_CalculateCoefficients.inv, Code02_CalculateCoefficients.MAXK, Code02_CalculateCoefficients.power(Code02_CalculateCoefficients.fac[Code02_CalculateCoefficients.MAXK], jcast('int', (Code02_CalculateCoefficients.MOD - 2))))
        i = jcast('int', jcast('int', (Code02_CalculateCoefficients.MAXK - 1)))
        while (i >= 0):
            Code02_CalculateCoefficients.inv[i] = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', jcast('int', jadd(i, 1))) * Code02_CalculateCoefficients.inv[jcast('int', jadd(i, 1))])), Code02_CalculateCoefficients.MOD)))
            i = jcast('int', (i - 1))

    # 组合公式
    @staticmethod
    def c(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        return jcast('long', jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (Code02_CalculateCoefficients.fac[n] * Code02_CalculateCoefficients.inv[k])), Code02_CalculateCoefficients.MOD)) * Code02_CalculateCoefficients.inv[jcast('int', (n - k))])), Code02_CalculateCoefficients.MOD)))

    @staticmethod
    def compute():
        Code02_CalculateCoefficients.build()
        return jcast('long', jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (Code02_CalculateCoefficients.power(Code02_CalculateCoefficients.a, Code02_CalculateCoefficients.n) * Code02_CalculateCoefficients.power(Code02_CalculateCoefficients.b, Code02_CalculateCoefficients.m))), Code02_CalculateCoefficients.MOD)) * Code02_CalculateCoefficients.c(Code02_CalculateCoefficients.k, jcast('int', (Code02_CalculateCoefficients.k - Code02_CalculateCoefficients.n))))), Code02_CalculateCoefficients.MOD)))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_CalculateCoefficients.a = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_CalculateCoefficients.b = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_CalculateCoefficients.k = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_CalculateCoefficients.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_CalculateCoefficients.m = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(out, 'println', Code02_CalculateCoefficients.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_CalculateCoefficients.MAXK = jcast('int', 1001)
Code02_CalculateCoefficients.MOD = jcast('int', 10007)
Code02_CalculateCoefficients.fac = jarray('long', [jcast('int', jadd(Code02_CalculateCoefficients.MAXK, 1))])
Code02_CalculateCoefficients.inv = jarray('long', [jcast('int', jadd(Code02_CalculateCoefficients.MAXK, 1))])
Code02_CalculateCoefficients.a = jcast('int', 0)
Code02_CalculateCoefficients.b = jcast('int', 0)
Code02_CalculateCoefficients.k = jcast('int', 0)
Code02_CalculateCoefficients.n = jcast('int', 0)
Code02_CalculateCoefficients.m = jcast('int', 0)

if __name__ == '__main__':
    Code02_CalculateCoefficients.main([])
