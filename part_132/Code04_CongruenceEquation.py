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

# 同余方程
# 求关于x的同余方程 ax ≡ 1(mod b) 的最小正整数解
# 题目保证一定有解，也就是a和b互质
# 2 <= a、b <= 2 * 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P1082
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_CongruenceEquation:
    __java_fields__ = {'d': 'd', 'x': 'x', 'y': 'y', 'px': 'px', 'py': 'py'}
    # 扩展欧几里得算法
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
            Code04_CongruenceEquation.d = jcast('long', a)
            Code04_CongruenceEquation.x = jcast('long', 1)
            Code04_CongruenceEquation.y = jcast('long', 0)
        else:
            Code04_CongruenceEquation.exgcd(b, jcast('long', jmod(a, b)))
            Code04_CongruenceEquation.px = jcast('long', Code04_CongruenceEquation.x)
            Code04_CongruenceEquation.py = jcast('long', Code04_CongruenceEquation.y)
            Code04_CongruenceEquation.x = jcast('long', Code04_CongruenceEquation.py)
            Code04_CongruenceEquation.y = jcast('long', jcast('long', (Code04_CongruenceEquation.px - jcast('long', (Code04_CongruenceEquation.py * jcast('long', jdiv(a, b)))))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        a = jcast('long', jcast('long', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        b = jcast('long', jcast('long', jget(in_, 'nval')))
        Code04_CongruenceEquation.exgcd(a, b)
        jcall(out, 'println', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(Code04_CongruenceEquation.x, b)), b)), b)))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_CongruenceEquation.d = jcast('long', 0)
Code04_CongruenceEquation.x = jcast('long', 0)
Code04_CongruenceEquation.y = jcast('long', 0)
Code04_CongruenceEquation.px = jcast('long', 0)
Code04_CongruenceEquation.py = jcast('long', 0)

if __name__ == '__main__':
    Code04_CongruenceEquation.main([])
