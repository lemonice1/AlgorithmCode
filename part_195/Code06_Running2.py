# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 长跑，Python版
# 一共n个点，每个点有点权，初始没有边，接下来有m条操作，格式如下
# 操作 1 x y : 点x和点y之间增加无向边
# 操作 2 x y : 点x的点权变成y
# 操作 3 x y : 每条边需要指定方向变成单向边，希望点x到点y的过程中
# 获得最多的点权累加和，重复经过某点只获得一次点权
# 打印能获得的点权累加和最大值，如果不连通打印-1
# 指定边的方向仅影响本次操作，不会影响后续操作
# 1 <= n <= 1.5 * 10^5    1 <= m <= 5 * n
# 测试链接 : https://www.luogu.com.cn/problem/P10658
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_Running2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'father': 'father', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'rev': 'rev', 'sta': 'sta', 'arr': 'arr', 'sum': 'sum', 'sumOfSum': 'sumOfSum'}
    MAXN = 0
    n = 0
    m = 0
    father = None
    fa = None
    ls = None
    rs = None
    rev = None
    sta = None
    # 单点的点权
    arr = None
    # sum[x]表示x代表的边双连通分量中，点权累加和
    sum = None
    # sumOfSum[x]表示以x为根的辅助splay中，点权累加和
    # 也就是整条实链的点权累加和，实链上的每个点，可能是代表点
    sumOfSum = None
    @staticmethod
    def find(x):
        x = jcast('int', x)
        if (x != Code06_Running2.father[x]):
            jset(Code06_Running2.father, x, Code06_Running2.find(Code06_Running2.father[x]))
        return jcast('int', Code06_Running2.father[x])

    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code06_Running2.sumOfSum[x] = jcast('long', jcast('long', jadd(jcast('long', jadd(Code06_Running2.sumOfSum[Code06_Running2.ls[x]], Code06_Running2.sumOfSum[Code06_Running2.rs[x]])), Code06_Running2.sum[x])))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code06_Running2.ls[Code06_Running2.fa[x]] != x) and (Code06_Running2.rs[Code06_Running2.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code06_Running2.ls[Code06_Running2.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code06_Running2.ls[x])
            Code06_Running2.ls[x] = jcast('int', Code06_Running2.rs[x])
            Code06_Running2.rs[x] = jcast('int', tmp)
            Code06_Running2.rev[x] = jcast('boolean', (not Code06_Running2.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code06_Running2.rev[x]:
            Code06_Running2.reverse(Code06_Running2.ls[x])
            Code06_Running2.reverse(Code06_Running2.rs[x])
            Code06_Running2.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code06_Running2.fa[x])
        g = jcast('int', Code06_Running2.fa[f])
        if (Code06_Running2.lr(x) == 0):
            Code06_Running2.ls[f] = jcast('int', Code06_Running2.rs[x])
            if (Code06_Running2.ls[f] != 0):
                jset(Code06_Running2.fa, Code06_Running2.ls[f], f)
            Code06_Running2.rs[x] = jcast('int', f)
        else:
            Code06_Running2.rs[f] = jcast('int', Code06_Running2.ls[x])
            if (Code06_Running2.rs[f] != 0):
                jset(Code06_Running2.fa, Code06_Running2.rs[f], f)
            Code06_Running2.ls[x] = jcast('int', f)
        if (not Code06_Running2.isroot(f)):
            if (Code06_Running2.lr(f) == 0):
                Code06_Running2.ls[g] = jcast('int', x)
            else:
                Code06_Running2.rs[g] = jcast('int', x)
        Code06_Running2.fa[f] = jcast('int', x)
        Code06_Running2.fa[x] = jcast('int', g)
        Code06_Running2.up(f)
        Code06_Running2.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code06_Running2.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code06_Running2.isroot(y)):
            jset(Code06_Running2.sta, (siz := jcast('int', (siz + (1)))), Code06_Running2.fa[y])
            y = jcast('int', Code06_Running2.fa[y])
        while (siz != 0):
            Code06_Running2.down(Code06_Running2.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code06_Running2.isroot(x)):
            f = jcast('int', Code06_Running2.fa[x])
            if (not Code06_Running2.isroot(f)):
                if (Code06_Running2.lr(x) == Code06_Running2.lr(f)):
                    Code06_Running2.rotate(f)
                else:
                    Code06_Running2.rotate(x)
            Code06_Running2.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        x = jcast('int', Code06_Running2.find(x))
        y = jcast('int', 0)
        while (x != 0):
            Code06_Running2.splay(x)
            Code06_Running2.rs[x] = jcast('int', y)
            Code06_Running2.up(x)
            jset(Code06_Running2.fa, x, Code06_Running2.find(Code06_Running2.fa[x]))
            y = jcast('int', x)
            x = jcast('int', Code06_Running2.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code06_Running2.access(x)
        Code06_Running2.splay(x)
        Code06_Running2.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code06_Running2.access(x)
        Code06_Running2.splay(x)
        Code06_Running2.down(x)
        while (Code06_Running2.ls[x] != 0):
            x = jcast('int', Code06_Running2.ls[x])
            Code06_Running2.down(x)
        Code06_Running2.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code06_Running2.makeroot(x)
        Code06_Running2.access(y)
        Code06_Running2.splay(y)

    @staticmethod
    def condense(x, root):
        x = jcast('int', x)
        root = jcast('int', root)
        if (x != 0):
            Code06_Running2.father[x] = jcast('int', root)
            Code06_Running2.sum[root] = jcast('long', jcast('long', jadd(Code06_Running2.sum[root], Code06_Running2.sum[x])))
            Code06_Running2.condense(Code06_Running2.ls[x], root)
            Code06_Running2.condense(Code06_Running2.rs[x], root)

    # 如果两点不连通就连接，如果连通，说明形成环，缩成一个边双
    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        x = jcast('int', Code06_Running2.find(x))
        y = jcast('int', Code06_Running2.find(y))
        if (x == y):
            return
        Code06_Running2.makeroot(x)
        if (Code06_Running2.findroot(y) != x):
            Code06_Running2.fa[x] = jcast('int', y)
        else:
            Code06_Running2.condense(Code06_Running2.rs[x], x)
            Code06_Running2.rs[x] = jcast('int', 0)
            Code06_Running2.up(x)

    # 修改点权
    @staticmethod
    def update(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        delta = jcast('long', jcast('long', (y - Code06_Running2.arr[x])))
        Code06_Running2.arr[x] = jcast('long', y)
        x = jcast('int', Code06_Running2.find(x))
        Code06_Running2.makeroot(x)
        Code06_Running2.sum[x] = jcast('long', jcast('long', jadd(Code06_Running2.sum[x], delta)))
        Code06_Running2.up(x)

    # 查询两点路径上，所有边双连通分量的权值和
    @staticmethod
    def query(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        x = jcast('int', Code06_Running2.find(x))
        y = jcast('int', Code06_Running2.find(y))
        if (Code06_Running2.findroot(x) != Code06_Running2.findroot(y)):
            return jcast('long', jcast('int', (-1)))
        Code06_Running2.split(x, y)
        return jcast('long', Code06_Running2.sumOfSum[y])

    @staticmethod
    def main(args):
        in_ = Code06_Running2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_Running2.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_Running2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_Running2.n):
            Code06_Running2.father[i] = jcast('int', i)
            jset(Code06_Running2.arr, i, jcall(in_, 'nextInt'))
            Code06_Running2.sum[i] = jcast('long', Code06_Running2.arr[i])
            Code06_Running2.sumOfSum[i] = jcast('long', Code06_Running2.arr[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        while (i <= Code06_Running2.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                Code06_Running2.link(x, y)
            else:
                if (op == 2):
                    Code06_Running2.update(x, y)
                else:
                    jcall(out, 'println', Code06_Running2.query(x, y))
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
            raise TypeError("No matching overload for Code06_Running2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_Running2.MAXN = jcast('int', 200001)
Code06_Running2.n = jcast('int', 0)
Code06_Running2.m = jcast('int', 0)
Code06_Running2.father = jarray('int', [Code06_Running2.MAXN])
Code06_Running2.fa = jarray('int', [Code06_Running2.MAXN])
Code06_Running2.ls = jarray('int', [Code06_Running2.MAXN])
Code06_Running2.rs = jarray('int', [Code06_Running2.MAXN])
Code06_Running2.rev = jarray('boolean', [Code06_Running2.MAXN])
Code06_Running2.sta = jarray('int', [Code06_Running2.MAXN])
Code06_Running2.arr = jarray('long', [Code06_Running2.MAXN])
Code06_Running2.sum = jarray('long', [Code06_Running2.MAXN])
Code06_Running2.sumOfSum = jarray('long', [Code06_Running2.MAXN])

if __name__ == '__main__':
    Code06_Running2.main([])
