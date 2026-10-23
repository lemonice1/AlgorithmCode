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

# 题目3，最优比率生成树，另一种二分的写法
# 思路是不变的，二分的写法多种多样
# 代码中打注释的位置，就是更简单的二分逻辑，其他代码没有变化
# 测试链接 : http://poj.org/problem?id=2728
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Other3:
    __java_fields__ = {'MAXN': 'MAXN', 'x': 'x', 'y': 'y', 'z': 'z', 'dist': 'dist', 'cost': 'cost', 'visit': 'visit', 'value': 'value', 'n': 'n'}
    MAXN = 0
    x = None
    y = None
    z = None
    dist = None
    cost = None
    visit = None
    value = None
    n = 0
    @staticmethod
    def prim(x):
        x = jcast('double', x)
        i = jcast('int', 1)
        while (i <= Other3.n):
            Other3.visit[i] = jcast('boolean', False)
            Other3.value[i] = jcast('double', (Other3.cost[1][i] - (x * Other3.dist[1][i])))
            i = jcast('int', (i + 1))
        Other3.visit[1] = jcast('boolean', True)
        sum = jcast('double', 0)
        i = jcast('int', 1)
        while (i <= jcast('int', (Other3.n - 1))):
            minDist = jcast('double', jget(Double, 'MAX_VALUE'))
            next = jcast('int', 0)
            j = jcast('int', 1)
            while (j <= Other3.n):
                if ((not Other3.visit[j]) and (Other3.value[j] < minDist)):
                    minDist = jcast('double', Other3.value[j])
                    next = jcast('int', j)
                j = jcast('int', (j + 1))
            sum = jcast('double', jadd(sum, minDist))
            Other3.visit[next] = jcast('boolean', True)
            j = jcast('int', 1)
            while (j <= Other3.n):
                if ((not Other3.visit[j]) and (Other3.value[j] > (Other3.cost[next][j] - (x * Other3.dist[next][j])))):
                    Other3.value[j] = jcast('double', (Other3.cost[next][j] - (x * Other3.dist[next][j])))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('double', sum)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Other3.n = jcast('int', jcast('int', jget(in_, 'nval')))
        while (Other3.n != 0):
            i = jcast('int', 1)
            while (i <= Other3.n):
                jcall(in_, 'nextToken')
                Other3.x[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Other3.y[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Other3.z[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Other3.n):
                j = jcast('int', 1)
                while (j <= Other3.n):
                    if (i != j):
                        jset(Other3.dist[i], j, jstatic('Math', 'sqrt', jcast('int', jadd(jcast('int', (jcast('int', (Other3.x[i] - Other3.x[j])) * jcast('int', (Other3.x[i] - Other3.x[j])))), jcast('int', (jcast('int', (Other3.y[i] - Other3.y[j])) * jcast('int', (Other3.y[i] - Other3.y[j]))))))))
                        jset(Other3.cost[i], j, jstatic('Math', 'abs', jcast('int', (Other3.z[i] - Other3.z[j]))))
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))
            l = jcast('double', 0)
            r = jcast('double', 100)
            x = 0.0
            # 二分进行60次，足够达到题目要求的精度
            # 二分完成后，l就是答案
            i = jcast('int', 1)
            while (i <= 60):
                x = jcast('double', jdiv(jadd(l, r), 2))
                if (Other3.prim(x) <= 0):
                    r = jcast('double', x)
                else:
                    l = jcast('double', x)
                i = jcast('int', (i + 1))
            jcall(out, 'printf', '%.3f\n', l)
            jcall(in_, 'nextToken')
            Other3.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Other3.MAXN = jcast('int', 1001)
Other3.x = jarray('int', [Other3.MAXN])
Other3.y = jarray('int', [Other3.MAXN])
Other3.z = jarray('int', [Other3.MAXN])
Other3.dist = jarray('double', [Other3.MAXN, Other3.MAXN])
Other3.cost = jarray('double', [Other3.MAXN, Other3.MAXN])
Other3.visit = jarray('boolean', [Other3.MAXN])
Other3.value = jarray('double', [Other3.MAXN])
Other3.n = jcast('int', 0)

if __name__ == '__main__':
    Other3.main([])
