# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 负环和差分约束模版题(转化成形式2进而转化成判断无限增加的环)
# 一共有n个变量，编号1~n，给定m个不等式，每个不等式的形式为
# Xi - Xj <= Ci，其中Xi和Xj为变量，Ci为常量
# 如果不等式存在矛盾导致无解，打印"NO"
# 如果有解，打印满足所有不等式的其中一组解(X1, X2...)
# 1 <= n、m <= 5 * 10^3
# -10^4 <= Ci <= +10^4
# 测试链接 : https://www.luogu.com.cn/problem/P5960
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_DifferenceConstraints2:
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
        Code01_DifferenceConstraints2.cnt = jcast('int', 1)
        Code01_DifferenceConstraints2.h = jcast('int', jset(Code01_DifferenceConstraints2, 't', 0))
        jstatic('Arrays', 'fill', Code01_DifferenceConstraints2.head, 0, jcast('int', jadd(Code01_DifferenceConstraints2.n, 1)), 0)
        # 所有距离先设置成最小值
        jstatic('Arrays', 'fill', Code01_DifferenceConstraints2.dist, 0, jcast('int', jadd(Code01_DifferenceConstraints2.n, 1)), jget(Integer, 'MIN_VALUE'))
        jstatic('Arrays', 'fill', Code01_DifferenceConstraints2.update, 0, jcast('int', jadd(Code01_DifferenceConstraints2.n, 1)), 0)
        jstatic('Arrays', 'fill', Code01_DifferenceConstraints2.enter, 0, jcast('int', jadd(Code01_DifferenceConstraints2.n, 1)), False)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        Code01_DifferenceConstraints2.next[Code01_DifferenceConstraints2.cnt] = jcast('int', Code01_DifferenceConstraints2.head[u])
        Code01_DifferenceConstraints2.to[Code01_DifferenceConstraints2.cnt] = jcast('int', v)
        Code01_DifferenceConstraints2.weight[Code01_DifferenceConstraints2.cnt] = jcast('int', w)
        jset(Code01_DifferenceConstraints2.head, u, ((_java_obj_1 := Code01_DifferenceConstraints2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    # 来自讲解065，spfa判断无限增加环，s是超级源点
    @staticmethod
    def spfa(s):
        s = jcast('int', s)
        Code01_DifferenceConstraints2.dist[s] = jcast('int', 0)
        Code01_DifferenceConstraints2.update[s] = jcast('int', 1)
        jset(Code01_DifferenceConstraints2.queue, ((_java_obj_4 := Code01_DifferenceConstraints2), (_java_key_5 := 't'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], s)
        Code01_DifferenceConstraints2.enter[s] = jcast('boolean', True)
        while (Code01_DifferenceConstraints2.h < Code01_DifferenceConstraints2.t):
            u = jcast('int', Code01_DifferenceConstraints2.queue[((_java_obj_7 := Code01_DifferenceConstraints2), (_java_key_8 := 'h'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])
            Code01_DifferenceConstraints2.enter[u] = jcast('boolean', False)
            ei = jcast('int', Code01_DifferenceConstraints2.head[u])
            v = 0
            w = 0
            while (ei > 0):
                v = jcast('int', Code01_DifferenceConstraints2.to[ei])
                w = jcast('int', Code01_DifferenceConstraints2.weight[ei])
                # 变大才更新
                if (Code01_DifferenceConstraints2.dist[v] < jcast('int', jadd(Code01_DifferenceConstraints2.dist[u], w))):
                    Code01_DifferenceConstraints2.dist[v] = jcast('int', jcast('int', jadd(Code01_DifferenceConstraints2.dist[u], w)))
                    if (not Code01_DifferenceConstraints2.enter[v]):
                        # 注意判断逻辑和讲解065的代码不一样
                        # 因为节点0是额外增加的超级源点
                        # 所以节点数量增加了1个，所以这么判断
                        if (((_java_obj_10 := Code01_DifferenceConstraints2.update), (_java_key_11 := v), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3] > Code01_DifferenceConstraints2.n):
                            return jcast('boolean', True)
                        jset(Code01_DifferenceConstraints2.queue, ((_java_obj_13 := Code01_DifferenceConstraints2), (_java_key_14 := 't'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))), _java_old_15)[4], v)
                        Code01_DifferenceConstraints2.enter[v] = jcast('boolean', True)
                ei = jcast('int', Code01_DifferenceConstraints2.next[ei])
        return jcast('boolean', False)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_DifferenceConstraints2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code01_DifferenceConstraints2.m = jcast('int', jcast('int', jget(in_, 'nval')))
        Code01_DifferenceConstraints2.prepare()
        # 0号点是连通超级源点，保证图的连通性
        i = jcast('int', 1)
        while (i <= Code01_DifferenceConstraints2.n):
            Code01_DifferenceConstraints2.addEdge(0, i, 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i <= Code01_DifferenceConstraints2.m):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            w = jcast('int', jcast('int', jget(in_, 'nval')))
            # 形式2的连边方式
            Code01_DifferenceConstraints2.addEdge(u, v, jcast('int', (-w)))
            i = jcast('int', (i + 1))
        if Code01_DifferenceConstraints2.spfa(0):
            jcall(out, 'println', 'NO')
        else:
            i = jcast('int', 1)
            while (i <= Code01_DifferenceConstraints2.n):
                jcall(out, 'print', jadd(Code01_DifferenceConstraints2.dist[i], ' '))
                i = jcast('int', (i + 1))
            jcall(out, 'println')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_DifferenceConstraints2.MAXN = jcast('int', 5001)
Code01_DifferenceConstraints2.MAXM = jcast('int', 10001)
Code01_DifferenceConstraints2.head = jarray('int', [Code01_DifferenceConstraints2.MAXN])
Code01_DifferenceConstraints2.next = jarray('int', [Code01_DifferenceConstraints2.MAXM])
Code01_DifferenceConstraints2.to = jarray('int', [Code01_DifferenceConstraints2.MAXM])
Code01_DifferenceConstraints2.weight = jarray('int', [Code01_DifferenceConstraints2.MAXM])
Code01_DifferenceConstraints2.cnt = jcast('int', 0)
Code01_DifferenceConstraints2.dist = jarray('int', [Code01_DifferenceConstraints2.MAXN])
Code01_DifferenceConstraints2.update = jarray('int', [Code01_DifferenceConstraints2.MAXN])
Code01_DifferenceConstraints2.MAXQ = jcast('int', 5000001)
Code01_DifferenceConstraints2.queue = jarray('int', [Code01_DifferenceConstraints2.MAXQ])
Code01_DifferenceConstraints2.h = jcast('int', 0)
Code01_DifferenceConstraints2.t = jcast('int', 0)
Code01_DifferenceConstraints2.enter = jarray('boolean', [Code01_DifferenceConstraints2.MAXN])
Code01_DifferenceConstraints2.n = jcast('int', 0)
Code01_DifferenceConstraints2.m = jcast('int', 0)

if __name__ == '__main__':
    Code01_DifferenceConstraints2.main([])
