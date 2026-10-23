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

# 星球联盟，Python版
# 一共有n个点、m条无向边，接下来依次加入p条无向边
# 如果两个点属于同一个联盟，必须存在一条环形线路经过这两个点
# 等价地说，两个点之间存在两条没有公共边的路径，也就是在同一个边双连通分量中
# 每次加入一条新边(x,y)，加入之后判断点x和点y是否属于同一个联盟
# 如果不属于同一个联盟，打印"No"
# 如果属于同一个联盟，打印这个联盟里的节点数
# 1 <= n、m、p <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P10657
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Alliance1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'p': 'p', 'father': 'father', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'rev': 'rev', 'sta': 'sta', 'nodeCnt': 'nodeCnt'}
    MAXN = 0
    n = 0
    m = 0
    p = 0
    father = None
    fa = None
    ls = None
    rs = None
    rev = None
    sta = None
    # nodeCnt[x]表示x代表的边双连通分量中，有多少个原图节点
    nodeCnt = None
    @staticmethod
    def find(x):
        x = jcast('int', x)
        if (x != Code05_Alliance1.father[x]):
            jset(Code05_Alliance1.father, x, Code05_Alliance1.find(Code05_Alliance1.father[x]))
        return jcast('int', Code05_Alliance1.father[x])

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code05_Alliance1.ls[Code05_Alliance1.fa[x]] != x) and (Code05_Alliance1.rs[Code05_Alliance1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code05_Alliance1.ls[Code05_Alliance1.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code05_Alliance1.ls[x])
            Code05_Alliance1.ls[x] = jcast('int', Code05_Alliance1.rs[x])
            Code05_Alliance1.rs[x] = jcast('int', tmp)
            Code05_Alliance1.rev[x] = jcast('boolean', (not Code05_Alliance1.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code05_Alliance1.rev[x]:
            Code05_Alliance1.reverse(Code05_Alliance1.ls[x])
            Code05_Alliance1.reverse(Code05_Alliance1.rs[x])
            Code05_Alliance1.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code05_Alliance1.fa[x])
        g = jcast('int', Code05_Alliance1.fa[f])
        if (Code05_Alliance1.lr(x) == 0):
            Code05_Alliance1.ls[f] = jcast('int', Code05_Alliance1.rs[x])
            if (Code05_Alliance1.ls[f] != 0):
                jset(Code05_Alliance1.fa, Code05_Alliance1.ls[f], f)
            Code05_Alliance1.rs[x] = jcast('int', f)
        else:
            Code05_Alliance1.rs[f] = jcast('int', Code05_Alliance1.ls[x])
            if (Code05_Alliance1.rs[f] != 0):
                jset(Code05_Alliance1.fa, Code05_Alliance1.rs[f], f)
            Code05_Alliance1.ls[x] = jcast('int', f)
        if (not Code05_Alliance1.isroot(f)):
            if (Code05_Alliance1.lr(f) == 0):
                Code05_Alliance1.ls[g] = jcast('int', x)
            else:
                Code05_Alliance1.rs[g] = jcast('int', x)
        Code05_Alliance1.fa[f] = jcast('int', x)
        Code05_Alliance1.fa[x] = jcast('int', g)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code05_Alliance1.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code05_Alliance1.isroot(y)):
            jset(Code05_Alliance1.sta, (siz := jcast('int', (siz + (1)))), Code05_Alliance1.fa[y])
            y = jcast('int', Code05_Alliance1.fa[y])
        while (siz != 0):
            Code05_Alliance1.down(Code05_Alliance1.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code05_Alliance1.isroot(x)):
            f = jcast('int', Code05_Alliance1.fa[x])
            if (not Code05_Alliance1.isroot(f)):
                if (Code05_Alliance1.lr(x) == Code05_Alliance1.lr(f)):
                    Code05_Alliance1.rotate(f)
                else:
                    Code05_Alliance1.rotate(x)
            Code05_Alliance1.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        x = jcast('int', Code05_Alliance1.find(x))
        y = jcast('int', 0)
        while (x != 0):
            Code05_Alliance1.splay(x)
            Code05_Alliance1.rs[x] = jcast('int', y)
            jset(Code05_Alliance1.fa, x, Code05_Alliance1.find(Code05_Alliance1.fa[x]))
            y = jcast('int', x)
            x = jcast('int', Code05_Alliance1.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code05_Alliance1.access(x)
        Code05_Alliance1.splay(x)
        Code05_Alliance1.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code05_Alliance1.access(x)
        Code05_Alliance1.splay(x)
        Code05_Alliance1.down(x)
        while (Code05_Alliance1.ls[x] != 0):
            x = jcast('int', Code05_Alliance1.ls[x])
            Code05_Alliance1.down(x)
        Code05_Alliance1.splay(x)
        return jcast('int', x)

    @staticmethod
    def condense(x, root):
        x = jcast('int', x)
        root = jcast('int', root)
        if (x != 0):
            Code05_Alliance1.father[x] = jcast('int', root)
            Code05_Alliance1.nodeCnt[root] = jcast('int', jcast('int', jadd(Code05_Alliance1.nodeCnt[root], Code05_Alliance1.nodeCnt[x])))
            Code05_Alliance1.condense(Code05_Alliance1.ls[x], root)
            Code05_Alliance1.condense(Code05_Alliance1.rs[x], root)

    # 如果两点不连通就连接，如果连通，说明形成环，缩成一个边双
    # 如果不连通就返回-1，否则返回边双的节点数量
    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        x = jcast('int', Code05_Alliance1.find(x))
        y = jcast('int', Code05_Alliance1.find(y))
        if (x == y):
            return jcast('int', Code05_Alliance1.nodeCnt[x])
        Code05_Alliance1.makeroot(x)
        if (Code05_Alliance1.findroot(y) != x):
            Code05_Alliance1.fa[x] = jcast('int', y)
            return jcast('int', jcast('int', (-1)))
        else:
            Code05_Alliance1.condense(Code05_Alliance1.rs[x], x)
            Code05_Alliance1.rs[x] = jcast('int', 0)
            return jcast('int', Code05_Alliance1.nodeCnt[x])

    @staticmethod
    def main(args):
        in_ = Code05_Alliance1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_Alliance1.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_Alliance1.m = jcast('int', jcall(in_, 'nextInt'))
        Code05_Alliance1.p = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_Alliance1.n):
            Code05_Alliance1.father[i] = jcast('int', i)
            Code05_Alliance1.nodeCnt[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= Code05_Alliance1.m):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            Code05_Alliance1.link(x, y)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= Code05_Alliance1.p):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            ans = jcast('int', Code05_Alliance1.link(x, y))
            if (ans == jcast('int', (-1))):
                jcall(out, 'println', 'No')
            else:
                jcall(out, 'println', ans)
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
            raise TypeError("No matching overload for Code05_Alliance1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Alliance1.MAXN = jcast('int', 200001)
Code05_Alliance1.n = jcast('int', 0)
Code05_Alliance1.m = jcast('int', 0)
Code05_Alliance1.p = jcast('int', 0)
Code05_Alliance1.father = jarray('int', [Code05_Alliance1.MAXN])
Code05_Alliance1.fa = jarray('int', [Code05_Alliance1.MAXN])
Code05_Alliance1.ls = jarray('int', [Code05_Alliance1.MAXN])
Code05_Alliance1.rs = jarray('int', [Code05_Alliance1.MAXN])
Code05_Alliance1.rev = jarray('boolean', [Code05_Alliance1.MAXN])
Code05_Alliance1.sta = jarray('int', [Code05_Alliance1.MAXN])
Code05_Alliance1.nodeCnt = jarray('int', [Code05_Alliance1.MAXN])

if __name__ == '__main__':
    Code05_Alliance1.main([])
