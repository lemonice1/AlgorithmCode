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

# 三叉神经树，Python版
# 节点有两种类型，细胞节点编号范围[1, n]，信号节点编号范围[n+1, 3*n+1]
# 每个信号节点没有儿子节点，每个细胞节点固定有三个儿子节点
# 给定每个细胞节点的三个儿子节点编号，每个儿子可能是细胞节点，或者信号节点
# 每个信号节点拥有自身的值，是0或者1，初始值会给定，该值向上输出给父节点
# 每个细胞节点没有自身的值，根据三个儿子的信号，决定向上的输出
# 三个儿子节点中，1多就向上输出1，0多就向上输出0，也是向上输出给父节点
# 一共q条操作，每次给定一个信号节点的编号，表示它的值发生了翻转
# 题目保证1号节点是整棵树的根，每次操作执行完，都打印1号节点的输出
# 1 <= n、q <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4332
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_TrigeminalTree1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'q': 'q', 'parent': 'parent', 'que': 'que', 'degree': 'degree', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'cnt': 'cnt', 'sig': 'sig', 'stop1': 'stop1', 'stop2': 'stop2', 'tag': 'tag', 'sta': 'sta', 'ans': 'ans'}
    MAXN = 0
    MAXT = 0
    n = 0
    q = 0
    # 原树的父节点
    parent = None
    # 拓扑排序，设置节点的初始输出
    que = None
    degree = None
    # 辅助splay
    fa = None
    ls = None
    rs = None
    # cnt[i]，细胞节点i的儿子中，输出为1的儿子数量，范围0~3
    cnt = None
    # sig[i]，信号节点i的值，范围0~1
    sig = None
    # x所在的实链中，从下往上第一个cnt != 1的节点，当外部输入从0变1时
    # 从下往上一路连续的cnt == 1的节点都改变输出，最终停在stop1[x]
    stop1 = None
    # x所在的实链中，从下往上第一个cnt != 2的节点，当外部输入从1变0时
    # 从下往上一路连续的cnt == 2的节点都改变输出，最终停在stop2[x]
    stop2 = None
    # 本题没有左右孩子的翻转，但是有传导状态的翻转，tag就表示这个
    tag = None
    sta = None
    # 1号节点的输出
    ans = 0
    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code03_TrigeminalTree1.stop1[x] = jcast('int', Code03_TrigeminalTree1.stop1[Code03_TrigeminalTree1.rs[x]])
        if ((Code03_TrigeminalTree1.stop1[x] == 0) and (Code03_TrigeminalTree1.cnt[x] != 1)):
            Code03_TrigeminalTree1.stop1[x] = jcast('int', x)
        if (Code03_TrigeminalTree1.stop1[x] == 0):
            Code03_TrigeminalTree1.stop1[x] = jcast('int', Code03_TrigeminalTree1.stop1[Code03_TrigeminalTree1.ls[x]])
        Code03_TrigeminalTree1.stop2[x] = jcast('int', Code03_TrigeminalTree1.stop2[Code03_TrigeminalTree1.rs[x]])
        if ((Code03_TrigeminalTree1.stop2[x] == 0) and (Code03_TrigeminalTree1.cnt[x] != 2)):
            Code03_TrigeminalTree1.stop2[x] = jcast('int', x)
        if (Code03_TrigeminalTree1.stop2[x] == 0):
            Code03_TrigeminalTree1.stop2[x] = jcast('int', Code03_TrigeminalTree1.stop2[Code03_TrigeminalTree1.ls[x]])

    # 传导状态翻转，只作用在连续传导段上
    # 要么连续一段，全是cnt == 1，变成cnt == 2
    # 要么连续一段，全是cnt == 2，变成cnt == 1
    # 只涉及这两种场景，不会有其他的cnt值
    @staticmethod
    def effect(x):
        x = jcast('int', x)
        if (x != 0):
            Code03_TrigeminalTree1.cnt[x] = jcast('int', jcast('int', (Code03_TrigeminalTree1.cnt[x] ^ 3)))
            tmp = jcast('int', Code03_TrigeminalTree1.stop1[x])
            Code03_TrigeminalTree1.stop1[x] = jcast('int', Code03_TrigeminalTree1.stop2[x])
            Code03_TrigeminalTree1.stop2[x] = jcast('int', tmp)
            Code03_TrigeminalTree1.tag[x] = jcast('boolean', (not Code03_TrigeminalTree1.tag[x]))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code03_TrigeminalTree1.ls[Code03_TrigeminalTree1.fa[x]] != x) and (Code03_TrigeminalTree1.rs[Code03_TrigeminalTree1.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code03_TrigeminalTree1.ls[Code03_TrigeminalTree1.fa[x]] == x) else 1))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code03_TrigeminalTree1.tag[x]:
            Code03_TrigeminalTree1.effect(Code03_TrigeminalTree1.ls[x])
            Code03_TrigeminalTree1.effect(Code03_TrigeminalTree1.rs[x])
            Code03_TrigeminalTree1.tag[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code03_TrigeminalTree1.fa[x])
        g = jcast('int', Code03_TrigeminalTree1.fa[f])
        if (Code03_TrigeminalTree1.lr(x) == 0):
            Code03_TrigeminalTree1.ls[f] = jcast('int', Code03_TrigeminalTree1.rs[x])
            if (Code03_TrigeminalTree1.ls[f] != 0):
                jset(Code03_TrigeminalTree1.fa, Code03_TrigeminalTree1.ls[f], f)
            Code03_TrigeminalTree1.rs[x] = jcast('int', f)
        else:
            Code03_TrigeminalTree1.rs[f] = jcast('int', Code03_TrigeminalTree1.ls[x])
            if (Code03_TrigeminalTree1.rs[f] != 0):
                jset(Code03_TrigeminalTree1.fa, Code03_TrigeminalTree1.rs[f], f)
            Code03_TrigeminalTree1.ls[x] = jcast('int', f)
        if (not Code03_TrigeminalTree1.isroot(f)):
            if (Code03_TrigeminalTree1.lr(f) == 0):
                Code03_TrigeminalTree1.ls[g] = jcast('int', x)
            else:
                Code03_TrigeminalTree1.rs[g] = jcast('int', x)
        Code03_TrigeminalTree1.fa[f] = jcast('int', x)
        Code03_TrigeminalTree1.fa[x] = jcast('int', g)
        Code03_TrigeminalTree1.up(f)
        Code03_TrigeminalTree1.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code03_TrigeminalTree1.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code03_TrigeminalTree1.isroot(y)):
            jset(Code03_TrigeminalTree1.sta, (siz := jcast('int', (siz + (1)))), Code03_TrigeminalTree1.fa[y])
            y = jcast('int', Code03_TrigeminalTree1.fa[y])
        while (siz != 0):
            Code03_TrigeminalTree1.down(Code03_TrigeminalTree1.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code03_TrigeminalTree1.isroot(x)):
            f = jcast('int', Code03_TrigeminalTree1.fa[x])
            if (not Code03_TrigeminalTree1.isroot(f)):
                if (Code03_TrigeminalTree1.lr(x) == Code03_TrigeminalTree1.lr(f)):
                    Code03_TrigeminalTree1.rotate(f)
                else:
                    Code03_TrigeminalTree1.rotate(x)
            Code03_TrigeminalTree1.rotate(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code03_TrigeminalTree1.splay(x)
            Code03_TrigeminalTree1.rs[x] = jcast('int', y)
            Code03_TrigeminalTree1.up(x)
            y = jcast('int', x)
            x = jcast('int', Code03_TrigeminalTree1.fa[x])

    @staticmethod
    def change(x):
        x = jcast('int', x)
        Code03_TrigeminalTree1.sig[x] = jcast('int', jcast('int', (Code03_TrigeminalTree1.sig[x] ^ 1)))
        delta = jcast('int', (1 if (Code03_TrigeminalTree1.sig[x] == 1) else jcast('int', (-1))))
        x = jcast('int', Code03_TrigeminalTree1.parent[x])
        Code03_TrigeminalTree1.access(x)
        Code03_TrigeminalTree1.splay(x)
        stop = jcast('int', (Code03_TrigeminalTree1.stop1[x] if (delta == 1) else Code03_TrigeminalTree1.stop2[x]))
        if (stop != 0):
            Code03_TrigeminalTree1.splay(stop)
            Code03_TrigeminalTree1.effect(Code03_TrigeminalTree1.rs[stop])
            Code03_TrigeminalTree1.cnt[stop] = jcast('int', jcast('int', jadd(Code03_TrigeminalTree1.cnt[stop], delta)))
            Code03_TrigeminalTree1.up(stop)
        else:
            Code03_TrigeminalTree1.effect(x)
            Code03_TrigeminalTree1.ans = jcast('int', jcast('int', (Code03_TrigeminalTree1.ans ^ 1)))

    @staticmethod
    def get01(x):
        x = jcast('int', x)
        if (x <= Code03_TrigeminalTree1.n):
            return jcast('int', (0 if (Code03_TrigeminalTree1.cnt[x] <= 1) else 1))
        else:
            return jcast('int', Code03_TrigeminalTree1.sig[x])

    @staticmethod
    def topo():
        i = jcast('int', 1)
        while (i <= Code03_TrigeminalTree1.n):
            Code03_TrigeminalTree1.degree[i] = jcast('int', 3)
            i = jcast('int', (i + 1))
        l = jcast('int', 1)
        r = jcast('int', 0)
        i = jcast('int', jcast('int', jadd(Code03_TrigeminalTree1.n, 1)))
        while (i <= jcast('int', jadd(jcast('int', (3 * Code03_TrigeminalTree1.n)), 1))):
            jset(Code03_TrigeminalTree1.que, (r := jcast('int', (r + (1)))), i)
            i = jcast('int', (i + 1))
        while (l <= r):
            x = jcast('int', Code03_TrigeminalTree1.que[((_java_old_2 := l), (l := jcast('int', (l + (1)))), _java_old_2)[2]])
            if (x <= Code03_TrigeminalTree1.n):
                Code03_TrigeminalTree1.up(x)
            p = jcast('int', Code03_TrigeminalTree1.parent[x])
            if (p != 0):
                ((_java_obj_3 := Code03_TrigeminalTree1.cnt), (_java_key_4 := p), jset(_java_obj_3, _java_key_4, jcast('int', jadd(jget(_java_obj_3, _java_key_4), Code03_TrigeminalTree1.get01(x)))))[2]
                if (((_java_obj_5 := Code03_TrigeminalTree1.degree), (_java_key_6 := p), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))))[3] == 0):
                    jset(Code03_TrigeminalTree1.que, (r := jcast('int', (r + (1)))), p)

    @staticmethod
    def main(args):
        in_ = Code03_TrigeminalTree1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_TrigeminalTree1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        while (i <= Code03_TrigeminalTree1.n):
            j = jcast('int', 1)
            while (j <= 3):
                x = jcast('int', jcall(in_, 'nextInt'))
                Code03_TrigeminalTree1.parent[x] = jcast('int', i)
                if (x <= Code03_TrigeminalTree1.n):
                    Code03_TrigeminalTree1.fa[x] = jcast('int', i)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', jcast('int', jadd(Code03_TrigeminalTree1.n, 1)))
        while (i <= jcast('int', jadd(jcast('int', (3 * Code03_TrigeminalTree1.n)), 1))):
            jset(Code03_TrigeminalTree1.sig, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code03_TrigeminalTree1.topo()
        Code03_TrigeminalTree1.ans = jcast('int', Code03_TrigeminalTree1.get01(1))
        Code03_TrigeminalTree1.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        while (i <= Code03_TrigeminalTree1.q):
            x = jcast('int', jcall(in_, 'nextInt'))
            Code03_TrigeminalTree1.change(x)
            jcall(out, 'println', Code03_TrigeminalTree1.ans)
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
            return jcast('int', self.buffer[((_java_obj_8 := self), (_java_key_9 := 'ptr'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))), _java_old_10)[4]])

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
            raise TypeError("No matching overload for Code03_TrigeminalTree1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_TrigeminalTree1.MAXN = jcast('int', 500001)
Code03_TrigeminalTree1.MAXT = jcast('int', jcast('int', (Code03_TrigeminalTree1.MAXN * 3)))
Code03_TrigeminalTree1.n = jcast('int', 0)
Code03_TrigeminalTree1.q = jcast('int', 0)
Code03_TrigeminalTree1.parent = jarray('int', [Code03_TrigeminalTree1.MAXT])
Code03_TrigeminalTree1.que = jarray('int', [Code03_TrigeminalTree1.MAXT])
Code03_TrigeminalTree1.degree = jarray('int', [Code03_TrigeminalTree1.MAXN])
Code03_TrigeminalTree1.fa = jarray('int', [Code03_TrigeminalTree1.MAXN])
Code03_TrigeminalTree1.ls = jarray('int', [Code03_TrigeminalTree1.MAXN])
Code03_TrigeminalTree1.rs = jarray('int', [Code03_TrigeminalTree1.MAXN])
Code03_TrigeminalTree1.cnt = jarray('int', [Code03_TrigeminalTree1.MAXN])
Code03_TrigeminalTree1.sig = jarray('int', [Code03_TrigeminalTree1.MAXT])
Code03_TrigeminalTree1.stop1 = jarray('int', [Code03_TrigeminalTree1.MAXN])
Code03_TrigeminalTree1.stop2 = jarray('int', [Code03_TrigeminalTree1.MAXN])
Code03_TrigeminalTree1.tag = jarray('boolean', [Code03_TrigeminalTree1.MAXN])
Code03_TrigeminalTree1.sta = jarray('int', [Code03_TrigeminalTree1.MAXN])
Code03_TrigeminalTree1.ans = jcast('int', 0)

if __name__ == '__main__':
    Code03_TrigeminalTree1.main([])
