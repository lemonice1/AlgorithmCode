# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# Dinic算法，Python版
# 图中一共n个点，m条有向边，给定源点s和汇点t
# 给定每条有向边的起点、终点、容量
# 计算源点s到汇点t的网络最大流
# 1 <= n <= 200
# 1 <= m <= 5000
# 边的容量为非负整数
# 测试链接 : https://www.luogu.com.cn/problem/P3376
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Dinic1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'INF': 'INF', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'limit': 'limit', 'cntg': 'cntg', 'dis': 'dis', 'que': 'que', 'cur': 'cur'}
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
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code02_Dinic1.nxt, ((_java_obj_1 := Code02_Dinic1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_Dinic1.head[u])
        Code02_Dinic1.to[Code02_Dinic1.cntg] = jcast('int', v)
        Code02_Dinic1.limit[Code02_Dinic1.cntg] = jcast('int', w)
        Code02_Dinic1.head[u] = jcast('int', Code02_Dinic1.cntg)

    @staticmethod
    def bfs(s):
        s = jcast('int', s)
        i = jcast('int', 1)
        while (i <= Code02_Dinic1.n):
            Code02_Dinic1.dis[i] = jcast('int', Code02_Dinic1.n)
            Code02_Dinic1.cur[i] = jcast('int', Code02_Dinic1.head[i])
            i = jcast('int', (i + 1))
        Code02_Dinic1.dis[s] = jcast('int', 0)
        l = jcast('int', 1)
        r = jcast('int', 0)
        jset(Code02_Dinic1.que, (r := jcast('int', (r + (1)))), s)
        while (l <= r):
            u = jcast('int', Code02_Dinic1.que[((_java_old_4 := l), (l := jcast('int', (l + (1)))), _java_old_4)[2]])
            e = jcast('int', Code02_Dinic1.head[u])
            while (e > 0):
                v = jcast('int', Code02_Dinic1.to[e])
                lim = jcast('int', Code02_Dinic1.limit[e])
                if ((Code02_Dinic1.dis[v] == Code02_Dinic1.n) and (lim > 0)):
                    Code02_Dinic1.dis[v] = jcast('int', jcast('int', jadd(Code02_Dinic1.dis[u], 1)))
                    jset(Code02_Dinic1.que, (r := jcast('int', (r + (1)))), v)
                e = jcast('int', Code02_Dinic1.nxt[e])

    @staticmethod
    def dfs(u, rest, t):
        u = jcast('int', u)
        rest = jcast('long', rest)
        t = jcast('int', t)
        if (u == t):
            return jcast('long', rest)
        flow = jcast('long', 0)
        e = jcast('int', Code02_Dinic1.cur[u])
        while ((e > 0) and (rest > 0)):
            Code02_Dinic1.cur[u] = jcast('int', e)
            v = jcast('int', Code02_Dinic1.to[e])
            c = jcast('long', jstatic('Math', 'min', rest, Code02_Dinic1.limit[e]))
            if ((jcast('int', jadd(Code02_Dinic1.dis[u], 1)) == Code02_Dinic1.dis[v]) and (c > 0)):
                k = jcast('long', Code02_Dinic1.dfs(v, c, t))
                flow = jcast('long', jcast('long', jadd(flow, k)))
                rest = jcast('long', jcast('long', (rest - k)))
                Code02_Dinic1.limit[e] = jcast('int', jcast('long', (Code02_Dinic1.limit[e] - k)))
                Code02_Dinic1.limit[jcast('int', (e ^ 1))] = jcast('int', jcast('long', jadd(Code02_Dinic1.limit[jcast('int', (e ^ 1))], k)))
            e = jcast('int', Code02_Dinic1.nxt[e])
        # 死点剪枝
        if (flow == 0):
            Code02_Dinic1.dis[u] = jcast('int', Code02_Dinic1.n)
        return jcast('long', flow)

    @staticmethod
    def maxflow(s, t):
        s = jcast('int', s)
        t = jcast('int', t)
        ans = jcast('long', 0)
        Code02_Dinic1.bfs(s)
        while (Code02_Dinic1.dis[t] != Code02_Dinic1.n):
            ans = jcast('long', jcast('long', jadd(ans, Code02_Dinic1.dfs(s, Code02_Dinic1.INF, t))))
            Code02_Dinic1.bfs(s)
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code02_Dinic1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_Dinic1.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_Dinic1.m = jcast('int', jcall(in_, 'nextInt'))
        s = jcast('int', jcall(in_, 'nextInt'))
        t = jcast('int', jcall(in_, 'nextInt'))
        Code02_Dinic1.cntg = jcast('int', 1)
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i <= Code02_Dinic1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code02_Dinic1.addEdge(u, v, w)
            Code02_Dinic1.addEdge(v, u, 0)
            i = jcast('int', (i + 1))
        ans = jcast('long', Code02_Dinic1.maxflow(s, t))
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
            return jcast('int', self.buffer[((_java_obj_5 := self), (_java_key_6 := 'ptr'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))), _java_old_7)[4]])

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
            raise TypeError("No matching overload for Code02_Dinic1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Dinic1.MAXN = jcast('int', 201)
Code02_Dinic1.MAXM = jcast('int', 5001)
Code02_Dinic1.INF = jcast('long', jcast('long', (1 << (60 & 63))))
Code02_Dinic1.n = jcast('int', 0)
Code02_Dinic1.m = jcast('int', 0)
Code02_Dinic1.head = jarray('int', [Code02_Dinic1.MAXN])
Code02_Dinic1.nxt = jarray('int', [jcast('int', (Code02_Dinic1.MAXM << (1 & 31)))])
Code02_Dinic1.to = jarray('int', [jcast('int', (Code02_Dinic1.MAXM << (1 & 31)))])
Code02_Dinic1.limit = jarray('int', [jcast('int', (Code02_Dinic1.MAXM << (1 & 31)))])
Code02_Dinic1.cntg = jcast('int', 0)
Code02_Dinic1.dis = jarray('int', [Code02_Dinic1.MAXN])
Code02_Dinic1.que = jarray('int', [Code02_Dinic1.MAXN])
Code02_Dinic1.cur = jarray('int', [Code02_Dinic1.MAXN])

if __name__ == '__main__':
    Code02_Dinic1.main([])
