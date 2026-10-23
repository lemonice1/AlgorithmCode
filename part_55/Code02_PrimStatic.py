# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# Prim算法优化（洛谷）
# 静态空间实现
# 时间复杂度O(n + m) + O((m+n) * log n)
# 测试链接 : https://www.luogu.com.cn/problem/P3366
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 建图用链式前向星
# 堆也是用数组结构手写的、且只和节点个数有关
# 这个实现留给有需要的同学
# 但是一般情况下并不需要做到这个程度
class Code02_PrimStatic:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'heap': 'heap', 'where': 'where', 'heapSize': 'heapSize', 'nodeCnt': 'nodeCnt', 'u': 'u', 'w': 'w'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    # 链式前向星建图
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    # 改写的堆结构
    heap = None
    # where[v] = -1，表示v这个节点，从来没有进入过堆
    # where[v] = -2，表示v这个节点，已经弹出过了
    # where[v] = i(>=0)，表示v这个节点，在堆上的i位置
    where = None
    # 堆的大小
    heapSize = 0
    # 找到的节点个数
    nodeCnt = 0
    @staticmethod
    def build():
        Code02_PrimStatic.cnt = jcast('int', 1)
        Code02_PrimStatic.heapSize = jcast('int', 0)
        Code02_PrimStatic.nodeCnt = jcast('int', 0)
        jstatic('Arrays', 'fill', Code02_PrimStatic.head, 1, jcast('int', jadd(Code02_PrimStatic.n, 1)), 0)
        jstatic('Arrays', 'fill', Code02_PrimStatic.where, 1, jcast('int', jadd(Code02_PrimStatic.n, 1)), jcast('int', (-1)))

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code02_PrimStatic.next[Code02_PrimStatic.cnt] = jcast('int', Code02_PrimStatic.head[u])
        Code02_PrimStatic.to[Code02_PrimStatic.cnt] = jcast('int', v)
        Code02_PrimStatic.weight[Code02_PrimStatic.cnt] = jcast('int', w)
        jset(Code02_PrimStatic.head, u, ((_java_obj_1 := Code02_PrimStatic), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # 当前处理的是编号为ei的边！
    @staticmethod
    def addOrUpdateOrIgnore(ei):
        ei = jcast('int', ei)
        v = jcast('int', Code02_PrimStatic.to[ei])
        w = jcast('int', Code02_PrimStatic.weight[ei])
        # 去往v点，权重w
        if (Code02_PrimStatic.where[v] == jcast('int', (-1))):
            # v这个点，从来没有进入过堆！
            jset(Code02_PrimStatic.heap[Code02_PrimStatic.heapSize], 0, v)
            jset(Code02_PrimStatic.heap[Code02_PrimStatic.heapSize], 1, w)
            jset(Code02_PrimStatic.where, v, ((_java_obj_4 := Code02_PrimStatic), (_java_key_5 := 'heapSize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4])
            Code02_PrimStatic.heapInsert(Code02_PrimStatic.where[v])
        else:
            if (Code02_PrimStatic.where[v] >= 0):
                # v这个点的记录，在堆上的位置是where[v]
                jset(Code02_PrimStatic.heap[Code02_PrimStatic.where[v]], 1, jstatic('Math', 'min', Code02_PrimStatic.heap[Code02_PrimStatic.where[v]][1], w))
                Code02_PrimStatic.heapInsert(Code02_PrimStatic.where[v])

    @staticmethod
    def heapInsert(i):
        i = jcast('int', i)
        while (Code02_PrimStatic.heap[i][1] < Code02_PrimStatic.heap[jcast('int', jdiv(jcast('int', (i - 1)), 2))][1]):
            Code02_PrimStatic.swap(i, jcast('int', jdiv(jcast('int', (i - 1)), 2)))
            i = jcast('int', jcast('int', jdiv(jcast('int', (i - 1)), 2)))

    u = 0
    w = 0
    # 堆顶的记录：节点 -> u、到节点的花费 -> w
    @staticmethod
    def pop():
        Code02_PrimStatic.u = jcast('int', Code02_PrimStatic.heap[0][0])
        Code02_PrimStatic.w = jcast('int', Code02_PrimStatic.heap[0][1])
        Code02_PrimStatic.swap(0, ((_java_obj_7 := Code02_PrimStatic), (_java_key_8 := 'heapSize'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))))[3])
        Code02_PrimStatic.heapify(0)
        Code02_PrimStatic.where[Code02_PrimStatic.u] = jcast('int', jcast('int', (-2)))
        Code02_PrimStatic.nodeCnt = jcast('int', (Code02_PrimStatic.nodeCnt + 1))

    @staticmethod
    def heapify(i):
        i = jcast('int', i)
        l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
        while (l < Code02_PrimStatic.heapSize):
            try:
                best = jcast('int', (jcast('int', jadd(l, 1)) if ((jcast('int', jadd(l, 1)) < Code02_PrimStatic.heapSize) and (Code02_PrimStatic.heap[jcast('int', jadd(l, 1))][1] < Code02_PrimStatic.heap[l][1])) else l))
                best = jcast('int', (best if (Code02_PrimStatic.heap[best][1] < Code02_PrimStatic.heap[i][1]) else i))
                if (best == i):
                    raise JBreak(None)
                Code02_PrimStatic.swap(best, i)
                i = jcast('int', best)
                l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break

    @staticmethod
    def isEmpty():
        return jcast('boolean', (Code02_PrimStatic.heapSize == 0))

    # 堆上，i位置的信息 和 j位置的信息 交换！
    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        a = jcast('int', Code02_PrimStatic.heap[i][0])
        b = jcast('int', Code02_PrimStatic.heap[j][0])
        Code02_PrimStatic.where[a] = jcast('int', j)
        Code02_PrimStatic.where[b] = jcast('int', i)
        tmp = Code02_PrimStatic.heap[i]
        Code02_PrimStatic.heap[i] = Code02_PrimStatic.heap[j]
        Code02_PrimStatic.heap[j] = tmp

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code02_PrimStatic.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code02_PrimStatic.m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_PrimStatic.build()
            i = jcast('int', 0)
            u = 0
            v = 0
            w = 0
            while (i < Code02_PrimStatic.m):
                jcall(in_, 'nextToken')
                u = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                w = jcast('int', jcast('int', jget(in_, 'nval')))
                Code02_PrimStatic.addEdge(u, v, w)
                Code02_PrimStatic.addEdge(v, u, w)
                i = jcast('int', (i + 1))
            ans = jcast('int', Code02_PrimStatic.prim())
            jcall(out, 'println', (ans if (Code02_PrimStatic.nodeCnt == Code02_PrimStatic.n) else 'orz'))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def prim():
        # 1节点出发
        Code02_PrimStatic.nodeCnt = jcast('int', 1)
        Code02_PrimStatic.where[1] = jcast('int', jcast('int', (-2)))
        ei = jcast('int', Code02_PrimStatic.head[1])
        while (ei > 0):
            Code02_PrimStatic.addOrUpdateOrIgnore(ei)
            ei = jcast('int', Code02_PrimStatic.next[ei])
        ans = jcast('int', 0)
        while (not Code02_PrimStatic.isEmpty()):
            Code02_PrimStatic.pop()
            ans = jcast('int', jcast('int', jadd(ans, Code02_PrimStatic.w)))
            ei = jcast('int', Code02_PrimStatic.head[Code02_PrimStatic.u])
            while (ei > 0):
                Code02_PrimStatic.addOrUpdateOrIgnore(ei)
                ei = jcast('int', Code02_PrimStatic.next[ei])
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_PrimStatic.MAXN = jcast('int', 5001)
Code02_PrimStatic.MAXM = jcast('int', 400001)
Code02_PrimStatic.n = jcast('int', 0)
Code02_PrimStatic.m = jcast('int', 0)
Code02_PrimStatic.head = jarray('int', [Code02_PrimStatic.MAXN])
Code02_PrimStatic.next = jarray('int', [Code02_PrimStatic.MAXM])
Code02_PrimStatic.to = jarray('int', [Code02_PrimStatic.MAXM])
Code02_PrimStatic.weight = jarray('int', [Code02_PrimStatic.MAXM])
Code02_PrimStatic.cnt = jcast('int', 0)
Code02_PrimStatic.heap = jarray('int', [Code02_PrimStatic.MAXN, 2])
Code02_PrimStatic.where = jarray('int', [Code02_PrimStatic.MAXN])
Code02_PrimStatic.heapSize = jcast('int', 0)
Code02_PrimStatic.nodeCnt = jcast('int', 0)
Code02_PrimStatic.u = jcast('int', 0)
Code02_PrimStatic.w = jcast('int', 0)

if __name__ == '__main__':
    Code02_PrimStatic.main([])
