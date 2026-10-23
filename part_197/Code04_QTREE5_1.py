# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# QTREE5，Python版
# 给定一棵n个节点的树，每个节点有黑白两种颜色，初始所有节点都是黑色
# 接下来有q条操作，操作类型如下
# 操作 0 x : 翻转节点x的颜色
# 操作 1 x : 打印节点x到最近白色节点的距离，不存在白色节点打印-1
# 1 <= n、q <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/SP2939
# 测试链接 : https://www.spoj.com/problems/QTREE5/
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 对应实现可参考 Code04_QTREE5_2.py
# 两个版本保留相同的算法逻辑
class Code04_QTREE5_1:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'q': 'q', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'color': 'color', 'siz': 'siz', 'lm': 'lm', 'rm': 'rm', 'vir': 'vir'}
    MAXN = 0
    INF = 0
    n = 0
    q = 0
    head = None
    nxt = None
    to = None
    cntg = 0
    fa = None
    ls = None
    rs = None
    # 节点颜色
    color = None
    # siz[x]表示以x为根的辅助splay节点数量，也就是实链节点数，不包括虚子树节点
    siz = None
    # lm[x]表示以x为根的辅助splay中，从深度最小的节点出发，也就是实链顶点，到最近白色节点的距离
    lm = None
    # rm[x]表示以x为根的辅助splay中，从深度最大的节点出发，也就是实链底点，到最近白色节点的距离
    rm = None
    # 节点x的有序表，记录每个虚儿子，各自去往下方，最近白点的距离和次数
    # 表中最小值+1，就是从x进入虚子树后，到最近白点的距离
    vir = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_QTREE5_1.nxt, ((_java_obj_1 := Code04_QTREE5_1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_QTREE5_1.head[u])
        Code04_QTREE5_1.to[Code04_QTREE5_1.cntg] = jcast('int', v)
        Code04_QTREE5_1.head[u] = jcast('int', Code04_QTREE5_1.cntg)

    @staticmethod
    def insert(x, v):
        x = jcast('int', x)
        v = jcast('int', v)
        if (not jcall(Code04_QTREE5_1.vir, 'containsKey', x)):
            jcall(Code04_QTREE5_1.vir, 'put', x, jnew('TreeMap'))
        jcall(jcall(Code04_QTREE5_1.vir, 'get', x), 'put', v, jadd(jcall(jcall(Code04_QTREE5_1.vir, 'get', x), 'getOrDefault', v, 0), 1))

    @staticmethod
    def remove(x, v):
        x = jcast('int', x)
        v = jcast('int', v)
        cnt = jcast('int', jcall(jcall(Code04_QTREE5_1.vir, 'get', x), 'get', v))
        if (cnt == 1):
            jcall(jcall(Code04_QTREE5_1.vir, 'get', x), 'remove', v)
        else:
            jcall(jcall(Code04_QTREE5_1.vir, 'get', x), 'put', v, jcast('int', (cnt - 1)))

    @staticmethod
    def getmin(x):
        x = jcast('int', x)
        if ((not jcall(Code04_QTREE5_1.vir, 'containsKey', x)) or jcall(jcall(Code04_QTREE5_1.vir, 'get', x), 'isEmpty')):
            return jcast('int', Code04_QTREE5_1.INF)
        return jcast('int', jcall(jcall(Code04_QTREE5_1.vir, 'get', x), 'firstKey'))

    # 课上重点图解了决策过程
    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code04_QTREE5_1.siz[x] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code04_QTREE5_1.siz[Code04_QTREE5_1.ls[x]], Code04_QTREE5_1.siz[Code04_QTREE5_1.rs[x]])), 1)))
        l1 = jcast('int', Code04_QTREE5_1.lm[Code04_QTREE5_1.ls[x]])
        l2 = jcast('int', jcast('int', jadd(Code04_QTREE5_1.siz[Code04_QTREE5_1.ls[x]], (0 if (Code04_QTREE5_1.color[x] == 1) else jcast('int', jadd(Code04_QTREE5_1.getmin(x), 1))))))
        l3 = jcast('int', jcast('int', jadd(jcast('int', jadd(Code04_QTREE5_1.siz[Code04_QTREE5_1.ls[x]], 1)), Code04_QTREE5_1.lm[Code04_QTREE5_1.rs[x]])))
        jset(Code04_QTREE5_1.lm, x, jstatic('Math', 'min', l1, jstatic('Math', 'min', l2, l3)))
        r1 = jcast('int', Code04_QTREE5_1.rm[Code04_QTREE5_1.rs[x]])
        r2 = jcast('int', jcast('int', jadd(Code04_QTREE5_1.siz[Code04_QTREE5_1.rs[x]], (0 if (Code04_QTREE5_1.color[x] == 1) else jcast('int', jadd(Code04_QTREE5_1.getmin(x), 1))))))
        r3 = jcast('int', jcast('int', jadd(jcast('int', jadd(Code04_QTREE5_1.siz[Code04_QTREE5_1.rs[x]], 1)), Code04_QTREE5_1.rm[Code04_QTREE5_1.ls[x]])))
        jset(Code04_QTREE5_1.rm, x, jstatic('Math', 'min', r1, jstatic('Math', 'min', r2, r3)))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code04_QTREE5_1.ls[Code04_QTREE5_1.fa[x]] != x) and (Code04_QTREE5_1.rs[Code04_QTREE5_1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code04_QTREE5_1.ls[Code04_QTREE5_1.fa[x]] == x) else 1))

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code04_QTREE5_1.fa[x])
        g = jcast('int', Code04_QTREE5_1.fa[f])
        if (Code04_QTREE5_1.lr(x) == 0):
            Code04_QTREE5_1.ls[f] = jcast('int', Code04_QTREE5_1.rs[x])
            if (Code04_QTREE5_1.ls[f] != 0):
                jset(Code04_QTREE5_1.fa, Code04_QTREE5_1.ls[f], f)
            Code04_QTREE5_1.rs[x] = jcast('int', f)
        else:
            Code04_QTREE5_1.rs[f] = jcast('int', Code04_QTREE5_1.ls[x])
            if (Code04_QTREE5_1.rs[f] != 0):
                jset(Code04_QTREE5_1.fa, Code04_QTREE5_1.rs[f], f)
            Code04_QTREE5_1.ls[x] = jcast('int', f)
        if (not Code04_QTREE5_1.isroot(f)):
            if (Code04_QTREE5_1.lr(f) == 0):
                Code04_QTREE5_1.ls[g] = jcast('int', x)
            else:
                Code04_QTREE5_1.rs[g] = jcast('int', x)
        Code04_QTREE5_1.fa[f] = jcast('int', x)
        Code04_QTREE5_1.fa[x] = jcast('int', g)
        Code04_QTREE5_1.up(f)
        Code04_QTREE5_1.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        while (not Code04_QTREE5_1.isroot(x)):
            f = jcast('int', Code04_QTREE5_1.fa[x])
            if (not Code04_QTREE5_1.isroot(f)):
                if (Code04_QTREE5_1.lr(x) == Code04_QTREE5_1.lr(f)):
                    Code04_QTREE5_1.rotate(f)
                else:
                    Code04_QTREE5_1.rotate(x)
            Code04_QTREE5_1.rotate(x)
        Code04_QTREE5_1.up(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code04_QTREE5_1.splay(x)
            if (Code04_QTREE5_1.rs[x] != 0):
                Code04_QTREE5_1.insert(x, Code04_QTREE5_1.lm[Code04_QTREE5_1.rs[x]])
            if (y != 0):
                Code04_QTREE5_1.remove(x, Code04_QTREE5_1.lm[y])
            Code04_QTREE5_1.rs[x] = jcast('int', y)
            Code04_QTREE5_1.up(x)
            y = jcast('int', x)
            x = jcast('int', Code04_QTREE5_1.fa[x])

    @staticmethod
    def reverseColor(x):
        x = jcast('int', x)
        Code04_QTREE5_1.access(x)
        Code04_QTREE5_1.splay(x)
        Code04_QTREE5_1.color[x] = jcast('int', jcast('int', (Code04_QTREE5_1.color[x] ^ 1)))
        Code04_QTREE5_1.up(x)

    @staticmethod
    def query(x):
        x = jcast('int', x)
        Code04_QTREE5_1.access(x)
        Code04_QTREE5_1.splay(x)
        # access(x)之后，x是当前辅助splay中，深度最大的节点
        # 所以rm[x]就是x到最近白点的距离
        return jcast('int', (jcast('int', (-1)) if (Code04_QTREE5_1.rm[x] == Code04_QTREE5_1.INF) else Code04_QTREE5_1.rm[x]))

    @staticmethod
    def dfs(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code04_QTREE5_1.fa[u] = jcast('int', f)
        Code04_QTREE5_1.siz[u] = jcast('int', 1)
        jset(Code04_QTREE5_1.lm, u, jset(Code04_QTREE5_1.rm, u, Code04_QTREE5_1.INF))
        e = jcast('int', Code04_QTREE5_1.head[u])
        while (e != 0):
            v = jcast('int', Code04_QTREE5_1.to[e])
            if (v != f):
                Code04_QTREE5_1.dfs(v, u)
                # 初始认为不存在实链，每个v都是u的虚儿子
                Code04_QTREE5_1.insert(u, Code04_QTREE5_1.lm[v])
            e = jcast('int', Code04_QTREE5_1.nxt[e])

    @staticmethod
    def main(args):
        in_ = Code04_QTREE5_1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_QTREE5_1.n = jcast('int', jcall(in_, 'nextInt'))
        jset(Code04_QTREE5_1.lm, 0, jset(Code04_QTREE5_1.rm, 0, Code04_QTREE5_1.INF))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code04_QTREE5_1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code04_QTREE5_1.addEdge(u, v)
            Code04_QTREE5_1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code04_QTREE5_1.dfs(1, 0)
        Code04_QTREE5_1.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        op = 0
        x = 0
        while (i <= Code04_QTREE5_1.q):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            if (op == 0):
                Code04_QTREE5_1.reverseColor(x)
            else:
                jcall(out, 'println', Code04_QTREE5_1.query(x))
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
            raise TypeError("No matching overload for Code04_QTREE5_1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_QTREE5_1.MAXN = jcast('int', 100001)
Code04_QTREE5_1.INF = jcast('int', 1000000001)
Code04_QTREE5_1.n = jcast('int', 0)
Code04_QTREE5_1.q = jcast('int', 0)
Code04_QTREE5_1.head = jarray('int', [Code04_QTREE5_1.MAXN])
Code04_QTREE5_1.nxt = jarray('int', [jcast('int', (Code04_QTREE5_1.MAXN << (1 & 31)))])
Code04_QTREE5_1.to = jarray('int', [jcast('int', (Code04_QTREE5_1.MAXN << (1 & 31)))])
Code04_QTREE5_1.cntg = jcast('int', 0)
Code04_QTREE5_1.fa = jarray('int', [Code04_QTREE5_1.MAXN])
Code04_QTREE5_1.ls = jarray('int', [Code04_QTREE5_1.MAXN])
Code04_QTREE5_1.rs = jarray('int', [Code04_QTREE5_1.MAXN])
Code04_QTREE5_1.color = jarray('int', [Code04_QTREE5_1.MAXN])
Code04_QTREE5_1.siz = jarray('int', [Code04_QTREE5_1.MAXN])
Code04_QTREE5_1.lm = jarray('int', [Code04_QTREE5_1.MAXN])
Code04_QTREE5_1.rm = jarray('int', [Code04_QTREE5_1.MAXN])
Code04_QTREE5_1.vir = jnew('HashMap')

if __name__ == '__main__':
    Code04_QTREE5_1.main([])
