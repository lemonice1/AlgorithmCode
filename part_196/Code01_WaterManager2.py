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

# 水管局长，Python版
# 一共n个点、m条无向边，给定每条边的两个端点和边权
# 接下来有q条操作，每条操作是如下两种类型中的一种
# 操作 1 x y : 打印点x到点y的所有路径中，最大边权的最小值
# 操作 2 x y : 删除点x和点y之间的直接边，该边一定存在
# 题目保证任何时刻图都连通，并且无重边无自环
# 1 <= n <= 10^3
# 1 <= m、q <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4172
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_WaterManager2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'q': 'q', 'ex': 'ex', 'ey': 'ey', 'ew': 'ew', 'qop': 'qop', 'qx': 'qx', 'qy': 'qy', 'father': 'father', 'deleted': 'deleted', 'edgeMap': 'edgeMap', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'rev': 'rev', 'sta': 'sta', 'maxEdge': 'maxEdge', 'ans': 'ans'}
    MAXN = 0
    n = 0
    m = 0
    q = 0
    ex = None
    ey = None
    ew = None
    qop = None
    qx = None
    qy = None
    # 并查集
    father = None
    # 时光倒流加边
    deleted = None
    edgeMap = None
    # 辅助splay
    fa = None
    ls = None
    rs = None
    rev = None
    sta = None
    # maxEdge[x]表示以x为根的辅助splay中，权值最大的边的编号
    maxEdge = None
    ans = None
    @staticmethod
    def find(x):
        x = jcast('int', x)
        if (x != Code01_WaterManager2.father[x]):
            jset(Code01_WaterManager2.father, x, Code01_WaterManager2.find(Code01_WaterManager2.father[x]))
        return jcast('int', Code01_WaterManager2.father[x])

    # 手撸双指针快排，根据边权从小到大排序
    @staticmethod
    def sort(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', Code01_WaterManager2.ew[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        tmp = 0
        while (i <= j):
            while (Code01_WaterManager2.ew[i] < pivot):
                i = jcast('int', (i + 1))
            while (Code01_WaterManager2.ew[j] > pivot):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', Code01_WaterManager2.ex[i])
                Code01_WaterManager2.ex[i] = jcast('int', Code01_WaterManager2.ex[j])
                Code01_WaterManager2.ex[j] = jcast('int', tmp)
                tmp = jcast('int', Code01_WaterManager2.ey[i])
                Code01_WaterManager2.ey[i] = jcast('int', Code01_WaterManager2.ey[j])
                Code01_WaterManager2.ey[j] = jcast('int', tmp)
                tmp = jcast('int', Code01_WaterManager2.ew[i])
                Code01_WaterManager2.ew[i] = jcast('int', Code01_WaterManager2.ew[j])
                Code01_WaterManager2.ew[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code01_WaterManager2.sort(l, j)
        Code01_WaterManager2.sort(i, r)

    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code01_WaterManager2.maxEdge[x] = jcast('int', (0 if (x <= Code01_WaterManager2.n) else jcast('int', (x - Code01_WaterManager2.n))))
        if (Code01_WaterManager2.ew[Code01_WaterManager2.maxEdge[Code01_WaterManager2.ls[x]]] > Code01_WaterManager2.ew[Code01_WaterManager2.maxEdge[x]]):
            Code01_WaterManager2.maxEdge[x] = jcast('int', Code01_WaterManager2.maxEdge[Code01_WaterManager2.ls[x]])
        if (Code01_WaterManager2.ew[Code01_WaterManager2.maxEdge[Code01_WaterManager2.rs[x]]] > Code01_WaterManager2.ew[Code01_WaterManager2.maxEdge[x]]):
            Code01_WaterManager2.maxEdge[x] = jcast('int', Code01_WaterManager2.maxEdge[Code01_WaterManager2.rs[x]])

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code01_WaterManager2.ls[Code01_WaterManager2.fa[x]] != x) and (Code01_WaterManager2.rs[Code01_WaterManager2.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code01_WaterManager2.ls[Code01_WaterManager2.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code01_WaterManager2.ls[x])
            Code01_WaterManager2.ls[x] = jcast('int', Code01_WaterManager2.rs[x])
            Code01_WaterManager2.rs[x] = jcast('int', tmp)
            Code01_WaterManager2.rev[x] = jcast('boolean', (not Code01_WaterManager2.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code01_WaterManager2.rev[x]:
            Code01_WaterManager2.reverse(Code01_WaterManager2.ls[x])
            Code01_WaterManager2.reverse(Code01_WaterManager2.rs[x])
            Code01_WaterManager2.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code01_WaterManager2.fa[x])
        g = jcast('int', Code01_WaterManager2.fa[f])
        if (Code01_WaterManager2.lr(x) == 0):
            Code01_WaterManager2.ls[f] = jcast('int', Code01_WaterManager2.rs[x])
            if (Code01_WaterManager2.ls[f] != 0):
                jset(Code01_WaterManager2.fa, Code01_WaterManager2.ls[f], f)
            Code01_WaterManager2.rs[x] = jcast('int', f)
        else:
            Code01_WaterManager2.rs[f] = jcast('int', Code01_WaterManager2.ls[x])
            if (Code01_WaterManager2.rs[f] != 0):
                jset(Code01_WaterManager2.fa, Code01_WaterManager2.rs[f], f)
            Code01_WaterManager2.ls[x] = jcast('int', f)
        if (not Code01_WaterManager2.isroot(f)):
            if (Code01_WaterManager2.lr(f) == 0):
                Code01_WaterManager2.ls[g] = jcast('int', x)
            else:
                Code01_WaterManager2.rs[g] = jcast('int', x)
        Code01_WaterManager2.fa[f] = jcast('int', x)
        Code01_WaterManager2.fa[x] = jcast('int', g)
        Code01_WaterManager2.up(f)
        Code01_WaterManager2.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code01_WaterManager2.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code01_WaterManager2.isroot(y)):
            jset(Code01_WaterManager2.sta, (siz := jcast('int', (siz + (1)))), Code01_WaterManager2.fa[y])
            y = jcast('int', Code01_WaterManager2.fa[y])
        while (siz != 0):
            Code01_WaterManager2.down(Code01_WaterManager2.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code01_WaterManager2.isroot(x)):
            f = jcast('int', Code01_WaterManager2.fa[x])
            if (not Code01_WaterManager2.isroot(f)):
                if (Code01_WaterManager2.lr(x) == Code01_WaterManager2.lr(f)):
                    Code01_WaterManager2.rotate(f)
                else:
                    Code01_WaterManager2.rotate(x)
            Code01_WaterManager2.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code01_WaterManager2.splay(x)
            Code01_WaterManager2.rs[x] = jcast('int', y)
            Code01_WaterManager2.up(x)
            y = jcast('int', x)
            x = jcast('int', Code01_WaterManager2.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code01_WaterManager2.access(x)
        Code01_WaterManager2.splay(x)
        Code01_WaterManager2.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code01_WaterManager2.access(x)
        Code01_WaterManager2.splay(x)
        Code01_WaterManager2.down(x)
        while (Code01_WaterManager2.ls[x] != 0):
            x = jcast('int', Code01_WaterManager2.ls[x])
            Code01_WaterManager2.down(x)
        Code01_WaterManager2.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code01_WaterManager2.makeroot(x)
        Code01_WaterManager2.access(y)
        Code01_WaterManager2.splay(y)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code01_WaterManager2.makeroot(x)
        if (Code01_WaterManager2.findroot(y) != x):
            Code01_WaterManager2.fa[x] = jcast('int', y)

    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code01_WaterManager2.makeroot(x)
        if ((((Code01_WaterManager2.findroot(y) == x) and (Code01_WaterManager2.fa[y] == x)) and (Code01_WaterManager2.ls[y] == 0)) and (Code01_WaterManager2.rs[x] == y)):
            jset(Code01_WaterManager2.fa, y, jset(Code01_WaterManager2.rs, x, 0))
            Code01_WaterManager2.up(x)

    @staticmethod
    def key(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        a = jcast('int', jstatic('Math', 'min', x, y))
        b = jcast('int', jstatic('Math', 'max', x, y))
        return jcast('long', jcast('long', (jcast('long', (jcast('long', a) << (32 & 63))) | b)))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code01_WaterManager2.n):
            Code01_WaterManager2.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        Code01_WaterManager2.sort(1, Code01_WaterManager2.m)
        i = jcast('int', 1)
        while (i <= Code01_WaterManager2.m):
            jcall(Code01_WaterManager2.edgeMap, 'put', Code01_WaterManager2.key(Code01_WaterManager2.ex[i], Code01_WaterManager2.ey[i]), i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_WaterManager2.q):
            if (Code01_WaterManager2.qop[i] == 2):
                jset(Code01_WaterManager2.deleted, jcall(Code01_WaterManager2.edgeMap, 'get', Code01_WaterManager2.key(Code01_WaterManager2.qx[i], Code01_WaterManager2.qy[i])), True)
            i = jcast('int', (i + 1))
        edgeCnt = jcast('int', 0)
        i = jcast('int', 1)
        while ((i <= Code01_WaterManager2.m) and (edgeCnt != jcast('int', (Code01_WaterManager2.n - 1)))):
            if (not Code01_WaterManager2.deleted[i]):
                x = jcast('int', Code01_WaterManager2.ex[i])
                y = jcast('int', Code01_WaterManager2.ey[i])
                fx = jcast('int', Code01_WaterManager2.find(x))
                fy = jcast('int', Code01_WaterManager2.find(y))
                if (fx != fy):
                    Code01_WaterManager2.father[fx] = jcast('int', fy)
                    Code01_WaterManager2.link(x, jcast('int', jadd(Code01_WaterManager2.n, i)))
                    Code01_WaterManager2.link(y, jcast('int', jadd(Code01_WaterManager2.n, i)))
                    edgeCnt = jcast('int', (edgeCnt + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(e):
        e = jcast('int', e)
        Code01_WaterManager2.split(Code01_WaterManager2.ex[e], Code01_WaterManager2.ey[e])
        maxe = jcast('int', Code01_WaterManager2.maxEdge[Code01_WaterManager2.ey[e]])
        if (Code01_WaterManager2.ew[e] < Code01_WaterManager2.ew[maxe]):
            Code01_WaterManager2.cut(Code01_WaterManager2.ex[maxe], jcast('int', jadd(Code01_WaterManager2.n, maxe)))
            Code01_WaterManager2.cut(Code01_WaterManager2.ey[maxe], jcast('int', jadd(Code01_WaterManager2.n, maxe)))
            Code01_WaterManager2.link(Code01_WaterManager2.ex[e], jcast('int', jadd(Code01_WaterManager2.n, e)))
            Code01_WaterManager2.link(Code01_WaterManager2.ey[e], jcast('int', jadd(Code01_WaterManager2.n, e)))

    @staticmethod
    def main(args):
        in_ = Code01_WaterManager2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_WaterManager2.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_WaterManager2.m = jcast('int', jcall(in_, 'nextInt'))
        Code01_WaterManager2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_WaterManager2.m):
            jset(Code01_WaterManager2.ex, i, jcall(in_, 'nextInt'))
            jset(Code01_WaterManager2.ey, i, jcall(in_, 'nextInt'))
            jset(Code01_WaterManager2.ew, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_WaterManager2.q):
            jset(Code01_WaterManager2.qop, i, jcall(in_, 'nextInt'))
            jset(Code01_WaterManager2.qx, i, jcall(in_, 'nextInt'))
            jset(Code01_WaterManager2.qy, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code01_WaterManager2.prepare()
        i = jcast('int', Code01_WaterManager2.q)
        while (i >= 1):
            if (Code01_WaterManager2.qop[i] == 1):
                Code01_WaterManager2.split(Code01_WaterManager2.qx[i], Code01_WaterManager2.qy[i])
                Code01_WaterManager2.ans[i] = jcast('int', Code01_WaterManager2.ew[Code01_WaterManager2.maxEdge[Code01_WaterManager2.qy[i]]])
            else:
                Code01_WaterManager2.addEdge(jcall(Code01_WaterManager2.edgeMap, 'get', Code01_WaterManager2.key(Code01_WaterManager2.qx[i], Code01_WaterManager2.qy[i])))
            i = jcast('int', (i - 1))
        i = jcast('int', 1)
        while (i <= Code01_WaterManager2.q):
            if (Code01_WaterManager2.qop[i] == 1):
                jcall(out, 'println', Code01_WaterManager2.ans[i])
            i = jcast('int', (i + 1))
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
            return jcast('int', self.buffer[((_java_obj_2 := self), (_java_key_3 := 'ptr'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))), _java_old_4)[4]])

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
            raise TypeError("No matching overload for Code01_WaterManager2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_WaterManager2.MAXN = jcast('int', 200001)
Code01_WaterManager2.n = jcast('int', 0)
Code01_WaterManager2.m = jcast('int', 0)
Code01_WaterManager2.q = jcast('int', 0)
Code01_WaterManager2.ex = jarray('int', [Code01_WaterManager2.MAXN])
Code01_WaterManager2.ey = jarray('int', [Code01_WaterManager2.MAXN])
Code01_WaterManager2.ew = jarray('int', [Code01_WaterManager2.MAXN])
Code01_WaterManager2.qop = jarray('int', [Code01_WaterManager2.MAXN])
Code01_WaterManager2.qx = jarray('int', [Code01_WaterManager2.MAXN])
Code01_WaterManager2.qy = jarray('int', [Code01_WaterManager2.MAXN])
Code01_WaterManager2.father = jarray('int', [Code01_WaterManager2.MAXN])
Code01_WaterManager2.deleted = jarray('boolean', [Code01_WaterManager2.MAXN])
Code01_WaterManager2.edgeMap = jnew('HashMap')
Code01_WaterManager2.fa = jarray('int', [Code01_WaterManager2.MAXN])
Code01_WaterManager2.ls = jarray('int', [Code01_WaterManager2.MAXN])
Code01_WaterManager2.rs = jarray('int', [Code01_WaterManager2.MAXN])
Code01_WaterManager2.rev = jarray('boolean', [Code01_WaterManager2.MAXN])
Code01_WaterManager2.sta = jarray('int', [Code01_WaterManager2.MAXN])
Code01_WaterManager2.maxEdge = jarray('int', [Code01_WaterManager2.MAXN])
Code01_WaterManager2.ans = jarray('int', [Code01_WaterManager2.MAXN])

if __name__ == '__main__':
    Code01_WaterManager2.main([])
