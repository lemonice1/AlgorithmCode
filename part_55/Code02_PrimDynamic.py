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

# Prim算法模版（洛谷）
# 动态空间实现
# 测试链接 : https://www.luogu.com.cn/problem/P3366
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 时间复杂度O(n + m) + O(m * log m)
class Code02_PrimDynamic:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            graph = jnew('ArrayList')
            n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i <= n):
                jcall(graph, 'add', jnew('ArrayList'))
                i = jcast('int', (i + 1))
            jcall(in_, 'nextToken')
            m = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            u = 0
            v = 0
            w = 0
            while (i < m):
                jcall(in_, 'nextToken')
                u = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                w = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(jcall(graph, 'get', u), 'add', jarray('int', [None], [v, w]))
                jcall(jcall(graph, 'get', v), 'add', jarray('int', [None], [u, w]))
                i = jcast('int', (i + 1))
            # int[] record
            # record[0] : 到达的节点
            # record[1] : 到达的花费
            heap = jnew('PriorityQueue', (lambda a, b: (a[1] - b[1])))
            for edge in jcall(graph, 'get', 1):
                jcall(heap, 'add', edge)
            # 哪些节点已经发现过了
            set = jarray('boolean', [jcast('int', jadd(n, 1))])
            nodeCnt = jcast('int', 1)
            set[1] = jcast('boolean', True)
            ans = jcast('int', 0)
            while (not jcall(heap, 'isEmpty')):
                edge = jcall(heap, 'poll')
                next = jcast('int', edge[0])
                cost = jcast('int', edge[1])
                if (not set[next]):
                    nodeCnt = jcast('int', (nodeCnt + 1))
                    set[next] = jcast('boolean', True)
                    ans = jcast('int', jcast('int', jadd(ans, cost)))
                    for e in jcall(graph, 'get', next):
                        jcall(heap, 'add', e)
            jcall(out, 'println', (ans if (nodeCnt == n) else 'orz'))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code02_PrimDynamic.main([])
