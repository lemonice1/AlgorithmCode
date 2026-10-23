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

# 最小差值生成树，Python版
# 一共n个点、m条无向边，给定每条边的两个端点和边权
# 题目保证图连通，图中可能存在自环，选择一棵生成树
# 希望树中最大边权减去最小边权的值尽量小，打印该值
# 1 <= n <= 5 * 10^4
# 1 <= m <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4234
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_MinimumDifference1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'ex': 'ex', 'ey': 'ey', 'ew': 'ew', 'removed': 'removed', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'rev': 'rev', 'sta': 'sta', 'minEdge': 'minEdge'}
    MAXN = 0
    n = 0
    m = 0
    ex = None
    ey = None
    ew = None
    # removed[i]表示第i条边是否被淘汰
    removed = None
    # 辅助splay
    fa = None
    ls = None
    rs = None
    rev = None
    sta = None
    # minEdge[x]表示以x为根的辅助splay中，编号最小的边
    # 因为按照权值从小到大排序，所以编号最小就是边权最小
    minEdge = None
    # 手撸双指针快排，根据边权从小到大排序
    @staticmethod
    def sort(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', Code02_MinimumDifference1.ew[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        tmp = 0
        while (i <= j):
            while (Code02_MinimumDifference1.ew[i] < pivot):
                i = jcast('int', (i + 1))
            while (Code02_MinimumDifference1.ew[j] > pivot):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', Code02_MinimumDifference1.ex[i])
                Code02_MinimumDifference1.ex[i] = jcast('int', Code02_MinimumDifference1.ex[j])
                Code02_MinimumDifference1.ex[j] = jcast('int', tmp)
                tmp = jcast('int', Code02_MinimumDifference1.ey[i])
                Code02_MinimumDifference1.ey[i] = jcast('int', Code02_MinimumDifference1.ey[j])
                Code02_MinimumDifference1.ey[j] = jcast('int', tmp)
                tmp = jcast('int', Code02_MinimumDifference1.ew[i])
                Code02_MinimumDifference1.ew[i] = jcast('int', Code02_MinimumDifference1.ew[j])
                Code02_MinimumDifference1.ew[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code02_MinimumDifference1.sort(l, j)
        Code02_MinimumDifference1.sort(i, r)

    @staticmethod
    def up(x):
        x = jcast('int', x)
        cur = jcast('int', (0 if (x <= Code02_MinimumDifference1.n) else jcast('int', (x - Code02_MinimumDifference1.n))))
        l = jcast('int', Code02_MinimumDifference1.minEdge[Code02_MinimumDifference1.ls[x]])
        r = jcast('int', Code02_MinimumDifference1.minEdge[Code02_MinimumDifference1.rs[x]])
        if ((cur == 0) or ((l != 0) and (l < cur))):
            cur = jcast('int', l)
        if ((cur == 0) or ((r != 0) and (r < cur))):
            cur = jcast('int', r)
        Code02_MinimumDifference1.minEdge[x] = jcast('int', cur)

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code02_MinimumDifference1.ls[Code02_MinimumDifference1.fa[x]] != x) and (Code02_MinimumDifference1.rs[Code02_MinimumDifference1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code02_MinimumDifference1.ls[Code02_MinimumDifference1.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code02_MinimumDifference1.ls[x])
            Code02_MinimumDifference1.ls[x] = jcast('int', Code02_MinimumDifference1.rs[x])
            Code02_MinimumDifference1.rs[x] = jcast('int', tmp)
            Code02_MinimumDifference1.rev[x] = jcast('boolean', (not Code02_MinimumDifference1.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code02_MinimumDifference1.rev[x]:
            Code02_MinimumDifference1.reverse(Code02_MinimumDifference1.ls[x])
            Code02_MinimumDifference1.reverse(Code02_MinimumDifference1.rs[x])
            Code02_MinimumDifference1.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code02_MinimumDifference1.fa[x])
        g = jcast('int', Code02_MinimumDifference1.fa[f])
        if (Code02_MinimumDifference1.lr(x) == 0):
            Code02_MinimumDifference1.ls[f] = jcast('int', Code02_MinimumDifference1.rs[x])
            if (Code02_MinimumDifference1.ls[f] != 0):
                jset(Code02_MinimumDifference1.fa, Code02_MinimumDifference1.ls[f], f)
            Code02_MinimumDifference1.rs[x] = jcast('int', f)
        else:
            Code02_MinimumDifference1.rs[f] = jcast('int', Code02_MinimumDifference1.ls[x])
            if (Code02_MinimumDifference1.rs[f] != 0):
                jset(Code02_MinimumDifference1.fa, Code02_MinimumDifference1.rs[f], f)
            Code02_MinimumDifference1.ls[x] = jcast('int', f)
        if (not Code02_MinimumDifference1.isroot(f)):
            if (Code02_MinimumDifference1.lr(f) == 0):
                Code02_MinimumDifference1.ls[g] = jcast('int', x)
            else:
                Code02_MinimumDifference1.rs[g] = jcast('int', x)
        Code02_MinimumDifference1.fa[f] = jcast('int', x)
        Code02_MinimumDifference1.fa[x] = jcast('int', g)
        Code02_MinimumDifference1.up(f)
        Code02_MinimumDifference1.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code02_MinimumDifference1.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code02_MinimumDifference1.isroot(y)):
            jset(Code02_MinimumDifference1.sta, (siz := jcast('int', (siz + (1)))), Code02_MinimumDifference1.fa[y])
            y = jcast('int', Code02_MinimumDifference1.fa[y])
        while (siz != 0):
            Code02_MinimumDifference1.down(Code02_MinimumDifference1.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code02_MinimumDifference1.isroot(x)):
            f = jcast('int', Code02_MinimumDifference1.fa[x])
            if (not Code02_MinimumDifference1.isroot(f)):
                if (Code02_MinimumDifference1.lr(x) == Code02_MinimumDifference1.lr(f)):
                    Code02_MinimumDifference1.rotate(f)
                else:
                    Code02_MinimumDifference1.rotate(x)
            Code02_MinimumDifference1.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code02_MinimumDifference1.splay(x)
            Code02_MinimumDifference1.rs[x] = jcast('int', y)
            Code02_MinimumDifference1.up(x)
            y = jcast('int', x)
            x = jcast('int', Code02_MinimumDifference1.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code02_MinimumDifference1.access(x)
        Code02_MinimumDifference1.splay(x)
        Code02_MinimumDifference1.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code02_MinimumDifference1.access(x)
        Code02_MinimumDifference1.splay(x)
        Code02_MinimumDifference1.down(x)
        while (Code02_MinimumDifference1.ls[x] != 0):
            x = jcast('int', Code02_MinimumDifference1.ls[x])
            Code02_MinimumDifference1.down(x)
        Code02_MinimumDifference1.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code02_MinimumDifference1.makeroot(x)
        Code02_MinimumDifference1.access(y)
        Code02_MinimumDifference1.splay(y)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code02_MinimumDifference1.makeroot(x)
        if (Code02_MinimumDifference1.findroot(y) != x):
            Code02_MinimumDifference1.fa[x] = jcast('int', y)

    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code02_MinimumDifference1.makeroot(x)
        if ((((Code02_MinimumDifference1.findroot(y) == x) and (Code02_MinimumDifference1.fa[y] == x)) and (Code02_MinimumDifference1.ls[y] == 0)) and (Code02_MinimumDifference1.rs[x] == y)):
            jset(Code02_MinimumDifference1.fa, y, jset(Code02_MinimumDifference1.rs, x, 0))
            Code02_MinimumDifference1.up(x)

    @staticmethod
    def compute():
        Code02_MinimumDifference1.sort(1, Code02_MinimumDifference1.m)
        edgeCnt = jcast('int', 0)
        first = jcast('int', 1)
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        i = jcast('int', 1)
        while (i <= Code02_MinimumDifference1.m):
            x = jcast('int', Code02_MinimumDifference1.ex[i])
            y = jcast('int', Code02_MinimumDifference1.ey[i])
            if (x == y):
                Code02_MinimumDifference1.removed[i] = jcast('boolean', True)
            else:
                Code02_MinimumDifference1.makeroot(x)
                if (Code02_MinimumDifference1.findroot(y) != x):
                    Code02_MinimumDifference1.link(x, jcast('int', jadd(Code02_MinimumDifference1.n, i)))
                    Code02_MinimumDifference1.link(y, jcast('int', jadd(Code02_MinimumDifference1.n, i)))
                    edgeCnt = jcast('int', (edgeCnt + 1))
                else:
                    Code02_MinimumDifference1.split(x, y)
                    pre = jcast('int', Code02_MinimumDifference1.minEdge[y])
                    Code02_MinimumDifference1.cut(Code02_MinimumDifference1.ex[pre], jcast('int', jadd(Code02_MinimumDifference1.n, pre)))
                    Code02_MinimumDifference1.cut(Code02_MinimumDifference1.ey[pre], jcast('int', jadd(Code02_MinimumDifference1.n, pre)))
                    Code02_MinimumDifference1.link(x, jcast('int', jadd(Code02_MinimumDifference1.n, i)))
                    Code02_MinimumDifference1.link(y, jcast('int', jadd(Code02_MinimumDifference1.n, i)))
                    Code02_MinimumDifference1.removed[pre] = jcast('boolean', True)
            while Code02_MinimumDifference1.removed[first]:
                first = jcast('int', (first + 1))
            if (edgeCnt == jcast('int', (Code02_MinimumDifference1.n - 1))):
                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', (Code02_MinimumDifference1.ew[i] - Code02_MinimumDifference1.ew[first]))))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code02_MinimumDifference1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_MinimumDifference1.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_MinimumDifference1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_MinimumDifference1.m):
            jset(Code02_MinimumDifference1.ex, i, jcall(in_, 'nextInt'))
            jset(Code02_MinimumDifference1.ey, i, jcall(in_, 'nextInt'))
            jset(Code02_MinimumDifference1.ew, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code02_MinimumDifference1.compute())
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
            raise TypeError("No matching overload for Code02_MinimumDifference1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_MinimumDifference1.MAXN = jcast('int', 300001)
Code02_MinimumDifference1.n = jcast('int', 0)
Code02_MinimumDifference1.m = jcast('int', 0)
Code02_MinimumDifference1.ex = jarray('int', [Code02_MinimumDifference1.MAXN])
Code02_MinimumDifference1.ey = jarray('int', [Code02_MinimumDifference1.MAXN])
Code02_MinimumDifference1.ew = jarray('int', [Code02_MinimumDifference1.MAXN])
Code02_MinimumDifference1.removed = jarray('boolean', [Code02_MinimumDifference1.MAXN])
Code02_MinimumDifference1.fa = jarray('int', [Code02_MinimumDifference1.MAXN])
Code02_MinimumDifference1.ls = jarray('int', [Code02_MinimumDifference1.MAXN])
Code02_MinimumDifference1.rs = jarray('int', [Code02_MinimumDifference1.MAXN])
Code02_MinimumDifference1.rev = jarray('boolean', [Code02_MinimumDifference1.MAXN])
Code02_MinimumDifference1.sta = jarray('int', [Code02_MinimumDifference1.MAXN])
Code02_MinimumDifference1.minEdge = jarray('int', [Code02_MinimumDifference1.MAXN])

if __name__ == '__main__':
    Code02_MinimumDifference1.main([])
