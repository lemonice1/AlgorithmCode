# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 墨墨的等式(两次转圈法)
# 一共有n种正数，每种数可以选择任意个，个数不能是负数
# 那么一定有某些数值可以由这些数字累加得到
# 请问在[l...r]范围上，有多少个数能被累加得到
# 0 <= n <= 12
# 0 <= 数值范围 <= 5 * 10^5
# 1 <= l <= r <= 10^12
# 测试链接 : https://www.luogu.com.cn/problem/P2371
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_MomoEquation2:
    __java_fields__ = {'MAXN': 'MAXN', 'inf': 'inf', 'v': 'v', 'dist': 'dist', 'n': 'n', 'x': 'x', 'l': 'l', 'r': 'r'}
    MAXN = 0
    inf = 0
    v = None
    dist = None
    n = 0
    x = 0
    l = 0
    r = 0
    @staticmethod
    def gcd(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        return jcast('int', (a if (b == 0) else Code04_MomoEquation2.gcd(b, jcast('int', jmod(a, b)))))

    @staticmethod
    def compute():
        jstatic('Arrays', 'sort', Code04_MomoEquation2.v, 1, jcast('int', jadd(Code04_MomoEquation2.n, 1)))
        size = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_MomoEquation2.n):
            if (Code04_MomoEquation2.v[i] != 0):
                jset(Code04_MomoEquation2.v, (size := jcast('int', (size + (1)))), Code04_MomoEquation2.v[i])
            i = jcast('int', (i + 1))
        if (size == 0):
            return jcast('long', 0)
        Code04_MomoEquation2.x = jcast('int', Code04_MomoEquation2.v[1])
        jstatic('Arrays', 'fill', Code04_MomoEquation2.dist, 0, Code04_MomoEquation2.x, Code04_MomoEquation2.inf)
        Code04_MomoEquation2.dist[0] = jcast('long', 0)
        # 出现基准数之外的其他数，更新最短路
        i = jcast('int', 2)
        d = 0
        while (i <= size):
            # 求最大公约数
            d = jcast('int', Code04_MomoEquation2.gcd(Code04_MomoEquation2.v[i], Code04_MomoEquation2.x))
            # j是每个子环的起点
            j = jcast('int', 0)
            while (j < d):
                cur = jcast('int', j)
                next = 0
                circle = jcast('int', 0)
                while (circle < 2):
                    next = jcast('int', jcast('int', jmod(jcast('int', jadd(cur, Code04_MomoEquation2.v[i])), Code04_MomoEquation2.x)))
                    if (Code04_MomoEquation2.dist[cur] != Code04_MomoEquation2.inf):
                        jset(Code04_MomoEquation2.dist, next, jstatic('Math', 'min', Code04_MomoEquation2.dist[next], jcast('long', jadd(Code04_MomoEquation2.dist[cur], Code04_MomoEquation2.v[i]))))
                    cur = jcast('int', next)
                    circle = jcast('int', jcast('int', jadd(circle, (1 if (cur == j) else 0))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        ans = jcast('long', 0)
        i = jcast('int', 0)
        while (i < Code04_MomoEquation2.x):
            if (Code04_MomoEquation2.r >= Code04_MomoEquation2.dist[i]):
                ans = jcast('long', jcast('long', jadd(ans, jstatic('Math', 'max', 0, jcast('long', jadd(jcast('long', jdiv(jcast('long', (Code04_MomoEquation2.r - Code04_MomoEquation2.dist[i])), Code04_MomoEquation2.x)), 1))))))
            if (Code04_MomoEquation2.l >= Code04_MomoEquation2.dist[i]):
                ans = jcast('long', jcast('long', (ans - jstatic('Math', 'max', 0, jcast('long', jadd(jcast('long', jdiv(jcast('long', (Code04_MomoEquation2.l - Code04_MomoEquation2.dist[i])), Code04_MomoEquation2.x)), 1))))))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_MomoEquation2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_MomoEquation2.l = jcast('long', jcast('long', (jcast('long', jget(in_, 'nval')) - 1)))
        jcall(in_, 'nextToken')
        Code04_MomoEquation2.r = jcast('long', jcast('long', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code04_MomoEquation2.n):
            jcall(in_, 'nextToken')
            Code04_MomoEquation2.v[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code04_MomoEquation2.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_MomoEquation2.MAXN = jcast('int', 500001)
Code04_MomoEquation2.inf = jcast('long', jget(Long, 'MAX_VALUE'))
Code04_MomoEquation2.v = jarray('int', [Code04_MomoEquation2.MAXN])
Code04_MomoEquation2.dist = jarray('long', [Code04_MomoEquation2.MAXN])
Code04_MomoEquation2.n = jcast('int', 0)
Code04_MomoEquation2.x = jcast('int', 0)
Code04_MomoEquation2.l = jcast('long', 0)
Code04_MomoEquation2.r = jcast('long', 0)

if __name__ == '__main__':
    Code04_MomoEquation2.main([])
