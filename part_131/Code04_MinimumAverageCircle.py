# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最小圈
# 一共有n个节点，m条有向边，每条边有权值
# 这个有向带权图中，可能有若干环，规定环的平均值为
# 环中边的权值和 / 环中边的数量
# 返回所有环的平均值中最少的平均值，结果保留小数点后8位，其余部分舍弃
# 1 <= n <= 3000
# 1 <= m <= 10000
# -10^7 <= 边权 <= 10^7
# 测试链接 : https://www.luogu.com.cn/problem/P3199
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_MinimumAverageCircle:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXE': 'MAXE', 'sml': 'sml', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'value': 'value', 'path': 'path', 'n': 'n', 'm': 'm'}
    MAXN = 0
    MAXM = 0
    MAXE = 0.0
    sml = 0.0
    # 链式前向星
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    # dfs判断负环，每个点的累积边权
    value = None
    # dfs判断负环，每个点是否是递归路径上的点
    path = None
    n = 0
    m = 0
    @staticmethod
    def prepare():
        Code04_MinimumAverageCircle.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code04_MinimumAverageCircle.head, 1, jcast('int', jadd(Code04_MinimumAverageCircle.n, 1)), 0)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('double', w)
        Code04_MinimumAverageCircle.next[Code04_MinimumAverageCircle.cnt] = jcast('int', Code04_MinimumAverageCircle.head[u])
        Code04_MinimumAverageCircle.to[Code04_MinimumAverageCircle.cnt] = jcast('int', v)
        Code04_MinimumAverageCircle.weight[Code04_MinimumAverageCircle.cnt] = jcast('double', w)
        jset(Code04_MinimumAverageCircle.head, u, ((_java_obj_1 := Code04_MinimumAverageCircle), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # 所有边都减去x，返回图中是否存在负环
    @staticmethod
    def check(x):
        x = jcast('double', x)
        jstatic('Arrays', 'fill', Code04_MinimumAverageCircle.value, 1, jcast('int', jadd(Code04_MinimumAverageCircle.n, 1)), 0)
        jstatic('Arrays', 'fill', Code04_MinimumAverageCircle.path, 1, jcast('int', jadd(Code04_MinimumAverageCircle.n, 1)), False)
        return jcast('boolean', Code04_MinimumAverageCircle.dfs(0, x))

    # 其实就是spfa的递归版，时间复杂度O(n * m)
    @staticmethod
    def dfs(u, x):
        u = jcast('int', u)
        x = jcast('double', x)
        if (u == 0):
            # 认为0号点是超级源点，具有通往所有点的有向边
            i = jcast('int', 1)
            while (i <= Code04_MinimumAverageCircle.n):
                if Code04_MinimumAverageCircle.dfs(i, x):
                    return jcast('boolean', True)
                i = jcast('int', (i + 1))
        else:
            Code04_MinimumAverageCircle.path[u] = jcast('boolean', True)
            e = jcast('int', Code04_MinimumAverageCircle.head[u])
            while (e != 0):
                v = jcast('int', Code04_MinimumAverageCircle.to[e])
                w = jcast('double', (Code04_MinimumAverageCircle.weight[e] - x))
                # 只有v的累积边权变小，才会递归，非常强的剪枝
                # 如果递归路径回到v，并且此时是v的累积边权更小的情况，说明遇到了负环
                # 或者后续递归找到了负环
                # 直接返回true
                if (Code04_MinimumAverageCircle.value[v] > jadd(Code04_MinimumAverageCircle.value[u], w)):
                    Code04_MinimumAverageCircle.value[v] = jcast('double', jadd(Code04_MinimumAverageCircle.value[u], w))
                    if (Code04_MinimumAverageCircle.path[v] or Code04_MinimumAverageCircle.dfs(v, x)):
                        return jcast('boolean', True)
                e = jcast('int', Code04_MinimumAverageCircle.next[e])
            Code04_MinimumAverageCircle.path[u] = jcast('boolean', False)
        return jcast('boolean', False)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_MinimumAverageCircle.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_MinimumAverageCircle.m = jcast('int', jcast('int', jget(in_, 'nval')))
        Code04_MinimumAverageCircle.prepare()
        i = jcast('int', 1)
        while (i <= Code04_MinimumAverageCircle.m):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            w = jcast('double', jget(in_, 'nval'))
            Code04_MinimumAverageCircle.addEdge(u, v, w)
            i = jcast('int', (i + 1))
        l = jcast('double', (-Code04_MinimumAverageCircle.MAXE))
        r = jcast('double', Code04_MinimumAverageCircle.MAXE)
        x = 0.0
        ans = jcast('double', 0)
        while ((l < r) and ((r - l) >= Code04_MinimumAverageCircle.sml)):
            x = jcast('double', jdiv(jadd(l, r), 2))
            if Code04_MinimumAverageCircle.check(x):
                r = jcast('double', (x - Code04_MinimumAverageCircle.sml))
            else:
                ans = jcast('double', x)
                l = jcast('double', jadd(x, Code04_MinimumAverageCircle.sml))
        jcall(out, 'printf', '%.8f\n', ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_MinimumAverageCircle.MAXN = jcast('int', 3001)
Code04_MinimumAverageCircle.MAXM = jcast('int', 10001)
Code04_MinimumAverageCircle.MAXE = jcast('double', 10000000.0)
Code04_MinimumAverageCircle.sml = jcast('double', 1e-09)
Code04_MinimumAverageCircle.head = jarray('int', [Code04_MinimumAverageCircle.MAXN])
Code04_MinimumAverageCircle.next = jarray('int', [Code04_MinimumAverageCircle.MAXM])
Code04_MinimumAverageCircle.to = jarray('int', [Code04_MinimumAverageCircle.MAXM])
Code04_MinimumAverageCircle.weight = jarray('double', [Code04_MinimumAverageCircle.MAXM])
Code04_MinimumAverageCircle.cnt = jcast('int', 0)
Code04_MinimumAverageCircle.value = jarray('double', [Code04_MinimumAverageCircle.MAXN])
Code04_MinimumAverageCircle.path = jarray('boolean', [Code04_MinimumAverageCircle.MAXN])
Code04_MinimumAverageCircle.n = jcast('int', 0)
Code04_MinimumAverageCircle.m = jcast('int', 0)

if __name__ == '__main__':
    Code04_MinimumAverageCircle.main([])
