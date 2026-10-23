# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 格点连线上有几个格点
# 二维网格中只有x和y的值都为整数的坐标，才叫格点
# 给定两个格点，A在(x1, y1)，B在(x2, y2)
# 返回A和B的连线上，包括A和B在内，一共有几个格点
# -10^9 <= x1、y1、x2、y2 <= 10^9
# 测试链接 : https://lightoj.com/problem/how-many-points
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_HowManyPoints:
    __java_fields__ = {}
    @staticmethod
    def gcd(a, b):
        a = jcast('long', a)
        b = jcast('long', b)
        return jcast('long', (a if (b == 0) else Code03_HowManyPoints.gcd(b, jcast('long', jmod(a, b)))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        cases = jcast('int', jcast('int', jget(in_, 'nval')))
        t = jcast('int', 1)
        while (t <= cases):
            jcall(in_, 'nextToken')
            x1 = jcast('long', jcast('long', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            y1 = jcast('long', jcast('long', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            x2 = jcast('long', jcast('long', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            y2 = jcast('long', jcast('long', jget(in_, 'nval')))
            ans = jcast('long', jcast('long', jadd(Code03_HowManyPoints.gcd(jstatic('Math', 'abs', jcast('long', (x1 - x2))), jstatic('Math', 'abs', jcast('long', (y1 - y2)))), 1)))
            jcall(out, 'println', jadd(jadd(jadd('Case ', t), ': '), ans))
            t = jcast('int', (t + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code03_HowManyPoints.main([])
