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

# 网络，Python版
# 无向图中有n个点，点有点权，有m条边，边有颜色，颜色总数量为C，颜色的数值0 ~ C-1
# 无向图保证没有重边和自环，并且始终满足如下两个性质
# 性质1，对于任意节点连出去的边中，相同颜色的边不超过两条
# 性质2，图中不存在同色的环，指相同颜色的边构成的环
# 一共有q条操作，类型如下
# 操作 0 x y   : 点x的点权变成y
# 操作 2 c x y : 颜色c的边构成的图中，打印x到y路径上的点权最大值，不连通打印-1
# 操作 1 x y c : 点x到点y的直接边，颜色改成c，下面是具体说明
# 若修改后不满足性质1，不修改边的颜色，打印 "Error 1.”
# 若修改后不满足性质2，不修改边的颜色，打印 "Error 2."
# 若同时不满足性质1和性质2，优先打印 "Error 1."
# 若不存在直接边，不修改边的颜色，打印 "No such edge."
# 若上述情况都没出现，那么修改边的颜色，打印 "Success."
# 1 <= n <= 10^4
# C <= 10
# 1 <= m、q <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P2173
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_Network2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'C': 'C', 'q': 'q', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'sta': 'sta', 'rev': 'rev', 'arr': 'arr', 'maxv': 'maxv', 'nodeDegree': 'nodeDegree', 'edgeColor': 'edgeColor'}
    MAXN = 0
    n = 0
    m = 0
    C = 0
    q = 0
    fa = None
    ls = None
    rs = None
    sta = None
    rev = None
    arr = None
    maxv = None
    nodeDegree = None
    edgeColor = None
    @staticmethod
    def up(x):
        x = jcast('int', x)
        jset(Code07_Network2.maxv, x, jstatic('Math', 'max', jstatic('Math', 'max', Code07_Network2.maxv[Code07_Network2.ls[x]], Code07_Network2.maxv[Code07_Network2.rs[x]]), Code07_Network2.arr[x]))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code07_Network2.ls[Code07_Network2.fa[x]] != x) and (Code07_Network2.rs[Code07_Network2.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code07_Network2.ls[Code07_Network2.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code07_Network2.ls[x])
            Code07_Network2.ls[x] = jcast('int', Code07_Network2.rs[x])
            Code07_Network2.rs[x] = jcast('int', tmp)
            Code07_Network2.rev[x] = jcast('boolean', (not Code07_Network2.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code07_Network2.rev[x]:
            Code07_Network2.reverse(Code07_Network2.ls[x])
            Code07_Network2.reverse(Code07_Network2.rs[x])
            Code07_Network2.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code07_Network2.fa[x])
        g = jcast('int', Code07_Network2.fa[f])
        if (Code07_Network2.lr(x) == 0):
            Code07_Network2.ls[f] = jcast('int', Code07_Network2.rs[x])
            if (Code07_Network2.ls[f] != 0):
                jset(Code07_Network2.fa, Code07_Network2.ls[f], f)
            Code07_Network2.rs[x] = jcast('int', f)
        else:
            Code07_Network2.rs[f] = jcast('int', Code07_Network2.ls[x])
            if (Code07_Network2.rs[f] != 0):
                jset(Code07_Network2.fa, Code07_Network2.rs[f], f)
            Code07_Network2.ls[x] = jcast('int', f)
        if (not Code07_Network2.isroot(f)):
            if (Code07_Network2.lr(f) == 0):
                Code07_Network2.ls[g] = jcast('int', x)
            else:
                Code07_Network2.rs[g] = jcast('int', x)
        Code07_Network2.fa[f] = jcast('int', x)
        Code07_Network2.fa[x] = jcast('int', g)
        Code07_Network2.up(f)
        Code07_Network2.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code07_Network2.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code07_Network2.isroot(y)):
            jset(Code07_Network2.sta, (siz := jcast('int', (siz + (1)))), Code07_Network2.fa[y])
            y = jcast('int', Code07_Network2.fa[y])
        while (siz != 0):
            Code07_Network2.down(Code07_Network2.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code07_Network2.isroot(x)):
            f = jcast('int', Code07_Network2.fa[x])
            if (not Code07_Network2.isroot(f)):
                if (Code07_Network2.lr(x) == Code07_Network2.lr(f)):
                    Code07_Network2.rotate(f)
                else:
                    Code07_Network2.rotate(x)
            Code07_Network2.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code07_Network2.splay(x)
            Code07_Network2.rs[x] = jcast('int', y)
            Code07_Network2.up(x)
            y = jcast('int', x)
            x = jcast('int', Code07_Network2.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code07_Network2.access(x)
        Code07_Network2.splay(x)
        Code07_Network2.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code07_Network2.access(x)
        Code07_Network2.splay(x)
        Code07_Network2.down(x)
        while (Code07_Network2.ls[x] != 0):
            x = jcast('int', Code07_Network2.ls[x])
            Code07_Network2.down(x)
        Code07_Network2.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code07_Network2.makeroot(x)
        Code07_Network2.access(y)
        Code07_Network2.splay(y)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code07_Network2.makeroot(x)
        if (Code07_Network2.findroot(y) != x):
            Code07_Network2.fa[x] = jcast('int', y)

    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code07_Network2.makeroot(x)
        if ((((Code07_Network2.findroot(y) == x) and (Code07_Network2.fa[y] == x)) and (Code07_Network2.ls[y] == 0)) and (Code07_Network2.rs[x] == y)):
            jset(Code07_Network2.fa, y, jset(Code07_Network2.rs, x, 0))
            Code07_Network2.up(x)

    @staticmethod
    def node(c, x):
        c = jcast('int', c)
        x = jcast('int', x)
        return jcast('int', jcast('int', jadd(jcast('int', (c * Code07_Network2.n)), x)))

    @staticmethod
    def edge(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        a = jcast('int', jstatic('Math', 'min', x, y))
        b = jcast('int', jstatic('Math', 'max', x, y))
        return jcast('long', jcast('long', (jcast('long', (jcast('long', (1 * a)) << (32 & 63))) | b)))

    @staticmethod
    def connect(c, x, y):
        c = jcast('int', c)
        x = jcast('int', x)
        y = jcast('int', y)
        u = jcast('int', Code07_Network2.node(c, x))
        v = jcast('int', Code07_Network2.node(c, y))
        Code07_Network2.nodeDegree[u] = jcast('int', (Code07_Network2.nodeDegree[u] + 1))
        Code07_Network2.nodeDegree[v] = jcast('int', (Code07_Network2.nodeDegree[v] + 1))
        Code07_Network2.link(u, v)
        jcall(Code07_Network2.edgeColor, 'put', Code07_Network2.edge(x, y), c)

    @staticmethod
    def disconnect(c, x, y):
        c = jcast('int', c)
        x = jcast('int', x)
        y = jcast('int', y)
        u = jcast('int', Code07_Network2.node(c, x))
        v = jcast('int', Code07_Network2.node(c, y))
        Code07_Network2.nodeDegree[u] = jcast('int', (Code07_Network2.nodeDegree[u] - 1))
        Code07_Network2.nodeDegree[v] = jcast('int', (Code07_Network2.nodeDegree[v] - 1))
        Code07_Network2.cut(u, v)
        jcall(Code07_Network2.edgeColor, 'remove', Code07_Network2.edge(x, y))

    @staticmethod
    def updateNode(x, v):
        x = jcast('int', x)
        v = jcast('int', v)
        c = jcast('int', 0)
        while (c < Code07_Network2.C):
            cur = jcast('int', Code07_Network2.node(c, x))
            Code07_Network2.splay(cur)
            Code07_Network2.arr[cur] = jcast('int', v)
            Code07_Network2.up(cur)
            c = jcast('int', (c + 1))

    @staticmethod
    def updateEdge(x, y, c):
        x = jcast('int', x)
        y = jcast('int', y)
        c = jcast('int', c)
        pre = jcall(Code07_Network2.edgeColor, 'get', Code07_Network2.edge(x, y))
        if (pre == None):
            return jcast('int', 3)
        p = jcast('int', pre)
        if (p == c):
            return jcast('int', 4)
        if ((Code07_Network2.nodeDegree[Code07_Network2.node(c, x)] >= 2) or (Code07_Network2.nodeDegree[Code07_Network2.node(c, y)] >= 2)):
            return jcast('int', 1)
        if (Code07_Network2.findroot(Code07_Network2.node(c, x)) == Code07_Network2.findroot(Code07_Network2.node(c, y))):
            return jcast('int', 2)
        Code07_Network2.disconnect(p, x, y)
        Code07_Network2.connect(c, x, y)
        return jcast('int', 4)

    @staticmethod
    def query(c, x, y):
        c = jcast('int', c)
        x = jcast('int', x)
        y = jcast('int', y)
        u = jcast('int', Code07_Network2.node(c, x))
        v = jcast('int', Code07_Network2.node(c, y))
        if (Code07_Network2.findroot(u) != Code07_Network2.findroot(v)):
            return jcast('int', jcast('int', (-1)))
        Code07_Network2.split(u, v)
        return jcast('int', Code07_Network2.maxv[v])

    @staticmethod
    def main(args):
        in_ = Code07_Network2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_Network2.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_Network2.m = jcast('int', jcall(in_, 'nextInt'))
        Code07_Network2.C = jcast('int', jcall(in_, 'nextInt'))
        Code07_Network2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        v = 0
        while (i <= Code07_Network2.n):
            v = jcast('int', jcall(in_, 'nextInt'))
            c = jcast('int', 0)
            while (c < Code07_Network2.C):
                cur = jcast('int', Code07_Network2.node(c, i))
                Code07_Network2.arr[cur] = jcast('int', v)
                Code07_Network2.maxv[cur] = jcast('int', v)
                c = jcast('int', (c + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        x = 0
        y = 0
        c = 0
        while (i <= Code07_Network2.m):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            c = jcast('int', jcall(in_, 'nextInt'))
            Code07_Network2.connect(c, x, y)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        c = 0
        while (i <= Code07_Network2.q):
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 0):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                Code07_Network2.updateNode(x, y)
            else:
                if (op == 1):
                    x = jcast('int', jcall(in_, 'nextInt'))
                    y = jcast('int', jcall(in_, 'nextInt'))
                    c = jcast('int', jcall(in_, 'nextInt'))
                    ans = jcast('int', Code07_Network2.updateEdge(x, y, c))
                    if (ans == 1):
                        jcall(out, 'println', 'Error 1.')
                    if (ans == 2):
                        jcall(out, 'println', 'Error 2.')
                    if (ans == 3):
                        jcall(out, 'println', 'No such edge.')
                    if (ans == 4):
                        jcall(out, 'println', 'Success.')
                else:
                    c = jcast('int', jcall(in_, 'nextInt'))
                    x = jcast('int', jcall(in_, 'nextInt'))
                    y = jcast('int', jcall(in_, 'nextInt'))
                    jcall(out, 'println', Code07_Network2.query(c, x, y))
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
            raise TypeError("No matching overload for Code07_Network2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_Network2.MAXN = jcast('int', 100001)
Code07_Network2.n = jcast('int', 0)
Code07_Network2.m = jcast('int', 0)
Code07_Network2.C = jcast('int', 0)
Code07_Network2.q = jcast('int', 0)
Code07_Network2.fa = jarray('int', [Code07_Network2.MAXN])
Code07_Network2.ls = jarray('int', [Code07_Network2.MAXN])
Code07_Network2.rs = jarray('int', [Code07_Network2.MAXN])
Code07_Network2.sta = jarray('int', [Code07_Network2.MAXN])
Code07_Network2.rev = jarray('boolean', [Code07_Network2.MAXN])
Code07_Network2.arr = jarray('int', [Code07_Network2.MAXN])
Code07_Network2.maxv = jarray('int', [Code07_Network2.MAXN])
Code07_Network2.nodeDegree = jarray('int', [Code07_Network2.MAXN])
Code07_Network2.edgeColor = jnew('HashMap')

if __name__ == '__main__':
    Code07_Network2.main([])
