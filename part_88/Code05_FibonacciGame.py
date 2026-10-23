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

# 斐波那契博弈(Fibonacci Game + Zeckendorf定理)
# 一共有n枚石子，两位玩家定了如下规则进行游戏：
# 先手后手轮流取石子，先手在第一轮可以取走任意的石子
# 接下来的每一轮当前的玩家最少要取走一个石子，最多取走上一次取的数量的2倍
# 当然，玩家取走的数量必须不大于目前场上剩余的石子数量，双方都以最优策略取石子
# 你也看出来了，根据规律先手一定会获胜，但是先手想知道
# 第一轮自己取走至少几颗石子就可以保证获胜了
# 测试链接 : https://www.luogu.com.cn/problem/P6487
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_FibonacciGame:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'f': 'f', 'size': 'size'}
    MAXN = 0
    MAXM = 0
    f = None
    size = 0
    @staticmethod
    def build():
        Code05_FibonacciGame.f[0] = jcast('long', 1)
        Code05_FibonacciGame.f[1] = jcast('long', 2)
        Code05_FibonacciGame.size = jcast('int', 1)
        while (Code05_FibonacciGame.f[Code05_FibonacciGame.size] <= Code05_FibonacciGame.MAXN):
            Code05_FibonacciGame.f[jcast('int', jadd(Code05_FibonacciGame.size, 1))] = jcast('long', jcast('long', jadd(Code05_FibonacciGame.f[Code05_FibonacciGame.size], Code05_FibonacciGame.f[jcast('int', (Code05_FibonacciGame.size - 1))])))
            Code05_FibonacciGame.size = jcast('int', (Code05_FibonacciGame.size + 1))

    @staticmethod
    def main(args):
        Code05_FibonacciGame.build()
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            jcall(out, 'println', Code05_FibonacciGame.compute(jcast('long', jget(in_, 'nval'))))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute(n):
        n = jcast('long', n)
        ans = jcast('long', jcast('int', (-1)))
        find = 0
        while ((n != 1) and (n != 2)):
            try:
                find = jcast('long', Code05_FibonacciGame.bs(n))
                if (n == find):
                    ans = jcast('long', find)
                    raise JBreak(None)
                else:
                    n = jcast('long', jcast('long', (n - find)))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        if (ans != jcast('int', (-1))):
            return jcast('long', ans)
        else:
            return jcast('long', n)

    @staticmethod
    def bs(n):
        n = jcast('long', n)
        l = jcast('int', 0)
        r = jcast('int', Code05_FibonacciGame.size)
        m = 0
        ans = jcast('long', jcast('int', (-1)))
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code05_FibonacciGame.f[m] <= n):
                ans = jcast('long', Code05_FibonacciGame.f[m])
                l = jcast('int', jcast('int', jadd(m, 1)))
            else:
                r = jcast('int', jcast('int', (m - 1)))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_FibonacciGame.MAXN = jcast('long', 1000000000000000)
Code05_FibonacciGame.MAXM = jcast('int', 101)
Code05_FibonacciGame.f = jarray('long', [Code05_FibonacciGame.MAXM])
Code05_FibonacciGame.size = jcast('int', 0)

if __name__ == '__main__':
    Code05_FibonacciGame.main([])
