# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 节点最多经过两次的tsp问题
# 给定有n个地点，用m条边无向边连接，每条边有权值
# 你可以任选一点出发，目标是经过所有的点，最终不必回到出发点
# 并且每个点最多可以到达两次
# 返回总路程最小是多少
# 1 <= n <= 10
# 1 <= m <= 100
# 测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=3001
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_TspTwice:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXS': 'MAXS', 'n': 'n', 'm': 'm', 'maxs': 'maxs', 'graph': 'graph', 'dp': 'dp', 'complete': 'complete', 'size': 'size'}
    MAXN = 0
    MAXS = 0
    n = 0
    m = 0
    maxs = 0
    graph = None
    dp = None
    complete = None
    size = 0
    @staticmethod
    def build():
        i = jcast('int', 0)
        while (i < Code03_TspTwice.n):
            j = jcast('int', 0)
            while (j < Code03_TspTwice.n):
                jset(Code03_TspTwice.graph[i], j, jget(Integer, 'MAX_VALUE'))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        Code03_TspTwice.maxs = jcast('int', jcast('int', jstatic('Math', 'pow', 3, Code03_TspTwice.n)))
        i = jcast('int', 0)
        while (i < Code03_TspTwice.n):
            s = jcast('int', 0)
            while (s < Code03_TspTwice.maxs):
                jset(Code03_TspTwice.dp[i], s, jcast('int', (-1)))
                s = jcast('int', (s + 1))
            i = jcast('int', (i + 1))
        Code03_TspTwice.size = jcast('int', 0)
        Code03_TspTwice.dfs(0, 1, 0)

    @staticmethod
    def dfs(i, bit, s):
        i = jcast('int', i)
        bit = jcast('int', bit)
        s = jcast('int', s)
        if (i == Code03_TspTwice.n):
            jset(Code03_TspTwice.complete, ((_java_obj_1 := Code03_TspTwice), (_java_key_2 := 'size'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], s)
        else:
            Code03_TspTwice.dfs(jcast('int', jadd(i, 1)), jcast('int', (bit * 3)), jcast('int', jadd(s, bit)))
            Code03_TspTwice.dfs(jcast('int', jadd(i, 1)), jcast('int', (bit * 3)), jcast('int', jadd(s, jcast('int', (2 * bit)))))

    @staticmethod
    def compute():
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        k = jcast('int', 0)
        while (k < Code03_TspTwice.size):
            i = jcast('int', 0)
            bit = jcast('int', 1)
            while (i < Code03_TspTwice.n):
                ans = jcast('int', jstatic('Math', 'min', ans, Code03_TspTwice.f(i, jcast('int', (Code03_TspTwice.complete[k] - bit)))))
                i = jcast('int', (i + 1))
                bit = jcast('int', jcast('int', (bit * 3)))
            k = jcast('int', (k + 1))
        return jcast('int', ans)

    @staticmethod
    def f(i, s):
        i = jcast('int', i)
        s = jcast('int', s)
        if (s == 0):
            return jcast('int', 0)
        if (Code03_TspTwice.dp[i][s] != jcast('int', (-1))):
            return jcast('int', Code03_TspTwice.dp[i][s])
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        j = jcast('int', 0)
        bit = jcast('int', 1)
        pre = 0
        while (j < Code03_TspTwice.n):
            if (jcast('int', jmod(jcast('int', jdiv(s, bit)), 3)) > 0):
                pre = jcast('int', Code03_TspTwice.f(j, jcast('int', (s - bit))))
                if ((pre != jget(Integer, 'MAX_VALUE')) and (Code03_TspTwice.graph[j][i] != jget(Integer, 'MAX_VALUE'))):
                    ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(pre, Code03_TspTwice.graph[j][i]))))
            j = jcast('int', (j + 1))
            bit = jcast('int', jcast('int', (bit * 3)))
        jset(Code03_TspTwice.dp[i], s, ans)
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_TspTwice.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code03_TspTwice.m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_TspTwice.build()
            i = jcast('int', 1)
            u = 0
            v = 0
            w = 0
            while (i <= Code03_TspTwice.m):
                jcall(in_, 'nextToken')
                u = jcast('int', jcast('int', (jcast('int', jget(in_, 'nval')) - 1)))
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', (jcast('int', jget(in_, 'nval')) - 1)))
                jcall(in_, 'nextToken')
                w = jcast('int', jcast('int', jget(in_, 'nval')))
                if (w < Code03_TspTwice.graph[u][v]):
                    jset(Code03_TspTwice.graph[u], v, jset(Code03_TspTwice.graph[v], u, w))
                i = jcast('int', (i + 1))
            ans = jcast('int', Code03_TspTwice.compute())
            jcall(out, 'println', (jcast('int', (-1)) if (ans == jget(Integer, 'MAX_VALUE')) else ans))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_TspTwice.MAXN = jcast('int', 10)
Code03_TspTwice.MAXS = jcast('int', jcast('int', jstatic('Math', 'pow', 3, Code03_TspTwice.MAXN)))
Code03_TspTwice.n = jcast('int', 0)
Code03_TspTwice.m = jcast('int', 0)
Code03_TspTwice.maxs = jcast('int', 0)
Code03_TspTwice.graph = jarray('int', [Code03_TspTwice.MAXN, Code03_TspTwice.MAXN])
Code03_TspTwice.dp = jarray('int', [Code03_TspTwice.MAXN, Code03_TspTwice.MAXS])
Code03_TspTwice.complete = jarray('int', [jcast('int', (1 << (Code03_TspTwice.MAXN & 31)))])
Code03_TspTwice.size = jcast('int', 0)

if __name__ == '__main__':
    Code03_TspTwice.main([])
