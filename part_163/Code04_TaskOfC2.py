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

# 老C的任务，Python版
# 有n个基站，每个基站给定x、y、v，表示基站在(x, y)位置，功率为v
# 接下来有m条查询，每条查询格式如下
# 查询 a b c d : 打印左上角(a, b)、右下角(c, d)的区域里基站的功率和
# 1 <= n、m <= 10^5
# 其余数值都在int类型的范围
# 测试链接 : https://www.luogu.com.cn/problem/P3755
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_TaskOfC2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'arr': 'arr', 'cnt': 'cnt', 'tmp': 'tmp', 'ans': 'ans'}
    MAXN = 0
    n = 0
    m = 0
    # op == 1代表基站，x、y、功率v
    # op == 2代表查询，x、y、效果v、查询编号q
    arr = None
    cnt = 0
    # 归并排序需要
    tmp = None
    # 问题的答案
    ans = None
    @staticmethod
    def clone(a, b):
        a[0] = jcast('int', b[0])
        a[1] = jcast('int', b[1])
        a[2] = jcast('int', b[2])
        a[3] = jcast('int', b[3])
        a[4] = jcast('int', b[4])

    @staticmethod
    def addStation(x, y, v):
        x = jcast('int', x)
        y = jcast('int', y)
        v = jcast('int', v)
        jset(Code04_TaskOfC2.arr[((_java_obj_1 := Code04_TaskOfC2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]], 0, 1)
        jset(Code04_TaskOfC2.arr[Code04_TaskOfC2.cnt], 1, x)
        jset(Code04_TaskOfC2.arr[Code04_TaskOfC2.cnt], 2, y)
        jset(Code04_TaskOfC2.arr[Code04_TaskOfC2.cnt], 3, v)

    @staticmethod
    def addQuery(x, y, v, q):
        x = jcast('int', x)
        y = jcast('int', y)
        v = jcast('int', v)
        q = jcast('int', q)
        jset(Code04_TaskOfC2.arr[((_java_obj_4 := Code04_TaskOfC2), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]], 0, 2)
        jset(Code04_TaskOfC2.arr[Code04_TaskOfC2.cnt], 1, x)
        jset(Code04_TaskOfC2.arr[Code04_TaskOfC2.cnt], 2, y)
        jset(Code04_TaskOfC2.arr[Code04_TaskOfC2.cnt], 3, v)
        jset(Code04_TaskOfC2.arr[Code04_TaskOfC2.cnt], 4, q)

    @staticmethod
    def merge(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        p1 = 0
        p2 = 0
        sum = jcast('long', 0)
        p1 = jcast('int', jcast('int', (l - 1)))
        p2 = jcast('int', jcast('int', jadd(m, 1)))
        while (p2 <= r):
            while ((jcast('int', jadd(p1, 1)) <= m) and (Code04_TaskOfC2.arr[jcast('int', jadd(p1, 1))][2] <= Code04_TaskOfC2.arr[p2][2])):
                p1 = jcast('int', (p1 + 1))
                if (Code04_TaskOfC2.arr[p1][0] == 1):
                    sum = jcast('long', jcast('long', jadd(sum, Code04_TaskOfC2.arr[p1][3])))
            if (Code04_TaskOfC2.arr[p2][0] == 2):
                ((_java_obj_7 := Code04_TaskOfC2.ans), (_java_key_8 := Code04_TaskOfC2.arr[p2][4]), jset(_java_obj_7, _java_key_8, jcast('long', jadd(jget(_java_obj_7, _java_key_8), jcast('long', (sum * Code04_TaskOfC2.arr[p2][3]))))))[2]
            p2 = jcast('int', (p2 + 1))
        # 下面是经典归并的过程，为啥不直接排序了？
        # 因为没有用到高级数据结构，复杂度可以做到O(n * log n)
        # 那么就维持最好的复杂度，不用排序
        p1 = jcast('int', l)
        p2 = jcast('int', jcast('int', jadd(m, 1)))
        i = jcast('int', l)
        while ((p1 <= m) and (p2 <= r)):
            Code04_TaskOfC2.clone(Code04_TaskOfC2.tmp[((_java_old_9 := i), (i := jcast('int', (i + (1)))), _java_old_9)[2]], (Code04_TaskOfC2.arr[((_java_old_10 := p1), (p1 := jcast('int', (p1 + (1)))), _java_old_10)[2]] if (Code04_TaskOfC2.arr[p1][2] <= Code04_TaskOfC2.arr[p2][2]) else Code04_TaskOfC2.arr[((_java_old_11 := p2), (p2 := jcast('int', (p2 + (1)))), _java_old_11)[2]]))
        while (p1 <= m):
            Code04_TaskOfC2.clone(Code04_TaskOfC2.tmp[((_java_old_12 := i), (i := jcast('int', (i + (1)))), _java_old_12)[2]], Code04_TaskOfC2.arr[((_java_old_13 := p1), (p1 := jcast('int', (p1 + (1)))), _java_old_13)[2]])
        while (p2 <= r):
            Code04_TaskOfC2.clone(Code04_TaskOfC2.tmp[((_java_old_14 := i), (i := jcast('int', (i + (1)))), _java_old_14)[2]], Code04_TaskOfC2.arr[((_java_old_15 := p2), (p2 := jcast('int', (p2 + (1)))), _java_old_15)[2]])
        i = jcast('int', l)
        while (i <= r):
            Code04_TaskOfC2.clone(Code04_TaskOfC2.arr[i], Code04_TaskOfC2.tmp[i])
            i = jcast('int', (i + 1))

    @staticmethod
    def cdq(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code04_TaskOfC2.cdq(l, mid)
        Code04_TaskOfC2.cdq(jcast('int', jadd(mid, 1)), r)
        Code04_TaskOfC2.merge(l, mid, r)

    @staticmethod
    def main(args):
        in_ = Code04_TaskOfC2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_TaskOfC2.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_TaskOfC2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        y = 0
        v = 0
        while (i <= Code04_TaskOfC2.n):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code04_TaskOfC2.addStation(x, y, v)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        a = 0
        b = 0
        c = 0
        d = 0
        while (i <= Code04_TaskOfC2.m):
            a = jcast('int', jcall(in_, 'nextInt'))
            b = jcast('int', jcall(in_, 'nextInt'))
            c = jcast('int', jcall(in_, 'nextInt'))
            d = jcast('int', jcall(in_, 'nextInt'))
            Code04_TaskOfC2.addQuery(c, d, 1, i)
            Code04_TaskOfC2.addQuery(jcast('int', (a - 1)), jcast('int', (b - 1)), 1, i)
            Code04_TaskOfC2.addQuery(jcast('int', (a - 1)), d, jcast('int', (-1)), i)
            Code04_TaskOfC2.addQuery(c, jcast('int', (b - 1)), jcast('int', (-1)), i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_TaskOfC2.arr, 1, jcast('int', jadd(Code04_TaskOfC2.cnt, 1)), (lambda a, b: ((a[1] - b[1]) if (a[1] != b[1]) else (a[0] - b[0]))))
        Code04_TaskOfC2.cdq(1, Code04_TaskOfC2.cnt)
        i = jcast('int', 1)
        while (i <= Code04_TaskOfC2.m):
            jcall(out, 'println', Code04_TaskOfC2.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_16 := self), (_java_key_17 := 'ptr'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))), _java_old_18)[4]])

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
            raise TypeError("No matching overload for Code04_TaskOfC2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_TaskOfC2.MAXN = jcast('int', 500001)
Code04_TaskOfC2.n = jcast('int', 0)
Code04_TaskOfC2.m = jcast('int', 0)
Code04_TaskOfC2.arr = jarray('int', [Code04_TaskOfC2.MAXN, 5])
Code04_TaskOfC2.cnt = jcast('int', 0)
Code04_TaskOfC2.tmp = jarray('int', [Code04_TaskOfC2.MAXN, 5])
Code04_TaskOfC2.ans = jarray('long', [Code04_TaskOfC2.MAXN])

if __name__ == '__main__':
    Code04_TaskOfC2.main([])
