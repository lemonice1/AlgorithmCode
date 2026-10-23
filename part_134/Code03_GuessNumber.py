# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 猜数字
# 给定两个长度为n数组，一组为r1，r2，r3...，另一组为m1，m2，m3...
# 其中第二组数字两两互质，求最小正数解x
# 要求x满足，mi | (x - ri)，即(x - ri)是mi的整数倍
# 1 <= n <= 10
# -10^9 <= ri <= +10^9
# 1 <= mi <= 6 * 10^3
# 所有mi的乘积 <= 10^18
# 测试链接 : https://www.luogu.com.cn/problem/P3868
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_GuessNumber:
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
            lcm = jcast('long', jcast('long', (lcm * Code03_GuessNumber.m[i])))
            i = jcast('int', (i + 1))
        ai = 0
        ci = 0
        ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= n):
            ai = jcast('long', jcast('long', jdiv(lcm, Code03_GuessNumber.m[i])))
            Code03_GuessNumber.exgcd(ai, Code03_GuessNumber.m[i])
            ci = jcast('long', Code03_GuessNumber.multiply(Code03_GuessNumber.r[i], Code03_GuessNumber.multiply(ai, Code03_GuessNumber.x, lcm), lcm))
            ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, ci)), lcm)))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

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
        i = jcast('int', 1)
        while (i <= n):
            b = jcast('long', Code03_GuessNumber.m[i])
            c = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(jcast('long', (Code03_GuessNumber.r[i] - tail)), b)), b)), b)))
            Code03_GuessNumber.exgcd(lcm, b)
            if (jcast('long', jmod(c, Code03_GuessNumber.d)) != 0):
                return jcast('long', jcast('int', (-1)))
            x0 = jcast('long', Code03_GuessNumber.multiply(Code03_GuessNumber.x, jcast('long', jdiv(c, Code03_GuessNumber.d)), jcast('long', jdiv(b, Code03_GuessNumber.d))))
            tmp = jcast('long', jcast('long', (lcm * jcast('long', jdiv(b, Code03_GuessNumber.d)))))
            tail = jcast('long', jcast('long', jmod(jcast('long', jadd(tail, Code03_GuessNumber.multiply(x0, lcm, tmp))), tmp)))
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
            Code03_GuessNumber.d = jcast('long', a)
            Code03_GuessNumber.x = jcast('long', 1)
            Code03_GuessNumber.y = jcast('long', 0)
        else:
            Code03_GuessNumber.exgcd(b, jcast('long', jmod(a, b)))
            Code03_GuessNumber.px = jcast('long', Code03_GuessNumber.x)
            Code03_GuessNumber.py = jcast('long', Code03_GuessNumber.y)
            Code03_GuessNumber.x = jcast('long', Code03_GuessNumber.py)
            Code03_GuessNumber.y = jcast('long', jcast('long', (Code03_GuessNumber.px - jcast('long', (Code03_GuessNumber.py * jcast('long', jdiv(a, b)))))))

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
            Code03_GuessNumber.r[i] = jcast('long', jcast('long', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= n):
            jcall(in_, 'nextToken')
            Code03_GuessNumber.m[i] = jcast('long', jcast('long', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        # 题目输入的余数可能为负所以转化成非负数
        i = jcast('int', 1)
        while (i <= n):
            Code03_GuessNumber.r[i] = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(Code03_GuessNumber.r[i], Code03_GuessNumber.m[i])), Code03_GuessNumber.m[i])), Code03_GuessNumber.m[i])))
            i = jcast('int', (i + 1))
        # out.println(crt(n)); // 中国剩余定理解决
        # 扩展中国剩余定理解决
        jcall(out, 'println', Code03_GuessNumber.excrt(n))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_GuessNumber.MAXN = jcast('int', 11)
Code03_GuessNumber.m = jarray('long', [Code03_GuessNumber.MAXN])
Code03_GuessNumber.r = jarray('long', [Code03_GuessNumber.MAXN])
Code03_GuessNumber.d = jcast('long', 0)
Code03_GuessNumber.x = jcast('long', 0)
Code03_GuessNumber.y = jcast('long', 0)
Code03_GuessNumber.px = jcast('long', 0)
Code03_GuessNumber.py = jcast('long', 0)

if __name__ == '__main__':
    Code03_GuessNumber.main([])
