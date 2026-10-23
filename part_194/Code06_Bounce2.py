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

# 弹飞绵羊，Python版
# 一共n个装置，编号0~n-1，从左到右摆成一条直线
# 每个装置给定弹力f，比如3号装置弹力为5，则从3号装置可以向右跳到8号装置
# 如果跳到的位置 >= n，也就是不存在这个装置，则认为被弹飞
# 一共m条操作，操作类型如下
# 操作 1 x   : 查询从x号装置出发，跳几次会弹飞
# 操作 2 x y : x号装置的弹力修改成y
# 1 <= n <= 2 * 10^5
# 1 <= m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3203
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_Bounce2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'force': 'force', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'sta': 'sta', 'rev': 'rev', 'siz': 'siz'}
    MAXN = 0
    n = 0
    m = 0
    force = None
    fa = None
    ls = None
    rs = None
    sta = None
    rev = None
    # 节点数量
    siz = None
    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code06_Bounce2.siz[x] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code06_Bounce2.siz[Code06_Bounce2.ls[x]], Code06_Bounce2.siz[Code06_Bounce2.rs[x]])), 1)))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code06_Bounce2.ls[Code06_Bounce2.fa[x]] != x) and (Code06_Bounce2.rs[Code06_Bounce2.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code06_Bounce2.ls[Code06_Bounce2.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code06_Bounce2.ls[x])
            Code06_Bounce2.ls[x] = jcast('int', Code06_Bounce2.rs[x])
            Code06_Bounce2.rs[x] = jcast('int', tmp)
            Code06_Bounce2.rev[x] = jcast('boolean', (not Code06_Bounce2.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code06_Bounce2.rev[x]:
            Code06_Bounce2.reverse(Code06_Bounce2.ls[x])
            Code06_Bounce2.reverse(Code06_Bounce2.rs[x])
            Code06_Bounce2.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code06_Bounce2.fa[x])
        g = jcast('int', Code06_Bounce2.fa[f])
        if (Code06_Bounce2.lr(x) == 0):
            Code06_Bounce2.ls[f] = jcast('int', Code06_Bounce2.rs[x])
            if (Code06_Bounce2.ls[f] != 0):
                jset(Code06_Bounce2.fa, Code06_Bounce2.ls[f], f)
            Code06_Bounce2.rs[x] = jcast('int', f)
        else:
            Code06_Bounce2.rs[f] = jcast('int', Code06_Bounce2.ls[x])
            if (Code06_Bounce2.rs[f] != 0):
                jset(Code06_Bounce2.fa, Code06_Bounce2.rs[f], f)
            Code06_Bounce2.ls[x] = jcast('int', f)
        if (not Code06_Bounce2.isroot(f)):
            if (Code06_Bounce2.lr(f) == 0):
                Code06_Bounce2.ls[g] = jcast('int', x)
            else:
                Code06_Bounce2.rs[g] = jcast('int', x)
        Code06_Bounce2.fa[f] = jcast('int', x)
        Code06_Bounce2.fa[x] = jcast('int', g)
        Code06_Bounce2.up(f)
        Code06_Bounce2.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code06_Bounce2.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code06_Bounce2.isroot(y)):
            jset(Code06_Bounce2.sta, (siz := jcast('int', (siz + (1)))), Code06_Bounce2.fa[y])
            y = jcast('int', Code06_Bounce2.fa[y])
        while (siz != 0):
            Code06_Bounce2.down(Code06_Bounce2.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code06_Bounce2.isroot(x)):
            f = jcast('int', Code06_Bounce2.fa[x])
            if (not Code06_Bounce2.isroot(f)):
                if (Code06_Bounce2.lr(x) == Code06_Bounce2.lr(f)):
                    Code06_Bounce2.rotate(f)
                else:
                    Code06_Bounce2.rotate(x)
            Code06_Bounce2.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code06_Bounce2.splay(x)
            Code06_Bounce2.rs[x] = jcast('int', y)
            Code06_Bounce2.up(x)
            y = jcast('int', x)
            x = jcast('int', Code06_Bounce2.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code06_Bounce2.access(x)
        Code06_Bounce2.splay(x)
        Code06_Bounce2.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code06_Bounce2.access(x)
        Code06_Bounce2.splay(x)
        Code06_Bounce2.down(x)
        while (Code06_Bounce2.ls[x] != 0):
            x = jcast('int', Code06_Bounce2.ls[x])
            Code06_Bounce2.down(x)
        Code06_Bounce2.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code06_Bounce2.makeroot(x)
        Code06_Bounce2.access(y)
        Code06_Bounce2.splay(y)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code06_Bounce2.makeroot(x)
        if (Code06_Bounce2.findroot(y) != x):
            Code06_Bounce2.fa[x] = jcast('int', y)

    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code06_Bounce2.makeroot(x)
        if ((((Code06_Bounce2.findroot(y) == x) and (Code06_Bounce2.fa[y] == x)) and (Code06_Bounce2.ls[y] == 0)) and (Code06_Bounce2.rs[x] == y)):
            jset(Code06_Bounce2.fa, y, jset(Code06_Bounce2.rs, x, 0))
            Code06_Bounce2.up(x)

    @staticmethod
    def main(args):
        in_ = Code06_Bounce2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_Bounce2.n = jcast('int', jcall(in_, 'nextInt'))
        x = jcast('int', 1)
        while (x <= jcast('int', jadd(Code06_Bounce2.n, 1))):
            Code06_Bounce2.siz[x] = jcast('int', 1)
            x = jcast('int', (x + 1))
        x = jcast('int', 1)
        while (x <= Code06_Bounce2.n):
            jset(Code06_Bounce2.force, x, jcall(in_, 'nextInt'))
            Code06_Bounce2.link(x, jstatic('Math', 'min', jcast('int', jadd(x, Code06_Bounce2.force[x])), jcast('int', jadd(Code06_Bounce2.n, 1))))
            x = jcast('int', (x + 1))
        Code06_Bounce2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        while (i <= Code06_Bounce2.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', (x + 1))
            if (op == 1):
                Code06_Bounce2.split(x, jcast('int', jadd(Code06_Bounce2.n, 1)))
                jcall(out, 'println', jcast('int', (Code06_Bounce2.siz[jcast('int', jadd(Code06_Bounce2.n, 1))] - 1)))
            else:
                y = jcast('int', jcall(in_, 'nextInt'))
                Code06_Bounce2.cut(x, jstatic('Math', 'min', jcast('int', jadd(x, Code06_Bounce2.force[x])), jcast('int', jadd(Code06_Bounce2.n, 1))))
                Code06_Bounce2.force[x] = jcast('int', y)
                Code06_Bounce2.link(x, jstatic('Math', 'min', jcast('int', jadd(x, Code06_Bounce2.force[x])), jcast('int', jadd(Code06_Bounce2.n, 1))))
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
            raise TypeError("No matching overload for Code06_Bounce2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_Bounce2.MAXN = jcast('int', 200002)
Code06_Bounce2.n = jcast('int', 0)
Code06_Bounce2.m = jcast('int', 0)
Code06_Bounce2.force = jarray('int', [Code06_Bounce2.MAXN])
Code06_Bounce2.fa = jarray('int', [Code06_Bounce2.MAXN])
Code06_Bounce2.ls = jarray('int', [Code06_Bounce2.MAXN])
Code06_Bounce2.rs = jarray('int', [Code06_Bounce2.MAXN])
Code06_Bounce2.sta = jarray('int', [Code06_Bounce2.MAXN])
Code06_Bounce2.rev = jarray('boolean', [Code06_Bounce2.MAXN])
Code06_Bounce2.siz = jarray('int', [Code06_Bounce2.MAXN])

if __name__ == '__main__':
    Code06_Bounce2.main([])
