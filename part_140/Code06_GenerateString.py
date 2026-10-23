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

# 生成字符串
# 有n个1和m个0，要组成n+m长度的数列，保证任意前缀上，1的数量 >= 0的数量
# 返回有多少种排列方法，答案对 20100403 取模
# 1 <= m <= n <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P1641
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_GenerateString:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'fac': 'fac', 'inv': 'inv'}
    MOD = 0
    MAXN = 0
    fac = None
    inv = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        jset(Code06_GenerateString.fac, 0, jset(Code06_GenerateString.inv, 0, 1))
        Code06_GenerateString.fac[1] = jcast('long', 1)
        i = jcast('int', 2)
        while (i <= n):
            Code06_GenerateString.fac[i] = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', i) * Code06_GenerateString.fac[jcast('int', (i - 1))])), Code06_GenerateString.MOD)))
            i = jcast('int', (i + 1))
        jset(Code06_GenerateString.inv, n, Code06_GenerateString.power(Code06_GenerateString.fac[n], jcast('int', (Code06_GenerateString.MOD - 2))))
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 1):
            Code06_GenerateString.inv[i] = jcast('long', jcast('long', jmod(jcast('long', (jcast('long', jcast('int', jadd(i, 1))) * Code06_GenerateString.inv[jcast('int', jadd(i, 1))])), Code06_GenerateString.MOD)))
            i = jcast('int', (i - 1))

    @staticmethod
    def power(x, p):
        x = jcast('long', x)
        p = jcast('long', p)
        ans = jcast('long', 1)
        while (p > 0):
            if (jcast('long', (p & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), Code06_GenerateString.MOD)))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), Code06_GenerateString.MOD)))
            p = jcast('long', jcast('long', (p >> (1 & 63))))
        return jcast('long', ans)

    @staticmethod
    def c(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        return jcast('long', jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (Code06_GenerateString.fac[n] * Code06_GenerateString.inv[k])), Code06_GenerateString.MOD)) * Code06_GenerateString.inv[jcast('int', (n - k))])), Code06_GenerateString.MOD)))

    @staticmethod
    def compute(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        Code06_GenerateString.build(jcast('int', jadd(n, m)))
        return jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', (Code06_GenerateString.c(jcast('int', jadd(n, m)), m) - Code06_GenerateString.c(jcast('int', jadd(n, m)), jcast('int', (m - 1))))), Code06_GenerateString.MOD)), Code06_GenerateString.MOD)))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(out, 'println', Code06_GenerateString.compute(n, m))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_GenerateString.MOD = jcast('int', 20100403)
Code06_GenerateString.MAXN = jcast('int', 2000001)
Code06_GenerateString.fac = jarray('long', [Code06_GenerateString.MAXN])
Code06_GenerateString.inv = jarray('long', [Code06_GenerateString.MAXN])

if __name__ == '__main__':
    Code06_GenerateString.main([])
