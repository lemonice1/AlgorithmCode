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

# 墨墨的等式(不排序+两次转圈法)
# 本版本去掉排序步骤，其余算法逻辑保持不变
# 一共有n种正数，每种数可以选择任意个，个数不能是负数
# 那么一定有某些数值可以由这些数字累加得到
# 请问在[l...r]范围上，有多少个数能被累加得到
# 0 <= n <= 12
# 0 <= 数值范围 <= 5 * 10^5
# 1 <= l <= r <= 10^12
# 测试链接 : https://www.luogu.com.cn/problem/P2371
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_MomoEquation3:
    __java_fields__ = {'MAXN': 'MAXN', 'inf': 'inf', 'v': 'v', 'dist': 'dist', 'n': 'n', 'size': 'size', 'x': 'x', 'l': 'l', 'r': 'r'}
    MAXN = 0
    inf = 0
    v = None
    dist = None
    n = 0
    size = 0
    x = 0
    l = 0
    r = 0
    @staticmethod
    def gcd(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        return jcast('int', (a if (b == 0) else Code04_MomoEquation3.gcd(b, jcast('int', jmod(a, b)))))

    @staticmethod
    def compute():
        Code04_MomoEquation3.x = jcast('int', Code04_MomoEquation3.v[1])
        jstatic('Arrays', 'fill', Code04_MomoEquation3.dist, 0, Code04_MomoEquation3.x, Code04_MomoEquation3.inf)
        Code04_MomoEquation3.dist[0] = jcast('long', 0)
        i = jcast('int', 2)
        d = 0
        while (i <= Code04_MomoEquation3.size):
            d = jcast('int', Code04_MomoEquation3.gcd(Code04_MomoEquation3.v[i], Code04_MomoEquation3.x))
            j = jcast('int', 0)
            while (j < d):
                cur = jcast('int', j)
                next = 0
                circle = jcast('int', 0)
                while (circle < 2):
                    next = jcast('int', jcast('int', jmod(jcast('int', jadd(cur, Code04_MomoEquation3.v[i])), Code04_MomoEquation3.x)))
                    if (Code04_MomoEquation3.dist[cur] != Code04_MomoEquation3.inf):
                        jset(Code04_MomoEquation3.dist, next, jstatic('Math', 'min', Code04_MomoEquation3.dist[next], jcast('long', jadd(Code04_MomoEquation3.dist[cur], Code04_MomoEquation3.v[i]))))
                    cur = jcast('int', next)
                    circle = jcast('int', jcast('int', jadd(circle, (1 if (cur == j) else 0))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        ans = jcast('long', 0)
        i = jcast('int', 0)
        while (i < Code04_MomoEquation3.x):
            if (Code04_MomoEquation3.r >= Code04_MomoEquation3.dist[i]):
                ans = jcast('long', jcast('long', jadd(ans, jstatic('Math', 'max', 0, jcast('long', jadd(jcast('long', jdiv(jcast('long', (Code04_MomoEquation3.r - Code04_MomoEquation3.dist[i])), Code04_MomoEquation3.x)), 1))))))
            if (Code04_MomoEquation3.l >= Code04_MomoEquation3.dist[i]):
                ans = jcast('long', jcast('long', (ans - jstatic('Math', 'max', 0, jcast('long', jadd(jcast('long', jdiv(jcast('long', (Code04_MomoEquation3.l - Code04_MomoEquation3.dist[i])), Code04_MomoEquation3.x)), 1))))))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_MomoEquation3.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code04_MomoEquation3.size = jcast('int', 0)
        jcall(in_, 'nextToken')
        Code04_MomoEquation3.l = jcast('long', jcast('long', (jcast('long', jget(in_, 'nval')) - 1)))
        jcall(in_, 'nextToken')
        Code04_MomoEquation3.r = jcast('long', jcast('long', jget(in_, 'nval')))
        i = jcast('int', 1)
        num = 0
        while (i <= Code04_MomoEquation3.n):
            jcall(in_, 'nextToken')
            num = jcast('int', jcast('int', jget(in_, 'nval')))
            if (num != 0):
                jset(Code04_MomoEquation3.v, ((_java_obj_1 := Code04_MomoEquation3), (_java_key_2 := 'size'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code04_MomoEquation3.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_MomoEquation3.MAXN = jcast('int', 500001)
Code04_MomoEquation3.inf = jcast('long', jget(Long, 'MAX_VALUE'))
Code04_MomoEquation3.v = jarray('int', [Code04_MomoEquation3.MAXN])
Code04_MomoEquation3.dist = jarray('long', [Code04_MomoEquation3.MAXN])
Code04_MomoEquation3.n = jcast('int', 0)
Code04_MomoEquation3.size = jcast('int', 0)
Code04_MomoEquation3.x = jcast('int', 0)
Code04_MomoEquation3.l = jcast('long', 0)
Code04_MomoEquation3.r = jcast('long', 0)

if __name__ == '__main__':
    Code04_MomoEquation3.main([])
