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

# QTREE6，Python版
# 给定一棵n个节点的树，每个节点有黑白两种颜色，初始所有节点都是黑色
# 接下来有q条操作，操作类型如下
# 操作 0 x : 打印节点x所在的同色连通块大小
# 操作 1 x : 翻转节点x的颜色
# 1 <= n、q <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/SP16549
# 测试链接 : https://www.spoj.com/problems/QTREE6/
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_QTREE6_1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'q': 'q', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'parent': 'parent', 'val': 'val', 'vir': 'vir', 'sum': 'sum'}
    MAXN = 0
    n = 0
    q = 0
    # 原树
    head = None
    nxt = None
    to = None
    cntg = 0
    # 节点x有黑白两个状态，x是黑状态，x+n是白状态
    # 两套颜色的森林共用一套LCT，彼此独立
    fa = None
    ls = None
    rs = None
    # 原树固定以1为根，每个状态节点都有同一颜色系统中的固定父亲
    # parent[x]表示黑色状态节点x的固定父亲
    # parent[x+n]表示白色状态节点x+n的固定父亲
    parent = None
    # 节点x有黑白两个状态，分别是x和x+n，有效状态只有一个
    val = None
    # vir[x]表示状态节点x的虚子树的点权累加和
    vir = None
    # sum[x]表示以x为根的辅助splay中，汇总所有点权累加和
    # 包括x自己的贡献、x的所有虚子树的贡献、左右儿子的贡献
    sum = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_QTREE6_1.nxt, ((_java_obj_1 := Code02_QTREE6_1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_QTREE6_1.head[u])
        Code02_QTREE6_1.to[Code02_QTREE6_1.cntg] = jcast('int', v)
        Code02_QTREE6_1.head[u] = jcast('int', Code02_QTREE6_1.cntg)

    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code02_QTREE6_1.sum[x] = jcast('int', jcast('int', jadd(jcast('int', jadd(jcast('int', jadd(Code02_QTREE6_1.sum[Code02_QTREE6_1.ls[x]], Code02_QTREE6_1.sum[Code02_QTREE6_1.rs[x]])), Code02_QTREE6_1.vir[x])), Code02_QTREE6_1.val[x])))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code02_QTREE6_1.ls[Code02_QTREE6_1.fa[x]] != x) and (Code02_QTREE6_1.rs[Code02_QTREE6_1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code02_QTREE6_1.ls[Code02_QTREE6_1.fa[x]] == x) else 1))

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code02_QTREE6_1.fa[x])
        g = jcast('int', Code02_QTREE6_1.fa[f])
        if (Code02_QTREE6_1.lr(x) == 0):
            Code02_QTREE6_1.ls[f] = jcast('int', Code02_QTREE6_1.rs[x])
            if (Code02_QTREE6_1.ls[f] != 0):
                jset(Code02_QTREE6_1.fa, Code02_QTREE6_1.ls[f], f)
            Code02_QTREE6_1.rs[x] = jcast('int', f)
        else:
            Code02_QTREE6_1.rs[f] = jcast('int', Code02_QTREE6_1.ls[x])
            if (Code02_QTREE6_1.rs[f] != 0):
                jset(Code02_QTREE6_1.fa, Code02_QTREE6_1.rs[f], f)
            Code02_QTREE6_1.ls[x] = jcast('int', f)
        if (not Code02_QTREE6_1.isroot(f)):
            if (Code02_QTREE6_1.lr(f) == 0):
                Code02_QTREE6_1.ls[g] = jcast('int', x)
            else:
                Code02_QTREE6_1.rs[g] = jcast('int', x)
        Code02_QTREE6_1.fa[f] = jcast('int', x)
        Code02_QTREE6_1.fa[x] = jcast('int', g)
        Code02_QTREE6_1.up(f)
        Code02_QTREE6_1.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        while (not Code02_QTREE6_1.isroot(x)):
            f = jcast('int', Code02_QTREE6_1.fa[x])
            if (not Code02_QTREE6_1.isroot(f)):
                if (Code02_QTREE6_1.lr(x) == Code02_QTREE6_1.lr(f)):
                    Code02_QTREE6_1.rotate(f)
                else:
                    Code02_QTREE6_1.rotate(x)
            Code02_QTREE6_1.rotate(x)
        Code02_QTREE6_1.up(x)

    # 注意修正虚子树贡献
    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code02_QTREE6_1.splay(x)
            Code02_QTREE6_1.vir[x] = jcast('int', jcast('int', jadd(Code02_QTREE6_1.vir[x], Code02_QTREE6_1.sum[Code02_QTREE6_1.rs[x]])))
            Code02_QTREE6_1.vir[x] = jcast('int', jcast('int', (Code02_QTREE6_1.vir[x] - Code02_QTREE6_1.sum[y])))
            Code02_QTREE6_1.rs[x] = jcast('int', y)
            Code02_QTREE6_1.up(x)
            y = jcast('int', x)
            x = jcast('int', Code02_QTREE6_1.fa[x])

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code02_QTREE6_1.access(x)
        Code02_QTREE6_1.splay(x)
        while (Code02_QTREE6_1.ls[x] != 0):
            x = jcast('int', Code02_QTREE6_1.ls[x])
        Code02_QTREE6_1.splay(x)
        return jcast('int', x)

    # 原树形态固定，连接父边(x, f)，x是子，f是父
    # 连接后x作为f的虚儿子
    @staticmethod
    def link(x, f):
        x = jcast('int', x)
        f = jcast('int', f)
        if (f == 0):
            return
        Code02_QTREE6_1.access(f)
        Code02_QTREE6_1.splay(f)
        Code02_QTREE6_1.splay(x)
        Code02_QTREE6_1.fa[x] = jcast('int', f)
        Code02_QTREE6_1.vir[f] = jcast('int', jcast('int', jadd(Code02_QTREE6_1.vir[f], Code02_QTREE6_1.sum[x])))
        Code02_QTREE6_1.up(f)

    # 原树形态固定，删除父边(x, f)，x是子，f是父
    @staticmethod
    def cut(x, f):
        x = jcast('int', x)
        f = jcast('int', f)
        Code02_QTREE6_1.access(x)
        Code02_QTREE6_1.splay(x)
        if (f != 0):
            left = jcast('int', Code02_QTREE6_1.ls[x])
            Code02_QTREE6_1.fa[left] = jcast('int', 0)
            Code02_QTREE6_1.ls[x] = jcast('int', 0)
            Code02_QTREE6_1.up(x)

    @staticmethod
    def query(x):
        x = jcast('int', x)
        # 得到x的状态xs，顶部节点的状态ys
        xs = jcast('int', (x if (Code02_QTREE6_1.val[x] == 1) else jcast('int', jadd(x, Code02_QTREE6_1.n))))
        ys = jcast('int', Code02_QTREE6_1.findroot(xs))
        # 如果顶部节点和x同色，返回整体sum，如果不同色，返回右儿子sum
        return jcast('int', (Code02_QTREE6_1.sum[ys] if (Code02_QTREE6_1.val[ys] == 1) else Code02_QTREE6_1.sum[Code02_QTREE6_1.rs[ys]]))

    @staticmethod
    def reverseColor(x):
        x = jcast('int', x)
        pre = jcast('int', (x if (Code02_QTREE6_1.val[x] == 1) else jcast('int', jadd(x, Code02_QTREE6_1.n))))
        cur = jcast('int', (jcast('int', jadd(pre, Code02_QTREE6_1.n)) if (pre <= Code02_QTREE6_1.n) else jcast('int', (pre - Code02_QTREE6_1.n))))
        # 老颜色的lct中要断边，新颜色的lct中要连边
        Code02_QTREE6_1.cut(pre, Code02_QTREE6_1.parent[pre])
        Code02_QTREE6_1.val[pre] = jcast('int', 0)
        Code02_QTREE6_1.val[cur] = jcast('int', 1)
        Code02_QTREE6_1.link(cur, Code02_QTREE6_1.parent[cur])

    @staticmethod
    def dfs(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        # 黑白的状态节点，各自记录父亲
        if (f != 0):
            Code02_QTREE6_1.parent[u] = jcast('int', f)
            Code02_QTREE6_1.parent[jcast('int', jadd(u, Code02_QTREE6_1.n))] = jcast('int', jcast('int', jadd(f, Code02_QTREE6_1.n)))
        # 节点初始都是黑色，黑色状态点才有贡献
        jset(Code02_QTREE6_1.val, u, jset(Code02_QTREE6_1.sum, u, 1))
        e = jcast('int', Code02_QTREE6_1.head[u])
        while (e != 0):
            v = jcast('int', Code02_QTREE6_1.to[e])
            if (v != f):
                Code02_QTREE6_1.dfs(v, u)
                Code02_QTREE6_1.link(v, u)
            e = jcast('int', Code02_QTREE6_1.nxt[e])

    @staticmethod
    def main(args):
        in_ = Code02_QTREE6_1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_QTREE6_1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code02_QTREE6_1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code02_QTREE6_1.addEdge(u, v)
            Code02_QTREE6_1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code02_QTREE6_1.dfs(1, 0)
        Code02_QTREE6_1.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        op = 0
        x = 0
        while (i <= Code02_QTREE6_1.q):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            if (op == 0):
                jcall(out, 'println', Code02_QTREE6_1.query(x))
            else:
                Code02_QTREE6_1.reverseColor(x)
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
            return jcast('int', self.buffer[((_java_obj_4 := self), (_java_key_5 := 'ptr'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]])

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
            raise TypeError("No matching overload for Code02_QTREE6_1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_QTREE6_1.MAXN = jcast('int', 200001)
Code02_QTREE6_1.n = jcast('int', 0)
Code02_QTREE6_1.q = jcast('int', 0)
Code02_QTREE6_1.head = jarray('int', [Code02_QTREE6_1.MAXN])
Code02_QTREE6_1.nxt = jarray('int', [Code02_QTREE6_1.MAXN])
Code02_QTREE6_1.to = jarray('int', [Code02_QTREE6_1.MAXN])
Code02_QTREE6_1.cntg = jcast('int', 0)
Code02_QTREE6_1.fa = jarray('int', [Code02_QTREE6_1.MAXN])
Code02_QTREE6_1.ls = jarray('int', [Code02_QTREE6_1.MAXN])
Code02_QTREE6_1.rs = jarray('int', [Code02_QTREE6_1.MAXN])
Code02_QTREE6_1.parent = jarray('int', [Code02_QTREE6_1.MAXN])
Code02_QTREE6_1.val = jarray('int', [Code02_QTREE6_1.MAXN])
Code02_QTREE6_1.vir = jarray('int', [Code02_QTREE6_1.MAXN])
Code02_QTREE6_1.sum = jarray('int', [Code02_QTREE6_1.MAXN])

if __name__ == '__main__':
    Code02_QTREE6_1.main([])
