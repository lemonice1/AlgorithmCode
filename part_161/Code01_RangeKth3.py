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

# 区间内第k小，第一种写法，Python版
# 给定一个长度为n的数组，接下来有m条查询，格式如下
# 查询 l r k : 打印[l..r]范围内第k小的值
# 1 <= n、m <= 2 * 10^5
# 1 <= 数组中的数字 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P3834
# 本题是讲解157，可持久化线段树模版题，现在作为整体二分的模版题
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_RangeKth3:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'arr': 'arr', 'qid': 'qid', 'l': 'l', 'r': 'r', 'k': 'k', 'tree': 'tree', 'lset': 'lset', 'rset': 'rset', 'ans': 'ans'}
    MAXN = 0
    n = 0
    m = 0
    # 位置i，数值v
    arr = None
    # 查询
    qid = None
    l = None
    r = None
    k = None
    # 树状数组
    tree = None
    # 整体二分
    lset = None
    rset = None
    # 查询的答案
    ans = None
    # 树状数组中的lowbit
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    # 树状数组中增加i位置的词频
    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code01_RangeKth3.n):
            Code01_RangeKth3.tree[i] = jcast('int', jcast('int', jadd(Code01_RangeKth3.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code01_RangeKth3.lowbit(i))))

    # 树状数组中查询[1~i]范围的词频累加和
    @staticmethod
    def sum(i):
        i = jcast('int', i)
        ret = jcast('int', 0)
        while (i > 0):
            ret = jcast('int', jcast('int', jadd(ret, Code01_RangeKth3.tree[i])))
            i = jcast('int', jcast('int', (i - Code01_RangeKth3.lowbit(i))))
        return jcast('int', ret)

    # 树状数组中查询[l~r]范围的词频累加和
    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        return jcast('int', jcast('int', (Code01_RangeKth3.sum(r) - Code01_RangeKth3.sum(jcast('int', (l - 1))))))

    # 整体二分的第一种写法
    # 问题范围[ql..qr]，答案范围[vl..vr]，答案范围的每个下标都是数字的排名
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
                jset(Code01_RangeKth3.ans, Code01_RangeKth3.qid[i], Code01_RangeKth3.arr[vl][1])
                i = jcast('int', (i + 1))
        else:
            # 修改数据状况
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(vl, vr)), 2)))
            i = jcast('int', vl)
            while (i <= mid):
                Code01_RangeKth3.add(Code01_RangeKth3.arr[i][0], 1)
                i = jcast('int', (i + 1))
            # 检查每个问题并划分左右
            lsiz = jcast('int', 0)
            rsiz = jcast('int', 0)
            i = jcast('int', ql)
            while (i <= qr):
                id = jcast('int', Code01_RangeKth3.qid[i])
                satisfy = jcast('int', Code01_RangeKth3.query(Code01_RangeKth3.l[id], Code01_RangeKth3.r[id]))
                if (satisfy >= Code01_RangeKth3.k[id]):
                    jset(Code01_RangeKth3.lset, (lsiz := jcast('int', (lsiz + (1)))), id)
                else:
                    Code01_RangeKth3.k[id] = jcast('int', jcast('int', (Code01_RangeKth3.k[id] - satisfy)))
                    jset(Code01_RangeKth3.rset, (rsiz := jcast('int', (rsiz + (1)))), id)
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= lsiz):
                Code01_RangeKth3.qid[jcast('int', (jcast('int', jadd(ql, i)) - 1))] = jcast('int', Code01_RangeKth3.lset[i])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= rsiz):
                Code01_RangeKth3.qid[jcast('int', (jcast('int', jadd(jcast('int', jadd(ql, lsiz)), i)) - 1))] = jcast('int', Code01_RangeKth3.rset[i])
                i = jcast('int', (i + 1))
            # 撤回数据状况
            i = jcast('int', vl)
            while (i <= mid):
                Code01_RangeKth3.add(Code01_RangeKth3.arr[i][0], jcast('int', (-1)))
                i = jcast('int', (i + 1))
            # 左右两侧各自递归
            Code01_RangeKth3.compute(ql, jcast('int', (jcast('int', jadd(ql, lsiz)) - 1)), vl, mid)
            Code01_RangeKth3.compute(jcast('int', jadd(ql, lsiz)), qr, jcast('int', jadd(mid, 1)), vr)

    @staticmethod
    def main(args):
        in_ = Code01_RangeKth3.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_RangeKth3.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_RangeKth3.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_RangeKth3.n):
            jset(Code01_RangeKth3.arr[i], 0, i)
            jset(Code01_RangeKth3.arr[i], 1, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_RangeKth3.m):
            Code01_RangeKth3.qid[i] = jcast('int', i)
            jset(Code01_RangeKth3.l, i, jcall(in_, 'nextInt'))
            jset(Code01_RangeKth3.r, i, jcall(in_, 'nextInt'))
            jset(Code01_RangeKth3.k, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code01_RangeKth3.arr, 1, jcast('int', jadd(Code01_RangeKth3.n, 1)), (lambda a, b: (a[1] - b[1])))
        Code01_RangeKth3.compute(1, Code01_RangeKth3.m, 1, Code01_RangeKth3.n)
        i = jcast('int', 1)
        while (i <= Code01_RangeKth3.m):
            jcall(out, 'println', Code01_RangeKth3.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_1 := self), (_java_key_2 := 'ptr'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]])

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
            raise TypeError("No matching overload for Code01_RangeKth3.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_RangeKth3.MAXN = jcast('int', 200001)
Code01_RangeKth3.n = jcast('int', 0)
Code01_RangeKth3.m = jcast('int', 0)
Code01_RangeKth3.arr = jarray('int', [Code01_RangeKth3.MAXN, 2])
Code01_RangeKth3.qid = jarray('int', [Code01_RangeKth3.MAXN])
Code01_RangeKth3.l = jarray('int', [Code01_RangeKth3.MAXN])
Code01_RangeKth3.r = jarray('int', [Code01_RangeKth3.MAXN])
Code01_RangeKth3.k = jarray('int', [Code01_RangeKth3.MAXN])
Code01_RangeKth3.tree = jarray('int', [Code01_RangeKth3.MAXN])
Code01_RangeKth3.lset = jarray('int', [Code01_RangeKth3.MAXN])
Code01_RangeKth3.rset = jarray('int', [Code01_RangeKth3.MAXN])
Code01_RangeKth3.ans = jarray('int', [Code01_RangeKth3.MAXN])

if __name__ == '__main__':
    Code01_RangeKth3.main([])
