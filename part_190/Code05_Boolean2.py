# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 布尔，Python版
# 一共n个变量，取值为0或1，一共m条限制，格式 u x v y，含义如下
# 如果u的取值为x，则v的取值为y，同时如果v的取值为y，则u的取值为x
# 限制的编号范围1~m，限制区间[a, b]如果满足如下条件，就认为是合法的
# 区间[a, b]内的所有限制，存在一种变量赋值方案，能让它们全部成立
# 一共有q条查询，格式 l r，含义如下
# 整个限制区间[l, r]，最少划分成多少段连续区间，使得每个连续区间都合法
# 打印划分的连续区间数量，如果怎么划分都做不到上述要求，打印-1
# 1 <= n <= 10^5
# 1 <= m <= 6 * 10^5
# 1 <= q <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P7843
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Boolean2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXQ': 'MAXQ', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'q': 'q', 'error': 'error', 'u': 'u', 'v': 'v', 'fa': 'fa', 'siz': 'siz', 'rollback': 'rollback', 'opsize': 'opsize', 'first': 'first', 'st': 'st'}
    MAXN = 0
    MAXM = 0
    MAXQ = 0
    MAXP = 0
    n = 0
    m = 0
    q = 0
    # 错误计数
    error = None
    # 决定编号
    u = None
    v = None
    # 可撤销并查集
    fa = None
    siz = None
    rollback = None
    opsize = 0
    # first[i] = 从i位置开始，向右不停添加限制，首次违规的位置
    first = None
    # st[i][p] = 从i位置开始，允许拆成2的p次个连续区间，每个都合法，往右能到什么位置
    st = None
    @staticmethod
    def find(i):
        i = jcast('int', i)
        while (i != Code05_Boolean2.fa[i]):
            i = jcast('int', Code05_Boolean2.fa[i])
        return jcast('int', i)

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code05_Boolean2.find(x))
        fy = jcast('int', Code05_Boolean2.find(y))
        if (fx != fy):
            if (Code05_Boolean2.siz[fx] < Code05_Boolean2.siz[fy]):
                tmp = jcast('int', fx)
                fx = jcast('int', fy)
                fy = jcast('int', tmp)
            Code05_Boolean2.fa[fy] = jcast('int', fx)
            Code05_Boolean2.siz[fx] = jcast('int', jcast('int', jadd(Code05_Boolean2.siz[fx], Code05_Boolean2.siz[fy])))
            jset(Code05_Boolean2.rollback[((_java_obj_1 := Code05_Boolean2), (_java_key_2 := 'opsize'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]], 0, fx)
            jset(Code05_Boolean2.rollback[Code05_Boolean2.opsize], 1, fy)

    @staticmethod
    def undo(oldsiz):
        oldsiz = jcast('int', oldsiz)
        while (Code05_Boolean2.opsize > oldsiz):
            fx = jcast('int', Code05_Boolean2.rollback[Code05_Boolean2.opsize][0])
            fy = jcast('int', Code05_Boolean2.rollback[((_java_obj_4 := Code05_Boolean2), (_java_key_5 := 'opsize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))), _java_old_6)[4]][1])
            Code05_Boolean2.fa[fy] = jcast('int', fy)
            Code05_Boolean2.siz[fx] = jcast('int', jcast('int', (Code05_Boolean2.siz[fx] - Code05_Boolean2.siz[fy])))

    @staticmethod
    def other(x):
        x = jcast('int', x)
        return jcast('int', (jcast('int', jadd(x, Code05_Boolean2.n)) if (x <= Code05_Boolean2.n) else jcast('int', (x - Code05_Boolean2.n))))

    @staticmethod
    def conflict(x):
        x = jcast('int', x)
        return jcast('boolean', (Code05_Boolean2.find(x) == Code05_Boolean2.find(Code05_Boolean2.other(x))))

    # 整体二分，计算每个位置i的first[i]信息
    @staticmethod
    def compute(ql, qr, vl, vr):
        ql = jcast('int', ql)
        qr = jcast('int', qr)
        vl = jcast('int', vl)
        vr = jcast('int', vr)
        if (ql > qr):
            return
        if (vl == vr):
            i = jcast('int', ql)
            while (i <= qr):
                Code05_Boolean2.first[i] = jcast('int', vl)
                i = jcast('int', (i + 1))
            return
        mid = jcast('int', jcast('int', (jcast('int', jadd(vl, vr)) >> (1 & 31))))
        backup1 = jcast('int', Code05_Boolean2.opsize)
        bad = jcast('boolean', False)
        i = jcast('int', jstatic('Math', 'max', jcast('int', jadd(qr, 1)), vl))
        while (i <= mid):
            try:
                Code05_Boolean2.union(Code05_Boolean2.u[i], Code05_Boolean2.v[i])
                Code05_Boolean2.union(Code05_Boolean2.other(Code05_Boolean2.u[i]), Code05_Boolean2.other(Code05_Boolean2.v[i]))
                if Code05_Boolean2.conflict(Code05_Boolean2.u[i]):
                    bad = jcast('boolean', True)
                    raise JBreak(None)
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if bad:
            Code05_Boolean2.undo(backup1)
            Code05_Boolean2.compute(ql, qr, vl, mid)
        else:
            backup2 = jcast('int', Code05_Boolean2.opsize)
            split = jcast('int', jstatic('Math', 'min', qr, mid))
            while (split >= ql):
                try:
                    Code05_Boolean2.union(Code05_Boolean2.u[split], Code05_Boolean2.v[split])
                    Code05_Boolean2.union(Code05_Boolean2.other(Code05_Boolean2.u[split]), Code05_Boolean2.other(Code05_Boolean2.v[split]))
                    if Code05_Boolean2.conflict(Code05_Boolean2.u[split]):
                        raise JBreak(None)
                except JContinue as _java_control_8:
                    if _java_control_8.label not in (None,):
                        raise
                except JBreak as _java_control_8:
                    if _java_control_8.label not in (None,):
                        raise
                    break
                split = jcast('int', (split - 1))
            Code05_Boolean2.undo(backup2)
            Code05_Boolean2.compute(jcast('int', jadd(split, 1)), qr, jcast('int', jadd(mid, 1)), vr)
            Code05_Boolean2.undo(backup1)
            i = jcast('int', jcast('int', jadd(split, 1)))
            while ((i <= qr) and (i < vl)):
                Code05_Boolean2.union(Code05_Boolean2.u[i], Code05_Boolean2.v[i])
                Code05_Boolean2.union(Code05_Boolean2.other(Code05_Boolean2.u[i]), Code05_Boolean2.other(Code05_Boolean2.v[i]))
                i = jcast('int', (i + 1))
            Code05_Boolean2.compute(ql, split, vl, mid)

    @staticmethod
    def buildst():
        Code05_Boolean2.opsize = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= jcast('int', (Code05_Boolean2.n << (1 & 31)))):
            Code05_Boolean2.fa[i] = jcast('int', i)
            Code05_Boolean2.siz[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        Code05_Boolean2.compute(1, Code05_Boolean2.m, 1, jcast('int', jadd(Code05_Boolean2.m, 1)))
        p = jcast('int', 0)
        while (p < Code05_Boolean2.MAXP):
            jset(Code05_Boolean2.st[jcast('int', jadd(Code05_Boolean2.m, 1))], p, jcast('int', jadd(Code05_Boolean2.m, 1)))
            p = jcast('int', (p + 1))
        i = jcast('int', Code05_Boolean2.m)
        while (i >= 1):
            jset(Code05_Boolean2.st[i], 0, Code05_Boolean2.first[i])
            p = jcast('int', 1)
            while (p < Code05_Boolean2.MAXP):
                jset(Code05_Boolean2.st[i], p, Code05_Boolean2.st[Code05_Boolean2.st[i][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                p = jcast('int', (p + 1))
            i = jcast('int', (i - 1))

    @staticmethod
    def main(args):
        in_ = Code05_Boolean2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_Boolean2.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_Boolean2.m = jcast('int', jcall(in_, 'nextInt'))
        Code05_Boolean2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= Code05_Boolean2.m):
            jset(Code05_Boolean2.u, i, jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            jset(Code05_Boolean2.v, i, jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            Code05_Boolean2.error[i] = jcast('int', (1 if ((Code05_Boolean2.u[i] == Code05_Boolean2.v[i]) and (x != y)) else 0))
            Code05_Boolean2.u[i] = jcast('int', (Code05_Boolean2.u[i] if (x == 0) else jcast('int', jadd(Code05_Boolean2.u[i], Code05_Boolean2.n))))
            Code05_Boolean2.v[i] = jcast('int', (Code05_Boolean2.v[i] if (y == 0) else jcast('int', jadd(Code05_Boolean2.v[i], Code05_Boolean2.n))))
            i = jcast('int', (i + 1))
        Code05_Boolean2.buildst()
        i = jcast('int', 1)
        while (i <= Code05_Boolean2.m):
            Code05_Boolean2.error[i] = jcast('int', jcast('int', jadd(Code05_Boolean2.error[i], Code05_Boolean2.error[jcast('int', (i - 1))])))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        l = 0
        r = 0
        while (i <= Code05_Boolean2.q):
            l = jcast('int', jcall(in_, 'nextInt'))
            r = jcast('int', jcall(in_, 'nextInt'))
            if (jcast('int', (Code05_Boolean2.error[r] - Code05_Boolean2.error[jcast('int', (l - 1))])) > 0):
                jcall(out, 'println', jcast('int', (-1)))
            else:
                ans = jcast('int', 0)
                p = jcast('int', jcast('int', (Code05_Boolean2.MAXP - 1)))
                while (p >= 0):
                    if (Code05_Boolean2.st[l][p] <= r):
                        l = jcast('int', Code05_Boolean2.st[l][p])
                        ans = jcast('int', jcast('int', jadd(ans, jcast('int', (1 << (p & 31))))))
                    p = jcast('int', (p - 1))
                ans = jcast('int', (ans + 1))
                jcall(out, 'println', ans)
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
            return jcast('int', self.buffer[((_java_obj_9 := self), (_java_key_10 := 'ptr'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))), _java_old_11)[4]])

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
            raise TypeError("No matching overload for Code05_Boolean2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Boolean2.MAXN = jcast('int', 200001)
Code05_Boolean2.MAXM = jcast('int', 600001)
Code05_Boolean2.MAXQ = jcast('int', 1000001)
Code05_Boolean2.MAXP = jcast('int', 20)
Code05_Boolean2.n = jcast('int', 0)
Code05_Boolean2.m = jcast('int', 0)
Code05_Boolean2.q = jcast('int', 0)
Code05_Boolean2.error = jarray('int', [Code05_Boolean2.MAXM])
Code05_Boolean2.u = jarray('int', [Code05_Boolean2.MAXM])
Code05_Boolean2.v = jarray('int', [Code05_Boolean2.MAXM])
Code05_Boolean2.fa = jarray('int', [Code05_Boolean2.MAXN])
Code05_Boolean2.siz = jarray('int', [Code05_Boolean2.MAXN])
Code05_Boolean2.rollback = jarray('int', [Code05_Boolean2.MAXN, 2])
Code05_Boolean2.opsize = jcast('int', 0)
Code05_Boolean2.first = jarray('int', [Code05_Boolean2.MAXM])
Code05_Boolean2.st = jarray('int', [jcast('int', jadd(Code05_Boolean2.MAXM, 1)), Code05_Boolean2.MAXP])

if __name__ == '__main__':
    Code05_Boolean2.main([])
