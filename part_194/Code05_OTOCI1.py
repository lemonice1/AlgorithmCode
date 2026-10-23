# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 群岛，Python版
# 一共n个点，每个点有点权，初始时没有边，一共m条操作，类型如下
# 操作 bridge x y    : 如果x和y已经连通，打印no，表示不需要连边
# 如果x和y不连通，打印yes，然后增加无向边
# 操作 penguins x y  : x的点权变成y
# 操作 excursion x y : 如果x和y不连通，打印impossible
# 如果x和y连通，打印路径的点权累加和
# 1 <= n <= 3 * 10^4
# 1 <= m <= 3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4312
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_OTOCI1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'arr': 'arr', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'sta': 'sta', 'rev': 'rev', 'sum': 'sum'}
    MAXN = 0
    n = 0
    m = 0
    arr = None
    fa = None
    ls = None
    rs = None
    sta = None
    rev = None
    # 点权和
    sum = None
    # 汇总点权和
    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code05_OTOCI1.sum[x] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code05_OTOCI1.sum[Code05_OTOCI1.ls[x]], Code05_OTOCI1.sum[Code05_OTOCI1.rs[x]])), Code05_OTOCI1.arr[x])))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code05_OTOCI1.ls[Code05_OTOCI1.fa[x]] != x) and (Code05_OTOCI1.rs[Code05_OTOCI1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code05_OTOCI1.ls[Code05_OTOCI1.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code05_OTOCI1.ls[x])
            Code05_OTOCI1.ls[x] = jcast('int', Code05_OTOCI1.rs[x])
            Code05_OTOCI1.rs[x] = jcast('int', tmp)
            Code05_OTOCI1.rev[x] = jcast('boolean', (not Code05_OTOCI1.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code05_OTOCI1.rev[x]:
            Code05_OTOCI1.reverse(Code05_OTOCI1.ls[x])
            Code05_OTOCI1.reverse(Code05_OTOCI1.rs[x])
            Code05_OTOCI1.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code05_OTOCI1.fa[x])
        g = jcast('int', Code05_OTOCI1.fa[f])
        if (Code05_OTOCI1.lr(x) == 0):
            Code05_OTOCI1.ls[f] = jcast('int', Code05_OTOCI1.rs[x])
            if (Code05_OTOCI1.ls[f] != 0):
                jset(Code05_OTOCI1.fa, Code05_OTOCI1.ls[f], f)
            Code05_OTOCI1.rs[x] = jcast('int', f)
        else:
            Code05_OTOCI1.rs[f] = jcast('int', Code05_OTOCI1.ls[x])
            if (Code05_OTOCI1.rs[f] != 0):
                jset(Code05_OTOCI1.fa, Code05_OTOCI1.rs[f], f)
            Code05_OTOCI1.ls[x] = jcast('int', f)
        if (not Code05_OTOCI1.isroot(f)):
            if (Code05_OTOCI1.lr(f) == 0):
                Code05_OTOCI1.ls[g] = jcast('int', x)
            else:
                Code05_OTOCI1.rs[g] = jcast('int', x)
        Code05_OTOCI1.fa[f] = jcast('int', x)
        Code05_OTOCI1.fa[x] = jcast('int', g)
        Code05_OTOCI1.up(f)
        Code05_OTOCI1.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code05_OTOCI1.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code05_OTOCI1.isroot(y)):
            jset(Code05_OTOCI1.sta, (siz := jcast('int', (siz + (1)))), Code05_OTOCI1.fa[y])
            y = jcast('int', Code05_OTOCI1.fa[y])
        while (siz != 0):
            Code05_OTOCI1.down(Code05_OTOCI1.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code05_OTOCI1.isroot(x)):
            f = jcast('int', Code05_OTOCI1.fa[x])
            if (not Code05_OTOCI1.isroot(f)):
                if (Code05_OTOCI1.lr(x) == Code05_OTOCI1.lr(f)):
                    Code05_OTOCI1.rotate(f)
                else:
                    Code05_OTOCI1.rotate(x)
            Code05_OTOCI1.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code05_OTOCI1.splay(x)
            Code05_OTOCI1.rs[x] = jcast('int', y)
            Code05_OTOCI1.up(x)
            y = jcast('int', x)
            x = jcast('int', Code05_OTOCI1.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code05_OTOCI1.access(x)
        Code05_OTOCI1.splay(x)
        Code05_OTOCI1.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code05_OTOCI1.access(x)
        Code05_OTOCI1.splay(x)
        Code05_OTOCI1.down(x)
        while (Code05_OTOCI1.ls[x] != 0):
            x = jcast('int', Code05_OTOCI1.ls[x])
            Code05_OTOCI1.down(x)
        Code05_OTOCI1.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code05_OTOCI1.makeroot(x)
        Code05_OTOCI1.access(y)
        Code05_OTOCI1.splay(y)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code05_OTOCI1.makeroot(x)
        if (Code05_OTOCI1.findroot(y) != x):
            Code05_OTOCI1.fa[x] = jcast('int', y)

    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code05_OTOCI1.makeroot(x)
        if ((((Code05_OTOCI1.findroot(y) == x) and (Code05_OTOCI1.fa[y] == x)) and (Code05_OTOCI1.ls[y] == 0)) and (Code05_OTOCI1.rs[x] == y)):
            jset(Code05_OTOCI1.fa, y, jset(Code05_OTOCI1.rs, x, 0))
            Code05_OTOCI1.up(x)

    @staticmethod
    def main(args):
        in_ = Code05_OTOCI1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_OTOCI1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_OTOCI1.n):
            jset(Code05_OTOCI1.arr, i, jcall(in_, 'nextInt'))
            Code05_OTOCI1.sum[i] = jcast('int', Code05_OTOCI1.arr[i])
            i = jcast('int', (i + 1))
        Code05_OTOCI1.m = jcast('int', jcall(in_, 'nextInt'))
        op = None
        x = 0
        y = 0
        i = jcast('int', 1)
        while (i <= Code05_OTOCI1.m):
            op = jcall(in_, 'nextString')
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            if jcall(op, 'equals', 'bridge'):
                if (Code05_OTOCI1.findroot(x) == Code05_OTOCI1.findroot(y)):
                    jcall(out, 'println', 'no')
                else:
                    jcall(out, 'println', 'yes')
                    Code05_OTOCI1.link(x, y)
            else:
                if jcall(op, 'equals', 'penguins'):
                    Code05_OTOCI1.splay(x)
                    Code05_OTOCI1.arr[x] = jcast('int', y)
                    Code05_OTOCI1.up(x)
                else:
                    if (Code05_OTOCI1.findroot(x) != Code05_OTOCI1.findroot(y)):
                        jcall(out, 'println', 'impossible')
                    else:
                        Code05_OTOCI1.split(x, y)
                        jcall(out, 'println', Code05_OTOCI1.sum[y])
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

        def nextString(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            if (c == jcast('int', (-1))):
                return None
            sb = jnew('StringBuilder')
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                jcall(sb, 'append', jcast('char', c))
                c = jcast('int', self.readByte())
            return jcall(sb, 'toString')

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_OTOCI1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_OTOCI1.MAXN = jcast('int', 30001)
Code05_OTOCI1.n = jcast('int', 0)
Code05_OTOCI1.m = jcast('int', 0)
Code05_OTOCI1.arr = jarray('int', [Code05_OTOCI1.MAXN])
Code05_OTOCI1.fa = jarray('int', [Code05_OTOCI1.MAXN])
Code05_OTOCI1.ls = jarray('int', [Code05_OTOCI1.MAXN])
Code05_OTOCI1.rs = jarray('int', [Code05_OTOCI1.MAXN])
Code05_OTOCI1.sta = jarray('int', [Code05_OTOCI1.MAXN])
Code05_OTOCI1.rev = jarray('boolean', [Code05_OTOCI1.MAXN])
Code05_OTOCI1.sum = jarray('int', [Code05_OTOCI1.MAXN])

if __name__ == '__main__':
    Code05_OTOCI1.main([])
