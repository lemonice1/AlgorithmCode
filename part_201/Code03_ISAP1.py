# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# ISAP算法，Python版
# 图中一共n个点，m条有向边，给定源点s和汇点t
# 给定每条有向边的起点、终点、容量
# 计算源点s到汇点t的网络最大流
# 1 <= n <= 200
# 1 <= m <= 5000
# 边的容量为非负整数
# 测试链接 : https://www.luogu.com.cn/problem/P3376
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_ISAP1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'INF': 'INF', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'limit': 'limit', 'cntg': 'cntg', 'dis': 'dis', 'que': 'que', 'cur': 'cur', 'gap': 'gap'}
    MAXN = 0
    MAXM = 0
    INF = 0
    n = 0
    m = 0
    head = None
    nxt = None
    to = None
    limit = None
    cntg = 0
    dis = None
    que = None
    cur = None
    gap = None
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code03_ISAP1.nxt, ((_java_obj_1 := Code03_ISAP1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_ISAP1.head[u])
        Code03_ISAP1.to[Code03_ISAP1.cntg] = jcast('int', v)
        Code03_ISAP1.limit[Code03_ISAP1.cntg] = jcast('int', w)
        Code03_ISAP1.head[u] = jcast('int', Code03_ISAP1.cntg)

    @staticmethod
    def bfs(t):
        t = jcast('int', t)
        Code03_ISAP1.gap[0] = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code03_ISAP1.n):
            Code03_ISAP1.gap[i] = jcast('int', 0)
            Code03_ISAP1.dis[i] = jcast('int', Code03_ISAP1.n)
            Code03_ISAP1.cur[i] = jcast('int', Code03_ISAP1.head[i])
            i = jcast('int', (i + 1))
        Code03_ISAP1.dis[t] = jcast('int', 0)
        l = jcast('int', 1)
        r = jcast('int', 0)
        jset(Code03_ISAP1.que, (r := jcast('int', (r + (1)))), t)
        while (l <= r):
            u = jcast('int', Code03_ISAP1.que[((_java_old_4 := l), (l := jcast('int', (l + (1)))), _java_old_4)[2]])
            e = jcast('int', Code03_ISAP1.head[u])
            while (e > 0):
                v = jcast('int', Code03_ISAP1.to[e])
                if ((Code03_ISAP1.dis[v] == Code03_ISAP1.n) and (Code03_ISAP1.limit[jcast('int', (e ^ 1))] > 0)):
                    Code03_ISAP1.dis[v] = jcast('int', jcast('int', jadd(Code03_ISAP1.dis[u], 1)))
                    jset(Code03_ISAP1.que, (r := jcast('int', (r + (1)))), v)
                e = jcast('int', Code03_ISAP1.nxt[e])
        i = jcast('int', 1)
        while (i <= Code03_ISAP1.n):
            ((_java_obj_5 := Code03_ISAP1.gap), (_java_key_6 := Code03_ISAP1.dis[i]), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))), _java_old_7)[4]
            i = jcast('int', (i + 1))

    @staticmethod
    def dfs(u, rest, s, t):
        u = jcast('int', u)
        rest = jcast('long', rest)
        s = jcast('int', s)
        t = jcast('int', t)
        if (u == t):
            return jcast('long', rest)
        flow = jcast('long', 0)
        e = jcast('int', Code03_ISAP1.cur[u])
        while ((e > 0) and (rest > 0)):
            Code03_ISAP1.cur[u] = jcast('int', e)
            v = jcast('int', Code03_ISAP1.to[e])
            c = jcast('long', jstatic('Math', 'min', rest, Code03_ISAP1.limit[e]))
            if ((Code03_ISAP1.dis[u] == jcast('int', jadd(Code03_ISAP1.dis[v], 1))) and (c > 0)):
                k = jcast('long', Code03_ISAP1.dfs(v, c, s, t))
                flow = jcast('long', jcast('long', jadd(flow, k)))
                rest = jcast('long', jcast('long', (rest - k)))
                Code03_ISAP1.limit[e] = jcast('int', jcast('long', (Code03_ISAP1.limit[e] - k)))
                Code03_ISAP1.limit[jcast('int', (e ^ 1))] = jcast('int', jcast('long', jadd(Code03_ISAP1.limit[jcast('int', (e ^ 1))], k)))
                if (Code03_ISAP1.dis[s] == Code03_ISAP1.n):
                    return jcast('long', flow)
            e = jcast('int', Code03_ISAP1.nxt[e])
        if (rest > 0):
            if (((_java_obj_8 := Code03_ISAP1.gap), (_java_key_9 := Code03_ISAP1.dis[u]), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (-1)))))[3] > 0):
                Code03_ISAP1.dis[u] = jcast('int', (Code03_ISAP1.dis[u] + 1))
                ((_java_obj_11 := Code03_ISAP1.gap), (_java_key_12 := Code03_ISAP1.dis[u]), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]
                Code03_ISAP1.cur[u] = jcast('int', Code03_ISAP1.head[u])
            else:
                Code03_ISAP1.dis[s] = jcast('int', Code03_ISAP1.n)
        return jcast('long', flow)

    @staticmethod
    def maxflow(s, t):
        s = jcast('int', s)
        t = jcast('int', t)
        ans = jcast('long', 0)
        Code03_ISAP1.bfs(t)
        while (Code03_ISAP1.dis[s] != Code03_ISAP1.n):
            ans = jcast('long', jcast('long', jadd(ans, Code03_ISAP1.dfs(s, Code03_ISAP1.INF, s, t))))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code03_ISAP1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_ISAP1.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_ISAP1.m = jcast('int', jcall(in_, 'nextInt'))
        s = jcast('int', jcall(in_, 'nextInt'))
        t = jcast('int', jcall(in_, 'nextInt'))
        Code03_ISAP1.cntg = jcast('int', 1)
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i <= Code03_ISAP1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code03_ISAP1.addEdge(u, v, w)
            Code03_ISAP1.addEdge(v, u, 0)
            i = jcast('int', (i + 1))
        ans = jcast('long', Code03_ISAP1.maxflow(s, t))
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
            return jcast('int', self.buffer[((_java_obj_14 := self), (_java_key_15 := 'ptr'), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))), _java_old_16)[4]])

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
            raise TypeError("No matching overload for Code03_ISAP1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_ISAP1.MAXN = jcast('int', 201)
Code03_ISAP1.MAXM = jcast('int', 5001)
Code03_ISAP1.INF = jcast('long', jcast('long', (1 << (60 & 63))))
Code03_ISAP1.n = jcast('int', 0)
Code03_ISAP1.m = jcast('int', 0)
Code03_ISAP1.head = jarray('int', [Code03_ISAP1.MAXN])
Code03_ISAP1.nxt = jarray('int', [jcast('int', (Code03_ISAP1.MAXM << (1 & 31)))])
Code03_ISAP1.to = jarray('int', [jcast('int', (Code03_ISAP1.MAXM << (1 & 31)))])
Code03_ISAP1.limit = jarray('int', [jcast('int', (Code03_ISAP1.MAXM << (1 & 31)))])
Code03_ISAP1.cntg = jcast('int', 0)
Code03_ISAP1.dis = jarray('int', [Code03_ISAP1.MAXN])
Code03_ISAP1.que = jarray('int', [Code03_ISAP1.MAXN])
Code03_ISAP1.cur = jarray('int', [Code03_ISAP1.MAXN])
Code03_ISAP1.gap = jarray('int', [Code03_ISAP1.MAXN])

if __name__ == '__main__':
    Code03_ISAP1.main([])
