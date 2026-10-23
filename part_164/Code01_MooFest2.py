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

# 奶牛音量和，Python版
# 一共有n只奶牛，每只奶牛给定，听力v、坐标x
# 任何一对奶牛产生的音量 = max(vi, vj) * 两只奶牛的距离
# 一共有n * (n - 1) / 2对奶牛，打印音量总和
# 1 <= n、v、x <= 5 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P5094
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_MooFest2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'arr': 'arr', 'tmp': 'tmp'}
    MAXN = 0
    n = 0
    # 听力v、位置x
    arr = None
    # 归并排序需要
    tmp = None
    @staticmethod
    def clone(a, b):
        a[0] = jcast('int', b[0])
        a[1] = jcast('int', b[1])

    @staticmethod
    def merge(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        p1 = 0
        p2 = 0
        rsum = jcast('long', 0)
        lsum = jcast('long', 0)
        ans = jcast('long', 0)
        p1 = jcast('int', l)
        while (p1 <= m):
            rsum = jcast('long', jcast('long', jadd(rsum, Code01_MooFest2.arr[p1][1])))
            p1 = jcast('int', (p1 + 1))
        p1 = jcast('int', jcast('int', (l - 1)))
        p2 = jcast('int', jcast('int', jadd(m, 1)))
        while (p2 <= r):
            while ((jcast('int', jadd(p1, 1)) <= m) and (Code01_MooFest2.arr[jcast('int', jadd(p1, 1))][1] < Code01_MooFest2.arr[p2][1])):
                p1 = jcast('int', (p1 + 1))
                rsum = jcast('long', jcast('long', (rsum - Code01_MooFest2.arr[p1][1])))
                lsum = jcast('long', jcast('long', jadd(lsum, Code01_MooFest2.arr[p1][1])))
            ans = jcast('long', jcast('long', jadd(ans, jcast('long', (jcast('long', (jcast('long', jadd(jcast('long', (jcast('long', (jcast('long', (1 * jcast('int', jadd(jcast('int', (p1 - l)), 1)))) * Code01_MooFest2.arr[p2][1])) - lsum)), rsum)) - jcast('long', (jcast('long', (1 * jcast('int', (m - p1)))) * Code01_MooFest2.arr[p2][1])))) * Code01_MooFest2.arr[p2][0])))))
            p2 = jcast('int', (p2 + 1))
        p1 = jcast('int', l)
        p2 = jcast('int', jcast('int', jadd(m, 1)))
        i = jcast('int', l)
        while ((p1 <= m) and (p2 <= r)):
            Code01_MooFest2.clone(Code01_MooFest2.tmp[((_java_old_1 := i), (i := jcast('int', (i + (1)))), _java_old_1)[2]], (Code01_MooFest2.arr[((_java_old_2 := p1), (p1 := jcast('int', (p1 + (1)))), _java_old_2)[2]] if (Code01_MooFest2.arr[p1][1] <= Code01_MooFest2.arr[p2][1]) else Code01_MooFest2.arr[((_java_old_3 := p2), (p2 := jcast('int', (p2 + (1)))), _java_old_3)[2]]))
        while (p1 <= m):
            Code01_MooFest2.clone(Code01_MooFest2.tmp[((_java_old_4 := i), (i := jcast('int', (i + (1)))), _java_old_4)[2]], Code01_MooFest2.arr[((_java_old_5 := p1), (p1 := jcast('int', (p1 + (1)))), _java_old_5)[2]])
        while (p2 <= r):
            Code01_MooFest2.clone(Code01_MooFest2.tmp[((_java_old_6 := i), (i := jcast('int', (i + (1)))), _java_old_6)[2]], Code01_MooFest2.arr[((_java_old_7 := p2), (p2 := jcast('int', (p2 + (1)))), _java_old_7)[2]])
        i = jcast('int', l)
        while (i <= r):
            Code01_MooFest2.clone(Code01_MooFest2.arr[i], Code01_MooFest2.tmp[i])
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def cdq(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return jcast('long', 0)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        return jcast('long', jcast('long', jadd(jcast('long', jadd(Code01_MooFest2.cdq(l, mid), Code01_MooFest2.cdq(jcast('int', jadd(mid, 1)), r))), Code01_MooFest2.merge(l, mid, r))))

    @staticmethod
    def main(args):
        in_ = Code01_MooFest2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_MooFest2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_MooFest2.n):
            jset(Code01_MooFest2.arr[i], 0, jcall(in_, 'nextInt'))
            jset(Code01_MooFest2.arr[i], 1, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code01_MooFest2.arr, 1, jcast('int', jadd(Code01_MooFest2.n, 1)), (lambda a, b: (a[0] - b[0])))
        jcall(out, 'println', Code01_MooFest2.cdq(1, Code01_MooFest2.n))
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
            self.buffer = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_MooFest2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_MooFest2.MAXN = jcast('int', 50001)
Code01_MooFest2.n = jcast('int', 0)
Code01_MooFest2.arr = jarray('int', [Code01_MooFest2.MAXN, 2])
Code01_MooFest2.tmp = jarray('int', [Code01_MooFest2.MAXN, 2])

if __name__ == '__main__':
    Code01_MooFest2.main([])
