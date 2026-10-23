# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 三维偏序，Python版
# 一共有n个对象，每个对象有a、b、c三个属性，每个属性值的范围都是[1, k]
# f(i)表示，aj <= ai 且 bj <= bi 且 cj <= ci 且 j != i 的j的数量
# ans(d)表示，f(i) == d 的i的数量
# 打印所有的ans[d]，d的范围[0, n)
# 1 <= n <= 10^5
# 1 <= k <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3810
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_3DPartialOrder2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 'n': 'n', 'k': 'k', 'arr': 'arr', 'tree': 'tree', 'f': 'f', 'ans': 'ans'}
    MAXN = 0
    MAXK = 0
    n = 0
    k = 0
    # 对象的编号i、属性a、属性b、属性c
    arr = None
    # 树状数组，根据属性c的值增加词频，查询 <= 某个数的词频累加和
    tree = None
    # 每个对象的答案
    f = None
    # 题目要求的ans[d]
    ans = None
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code01_3DPartialOrder2.k):
            Code01_3DPartialOrder2.tree[i] = jcast('int', jcast('int', jadd(Code01_3DPartialOrder2.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code01_3DPartialOrder2.lowbit(i))))

    @staticmethod
    def query(i):
        i = jcast('int', i)
        ret = jcast('int', 0)
        while (i > 0):
            ret = jcast('int', jcast('int', jadd(ret, Code01_3DPartialOrder2.tree[i])))
            i = jcast('int', jcast('int', (i - Code01_3DPartialOrder2.lowbit(i))))
        return jcast('int', ret)

    @staticmethod
    def merge(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        # 利用左、右各自b属性有序
        # 不回退的找，当前右组对象包括了几个左组的对象
        p1 = 0
        p2 = 0
        p1 = jcast('int', jcast('int', (l - 1)))
        p2 = jcast('int', jcast('int', jadd(m, 1)))
        while (p2 <= r):
            while ((jcast('int', jadd(p1, 1)) <= m) and (Code01_3DPartialOrder2.arr[jcast('int', jadd(p1, 1))][2] <= Code01_3DPartialOrder2.arr[p2][2])):
                p1 = jcast('int', (p1 + 1))
                Code01_3DPartialOrder2.add(Code01_3DPartialOrder2.arr[p1][3], 1)
            ((_java_obj_1 := Code01_3DPartialOrder2.f), (_java_key_2 := Code01_3DPartialOrder2.arr[p2][0]), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), Code01_3DPartialOrder2.query(Code01_3DPartialOrder2.arr[p2][3])))))[2]
            p2 = jcast('int', (p2 + 1))
        # 清空树状数组
        i = jcast('int', l)
        while (i <= p1):
            Code01_3DPartialOrder2.add(Code01_3DPartialOrder2.arr[i][3], jcast('int', (-1)))
            i = jcast('int', (i + 1))
        # 直接根据b属性排序，无需写经典的归并过程，课上重点解释了原因
        jstatic('Arrays', 'sort', Code01_3DPartialOrder2.arr, l, jcast('int', jadd(r, 1)), (lambda a, b: (a[2] - b[2])))

    # 大顺序已经按a属性排序，cdq分治里按b属性重新排序
    @staticmethod
    def cdq(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code01_3DPartialOrder2.cdq(l, mid)
        Code01_3DPartialOrder2.cdq(jcast('int', jadd(mid, 1)), r)
        Code01_3DPartialOrder2.merge(l, mid, r)

    @staticmethod
    def prepare():
        # 根据a排序，a一样根据b排序，b一样根据c排序
        # 排序后a、b、c一样的同组内，组前的下标得不到同组后面的统计量
        # 所以把这部分的贡献，提前补偿给组前的下标，然后再跑CDQ分治
        jstatic('Arrays', 'sort', Code01_3DPartialOrder2.arr, 1, jcast('int', jadd(Code01_3DPartialOrder2.n, 1)), (lambda a, b: ((a[1] - b[1]) if (a[1] != b[1]) else ((a[2] - b[2]) if (a[2] != b[2]) else (a[3] - b[3])))))
        l = jcast('int', 1)
        r = jcast('int', 1)
        while (l <= Code01_3DPartialOrder2.n):
            while ((((jcast('int', jadd(r, 1)) <= Code01_3DPartialOrder2.n) and (Code01_3DPartialOrder2.arr[l][1] == Code01_3DPartialOrder2.arr[jcast('int', jadd(r, 1))][1])) and (Code01_3DPartialOrder2.arr[l][2] == Code01_3DPartialOrder2.arr[jcast('int', jadd(r, 1))][2])) and (Code01_3DPartialOrder2.arr[l][3] == Code01_3DPartialOrder2.arr[jcast('int', jadd(r, 1))][3])):
                r = jcast('int', (r + 1))
            i = jcast('int', l)
            while (i <= r):
                jset(Code01_3DPartialOrder2.f, Code01_3DPartialOrder2.arr[i][0], jcast('int', (r - i)))
                i = jcast('int', (i + 1))
            l = jcast('int', (r := jcast('int', (r + (1)))))

    @staticmethod
    def main(args):
        in_ = Code01_3DPartialOrder2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_3DPartialOrder2.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_3DPartialOrder2.k = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_3DPartialOrder2.n):
            jset(Code01_3DPartialOrder2.arr[i], 0, i)
            jset(Code01_3DPartialOrder2.arr[i], 1, jcall(in_, 'nextInt'))
            jset(Code01_3DPartialOrder2.arr[i], 2, jcall(in_, 'nextInt'))
            jset(Code01_3DPartialOrder2.arr[i], 3, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code01_3DPartialOrder2.prepare()
        Code01_3DPartialOrder2.cdq(1, Code01_3DPartialOrder2.n)
        i = jcast('int', 1)
        while (i <= Code01_3DPartialOrder2.n):
            ((_java_obj_3 := Code01_3DPartialOrder2.ans), (_java_key_4 := Code01_3DPartialOrder2.f[i]), (_java_old_5 := jget(_java_obj_3, _java_key_4)), jset(_java_obj_3, _java_key_4, jcast('int', (_java_old_5 + (1)))), _java_old_5)[4]
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < Code01_3DPartialOrder2.n):
            jcall(out, 'println', Code01_3DPartialOrder2.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_6 := self), (_java_key_7 := 'ptr'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))), _java_old_8)[4]])

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
            raise TypeError("No matching overload for Code01_3DPartialOrder2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_3DPartialOrder2.MAXN = jcast('int', 100001)
Code01_3DPartialOrder2.MAXK = jcast('int', 200001)
Code01_3DPartialOrder2.n = jcast('int', 0)
Code01_3DPartialOrder2.k = jcast('int', 0)
Code01_3DPartialOrder2.arr = jarray('int', [Code01_3DPartialOrder2.MAXN, 4])
Code01_3DPartialOrder2.tree = jarray('int', [Code01_3DPartialOrder2.MAXK])
Code01_3DPartialOrder2.f = jarray('int', [Code01_3DPartialOrder2.MAXN])
Code01_3DPartialOrder2.ans = jarray('int', [Code01_3DPartialOrder2.MAXN])

if __name__ == '__main__':
    Code01_3DPartialOrder2.main([])
