# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 严格次小生成树，lct判断连通性，Python版
# 一共n个点、m条无向边，每条边有边权，图中可能存在自环
# 严格次小生成树的边权和，必须严格大于最小生成树的边权和
# 题目保证严格次小生成树一定存在，打印其边权和
# 1 <= n <= 10^5
# 1 <= m <= 3 * 10^5
# 0 <= 边权 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P4180
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 此实现用于展示算法思路，性能需结合题目规模评估
# 对应实现可参考 Code05_StrictSecondMinimum2.py
class Code05_StrictSecondMinimum1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'INF': 'INF', 'n': 'n', 'm': 'm', 'ex': 'ex', 'ey': 'ey', 'ew': 'ew', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'rev': 'rev', 'sta': 'sta', 'max1': 'max1', 'max2': 'max2'}
    MAXN = 0
    MAXM = 0
    INF = 0
    n = 0
    m = 0
    ex = None
    ey = None
    ew = None
    fa = None
    ls = None
    rs = None
    rev = None
    sta = None
    # max1[x]表示以x为根的辅助splay中，最大边权的值，记录值即可，不需要记录边的编号
    max1 = None
    # max2[x]表示以x为根的辅助splay中，严格次大边权的值，记录值即可，不需要记录边的编号
    max2 = None
    @staticmethod
    def sort(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', Code05_StrictSecondMinimum1.ew[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        tmp = 0
        while (i <= j):
            while (Code05_StrictSecondMinimum1.ew[i] < pivot):
                i = jcast('int', (i + 1))
            while (Code05_StrictSecondMinimum1.ew[j] > pivot):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', Code05_StrictSecondMinimum1.ex[i])
                Code05_StrictSecondMinimum1.ex[i] = jcast('int', Code05_StrictSecondMinimum1.ex[j])
                Code05_StrictSecondMinimum1.ex[j] = jcast('int', tmp)
                tmp = jcast('int', Code05_StrictSecondMinimum1.ey[i])
                Code05_StrictSecondMinimum1.ey[i] = jcast('int', Code05_StrictSecondMinimum1.ey[j])
                Code05_StrictSecondMinimum1.ey[j] = jcast('int', tmp)
                tmp = jcast('int', Code05_StrictSecondMinimum1.ew[i])
                Code05_StrictSecondMinimum1.ew[i] = jcast('int', Code05_StrictSecondMinimum1.ew[j])
                Code05_StrictSecondMinimum1.ew[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code05_StrictSecondMinimum1.sort(l, j)
        Code05_StrictSecondMinimum1.sort(i, r)

    @staticmethod
    def up(x):
        x = jcast('int', x)
        l = jcast('int', Code05_StrictSecondMinimum1.ls[x])
        lmax1 = jcast('int', Code05_StrictSecondMinimum1.max1[l])
        lmax2 = jcast('int', Code05_StrictSecondMinimum1.max2[l])
        r = jcast('int', Code05_StrictSecondMinimum1.rs[x])
        rmax1 = jcast('int', Code05_StrictSecondMinimum1.max1[r])
        rmax2 = jcast('int', Code05_StrictSecondMinimum1.max2[r])
        if (lmax1 > rmax1):
            Code05_StrictSecondMinimum1.max1[x] = jcast('int', lmax1)
            jset(Code05_StrictSecondMinimum1.max2, x, jstatic('Math', 'max', rmax1, lmax2))
        else:
            if (rmax1 > lmax1):
                Code05_StrictSecondMinimum1.max1[x] = jcast('int', rmax1)
                jset(Code05_StrictSecondMinimum1.max2, x, jstatic('Math', 'max', lmax1, rmax2))
            else:
                Code05_StrictSecondMinimum1.max1[x] = jcast('int', lmax1)
                jset(Code05_StrictSecondMinimum1.max2, x, jstatic('Math', 'max', lmax2, rmax2))
        v = jcast('int', (jcast('int', (-Code05_StrictSecondMinimum1.INF)) if (x <= Code05_StrictSecondMinimum1.n) else Code05_StrictSecondMinimum1.ew[jcast('int', (x - Code05_StrictSecondMinimum1.n))]))
        if (v > Code05_StrictSecondMinimum1.max1[x]):
            Code05_StrictSecondMinimum1.max2[x] = jcast('int', Code05_StrictSecondMinimum1.max1[x])
            Code05_StrictSecondMinimum1.max1[x] = jcast('int', v)
        else:
            if ((v < Code05_StrictSecondMinimum1.max1[x]) and (v > Code05_StrictSecondMinimum1.max2[x])):
                Code05_StrictSecondMinimum1.max2[x] = jcast('int', v)

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code05_StrictSecondMinimum1.ls[Code05_StrictSecondMinimum1.fa[x]] != x) and (Code05_StrictSecondMinimum1.rs[Code05_StrictSecondMinimum1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code05_StrictSecondMinimum1.ls[Code05_StrictSecondMinimum1.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code05_StrictSecondMinimum1.ls[x])
            Code05_StrictSecondMinimum1.ls[x] = jcast('int', Code05_StrictSecondMinimum1.rs[x])
            Code05_StrictSecondMinimum1.rs[x] = jcast('int', tmp)
            Code05_StrictSecondMinimum1.rev[x] = jcast('boolean', (not Code05_StrictSecondMinimum1.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code05_StrictSecondMinimum1.rev[x]:
            Code05_StrictSecondMinimum1.reverse(Code05_StrictSecondMinimum1.ls[x])
            Code05_StrictSecondMinimum1.reverse(Code05_StrictSecondMinimum1.rs[x])
            Code05_StrictSecondMinimum1.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code05_StrictSecondMinimum1.fa[x])
        g = jcast('int', Code05_StrictSecondMinimum1.fa[f])
        if (Code05_StrictSecondMinimum1.lr(x) == 0):
            Code05_StrictSecondMinimum1.ls[f] = jcast('int', Code05_StrictSecondMinimum1.rs[x])
            if (Code05_StrictSecondMinimum1.ls[f] != 0):
                jset(Code05_StrictSecondMinimum1.fa, Code05_StrictSecondMinimum1.ls[f], f)
            Code05_StrictSecondMinimum1.rs[x] = jcast('int', f)
        else:
            Code05_StrictSecondMinimum1.rs[f] = jcast('int', Code05_StrictSecondMinimum1.ls[x])
            if (Code05_StrictSecondMinimum1.rs[f] != 0):
                jset(Code05_StrictSecondMinimum1.fa, Code05_StrictSecondMinimum1.rs[f], f)
            Code05_StrictSecondMinimum1.ls[x] = jcast('int', f)
        if (not Code05_StrictSecondMinimum1.isroot(f)):
            if (Code05_StrictSecondMinimum1.lr(f) == 0):
                Code05_StrictSecondMinimum1.ls[g] = jcast('int', x)
            else:
                Code05_StrictSecondMinimum1.rs[g] = jcast('int', x)
        Code05_StrictSecondMinimum1.fa[f] = jcast('int', x)
        Code05_StrictSecondMinimum1.fa[x] = jcast('int', g)
        Code05_StrictSecondMinimum1.up(f)
        Code05_StrictSecondMinimum1.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code05_StrictSecondMinimum1.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code05_StrictSecondMinimum1.isroot(y)):
            jset(Code05_StrictSecondMinimum1.sta, (siz := jcast('int', (siz + (1)))), Code05_StrictSecondMinimum1.fa[y])
            y = jcast('int', Code05_StrictSecondMinimum1.fa[y])
        while (siz != 0):
            Code05_StrictSecondMinimum1.down(Code05_StrictSecondMinimum1.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code05_StrictSecondMinimum1.isroot(x)):
            f = jcast('int', Code05_StrictSecondMinimum1.fa[x])
            if (not Code05_StrictSecondMinimum1.isroot(f)):
                if (Code05_StrictSecondMinimum1.lr(x) == Code05_StrictSecondMinimum1.lr(f)):
                    Code05_StrictSecondMinimum1.rotate(f)
                else:
                    Code05_StrictSecondMinimum1.rotate(x)
            Code05_StrictSecondMinimum1.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code05_StrictSecondMinimum1.splay(x)
            Code05_StrictSecondMinimum1.rs[x] = jcast('int', y)
            Code05_StrictSecondMinimum1.up(x)
            y = jcast('int', x)
            x = jcast('int', Code05_StrictSecondMinimum1.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code05_StrictSecondMinimum1.access(x)
        Code05_StrictSecondMinimum1.splay(x)
        Code05_StrictSecondMinimum1.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code05_StrictSecondMinimum1.access(x)
        Code05_StrictSecondMinimum1.splay(x)
        Code05_StrictSecondMinimum1.down(x)
        while (Code05_StrictSecondMinimum1.ls[x] != 0):
            x = jcast('int', Code05_StrictSecondMinimum1.ls[x])
            Code05_StrictSecondMinimum1.down(x)
        Code05_StrictSecondMinimum1.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code05_StrictSecondMinimum1.makeroot(x)
        Code05_StrictSecondMinimum1.access(y)
        Code05_StrictSecondMinimum1.splay(y)

    # 保证x和y不连通，所以逻辑化简了
    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code05_StrictSecondMinimum1.makeroot(x)
        Code05_StrictSecondMinimum1.fa[x] = jcast('int', y)

    @staticmethod
    def compute():
        Code05_StrictSecondMinimum1.sort(1, Code05_StrictSecondMinimum1.m)
        sum = jcast('long', 0)
        minAdd = jcast('int', Code05_StrictSecondMinimum1.INF)
        i = jcast('int', 1)
        while (i <= Code05_StrictSecondMinimum1.m):
            x = jcast('int', Code05_StrictSecondMinimum1.ex[i])
            y = jcast('int', Code05_StrictSecondMinimum1.ey[i])
            w = jcast('int', Code05_StrictSecondMinimum1.ew[i])
            if (x != y):
                Code05_StrictSecondMinimum1.makeroot(x)
                if (Code05_StrictSecondMinimum1.findroot(y) != x):
                    Code05_StrictSecondMinimum1.max1[jcast('int', jadd(Code05_StrictSecondMinimum1.n, i))] = jcast('int', w)
                    Code05_StrictSecondMinimum1.max2[jcast('int', jadd(Code05_StrictSecondMinimum1.n, i))] = jcast('int', jcast('int', (-Code05_StrictSecondMinimum1.INF)))
                    Code05_StrictSecondMinimum1.link(x, jcast('int', jadd(Code05_StrictSecondMinimum1.n, i)))
                    Code05_StrictSecondMinimum1.link(y, jcast('int', jadd(Code05_StrictSecondMinimum1.n, i)))
                    sum = jcast('long', jcast('long', jadd(sum, w)))
                else:
                    Code05_StrictSecondMinimum1.split(x, y)
                    v1 = jcast('int', Code05_StrictSecondMinimum1.max1[y])
                    v2 = jcast('int', Code05_StrictSecondMinimum1.max2[y])
                    if (w > v1):
                        minAdd = jcast('int', jstatic('Math', 'min', minAdd, jcast('int', (w - v1))))
                    else:
                        if ((w == v1) and (v2 != jcast('int', (-Code05_StrictSecondMinimum1.INF)))):
                            minAdd = jcast('int', jstatic('Math', 'min', minAdd, jcast('int', (w - v2))))
            i = jcast('int', (i + 1))
        return jcast('long', jcast('long', jadd(sum, minAdd)))

    @staticmethod
    def main(args):
        in_ = Code05_StrictSecondMinimum1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_StrictSecondMinimum1.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_StrictSecondMinimum1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_StrictSecondMinimum1.m):
            jset(Code05_StrictSecondMinimum1.ex, i, jcall(in_, 'nextInt'))
            jset(Code05_StrictSecondMinimum1.ey, i, jcall(in_, 'nextInt'))
            jset(Code05_StrictSecondMinimum1.ew, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i <= Code05_StrictSecondMinimum1.n):
            jset(Code05_StrictSecondMinimum1.max1, i, jset(Code05_StrictSecondMinimum1.max2, i, jcast('int', (-Code05_StrictSecondMinimum1.INF))))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code05_StrictSecondMinimum1.compute())
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
                val = jcast('int', jcast('int', (jcast('int', jadd(jcast('int', (val * 10)), c)) - jchar('0'))))
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
            raise TypeError("No matching overload for Code05_StrictSecondMinimum1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_StrictSecondMinimum1.MAXN = jcast('int', 400001)
Code05_StrictSecondMinimum1.MAXM = jcast('int', 300001)
Code05_StrictSecondMinimum1.INF = jcast('int', 1000000001)
Code05_StrictSecondMinimum1.n = jcast('int', 0)
Code05_StrictSecondMinimum1.m = jcast('int', 0)
Code05_StrictSecondMinimum1.ex = jarray('int', [Code05_StrictSecondMinimum1.MAXM])
Code05_StrictSecondMinimum1.ey = jarray('int', [Code05_StrictSecondMinimum1.MAXM])
Code05_StrictSecondMinimum1.ew = jarray('int', [Code05_StrictSecondMinimum1.MAXM])
Code05_StrictSecondMinimum1.fa = jarray('int', [Code05_StrictSecondMinimum1.MAXN])
Code05_StrictSecondMinimum1.ls = jarray('int', [Code05_StrictSecondMinimum1.MAXN])
Code05_StrictSecondMinimum1.rs = jarray('int', [Code05_StrictSecondMinimum1.MAXN])
Code05_StrictSecondMinimum1.rev = jarray('boolean', [Code05_StrictSecondMinimum1.MAXN])
Code05_StrictSecondMinimum1.sta = jarray('int', [Code05_StrictSecondMinimum1.MAXN])
Code05_StrictSecondMinimum1.max1 = jarray('int', [Code05_StrictSecondMinimum1.MAXN])
Code05_StrictSecondMinimum1.max2 = jarray('int', [Code05_StrictSecondMinimum1.MAXN])

if __name__ == '__main__':
    Code05_StrictSecondMinimum1.main([])
