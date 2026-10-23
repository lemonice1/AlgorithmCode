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

# 小k的农场
# 一共有n个农场，编号1~n，给定m条关系，每条关系是如下三种形式中的一种
# 关系1 a b c : 表示农场a比农场b至少多种植了c个作物
# 关系2 a b c : 表示农场a比农场b至多多种植了c个作物
# 关系3 a b   : 表示农场a和农场b种植了一样多的作物
# 如果关系之间能推出矛盾，打印"No"，不存在矛盾，打印"Yes"
# 1 <= n、m <= 5 * 10^3
# 1 <= c <= 5 * 10^3
# 测试链接 : https://www.luogu.com.cn/problem/P1993
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_KsFarm:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'dist': 'dist', 'update': 'update', 'MAXQ': 'MAXQ', 'queue': 'queue', 'h': 'h', 't': 't', 'enter': 'enter', 'n': 'n', 'm': 'm'}
    MAXN = 0
    MAXM = 0
    # 链式前向星需要
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    # spfa需要
    dist = None
    update = None
    MAXQ = 0
    queue = None
    h = 0
    t = 0
    enter = None
    n = 0
    m = 0
    @staticmethod
    def prepare():
        Code02_KsFarm.cnt = jcast('int', 1)
        Code02_KsFarm.h = jcast('int', jset(Code02_KsFarm, 't', 0))
        jstatic('Arrays', 'fill', Code02_KsFarm.head, 0, jcast('int', jadd(Code02_KsFarm.n, 1)), 0)
        jstatic('Arrays', 'fill', Code02_KsFarm.dist, 0, jcast('int', jadd(Code02_KsFarm.n, 1)), jget(Integer, 'MAX_VALUE'))
        jstatic('Arrays', 'fill', Code02_KsFarm.update, 0, jcast('int', jadd(Code02_KsFarm.n, 1)), 0)
        jstatic('Arrays', 'fill', Code02_KsFarm.enter, 0, jcast('int', jadd(Code02_KsFarm.n, 1)), False)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code02_KsFarm.next[Code02_KsFarm.cnt] = jcast('int', Code02_KsFarm.head[u])
        Code02_KsFarm.to[Code02_KsFarm.cnt] = jcast('int', v)
        Code02_KsFarm.weight[Code02_KsFarm.cnt] = jcast('int', w)
        jset(Code02_KsFarm.head, u, ((_java_obj_1 := Code02_KsFarm), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def spfa(s):
        s = jcast('int', s)
        Code02_KsFarm.dist[s] = jcast('int', 0)
        Code02_KsFarm.update[s] = jcast('int', 1)
        jset(Code02_KsFarm.queue, ((_java_obj_4 := Code02_KsFarm), (_java_key_5 := 't'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], s)
        Code02_KsFarm.enter[s] = jcast('boolean', True)
        while (Code02_KsFarm.h < Code02_KsFarm.t):
            u = jcast('int', Code02_KsFarm.queue[((_java_obj_7 := Code02_KsFarm), (_java_key_8 := 'h'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])
            Code02_KsFarm.enter[u] = jcast('boolean', False)
            ei = jcast('int', Code02_KsFarm.head[u])
            v = 0
            w = 0
            while (ei > 0):
                v = jcast('int', Code02_KsFarm.to[ei])
                w = jcast('int', Code02_KsFarm.weight[ei])
                if (Code02_KsFarm.dist[v] > jcast('int', jadd(Code02_KsFarm.dist[u], w))):
                    Code02_KsFarm.dist[v] = jcast('int', jcast('int', jadd(Code02_KsFarm.dist[u], w)))
                    if (not Code02_KsFarm.enter[v]):
                        if (((_java_obj_10 := Code02_KsFarm.update), (_java_key_11 := v), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3] > Code02_KsFarm.n):
                            return jcast('boolean', True)
                        jset(Code02_KsFarm.queue, ((_java_obj_13 := Code02_KsFarm), (_java_key_14 := 't'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))), _java_old_15)[4], v)
                        Code02_KsFarm.enter[v] = jcast('boolean', True)
                ei = jcast('int', Code02_KsFarm.next[ei])
        return jcast('boolean', False)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_KsFarm.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_KsFarm.m = jcast('int', jcast('int', jget(in_, 'nval')))
        Code02_KsFarm.prepare()
        i = jcast('int', 1)
        while (i <= Code02_KsFarm.n):
            Code02_KsFarm.addEdge(0, i, 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        type = 0
        u = 0
        v = 0
        w = 0
        while (i <= Code02_KsFarm.m):
            jcall(in_, 'nextToken')
            type = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            if (type == 1):
                jcall(in_, 'nextToken')
                w = jcast('int', jcast('int', jget(in_, 'nval')))
                Code02_KsFarm.addEdge(u, v, jcast('int', (-w)))
            else:
                if (type == 2):
                    jcall(in_, 'nextToken')
                    w = jcast('int', jcast('int', jget(in_, 'nval')))
                    Code02_KsFarm.addEdge(v, u, w)
                else:
                    Code02_KsFarm.addEdge(u, v, 0)
                    Code02_KsFarm.addEdge(v, u, 0)
            i = jcast('int', (i + 1))
        if Code02_KsFarm.spfa(0):
            jcall(out, 'println', 'No')
        else:
            jcall(out, 'println', 'Yes')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_KsFarm.MAXN = jcast('int', 5001)
Code02_KsFarm.MAXM = jcast('int', 20001)
Code02_KsFarm.head = jarray('int', [Code02_KsFarm.MAXN])
Code02_KsFarm.next = jarray('int', [Code02_KsFarm.MAXM])
Code02_KsFarm.to = jarray('int', [Code02_KsFarm.MAXM])
Code02_KsFarm.weight = jarray('int', [Code02_KsFarm.MAXM])
Code02_KsFarm.cnt = jcast('int', 0)
Code02_KsFarm.dist = jarray('int', [Code02_KsFarm.MAXN])
Code02_KsFarm.update = jarray('int', [Code02_KsFarm.MAXN])
Code02_KsFarm.MAXQ = jcast('int', 20000001)
Code02_KsFarm.queue = jarray('int', [Code02_KsFarm.MAXQ])
Code02_KsFarm.h = jcast('int', 0)
Code02_KsFarm.t = jcast('int', 0)
Code02_KsFarm.enter = jarray('boolean', [Code02_KsFarm.MAXN])
Code02_KsFarm.n = jcast('int', 0)
Code02_KsFarm.m = jcast('int', 0)

if __name__ == '__main__':
    Code02_KsFarm.main([])
