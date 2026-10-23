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

# 扩展中国剩余定理模版
# 给出n个同余方程，求满足同余方程的最小正数解x
# 一共n个同余方程，x ≡ ri(% mi)
# 1 <= n <= 10^5
# 0 <= ri、mi <= 10^12
# 所有mi不一定互质
# 所有mi的最小公倍数 <= 10^18
# 测试链接 : https://www.luogu.com.cn/problem/P4777
# 测试链接 : https://www.luogu.com.cn/problem/P1495
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_EXCRT:
    __java_fields__ = {'MAXN': 'MAXN', 'm': 'm', 'r': 'r', 'd': 'd', 'x': 'x', 'y': 'y', 'px': 'px', 'py': 'py'}
    MAXN = 0
    m = None
    r = None
    # 扩展中国剩余定理模版
    @staticmethod
    def excrt(n):
        n = jcast('int', n)
        tail = jcast('long', 0)
        lcm = jcast('long', 1)
        tmp = 0
        b = 0
        c = 0
        x0 = 0
        # ans = lcm * x + tail
        i = jcast('int', 1)
        while (i <= n):
            # ans = m[i] * y + ri
            # lcm * x + m[i] * y = ri - tail
            # a = lcm
            # b = m[i]
            # c = ri - tail
            b = jcast('long', Code02_EXCRT.m[i])
            c = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(jcast('long', (Code02_EXCRT.r[i] - tail)), b)), b)), b)))
            Code02_EXCRT.exgcd(lcm, b)
            if (jcast('long', jmod(c, Code02_EXCRT.d)) != 0):
                return jcast('long', jcast('int', (-1)))
            # ax + by = gcd(a,b)，特解是，x变量
            # ax + by = c，特解是，x变量 * (c/d)
            # ax + by = c，最小非负特解x0 = (x * (c/d)) % (b/d) 取非负余数
            # 通解 = x0 + (b/d) * n
            x0 = jcast('long', Code02_EXCRT.multiply(Code02_EXCRT.x, jcast('long', jdiv(c, Code02_EXCRT.d)), jcast('long', jdiv(b, Code02_EXCRT.d))))
            # ans = lcm * x + tail，带入通解
            # ans = lcm * (x0 + (b/d) * n) + tail
            # ans = lcm * (b/d) * n + lcm * x0 + tail
            # tail' = tail' % lcm'
            tmp = jcast('long', jcast('long', (lcm * jcast('long', jdiv(b, Code02_EXCRT.d)))))
            tail = jcast('long', jcast('long', jmod(jcast('long', jadd(tail, Code02_EXCRT.multiply(x0, lcm, tmp))), tmp)))
            lcm = jcast('long', tmp)
            i = jcast('int', (i + 1))
        return jcast('long', tail)

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
            Code02_EXCRT.d = jcast('long', a)
            Code02_EXCRT.x = jcast('long', 1)
            Code02_EXCRT.y = jcast('long', 0)
        else:
            Code02_EXCRT.exgcd(b, jcast('long', jmod(a, b)))
            Code02_EXCRT.px = jcast('long', Code02_EXCRT.x)
            Code02_EXCRT.py = jcast('long', Code02_EXCRT.y)
            Code02_EXCRT.x = jcast('long', Code02_EXCRT.py)
            Code02_EXCRT.y = jcast('long', jcast('long', (Code02_EXCRT.px - jcast('long', (Code02_EXCRT.py * jcast('long', jdiv(a, b)))))))

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
            Code02_EXCRT.m[i] = jcast('long', jcast('long', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code02_EXCRT.r[i] = jcast('long', jcast('long', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code02_EXCRT.excrt(n))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_EXCRT.MAXN = jcast('int', 100001)
Code02_EXCRT.m = jarray('long', [Code02_EXCRT.MAXN])
Code02_EXCRT.r = jarray('long', [Code02_EXCRT.MAXN])
Code02_EXCRT.d = jcast('long', 0)
Code02_EXCRT.x = jcast('long', 0)
Code02_EXCRT.y = jcast('long', 0)
Code02_EXCRT.px = jcast('long', 0)
Code02_EXCRT.py = jcast('long', 0)

if __name__ == '__main__':
    Code02_EXCRT.main([])
