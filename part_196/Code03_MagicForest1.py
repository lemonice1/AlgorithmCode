# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 魔法森林，Python版
# 无向图有n个点、m条边，每条边有a、b两种权值，可能存在重边和自环
# 定义路径的代价为，路径上最大的a + 路径上最大的b
# 选择1号点到n号点的路径，打印路径代价的最小值，无法到达打印-1
# 2 <= n <= 5 * 10^4
# 0 <= m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P2387
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_MagicForest1:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'm': 'm', 'ex': 'ex', 'ey': 'ey', 'ea': 'ea', 'eb': 'eb', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'rev': 'rev', 'sta': 'sta', 'maxaEdge': 'maxaEdge', 'maxbEdge': 'maxbEdge'}
    MAXN = 0
    INF = 0
    n = 0
    m = 0
    ex = None
    ey = None
    ea = None
    eb = None
    fa = None
    ls = None
    rs = None
    rev = None
    sta = None
    # maxaEdge[x]表示以x为根的辅助splay中，最大a权值的边的编号
    maxaEdge = None
    # maxbEdge[x]表示以x为根的辅助splay中，最大b权值的边的编号
    maxbEdge = None
    # 手撸双指针快排，根据a权值从小到大排序
    @staticmethod
    def sort(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', Code03_MagicForest1.ea[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        tmp = 0
        while (i <= j):
            while (Code03_MagicForest1.ea[i] < pivot):
                i = jcast('int', (i + 1))
            while (Code03_MagicForest1.ea[j] > pivot):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', Code03_MagicForest1.ex[i])
                Code03_MagicForest1.ex[i] = jcast('int', Code03_MagicForest1.ex[j])
                Code03_MagicForest1.ex[j] = jcast('int', tmp)
                tmp = jcast('int', Code03_MagicForest1.ey[i])
                Code03_MagicForest1.ey[i] = jcast('int', Code03_MagicForest1.ey[j])
                Code03_MagicForest1.ey[j] = jcast('int', tmp)
                tmp = jcast('int', Code03_MagicForest1.ea[i])
                Code03_MagicForest1.ea[i] = jcast('int', Code03_MagicForest1.ea[j])
                Code03_MagicForest1.ea[j] = jcast('int', tmp)
                tmp = jcast('int', Code03_MagicForest1.eb[i])
                Code03_MagicForest1.eb[i] = jcast('int', Code03_MagicForest1.eb[j])
                Code03_MagicForest1.eb[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code03_MagicForest1.sort(l, j)
        Code03_MagicForest1.sort(i, r)

    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code03_MagicForest1.maxaEdge[x] = jcast('int', (0 if (x <= Code03_MagicForest1.n) else jcast('int', (x - Code03_MagicForest1.n))))
        if (Code03_MagicForest1.ea[Code03_MagicForest1.maxaEdge[Code03_MagicForest1.ls[x]]] > Code03_MagicForest1.ea[Code03_MagicForest1.maxaEdge[x]]):
            Code03_MagicForest1.maxaEdge[x] = jcast('int', Code03_MagicForest1.maxaEdge[Code03_MagicForest1.ls[x]])
        if (Code03_MagicForest1.ea[Code03_MagicForest1.maxaEdge[Code03_MagicForest1.rs[x]]] > Code03_MagicForest1.ea[Code03_MagicForest1.maxaEdge[x]]):
            Code03_MagicForest1.maxaEdge[x] = jcast('int', Code03_MagicForest1.maxaEdge[Code03_MagicForest1.rs[x]])
        Code03_MagicForest1.maxbEdge[x] = jcast('int', (0 if (x <= Code03_MagicForest1.n) else jcast('int', (x - Code03_MagicForest1.n))))
        if (Code03_MagicForest1.eb[Code03_MagicForest1.maxbEdge[Code03_MagicForest1.ls[x]]] > Code03_MagicForest1.eb[Code03_MagicForest1.maxbEdge[x]]):
            Code03_MagicForest1.maxbEdge[x] = jcast('int', Code03_MagicForest1.maxbEdge[Code03_MagicForest1.ls[x]])
        if (Code03_MagicForest1.eb[Code03_MagicForest1.maxbEdge[Code03_MagicForest1.rs[x]]] > Code03_MagicForest1.eb[Code03_MagicForest1.maxbEdge[x]]):
            Code03_MagicForest1.maxbEdge[x] = jcast('int', Code03_MagicForest1.maxbEdge[Code03_MagicForest1.rs[x]])

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code03_MagicForest1.ls[Code03_MagicForest1.fa[x]] != x) and (Code03_MagicForest1.rs[Code03_MagicForest1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code03_MagicForest1.ls[Code03_MagicForest1.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code03_MagicForest1.ls[x])
            Code03_MagicForest1.ls[x] = jcast('int', Code03_MagicForest1.rs[x])
            Code03_MagicForest1.rs[x] = jcast('int', tmp)
            Code03_MagicForest1.rev[x] = jcast('boolean', (not Code03_MagicForest1.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code03_MagicForest1.rev[x]:
            Code03_MagicForest1.reverse(Code03_MagicForest1.ls[x])
            Code03_MagicForest1.reverse(Code03_MagicForest1.rs[x])
            Code03_MagicForest1.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code03_MagicForest1.fa[x])
        g = jcast('int', Code03_MagicForest1.fa[f])
        if (Code03_MagicForest1.lr(x) == 0):
            Code03_MagicForest1.ls[f] = jcast('int', Code03_MagicForest1.rs[x])
            if (Code03_MagicForest1.ls[f] != 0):
                jset(Code03_MagicForest1.fa, Code03_MagicForest1.ls[f], f)
            Code03_MagicForest1.rs[x] = jcast('int', f)
        else:
            Code03_MagicForest1.rs[f] = jcast('int', Code03_MagicForest1.ls[x])
            if (Code03_MagicForest1.rs[f] != 0):
                jset(Code03_MagicForest1.fa, Code03_MagicForest1.rs[f], f)
            Code03_MagicForest1.ls[x] = jcast('int', f)
        if (not Code03_MagicForest1.isroot(f)):
            if (Code03_MagicForest1.lr(f) == 0):
                Code03_MagicForest1.ls[g] = jcast('int', x)
            else:
                Code03_MagicForest1.rs[g] = jcast('int', x)
        Code03_MagicForest1.fa[f] = jcast('int', x)
        Code03_MagicForest1.fa[x] = jcast('int', g)
        Code03_MagicForest1.up(f)
        Code03_MagicForest1.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code03_MagicForest1.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code03_MagicForest1.isroot(y)):
            jset(Code03_MagicForest1.sta, (siz := jcast('int', (siz + (1)))), Code03_MagicForest1.fa[y])
            y = jcast('int', Code03_MagicForest1.fa[y])
        while (siz != 0):
            Code03_MagicForest1.down(Code03_MagicForest1.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code03_MagicForest1.isroot(x)):
            f = jcast('int', Code03_MagicForest1.fa[x])
            if (not Code03_MagicForest1.isroot(f)):
                if (Code03_MagicForest1.lr(x) == Code03_MagicForest1.lr(f)):
                    Code03_MagicForest1.rotate(f)
                else:
                    Code03_MagicForest1.rotate(x)
            Code03_MagicForest1.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code03_MagicForest1.splay(x)
            Code03_MagicForest1.rs[x] = jcast('int', y)
            Code03_MagicForest1.up(x)
            y = jcast('int', x)
            x = jcast('int', Code03_MagicForest1.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code03_MagicForest1.access(x)
        Code03_MagicForest1.splay(x)
        Code03_MagicForest1.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code03_MagicForest1.access(x)
        Code03_MagicForest1.splay(x)
        Code03_MagicForest1.down(x)
        while (Code03_MagicForest1.ls[x] != 0):
            x = jcast('int', Code03_MagicForest1.ls[x])
            Code03_MagicForest1.down(x)
        Code03_MagicForest1.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code03_MagicForest1.makeroot(x)
        Code03_MagicForest1.access(y)
        Code03_MagicForest1.splay(y)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code03_MagicForest1.makeroot(x)
        if (Code03_MagicForest1.findroot(y) != x):
            Code03_MagicForest1.fa[x] = jcast('int', y)

    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code03_MagicForest1.makeroot(x)
        if ((((Code03_MagicForest1.findroot(y) == x) and (Code03_MagicForest1.fa[y] == x)) and (Code03_MagicForest1.ls[y] == 0)) and (Code03_MagicForest1.rs[x] == y)):
            jset(Code03_MagicForest1.fa, y, jset(Code03_MagicForest1.rs, x, 0))
            Code03_MagicForest1.up(x)

    @staticmethod
    def compute():
        Code03_MagicForest1.sort(1, Code03_MagicForest1.m)
        ans = jcast('int', Code03_MagicForest1.INF)
        i = jcast('int', 1)
        while (i <= Code03_MagicForest1.m):
            x = jcast('int', Code03_MagicForest1.ex[i])
            y = jcast('int', Code03_MagicForest1.ey[i])
            if (x != y):
                Code03_MagicForest1.makeroot(x)
                if (Code03_MagicForest1.findroot(y) != x):
                    Code03_MagicForest1.link(x, jcast('int', jadd(Code03_MagicForest1.n, i)))
                    Code03_MagicForest1.link(y, jcast('int', jadd(Code03_MagicForest1.n, i)))
                else:
                    Code03_MagicForest1.split(x, y)
                    pre = jcast('int', Code03_MagicForest1.maxbEdge[y])
                    if (Code03_MagicForest1.eb[i] < Code03_MagicForest1.eb[pre]):
                        Code03_MagicForest1.cut(Code03_MagicForest1.ex[pre], jcast('int', jadd(Code03_MagicForest1.n, pre)))
                        Code03_MagicForest1.cut(Code03_MagicForest1.ey[pre], jcast('int', jadd(Code03_MagicForest1.n, pre)))
                        Code03_MagicForest1.link(x, jcast('int', jadd(Code03_MagicForest1.n, i)))
                        Code03_MagicForest1.link(y, jcast('int', jadd(Code03_MagicForest1.n, i)))
            Code03_MagicForest1.makeroot(1)
            if (Code03_MagicForest1.findroot(Code03_MagicForest1.n) == 1):
                Code03_MagicForest1.split(1, Code03_MagicForest1.n)
                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(Code03_MagicForest1.ea[Code03_MagicForest1.maxaEdge[Code03_MagicForest1.n]], Code03_MagicForest1.eb[Code03_MagicForest1.maxbEdge[Code03_MagicForest1.n]]))))
            i = jcast('int', (i + 1))
        return jcast('int', (jcast('int', (-1)) if (ans == Code03_MagicForest1.INF) else ans))

    @staticmethod
    def main(args):
        in_ = Code03_MagicForest1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_MagicForest1.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_MagicForest1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_MagicForest1.m):
            jset(Code03_MagicForest1.ex, i, jcall(in_, 'nextInt'))
            jset(Code03_MagicForest1.ey, i, jcall(in_, 'nextInt'))
            jset(Code03_MagicForest1.ea, i, jcall(in_, 'nextInt'))
            jset(Code03_MagicForest1.eb, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        ans = jcast('int', Code03_MagicForest1.compute())
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
            raise TypeError("No matching overload for Code03_MagicForest1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_MagicForest1.MAXN = jcast('int', 200001)
Code03_MagicForest1.INF = jcast('int', 1000000001)
Code03_MagicForest1.n = jcast('int', 0)
Code03_MagicForest1.m = jcast('int', 0)
Code03_MagicForest1.ex = jarray('int', [Code03_MagicForest1.MAXN])
Code03_MagicForest1.ey = jarray('int', [Code03_MagicForest1.MAXN])
Code03_MagicForest1.ea = jarray('int', [Code03_MagicForest1.MAXN])
Code03_MagicForest1.eb = jarray('int', [Code03_MagicForest1.MAXN])
Code03_MagicForest1.fa = jarray('int', [Code03_MagicForest1.MAXN])
Code03_MagicForest1.ls = jarray('int', [Code03_MagicForest1.MAXN])
Code03_MagicForest1.rs = jarray('int', [Code03_MagicForest1.MAXN])
Code03_MagicForest1.rev = jarray('boolean', [Code03_MagicForest1.MAXN])
Code03_MagicForest1.sta = jarray('int', [Code03_MagicForest1.MAXN])
Code03_MagicForest1.maxaEdge = jarray('int', [Code03_MagicForest1.MAXN])
Code03_MagicForest1.maxbEdge = jarray('int', [Code03_MagicForest1.MAXN])

if __name__ == '__main__':
    Code03_MagicForest1.main([])
