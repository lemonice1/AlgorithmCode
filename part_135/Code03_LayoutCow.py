# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 布局奶牛
# 编号1到编号n的奶牛从左往右站成一排，你可以决定任意相邻奶牛之间的距离
# 有m1条好友信息，有m2条情敌信息，好友间希望距离更近，情敌间希望距离更远
# 每条好友信息为 : u v w，表示希望u和v之间的距离 <= w，输入保证u < v
# 每条情敌信息为 : u v w，表示希望u和v之间的距离 >= w，输入保证u < v
# 你需要安排奶牛的布局，满足所有的好友信息和情敌信息
# 如果不存在合法方案，返回-1
# 如果存在合法方案，返回1号奶牛和n号奶牛之间的最大距离
# 如果存在合法方案，并且1号奶牛和n号奶牛之间的距离可以无穷远，返回-2
# 测试链接 : https://www.luogu.com.cn/problem/P4878
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_LayoutCow:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'dist': 'dist', 'update': 'update', 'MAXQ': 'MAXQ', 'queue': 'queue', 'h': 'h', 't': 't', 'enter': 'enter', 'n': 'n', 'm1': 'm1', 'm2': 'm2'}
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
    m1 = 0
    m2 = 0
    @staticmethod
    def prepare():
        Code03_LayoutCow.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code03_LayoutCow.head, 0, jcast('int', jadd(Code03_LayoutCow.n, 1)), 0)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code03_LayoutCow.next[Code03_LayoutCow.cnt] = jcast('int', Code03_LayoutCow.head[u])
        Code03_LayoutCow.to[Code03_LayoutCow.cnt] = jcast('int', v)
        Code03_LayoutCow.weight[Code03_LayoutCow.cnt] = jcast('int', w)
        jset(Code03_LayoutCow.head, u, ((_java_obj_1 := Code03_LayoutCow), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def spfa(s):
        s = jcast('int', s)
        Code03_LayoutCow.h = jcast('int', jset(Code03_LayoutCow, 't', 0))
        jstatic('Arrays', 'fill', Code03_LayoutCow.dist, 0, jcast('int', jadd(Code03_LayoutCow.n, 1)), jget(Integer, 'MAX_VALUE'))
        jstatic('Arrays', 'fill', Code03_LayoutCow.update, 0, jcast('int', jadd(Code03_LayoutCow.n, 1)), 0)
        jstatic('Arrays', 'fill', Code03_LayoutCow.enter, 0, jcast('int', jadd(Code03_LayoutCow.n, 1)), False)
        Code03_LayoutCow.dist[s] = jcast('int', 0)
        Code03_LayoutCow.update[s] = jcast('int', 1)
        jset(Code03_LayoutCow.queue, ((_java_obj_4 := Code03_LayoutCow), (_java_key_5 := 't'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], s)
        Code03_LayoutCow.enter[s] = jcast('boolean', True)
        while (Code03_LayoutCow.h < Code03_LayoutCow.t):
            u = jcast('int', Code03_LayoutCow.queue[((_java_obj_7 := Code03_LayoutCow), (_java_key_8 := 'h'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])
            Code03_LayoutCow.enter[u] = jcast('boolean', False)
            ei = jcast('int', Code03_LayoutCow.head[u])
            v = 0
            w = 0
            while (ei > 0):
                v = jcast('int', Code03_LayoutCow.to[ei])
                w = jcast('int', Code03_LayoutCow.weight[ei])
                if (Code03_LayoutCow.dist[v] > jcast('int', jadd(Code03_LayoutCow.dist[u], w))):
                    Code03_LayoutCow.dist[v] = jcast('int', jcast('int', jadd(Code03_LayoutCow.dist[u], w)))
                    if (not Code03_LayoutCow.enter[v]):
                        if (((_java_obj_10 := Code03_LayoutCow.update), (_java_key_11 := v), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3] > Code03_LayoutCow.n):
                            return jcast('int', jcast('int', (-1)))
                        jset(Code03_LayoutCow.queue, ((_java_obj_13 := Code03_LayoutCow), (_java_key_14 := 't'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))), _java_old_15)[4], v)
                        Code03_LayoutCow.enter[v] = jcast('boolean', True)
                ei = jcast('int', Code03_LayoutCow.next[ei])
        if (Code03_LayoutCow.dist[Code03_LayoutCow.n] == jget(Integer, 'MAX_VALUE')):
            return jcast('int', jcast('int', (-2)))
        return jcast('int', Code03_LayoutCow.dist[Code03_LayoutCow.n])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_LayoutCow.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code03_LayoutCow.m1 = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code03_LayoutCow.m2 = jcast('int', jcast('int', jget(in_, 'nval')))
        Code03_LayoutCow.prepare()
        # 0号点是连通超级源点，保证图的连通性
        i = jcast('int', 1)
        while (i <= Code03_LayoutCow.n):
            Code03_LayoutCow.addEdge(0, i, 0)
            i = jcast('int', (i + 1))
        # 好友关系连边
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i <= Code03_LayoutCow.m1):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            w = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_LayoutCow.addEdge(u, v, w)
            i = jcast('int', (i + 1))
        # 情敌关系连边
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i <= Code03_LayoutCow.m2):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            w = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_LayoutCow.addEdge(v, u, jcast('int', (-w)))
            i = jcast('int', (i + 1))
        # 根据本题的模型，一定要增加如下的边，不然会出错
        i = jcast('int', 1)
        while (i < Code03_LayoutCow.n):
            Code03_LayoutCow.addEdge(jcast('int', jadd(i, 1)), i, 0)
            i = jcast('int', (i + 1))
        ans = jcast('int', Code03_LayoutCow.spfa(0))
        if (ans == jcast('int', (-1))):
            jcall(out, 'println', ans)
        else:
            ans = jcast('int', Code03_LayoutCow.spfa(1))
            jcall(out, 'println', ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_LayoutCow.MAXN = jcast('int', 1001)
Code03_LayoutCow.MAXM = jcast('int', 20001)
Code03_LayoutCow.head = jarray('int', [Code03_LayoutCow.MAXN])
Code03_LayoutCow.next = jarray('int', [Code03_LayoutCow.MAXM])
Code03_LayoutCow.to = jarray('int', [Code03_LayoutCow.MAXM])
Code03_LayoutCow.weight = jarray('int', [Code03_LayoutCow.MAXM])
Code03_LayoutCow.cnt = jcast('int', 0)
Code03_LayoutCow.dist = jarray('int', [Code03_LayoutCow.MAXN])
Code03_LayoutCow.update = jarray('int', [Code03_LayoutCow.MAXN])
Code03_LayoutCow.MAXQ = jcast('int', 1000001)
Code03_LayoutCow.queue = jarray('int', [Code03_LayoutCow.MAXQ])
Code03_LayoutCow.h = jcast('int', 0)
Code03_LayoutCow.t = jcast('int', 0)
Code03_LayoutCow.enter = jarray('boolean', [Code03_LayoutCow.MAXN])
Code03_LayoutCow.n = jcast('int', 0)
Code03_LayoutCow.m1 = jcast('int', 0)
Code03_LayoutCow.m2 = jcast('int', 0)

if __name__ == '__main__':
    Code03_LayoutCow.main([])
