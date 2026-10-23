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

# 大融合，Python版
# 本题就是讲解166，题目5，讲了线段树分治的解法，这里用lct的解法
# 一共有n个点，一共有q条操作，每条操作是如下两种类型中的一种
# 操作 A x y : 点x和点y之间连一条边，保证之前x和y是不联通的
# 操作 Q x y : 打印点x和点y之间这条边的负载，保证x和y之间有一条边
# 边负载定义为，这条边两侧端点各自连通区大小的乘积
# 1 <= n、q <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4219
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_GreatIntegration2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'q': 'q', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'rev': 'rev', 'sta': 'sta', 'vir': 'vir', 'sum': 'sum'}
    MAXN = 0
    n = 0
    q = 0
    fa = None
    ls = None
    rs = None
    rev = None
    sta = None
    # vir[x]表示x所有虚子树的大小总和
    vir = None
    # sum[x]表示以x为根的辅助splay中，汇总所有节点的数量
    # 包括x自己、x的所有虚子树大小、左右儿子的贡献
    sum = None
    # 汇总贡献
    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code01_GreatIntegration2.sum[x] = jcast('int', jcast('int', jadd(jcast('int', jadd(jcast('int', jadd(Code01_GreatIntegration2.sum[Code01_GreatIntegration2.ls[x]], Code01_GreatIntegration2.sum[Code01_GreatIntegration2.rs[x]])), Code01_GreatIntegration2.vir[x])), 1)))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code01_GreatIntegration2.ls[Code01_GreatIntegration2.fa[x]] != x) and (Code01_GreatIntegration2.rs[Code01_GreatIntegration2.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code01_GreatIntegration2.ls[Code01_GreatIntegration2.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code01_GreatIntegration2.ls[x])
            Code01_GreatIntegration2.ls[x] = jcast('int', Code01_GreatIntegration2.rs[x])
            Code01_GreatIntegration2.rs[x] = jcast('int', tmp)
            Code01_GreatIntegration2.rev[x] = jcast('boolean', (not Code01_GreatIntegration2.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code01_GreatIntegration2.rev[x]:
            Code01_GreatIntegration2.reverse(Code01_GreatIntegration2.ls[x])
            Code01_GreatIntegration2.reverse(Code01_GreatIntegration2.rs[x])
            Code01_GreatIntegration2.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code01_GreatIntegration2.fa[x])
        g = jcast('int', Code01_GreatIntegration2.fa[f])
        if (Code01_GreatIntegration2.lr(x) == 0):
            Code01_GreatIntegration2.ls[f] = jcast('int', Code01_GreatIntegration2.rs[x])
            if (Code01_GreatIntegration2.ls[f] != 0):
                jset(Code01_GreatIntegration2.fa, Code01_GreatIntegration2.ls[f], f)
            Code01_GreatIntegration2.rs[x] = jcast('int', f)
        else:
            Code01_GreatIntegration2.rs[f] = jcast('int', Code01_GreatIntegration2.ls[x])
            if (Code01_GreatIntegration2.rs[f] != 0):
                jset(Code01_GreatIntegration2.fa, Code01_GreatIntegration2.rs[f], f)
            Code01_GreatIntegration2.ls[x] = jcast('int', f)
        if (not Code01_GreatIntegration2.isroot(f)):
            if (Code01_GreatIntegration2.lr(f) == 0):
                Code01_GreatIntegration2.ls[g] = jcast('int', x)
            else:
                Code01_GreatIntegration2.rs[g] = jcast('int', x)
        Code01_GreatIntegration2.fa[f] = jcast('int', x)
        Code01_GreatIntegration2.fa[x] = jcast('int', g)
        Code01_GreatIntegration2.up(f)
        Code01_GreatIntegration2.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code01_GreatIntegration2.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code01_GreatIntegration2.isroot(y)):
            jset(Code01_GreatIntegration2.sta, (siz := jcast('int', (siz + (1)))), Code01_GreatIntegration2.fa[y])
            y = jcast('int', Code01_GreatIntegration2.fa[y])
        while (siz != 0):
            Code01_GreatIntegration2.down(Code01_GreatIntegration2.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code01_GreatIntegration2.isroot(x)):
            f = jcast('int', Code01_GreatIntegration2.fa[x])
            if (not Code01_GreatIntegration2.isroot(f)):
                if (Code01_GreatIntegration2.lr(x) == Code01_GreatIntegration2.lr(f)):
                    Code01_GreatIntegration2.rotate(f)
                else:
                    Code01_GreatIntegration2.rotate(x)
            Code01_GreatIntegration2.rotate(x)

    # 原右儿子由实儿子变成虚儿子，加入贡献
    # 新右儿子由虚儿子变成实儿子，删除贡献
    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code01_GreatIntegration2.splay(x)
            Code01_GreatIntegration2.vir[x] = jcast('int', jcast('int', jadd(Code01_GreatIntegration2.vir[x], Code01_GreatIntegration2.sum[Code01_GreatIntegration2.rs[x]])))
            Code01_GreatIntegration2.vir[x] = jcast('int', jcast('int', (Code01_GreatIntegration2.vir[x] - Code01_GreatIntegration2.sum[y])))
            Code01_GreatIntegration2.rs[x] = jcast('int', y)
            Code01_GreatIntegration2.up(x)
            y = jcast('int', x)
            x = jcast('int', Code01_GreatIntegration2.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code01_GreatIntegration2.access(x)
        Code01_GreatIntegration2.splay(x)
        Code01_GreatIntegration2.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code01_GreatIntegration2.access(x)
        Code01_GreatIntegration2.splay(x)
        Code01_GreatIntegration2.down(x)
        while (Code01_GreatIntegration2.ls[x] != 0):
            x = jcast('int', Code01_GreatIntegration2.ls[x])
            Code01_GreatIntegration2.down(x)
        Code01_GreatIntegration2.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code01_GreatIntegration2.makeroot(x)
        Code01_GreatIntegration2.access(y)
        Code01_GreatIntegration2.splay(y)

    # 连接x和y，x和y成为各自树的头，然后x作为y的虚儿子
    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code01_GreatIntegration2.makeroot(x)
        if (Code01_GreatIntegration2.findroot(y) != x):
            Code01_GreatIntegration2.access(y)
            Code01_GreatIntegration2.splay(y)
            Code01_GreatIntegration2.fa[x] = jcast('int', y)
            Code01_GreatIntegration2.vir[y] = jcast('int', jcast('int', jadd(Code01_GreatIntegration2.vir[y], Code01_GreatIntegration2.sum[x])))
            Code01_GreatIntegration2.up(y)

    # cut方法和lct模版代码完全一样，但是注意
    # 判断x和y之间是否存在直接边，如果判定成立
    # 此时x和y之间的边已经是实边，所以删除该边不需要修改vir
    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code01_GreatIntegration2.makeroot(x)
        if ((((Code01_GreatIntegration2.findroot(y) == x) and (Code01_GreatIntegration2.fa[y] == x)) and (Code01_GreatIntegration2.ls[y] == 0)) and (Code01_GreatIntegration2.rs[x] == y)):
            jset(Code01_GreatIntegration2.fa, y, jset(Code01_GreatIntegration2.rs, x, 0))
            Code01_GreatIntegration2.up(x)

    # 临时删除询问边
    # 将两个端点分别作为各自原树的根，得到各自连通块的大小
    # 然后恢复询问边
    @staticmethod
    def query(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code01_GreatIntegration2.cut(x, y)
        Code01_GreatIntegration2.makeroot(x)
        sizx = jcast('int', Code01_GreatIntegration2.sum[x])
        Code01_GreatIntegration2.makeroot(y)
        sizy = jcast('int', Code01_GreatIntegration2.sum[y])
        Code01_GreatIntegration2.link(x, y)
        return jcast('long', jcast('long', (jcast('long', (1 * sizx)) * sizy)))

    @staticmethod
    def main(args):
        in_ = Code01_GreatIntegration2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_GreatIntegration2.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_GreatIntegration2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_GreatIntegration2.n):
            Code01_GreatIntegration2.sum[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_GreatIntegration2.q):
            op = jcast('char', jcall(in_, 'nextChar'))
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            if (op == jchar('A')):
                Code01_GreatIntegration2.link(x, y)
            else:
                jcall(out, 'println', Code01_GreatIntegration2.query(x, y))
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

        def nextChar(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            return jcast('char', jcast('char', c))

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
                val = jcast('int', jcast('int', (jcast('int', jadd(jcast('int', (val * 10)), c)) - jchar('0'))))
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
            raise TypeError("No matching overload for Code01_GreatIntegration2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_GreatIntegration2.MAXN = jcast('int', 100001)
Code01_GreatIntegration2.n = jcast('int', 0)
Code01_GreatIntegration2.q = jcast('int', 0)
Code01_GreatIntegration2.fa = jarray('int', [Code01_GreatIntegration2.MAXN])
Code01_GreatIntegration2.ls = jarray('int', [Code01_GreatIntegration2.MAXN])
Code01_GreatIntegration2.rs = jarray('int', [Code01_GreatIntegration2.MAXN])
Code01_GreatIntegration2.rev = jarray('boolean', [Code01_GreatIntegration2.MAXN])
Code01_GreatIntegration2.sta = jarray('int', [Code01_GreatIntegration2.MAXN])
Code01_GreatIntegration2.vir = jarray('int', [Code01_GreatIntegration2.MAXN])
Code01_GreatIntegration2.sum = jarray('int', [Code01_GreatIntegration2.MAXN])

if __name__ == '__main__':
    Code01_GreatIntegration2.main([])
