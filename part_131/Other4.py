# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 题目4，最小圈，另一种二分的写法
# 思路是不变的，二分的写法多种多样
# 代码中打注释的位置，就是更简单的二分逻辑，其他代码没有变化
# 测试链接 : https://www.luogu.com.cn/problem/P3199
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Other4:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXE': 'MAXE', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'value': 'value', 'path': 'path', 'n': 'n', 'm': 'm'}
    MAXN = 0
    MAXM = 0
    MAXE = 0.0
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    value = None
    path = None
    n = 0
    m = 0
    @staticmethod
    def prepare():
        Other4.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Other4.head, 1, jcast('int', jadd(Other4.n, 1)), 0)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('double', w)
        Other4.next[Other4.cnt] = jcast('int', Other4.head[u])
        Other4.to[Other4.cnt] = jcast('int', v)
        Other4.weight[Other4.cnt] = jcast('double', w)
        jset(Other4.head, u, ((_java_obj_1 := Other4), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def check(x):
        x = jcast('double', x)
        jstatic('Arrays', 'fill', Other4.value, 1, jcast('int', jadd(Other4.n, 1)), 0)
        jstatic('Arrays', 'fill', Other4.path, 1, jcast('int', jadd(Other4.n, 1)), False)
        return jcast('boolean', Other4.dfs(0, x))

    @staticmethod
    def dfs(u, x):
        u = jcast('int', u)
        x = jcast('double', x)
        if (u == 0):
            i = jcast('int', 1)
            while (i <= Other4.n):
                if Other4.dfs(i, x):
                    return jcast('boolean', True)
                i = jcast('int', (i + 1))
        else:
            Other4.path[u] = jcast('boolean', True)
            e = jcast('int', Other4.head[u])
            while (e != 0):
                v = jcast('int', Other4.to[e])
                w = jcast('double', (Other4.weight[e] - x))
                if (Other4.value[v] > jadd(Other4.value[u], w)):
                    Other4.value[v] = jcast('double', jadd(Other4.value[u], w))
                    if (Other4.path[v] or Other4.dfs(v, x)):
                        return jcast('boolean', True)
                e = jcast('int', Other4.next[e])
            Other4.path[u] = jcast('boolean', False)
        return jcast('boolean', False)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Other4.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Other4.m = jcast('int', jcast('int', jget(in_, 'nval')))
        Other4.prepare()
        i = jcast('int', 1)
        while (i <= Other4.m):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            w = jcast('double', jget(in_, 'nval'))
            Other4.addEdge(u, v, w)
            i = jcast('int', (i + 1))
        l = jcast('double', (-Other4.MAXE))
        r = jcast('double', Other4.MAXE)
        x = 0.0
        # 二分进行60次，足够达到题目要求的精度
        # 二分完成后，l就是答案
        i = jcast('int', 1)
        while (i <= 60):
            x = jcast('double', jdiv(jadd(l, r), 2))
            if Other4.check(x):
                r = jcast('double', x)
            else:
                l = jcast('double', x)
            i = jcast('int', (i + 1))
        jcall(out, 'printf', '%.8f\n', l)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Other4.MAXN = jcast('int', 3001)
Other4.MAXM = jcast('int', 10001)
Other4.MAXE = jcast('double', 10000000.0)
Other4.head = jarray('int', [Other4.MAXN])
Other4.next = jarray('int', [Other4.MAXM])
Other4.to = jarray('int', [Other4.MAXM])
Other4.weight = jarray('double', [Other4.MAXM])
Other4.cnt = jcast('int', 0)
Other4.value = jarray('double', [Other4.MAXN])
Other4.path = jarray('boolean', [Other4.MAXN])
Other4.n = jcast('int', 0)
Other4.m = jcast('int', 0)

if __name__ == '__main__':
    Other4.main([])
