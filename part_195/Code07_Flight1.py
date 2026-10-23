# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 航线规划，Python版
# 一共有n个点，m条无向边，任何时刻图连通，没有重边
# 一共有q条操作，操作有两种类型，具体格式如下
# 操作 0 x y : 删除点x和点y之间的直接边
# 操作 1 x y : 查询点x和点y之间有多少条必经边
# 1 <= n <= 3 * 10^4
# 1 <= m <= 10^5
# 1 <= q <= 4 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P2542
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_Flight1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXQ': 'MAXQ', 'n': 'n', 'm': 'm', 'q': 'q', 'ex': 'ex', 'ey': 'ey', 'qop': 'qop', 'qx': 'qx', 'qy': 'qy', 'queryAns': 'queryAns', 'queryCnt': 'queryCnt', 'deleted': 'deleted', 'edgeMap': 'edgeMap', 'father': 'father', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'rev': 'rev', 'sta': 'sta', 'ebcc': 'ebcc'}
    MAXN = 0
    MAXM = 0
    MAXQ = 0
    n = 0
    m = 0
    q = 0
    ex = None
    ey = None
    qop = None
    qx = None
    qy = None
    queryAns = None
    queryCnt = 0
    deleted = None
    edgeMap = None
    # 并查集，维护每个点归属的边双连通分量
    father = None
    # 辅助splay
    fa = None
    ls = None
    rs = None
    rev = None
    sta = None
    # ebcc[x]表示以x为根的辅助splay，有多少个边双连通分量
    ebcc = None
    @staticmethod
    def find(x):
        x = jcast('int', x)
        if (x != Code07_Flight1.father[x]):
            jset(Code07_Flight1.father, x, Code07_Flight1.find(Code07_Flight1.father[x]))
        return jcast('int', Code07_Flight1.father[x])

    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code07_Flight1.ebcc[x] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code07_Flight1.ebcc[Code07_Flight1.ls[x]], Code07_Flight1.ebcc[Code07_Flight1.rs[x]])), 1)))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code07_Flight1.ls[Code07_Flight1.fa[x]] != x) and (Code07_Flight1.rs[Code07_Flight1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code07_Flight1.ls[Code07_Flight1.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code07_Flight1.ls[x])
            Code07_Flight1.ls[x] = jcast('int', Code07_Flight1.rs[x])
            Code07_Flight1.rs[x] = jcast('int', tmp)
            Code07_Flight1.rev[x] = jcast('boolean', (not Code07_Flight1.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code07_Flight1.rev[x]:
            Code07_Flight1.reverse(Code07_Flight1.ls[x])
            Code07_Flight1.reverse(Code07_Flight1.rs[x])
            Code07_Flight1.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code07_Flight1.fa[x])
        g = jcast('int', Code07_Flight1.fa[f])
        if (Code07_Flight1.lr(x) == 0):
            Code07_Flight1.ls[f] = jcast('int', Code07_Flight1.rs[x])
            if (Code07_Flight1.ls[f] != 0):
                jset(Code07_Flight1.fa, Code07_Flight1.ls[f], f)
            Code07_Flight1.rs[x] = jcast('int', f)
        else:
            Code07_Flight1.rs[f] = jcast('int', Code07_Flight1.ls[x])
            if (Code07_Flight1.rs[f] != 0):
                jset(Code07_Flight1.fa, Code07_Flight1.rs[f], f)
            Code07_Flight1.ls[x] = jcast('int', f)
        if (not Code07_Flight1.isroot(f)):
            if (Code07_Flight1.lr(f) == 0):
                Code07_Flight1.ls[g] = jcast('int', x)
            else:
                Code07_Flight1.rs[g] = jcast('int', x)
        Code07_Flight1.fa[f] = jcast('int', x)
        Code07_Flight1.fa[x] = jcast('int', g)
        Code07_Flight1.up(f)
        Code07_Flight1.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code07_Flight1.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code07_Flight1.isroot(y)):
            jset(Code07_Flight1.sta, (siz := jcast('int', (siz + (1)))), Code07_Flight1.fa[y])
            y = jcast('int', Code07_Flight1.fa[y])
        while (siz != 0):
            Code07_Flight1.down(Code07_Flight1.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code07_Flight1.isroot(x)):
            f = jcast('int', Code07_Flight1.fa[x])
            if (not Code07_Flight1.isroot(f)):
                if (Code07_Flight1.lr(x) == Code07_Flight1.lr(f)):
                    Code07_Flight1.rotate(f)
                else:
                    Code07_Flight1.rotate(x)
            Code07_Flight1.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        x = jcast('int', Code07_Flight1.find(x))
        y = jcast('int', 0)
        while (x != 0):
            Code07_Flight1.splay(x)
            Code07_Flight1.rs[x] = jcast('int', y)
            Code07_Flight1.up(x)
            jset(Code07_Flight1.fa, x, Code07_Flight1.find(Code07_Flight1.fa[x]))
            y = jcast('int', x)
            x = jcast('int', Code07_Flight1.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code07_Flight1.access(x)
        Code07_Flight1.splay(x)
        Code07_Flight1.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code07_Flight1.access(x)
        Code07_Flight1.splay(x)
        Code07_Flight1.down(x)
        while (Code07_Flight1.ls[x] != 0):
            x = jcast('int', Code07_Flight1.ls[x])
            Code07_Flight1.down(x)
        Code07_Flight1.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code07_Flight1.makeroot(x)
        Code07_Flight1.access(y)
        Code07_Flight1.splay(y)

    @staticmethod
    def condense(x, root):
        x = jcast('int', x)
        root = jcast('int', root)
        if (x != 0):
            Code07_Flight1.father[x] = jcast('int', root)
            Code07_Flight1.condense(Code07_Flight1.ls[x], root)
            Code07_Flight1.condense(Code07_Flight1.rs[x], root)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        x = jcast('int', Code07_Flight1.find(x))
        y = jcast('int', Code07_Flight1.find(y))
        if (x == y):
            return
        Code07_Flight1.makeroot(x)
        if (Code07_Flight1.findroot(y) != x):
            Code07_Flight1.fa[x] = jcast('int', y)
        else:
            Code07_Flight1.condense(Code07_Flight1.rs[x], x)
            Code07_Flight1.rs[x] = jcast('int', 0)
            Code07_Flight1.up(x)

    @staticmethod
    def key(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        a = jcast('int', jstatic('Math', 'min', x, y))
        b = jcast('int', jstatic('Math', 'max', x, y))
        return jcast('long', jcast('long', (jcast('long', (jcast('long', a) << (32 & 63))) | b)))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code07_Flight1.n):
            Code07_Flight1.father[i] = jcast('int', i)
            Code07_Flight1.ebcc[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_Flight1.m):
            jcall(Code07_Flight1.edgeMap, 'put', Code07_Flight1.key(Code07_Flight1.ex[i], Code07_Flight1.ey[i]), i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_Flight1.q):
            if (Code07_Flight1.qop[i] == 0):
                jset(Code07_Flight1.deleted, jcall(Code07_Flight1.edgeMap, 'get', Code07_Flight1.key(Code07_Flight1.qx[i], Code07_Flight1.qy[i])), True)
            else:
                Code07_Flight1.queryCnt = jcast('int', (Code07_Flight1.queryCnt + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_Flight1.m):
            if (not Code07_Flight1.deleted[i]):
                Code07_Flight1.link(Code07_Flight1.ex[i], Code07_Flight1.ey[i])
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code07_Flight1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_Flight1.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_Flight1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_Flight1.m):
            jset(Code07_Flight1.ex, i, jcall(in_, 'nextInt'))
            jset(Code07_Flight1.ey, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        op = jcast('int', jcall(in_, 'nextInt'))
        while (op != jcast('int', (-1))):
            jset(Code07_Flight1.qop, ((_java_obj_2 := Code07_Flight1), (_java_key_3 := 'q'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))))[3], op)
            jset(Code07_Flight1.qx, Code07_Flight1.q, jcall(in_, 'nextInt'))
            jset(Code07_Flight1.qy, Code07_Flight1.q, jcall(in_, 'nextInt'))
            op = jcast('int', jcall(in_, 'nextInt'))
        Code07_Flight1.prepare()
        i = jcast('int', Code07_Flight1.q)
        j = jcast('int', Code07_Flight1.queryCnt)
        while (i >= 1):
            x = jcast('int', Code07_Flight1.find(Code07_Flight1.qx[i]))
            y = jcast('int', Code07_Flight1.find(Code07_Flight1.qy[i]))
            if (Code07_Flight1.qop[i] == 0):
                Code07_Flight1.link(x, y)
            else:
                if (x == y):
                    jset(Code07_Flight1.queryAns, ((_java_old_5 := j), (j := jcast('int', (j + (-1)))), _java_old_5)[2], 0)
                else:
                    Code07_Flight1.split(x, y)
                    jset(Code07_Flight1.queryAns, ((_java_old_6 := j), (j := jcast('int', (j + (-1)))), _java_old_6)[2], jcast('int', (Code07_Flight1.ebcc[y] - 1)))
            i = jcast('int', (i - 1))
        i = jcast('int', 1)
        while (i <= Code07_Flight1.queryCnt):
            jcall(out, 'println', Code07_Flight1.queryAns[i])
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
            return jcast('int', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

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
            raise TypeError("No matching overload for Code07_Flight1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_Flight1.MAXN = jcast('int', 30001)
Code07_Flight1.MAXM = jcast('int', 100001)
Code07_Flight1.MAXQ = jcast('int', 40001)
Code07_Flight1.n = jcast('int', 0)
Code07_Flight1.m = jcast('int', 0)
Code07_Flight1.q = jcast('int', 0)
Code07_Flight1.ex = jarray('int', [Code07_Flight1.MAXM])
Code07_Flight1.ey = jarray('int', [Code07_Flight1.MAXM])
Code07_Flight1.qop = jarray('int', [Code07_Flight1.MAXQ])
Code07_Flight1.qx = jarray('int', [Code07_Flight1.MAXQ])
Code07_Flight1.qy = jarray('int', [Code07_Flight1.MAXQ])
Code07_Flight1.queryAns = jarray('int', [Code07_Flight1.MAXQ])
Code07_Flight1.queryCnt = jcast('int', 0)
Code07_Flight1.deleted = jarray('boolean', [Code07_Flight1.MAXM])
Code07_Flight1.edgeMap = jnew('HashMap')
Code07_Flight1.father = jarray('int', [Code07_Flight1.MAXN])
Code07_Flight1.fa = jarray('int', [Code07_Flight1.MAXN])
Code07_Flight1.ls = jarray('int', [Code07_Flight1.MAXN])
Code07_Flight1.rs = jarray('int', [Code07_Flight1.MAXN])
Code07_Flight1.rev = jarray('boolean', [Code07_Flight1.MAXN])
Code07_Flight1.sta = jarray('int', [Code07_Flight1.MAXN])
Code07_Flight1.ebcc = jarray('int', [Code07_Flight1.MAXN])

if __name__ == '__main__':
    Code07_Flight1.main([])
