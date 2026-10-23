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

# 永无乡，Python版
# 一共有n个岛，每个岛分配到一个不同的数字，数字范围1~n
# 给定初始的m座桥梁，若干点会连通起来，接下来有q条操作，格式如下
# 操作 B x y : x号岛和y号岛之间新修建了一座桥
# 操作 Q x k : x号岛所在的连通区里，打印第k小的数字来自几号岛，不存在打印-1
# 1 <= n、m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3224
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_NeverLand2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 'q': 'q', 'pos': 'pos', 'father': 'father', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'siz': 'siz', 'cntt': 'cntt'}
    MAXN = 0
    MAXT = 0
    n = 0
    m = 0
    q = 0
    # pos[v] = i，表示数字v属于第i号岛
    pos = None
    # 并查集
    father = None
    # 权值线段树
    root = None
    ls = None
    rs = None
    siz = None
    cntt = 0
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code02_NeverLand2.siz[i] = jcast('int', jcast('int', jadd(Code02_NeverLand2.siz[Code02_NeverLand2.ls[i]], Code02_NeverLand2.siz[Code02_NeverLand2.rs[i]])))

    @staticmethod
    def add(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', i)
        if (rt == 0):
            rt = jcast('int', ((_java_obj_1 := Code02_NeverLand2), (_java_key_2 := 'cntt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        if (l == r):
            Code02_NeverLand2.siz[rt] = jcast('int', (Code02_NeverLand2.siz[rt] + 1))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code02_NeverLand2.ls, rt, Code02_NeverLand2.add(jobi, l, mid, Code02_NeverLand2.ls[rt]))
            else:
                jset(Code02_NeverLand2.rs, rt, Code02_NeverLand2.add(jobi, jcast('int', jadd(mid, 1)), r, Code02_NeverLand2.rs[rt]))
            Code02_NeverLand2.up(rt)
        return jcast('int', rt)

    @staticmethod
    def merge(l, r, t1, t2):
        l = jcast('int', l)
        r = jcast('int', r)
        t1 = jcast('int', t1)
        t2 = jcast('int', t2)
        if ((t1 == 0) or (t2 == 0)):
            return jcast('int', jcast('int', jadd(t1, t2)))
        if (l == r):
            Code02_NeverLand2.siz[t1] = jcast('int', jcast('int', jadd(Code02_NeverLand2.siz[t1], Code02_NeverLand2.siz[t2])))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code02_NeverLand2.ls, t1, Code02_NeverLand2.merge(l, mid, Code02_NeverLand2.ls[t1], Code02_NeverLand2.ls[t2]))
            jset(Code02_NeverLand2.rs, t1, Code02_NeverLand2.merge(jcast('int', jadd(mid, 1)), r, Code02_NeverLand2.rs[t1], Code02_NeverLand2.rs[t2]))
            Code02_NeverLand2.up(t1)
        return jcast('int', t1)

    @staticmethod
    def query(jobk, l, r, i):
        jobk = jcast('int', jobk)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((i == 0) or (jobk > Code02_NeverLand2.siz[i])):
            return jcast('int', jcast('int', (-1)))
        if (l == r):
            return jcast('int', Code02_NeverLand2.pos[l])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        if (Code02_NeverLand2.siz[Code02_NeverLand2.ls[i]] >= jobk):
            return jcast('int', Code02_NeverLand2.query(jobk, l, mid, Code02_NeverLand2.ls[i]))
        else:
            return jcast('int', Code02_NeverLand2.query(jcast('int', (jobk - Code02_NeverLand2.siz[Code02_NeverLand2.ls[i]])), jcast('int', jadd(mid, 1)), r, Code02_NeverLand2.rs[i]))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code02_NeverLand2.father[i]):
            jset(Code02_NeverLand2.father, i, Code02_NeverLand2.find(Code02_NeverLand2.father[i]))
        return jcast('int', Code02_NeverLand2.father[i])

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        xfa = jcast('int', Code02_NeverLand2.find(x))
        yfa = jcast('int', Code02_NeverLand2.find(y))
        if (xfa != yfa):
            Code02_NeverLand2.father[xfa] = jcast('int', yfa)
            jset(Code02_NeverLand2.root, yfa, Code02_NeverLand2.merge(1, Code02_NeverLand2.n, Code02_NeverLand2.root[yfa], Code02_NeverLand2.root[xfa]))

    @staticmethod
    def main(args):
        in_ = Code02_NeverLand2.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_NeverLand2.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_NeverLand2.m = jcast('int', jcall(in_, 'nextInt'))
        num = 0
        i = jcast('int', 1)
        while (i <= Code02_NeverLand2.n):
            num = jcast('int', jcall(in_, 'nextInt'))
            Code02_NeverLand2.pos[num] = jcast('int', i)
            Code02_NeverLand2.father[i] = jcast('int', i)
            jset(Code02_NeverLand2.root, i, Code02_NeverLand2.add(num, 1, Code02_NeverLand2.n, Code02_NeverLand2.root[i]))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= Code02_NeverLand2.m):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            Code02_NeverLand2.union(x, y)
            i = jcast('int', (i + 1))
        Code02_NeverLand2.q = jcast('int', jcall(in_, 'nextInt'))
        op = jchar(0)
        x = 0
        y = 0
        k = 0
        i = jcast('int', 1)
        while (i <= Code02_NeverLand2.q):
            op = jcast('char', jcall(in_, 'nextChar'))
            if (op == jchar('B')):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                Code02_NeverLand2.union(x, y)
            else:
                x = jcast('int', jcall(in_, 'nextInt'))
                k = jcast('int', jcall(in_, 'nextInt'))
                jcall(out, 'println', Code02_NeverLand2.query(k, 1, Code02_NeverLand2.n, Code02_NeverLand2.root[Code02_NeverLand2.find(x)]))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'BUFFER_SIZE': 'BUFFER_SIZE', 'in': 'in_', 'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len'}
        # BUFFER_SIZE：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.in_ = jget(System, 'in')
            self.buffer = jarray('byte', [self.BUFFER_SIZE])
            self.ptr = jcast('int', jset(self, 'len', 0))

        def hasNextByte(self):
            if (self.ptr < self.len):
                return jcast('boolean', True)
            self.ptr = jcast('int', 0)
            self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
            return jcast('boolean', (self.len > 0))

        def readByte(self):
            if (not self.hasNextByte()):
                return jcast('byte', jcast('int', (-1)))
            return jcast('byte', self.buffer[((_java_obj_4 := self), (_java_key_5 := 'ptr'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]])

        def nextChar(self):
            c = 0
            while True:
                c = jcast('byte', self.readByte())
                if (c == jcast('int', (-1))):
                    return jcast('char', 0)
                if not ((c <= jchar(' '))):
                    break
            ans = jcast('char', 0)
            while (c > jchar(' ')):
                ans = jcast('char', jcast('char', c))
                c = jcast('byte', self.readByte())
            return jcast('char', ans)

        def nextInt(self):
            num = jcast('int', 0)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                num = jcast('int', jcast('int', jadd(jcast('int', (num * 10)), jcast('int', (b - jchar('0'))))))
                b = jcast('byte', self.readByte())
            return jcast('int', (jcast('int', (-num)) if minus else num))

        def isWhitespace(self, b):
            b = jcast('byte', b)
            return jcast('boolean', ((((b == jchar(' ')) or (b == jchar('\n'))) or (b == jchar('\r'))) or (b == jchar('\t'))))

        def __init__(self, *args, _java_ctor=None):
            self.BUFFER_SIZE = jcast('int', jcast('int', (1 << (16 & 31))))
            self.in_ = None
            self.buffer = None
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_NeverLand2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_NeverLand2.MAXN = jcast('int', 100001)
Code02_NeverLand2.MAXT = jcast('int', jcast('int', (Code02_NeverLand2.MAXN * 40)))
Code02_NeverLand2.n = jcast('int', 0)
Code02_NeverLand2.m = jcast('int', 0)
Code02_NeverLand2.q = jcast('int', 0)
Code02_NeverLand2.pos = jarray('int', [Code02_NeverLand2.MAXN])
Code02_NeverLand2.father = jarray('int', [Code02_NeverLand2.MAXN])
Code02_NeverLand2.root = jarray('int', [Code02_NeverLand2.MAXN])
Code02_NeverLand2.ls = jarray('int', [Code02_NeverLand2.MAXT])
Code02_NeverLand2.rs = jarray('int', [Code02_NeverLand2.MAXT])
Code02_NeverLand2.siz = jarray('int', [Code02_NeverLand2.MAXT])
Code02_NeverLand2.cntt = jcast('int', 0)

if __name__ == '__main__':
    Code02_NeverLand2.main([])
