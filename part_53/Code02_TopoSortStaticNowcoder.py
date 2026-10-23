# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 拓扑排序模版（牛客）
# 链式前向星建图（静态方式）
# 测试链接 : https://www.nowcoder.com/practice/88f7e156ca7d43a1a535f619cd3f495c
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_TopoSortStaticNowcoder:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'queue': 'queue', 'l': 'l', 'r': 'r', 'indegree': 'indegree', 'ans': 'ans', 'n': 'n', 'm': 'm'}
    MAXN = 0
    MAXM = 0
    # 建图相关，链式前向星
    head = None
    next = None
    to = None
    cnt = 0
    # 拓扑排序，用到队列
    queue = None
    l = 0
    r = 0
    # 拓扑排序，入度表
    indegree = None
    # 收集拓扑排序的结果
    ans = None
    n = 0
    m = 0
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code02_TopoSortStaticNowcoder.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code02_TopoSortStaticNowcoder.head, 0, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code02_TopoSortStaticNowcoder.indegree, 0, jcast('int', jadd(n, 1)), 0)

    # 用链式前向星建图
    @staticmethod
    def addEdge(f, t):
        f = jcast('int', f)
        t = jcast('int', t)
        Code02_TopoSortStaticNowcoder.next[Code02_TopoSortStaticNowcoder.cnt] = jcast('int', Code02_TopoSortStaticNowcoder.head[f])
        Code02_TopoSortStaticNowcoder.to[Code02_TopoSortStaticNowcoder.cnt] = jcast('int', t)
        jset(Code02_TopoSortStaticNowcoder.head, f, ((_java_obj_1 := Code02_TopoSortStaticNowcoder), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code02_TopoSortStaticNowcoder.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code02_TopoSortStaticNowcoder.m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_TopoSortStaticNowcoder.build(Code02_TopoSortStaticNowcoder.n)
            i = jcast('int', 0)
            from_ = 0
            to = 0
            while (i < Code02_TopoSortStaticNowcoder.m):
                jcall(in_, 'nextToken')
                from_ = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                to = jcast('int', jcast('int', jget(in_, 'nval')))
                Code02_TopoSortStaticNowcoder.addEdge(from_, to)
                Code02_TopoSortStaticNowcoder.indegree[to] = jcast('int', (Code02_TopoSortStaticNowcoder.indegree[to] + 1))
                i = jcast('int', (i + 1))
            if (not Code02_TopoSortStaticNowcoder.topoSort()):
                jcall(out, 'println', jcast('int', (-1)))
            else:
                i = jcast('int', 0)
                while (i < jcast('int', (Code02_TopoSortStaticNowcoder.n - 1))):
                    jcall(out, 'print', jadd(Code02_TopoSortStaticNowcoder.ans[i], ' '))
                    i = jcast('int', (i + 1))
                jcall(out, 'println', Code02_TopoSortStaticNowcoder.ans[jcast('int', (Code02_TopoSortStaticNowcoder.n - 1))])
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def topoSort():
        Code02_TopoSortStaticNowcoder.l = jcast('int', jset(Code02_TopoSortStaticNowcoder, 'r', 0))
        i = jcast('int', 1)
        while (i <= Code02_TopoSortStaticNowcoder.n):
            if (Code02_TopoSortStaticNowcoder.indegree[i] == 0):
                jset(Code02_TopoSortStaticNowcoder.queue, ((_java_obj_4 := Code02_TopoSortStaticNowcoder), (_java_key_5 := 'r'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], i)
            i = jcast('int', (i + 1))
        fill = jcast('int', 0)
        while (Code02_TopoSortStaticNowcoder.l < Code02_TopoSortStaticNowcoder.r):
            cur = jcast('int', Code02_TopoSortStaticNowcoder.queue[((_java_obj_7 := Code02_TopoSortStaticNowcoder), (_java_key_8 := 'l'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])
            jset(Code02_TopoSortStaticNowcoder.ans, ((_java_old_10 := fill), (fill := jcast('int', (fill + (1)))), _java_old_10)[2], cur)
            # 用链式前向星的方式，遍历cur的相邻节点
            ei = jcast('int', Code02_TopoSortStaticNowcoder.head[cur])
            while (ei != 0):
                if (((_java_obj_11 := Code02_TopoSortStaticNowcoder.indegree), (_java_key_12 := Code02_TopoSortStaticNowcoder.to[ei]), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (-1)))))[3] == 0):
                    jset(Code02_TopoSortStaticNowcoder.queue, ((_java_obj_14 := Code02_TopoSortStaticNowcoder), (_java_key_15 := 'r'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))), _java_old_16)[4], Code02_TopoSortStaticNowcoder.to[ei])
                ei = jcast('int', Code02_TopoSortStaticNowcoder.next[ei])
        return jcast('boolean', (fill == Code02_TopoSortStaticNowcoder.n))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_TopoSortStaticNowcoder.MAXN = jcast('int', 200001)
Code02_TopoSortStaticNowcoder.MAXM = jcast('int', 200001)
Code02_TopoSortStaticNowcoder.head = jarray('int', [Code02_TopoSortStaticNowcoder.MAXN])
Code02_TopoSortStaticNowcoder.next = jarray('int', [Code02_TopoSortStaticNowcoder.MAXM])
Code02_TopoSortStaticNowcoder.to = jarray('int', [Code02_TopoSortStaticNowcoder.MAXM])
Code02_TopoSortStaticNowcoder.cnt = jcast('int', 0)
Code02_TopoSortStaticNowcoder.queue = jarray('int', [Code02_TopoSortStaticNowcoder.MAXN])
Code02_TopoSortStaticNowcoder.l = jcast('int', 0)
Code02_TopoSortStaticNowcoder.r = jcast('int', 0)
Code02_TopoSortStaticNowcoder.indegree = jarray('int', [Code02_TopoSortStaticNowcoder.MAXN])
Code02_TopoSortStaticNowcoder.ans = jarray('int', [Code02_TopoSortStaticNowcoder.MAXN])
Code02_TopoSortStaticNowcoder.n = jcast('int', 0)
Code02_TopoSortStaticNowcoder.m = jcast('int', 0)

if __name__ == '__main__':
    Code02_TopoSortStaticNowcoder.main([])
