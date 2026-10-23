# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 染色，Python版
# 本题就是讲解161，题目5，讲了树链剖分的解法，这里用lct的解法
# 一共有n个节点，给定n-1条边，节点连成一棵树，每个节点给定初始颜色值
# 连续相同颜色被认为是一段，变化了就认为是另一段
# 比如，112221，有三个颜色段，分别为 11、222、1
# 一共有m条操作，每种操作是如下2种类型中的一种
# 操作 C x y z : x到y的路径上，每个节点的颜色都改为z
# 操作 Q x y   : x到y的路径上，打印有几个颜色段
# 1 <= n、m <= 10^5
# 1 <= 任何时候的颜色值 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P2486
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Coloring1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'sta': 'sta', 'rev': 'rev', 'arr': 'arr', 'colorAns': 'colorAns', 'lcolor': 'lcolor', 'rcolor': 'rcolor', 'colorTag': 'colorTag'}
    MAXN = 0
    n = 0
    m = 0
    fa = None
    ls = None
    rs = None
    sta = None
    rev = None
    arr = None
    colorAns = None
    lcolor = None
    rcolor = None
    # 修改颜色的懒更新信息
    colorTag = None
    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code02_Coloring1.lcolor[x] = jcast('int', (Code02_Coloring1.arr[x] if (Code02_Coloring1.ls[x] == 0) else Code02_Coloring1.lcolor[Code02_Coloring1.ls[x]]))
        Code02_Coloring1.rcolor[x] = jcast('int', (Code02_Coloring1.arr[x] if (Code02_Coloring1.rs[x] == 0) else Code02_Coloring1.rcolor[Code02_Coloring1.rs[x]]))
        Code02_Coloring1.colorAns[x] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code02_Coloring1.colorAns[Code02_Coloring1.ls[x]], Code02_Coloring1.colorAns[Code02_Coloring1.rs[x]])), 1)))
        if ((Code02_Coloring1.ls[x] != 0) and (Code02_Coloring1.rcolor[Code02_Coloring1.ls[x]] == Code02_Coloring1.arr[x])):
            Code02_Coloring1.colorAns[x] = jcast('int', (Code02_Coloring1.colorAns[x] - 1))
        if ((Code02_Coloring1.rs[x] != 0) and (Code02_Coloring1.arr[x] == Code02_Coloring1.lcolor[Code02_Coloring1.rs[x]])):
            Code02_Coloring1.colorAns[x] = jcast('int', (Code02_Coloring1.colorAns[x] - 1))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code02_Coloring1.ls[Code02_Coloring1.fa[x]] != x) and (Code02_Coloring1.rs[Code02_Coloring1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code02_Coloring1.ls[Code02_Coloring1.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code02_Coloring1.ls[x])
            Code02_Coloring1.ls[x] = jcast('int', Code02_Coloring1.rs[x])
            Code02_Coloring1.rs[x] = jcast('int', tmp)
            tmp = jcast('int', Code02_Coloring1.lcolor[x])
            Code02_Coloring1.lcolor[x] = jcast('int', Code02_Coloring1.rcolor[x])
            Code02_Coloring1.rcolor[x] = jcast('int', tmp)
            Code02_Coloring1.rev[x] = jcast('boolean', (not Code02_Coloring1.rev[x]))

    @staticmethod
    def effect(x, c):
        x = jcast('int', x)
        c = jcast('int', c)
        if (x != 0):
            Code02_Coloring1.arr[x] = jcast('int', c)
            Code02_Coloring1.lcolor[x] = jcast('int', c)
            Code02_Coloring1.rcolor[x] = jcast('int', c)
            Code02_Coloring1.colorAns[x] = jcast('int', 1)
            Code02_Coloring1.colorTag[x] = jcast('int', c)

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code02_Coloring1.rev[x]:
            Code02_Coloring1.reverse(Code02_Coloring1.ls[x])
            Code02_Coloring1.reverse(Code02_Coloring1.rs[x])
            Code02_Coloring1.rev[x] = jcast('boolean', False)
        if (Code02_Coloring1.colorTag[x] != 0):
            Code02_Coloring1.effect(Code02_Coloring1.ls[x], Code02_Coloring1.colorTag[x])
            Code02_Coloring1.effect(Code02_Coloring1.rs[x], Code02_Coloring1.colorTag[x])
            Code02_Coloring1.colorTag[x] = jcast('int', 0)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code02_Coloring1.fa[x])
        g = jcast('int', Code02_Coloring1.fa[f])
        if (Code02_Coloring1.lr(x) == 0):
            Code02_Coloring1.ls[f] = jcast('int', Code02_Coloring1.rs[x])
            if (Code02_Coloring1.ls[f] != 0):
                jset(Code02_Coloring1.fa, Code02_Coloring1.ls[f], f)
            Code02_Coloring1.rs[x] = jcast('int', f)
        else:
            Code02_Coloring1.rs[f] = jcast('int', Code02_Coloring1.ls[x])
            if (Code02_Coloring1.rs[f] != 0):
                jset(Code02_Coloring1.fa, Code02_Coloring1.rs[f], f)
            Code02_Coloring1.ls[x] = jcast('int', f)
        if (not Code02_Coloring1.isroot(f)):
            if (Code02_Coloring1.lr(f) == 0):
                Code02_Coloring1.ls[g] = jcast('int', x)
            else:
                Code02_Coloring1.rs[g] = jcast('int', x)
        Code02_Coloring1.fa[f] = jcast('int', x)
        Code02_Coloring1.fa[x] = jcast('int', g)
        Code02_Coloring1.up(f)
        Code02_Coloring1.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code02_Coloring1.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code02_Coloring1.isroot(y)):
            jset(Code02_Coloring1.sta, (siz := jcast('int', (siz + (1)))), Code02_Coloring1.fa[y])
            y = jcast('int', Code02_Coloring1.fa[y])
        while (siz != 0):
            Code02_Coloring1.down(Code02_Coloring1.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code02_Coloring1.isroot(x)):
            f = jcast('int', Code02_Coloring1.fa[x])
            if (not Code02_Coloring1.isroot(f)):
                if (Code02_Coloring1.lr(x) == Code02_Coloring1.lr(f)):
                    Code02_Coloring1.rotate(f)
                else:
                    Code02_Coloring1.rotate(x)
            Code02_Coloring1.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code02_Coloring1.splay(x)
            Code02_Coloring1.rs[x] = jcast('int', y)
            Code02_Coloring1.up(x)
            y = jcast('int', x)
            x = jcast('int', Code02_Coloring1.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code02_Coloring1.access(x)
        Code02_Coloring1.splay(x)
        Code02_Coloring1.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code02_Coloring1.access(x)
        Code02_Coloring1.splay(x)
        Code02_Coloring1.down(x)
        while (Code02_Coloring1.ls[x] != 0):
            x = jcast('int', Code02_Coloring1.ls[x])
            Code02_Coloring1.down(x)
        Code02_Coloring1.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code02_Coloring1.makeroot(x)
        Code02_Coloring1.access(y)
        Code02_Coloring1.splay(y)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code02_Coloring1.makeroot(x)
        if (Code02_Coloring1.findroot(y) != x):
            Code02_Coloring1.fa[x] = jcast('int', y)

    @staticmethod
    def main(args):
        in_ = Code02_Coloring1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_Coloring1.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_Coloring1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_Coloring1.n):
            jset(Code02_Coloring1.arr, i, jcall(in_, 'nextInt'))
            Code02_Coloring1.lcolor[i] = jcast('int', Code02_Coloring1.arr[i])
            Code02_Coloring1.rcolor[i] = jcast('int', Code02_Coloring1.arr[i])
            Code02_Coloring1.colorAns[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i < Code02_Coloring1.n):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            Code02_Coloring1.link(x, y)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        x = 0
        y = 0
        c = 0
        while (i <= Code02_Coloring1.m):
            op = jcall(in_, 'nextString')
            if jcall(op, 'equals', 'C'):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                c = jcast('int', jcall(in_, 'nextInt'))
                Code02_Coloring1.split(x, y)
                Code02_Coloring1.effect(y, c)
            else:
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                Code02_Coloring1.split(x, y)
                jcall(out, 'println', Code02_Coloring1.colorAns[y])
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
            raise TypeError("No matching overload for Code02_Coloring1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Coloring1.MAXN = jcast('int', 100001)
Code02_Coloring1.n = jcast('int', 0)
Code02_Coloring1.m = jcast('int', 0)
Code02_Coloring1.fa = jarray('int', [Code02_Coloring1.MAXN])
Code02_Coloring1.ls = jarray('int', [Code02_Coloring1.MAXN])
Code02_Coloring1.rs = jarray('int', [Code02_Coloring1.MAXN])
Code02_Coloring1.sta = jarray('int', [Code02_Coloring1.MAXN])
Code02_Coloring1.rev = jarray('boolean', [Code02_Coloring1.MAXN])
Code02_Coloring1.arr = jarray('int', [Code02_Coloring1.MAXN])
Code02_Coloring1.colorAns = jarray('int', [Code02_Coloring1.MAXN])
Code02_Coloring1.lcolor = jarray('int', [Code02_Coloring1.MAXN])
Code02_Coloring1.rcolor = jarray('int', [Code02_Coloring1.MAXN])
Code02_Coloring1.colorTag = jarray('int', [Code02_Coloring1.MAXN])

if __name__ == '__main__':
    Code02_Coloring1.main([])
