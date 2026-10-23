# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 部落冲突，Python版
# 一共n个点，给定n-1条边，所有点组成一棵树，一共m条操作，类型如下
# 操作 C x y : x和y在树中相邻，之前未开战，现在开战，x和y的直接边变成不可通行
# 每条C操作代表一次战争事件，战争事件从1开始编号，每次编号自增
# 操作 U x   : 第x号战争事件结束，对应的直接边变为可通行，保证战争不会重复结束
# 操作 Q x y : 查询点x和点y之间是否连通，打印 Yes 或 No
# 1 <= n、m <= 3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3950
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Conflict1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'sta': 'sta', 'rev': 'rev', 'cutx': 'cutx', 'cuty': 'cuty', 'cutc': 'cutc'}
    MAXN = 0
    n = 0
    m = 0
    fa = None
    ls = None
    rs = None
    sta = None
    rev = None
    cutx = None
    cuty = None
    cutc = 0
    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code04_Conflict1.ls[Code04_Conflict1.fa[x]] != x) and (Code04_Conflict1.rs[Code04_Conflict1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code04_Conflict1.ls[Code04_Conflict1.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code04_Conflict1.ls[x])
            Code04_Conflict1.ls[x] = jcast('int', Code04_Conflict1.rs[x])
            Code04_Conflict1.rs[x] = jcast('int', tmp)
            Code04_Conflict1.rev[x] = jcast('boolean', (not Code04_Conflict1.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code04_Conflict1.rev[x]:
            Code04_Conflict1.reverse(Code04_Conflict1.ls[x])
            Code04_Conflict1.reverse(Code04_Conflict1.rs[x])
            Code04_Conflict1.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code04_Conflict1.fa[x])
        g = jcast('int', Code04_Conflict1.fa[f])
        if (Code04_Conflict1.lr(x) == 0):
            Code04_Conflict1.ls[f] = jcast('int', Code04_Conflict1.rs[x])
            if (Code04_Conflict1.ls[f] != 0):
                jset(Code04_Conflict1.fa, Code04_Conflict1.ls[f], f)
            Code04_Conflict1.rs[x] = jcast('int', f)
        else:
            Code04_Conflict1.rs[f] = jcast('int', Code04_Conflict1.ls[x])
            if (Code04_Conflict1.rs[f] != 0):
                jset(Code04_Conflict1.fa, Code04_Conflict1.rs[f], f)
            Code04_Conflict1.ls[x] = jcast('int', f)
        if (not Code04_Conflict1.isroot(f)):
            if (Code04_Conflict1.lr(f) == 0):
                Code04_Conflict1.ls[g] = jcast('int', x)
            else:
                Code04_Conflict1.rs[g] = jcast('int', x)
        Code04_Conflict1.fa[f] = jcast('int', x)
        Code04_Conflict1.fa[x] = jcast('int', g)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code04_Conflict1.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code04_Conflict1.isroot(y)):
            jset(Code04_Conflict1.sta, (siz := jcast('int', (siz + (1)))), Code04_Conflict1.fa[y])
            y = jcast('int', Code04_Conflict1.fa[y])
        while (siz != 0):
            Code04_Conflict1.down(Code04_Conflict1.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code04_Conflict1.isroot(x)):
            f = jcast('int', Code04_Conflict1.fa[x])
            if (not Code04_Conflict1.isroot(f)):
                if (Code04_Conflict1.lr(x) == Code04_Conflict1.lr(f)):
                    Code04_Conflict1.rotate(f)
                else:
                    Code04_Conflict1.rotate(x)
            Code04_Conflict1.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code04_Conflict1.splay(x)
            Code04_Conflict1.rs[x] = jcast('int', y)
            y = jcast('int', x)
            x = jcast('int', Code04_Conflict1.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code04_Conflict1.access(x)
        Code04_Conflict1.splay(x)
        Code04_Conflict1.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code04_Conflict1.access(x)
        Code04_Conflict1.splay(x)
        Code04_Conflict1.down(x)
        while (Code04_Conflict1.ls[x] != 0):
            x = jcast('int', Code04_Conflict1.ls[x])
            Code04_Conflict1.down(x)
        Code04_Conflict1.splay(x)
        return jcast('int', x)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code04_Conflict1.makeroot(x)
        if (Code04_Conflict1.findroot(y) != x):
            Code04_Conflict1.fa[x] = jcast('int', y)

    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code04_Conflict1.makeroot(x)
        if ((((Code04_Conflict1.findroot(y) == x) and (Code04_Conflict1.fa[y] == x)) and (Code04_Conflict1.ls[y] == 0)) and (Code04_Conflict1.rs[x] == y)):
            jset(Code04_Conflict1.fa, y, jset(Code04_Conflict1.rs, x, 0))

    @staticmethod
    def main(args):
        in_ = Code04_Conflict1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_Conflict1.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_Conflict1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i < Code04_Conflict1.n):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            Code04_Conflict1.link(x, y)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= Code04_Conflict1.m):
            op = jcall(in_, 'nextString')
            if jcall(op, 'equals', 'C'):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                Code04_Conflict1.cut(x, y)
                jset(Code04_Conflict1.cutx, ((_java_obj_2 := Code04_Conflict1), (_java_key_3 := 'cutc'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))))[3], x)
                Code04_Conflict1.cuty[Code04_Conflict1.cutc] = jcast('int', y)
            else:
                if jcall(op, 'equals', 'U'):
                    x = jcast('int', jcall(in_, 'nextInt'))
                    Code04_Conflict1.link(Code04_Conflict1.cutx[x], Code04_Conflict1.cuty[x])
                else:
                    x = jcast('int', jcall(in_, 'nextInt'))
                    y = jcast('int', jcall(in_, 'nextInt'))
                    if (Code04_Conflict1.findroot(x) == Code04_Conflict1.findroot(y)):
                        jcall(out, 'println', 'Yes')
                    else:
                        jcall(out, 'println', 'No')
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
            raise TypeError("No matching overload for Code04_Conflict1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Conflict1.MAXN = jcast('int', 300001)
Code04_Conflict1.n = jcast('int', 0)
Code04_Conflict1.m = jcast('int', 0)
Code04_Conflict1.fa = jarray('int', [Code04_Conflict1.MAXN])
Code04_Conflict1.ls = jarray('int', [Code04_Conflict1.MAXN])
Code04_Conflict1.rs = jarray('int', [Code04_Conflict1.MAXN])
Code04_Conflict1.sta = jarray('int', [Code04_Conflict1.MAXN])
Code04_Conflict1.rev = jarray('boolean', [Code04_Conflict1.MAXN])
Code04_Conflict1.cutx = jarray('int', [Code04_Conflict1.MAXN])
Code04_Conflict1.cuty = jarray('int', [Code04_Conflict1.MAXN])
Code04_Conflict1.cutc = jcast('int', 0)

if __name__ == '__main__':
    Code04_Conflict1.main([])
