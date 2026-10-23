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

# 动态树LCA，Python版
# 一共n个点，初始时每个点各自是一棵单点有根树，一共m条操作，操作类型如下
# 操作 link x y : 让点x成为点y的儿子，保证x是所在树的根，并且x和y不连通
# 操作 cut x    : 删除点x和它父亲节点之间的直接边，保证x不是根
# 操作 lca x y  : 查询点x和点y的最低公共祖先，保证x和y在同一棵树中
# 1 <= n、m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/SP8791
# 测试链接 : https://www.spoj.com/problems/DYNALCA/
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_DynamicLCA1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs'}
    MAXN = 0
    n = 0
    m = 0
    fa = None
    ls = None
    rs = None
    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code02_DynamicLCA1.ls[Code02_DynamicLCA1.fa[x]] != x) and (Code02_DynamicLCA1.rs[Code02_DynamicLCA1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code02_DynamicLCA1.ls[Code02_DynamicLCA1.fa[x]] == x) else 1))

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code02_DynamicLCA1.fa[x])
        g = jcast('int', Code02_DynamicLCA1.fa[f])
        if (Code02_DynamicLCA1.lr(x) == 0):
            Code02_DynamicLCA1.ls[f] = jcast('int', Code02_DynamicLCA1.rs[x])
            if (Code02_DynamicLCA1.ls[f] != 0):
                jset(Code02_DynamicLCA1.fa, Code02_DynamicLCA1.ls[f], f)
            Code02_DynamicLCA1.rs[x] = jcast('int', f)
        else:
            Code02_DynamicLCA1.rs[f] = jcast('int', Code02_DynamicLCA1.ls[x])
            if (Code02_DynamicLCA1.rs[f] != 0):
                jset(Code02_DynamicLCA1.fa, Code02_DynamicLCA1.rs[f], f)
            Code02_DynamicLCA1.ls[x] = jcast('int', f)
        if (not Code02_DynamicLCA1.isroot(f)):
            if (Code02_DynamicLCA1.lr(f) == 0):
                Code02_DynamicLCA1.ls[g] = jcast('int', x)
            else:
                Code02_DynamicLCA1.rs[g] = jcast('int', x)
        Code02_DynamicLCA1.fa[f] = jcast('int', x)
        Code02_DynamicLCA1.fa[x] = jcast('int', g)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        while (not Code02_DynamicLCA1.isroot(x)):
            f = jcast('int', Code02_DynamicLCA1.fa[x])
            if (not Code02_DynamicLCA1.isroot(f)):
                if (Code02_DynamicLCA1.lr(x) == Code02_DynamicLCA1.lr(f)):
                    Code02_DynamicLCA1.rotate(f)
                else:
                    Code02_DynamicLCA1.rotate(x)
            Code02_DynamicLCA1.rotate(x)

    # 返回最后一次接上的点
    @staticmethod
    def access(x):
        x = jcast('int', x)
        ans = jcast('int', 0)
        y = jcast('int', 0)
        while (x != 0):
            Code02_DynamicLCA1.splay(x)
            Code02_DynamicLCA1.rs[x] = jcast('int', y)
            ans = jcast('int', x)
            y = jcast('int', x)
            x = jcast('int', Code02_DynamicLCA1.fa[x])
        return jcast('int', ans)

    # 让x成为y的孩子，保证x是所在树的根，并且x和y不连通
    @staticmethod
    def makeson(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code02_DynamicLCA1.access(x)
        Code02_DynamicLCA1.splay(x)
        Code02_DynamicLCA1.fa[x] = jcast('int', y)

    # 切断x和原树父亲之间的边，保证x不是根
    @staticmethod
    def cutfa(x):
        x = jcast('int', x)
        Code02_DynamicLCA1.access(x)
        Code02_DynamicLCA1.splay(x)
        jset(Code02_DynamicLCA1.fa, Code02_DynamicLCA1.ls[x], 0)
        Code02_DynamicLCA1.ls[x] = jcast('int', 0)

    # 第二次的返回值就是lca
    @staticmethod
    def lca(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        if (x == y):
            return jcast('int', x)
        Code02_DynamicLCA1.access(x)
        return jcast('int', Code02_DynamicLCA1.access(y))

    @staticmethod
    def main(args):
        in_ = Code02_DynamicLCA1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_DynamicLCA1.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_DynamicLCA1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= Code02_DynamicLCA1.m):
            op = jcall(in_, 'nextString')
            if jcall(op, 'equals', 'link'):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                Code02_DynamicLCA1.makeson(x, y)
            else:
                if jcall(op, 'equals', 'cut'):
                    x = jcast('int', jcall(in_, 'nextInt'))
                    Code02_DynamicLCA1.cutfa(x)
                else:
                    x = jcast('int', jcall(in_, 'nextInt'))
                    y = jcast('int', jcall(in_, 'nextInt'))
                    jcall(out, 'println', Code02_DynamicLCA1.lca(x, y))
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
            return jcast('int', self.buffer[((_java_obj_1 := self), (_java_key_2 := 'ptr'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]])

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
            raise TypeError("No matching overload for Code02_DynamicLCA1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_DynamicLCA1.MAXN = jcast('int', 100001)
Code02_DynamicLCA1.n = jcast('int', 0)
Code02_DynamicLCA1.m = jcast('int', 0)
Code02_DynamicLCA1.fa = jarray('int', [Code02_DynamicLCA1.MAXN])
Code02_DynamicLCA1.ls = jarray('int', [Code02_DynamicLCA1.MAXN])
Code02_DynamicLCA1.rs = jarray('int', [Code02_DynamicLCA1.MAXN])

if __name__ == '__main__':
    Code02_DynamicLCA1.main([])
