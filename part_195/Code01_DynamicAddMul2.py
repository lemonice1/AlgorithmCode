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

# 动态树的加和乘，Python版
# 一共有n个点、n-1条边，每个点的初始点权都是1，所有节点组成一棵树
# 接下来有q条操作，操作类型有四种，格式如下
# 操作 + x y z   : x到y的路径上，点的权值都加上z，z是非负整数
# 操作 * x y z   : x到y的路径上，点的权值都乘上z，z是非负整数
# 操作 - x y a b : 删除原边(x,y)，加入新边(a,b)，操作后仍然是一棵树
# 操作 / x y     : x到y的路径上，查询点权累加和，对 51061 取模
# 1 <= n、q <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P1501
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_DynamicAddMul2:
    __java_fields__ = {'MAXN': 'MAXN', 'MOD': 'MOD', 'n': 'n', 'q': 'q', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'sta': 'sta', 'rev': 'rev', 'siz': 'siz', 'arr': 'arr', 'sum': 'sum', 'mulTag': 'mulTag', 'addTag': 'addTag'}
    MAXN = 0
    MOD = 0
    n = 0
    q = 0
    fa = None
    ls = None
    rs = None
    sta = None
    rev = None
    siz = None
    arr = None
    sum = None
    mulTag = None
    addTag = None
    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code01_DynamicAddMul2.siz[x] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code01_DynamicAddMul2.siz[Code01_DynamicAddMul2.ls[x]], Code01_DynamicAddMul2.siz[Code01_DynamicAddMul2.rs[x]])), 1)))
        Code01_DynamicAddMul2.sum[x] = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jadd(Code01_DynamicAddMul2.sum[Code01_DynamicAddMul2.ls[x]], Code01_DynamicAddMul2.sum[Code01_DynamicAddMul2.rs[x]])), Code01_DynamicAddMul2.arr[x])), Code01_DynamicAddMul2.MOD)))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code01_DynamicAddMul2.ls[Code01_DynamicAddMul2.fa[x]] != x) and (Code01_DynamicAddMul2.rs[Code01_DynamicAddMul2.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code01_DynamicAddMul2.ls[Code01_DynamicAddMul2.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code01_DynamicAddMul2.ls[x])
            Code01_DynamicAddMul2.ls[x] = jcast('int', Code01_DynamicAddMul2.rs[x])
            Code01_DynamicAddMul2.rs[x] = jcast('int', tmp)
            Code01_DynamicAddMul2.rev[x] = jcast('boolean', (not Code01_DynamicAddMul2.rev[x]))

    @staticmethod
    def effect(x, mul, add):
        x = jcast('int', x)
        mul = jcast('long', mul)
        add = jcast('long', add)
        if (x != 0):
            Code01_DynamicAddMul2.arr[x] = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', (Code01_DynamicAddMul2.arr[x] * mul)), add)), Code01_DynamicAddMul2.MOD)))
            Code01_DynamicAddMul2.sum[x] = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', (Code01_DynamicAddMul2.sum[x] * mul)), jcast('long', (Code01_DynamicAddMul2.siz[x] * add)))), Code01_DynamicAddMul2.MOD)))
            Code01_DynamicAddMul2.mulTag[x] = jcast('long', jcast('long', jmod(jcast('long', (Code01_DynamicAddMul2.mulTag[x] * mul)), Code01_DynamicAddMul2.MOD)))
            Code01_DynamicAddMul2.addTag[x] = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', (Code01_DynamicAddMul2.addTag[x] * mul)), add)), Code01_DynamicAddMul2.MOD)))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code01_DynamicAddMul2.rev[x]:
            Code01_DynamicAddMul2.reverse(Code01_DynamicAddMul2.ls[x])
            Code01_DynamicAddMul2.reverse(Code01_DynamicAddMul2.rs[x])
            Code01_DynamicAddMul2.rev[x] = jcast('boolean', False)
        if ((Code01_DynamicAddMul2.mulTag[x] != 1) or (Code01_DynamicAddMul2.addTag[x] != 0)):
            Code01_DynamicAddMul2.effect(Code01_DynamicAddMul2.ls[x], Code01_DynamicAddMul2.mulTag[x], Code01_DynamicAddMul2.addTag[x])
            Code01_DynamicAddMul2.effect(Code01_DynamicAddMul2.rs[x], Code01_DynamicAddMul2.mulTag[x], Code01_DynamicAddMul2.addTag[x])
            Code01_DynamicAddMul2.mulTag[x] = jcast('long', 1)
            Code01_DynamicAddMul2.addTag[x] = jcast('long', 0)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code01_DynamicAddMul2.fa[x])
        g = jcast('int', Code01_DynamicAddMul2.fa[f])
        if (Code01_DynamicAddMul2.lr(x) == 0):
            Code01_DynamicAddMul2.ls[f] = jcast('int', Code01_DynamicAddMul2.rs[x])
            if (Code01_DynamicAddMul2.ls[f] != 0):
                jset(Code01_DynamicAddMul2.fa, Code01_DynamicAddMul2.ls[f], f)
            Code01_DynamicAddMul2.rs[x] = jcast('int', f)
        else:
            Code01_DynamicAddMul2.rs[f] = jcast('int', Code01_DynamicAddMul2.ls[x])
            if (Code01_DynamicAddMul2.rs[f] != 0):
                jset(Code01_DynamicAddMul2.fa, Code01_DynamicAddMul2.rs[f], f)
            Code01_DynamicAddMul2.ls[x] = jcast('int', f)
        if (not Code01_DynamicAddMul2.isroot(f)):
            if (Code01_DynamicAddMul2.lr(f) == 0):
                Code01_DynamicAddMul2.ls[g] = jcast('int', x)
            else:
                Code01_DynamicAddMul2.rs[g] = jcast('int', x)
        Code01_DynamicAddMul2.fa[f] = jcast('int', x)
        Code01_DynamicAddMul2.fa[x] = jcast('int', g)
        Code01_DynamicAddMul2.up(f)
        Code01_DynamicAddMul2.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code01_DynamicAddMul2.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code01_DynamicAddMul2.isroot(y)):
            jset(Code01_DynamicAddMul2.sta, (siz := jcast('int', (siz + (1)))), Code01_DynamicAddMul2.fa[y])
            y = jcast('int', Code01_DynamicAddMul2.fa[y])
        while (siz != 0):
            Code01_DynamicAddMul2.down(Code01_DynamicAddMul2.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code01_DynamicAddMul2.isroot(x)):
            f = jcast('int', Code01_DynamicAddMul2.fa[x])
            if (not Code01_DynamicAddMul2.isroot(f)):
                if (Code01_DynamicAddMul2.lr(x) == Code01_DynamicAddMul2.lr(f)):
                    Code01_DynamicAddMul2.rotate(f)
                else:
                    Code01_DynamicAddMul2.rotate(x)
            Code01_DynamicAddMul2.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code01_DynamicAddMul2.splay(x)
            Code01_DynamicAddMul2.rs[x] = jcast('int', y)
            Code01_DynamicAddMul2.up(x)
            y = jcast('int', x)
            x = jcast('int', Code01_DynamicAddMul2.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code01_DynamicAddMul2.access(x)
        Code01_DynamicAddMul2.splay(x)
        Code01_DynamicAddMul2.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code01_DynamicAddMul2.access(x)
        Code01_DynamicAddMul2.splay(x)
        Code01_DynamicAddMul2.down(x)
        while (Code01_DynamicAddMul2.ls[x] != 0):
            x = jcast('int', Code01_DynamicAddMul2.ls[x])
            Code01_DynamicAddMul2.down(x)
        Code01_DynamicAddMul2.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code01_DynamicAddMul2.makeroot(x)
        Code01_DynamicAddMul2.access(y)
        Code01_DynamicAddMul2.splay(y)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code01_DynamicAddMul2.makeroot(x)
        if (Code01_DynamicAddMul2.findroot(y) != x):
            Code01_DynamicAddMul2.fa[x] = jcast('int', y)

    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code01_DynamicAddMul2.makeroot(x)
        if ((((Code01_DynamicAddMul2.findroot(y) == x) and (Code01_DynamicAddMul2.fa[y] == x)) and (Code01_DynamicAddMul2.ls[y] == 0)) and (Code01_DynamicAddMul2.rs[x] == y)):
            jset(Code01_DynamicAddMul2.fa, y, jset(Code01_DynamicAddMul2.rs, x, 0))
            Code01_DynamicAddMul2.up(x)

    @staticmethod
    def main(args):
        in_ = Code01_DynamicAddMul2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_DynamicAddMul2.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_DynamicAddMul2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_DynamicAddMul2.n):
            Code01_DynamicAddMul2.siz[i] = jcast('int', 1)
            Code01_DynamicAddMul2.arr[i] = jcast('long', 1)
            Code01_DynamicAddMul2.sum[i] = jcast('long', 1)
            Code01_DynamicAddMul2.mulTag[i] = jcast('long', 1)
            Code01_DynamicAddMul2.addTag[i] = jcast('long', 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i < Code01_DynamicAddMul2.n):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            Code01_DynamicAddMul2.link(x, y)
            i = jcast('int', (i + 1))
        op = None
        x = 0
        y = 0
        z = 0
        a = 0
        b = 0
        i = jcast('int', 1)
        while (i <= Code01_DynamicAddMul2.q):
            op = jcall(in_, 'nextString')
            if jcall(op, 'equals', '+'):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                z = jcast('int', jcall(in_, 'nextInt'))
                z = jcast('int', jcast('int', jmod(z, Code01_DynamicAddMul2.MOD)))
                Code01_DynamicAddMul2.split(x, y)
                Code01_DynamicAddMul2.effect(y, 1, z)
            else:
                if jcall(op, 'equals', '*'):
                    x = jcast('int', jcall(in_, 'nextInt'))
                    y = jcast('int', jcall(in_, 'nextInt'))
                    z = jcast('int', jcall(in_, 'nextInt'))
                    z = jcast('int', jcast('int', jmod(z, Code01_DynamicAddMul2.MOD)))
                    Code01_DynamicAddMul2.split(x, y)
                    Code01_DynamicAddMul2.effect(y, z, 0)
                else:
                    if jcall(op, 'equals', '-'):
                        x = jcast('int', jcall(in_, 'nextInt'))
                        y = jcast('int', jcall(in_, 'nextInt'))
                        a = jcast('int', jcall(in_, 'nextInt'))
                        b = jcast('int', jcall(in_, 'nextInt'))
                        Code01_DynamicAddMul2.cut(x, y)
                        Code01_DynamicAddMul2.link(a, b)
                    else:
                        x = jcast('int', jcall(in_, 'nextInt'))
                        y = jcast('int', jcall(in_, 'nextInt'))
                        Code01_DynamicAddMul2.split(x, y)
                        jcall(out, 'println', Code01_DynamicAddMul2.sum[y])
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
            raise TypeError("No matching overload for Code01_DynamicAddMul2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_DynamicAddMul2.MAXN = jcast('int', 100001)
Code01_DynamicAddMul2.MOD = jcast('int', 51061)
Code01_DynamicAddMul2.n = jcast('int', 0)
Code01_DynamicAddMul2.q = jcast('int', 0)
Code01_DynamicAddMul2.fa = jarray('int', [Code01_DynamicAddMul2.MAXN])
Code01_DynamicAddMul2.ls = jarray('int', [Code01_DynamicAddMul2.MAXN])
Code01_DynamicAddMul2.rs = jarray('int', [Code01_DynamicAddMul2.MAXN])
Code01_DynamicAddMul2.sta = jarray('int', [Code01_DynamicAddMul2.MAXN])
Code01_DynamicAddMul2.rev = jarray('boolean', [Code01_DynamicAddMul2.MAXN])
Code01_DynamicAddMul2.siz = jarray('int', [Code01_DynamicAddMul2.MAXN])
Code01_DynamicAddMul2.arr = jarray('long', [Code01_DynamicAddMul2.MAXN])
Code01_DynamicAddMul2.sum = jarray('long', [Code01_DynamicAddMul2.MAXN])
Code01_DynamicAddMul2.mulTag = jarray('long', [Code01_DynamicAddMul2.MAXN])
Code01_DynamicAddMul2.addTag = jarray('long', [Code01_DynamicAddMul2.MAXN])

if __name__ == '__main__':
    Code01_DynamicAddMul2.main([])
