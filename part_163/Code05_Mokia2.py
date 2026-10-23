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

# 摩基亚，Python版
# 给定数字w，表示一个w * w的正方形区域，所有位置都在其中
# 接下来有m条操作，每种操作是如下两种类型中的一种
# 操作 1 x y v   : 坐标(x, y)位置增加了v个人
# 操作 2 a b c d : 打印左上角(a, b)、右下角(c, d)区域里的人数
# 1 <= w <= 2 * 10^6
# 1 <= m <= 2 * 10^5
# 0 <= v <= 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P4390
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Mokia2:
    __java_fields__ = {'MAXM': 'MAXM', 'MAXV': 'MAXV', 'w': 'w', 'arr': 'arr', 'cnte': 'cnte', 'cntq': 'cntq', 'tree': 'tree', 'ans': 'ans'}
    MAXM = 0
    MAXV = 0
    w = 0
    # op == 1表示增加事件，x、y、人数v
    # op == 2表示查询事件，x、y、效果v、查询编号q
    arr = None
    cnte = 0
    cntq = 0
    # 树状数组
    tree = None
    ans = None
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code05_Mokia2.w):
            Code05_Mokia2.tree[i] = jcast('int', jcast('int', jadd(Code05_Mokia2.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code05_Mokia2.lowbit(i))))

    @staticmethod
    def query(i):
        i = jcast('int', i)
        ret = jcast('int', 0)
        while (i > 0):
            ret = jcast('int', jcast('int', jadd(ret, Code05_Mokia2.tree[i])))
            i = jcast('int', jcast('int', (i - Code05_Mokia2.lowbit(i))))
        return jcast('int', ret)

    @staticmethod
    def addPeople(x, y, v):
        x = jcast('int', x)
        y = jcast('int', y)
        v = jcast('int', v)
        jset(Code05_Mokia2.arr[((_java_obj_1 := Code05_Mokia2), (_java_key_2 := 'cnte'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]], 0, 1)
        jset(Code05_Mokia2.arr[Code05_Mokia2.cnte], 1, x)
        jset(Code05_Mokia2.arr[Code05_Mokia2.cnte], 2, y)
        jset(Code05_Mokia2.arr[Code05_Mokia2.cnte], 3, v)

    @staticmethod
    def addQuery(x, y, v, q):
        x = jcast('int', x)
        y = jcast('int', y)
        v = jcast('int', v)
        q = jcast('int', q)
        jset(Code05_Mokia2.arr[((_java_obj_4 := Code05_Mokia2), (_java_key_5 := 'cnte'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]], 0, 2)
        jset(Code05_Mokia2.arr[Code05_Mokia2.cnte], 1, x)
        jset(Code05_Mokia2.arr[Code05_Mokia2.cnte], 2, y)
        jset(Code05_Mokia2.arr[Code05_Mokia2.cnte], 3, v)
        jset(Code05_Mokia2.arr[Code05_Mokia2.cnte], 4, q)

    @staticmethod
    def merge(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        p1 = 0
        p2 = 0
        p1 = jcast('int', jcast('int', (l - 1)))
        p2 = jcast('int', jcast('int', jadd(m, 1)))
        while (p2 <= r):
            while ((jcast('int', jadd(p1, 1)) <= m) and (Code05_Mokia2.arr[jcast('int', jadd(p1, 1))][1] <= Code05_Mokia2.arr[p2][1])):
                p1 = jcast('int', (p1 + 1))
                if (Code05_Mokia2.arr[p1][0] == 1):
                    Code05_Mokia2.add(Code05_Mokia2.arr[p1][2], Code05_Mokia2.arr[p1][3])
            if (Code05_Mokia2.arr[p2][0] == 2):
                ((_java_obj_7 := Code05_Mokia2.ans), (_java_key_8 := Code05_Mokia2.arr[p2][4]), jset(_java_obj_7, _java_key_8, jcast('int', jadd(jget(_java_obj_7, _java_key_8), jcast('int', (Code05_Mokia2.arr[p2][3] * Code05_Mokia2.query(Code05_Mokia2.arr[p2][2])))))))[2]
            p2 = jcast('int', (p2 + 1))
        i = jcast('int', l)
        while (i <= p1):
            if (Code05_Mokia2.arr[i][0] == 1):
                Code05_Mokia2.add(Code05_Mokia2.arr[i][2], jcast('int', (-Code05_Mokia2.arr[i][3])))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_Mokia2.arr, l, jcast('int', jadd(r, 1)), (lambda a, b: (a[1] - b[1])))

    @staticmethod
    def cdq(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code05_Mokia2.cdq(l, mid)
        Code05_Mokia2.cdq(jcast('int', jadd(mid, 1)), r)
        Code05_Mokia2.merge(l, mid, r)

    @staticmethod
    def main(args):
        in_ = Code05_Mokia2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextInt')
        Code05_Mokia2.w = jcast('int', jcast('int', jadd(jcall(in_, 'nextInt'), 1)))
        op = 0
        x = 0
        y = 0
        v = 0
        a = 0
        b = 0
        c = 0
        d = 0
        op = jcast('int', jcall(in_, 'nextInt'))
        while (op != 3):
            if (op == 1):
                x = jcast('int', jcast('int', jadd(jcall(in_, 'nextInt'), 1)))
                y = jcast('int', jcast('int', jadd(jcall(in_, 'nextInt'), 1)))
                v = jcast('int', jcall(in_, 'nextInt'))
                Code05_Mokia2.addPeople(x, y, v)
            else:
                a = jcast('int', jcast('int', jadd(jcall(in_, 'nextInt'), 1)))
                b = jcast('int', jcast('int', jadd(jcall(in_, 'nextInt'), 1)))
                c = jcast('int', jcast('int', jadd(jcall(in_, 'nextInt'), 1)))
                d = jcast('int', jcast('int', jadd(jcall(in_, 'nextInt'), 1)))
                Code05_Mokia2.addQuery(c, d, 1, ((_java_obj_9 := Code05_Mokia2), (_java_key_10 := 'cntq'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))))[3])
                Code05_Mokia2.addQuery(jcast('int', (a - 1)), jcast('int', (b - 1)), 1, Code05_Mokia2.cntq)
                Code05_Mokia2.addQuery(jcast('int', (a - 1)), d, jcast('int', (-1)), Code05_Mokia2.cntq)
                Code05_Mokia2.addQuery(c, jcast('int', (b - 1)), jcast('int', (-1)), Code05_Mokia2.cntq)
            op = jcast('int', jcall(in_, 'nextInt'))
        Code05_Mokia2.cdq(1, Code05_Mokia2.cnte)
        i = jcast('int', 1)
        while (i <= Code05_Mokia2.cntq):
            jcall(out, 'println', Code05_Mokia2.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_12 := self), (_java_key_13 := 'ptr'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))), _java_old_14)[4]])

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
            raise TypeError("No matching overload for Code05_Mokia2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Mokia2.MAXM = jcast('int', 200001)
Code05_Mokia2.MAXV = jcast('int', 2000002)
Code05_Mokia2.w = jcast('int', 0)
Code05_Mokia2.arr = jarray('int', [Code05_Mokia2.MAXM, 5])
Code05_Mokia2.cnte = jcast('int', 0)
Code05_Mokia2.cntq = jcast('int', 0)
Code05_Mokia2.tree = jarray('int', [Code05_Mokia2.MAXV])
Code05_Mokia2.ans = jarray('int', [Code05_Mokia2.MAXM])

if __name__ == '__main__':
    Code05_Mokia2.main([])
