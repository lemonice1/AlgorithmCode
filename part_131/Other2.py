# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 题目2，牛群的才艺展示，另一种二分的写法
# 思路是不变的，二分的写法多种多样
# 代码中打注释的位置，就是更简单的二分逻辑，其他代码没有变化
# 测试链接 : https://www.luogu.com.cn/problem/P4377
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Other2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXW': 'MAXW', 'NA': 'NA', 'weight': 'weight', 'talent': 'talent', 'value': 'value', 'dp': 'dp', 'n': 'n', 'w': 'w'}
    MAXN = 0
    MAXW = 0
    NA = 0.0
    weight = None
    talent = None
    value = None
    dp = None
    n = 0
    w = 0
    @staticmethod
    def check(x):
        x = jcast('double', x)
        i = jcast('int', 1)
        while (i <= Other2.n):
            Other2.value[i] = jcast('double', (jcast('double', Other2.talent[i]) - (x * Other2.weight[i])))
            i = jcast('int', (i + 1))
        Other2.dp[0] = jcast('double', 0)
        jstatic('Arrays', 'fill', Other2.dp, 1, jcast('int', jadd(Other2.w, 1)), Other2.NA)
        i = jcast('int', 1)
        while (i <= Other2.n):
            p = jcast('int', Other2.w)
            j = 0
            while (p >= 0):
                j = jcast('int', jcast('int', jcast('int', jadd(p, Other2.weight[i]))))
                if (j >= Other2.w):
                    jset(Other2.dp, Other2.w, jstatic('Math', 'max', Other2.dp[Other2.w], jadd(Other2.dp[p], Other2.value[i])))
                else:
                    jset(Other2.dp, j, jstatic('Math', 'max', Other2.dp[j], jadd(Other2.dp[p], Other2.value[i])))
                p = jcast('int', (p - 1))
            i = jcast('int', (i + 1))
        return jcast('boolean', (Other2.dp[Other2.w] >= 0))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Other2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Other2.w = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Other2.n):
            jcall(in_, 'nextToken')
            Other2.weight[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Other2.talent[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        l = jcast('double', 0)
        r = jcast('double', 0)
        x = 0.0
        i = jcast('int', 1)
        while (i <= Other2.n):
            r = jcast('double', jadd(r, Other2.talent[i]))
            i = jcast('int', (i + 1))
        # 二分进行60次，足够达到题目要求的精度
        # 二分完成后，l就是答案
        i = jcast('int', 1)
        while (i <= 60):
            x = jcast('double', jdiv(jadd(l, r), 2))
            if Other2.check(x):
                l = jcast('double', x)
            else:
                r = jcast('double', x)
            i = jcast('int', (i + 1))
        jcall(out, 'println', jcast('int', (l * 1000)))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Other2.MAXN = jcast('int', 251)
Other2.MAXW = jcast('int', 1001)
Other2.NA = jcast('double', (-1000000000.0))
Other2.weight = jarray('int', [Other2.MAXN])
Other2.talent = jarray('int', [Other2.MAXN])
Other2.value = jarray('double', [Other2.MAXN])
Other2.dp = jarray('double', [Other2.MAXW])
Other2.n = jcast('int', 0)
Other2.w = jcast('int', 0)

if __name__ == '__main__':
    Other2.main([])
