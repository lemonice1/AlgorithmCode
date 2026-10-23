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

# 区间父变小，Python版
# 一棵大小为n树，节点1是树头，给定fa[2..n]表示父亲节点编号
# 对于每个i > 1，都有fa[i] < i，下来有m条操作，操作类型如下
# 操作 1 x y z : [x..y]范围上任何一点i，fa[i] = max(1, fa[i] - z)
# 操作 2 x y   : 查询点x和点y的最低公共祖先
# 2 <= n、m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF1491H
# 测试链接 : https://codeforces.com/problemset/problem/1491/H
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code08_FatherMinus1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'fa': 'fa', 'out': 'out', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'bl': 'bl', 'br': 'br', 'lazy': 'lazy', 'minusCnt': 'minusCnt'}
    MAXN = 0
    MAXB = 0
    n = 0
    m = 0
    # 节点的父亲节点
    fa = None
    # 节点如果从所在块出去，会去往的最近节点
    out = None
    blen = 0
    bnum = 0
    bi = None
    bl = None
    br = None
    # 块内所有节点的父亲编号，统一减少的幅度
    lazy = None
    # 块内所有节点的父亲编号，统一削减的次数
    minusCnt = None
    @staticmethod
    def innerUpdate(b):
        b = jcast('int', b)
        i = jcast('int', Code08_FatherMinus1.bl[b])
        while (i <= Code08_FatherMinus1.br[b]):
            jset(Code08_FatherMinus1.fa, i, jstatic('Math', 'max', 1, jcast('int', (Code08_FatherMinus1.fa[i] - Code08_FatherMinus1.lazy[b]))))
            i = jcast('int', (i + 1))
        Code08_FatherMinus1.lazy[b] = jcast('int', 0)
        i = jcast('int', Code08_FatherMinus1.bl[b])
        while (i <= Code08_FatherMinus1.br[b]):
            if (Code08_FatherMinus1.fa[i] < Code08_FatherMinus1.bl[b]):
                Code08_FatherMinus1.out[i] = jcast('int', Code08_FatherMinus1.fa[i])
            else:
                Code08_FatherMinus1.out[i] = jcast('int', Code08_FatherMinus1.out[Code08_FatherMinus1.fa[i]])
            i = jcast('int', (i + 1))

    @staticmethod
    def update(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        if (Code08_FatherMinus1.bi[l] == Code08_FatherMinus1.bi[r]):
            i = jcast('int', l)
            while (i <= r):
                jset(Code08_FatherMinus1.fa, i, jstatic('Math', 'max', 1, jcast('int', (Code08_FatherMinus1.fa[i] - v))))
                i = jcast('int', (i + 1))
            Code08_FatherMinus1.innerUpdate(Code08_FatherMinus1.bi[l])
        else:
            i = jcast('int', l)
            while (i <= Code08_FatherMinus1.br[Code08_FatherMinus1.bi[l]]):
                jset(Code08_FatherMinus1.fa, i, jstatic('Math', 'max', 1, jcast('int', (Code08_FatherMinus1.fa[i] - v))))
                i = jcast('int', (i + 1))
            Code08_FatherMinus1.innerUpdate(Code08_FatherMinus1.bi[l])
            i = jcast('int', Code08_FatherMinus1.bl[Code08_FatherMinus1.bi[r]])
            while (i <= r):
                jset(Code08_FatherMinus1.fa, i, jstatic('Math', 'max', 1, jcast('int', (Code08_FatherMinus1.fa[i] - v))))
                i = jcast('int', (i + 1))
            Code08_FatherMinus1.innerUpdate(Code08_FatherMinus1.bi[r])
            b = jcast('int', jcast('int', jadd(Code08_FatherMinus1.bi[l], 1)))
            while (b <= jcast('int', (Code08_FatherMinus1.bi[r] - 1))):
                # 减少的幅度最多到n，不会更大
                # 这样还可以让lazy保持int类型并且不溢出
                jset(Code08_FatherMinus1.lazy, b, jstatic('Math', 'min', Code08_FatherMinus1.n, jcast('int', jadd(Code08_FatherMinus1.lazy[b], v))))
                if (((_java_obj_1 := Code08_FatherMinus1.minusCnt), (_java_key_2 := b), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3] <= Code08_FatherMinus1.blen):
                    Code08_FatherMinus1.innerUpdate(b)
                b = jcast('int', (b + 1))

    @staticmethod
    def jumpFa(i):
        i = jcast('int', i)
        return jcast('int', jstatic('Math', 'max', 1, jcast('int', (Code08_FatherMinus1.fa[i] - Code08_FatherMinus1.lazy[Code08_FatherMinus1.bi[i]]))))

    @staticmethod
    def jumpOut(i):
        i = jcast('int', i)
        return jcast('int', jstatic('Math', 'max', 1, jcast('int', (Code08_FatherMinus1.out[i] - Code08_FatherMinus1.lazy[Code08_FatherMinus1.bi[i]]))))

    @staticmethod
    def lca(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        while ((Code08_FatherMinus1.bi[x] != Code08_FatherMinus1.bi[y]) or (Code08_FatherMinus1.jumpOut(x) != Code08_FatherMinus1.jumpOut(y))):
            if (Code08_FatherMinus1.bi[x] != Code08_FatherMinus1.bi[y]):
                if (Code08_FatherMinus1.bi[x] < Code08_FatherMinus1.bi[y]):
                    tmp = jcast('int', x)
                    x = jcast('int', y)
                    y = jcast('int', tmp)
                x = jcast('int', Code08_FatherMinus1.jumpOut(x))
            else:
                x = jcast('int', Code08_FatherMinus1.jumpOut(x))
                y = jcast('int', Code08_FatherMinus1.jumpOut(y))
        while (x != y):
            if (x < y):
                tmp = jcast('int', x)
                x = jcast('int', y)
                y = jcast('int', tmp)
            x = jcast('int', Code08_FatherMinus1.jumpFa(x))
        return jcast('int', x)

    @staticmethod
    def prepare():
        Code08_FatherMinus1.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code08_FatherMinus1.n)))
        Code08_FatherMinus1.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code08_FatherMinus1.n, Code08_FatherMinus1.blen)) - 1)), Code08_FatherMinus1.blen)))
        i = jcast('int', 1)
        while (i <= Code08_FatherMinus1.n):
            Code08_FatherMinus1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code08_FatherMinus1.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code08_FatherMinus1.bnum):
            Code08_FatherMinus1.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code08_FatherMinus1.blen)), 1)))
            jset(Code08_FatherMinus1.br, i, jstatic('Math', 'min', jcast('int', (i * Code08_FatherMinus1.blen)), Code08_FatherMinus1.n))
            Code08_FatherMinus1.innerUpdate(i)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code08_FatherMinus1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code08_FatherMinus1.n = jcast('int', jcall(in_, 'nextInt'))
        Code08_FatherMinus1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 2)
        while (i <= Code08_FatherMinus1.n):
            jset(Code08_FatherMinus1.fa, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code08_FatherMinus1.prepare()
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        z = 0
        while (i <= Code08_FatherMinus1.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                z = jcast('int', jcall(in_, 'nextInt'))
                Code08_FatherMinus1.update(x, y, z)
            else:
                jcall(out, 'println', Code08_FatherMinus1.lca(x, y))
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
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('int', (jcast('int', (-val)) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code08_FatherMinus1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code08_FatherMinus1.MAXN = jcast('int', 100001)
Code08_FatherMinus1.MAXB = jcast('int', 501)
Code08_FatherMinus1.n = jcast('int', 0)
Code08_FatherMinus1.m = jcast('int', 0)
Code08_FatherMinus1.fa = jarray('int', [Code08_FatherMinus1.MAXN])
Code08_FatherMinus1.out = jarray('int', [Code08_FatherMinus1.MAXN])
Code08_FatherMinus1.blen = jcast('int', 0)
Code08_FatherMinus1.bnum = jcast('int', 0)
Code08_FatherMinus1.bi = jarray('int', [Code08_FatherMinus1.MAXN])
Code08_FatherMinus1.bl = jarray('int', [Code08_FatherMinus1.MAXB])
Code08_FatherMinus1.br = jarray('int', [Code08_FatherMinus1.MAXB])
Code08_FatherMinus1.lazy = jarray('int', [Code08_FatherMinus1.MAXB])
Code08_FatherMinus1.minusCnt = jarray('int', [Code08_FatherMinus1.MAXB])

if __name__ == '__main__':
    Code08_FatherMinus1.main([])
