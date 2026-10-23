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

# 卡特兰数模版
# 进栈顺序规定为1、2、3..n，返回有多少种不同的出栈顺序
# 测试题目的数据量很小，得到的卡特兰数没有多大，不需要取模处理
# 但是请假设，当n比较大时，卡特兰数是很大的，答案对 1000000007 取模
# 测试链接 : https://www.luogu.com.cn/problem/P1044
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_Catalan:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'fac': 'fac', 'inv1': 'inv1', 'inv2': 'inv2'}
    MOD = 0
    MAXN = 0
    # 阶乘余数表
    fac = None
    # 阶乘逆元表
    inv1 = None
    # 连续数逆元表
    inv2 = None
    # 来自讲解099，题目3，生成阶乘余数表、阶乘逆元表
    @staticmethod
    def build1(n):
        n = jcast('int', n)
        jset(Code01_Catalan.fac, 0, jset(Code01_Catalan.inv1, 0, 1))
        Code01_Catalan.fac[1] = jcast('long', 1)
        i = jcast('int', 2)
        while (i <= n):
            Code01_Catalan.fac[i] = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', i) * Code01_Catalan.fac[jcast('int', (i - 1))])), Code01_Catalan.MOD)))
            i = jcast('int', (i + 1))
        jset(Code01_Catalan.inv1, n, Code01_Catalan.power(Code01_Catalan.fac[n], jcast('int', (Code01_Catalan.MOD - 2))))
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 1):
            Code01_Catalan.inv1[i] = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', jcast('int', jadd(i, 1))) * Code01_Catalan.inv1[jcast('int', jadd(i, 1))])), Code01_Catalan.MOD)))
            i = jcast('int', (i - 1))

    # 来自讲解099，题目2，生成连续数逆元表
    @staticmethod
    def build2(n):
        n = jcast('int', n)
        Code01_Catalan.inv2[1] = jcast('long', 1)
        i = jcast('int', 2)
        while (i <= jcast('int', jadd(n, 1))):
            Code01_Catalan.inv2[i] = jcast('long', jcast('long', (Code01_Catalan.MOD - jcast('long', jmod(jcast('long', (Code01_Catalan.inv2[jcast('int', jmod(Code01_Catalan.MOD, i))] * jcast('int', jdiv(Code01_Catalan.MOD, i)))), Code01_Catalan.MOD)))))
            i = jcast('int', (i + 1))

    @staticmethod
    def power(x, p):
        x = jcast('long', x)
        p = jcast('long', p)
        ans = jcast('long', 1)
        while (p > 0):
            if (jcast('long', (p & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), Code01_Catalan.MOD)))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), Code01_Catalan.MOD)))
            p = jcast('long', jcast('long', (p >> (1 & 63))))
        return jcast('long', ans)

    @staticmethod
    def c(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        return jcast('long', jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (Code01_Catalan.fac[n] * Code01_Catalan.inv1[k])), Code01_Catalan.MOD)) * Code01_Catalan.inv1[jcast('int', (n - k))])), Code01_Catalan.MOD)))

    # 公式1
    @staticmethod
    def compute1(n):
        n = jcast('int', n)
        Code01_Catalan.build1(jcast('int', (2 * n)))
        return jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', (Code01_Catalan.c(jcast('int', (2 * n)), n) - Code01_Catalan.c(jcast('int', (2 * n)), jcast('int', (n - 1))))), Code01_Catalan.MOD)), Code01_Catalan.MOD)))

    # 公式2
    @staticmethod
    def compute2(n):
        n = jcast('int', n)
        Code01_Catalan.build1(jcast('int', (2 * n)))
        return jcast('long', jcast('long', jmod(jcast('long', (Code01_Catalan.c(jcast('int', (2 * n)), n) * Code01_Catalan.power(jcast('int', jadd(n, 1)), jcast('int', (Code01_Catalan.MOD - 2))))), Code01_Catalan.MOD)))

    # 公式3
    @staticmethod
    def compute3(n):
        n = jcast('int', n)
        Code01_Catalan.build2(n)
        f = jarray('long', [jcast('int', jadd(n, 1))])
        jset(f, 0, jset(f, 1, 1))
        i = jcast('int', 2)
        while (i <= n):
            f[i] = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (f[jcast('int', (i - 1))] * jcast('int', (jcast('int', (4 * i)) - 2)))), Code01_Catalan.MOD)) * Code01_Catalan.inv2[jcast('int', jadd(i, 1))])), Code01_Catalan.MOD)))
            i = jcast('int', (i + 1))
        return jcast('long', f[n])

    # 公式4
    @staticmethod
    def compute4(n):
        n = jcast('int', n)
        f = jarray('long', [jcast('int', jadd(n, 1))])
        jset(f, 0, jset(f, 1, 1))
        i = jcast('int', 2)
        while (i <= n):
            l = jcast('int', 0)
            r = jcast('int', jcast('int', (i - 1)))
            while (l < i):
                f[i] = jcast('long', jcast('long', jmod(jcast('long', jadd(f[i], jcast('long', jmod(jcast('long', (f[l] * f[r])), Code01_Catalan.MOD)))), Code01_Catalan.MOD)))
                l = jcast('int', (l + 1))
                r = jcast('int', (r - 1))
            i = jcast('int', (i + 1))
        return jcast('long', f[n])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(out, 'println', Code01_Catalan.compute1(n))
        # out.println(compute2(n));
        # out.println(compute3(n));
        # out.println(compute4(n));
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_Catalan.MOD = jcast('int', 1000000007)
Code01_Catalan.MAXN = jcast('int', 1000001)
Code01_Catalan.fac = jarray('long', [Code01_Catalan.MAXN])
Code01_Catalan.inv1 = jarray('long', [Code01_Catalan.MAXN])
Code01_Catalan.inv2 = jarray('long', [Code01_Catalan.MAXN])

if __name__ == '__main__':
    Code01_Catalan.main([])
