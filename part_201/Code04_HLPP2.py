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

# HLPP算法，Python版
# 图中一共n个点，m条有向边，给定源点s和汇点t
# 给定每条有向边的起点、终点、容量
# 计算源点s到汇点t的网络最大流
# 1 <= n <= 1200
# 1 <= m <= 120000
# 边的容量为非负整数
# 测试链接 : https://www.luogu.com.cn/problem/P4722
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_HLPP2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'limit': 'limit', 'cntg': 'cntg', 'excess': 'excess', 'dis': 'dis', 'que': 'que', 'cur': 'cur', 'gap': 'gap', 'bucket': 'bucket', 'nextActive': 'nextActive', 'highest': 'highest'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    head = None
    nxt = None
    to = None
    limit = None
    cntg = 0
    excess = None
    dis = None
    que = None
    cur = None
    gap = None
    bucket = None
    nextActive = None
    highest = 0
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code04_HLPP2.nxt, ((_java_obj_1 := Code04_HLPP2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_HLPP2.head[u])
        Code04_HLPP2.to[Code04_HLPP2.cntg] = jcast('int', v)
        Code04_HLPP2.limit[Code04_HLPP2.cntg] = jcast('int', w)
        Code04_HLPP2.head[u] = jcast('int', Code04_HLPP2.cntg)

    @staticmethod
    def addActive(u):
        u = jcast('int', u)
        Code04_HLPP2.highest = jcast('int', jstatic('Math', 'max', Code04_HLPP2.highest, Code04_HLPP2.dis[u]))
        Code04_HLPP2.nextActive[u] = jcast('int', Code04_HLPP2.bucket[Code04_HLPP2.dis[u]])
        jset(Code04_HLPP2.bucket, Code04_HLPP2.dis[u], u)

    @staticmethod
    def pushFlow(u, v, e, k):
        u = jcast('int', u)
        v = jcast('int', v)
        e = jcast('int', e)
        k = jcast('long', k)
        Code04_HLPP2.excess[u] = jcast('long', jcast('long', (Code04_HLPP2.excess[u] - k)))
        Code04_HLPP2.excess[v] = jcast('long', jcast('long', jadd(Code04_HLPP2.excess[v], k)))
        Code04_HLPP2.limit[e] = jcast('int', jcast('long', (Code04_HLPP2.limit[e] - k)))
        Code04_HLPP2.limit[jcast('int', (e ^ 1))] = jcast('int', jcast('long', jadd(Code04_HLPP2.limit[jcast('int', (e ^ 1))], k)))

    @staticmethod
    def bfs(t):
        t = jcast('int', t)
        i = jcast('int', 1)
        while (i <= Code04_HLPP2.n):
            Code04_HLPP2.dis[i] = jcast('int', jcast('int', jadd(Code04_HLPP2.n, 1)))
            Code04_HLPP2.cur[i] = jcast('int', Code04_HLPP2.head[i])
            i = jcast('int', (i + 1))
        Code04_HLPP2.dis[t] = jcast('int', 0)
        l = jcast('int', 1)
        r = jcast('int', 0)
        jset(Code04_HLPP2.que, (r := jcast('int', (r + (1)))), t)
        while (l <= r):
            u = jcast('int', Code04_HLPP2.que[((_java_old_4 := l), (l := jcast('int', (l + (1)))), _java_old_4)[2]])
            e = jcast('int', Code04_HLPP2.head[u])
            while (e > 0):
                v = jcast('int', Code04_HLPP2.to[e])
                if ((Code04_HLPP2.dis[v] == jcast('int', jadd(Code04_HLPP2.n, 1))) and (Code04_HLPP2.limit[jcast('int', (e ^ 1))] > 0)):
                    Code04_HLPP2.dis[v] = jcast('int', jcast('int', jadd(Code04_HLPP2.dis[u], 1)))
                    jset(Code04_HLPP2.que, (r := jcast('int', (r + (1)))), v)
                e = jcast('int', Code04_HLPP2.nxt[e])

    @staticmethod
    def relabel(u, s, t):
        u = jcast('int', u)
        s = jcast('int', s)
        t = jcast('int', t)
        if ((Code04_HLPP2.dis[u] < Code04_HLPP2.n) and (Code04_HLPP2.gap[Code04_HLPP2.dis[u]] == 1)):
            h = jcast('int', Code04_HLPP2.dis[u])
            i = jcast('int', 1)
            while (i <= Code04_HLPP2.n):
                if ((((i != s) and (i != t)) and (Code04_HLPP2.dis[i] >= h)) and (Code04_HLPP2.dis[i] < Code04_HLPP2.n)):
                    ((_java_obj_5 := Code04_HLPP2.gap), (_java_key_6 := Code04_HLPP2.dis[i]), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4]
                    Code04_HLPP2.dis[i] = jcast('int', jcast('int', jadd(Code04_HLPP2.n, 1)))
                    ((_java_obj_8 := Code04_HLPP2.gap), (_java_key_9 := Code04_HLPP2.dis[i]), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))), _java_old_10)[4]
                    Code04_HLPP2.cur[i] = jcast('int', Code04_HLPP2.head[i])
                i = jcast('int', (i + 1))
        else:
            lowest = jcast('int', jcast('int', (jcast('int', (Code04_HLPP2.n << (1 & 31))) - 1)))
            e = jcast('int', Code04_HLPP2.head[u])
            while (e > 0):
                v = jcast('int', Code04_HLPP2.to[e])
                if ((u != v) and (Code04_HLPP2.limit[e] > 0)):
                    lowest = jcast('int', jstatic('Math', 'min', lowest, Code04_HLPP2.dis[v]))
                e = jcast('int', Code04_HLPP2.nxt[e])
            ((_java_obj_11 := Code04_HLPP2.gap), (_java_key_12 := Code04_HLPP2.dis[u]), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (-1)))), _java_old_13)[4]
            Code04_HLPP2.dis[u] = jcast('int', jcast('int', jadd(lowest, 1)))
            ((_java_obj_14 := Code04_HLPP2.gap), (_java_key_15 := Code04_HLPP2.dis[u]), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))), _java_old_16)[4]
            Code04_HLPP2.cur[u] = jcast('int', Code04_HLPP2.head[u])

    @staticmethod
    def discharge(s, t):
        s = jcast('int', s)
        t = jcast('int', t)
        u = jcast('int', Code04_HLPP2.bucket[Code04_HLPP2.highest])
        Code04_HLPP2.bucket[Code04_HLPP2.highest] = jcast('int', Code04_HLPP2.nextActive[u])
        while (Code04_HLPP2.excess[u] > 0):
            e = jcast('int', Code04_HLPP2.cur[u])
            while (e > 0):
                Code04_HLPP2.cur[u] = jcast('int', e)
                v = jcast('int', Code04_HLPP2.to[e])
                lim = jcast('int', Code04_HLPP2.limit[e])
                if ((Code04_HLPP2.dis[u] == jcast('int', jadd(Code04_HLPP2.dis[v], 1))) and (lim > 0)):
                    if (((v != s) and (v != t)) and (Code04_HLPP2.excess[v] == 0)):
                        Code04_HLPP2.addActive(v)
                    Code04_HLPP2.pushFlow(u, v, e, jstatic('Math', 'min', Code04_HLPP2.excess[u], lim))
                    if (Code04_HLPP2.excess[u] == 0):
                        return
                e = jcast('int', Code04_HLPP2.nxt[e])
            Code04_HLPP2.relabel(u, s, t)

    @staticmethod
    def maxflow(s, t):
        s = jcast('int', s)
        t = jcast('int', t)
        Code04_HLPP2.bfs(t)
        if (Code04_HLPP2.dis[s] == jcast('int', jadd(Code04_HLPP2.n, 1))):
            return jcast('long', 0)
        Code04_HLPP2.dis[s] = jcast('int', Code04_HLPP2.n)
        i = jcast('int', 1)
        while (i <= Code04_HLPP2.n):
            ((_java_obj_17 := Code04_HLPP2.gap), (_java_key_18 := Code04_HLPP2.dis[i]), (_java_old_19 := jget(_java_obj_17, _java_key_18)), jset(_java_obj_17, _java_key_18, jcast('int', (_java_old_19 + (1)))), _java_old_19)[4]
            i = jcast('int', (i + 1))
        e = jcast('int', Code04_HLPP2.head[s])
        while (e > 0):
            v = jcast('int', Code04_HLPP2.to[e])
            if (Code04_HLPP2.dis[v] < Code04_HLPP2.n):
                Code04_HLPP2.pushFlow(s, v, e, Code04_HLPP2.limit[e])
            e = jcast('int', Code04_HLPP2.nxt[e])
        i = jcast('int', 0)
        while (i <= jcast('int', (Code04_HLPP2.n << (1 & 31)))):
            Code04_HLPP2.bucket[i] = jcast('int', 0)
            i = jcast('int', (i + 1))
        Code04_HLPP2.highest = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= Code04_HLPP2.n):
            if (((i != s) and (i != t)) and (Code04_HLPP2.excess[i] > 0)):
                Code04_HLPP2.addActive(i)
            i = jcast('int', (i + 1))
        while (Code04_HLPP2.highest >= 0):
            if (Code04_HLPP2.bucket[Code04_HLPP2.highest] == 0):
                Code04_HLPP2.highest = jcast('int', (Code04_HLPP2.highest - 1))
            else:
                Code04_HLPP2.discharge(s, t)
        return jcast('long', Code04_HLPP2.excess[t])

    @staticmethod
    def main(args):
        in_ = Code04_HLPP2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_HLPP2.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_HLPP2.m = jcast('int', jcall(in_, 'nextInt'))
        s = jcast('int', jcall(in_, 'nextInt'))
        t = jcast('int', jcall(in_, 'nextInt'))
        Code04_HLPP2.cntg = jcast('int', 1)
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i <= Code04_HLPP2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code04_HLPP2.addEdge(u, v, w)
            Code04_HLPP2.addEdge(v, u, 0)
            i = jcast('int', (i + 1))
        ans = jcast('long', Code04_HLPP2.maxflow(s, t))
        jcall(out, 'println', ans)
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len', 'in': 'in_'}
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        def _java_init_0(self, in_):
            self.in_ = in_

        def readByte(self):
            if (self.ptr >= self.len):
                self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
                self.ptr = jcast('int', 0)
                if (self.len <= 0):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', self.buffer[((_java_obj_20 := self), (_java_key_21 := 'ptr'), (_java_old_22 := jget(_java_obj_20, _java_key_21)), jset(_java_obj_20, _java_key_21, jcast('int', (_java_old_22 + (1)))), _java_old_22)[4]])

        def nextInt(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('int', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('int', (jcast('int', (-val)) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_HLPP2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_HLPP2.MAXN = jcast('int', 1201)
Code04_HLPP2.MAXM = jcast('int', 120001)
Code04_HLPP2.n = jcast('int', 0)
Code04_HLPP2.m = jcast('int', 0)
Code04_HLPP2.head = jarray('int', [Code04_HLPP2.MAXN])
Code04_HLPP2.nxt = jarray('int', [jcast('int', (Code04_HLPP2.MAXM << (1 & 31)))])
Code04_HLPP2.to = jarray('int', [jcast('int', (Code04_HLPP2.MAXM << (1 & 31)))])
Code04_HLPP2.limit = jarray('int', [jcast('int', (Code04_HLPP2.MAXM << (1 & 31)))])
Code04_HLPP2.cntg = jcast('int', 0)
Code04_HLPP2.excess = jarray('long', [Code04_HLPP2.MAXN])
Code04_HLPP2.dis = jarray('int', [Code04_HLPP2.MAXN])
Code04_HLPP2.que = jarray('int', [Code04_HLPP2.MAXN])
Code04_HLPP2.cur = jarray('int', [Code04_HLPP2.MAXN])
Code04_HLPP2.gap = jarray('int', [jcast('int', (Code04_HLPP2.MAXN << (1 & 31)))])
Code04_HLPP2.bucket = jarray('int', [jcast('int', (Code04_HLPP2.MAXN << (1 & 31)))])
Code04_HLPP2.nextActive = jarray('int', [Code04_HLPP2.MAXN])
Code04_HLPP2.highest = jcast('int', 0)

if __name__ == '__main__':
    Code04_HLPP2.main([])
