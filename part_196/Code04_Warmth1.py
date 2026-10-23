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

# 温暖会指引我们前行，Python版
# 一共n个地点，地点之间的道路是无向边，每条道路有温度和长度两种权值
# 初始时没有任何道路，之后出现的所有道路，温度互不相同
# 对于点x到点y的每一条路径，将路径上的道路按温度升序排列，形成该路径的温度序列
# 温度序列字典序最大的路径叫做最佳路径，因为道路温度互不相同，所以最佳路径唯一
# 接下来有m条操作，操作类型有三种，具体格式如下
# find e x y t l : 建立编号为e的边，端点x和y、温度t、长度l，编号保证唯一
# move x y       : 打印点x到点y最佳路径的长度总和，如果不连通打印-1
# change e l     : 编号为e的道路长度修改为l，该道路保证已经建立
# 1 <= n <= 10^5    1 <= m <= 3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P6664
# 测试链接 : https://uoj.ac/problem/274
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Warmth1:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'm': 'm', 'ex': 'ex', 'ey': 'ey', 'et': 'et', 'el': 'el', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'rev': 'rev', 'sta': 'sta', 'sum': 'sum', 'mintEdge': 'mintEdge'}
    MAXN = 0
    INF = 0
    n = 0
    m = 0
    ex = None
    ey = None
    et = None
    el = None
    # 辅助splay
    fa = None
    ls = None
    rs = None
    rev = None
    sta = None
    # sumLen[x]表示以x为根的辅助splay中，边长累加和
    sum = None
    # minEdge[x]表示以x为根的辅助splay中，温度最低的边的编号
    mintEdge = None
    @staticmethod
    def up(x):
        x = jcast('int', x)
        e = jcast('int', (0 if (x <= Code04_Warmth1.n) else jcast('int', (x - Code04_Warmth1.n))))
        Code04_Warmth1.sum[x] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code04_Warmth1.sum[Code04_Warmth1.ls[x]], Code04_Warmth1.sum[Code04_Warmth1.rs[x]])), Code04_Warmth1.el[e])))
        Code04_Warmth1.mintEdge[x] = jcast('int', e)
        if (Code04_Warmth1.et[Code04_Warmth1.mintEdge[Code04_Warmth1.ls[x]]] < Code04_Warmth1.et[Code04_Warmth1.mintEdge[x]]):
            Code04_Warmth1.mintEdge[x] = jcast('int', Code04_Warmth1.mintEdge[Code04_Warmth1.ls[x]])
        if (Code04_Warmth1.et[Code04_Warmth1.mintEdge[Code04_Warmth1.rs[x]]] < Code04_Warmth1.et[Code04_Warmth1.mintEdge[x]]):
            Code04_Warmth1.mintEdge[x] = jcast('int', Code04_Warmth1.mintEdge[Code04_Warmth1.rs[x]])

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code04_Warmth1.ls[Code04_Warmth1.fa[x]] != x) and (Code04_Warmth1.rs[Code04_Warmth1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code04_Warmth1.ls[Code04_Warmth1.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code04_Warmth1.ls[x])
            Code04_Warmth1.ls[x] = jcast('int', Code04_Warmth1.rs[x])
            Code04_Warmth1.rs[x] = jcast('int', tmp)
            Code04_Warmth1.rev[x] = jcast('boolean', (not Code04_Warmth1.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code04_Warmth1.rev[x]:
            Code04_Warmth1.reverse(Code04_Warmth1.ls[x])
            Code04_Warmth1.reverse(Code04_Warmth1.rs[x])
            Code04_Warmth1.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code04_Warmth1.fa[x])
        g = jcast('int', Code04_Warmth1.fa[f])
        if (Code04_Warmth1.lr(x) == 0):
            Code04_Warmth1.ls[f] = jcast('int', Code04_Warmth1.rs[x])
            if (Code04_Warmth1.ls[f] != 0):
                jset(Code04_Warmth1.fa, Code04_Warmth1.ls[f], f)
            Code04_Warmth1.rs[x] = jcast('int', f)
        else:
            Code04_Warmth1.rs[f] = jcast('int', Code04_Warmth1.ls[x])
            if (Code04_Warmth1.rs[f] != 0):
                jset(Code04_Warmth1.fa, Code04_Warmth1.rs[f], f)
            Code04_Warmth1.ls[x] = jcast('int', f)
        if (not Code04_Warmth1.isroot(f)):
            if (Code04_Warmth1.lr(f) == 0):
                Code04_Warmth1.ls[g] = jcast('int', x)
            else:
                Code04_Warmth1.rs[g] = jcast('int', x)
        Code04_Warmth1.fa[f] = jcast('int', x)
        Code04_Warmth1.fa[x] = jcast('int', g)
        Code04_Warmth1.up(f)
        Code04_Warmth1.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code04_Warmth1.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code04_Warmth1.isroot(y)):
            jset(Code04_Warmth1.sta, (siz := jcast('int', (siz + (1)))), Code04_Warmth1.fa[y])
            y = jcast('int', Code04_Warmth1.fa[y])
        while (siz != 0):
            Code04_Warmth1.down(Code04_Warmth1.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code04_Warmth1.isroot(x)):
            f = jcast('int', Code04_Warmth1.fa[x])
            if (not Code04_Warmth1.isroot(f)):
                if (Code04_Warmth1.lr(x) == Code04_Warmth1.lr(f)):
                    Code04_Warmth1.rotate(f)
                else:
                    Code04_Warmth1.rotate(x)
            Code04_Warmth1.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code04_Warmth1.splay(x)
            Code04_Warmth1.rs[x] = jcast('int', y)
            Code04_Warmth1.up(x)
            y = jcast('int', x)
            x = jcast('int', Code04_Warmth1.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code04_Warmth1.access(x)
        Code04_Warmth1.splay(x)
        Code04_Warmth1.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code04_Warmth1.access(x)
        Code04_Warmth1.splay(x)
        Code04_Warmth1.down(x)
        while (Code04_Warmth1.ls[x] != 0):
            x = jcast('int', Code04_Warmth1.ls[x])
            Code04_Warmth1.down(x)
        Code04_Warmth1.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code04_Warmth1.makeroot(x)
        Code04_Warmth1.access(y)
        Code04_Warmth1.splay(y)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code04_Warmth1.makeroot(x)
        if (Code04_Warmth1.findroot(y) != x):
            Code04_Warmth1.fa[x] = jcast('int', y)

    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code04_Warmth1.makeroot(x)
        if ((((Code04_Warmth1.findroot(y) == x) and (Code04_Warmth1.fa[y] == x)) and (Code04_Warmth1.ls[y] == 0)) and (Code04_Warmth1.rs[x] == y)):
            jset(Code04_Warmth1.fa, y, jset(Code04_Warmth1.rs, x, 0))
            Code04_Warmth1.up(x)

    @staticmethod
    def addEdge(e):
        e = jcast('int', e)
        x = jcast('int', Code04_Warmth1.ex[e])
        y = jcast('int', Code04_Warmth1.ey[e])
        Code04_Warmth1.makeroot(x)
        if (Code04_Warmth1.findroot(y) != x):
            Code04_Warmth1.link(x, jcast('int', jadd(Code04_Warmth1.n, e)))
            Code04_Warmth1.link(y, jcast('int', jadd(Code04_Warmth1.n, e)))
        else:
            Code04_Warmth1.split(x, y)
            p = jcast('int', Code04_Warmth1.mintEdge[y])
            if (Code04_Warmth1.et[e] > Code04_Warmth1.et[p]):
                Code04_Warmth1.cut(Code04_Warmth1.ex[p], jcast('int', jadd(Code04_Warmth1.n, p)))
                Code04_Warmth1.cut(Code04_Warmth1.ey[p], jcast('int', jadd(Code04_Warmth1.n, p)))
                Code04_Warmth1.link(x, jcast('int', jadd(Code04_Warmth1.n, e)))
                Code04_Warmth1.link(y, jcast('int', jadd(Code04_Warmth1.n, e)))

    @staticmethod
    def change(e, l):
        e = jcast('int', e)
        l = jcast('int', l)
        Code04_Warmth1.splay(jcast('int', jadd(Code04_Warmth1.n, e)))
        Code04_Warmth1.el[e] = jcast('int', l)
        Code04_Warmth1.up(jcast('int', jadd(Code04_Warmth1.n, e)))

    @staticmethod
    def query(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code04_Warmth1.makeroot(x)
        if (Code04_Warmth1.findroot(y) != x):
            return jcast('int', jcast('int', (-1)))
        Code04_Warmth1.split(x, y)
        return jcast('int', Code04_Warmth1.sum[y])

    @staticmethod
    def main(args):
        in_ = Code04_Warmth1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_Warmth1.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_Warmth1.m = jcast('int', jcall(in_, 'nextInt'))
        Code04_Warmth1.et[0] = jcast('int', Code04_Warmth1.INF)
        op = None
        e = 0
        x = 0
        y = 0
        t = 0
        l = 0
        i = jcast('int', 1)
        while (i <= Code04_Warmth1.m):
            op = jcall(in_, 'nextString')
            if jcall(op, 'equals', 'find'):
                e = jcast('int', jcall(in_, 'nextInt'))
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                t = jcast('int', jcall(in_, 'nextInt'))
                l = jcast('int', jcall(in_, 'nextInt'))
                e = jcast('int', (e + 1))
                x = jcast('int', (x + 1))
                y = jcast('int', (y + 1))
                Code04_Warmth1.ex[e] = jcast('int', x)
                Code04_Warmth1.ey[e] = jcast('int', y)
                Code04_Warmth1.et[e] = jcast('int', t)
                Code04_Warmth1.el[e] = jcast('int', l)
                Code04_Warmth1.addEdge(e)
            else:
                if jcall(op, 'equals', 'move'):
                    x = jcast('int', jcall(in_, 'nextInt'))
                    y = jcast('int', jcall(in_, 'nextInt'))
                    x = jcast('int', (x + 1))
                    y = jcast('int', (y + 1))
                    jcall(out, 'println', Code04_Warmth1.query(x, y))
                else:
                    e = jcast('int', jcall(in_, 'nextInt'))
                    l = jcast('int', jcall(in_, 'nextInt'))
                    e = jcast('int', (e + 1))
                    Code04_Warmth1.change(e, l)
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
            raise TypeError("No matching overload for Code04_Warmth1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Warmth1.MAXN = jcast('int', 400001)
Code04_Warmth1.INF = jcast('int', 1000000001)
Code04_Warmth1.n = jcast('int', 0)
Code04_Warmth1.m = jcast('int', 0)
Code04_Warmth1.ex = jarray('int', [Code04_Warmth1.MAXN])
Code04_Warmth1.ey = jarray('int', [Code04_Warmth1.MAXN])
Code04_Warmth1.et = jarray('int', [Code04_Warmth1.MAXN])
Code04_Warmth1.el = jarray('int', [Code04_Warmth1.MAXN])
Code04_Warmth1.fa = jarray('int', [Code04_Warmth1.MAXN])
Code04_Warmth1.ls = jarray('int', [Code04_Warmth1.MAXN])
Code04_Warmth1.rs = jarray('int', [Code04_Warmth1.MAXN])
Code04_Warmth1.rev = jarray('boolean', [Code04_Warmth1.MAXN])
Code04_Warmth1.sta = jarray('int', [Code04_Warmth1.MAXN])
Code04_Warmth1.sum = jarray('int', [Code04_Warmth1.MAXN])
Code04_Warmth1.mintEdge = jarray('int', [Code04_Warmth1.MAXN])

if __name__ == '__main__':
    Code04_Warmth1.main([])
