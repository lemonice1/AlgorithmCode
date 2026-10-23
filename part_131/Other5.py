# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 题目5，最佳团体，另一种二分的写法
# 思路是不变的，二分的写法多种多样
# 代码中打注释的位置，就是更简单的二分逻辑，其他代码没有变化
# 测试链接 : https://www.luogu.com.cn/problem/P4322
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Other5:
    __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'NA': 'NA', 'head': 'head', 'next': 'next', 'to': 'to', 'edgeCnt': 'edgeCnt', 'cost': 'cost', 'strength': 'strength', 'dfn': 'dfn', 'dfnCnt': 'dfnCnt', 'value': 'value', 'size': 'size', 'dp': 'dp', 'k': 'k', 'n': 'n'}
    MAXN = 0
    LIMIT = 0
    NA = 0.0
    head = None
    next = None
    to = None
    edgeCnt = 0
    cost = None
    strength = None
    dfn = None
    dfnCnt = 0
    value = None
    size = None
    dp = None
    k = 0
    n = 0
    @staticmethod
    def prepare():
        Other5.edgeCnt = jcast('int', 1)
        Other5.dfnCnt = jcast('int', 0)
        jstatic('Arrays', 'fill', Other5.head, 1, jcast('int', jadd(Other5.n, 1)), 0)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Other5.next[Other5.edgeCnt] = jcast('int', Other5.head[u])
        Other5.to[Other5.edgeCnt] = jcast('int', v)
        jset(Other5.head, u, ((_java_obj_1 := Other5), (_java_key_2 := 'edgeCnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dfs(u):
        u = jcast('int', u)
        i = jcast('int', ((_java_obj_4 := Other5), (_java_key_5 := 'dfnCnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Other5.dfn[u] = jcast('int', i)
        Other5.size[i] = jcast('int', 1)
        e = jcast('int', Other5.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Other5.to[e])
            ((_java_obj_7 := Other5.size), (_java_key_8 := i), jset(_java_obj_7, _java_key_8, jcast('int', jadd(jget(_java_obj_7, _java_key_8), Other5.dfs(v)))))[2]
            e = jcast('int', Other5.next[e])
        return jcast('int', Other5.size[i])

    @staticmethod
    def check(x):
        x = jcast('double', x)
        i = jcast('int', 0)
        while (i <= Other5.n):
            jset(Other5.value, Other5.dfn[i], (jcast('double', Other5.strength[i]) - (x * Other5.cost[i])))
            i = jcast('int', (i + 1))
        j = jcast('int', 1)
        while (j <= Other5.k):
            jset(Other5.dp[jcast('int', jadd(Other5.dfnCnt, 1))], j, Other5.NA)
            j = jcast('int', (j + 1))
        i = jcast('int', Other5.dfnCnt)
        while (i >= 2):
            j = jcast('int', 1)
            while (j <= Other5.k):
                jset(Other5.dp[i], j, jstatic('Math', 'max', Other5.dp[jcast('int', jadd(i, Other5.size[i]))][j], jadd(Other5.value[i], Other5.dp[jcast('int', jadd(i, 1))][jcast('int', (j - 1))])))
                j = jcast('int', (j + 1))
            i = jcast('int', (i - 1))
        return jcast('boolean', (Other5.dp[2][Other5.k] >= 0))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Other5.k = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Other5.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Other5.prepare()
        i = jcast('int', 1)
        while (i <= Other5.n):
            jcall(in_, 'nextToken')
            Other5.cost[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Other5.strength[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Other5.addEdge(jcast('int', jget(in_, 'nval')), i)
            i = jcast('int', (i + 1))
        Other5.dfs(0)
        l = jcast('double', 0)
        r = jcast('double', Other5.LIMIT)
        x = 0.0
        # 二分进行60次，足够达到题目要求的精度
        # 二分完成后，l就是答案
        i = jcast('int', 1)
        while (i <= 60):
            x = jcast('double', jdiv(jadd(l, r), 2))
            if Other5.check(x):
                l = jcast('double', x)
            else:
                r = jcast('double', x)
            i = jcast('int', (i + 1))
        jcall(out, 'printf', '%.3f\n', l)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Other5.MAXN = jcast('int', 3001)
Other5.LIMIT = jcast('int', 10000)
Other5.NA = jcast('double', (-1000000000.0))
Other5.head = jarray('int', [Other5.MAXN])
Other5.next = jarray('int', [Other5.MAXN])
Other5.to = jarray('int', [Other5.MAXN])
Other5.edgeCnt = jcast('int', 0)
Other5.cost = jarray('int', [Other5.MAXN])
Other5.strength = jarray('int', [Other5.MAXN])
Other5.dfn = jarray('int', [Other5.MAXN])
Other5.dfnCnt = jcast('int', 0)
Other5.value = jarray('double', [Other5.MAXN])
Other5.size = jarray('int', [Other5.MAXN])
Other5.dp = jarray('double', [Other5.MAXN, Other5.MAXN])
Other5.k = jcast('int', 0)
Other5.n = jcast('int', 0)

if __name__ == '__main__':
    Other5.main([])
