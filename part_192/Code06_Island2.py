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

# 岛屿，Python版
# 图中有n个点、n条无向边，每条边有边权
# 图中可能有多个连通块，保证每个连通块都是一棵基环树
# 对每个连通块，计算点不重复的路径能得到的最大边权和，即基环树直径
# 图中每棵基环树的直径累加起来，打印这个结果
# 2 <= n <= 10^6
# 1 <= 边权 <= 10^8
# 测试链接 : https://www.luogu.com.cn/problem/P4381
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_Island2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'dfn': 'dfn', 'cntd': 'cntd', 'fromNode': 'fromNode', 'fromWeight': 'fromWeight', 'cycle': 'cycle', 'arr': 'arr', 'val': 'val', 'cnta': 'cnta', 'dist': 'dist', 'diameter': 'diameter', 'sum': 'sum', 'height': 'height', 'que': 'que', 'stau': 'stau', 'stas': 'stas', 'stae': 'stae', 'stacksize': 'stacksize', 'u': 'u', 'status': 'status', 'e': 'e'}
    MAXN = 0
    n = 0
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    dfn = None
    cntd = 0
    fromNode = None
    fromWeight = None
    cycle = None
    arr = None
    val = None
    cnta = 0
    dist = None
    diameter = 0
    sum = None
    height = None
    que = None
    # 递归改迭代需要的栈
    stau = None
    stas = None
    stae = None
    stacksize = 0
    u = 0
    status = 0
    e = 0
    @staticmethod
    def push(u, status, e):
        u = jcast('int', u)
        status = jcast('int', status)
        e = jcast('int', e)
        Code06_Island2.stau[Code06_Island2.stacksize] = jcast('int', u)
        Code06_Island2.stas[Code06_Island2.stacksize] = jcast('int', status)
        Code06_Island2.stae[Code06_Island2.stacksize] = jcast('int', e)
        Code06_Island2.stacksize = jcast('int', (Code06_Island2.stacksize + 1))

    @staticmethod
    def pop():
        Code06_Island2.stacksize = jcast('int', (Code06_Island2.stacksize - 1))
        Code06_Island2.u = jcast('int', Code06_Island2.stau[Code06_Island2.stacksize])
        Code06_Island2.status = jcast('int', Code06_Island2.stas[Code06_Island2.stacksize])
        Code06_Island2.e = jcast('int', Code06_Island2.stae[Code06_Island2.stacksize])

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code06_Island2.nxt, ((_java_obj_1 := Code06_Island2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_Island2.head[u])
        Code06_Island2.to[Code06_Island2.cntg] = jcast('int', v)
        Code06_Island2.weight[Code06_Island2.cntg] = jcast('int', w)
        Code06_Island2.head[u] = jcast('int', Code06_Island2.cntg)

    # 递归版
    @staticmethod
    def dfs1(u):
        u = jcast('int', u)
        jset(Code06_Island2.dfn, u, ((_java_obj_4 := Code06_Island2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        e = jcast('int', Code06_Island2.head[u])
        while (e > 0):
            v = jcast('int', Code06_Island2.to[e])
            if (Code06_Island2.dfn[v] == 0):
                Code06_Island2.fromNode[v] = jcast('int', u)
                Code06_Island2.fromWeight[v] = jcast('int', Code06_Island2.weight[e])
                Code06_Island2.dfs1(v)
            else:
                if (Code06_Island2.dfn[u] < Code06_Island2.dfn[v]):
                    Code06_Island2.cycle[u] = jcast('boolean', True)
                    jset(Code06_Island2.arr, ((_java_obj_7 := Code06_Island2), (_java_key_8 := 'cnta'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
                    Code06_Island2.val[Code06_Island2.cnta] = jcast('int', Code06_Island2.weight[e])
                    i = jcast('int', v)
                    while (i != u):
                        Code06_Island2.cycle[i] = jcast('boolean', True)
                        jset(Code06_Island2.arr, ((_java_obj_10 := Code06_Island2), (_java_key_11 := 'cnta'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], i)
                        Code06_Island2.val[Code06_Island2.cnta] = jcast('int', Code06_Island2.fromWeight[i])
                        i = jcast('int', Code06_Island2.fromNode[i])
            e = jcast('int', Code06_Island2.nxt[e])

    # 迭代版
    @staticmethod
    def dfs2(cur):
        cur = jcast('int', cur)
        Code06_Island2.stacksize = jcast('int', 0)
        Code06_Island2.push(cur, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code06_Island2.stacksize > 0):
            Code06_Island2.pop()
            if (Code06_Island2.status == jcast('int', (-1))):
                jset(Code06_Island2.dfn, Code06_Island2.u, ((_java_obj_13 := Code06_Island2), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
                Code06_Island2.e = jcast('int', Code06_Island2.head[Code06_Island2.u])
            else:
                v = jcast('int', Code06_Island2.to[Code06_Island2.e])
                if ((Code06_Island2.status == 1) and (Code06_Island2.dfn[Code06_Island2.u] < Code06_Island2.dfn[v])):
                    Code06_Island2.cycle[Code06_Island2.u] = jcast('boolean', True)
                    jset(Code06_Island2.arr, ((_java_obj_16 := Code06_Island2), (_java_key_17 := 'cnta'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code06_Island2.u)
                    Code06_Island2.val[Code06_Island2.cnta] = jcast('int', Code06_Island2.weight[Code06_Island2.e])
                    i = jcast('int', v)
                    while (i != Code06_Island2.u):
                        Code06_Island2.cycle[i] = jcast('boolean', True)
                        jset(Code06_Island2.arr, ((_java_obj_19 := Code06_Island2), (_java_key_20 := 'cnta'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], i)
                        Code06_Island2.val[Code06_Island2.cnta] = jcast('int', Code06_Island2.fromWeight[i])
                        i = jcast('int', Code06_Island2.fromNode[i])
                Code06_Island2.e = jcast('int', Code06_Island2.nxt[Code06_Island2.e])
            if (Code06_Island2.e != 0):
                v = jcast('int', Code06_Island2.to[Code06_Island2.e])
                if (Code06_Island2.dfn[v] == 0):
                    Code06_Island2.push(Code06_Island2.u, 0, Code06_Island2.e)
                    Code06_Island2.fromNode[v] = jcast('int', Code06_Island2.u)
                    Code06_Island2.fromWeight[v] = jcast('int', Code06_Island2.weight[Code06_Island2.e])
                    Code06_Island2.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code06_Island2.push(Code06_Island2.u, 1, Code06_Island2.e)

    @staticmethod
    def dpOnTree(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        e = jcast('int', Code06_Island2.head[u])
        while (e > 0):
            v = jcast('int', Code06_Island2.to[e])
            w = jcast('int', Code06_Island2.weight[e])
            if ((v != fa) and (not Code06_Island2.cycle[v])):
                Code06_Island2.dpOnTree(v, u)
                Code06_Island2.diameter = jcast('long', jstatic('Math', 'max', Code06_Island2.diameter, jcast('long', jadd(jcast('long', jadd(Code06_Island2.dist[u], Code06_Island2.dist[v])), w))))
                jset(Code06_Island2.dist, u, jstatic('Math', 'max', Code06_Island2.dist[u], jcast('long', jadd(Code06_Island2.dist[v], w))))
            e = jcast('int', Code06_Island2.nxt[e])

    @staticmethod
    def compute(root):
        root = jcast('int', root)
        Code06_Island2.cnta = jcast('int', 0)
        # dfs1(root);
        Code06_Island2.dfs2(root)
        Code06_Island2.sum[1] = jcast('long', 0)
        i = jcast('int', 2)
        j = jcast('int', 1)
        while (j <= Code06_Island2.cnta):
            Code06_Island2.sum[i] = jcast('long', Code06_Island2.val[j])
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        i = jcast('int', jcast('int', jadd(Code06_Island2.cnta, 2)))
        while (i <= jcast('int', (Code06_Island2.cnta * 2))):
            Code06_Island2.sum[i] = jcast('long', Code06_Island2.sum[jcast('int', (i - Code06_Island2.cnta))])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= jcast('int', (Code06_Island2.cnta * 2))):
            Code06_Island2.sum[i] = jcast('long', jcast('long', jadd(Code06_Island2.sum[i], Code06_Island2.sum[jcast('int', (i - 1))])))
            i = jcast('int', (i + 1))
        ans1 = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code06_Island2.cnta):
            Code06_Island2.diameter = jcast('long', 0)
            Code06_Island2.dpOnTree(Code06_Island2.arr[i], 0)
            ans1 = jcast('long', jstatic('Math', 'max', ans1, Code06_Island2.diameter))
            Code06_Island2.height[i] = jcast('long', Code06_Island2.dist[Code06_Island2.arr[i]])
            Code06_Island2.height[jcast('int', jadd(i, Code06_Island2.cnta))] = jcast('long', Code06_Island2.height[i])
            i = jcast('int', (i + 1))
        ans2 = jcast('long', 0)
        ql = jcast('int', 1)
        qr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= jcast('int', (Code06_Island2.cnta * 2))):
            while ((ql <= qr) and (Code06_Island2.que[ql] <= jcast('int', (i - Code06_Island2.cnta)))):
                ql = jcast('int', (ql + 1))
            if (ql <= qr):
                ans2 = jcast('long', jstatic('Math', 'max', ans2, jcast('long', (jcast('long', jadd(jcast('long', jadd(Code06_Island2.height[i], Code06_Island2.height[Code06_Island2.que[ql]])), Code06_Island2.sum[i])) - Code06_Island2.sum[Code06_Island2.que[ql]]))))
            while ((ql <= qr) and (jcast('long', (Code06_Island2.height[Code06_Island2.que[qr]] - Code06_Island2.sum[Code06_Island2.que[qr]])) <= jcast('long', (Code06_Island2.height[i] - Code06_Island2.sum[i])))):
                qr = jcast('int', (qr - 1))
            jset(Code06_Island2.que, (qr := jcast('int', (qr + (1)))), i)
            i = jcast('int', (i + 1))
        return jcast('long', jstatic('Math', 'max', ans1, ans2))

    @staticmethod
    def main(args):
        in_ = Code06_Island2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_Island2.n = jcast('int', jcall(in_, 'nextInt'))
        u = jcast('int', 1)
        v = 0
        w = 0
        while (u <= Code06_Island2.n):
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code06_Island2.addEdge(u, v, w)
            Code06_Island2.addEdge(v, u, w)
            u = jcast('int', (u + 1))
        ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code06_Island2.n):
            if (Code06_Island2.dfn[i] == 0):
                ans = jcast('long', jcast('long', jadd(ans, Code06_Island2.compute(i))))
            i = jcast('int', (i + 1))
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
            return jcast('int', self.buffer[((_java_obj_22 := self), (_java_key_23 := 'ptr'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))), _java_old_24)[4]])

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
            raise TypeError("No matching overload for Code06_Island2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_Island2.MAXN = jcast('int', 1000001)
Code06_Island2.n = jcast('int', 0)
Code06_Island2.head = jarray('int', [Code06_Island2.MAXN])
Code06_Island2.nxt = jarray('int', [jcast('int', (Code06_Island2.MAXN << (1 & 31)))])
Code06_Island2.to = jarray('int', [jcast('int', (Code06_Island2.MAXN << (1 & 31)))])
Code06_Island2.weight = jarray('int', [jcast('int', (Code06_Island2.MAXN << (1 & 31)))])
Code06_Island2.cntg = jcast('int', 0)
Code06_Island2.dfn = jarray('int', [Code06_Island2.MAXN])
Code06_Island2.cntd = jcast('int', 0)
Code06_Island2.fromNode = jarray('int', [Code06_Island2.MAXN])
Code06_Island2.fromWeight = jarray('int', [Code06_Island2.MAXN])
Code06_Island2.cycle = jarray('boolean', [Code06_Island2.MAXN])
Code06_Island2.arr = jarray('int', [Code06_Island2.MAXN])
Code06_Island2.val = jarray('int', [Code06_Island2.MAXN])
Code06_Island2.cnta = jcast('int', 0)
Code06_Island2.dist = jarray('long', [Code06_Island2.MAXN])
Code06_Island2.diameter = jcast('long', 0)
Code06_Island2.sum = jarray('long', [jcast('int', (Code06_Island2.MAXN << (1 & 31)))])
Code06_Island2.height = jarray('long', [jcast('int', (Code06_Island2.MAXN << (1 & 31)))])
Code06_Island2.que = jarray('int', [jcast('int', (Code06_Island2.MAXN << (1 & 31)))])
Code06_Island2.stau = jarray('int', [Code06_Island2.MAXN])
Code06_Island2.stas = jarray('int', [Code06_Island2.MAXN])
Code06_Island2.stae = jarray('int', [Code06_Island2.MAXN])
Code06_Island2.stacksize = jcast('int', 0)
Code06_Island2.u = jcast('int', 0)
Code06_Island2.status = jcast('int', 0)
Code06_Island2.e = jcast('int', 0)

if __name__ == '__main__':
    Code06_Island2.main([])
