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

# 丁香之路，Python版
# 一共有n个点，点i和点j的距离为|i - j|，所以这是完全图，边是无向边
# 给定m个点对，每个点对(a, b)，保证 a != b，表示a和b之间的无向边做了标记
# 给定起点s，不管终点是什么，每条被标记的无向边，走过至少一次
# 打印起点s，终点i的情况下，走过路程的最小距离是多少
# 终点i可以是1~n中的任意一点，所以一共打印n个数值
# 1 <= n <= 2500
# m <= n个顶点的完全图的边数
# 测试链接 : https://www.luogu.com.cn/problem/P6628
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code11_DingXiangRoad2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 's': 's', 'a': 'a', 'b': 'b', 'fix': 'fix', 'nodeSet': 'nodeSet', 'nodeArr': 'nodeArr', 'cnt': 'cnt', 'fa1': 'fa1', 'deg1': 'deg1', 'fa2': 'fa2', 'deg2': 'deg2', 'edgeArr': 'edgeArr', 'sum': 'sum'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    s = 0
    a = None
    b = None
    fix = None
    nodeSet = None
    nodeArr = None
    cnt = 0
    fa1 = None
    deg1 = None
    fa2 = None
    deg2 = None
    # u、v、w
    edgeArr = None
    sum = 0
    class EdgeCmp:
        __java_fields__ = {}
        def compare(self, e1, e2):
            if (e1[2] != e2[2]):
                return jcast('int', jcast('int', (e1[2] - e2[2])))
            if (e1[0] != e2[0]):
                return jcast('int', jcast('int', (e1[0] - e2[0])))
            return jcast('int', jcast('int', (e1[1] - e2[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def dist(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('int', jstatic('Math', 'abs', jcast('int', (x - y))))

    @staticmethod
    def find(fa, x):
        x = jcast('int', x)
        if (x != fa[x]):
            jset(fa, x, Code11_DingXiangRoad2.find(fa, fa[x]))
        return jcast('int', fa[x])

    @staticmethod
    def union(fa, x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code11_DingXiangRoad2.find(fa, x))
        fy = jcast('int', Code11_DingXiangRoad2.find(fa, y))
        if (fx != fy):
            fa[fx] = jcast('int', fy)

    @staticmethod
    def kruskal():
        cost = jcast('long', 0)
        edgeCnt = jcast('int', jcast('int', (Code11_DingXiangRoad2.cnt - 1)))
        jstatic('Arrays', 'sort', Code11_DingXiangRoad2.edgeArr, 1, jcast('int', jadd(edgeCnt, 1)), Code11_DingXiangRoad2.EdgeCmp())
        i = jcast('int', 1)
        while (i <= edgeCnt):
            u = jcast('int', Code11_DingXiangRoad2.edgeArr[i][0])
            v = jcast('int', Code11_DingXiangRoad2.edgeArr[i][1])
            w = jcast('int', Code11_DingXiangRoad2.edgeArr[i][2])
            if (Code11_DingXiangRoad2.find(Code11_DingXiangRoad2.fa2, u) != Code11_DingXiangRoad2.find(Code11_DingXiangRoad2.fa2, v)):
                cost = jcast('long', jcast('long', jadd(cost, jcast('int', (w * 2)))))
                Code11_DingXiangRoad2.union(Code11_DingXiangRoad2.fa2, u, v)
            i = jcast('int', (i + 1))
        return jcast('long', cost)

    @staticmethod
    def compute(start, end):
        start = jcast('int', start)
        end = jcast('int', end)
        Code11_DingXiangRoad2.cnt = jcast('int', 0)
        for x in Code11_DingXiangRoad2.nodeSet:
            jset(Code11_DingXiangRoad2.nodeArr, ((_java_obj_1 := Code11_DingXiangRoad2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], x)
        i = jcast('int', 1)
        while (i <= Code11_DingXiangRoad2.n):
            jset(Code11_DingXiangRoad2.fa2, i, Code11_DingXiangRoad2.find(Code11_DingXiangRoad2.fa1, i))
            Code11_DingXiangRoad2.deg2[i] = jcast('int', Code11_DingXiangRoad2.deg1[i])
            i = jcast('int', (i + 1))
        ans = jcast('long', Code11_DingXiangRoad2.sum)
        Code11_DingXiangRoad2.deg2[start] = jcast('int', (Code11_DingXiangRoad2.deg2[start] + 1))
        Code11_DingXiangRoad2.deg2[end] = jcast('int', (Code11_DingXiangRoad2.deg2[end] + 1))
        Code11_DingXiangRoad2.union(Code11_DingXiangRoad2.fa2, start, end)
        i = jcast('int', 1)
        p = jcast('int', 0)
        while (i <= Code11_DingXiangRoad2.cnt):
            if (jcast('int', (Code11_DingXiangRoad2.deg2[Code11_DingXiangRoad2.nodeArr[i]] & 1)) == 1):
                if (p == 0):
                    p = jcast('int', i)
                else:
                    ans = jcast('long', jcast('long', jadd(ans, Code11_DingXiangRoad2.dist(Code11_DingXiangRoad2.nodeArr[p], Code11_DingXiangRoad2.nodeArr[i]))))
                    while (p < i):
                        Code11_DingXiangRoad2.union(Code11_DingXiangRoad2.fa2, Code11_DingXiangRoad2.nodeArr[((_java_old_4 := p), (p := jcast('int', (p + (1)))), _java_old_4)[2]], Code11_DingXiangRoad2.nodeArr[i])
                    p = jcast('int', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= jcast('int', (Code11_DingXiangRoad2.cnt - 1))):
            jset(Code11_DingXiangRoad2.edgeArr[i], 0, Code11_DingXiangRoad2.nodeArr[i])
            jset(Code11_DingXiangRoad2.edgeArr[i], 1, Code11_DingXiangRoad2.nodeArr[jcast('int', jadd(i, 1))])
            jset(Code11_DingXiangRoad2.edgeArr[i], 2, jcast('int', (Code11_DingXiangRoad2.nodeArr[jcast('int', jadd(i, 1))] - Code11_DingXiangRoad2.nodeArr[i])))
            i = jcast('int', (i + 1))
        ans = jcast('long', jcast('long', jadd(ans, Code11_DingXiangRoad2.kruskal())))
        return jcast('long', ans)

    @staticmethod
    def prepare():
        Code11_DingXiangRoad2.fix[Code11_DingXiangRoad2.s] = jcast('boolean', True)
        jcall(Code11_DingXiangRoad2.nodeSet, 'add', Code11_DingXiangRoad2.s)
        Code11_DingXiangRoad2.sum = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code11_DingXiangRoad2.n):
            Code11_DingXiangRoad2.fa1[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code11_DingXiangRoad2.m):
            u = jcast('int', Code11_DingXiangRoad2.a[i])
            v = jcast('int', Code11_DingXiangRoad2.b[i])
            Code11_DingXiangRoad2.deg1[u] = jcast('int', (Code11_DingXiangRoad2.deg1[u] + 1))
            Code11_DingXiangRoad2.deg1[v] = jcast('int', (Code11_DingXiangRoad2.deg1[v] + 1))
            Code11_DingXiangRoad2.fix[u] = jcast('boolean', True)
            Code11_DingXiangRoad2.fix[v] = jcast('boolean', True)
            jcall(Code11_DingXiangRoad2.nodeSet, 'add', u)
            jcall(Code11_DingXiangRoad2.nodeSet, 'add', v)
            Code11_DingXiangRoad2.union(Code11_DingXiangRoad2.fa1, u, v)
            Code11_DingXiangRoad2.sum = jcast('long', jcast('long', jadd(Code11_DingXiangRoad2.sum, Code11_DingXiangRoad2.dist(u, v))))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code11_DingXiangRoad2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code11_DingXiangRoad2.n = jcast('int', jcall(in_, 'nextInt'))
        Code11_DingXiangRoad2.m = jcast('int', jcall(in_, 'nextInt'))
        Code11_DingXiangRoad2.s = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code11_DingXiangRoad2.m):
            jset(Code11_DingXiangRoad2.a, i, jcall(in_, 'nextInt'))
            jset(Code11_DingXiangRoad2.b, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code11_DingXiangRoad2.prepare()
        i = jcast('int', 1)
        while (i <= Code11_DingXiangRoad2.n):
            if (not Code11_DingXiangRoad2.fix[i]):
                jcall(Code11_DingXiangRoad2.nodeSet, 'add', i)
            jcall(out, 'print', jadd(Code11_DingXiangRoad2.compute(Code11_DingXiangRoad2.s, i), ' '))
            if (not Code11_DingXiangRoad2.fix[i]):
                jcall(Code11_DingXiangRoad2.nodeSet, 'remove', i)
            i = jcast('int', (i + 1))
        jcall(out, 'println')
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
            raise TypeError("No matching overload for Code11_DingXiangRoad2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code11_DingXiangRoad2.MAXN = jcast('int', 3001)
Code11_DingXiangRoad2.MAXM = jcast('int', 3000001)
Code11_DingXiangRoad2.n = jcast('int', 0)
Code11_DingXiangRoad2.m = jcast('int', 0)
Code11_DingXiangRoad2.s = jcast('int', 0)
Code11_DingXiangRoad2.a = jarray('int', [Code11_DingXiangRoad2.MAXM])
Code11_DingXiangRoad2.b = jarray('int', [Code11_DingXiangRoad2.MAXM])
Code11_DingXiangRoad2.fix = jarray('boolean', [Code11_DingXiangRoad2.MAXN])
Code11_DingXiangRoad2.nodeSet = jnew('TreeSet')
Code11_DingXiangRoad2.nodeArr = jarray('int', [Code11_DingXiangRoad2.MAXN])
Code11_DingXiangRoad2.cnt = jcast('int', 0)
Code11_DingXiangRoad2.fa1 = jarray('int', [Code11_DingXiangRoad2.MAXN])
Code11_DingXiangRoad2.deg1 = jarray('int', [Code11_DingXiangRoad2.MAXN])
Code11_DingXiangRoad2.fa2 = jarray('int', [Code11_DingXiangRoad2.MAXN])
Code11_DingXiangRoad2.deg2 = jarray('int', [Code11_DingXiangRoad2.MAXN])
Code11_DingXiangRoad2.edgeArr = jarray('int', [Code11_DingXiangRoad2.MAXN, 3])
Code11_DingXiangRoad2.sum = jcast('long', 0)

if __name__ == '__main__':
    Code11_DingXiangRoad2.main([])
