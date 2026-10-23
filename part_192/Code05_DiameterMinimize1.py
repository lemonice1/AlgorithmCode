# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 树直径最小化，Python版
# 图中有n个点、n条无向边，每条边有边权，图是一棵基环树
# 可以任意删掉环上的一条边，让图变成树，希望让树的直径最小
# 第一个测试链接，计算树的直径最小值
# 第二个测试链接，等价于计算树的直径最小值 / 2，结果保留一位小数
# 1 <= n <= 2 * 10^5
# 1 <= 边权 <= 10^9
# 测试链接 : https://codeforces.com/problemset/problem/835/F
# 测试链接 : https://www.luogu.com.cn/problem/P1399
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_DiameterMinimize1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'dfn': 'dfn', 'cntd': 'cntd', 'fromNode': 'fromNode', 'fromWeight': 'fromWeight', 'cycle': 'cycle', 'arr': 'arr', 'val': 'val', 'cnta': 'cnta', 'dist': 'dist', 'diameter': 'diameter', 'height': 'height', 'preMax': 'preMax', 'preDiameter': 'preDiameter', 'sufMax': 'sufMax', 'sufDiameter': 'sufDiameter', 'stau': 'stau', 'stas': 'stas', 'stae': 'stae', 'stacksize': 'stacksize', 'u': 'u', 'status': 'status', 'e': 'e'}
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
    height = None
    preMax = None
    preDiameter = None
    sufMax = None
    sufDiameter = None
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
        Code05_DiameterMinimize1.stau[Code05_DiameterMinimize1.stacksize] = jcast('int', u)
        Code05_DiameterMinimize1.stas[Code05_DiameterMinimize1.stacksize] = jcast('int', status)
        Code05_DiameterMinimize1.stae[Code05_DiameterMinimize1.stacksize] = jcast('int', e)
        Code05_DiameterMinimize1.stacksize = jcast('int', (Code05_DiameterMinimize1.stacksize + 1))

    @staticmethod
    def pop():
        Code05_DiameterMinimize1.stacksize = jcast('int', (Code05_DiameterMinimize1.stacksize - 1))
        Code05_DiameterMinimize1.u = jcast('int', Code05_DiameterMinimize1.stau[Code05_DiameterMinimize1.stacksize])
        Code05_DiameterMinimize1.status = jcast('int', Code05_DiameterMinimize1.stas[Code05_DiameterMinimize1.stacksize])
        Code05_DiameterMinimize1.e = jcast('int', Code05_DiameterMinimize1.stae[Code05_DiameterMinimize1.stacksize])

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code05_DiameterMinimize1.nxt, ((_java_obj_1 := Code05_DiameterMinimize1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_DiameterMinimize1.head[u])
        Code05_DiameterMinimize1.to[Code05_DiameterMinimize1.cntg] = jcast('int', v)
        Code05_DiameterMinimize1.weight[Code05_DiameterMinimize1.cntg] = jcast('int', w)
        Code05_DiameterMinimize1.head[u] = jcast('int', Code05_DiameterMinimize1.cntg)

    # 递归版
    @staticmethod
    def dfs1(u):
        u = jcast('int', u)
        jset(Code05_DiameterMinimize1.dfn, u, ((_java_obj_4 := Code05_DiameterMinimize1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        e = jcast('int', Code05_DiameterMinimize1.head[u])
        while (e > 0):
            v = jcast('int', Code05_DiameterMinimize1.to[e])
            if (Code05_DiameterMinimize1.dfn[v] == 0):
                Code05_DiameterMinimize1.fromNode[v] = jcast('int', u)
                Code05_DiameterMinimize1.fromWeight[v] = jcast('int', Code05_DiameterMinimize1.weight[e])
                Code05_DiameterMinimize1.dfs1(v)
            else:
                if (Code05_DiameterMinimize1.dfn[u] < Code05_DiameterMinimize1.dfn[v]):
                    Code05_DiameterMinimize1.cycle[u] = jcast('boolean', True)
                    jset(Code05_DiameterMinimize1.arr, ((_java_obj_7 := Code05_DiameterMinimize1), (_java_key_8 := 'cnta'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
                    Code05_DiameterMinimize1.val[Code05_DiameterMinimize1.cnta] = jcast('int', Code05_DiameterMinimize1.weight[e])
                    i = jcast('int', v)
                    while (i != u):
                        Code05_DiameterMinimize1.cycle[i] = jcast('boolean', True)
                        jset(Code05_DiameterMinimize1.arr, ((_java_obj_10 := Code05_DiameterMinimize1), (_java_key_11 := 'cnta'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], i)
                        Code05_DiameterMinimize1.val[Code05_DiameterMinimize1.cnta] = jcast('int', Code05_DiameterMinimize1.fromWeight[i])
                        i = jcast('int', Code05_DiameterMinimize1.fromNode[i])
            e = jcast('int', Code05_DiameterMinimize1.nxt[e])

    # 迭代版
    @staticmethod
    def dfs2(cur):
        cur = jcast('int', cur)
        Code05_DiameterMinimize1.stacksize = jcast('int', 0)
        Code05_DiameterMinimize1.push(cur, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code05_DiameterMinimize1.stacksize > 0):
            Code05_DiameterMinimize1.pop()
            if (Code05_DiameterMinimize1.status == jcast('int', (-1))):
                jset(Code05_DiameterMinimize1.dfn, Code05_DiameterMinimize1.u, ((_java_obj_13 := Code05_DiameterMinimize1), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
                Code05_DiameterMinimize1.e = jcast('int', Code05_DiameterMinimize1.head[Code05_DiameterMinimize1.u])
            else:
                v = jcast('int', Code05_DiameterMinimize1.to[Code05_DiameterMinimize1.e])
                if ((Code05_DiameterMinimize1.status == 1) and (Code05_DiameterMinimize1.dfn[Code05_DiameterMinimize1.u] < Code05_DiameterMinimize1.dfn[v])):
                    Code05_DiameterMinimize1.cycle[Code05_DiameterMinimize1.u] = jcast('boolean', True)
                    jset(Code05_DiameterMinimize1.arr, ((_java_obj_16 := Code05_DiameterMinimize1), (_java_key_17 := 'cnta'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code05_DiameterMinimize1.u)
                    Code05_DiameterMinimize1.val[Code05_DiameterMinimize1.cnta] = jcast('int', Code05_DiameterMinimize1.weight[Code05_DiameterMinimize1.e])
                    i = jcast('int', v)
                    while (i != Code05_DiameterMinimize1.u):
                        Code05_DiameterMinimize1.cycle[i] = jcast('boolean', True)
                        jset(Code05_DiameterMinimize1.arr, ((_java_obj_19 := Code05_DiameterMinimize1), (_java_key_20 := 'cnta'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], i)
                        Code05_DiameterMinimize1.val[Code05_DiameterMinimize1.cnta] = jcast('int', Code05_DiameterMinimize1.fromWeight[i])
                        i = jcast('int', Code05_DiameterMinimize1.fromNode[i])
                Code05_DiameterMinimize1.e = jcast('int', Code05_DiameterMinimize1.nxt[Code05_DiameterMinimize1.e])
            if (Code05_DiameterMinimize1.e != 0):
                v = jcast('int', Code05_DiameterMinimize1.to[Code05_DiameterMinimize1.e])
                if (Code05_DiameterMinimize1.dfn[v] == 0):
                    Code05_DiameterMinimize1.push(Code05_DiameterMinimize1.u, 0, Code05_DiameterMinimize1.e)
                    Code05_DiameterMinimize1.fromNode[v] = jcast('int', Code05_DiameterMinimize1.u)
                    Code05_DiameterMinimize1.fromWeight[v] = jcast('int', Code05_DiameterMinimize1.weight[Code05_DiameterMinimize1.e])
                    Code05_DiameterMinimize1.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code05_DiameterMinimize1.push(Code05_DiameterMinimize1.u, 1, Code05_DiameterMinimize1.e)

    @staticmethod
    def dpOnTree(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        e = jcast('int', Code05_DiameterMinimize1.head[u])
        while (e > 0):
            v = jcast('int', Code05_DiameterMinimize1.to[e])
            w = jcast('int', Code05_DiameterMinimize1.weight[e])
            if ((v != fa) and (not Code05_DiameterMinimize1.cycle[v])):
                Code05_DiameterMinimize1.dpOnTree(v, u)
                Code05_DiameterMinimize1.diameter = jcast('long', jstatic('Math', 'max', Code05_DiameterMinimize1.diameter, jcast('long', jadd(jcast('long', jadd(Code05_DiameterMinimize1.dist[u], Code05_DiameterMinimize1.dist[v])), w))))
                jset(Code05_DiameterMinimize1.dist, u, jstatic('Math', 'max', Code05_DiameterMinimize1.dist[u], jcast('long', jadd(Code05_DiameterMinimize1.dist[v], w))))
            e = jcast('int', Code05_DiameterMinimize1.nxt[e])

    @staticmethod
    def dpOnCycle():
        best = jcast('long', 0)
        sum = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code05_DiameterMinimize1.cnta):
            jset(Code05_DiameterMinimize1.preMax, i, jstatic('Math', 'max', Code05_DiameterMinimize1.preMax[jcast('int', (i - 1))], jcast('long', jadd(Code05_DiameterMinimize1.height[i], sum))))
            jset(Code05_DiameterMinimize1.preDiameter, i, jstatic('Math', 'max', Code05_DiameterMinimize1.preDiameter[jcast('int', (i - 1))], jcast('long', jadd(jcast('long', jadd(sum, Code05_DiameterMinimize1.height[i])), best))))
            best = jcast('long', jstatic('Math', 'max', best, jcast('long', (Code05_DiameterMinimize1.height[i] - sum))))
            sum = jcast('long', jcast('long', jadd(sum, Code05_DiameterMinimize1.val[i])))
            i = jcast('int', (i + 1))
        Code05_DiameterMinimize1.sufMax[Code05_DiameterMinimize1.cnta] = jcast('long', jcast('long', jadd(Code05_DiameterMinimize1.height[Code05_DiameterMinimize1.cnta], Code05_DiameterMinimize1.val[Code05_DiameterMinimize1.cnta])))
        Code05_DiameterMinimize1.sufDiameter[Code05_DiameterMinimize1.cnta] = jcast('long', Code05_DiameterMinimize1.height[Code05_DiameterMinimize1.cnta])
        best = jcast('long', jcast('long', (Code05_DiameterMinimize1.height[Code05_DiameterMinimize1.cnta] - Code05_DiameterMinimize1.val[Code05_DiameterMinimize1.cnta])))
        sum = jcast('long', jcast('int', jadd(Code05_DiameterMinimize1.val[Code05_DiameterMinimize1.cnta], Code05_DiameterMinimize1.val[jcast('int', (Code05_DiameterMinimize1.cnta - 1))])))
        i = jcast('int', jcast('int', (Code05_DiameterMinimize1.cnta - 1)))
        while (i >= 1):
            jset(Code05_DiameterMinimize1.sufMax, i, jstatic('Math', 'max', Code05_DiameterMinimize1.sufMax[jcast('int', jadd(i, 1))], jcast('long', jadd(Code05_DiameterMinimize1.height[i], sum))))
            jset(Code05_DiameterMinimize1.sufDiameter, i, jstatic('Math', 'max', Code05_DiameterMinimize1.sufDiameter[jcast('int', jadd(i, 1))], jcast('long', jadd(jcast('long', jadd(sum, Code05_DiameterMinimize1.height[i])), best))))
            best = jcast('long', jstatic('Math', 'max', best, jcast('long', (Code05_DiameterMinimize1.height[i] - sum))))
            sum = jcast('long', jcast('long', jadd(sum, Code05_DiameterMinimize1.val[jcast('int', (i - 1))])))
            i = jcast('int', (i - 1))
        ans = jcast('long', jget(Long, 'MAX_VALUE'))
        i = jcast('int', 1)
        while (i < Code05_DiameterMinimize1.cnta):
            ans = jcast('long', jstatic('Math', 'min', ans, jstatic('Math', 'max', jcast('long', jadd(Code05_DiameterMinimize1.preMax[i], Code05_DiameterMinimize1.sufMax[jcast('int', jadd(i, 1))])), jstatic('Math', 'max', Code05_DiameterMinimize1.preDiameter[i], Code05_DiameterMinimize1.sufDiameter[jcast('int', jadd(i, 1))]))))
            i = jcast('int', (i + 1))
        ans = jcast('long', jstatic('Math', 'min', ans, Code05_DiameterMinimize1.preDiameter[Code05_DiameterMinimize1.cnta]))
        return jcast('long', ans)

    @staticmethod
    def compute():
        # dfs1(1);
        Code05_DiameterMinimize1.dfs2(1)
        ans1 = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code05_DiameterMinimize1.cnta):
            Code05_DiameterMinimize1.diameter = jcast('long', 0)
            Code05_DiameterMinimize1.dpOnTree(Code05_DiameterMinimize1.arr[i], 0)
            ans1 = jcast('long', jstatic('Math', 'max', ans1, Code05_DiameterMinimize1.diameter))
            Code05_DiameterMinimize1.height[i] = jcast('long', Code05_DiameterMinimize1.dist[Code05_DiameterMinimize1.arr[i]])
            i = jcast('int', (i + 1))
        ans2 = jcast('long', Code05_DiameterMinimize1.dpOnCycle())
        return jcast('long', jstatic('Math', 'max', ans1, ans2))

    @staticmethod
    def main(args):
        in_ = Code05_DiameterMinimize1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_DiameterMinimize1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i <= Code05_DiameterMinimize1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code05_DiameterMinimize1.addEdge(u, v, w)
            Code05_DiameterMinimize1.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        ans = jcast('long', Code05_DiameterMinimize1.compute())
        # 王国道路，CF835F，使用如下打印
        jcall(out, 'println', ans)
        # 快餐店，洛谷P1399，使用如下打印
        # out.printf("%.1f\n", (double) ans / 2.0);
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
            raise TypeError("No matching overload for Code05_DiameterMinimize1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_DiameterMinimize1.MAXN = jcast('int', 200001)
Code05_DiameterMinimize1.n = jcast('int', 0)
Code05_DiameterMinimize1.head = jarray('int', [Code05_DiameterMinimize1.MAXN])
Code05_DiameterMinimize1.nxt = jarray('int', [jcast('int', (Code05_DiameterMinimize1.MAXN << (1 & 31)))])
Code05_DiameterMinimize1.to = jarray('int', [jcast('int', (Code05_DiameterMinimize1.MAXN << (1 & 31)))])
Code05_DiameterMinimize1.weight = jarray('int', [jcast('int', (Code05_DiameterMinimize1.MAXN << (1 & 31)))])
Code05_DiameterMinimize1.cntg = jcast('int', 0)
Code05_DiameterMinimize1.dfn = jarray('int', [Code05_DiameterMinimize1.MAXN])
Code05_DiameterMinimize1.cntd = jcast('int', 0)
Code05_DiameterMinimize1.fromNode = jarray('int', [Code05_DiameterMinimize1.MAXN])
Code05_DiameterMinimize1.fromWeight = jarray('int', [Code05_DiameterMinimize1.MAXN])
Code05_DiameterMinimize1.cycle = jarray('boolean', [Code05_DiameterMinimize1.MAXN])
Code05_DiameterMinimize1.arr = jarray('int', [Code05_DiameterMinimize1.MAXN])
Code05_DiameterMinimize1.val = jarray('int', [Code05_DiameterMinimize1.MAXN])
Code05_DiameterMinimize1.cnta = jcast('int', 0)
Code05_DiameterMinimize1.dist = jarray('long', [Code05_DiameterMinimize1.MAXN])
Code05_DiameterMinimize1.diameter = jcast('long', 0)
Code05_DiameterMinimize1.height = jarray('long', [Code05_DiameterMinimize1.MAXN])
Code05_DiameterMinimize1.preMax = jarray('long', [Code05_DiameterMinimize1.MAXN])
Code05_DiameterMinimize1.preDiameter = jarray('long', [Code05_DiameterMinimize1.MAXN])
Code05_DiameterMinimize1.sufMax = jarray('long', [Code05_DiameterMinimize1.MAXN])
Code05_DiameterMinimize1.sufDiameter = jarray('long', [Code05_DiameterMinimize1.MAXN])
Code05_DiameterMinimize1.stau = jarray('int', [Code05_DiameterMinimize1.MAXN])
Code05_DiameterMinimize1.stas = jarray('int', [Code05_DiameterMinimize1.MAXN])
Code05_DiameterMinimize1.stae = jarray('int', [Code05_DiameterMinimize1.MAXN])
Code05_DiameterMinimize1.stacksize = jcast('int', 0)
Code05_DiameterMinimize1.u = jcast('int', 0)
Code05_DiameterMinimize1.status = jcast('int', 0)
Code05_DiameterMinimize1.e = jcast('int', 0)

if __name__ == '__main__':
    Code05_DiameterMinimize1.main([])
