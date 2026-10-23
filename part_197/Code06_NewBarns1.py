# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 查询最远距离，Python版
# 初始没有节点，接下来有q条操作，操作类型如下
# 操作 B p : 新建一个节点，并与节点p连接，如果p为-1则新建一个独立节点
# 操作 Q x : 打印节点x到所在连通块中最远节点的距离
# 1 <= q <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4271
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_NewBarns1:
    __java_fields__ = {'MAXN': 'MAXN', 'q': 'q', 'cntn': 'cntn', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'rev': 'rev', 'sta': 'sta', 'siz': 'siz', 'father': 'father', 'diameter': 'diameter', 'dl': 'dl', 'dr': 'dr'}
    MAXN = 0
    q = 0
    cntn = 0
    fa = None
    ls = None
    rs = None
    rev = None
    sta = None
    # siz[x]表示以x为根的辅助splay的节点数量
    # 节点数量-1是实链的边的数量，方便查出距离
    siz = None
    # 并查集维护连通性，连通块先查代表节点root
    # diameter[root]就是连通块的直径长度
    # dl[root]和dr[root]就是连通块的直径端点
    father = None
    diameter = None
    dl = None
    dr = None
    @staticmethod
    def find(x):
        x = jcast('int', x)
        if (Code06_NewBarns1.father[x] != x):
            jset(Code06_NewBarns1.father, x, Code06_NewBarns1.find(Code06_NewBarns1.father[x]))
        return jcast('int', Code06_NewBarns1.father[x])

    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code06_NewBarns1.siz[x] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code06_NewBarns1.siz[Code06_NewBarns1.ls[x]], Code06_NewBarns1.siz[Code06_NewBarns1.rs[x]])), 1)))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code06_NewBarns1.ls[Code06_NewBarns1.fa[x]] != x) and (Code06_NewBarns1.rs[Code06_NewBarns1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code06_NewBarns1.ls[Code06_NewBarns1.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code06_NewBarns1.ls[x])
            Code06_NewBarns1.ls[x] = jcast('int', Code06_NewBarns1.rs[x])
            Code06_NewBarns1.rs[x] = jcast('int', tmp)
            Code06_NewBarns1.rev[x] = jcast('boolean', (not Code06_NewBarns1.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code06_NewBarns1.rev[x]:
            Code06_NewBarns1.reverse(Code06_NewBarns1.ls[x])
            Code06_NewBarns1.reverse(Code06_NewBarns1.rs[x])
            Code06_NewBarns1.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code06_NewBarns1.fa[x])
        g = jcast('int', Code06_NewBarns1.fa[f])
        if (Code06_NewBarns1.lr(x) == 0):
            Code06_NewBarns1.ls[f] = jcast('int', Code06_NewBarns1.rs[x])
            if (Code06_NewBarns1.ls[f] != 0):
                jset(Code06_NewBarns1.fa, Code06_NewBarns1.ls[f], f)
            Code06_NewBarns1.rs[x] = jcast('int', f)
        else:
            Code06_NewBarns1.rs[f] = jcast('int', Code06_NewBarns1.ls[x])
            if (Code06_NewBarns1.rs[f] != 0):
                jset(Code06_NewBarns1.fa, Code06_NewBarns1.rs[f], f)
            Code06_NewBarns1.ls[x] = jcast('int', f)
        if (not Code06_NewBarns1.isroot(f)):
            if (Code06_NewBarns1.lr(f) == 0):
                Code06_NewBarns1.ls[g] = jcast('int', x)
            else:
                Code06_NewBarns1.rs[g] = jcast('int', x)
        Code06_NewBarns1.fa[f] = jcast('int', x)
        Code06_NewBarns1.fa[x] = jcast('int', g)
        Code06_NewBarns1.up(f)
        Code06_NewBarns1.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        size = jcast('int', 0)
        jset(Code06_NewBarns1.sta, (size := jcast('int', (size + (1)))), x)
        y = jcast('int', x)
        while (not Code06_NewBarns1.isroot(y)):
            jset(Code06_NewBarns1.sta, (size := jcast('int', (size + (1)))), Code06_NewBarns1.fa[y])
            y = jcast('int', Code06_NewBarns1.fa[y])
        while (size != 0):
            Code06_NewBarns1.down(Code06_NewBarns1.sta[((_java_old_1 := size), (size := jcast('int', (size + (-1)))), _java_old_1)[2]])
        while (not Code06_NewBarns1.isroot(x)):
            f = jcast('int', Code06_NewBarns1.fa[x])
            if (not Code06_NewBarns1.isroot(f)):
                if (Code06_NewBarns1.lr(x) == Code06_NewBarns1.lr(f)):
                    Code06_NewBarns1.rotate(f)
                else:
                    Code06_NewBarns1.rotate(x)
            Code06_NewBarns1.rotate(x)
        Code06_NewBarns1.up(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code06_NewBarns1.splay(x)
            Code06_NewBarns1.rs[x] = jcast('int', y)
            Code06_NewBarns1.up(x)
            y = jcast('int', x)
            x = jcast('int', Code06_NewBarns1.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code06_NewBarns1.access(x)
        Code06_NewBarns1.splay(x)
        Code06_NewBarns1.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code06_NewBarns1.access(x)
        Code06_NewBarns1.splay(x)
        Code06_NewBarns1.down(x)
        while (Code06_NewBarns1.ls[x] != 0):
            x = jcast('int', Code06_NewBarns1.ls[x])
            Code06_NewBarns1.down(x)
        Code06_NewBarns1.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code06_NewBarns1.makeroot(x)
        Code06_NewBarns1.access(y)
        Code06_NewBarns1.splay(y)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code06_NewBarns1.makeroot(x)
        if (Code06_NewBarns1.findroot(y) != x):
            Code06_NewBarns1.fa[x] = jcast('int', y)

    # 节点数量-1就是边的数量
    @staticmethod
    def getDist(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code06_NewBarns1.split(x, y)
        return jcast('int', jcast('int', (Code06_NewBarns1.siz[y] - 1)))

    @staticmethod
    def build(p):
        p = jcast('int', p)
        # 初始时，新节点是独立的连通块
        x = jcast('int', ((_java_obj_2 := Code06_NewBarns1), (_java_key_3 := 'cntn'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))))[3])
        Code06_NewBarns1.siz[x] = jcast('int', 1)
        Code06_NewBarns1.father[x] = jcast('int', x)
        Code06_NewBarns1.dl[x] = jcast('int', x)
        Code06_NewBarns1.dr[x] = jcast('int', x)
        Code06_NewBarns1.diameter[x] = jcast('int', 0)
        if (p != jcast('int', (-1))):
            # 得到原连通块的直径端点和直径长度
            root = jcast('int', Code06_NewBarns1.find(p))
            a = jcast('int', Code06_NewBarns1.dl[root])
            b = jcast('int', Code06_NewBarns1.dr[root])
            best = jcast('int', Code06_NewBarns1.diameter[root])
            bestl = jcast('int', a)
            bestr = jcast('int', b)
            Code06_NewBarns1.link(x, p)
            # 新的直径可能就是老的直径
            # 或者新节点x与旧直径的某个端点组成的路径
            dista = jcast('int', Code06_NewBarns1.getDist(x, a))
            if (dista > best):
                best = jcast('int', dista)
                bestl = jcast('int', x)
                bestr = jcast('int', a)
            distb = jcast('int', Code06_NewBarns1.getDist(x, b))
            if (distb > best):
                best = jcast('int', distb)
                bestl = jcast('int', x)
                bestr = jcast('int', b)
            Code06_NewBarns1.father[x] = jcast('int', root)
            Code06_NewBarns1.dl[root] = jcast('int', bestl)
            Code06_NewBarns1.dr[root] = jcast('int', bestr)
            Code06_NewBarns1.diameter[root] = jcast('int', best)

    # 某点在树中的最远点，一定是直径的两个端点的其中之一
    @staticmethod
    def query(x):
        x = jcast('int', x)
        fx = jcast('int', Code06_NewBarns1.find(x))
        return jcast('int', jstatic('Math', 'max', Code06_NewBarns1.getDist(x, Code06_NewBarns1.dl[fx]), Code06_NewBarns1.getDist(x, Code06_NewBarns1.dr[fx])))

    @staticmethod
    def main(args):
        in_ = Code06_NewBarns1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_NewBarns1.q = jcast('int', jcall(in_, 'nextInt'))
        op = None
        x = 0
        i = jcast('int', 1)
        while (i <= Code06_NewBarns1.q):
            op = jcall(in_, 'nextString')
            x = jcast('int', jcall(in_, 'nextInt'))
            if jcall(op, 'equals', 'B'):
                Code06_NewBarns1.build(x)
            else:
                jcall(out, 'println', Code06_NewBarns1.query(x))
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
            raise TypeError("No matching overload for Code06_NewBarns1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_NewBarns1.MAXN = jcast('int', 100001)
Code06_NewBarns1.q = jcast('int', 0)
Code06_NewBarns1.cntn = jcast('int', 0)
Code06_NewBarns1.fa = jarray('int', [Code06_NewBarns1.MAXN])
Code06_NewBarns1.ls = jarray('int', [Code06_NewBarns1.MAXN])
Code06_NewBarns1.rs = jarray('int', [Code06_NewBarns1.MAXN])
Code06_NewBarns1.rev = jarray('boolean', [Code06_NewBarns1.MAXN])
Code06_NewBarns1.sta = jarray('int', [Code06_NewBarns1.MAXN])
Code06_NewBarns1.siz = jarray('int', [Code06_NewBarns1.MAXN])
Code06_NewBarns1.father = jarray('int', [Code06_NewBarns1.MAXN])
Code06_NewBarns1.diameter = jarray('int', [Code06_NewBarns1.MAXN])
Code06_NewBarns1.dl = jarray('int', [Code06_NewBarns1.MAXN])
Code06_NewBarns1.dr = jarray('int', [Code06_NewBarns1.MAXN])

if __name__ == '__main__':
    Code06_NewBarns1.main([])
