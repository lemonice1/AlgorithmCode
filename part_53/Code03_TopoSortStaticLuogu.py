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

# 字典序最小的拓扑排序
# 要求返回所有正确的拓扑排序中 字典序最小 的结果
# 建图请使用链式前向星方式，因为比赛平台用其他建图方式会卡空间
# 测试链接 : https://www.luogu.com.cn/problem/U107394
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_TopoSortStaticLuogu:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'heap': 'heap', 'heapSize': 'heapSize', 'indegree': 'indegree', 'ans': 'ans', 'n': 'n', 'm': 'm'}
    MAXN = 0
    MAXM = 0
    # 建图相关，链式前向星
    head = None
    next = None
    to = None
    cnt = 0
    # 拓扑排序，不用队列，用小根堆，为了得到字典序最小的拓扑排序
    heap = None
    heapSize = 0
    # 拓扑排序，入度表
    indegree = None
    # 收集拓扑排序的结果
    ans = None
    n = 0
    m = 0
    # 清理之前的脏数据
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code03_TopoSortStaticLuogu.cnt = jcast('int', 1)
        Code03_TopoSortStaticLuogu.heapSize = jcast('int', 0)
        jstatic('Arrays', 'fill', Code03_TopoSortStaticLuogu.head, 0, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code03_TopoSortStaticLuogu.indegree, 0, jcast('int', jadd(n, 1)), 0)

    # 用链式前向星建图
    @staticmethod
    def addEdge(f, t):
        f = jcast('int', f)
        t = jcast('int', t)
        Code03_TopoSortStaticLuogu.next[Code03_TopoSortStaticLuogu.cnt] = jcast('int', Code03_TopoSortStaticLuogu.head[f])
        Code03_TopoSortStaticLuogu.to[Code03_TopoSortStaticLuogu.cnt] = jcast('int', t)
        jset(Code03_TopoSortStaticLuogu.head, f, ((_java_obj_1 := Code03_TopoSortStaticLuogu), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # 小根堆里加入数字
    @staticmethod
    def push(num):
        num = jcast('int', num)
        i = jcast('int', ((_java_obj_4 := Code03_TopoSortStaticLuogu), (_java_key_5 := 'heapSize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4])
        Code03_TopoSortStaticLuogu.heap[i] = jcast('int', num)
        # heapInsert的过程
        while (Code03_TopoSortStaticLuogu.heap[i] < Code03_TopoSortStaticLuogu.heap[jcast('int', jdiv(jcast('int', (i - 1)), 2))]):
            Code03_TopoSortStaticLuogu.swap(i, jcast('int', jdiv(jcast('int', (i - 1)), 2)))
            i = jcast('int', jcast('int', jdiv(jcast('int', (i - 1)), 2)))

    # 小根堆里弹出最小值
    @staticmethod
    def pop():
        ans = jcast('int', Code03_TopoSortStaticLuogu.heap[0])
        jset(Code03_TopoSortStaticLuogu.heap, 0, Code03_TopoSortStaticLuogu.heap[((_java_obj_7 := Code03_TopoSortStaticLuogu), (_java_key_8 := 'heapSize'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))))[3]])
        # heapify的过程
        i = jcast('int', 0)
        l = jcast('int', 1)
        while (l < Code03_TopoSortStaticLuogu.heapSize):
            try:
                best = jcast('int', (jcast('int', jadd(l, 1)) if ((jcast('int', jadd(l, 1)) < Code03_TopoSortStaticLuogu.heapSize) and (Code03_TopoSortStaticLuogu.heap[jcast('int', jadd(l, 1))] < Code03_TopoSortStaticLuogu.heap[l])) else l))
                best = jcast('int', (best if (Code03_TopoSortStaticLuogu.heap[best] < Code03_TopoSortStaticLuogu.heap[i]) else i))
                if (best == i):
                    raise JBreak(None)
                Code03_TopoSortStaticLuogu.swap(best, i)
                i = jcast('int', best)
                l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
            except JContinue as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
            except JBreak as _java_control_10:
                if _java_control_10.label not in (None,):
                    raise
                break
        return jcast('int', ans)

    # 判断小根堆是否为空
    @staticmethod
    def isEmpty():
        return jcast('boolean', (Code03_TopoSortStaticLuogu.heapSize == 0))

    # 交换堆上两个位置的数字
    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code03_TopoSortStaticLuogu.heap[i])
        Code03_TopoSortStaticLuogu.heap[i] = jcast('int', Code03_TopoSortStaticLuogu.heap[j])
        Code03_TopoSortStaticLuogu.heap[j] = jcast('int', tmp)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_TopoSortStaticLuogu.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code03_TopoSortStaticLuogu.m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_TopoSortStaticLuogu.build(Code03_TopoSortStaticLuogu.n)
            i = jcast('int', 0)
            from_ = 0
            to = 0
            while (i < Code03_TopoSortStaticLuogu.m):
                jcall(in_, 'nextToken')
                from_ = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                to = jcast('int', jcast('int', jget(in_, 'nval')))
                Code03_TopoSortStaticLuogu.addEdge(from_, to)
                Code03_TopoSortStaticLuogu.indegree[to] = jcast('int', (Code03_TopoSortStaticLuogu.indegree[to] + 1))
                i = jcast('int', (i + 1))
            Code03_TopoSortStaticLuogu.topoSort()
            i = jcast('int', 0)
            while (i < jcast('int', (Code03_TopoSortStaticLuogu.n - 1))):
                jcall(out, 'print', jadd(Code03_TopoSortStaticLuogu.ans[i], ' '))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code03_TopoSortStaticLuogu.ans[jcast('int', (Code03_TopoSortStaticLuogu.n - 1))])
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def topoSort():
        i = jcast('int', 1)
        while (i <= Code03_TopoSortStaticLuogu.n):
            if (Code03_TopoSortStaticLuogu.indegree[i] == 0):
                Code03_TopoSortStaticLuogu.push(i)
            i = jcast('int', (i + 1))
        fill = jcast('int', 0)
        while (not Code03_TopoSortStaticLuogu.isEmpty()):
            cur = jcast('int', Code03_TopoSortStaticLuogu.pop())
            jset(Code03_TopoSortStaticLuogu.ans, ((_java_old_11 := fill), (fill := jcast('int', (fill + (1)))), _java_old_11)[2], cur)
            # 用链式前向星的方式，遍历cur的相邻节点
            ei = jcast('int', Code03_TopoSortStaticLuogu.head[cur])
            while (ei != 0):
                if (((_java_obj_12 := Code03_TopoSortStaticLuogu.indegree), (_java_key_13 := Code03_TopoSortStaticLuogu.to[ei]), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (-1)))))[3] == 0):
                    Code03_TopoSortStaticLuogu.push(Code03_TopoSortStaticLuogu.to[ei])
                ei = jcast('int', Code03_TopoSortStaticLuogu.next[ei])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_TopoSortStaticLuogu.MAXN = jcast('int', 100001)
Code03_TopoSortStaticLuogu.MAXM = jcast('int', 100001)
Code03_TopoSortStaticLuogu.head = jarray('int', [Code03_TopoSortStaticLuogu.MAXN])
Code03_TopoSortStaticLuogu.next = jarray('int', [Code03_TopoSortStaticLuogu.MAXM])
Code03_TopoSortStaticLuogu.to = jarray('int', [Code03_TopoSortStaticLuogu.MAXM])
Code03_TopoSortStaticLuogu.cnt = jcast('int', 0)
Code03_TopoSortStaticLuogu.heap = jarray('int', [Code03_TopoSortStaticLuogu.MAXN])
Code03_TopoSortStaticLuogu.heapSize = jcast('int', 0)
Code03_TopoSortStaticLuogu.indegree = jarray('int', [Code03_TopoSortStaticLuogu.MAXN])
Code03_TopoSortStaticLuogu.ans = jarray('int', [Code03_TopoSortStaticLuogu.MAXN])
Code03_TopoSortStaticLuogu.n = jcast('int', 0)
Code03_TopoSortStaticLuogu.m = jcast('int', 0)

if __name__ == '__main__':
    Code03_TopoSortStaticLuogu.main([])
