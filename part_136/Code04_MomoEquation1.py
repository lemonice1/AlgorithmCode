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

# 墨墨的等式(dijkstra算法)
# 一共有n种正数，每种数可以选择任意个，个数不能是负数
# 那么一定有某些数值可以由这些数字累加得到
# 请问在[l...r]范围上，有多少个数能被累加得到
# 0 <= n <= 12
# 0 <= 数值范围 <= 5 * 10^5
# 1 <= l <= r <= 10^12
# 测试链接 : https://www.luogu.com.cn/problem/P2371
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_MomoEquation1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'x': 'x', 'l': 'l', 'r': 'r', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'heap': 'heap', 'distance': 'distance', 'visited': 'visited'}
    MAXN = 0
    MAXM = 0
    n = 0
    x = 0
    l = 0
    r = 0
    # 链式前向星需要
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    # dijkstra算法需要
    # 0 : 当前节点
    # 1 : 源点到当前点距离
    heap = None
    distance = None
    visited = None
    @staticmethod
    def prepare():
        Code04_MomoEquation1.cnt = jcast('int', 1)
        jcall(Code04_MomoEquation1.heap, 'clear')
        jstatic('Arrays', 'fill', Code04_MomoEquation1.head, 0, Code04_MomoEquation1.x, 0)
        jstatic('Arrays', 'fill', Code04_MomoEquation1.distance, 0, Code04_MomoEquation1.x, jget(Long, 'MAX_VALUE'))
        jstatic('Arrays', 'fill', Code04_MomoEquation1.visited, 0, Code04_MomoEquation1.x, False)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('long', w)
        Code04_MomoEquation1.next[Code04_MomoEquation1.cnt] = jcast('int', Code04_MomoEquation1.head[u])
        Code04_MomoEquation1.to[Code04_MomoEquation1.cnt] = jcast('int', v)
        Code04_MomoEquation1.weight[Code04_MomoEquation1.cnt] = jcast('long', w)
        jset(Code04_MomoEquation1.head, u, ((_java_obj_1 := Code04_MomoEquation1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dijkstra():
        jcall(Code04_MomoEquation1.heap, 'add', jarray('long', [None], [0, 0]))
        Code04_MomoEquation1.distance[0] = jcast('long', 0)
        cur = None
        u = 0
        w = 0
        while (not jcall(Code04_MomoEquation1.heap, 'isEmpty')):
            try:
                cur = jcall(Code04_MomoEquation1.heap, 'poll')
                u = jcast('int', jcast('int', cur[0]))
                w = jcast('long', cur[1])
                if Code04_MomoEquation1.visited[u]:
                    raise JContinue(None)
                Code04_MomoEquation1.visited[u] = jcast('boolean', True)
                ei = jcast('int', Code04_MomoEquation1.head[u])
                v = 0
                while (ei > 0):
                    v = jcast('int', Code04_MomoEquation1.to[ei])
                    if ((not Code04_MomoEquation1.visited[v]) and (Code04_MomoEquation1.distance[v] > jcast('long', jadd(w, Code04_MomoEquation1.weight[ei])))):
                        Code04_MomoEquation1.distance[v] = jcast('long', jcast('long', jadd(w, Code04_MomoEquation1.weight[ei])))
                        jcall(Code04_MomoEquation1.heap, 'add', jarray('long', [None], [v, Code04_MomoEquation1.distance[v]]))
                    ei = jcast('int', Code04_MomoEquation1.next[ei])
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break

    @staticmethod
    def compute():
        Code04_MomoEquation1.dijkstra()
        ans = jcast('long', 0)
        i = jcast('int', 0)
        while (i < Code04_MomoEquation1.x):
            if (Code04_MomoEquation1.r >= Code04_MomoEquation1.distance[i]):
                ans = jcast('long', jcast('long', jadd(ans, jcast('long', jadd(jcast('long', jdiv(jcast('long', (Code04_MomoEquation1.r - Code04_MomoEquation1.distance[i])), Code04_MomoEquation1.x)), 1)))))
            if (Code04_MomoEquation1.l >= Code04_MomoEquation1.distance[i]):
                ans = jcast('long', jcast('long', (ans - jcast('long', jadd(jcast('long', jdiv(jcast('long', (Code04_MomoEquation1.l - Code04_MomoEquation1.distance[i])), Code04_MomoEquation1.x)), 1)))))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_MomoEquation1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_MomoEquation1.l = jcast('long', jcast('long', (jcast('long', jget(in_, 'nval')) - 1)))
        jcall(in_, 'nextToken')
        Code04_MomoEquation1.r = jcast('long', jcast('long', jget(in_, 'nval')))
        Code04_MomoEquation1.x = jcast('int', 0)
        i = jcast('int', 1)
        vi = 0
        while (i <= Code04_MomoEquation1.n):
            jcall(in_, 'nextToken')
            vi = jcast('int', jcast('int', jget(in_, 'nval')))
            if (vi != 0):
                if (Code04_MomoEquation1.x == 0):
                    Code04_MomoEquation1.x = jcast('int', vi)
                    Code04_MomoEquation1.prepare()
                else:
                    j = jcast('int', 0)
                    while (j < Code04_MomoEquation1.x):
                        Code04_MomoEquation1.addEdge(j, jcast('int', jmod(jcast('int', jadd(j, vi)), Code04_MomoEquation1.x)), vi)
                        j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code04_MomoEquation1.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_MomoEquation1.MAXN = jcast('int', 500001)
Code04_MomoEquation1.MAXM = jcast('int', 5000001)
Code04_MomoEquation1.n = jcast('int', 0)
Code04_MomoEquation1.x = jcast('int', 0)
Code04_MomoEquation1.l = jcast('long', 0)
Code04_MomoEquation1.r = jcast('long', 0)
Code04_MomoEquation1.head = jarray('int', [Code04_MomoEquation1.MAXN])
Code04_MomoEquation1.next = jarray('int', [Code04_MomoEquation1.MAXM])
Code04_MomoEquation1.to = jarray('int', [Code04_MomoEquation1.MAXM])
Code04_MomoEquation1.weight = jarray('long', [Code04_MomoEquation1.MAXM])
Code04_MomoEquation1.cnt = jcast('int', 0)
Code04_MomoEquation1.heap = jnew('PriorityQueue', (lambda a, b: (jcast('int', (-1)) if (a[1] <= b[1]) else 1)))
Code04_MomoEquation1.distance = jarray('long', [Code04_MomoEquation1.MAXN])
Code04_MomoEquation1.visited = jarray('boolean', [Code04_MomoEquation1.MAXN])

if __name__ == '__main__':
    Code04_MomoEquation1.main([])
