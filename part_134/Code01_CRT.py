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

# 中国剩余定理模版
# 给出n个同余方程，求满足同余方程的最小正数解x
# 一共n个同余方程，x ≡ ri(% mi)
# 1 <= n <= 10
# 0 <= ri、mi <= 10^5
# 所有mi一定互质
# 所有mi整体乘积 <= 10^18
# 测试链接 : https://www.luogu.com.cn/problem/P1495
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_CRT:
    __java_fields__ = {'MAXN': 'MAXN', 'm': 'm', 'r': 'r', 'd': 'd', 'x': 'x', 'y': 'y', 'px': 'px', 'py': 'py'}
    MAXN = 0
    m = None
    r = None
    # 中国剩余定理模版
    @staticmethod
    def crt(n):
        n = jcast('int', n)
        lcm = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= n):
            lcm = jcast('long', jcast('long', (lcm * Code01_CRT.m[i])))
            i = jcast('int', (i + 1))
        ai = 0
        ci = 0
        ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= n):
            # ai = lcm / m[i]
            ai = jcast('long', jcast('long', jdiv(lcm, Code01_CRT.m[i])))
            # ai逆元，在%m[i]意义下的逆元
            Code01_CRT.exgcd(ai, Code01_CRT.m[i])
            # ci = (ri * ai * ai逆元) % lcm
            ci = jcast('long', Code01_CRT.multiply(Code01_CRT.r[i], Code01_CRT.multiply(ai, Code01_CRT.x, lcm), lcm))
            ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, ci)), lcm)))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    # 讲解139 - 扩展欧几里得算法
    d = 0
    x = 0
    y = 0
    px = 0
    py = 0
    @staticmethod
    def exgcd(a, b):
        a = jcast('long', a)
        b = jcast('long', b)
        if (b == 0):
            Code01_CRT.d = jcast('long', a)
            Code01_CRT.x = jcast('long', 1)
            Code01_CRT.y = jcast('long', 0)
        else:
            Code01_CRT.exgcd(b, jcast('long', jmod(a, b)))
            Code01_CRT.px = jcast('long', Code01_CRT.x)
            Code01_CRT.py = jcast('long', Code01_CRT.y)
            Code01_CRT.x = jcast('long', Code01_CRT.py)
            Code01_CRT.y = jcast('long', jcast('long', (Code01_CRT.px - jcast('long', (Code01_CRT.py * jcast('long', jdiv(a, b)))))))

    # 讲解033 - 位运算实现乘法
    # a*b过程每一步都%mod，这么写是防止溢出，也叫龟速乘
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

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= n):
            jcall(in_, 'nextToken')
            Code01_CRT.m[i] = jcast('long', jcast('long', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code01_CRT.r[i] = jcast('long', jcast('long', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code01_CRT.crt(n))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_CRT.MAXN = jcast('int', 11)
Code01_CRT.m = jarray('long', [Code01_CRT.MAXN])
Code01_CRT.r = jarray('long', [Code01_CRT.MAXN])
Code01_CRT.d = jcast('long', 0)
Code01_CRT.x = jcast('long', 0)
Code01_CRT.y = jcast('long', 0)
Code01_CRT.px = jcast('long', 0)
Code01_CRT.py = jcast('long', 0)

if __name__ == '__main__':
    Code01_CRT.main([])
