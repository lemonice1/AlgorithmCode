# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 初始化，Python版
# 给定一个长度为n的数组arr，接下来有m条操作，操作格式如下
# 操作 1 x y z : 从arr[y]开始，下标每次+x，所有相应位置的数都+z，题目保证 y <= x
# 操作 2 x y   : 打印arr[x..y]的累加和，答案对1000000007取余
# 1 <= n、m <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P5309
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Initialization2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'MOD': 'MOD', 'n': 'n', 'm': 'm', 'pre': 'pre', 'suf': 'suf', 'arr': 'arr', 'sum': 'sum', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'bl': 'bl', 'br': 'br'}
    MAXN = 0
    MAXB = 0
    MOD = 0
    n = 0
    m = 0
    pre = None
    suf = None
    arr = None
    sum = None
    blen = 0
    bnum = 0
    bi = None
    bl = None
    br = None
    @staticmethod
    def add(x, y, z):
        x = jcast('int', x)
        y = jcast('int', y)
        z = jcast('int', z)
        if (x <= Code04_Initialization2.blen):
            i = jcast('int', y)
            while (i <= x):
                ((_java_obj_1 := Code04_Initialization2.pre[x]), (_java_key_2 := i), jset(_java_obj_1, _java_key_2, jcast('long', jadd(jget(_java_obj_1, _java_key_2), z))))[2]
                i = jcast('int', (i + 1))
            i = jcast('int', y)
            while (i >= 1):
                ((_java_obj_3 := Code04_Initialization2.suf[x]), (_java_key_4 := i), jset(_java_obj_3, _java_key_4, jcast('long', jadd(jget(_java_obj_3, _java_key_4), z))))[2]
                i = jcast('int', (i - 1))
        else:
            i = jcast('int', y)
            while (i <= Code04_Initialization2.n):
                Code04_Initialization2.arr[i] = jcast('long', jcast('long', jadd(Code04_Initialization2.arr[i], z)))
                ((_java_obj_5 := Code04_Initialization2.sum), (_java_key_6 := Code04_Initialization2.bi[i]), jset(_java_obj_5, _java_key_6, jcast('long', jadd(jget(_java_obj_5, _java_key_6), z))))[2]
                i = jcast('int', jcast('int', jadd(i, x)))

    @staticmethod
    def querySum(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        lb = jcast('int', Code04_Initialization2.bi[l])
        rb = jcast('int', Code04_Initialization2.bi[r])
        ans = jcast('long', 0)
        if (lb == rb):
            i = jcast('int', l)
            while (i <= r):
                ans = jcast('long', jcast('long', jadd(ans, Code04_Initialization2.arr[i])))
                i = jcast('int', (i + 1))
        else:
            i = jcast('int', l)
            while (i <= Code04_Initialization2.br[lb]):
                ans = jcast('long', jcast('long', jadd(ans, Code04_Initialization2.arr[i])))
                i = jcast('int', (i + 1))
            i = jcast('int', Code04_Initialization2.bl[rb])
            while (i <= r):
                ans = jcast('long', jcast('long', jadd(ans, Code04_Initialization2.arr[i])))
                i = jcast('int', (i + 1))
            b = jcast('int', jcast('int', jadd(lb, 1)))
            while (b <= jcast('int', (rb - 1))):
                ans = jcast('long', jcast('long', jadd(ans, Code04_Initialization2.sum[b])))
                b = jcast('int', (b + 1))
        return jcast('long', ans)

    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        ans = jcast('long', Code04_Initialization2.querySum(l, r))
        x = jcast('int', 1)
        lth = 0
        rth = 0
        num = 0
        while (x <= Code04_Initialization2.blen):
            lth = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (l - 1)), x)), 1)))
            rth = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (r - 1)), x)), 1)))
            num = jcast('int', jcast('int', (jcast('int', (rth - lth)) - 1)))
            if (lth == rth):
                ans = jcast('long', jcast('long', (jcast('long', jadd(ans, Code04_Initialization2.pre[x][jcast('int', jadd(jcast('int', jmod(jcast('int', (r - 1)), x)), 1))])) - Code04_Initialization2.pre[x][jcast('int', jmod(jcast('int', (l - 1)), x))])))
            else:
                ans = jcast('long', jcast('long', jadd(jcast('long', jadd(jcast('long', jadd(ans, Code04_Initialization2.suf[x][jcast('int', jadd(jcast('int', jmod(jcast('int', (l - 1)), x)), 1))])), jcast('long', (jcast('long', jmod(Code04_Initialization2.pre[x][x], Code04_Initialization2.MOD)) * num)))), Code04_Initialization2.pre[x][jcast('int', jadd(jcast('int', jmod(jcast('int', (r - 1)), x)), 1))])))
            x = jcast('int', (x + 1))
        return jcast('long', jcast('long', jmod(ans, Code04_Initialization2.MOD)))

    @staticmethod
    def prepare():
        Code04_Initialization2.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code04_Initialization2.n)))
        Code04_Initialization2.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code04_Initialization2.n, Code04_Initialization2.blen)) - 1)), Code04_Initialization2.blen)))
        i = jcast('int', 1)
        while (i <= Code04_Initialization2.n):
            Code04_Initialization2.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code04_Initialization2.blen)), 1)))
            i = jcast('int', (i + 1))
        b = jcast('int', 1)
        while (b <= Code04_Initialization2.bnum):
            Code04_Initialization2.bl[b] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (b - 1)) * Code04_Initialization2.blen)), 1)))
            jset(Code04_Initialization2.br, b, jstatic('Math', 'min', jcast('int', (b * Code04_Initialization2.blen)), Code04_Initialization2.n))
            i = jcast('int', Code04_Initialization2.bl[b])
            while (i <= Code04_Initialization2.br[b]):
                Code04_Initialization2.sum[b] = jcast('long', jcast('long', jadd(Code04_Initialization2.sum[b], Code04_Initialization2.arr[i])))
                i = jcast('int', (i + 1))
            b = jcast('int', (b + 1))

    @staticmethod
    def main(args):
        in_ = Code04_Initialization2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_Initialization2.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_Initialization2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_Initialization2.n):
            jset(Code04_Initialization2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code04_Initialization2.prepare()
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        z = 0
        while (i <= Code04_Initialization2.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                z = jcast('int', jcall(in_, 'nextInt'))
                Code04_Initialization2.add(x, y, z)
            else:
                jcall(out, 'println', Code04_Initialization2.query(x, y))
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
            return jcast('int', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

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
            raise TypeError("No matching overload for Code04_Initialization2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Initialization2.MAXN = jcast('int', 200001)
Code04_Initialization2.MAXB = jcast('int', 501)
Code04_Initialization2.MOD = jcast('int', 1000000007)
Code04_Initialization2.n = jcast('int', 0)
Code04_Initialization2.m = jcast('int', 0)
Code04_Initialization2.pre = jarray('long', [Code04_Initialization2.MAXB, Code04_Initialization2.MAXB])
Code04_Initialization2.suf = jarray('long', [Code04_Initialization2.MAXB, Code04_Initialization2.MAXB])
Code04_Initialization2.arr = jarray('long', [Code04_Initialization2.MAXN])
Code04_Initialization2.sum = jarray('long', [Code04_Initialization2.MAXB])
Code04_Initialization2.blen = jcast('int', 0)
Code04_Initialization2.bnum = jcast('int', 0)
Code04_Initialization2.bi = jarray('int', [Code04_Initialization2.MAXN])
Code04_Initialization2.bl = jarray('int', [Code04_Initialization2.MAXB])
Code04_Initialization2.br = jarray('int', [Code04_Initialization2.MAXB])

if __name__ == '__main__':
    Code04_Initialization2.main([])
