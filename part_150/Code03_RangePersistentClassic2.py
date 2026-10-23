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

# 范围修改的可持久化线段树，经典的方式，Python版
# 给定一个长度为n的数组arr，下标1~n，时间戳t=0，arr认为是0版本的数组
# 一共有m条操作，每条操作为如下四种类型中的一种
# C x y z : 当前时间戳t版本的数组，[x..y]范围每个数字增加z，得到t+1版本数组，并且t++
# Q x y   : 当前时间戳t版本的数组，打印[x..y]范围累加和
# H x y z : z版本的数组，打印[x..y]范围的累加和
# B x     : 当前时间戳t设置成x
# 1 <= n、m <= 10^5
# -10^9 <= arr[i] <= +10^9
# 测试链接 : https://www.luogu.com.cn/problem/SP11470
# 测试链接 : https://www.spoj.com/problems/TTM
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_RangePersistentClassic2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 't': 't', 'arr': 'arr', 'root': 'root', 'left': 'left', 'right': 'right', 'sum': 'sum', 'add': 'add_data', 'cnt': 'cnt'}
    MAXN = 0
    MAXT = 0
    n = 0
    m = 0
    t = 0
    arr = None
    root = None
    left = None
    right = None
    # 累加和信息
    sum = None
    # 懒更新信息，范围增加的懒更新
    add_data = None
    cnt = 0
    @staticmethod
    def clone(i):
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_1 := Code03_RangePersistentClassic2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        Code03_RangePersistentClassic2.left[rt] = jcast('int', Code03_RangePersistentClassic2.left[i])
        Code03_RangePersistentClassic2.right[rt] = jcast('int', Code03_RangePersistentClassic2.right[i])
        Code03_RangePersistentClassic2.sum[rt] = jcast('long', Code03_RangePersistentClassic2.sum[i])
        Code03_RangePersistentClassic2.add_data[rt] = jcast('long', Code03_RangePersistentClassic2.add_data[i])
        return jcast('int', rt)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code03_RangePersistentClassic2.sum[i] = jcast('long', jcast('long', jadd(Code03_RangePersistentClassic2.sum[Code03_RangePersistentClassic2.left[i]], Code03_RangePersistentClassic2.sum[Code03_RangePersistentClassic2.right[i]])))

    @staticmethod
    def lazy(i, v, n):
        i = jcast('int', i)
        v = jcast('long', v)
        n = jcast('int', n)
        Code03_RangePersistentClassic2.sum[i] = jcast('long', jcast('long', jadd(Code03_RangePersistentClassic2.sum[i], jcast('long', (v * n)))))
        Code03_RangePersistentClassic2.add_data[i] = jcast('long', jcast('long', jadd(Code03_RangePersistentClassic2.add_data[i], v)))

    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        if (Code03_RangePersistentClassic2.add_data[i] != 0):
            jset(Code03_RangePersistentClassic2.left, i, Code03_RangePersistentClassic2.clone(Code03_RangePersistentClassic2.left[i]))
            jset(Code03_RangePersistentClassic2.right, i, Code03_RangePersistentClassic2.clone(Code03_RangePersistentClassic2.right[i]))
            Code03_RangePersistentClassic2.lazy(Code03_RangePersistentClassic2.left[i], Code03_RangePersistentClassic2.add_data[i], ln)
            Code03_RangePersistentClassic2.lazy(Code03_RangePersistentClassic2.right[i], Code03_RangePersistentClassic2.add_data[i], rn)
            Code03_RangePersistentClassic2.add_data[i] = jcast('long', 0)

    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_4 := Code03_RangePersistentClassic2), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code03_RangePersistentClassic2.add_data[rt] = jcast('long', 0)
        if (l == r):
            Code03_RangePersistentClassic2.sum[rt] = jcast('long', Code03_RangePersistentClassic2.arr[l])
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            jset(Code03_RangePersistentClassic2.left, rt, Code03_RangePersistentClassic2.build(l, mid))
            jset(Code03_RangePersistentClassic2.right, rt, Code03_RangePersistentClassic2.build(jcast('int', jadd(mid, 1)), r))
            Code03_RangePersistentClassic2.up(rt)
        return jcast('int', rt)

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', Code03_RangePersistentClassic2.clone(i))
        if ((jobl <= l) and (r <= jobr)):
            Code03_RangePersistentClassic2.lazy(rt, jobv, jcast('int', jadd(jcast('int', (r - l)), 1)))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            Code03_RangePersistentClassic2.down(rt, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                jset(Code03_RangePersistentClassic2.left, rt, Code03_RangePersistentClassic2.add(jobl, jobr, jobv, l, mid, Code03_RangePersistentClassic2.left[rt]))
            if (jobr > mid):
                jset(Code03_RangePersistentClassic2.right, rt, Code03_RangePersistentClassic2.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, Code03_RangePersistentClassic2.right[rt]))
            Code03_RangePersistentClassic2.up(rt)
        return jcast('int', rt)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code03_RangePersistentClassic2.sum[i])
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code03_RangePersistentClassic2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
        ans = jcast('long', 0)
        if (jobl <= mid):
            ans = jcast('long', jcast('long', jadd(ans, Code03_RangePersistentClassic2.query(jobl, jobr, l, mid, Code03_RangePersistentClassic2.left[i]))))
        if (jobr > mid):
            ans = jcast('long', jcast('long', jadd(ans, Code03_RangePersistentClassic2.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code03_RangePersistentClassic2.right[i]))))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code03_RangePersistentClassic2.FastReader(_java_ctor=0)
        out = jnew('BufferedWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_RangePersistentClassic2.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_RangePersistentClassic2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_RangePersistentClassic2.n):
            jset(Code03_RangePersistentClassic2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        jset(Code03_RangePersistentClassic2.root, 0, Code03_RangePersistentClassic2.build(1, Code03_RangePersistentClassic2.n))
        op = None
        i = jcast('int', 1)
        x = 0
        y = 0
        z = 0
        while (i <= Code03_RangePersistentClassic2.m):
            op = jcall(in_, 'next')
            if jcall(op, 'equals', 'C'):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                z = jcast('int', jcall(in_, 'nextInt'))
                jset(Code03_RangePersistentClassic2.root, jcast('int', jadd(Code03_RangePersistentClassic2.t, 1)), Code03_RangePersistentClassic2.add(x, y, z, 1, Code03_RangePersistentClassic2.n, Code03_RangePersistentClassic2.root[Code03_RangePersistentClassic2.t]))
                Code03_RangePersistentClassic2.t = jcast('int', (Code03_RangePersistentClassic2.t + 1))
            else:
                if jcall(op, 'equals', 'Q'):
                    x = jcast('int', jcall(in_, 'nextInt'))
                    y = jcast('int', jcall(in_, 'nextInt'))
                    jcall(out, 'write', jadd(Code03_RangePersistentClassic2.query(x, y, 1, Code03_RangePersistentClassic2.n, Code03_RangePersistentClassic2.root[Code03_RangePersistentClassic2.t]), '\n'))
                else:
                    if jcall(op, 'equals', 'H'):
                        x = jcast('int', jcall(in_, 'nextInt'))
                        y = jcast('int', jcall(in_, 'nextInt'))
                        z = jcast('int', jcall(in_, 'nextInt'))
                        jcall(out, 'write', jadd(Code03_RangePersistentClassic2.query(x, y, 1, Code03_RangePersistentClassic2.n, Code03_RangePersistentClassic2.root[z]), '\n'))
                    else:
                        x = jcast('int', jcall(in_, 'nextInt'))
                        Code03_RangePersistentClassic2.t = jcast('int', x)
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
            return jcast('byte', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

        def hasNext(self):
            while self.hasNextByte():
                b = jcast('byte', self.buffer[self.ptr])
                if (not self.isWhitespace(b)):
                    return jcast('boolean', True)
                self.ptr = jcast('int', (self.ptr + 1))
            return jcast('boolean', False)

        def next(self):
            c = 0
            while True:
                c = jcast('byte', self.readByte())
                if (c == jcast('int', (-1))):
                    return None
                if not ((c <= jchar(' '))):
                    break
            sb = jnew('StringBuilder')
            while (c > jchar(' ')):
                jcall(sb, 'append', jcast('char', c))
                c = jcast('byte', self.readByte())
            return jcall(sb, 'toString')

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

        def nextDouble(self):
            num = jcast('double', 0)
            div = jcast('double', 1)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while (((not self.isWhitespace(b)) and (b != jchar('.'))) and (b != jcast('int', (-1)))):
                num = jcast('double', jadd((num * 10), jcast('int', (b - jchar('0')))))
                b = jcast('byte', self.readByte())
            if (b == jchar('.')):
                b = jcast('byte', self.readByte())
                while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                    num = jcast('double', jadd(num, jdiv(jcast('int', (b - jchar('0'))), (div := (div * 10)))))
                    b = jcast('byte', self.readByte())
            return jcast('double', ((-num) if minus else num))

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
            raise TypeError("No matching overload for Code03_RangePersistentClassic2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_RangePersistentClassic2.MAXN = jcast('int', 100001)
Code03_RangePersistentClassic2.MAXT = jcast('int', jcast('int', (Code03_RangePersistentClassic2.MAXN * 70)))
Code03_RangePersistentClassic2.n = jcast('int', 0)
Code03_RangePersistentClassic2.m = jcast('int', 0)
Code03_RangePersistentClassic2.t = jcast('int', 0)
Code03_RangePersistentClassic2.arr = jarray('int', [Code03_RangePersistentClassic2.MAXN])
Code03_RangePersistentClassic2.root = jarray('int', [Code03_RangePersistentClassic2.MAXN])
Code03_RangePersistentClassic2.left = jarray('int', [Code03_RangePersistentClassic2.MAXT])
Code03_RangePersistentClassic2.right = jarray('int', [Code03_RangePersistentClassic2.MAXT])
Code03_RangePersistentClassic2.sum = jarray('long', [Code03_RangePersistentClassic2.MAXT])
Code03_RangePersistentClassic2.add_data = jarray('long', [Code03_RangePersistentClassic2.MAXT])
Code03_RangePersistentClassic2.cnt = jcast('int', 0)

if __name__ == '__main__':
    Code03_RangePersistentClassic2.main([])
