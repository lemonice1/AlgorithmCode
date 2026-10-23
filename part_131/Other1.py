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

# 题目1，01分数规划模版题，另一种二分的写法
# 思路是不变的，二分的写法多种多样
# 代码中打注释的位置，就是更简单的二分逻辑，其他代码没有变化
# 测试链接 : https://www.luogu.com.cn/problem/P10505
# 测试链接 : http://poj.org/problem?id=2976
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Other1:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'n': 'n', 'k': 'k'}
    MAXN = 0
    arr = None
    n = 0
    k = 0
    @staticmethod
    def check(x):
        x = jcast('double', x)
        i = jcast('int', 1)
        while (i <= Other1.n):
            jset(Other1.arr[i], 2, (Other1.arr[i][0] - (x * Other1.arr[i][1])))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Other1.arr, 1, jcast('int', jadd(Other1.n, 1)), Other1.MyComparator())
        sum = jcast('double', 0)
        i = jcast('int', 1)
        while (i <= Other1.k):
            sum = jcast('double', jadd(sum, Other1.arr[i][2]))
            i = jcast('int', (i + 1))
        return jcast('boolean', (sum >= 0))

    class MyComparator:
        __java_fields__ = {}
        def compare(self, o1, o2):
            return jcast('int', (jcast('int', (-1)) if (o1[2] >= o2[2]) else 1))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Other1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Other1.k = jcast('int', jcast('int', jget(in_, 'nval')))
        while ((Other1.n != 0) or (Other1.k != 0)):
            Other1.k = jcast('int', jcast('int', (Other1.n - Other1.k)))
            i = jcast('int', 1)
            while (i <= Other1.n):
                jcall(in_, 'nextToken')
                jset(Other1.arr[i], 0, jget(in_, 'nval'))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Other1.n):
                jcall(in_, 'nextToken')
                jset(Other1.arr[i], 1, jget(in_, 'nval'))
                i = jcast('int', (i + 1))
            l = jcast('double', 0)
            r = jcast('double', 0)
            x = 0.0
            i = jcast('int', 1)
            while (i <= Other1.n):
                r = jcast('double', jadd(r, Other1.arr[i][0]))
                i = jcast('int', (i + 1))
            # 二分进行60次，足够达到题目要求的精度
            # 二分完成后，l就是答案
            i = jcast('int', 1)
            while (i <= 60):
                x = jcast('double', jdiv(jadd(l, r), 2))
                if Other1.check(x):
                    l = jcast('double', x)
                else:
                    r = jcast('double', x)
                i = jcast('int', (i + 1))
            jcall(out, 'println', jcast('int', (100 * jadd(l, 0.005))))
            jcall(in_, 'nextToken')
            Other1.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Other1.k = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Other1.MAXN = jcast('int', 1001)
Other1.arr = jarray('double', [Other1.MAXN, 3])
Other1.n = jcast('int', 0)
Other1.k = jcast('int', 0)

if __name__ == '__main__':
    Other1.main([])
