# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 矩阵内第k小，第一种写法，Python版
# 给定一个n * n的矩阵，接下来有q条查询，格式如下
# 查询 a b c d k : 左上角(a, b)，右下角(c, d)，打印该区域中第k小的数
# 1 <= n <= 500
# 1 <= q <= 6 * 10^4
# 0 <= 矩阵中的数字 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P1527
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_MatrixKth1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXQ': 'MAXQ', 'n': 'n', 'q': 'q', 'xyv': 'xyv', 'cntv': 'cntv', 'qid': 'qid', 'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'k': 'k', 'tree': 'tree', 'lset': 'lset', 'rset': 'rset', 'ans': 'ans'}
    MAXN = 0
    MAXQ = 0
    n = 0
    q = 0
    # 矩阵中的每个数字，所在行x、所在列y、数值v
    xyv = None
    # 矩阵中一共有多少个数字，cntv就是矩阵的规模
    cntv = 0
    # 查询任务的编号
    qid = None
    # 查询范围的左上角坐标
    a = None
    b = None
    # 查询范围的右下角坐标
    c = None
    d = None
    # 查询矩阵内第k小
    k = None
    # 二维树状数组
    tree = None
    # 整体二分
    lset = None
    rset = None
    # 每条查询的答案
    ans = None
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    # 二维空间中，(x,y)位置的词频加v
    @staticmethod
    def add(x, y, v):
        x = jcast('int', x)
        y = jcast('int', y)
        v = jcast('int', v)
        i = jcast('int', x)
        while (i <= Code02_MatrixKth1.n):
            j = jcast('int', y)
            while (j <= Code02_MatrixKth1.n):
                ((_java_obj_1 := Code02_MatrixKth1.tree[i]), (_java_key_2 := j), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), v))))[2]
                j = jcast('int', jcast('int', jadd(j, Code02_MatrixKth1.lowbit(j))))
            i = jcast('int', jcast('int', jadd(i, Code02_MatrixKth1.lowbit(i))))

    # 二维空间中，左上角(1,1)到右下角(x,y)范围上的词频累加和
    @staticmethod
    def sum(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        ret = jcast('int', 0)
        i = jcast('int', x)
        while (i > 0):
            j = jcast('int', y)
            while (j > 0):
                ret = jcast('int', jcast('int', jadd(ret, Code02_MatrixKth1.tree[i][j])))
                j = jcast('int', jcast('int', (j - Code02_MatrixKth1.lowbit(j))))
            i = jcast('int', jcast('int', (i - Code02_MatrixKth1.lowbit(i))))
        return jcast('int', ret)

    # 二维空间中，左上角(a,b)到右下角(c,d)范围上的词频累加和
    @staticmethod
    def query(a, b, c, d):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        d = jcast('int', d)
        return jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (Code02_MatrixKth1.sum(c, d) - Code02_MatrixKth1.sum(jcast('int', (a - 1)), d))) - Code02_MatrixKth1.sum(c, jcast('int', (b - 1))))), Code02_MatrixKth1.sum(jcast('int', (a - 1)), jcast('int', (b - 1))))))

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
                jset(Code02_MatrixKth1.ans, Code02_MatrixKth1.qid[i], Code02_MatrixKth1.xyv[vl][2])
                i = jcast('int', (i + 1))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(vl, vr)) >> (1 & 31))))
            i = jcast('int', vl)
            while (i <= mid):
                Code02_MatrixKth1.add(Code02_MatrixKth1.xyv[i][0], Code02_MatrixKth1.xyv[i][1], 1)
                i = jcast('int', (i + 1))
            lsiz = jcast('int', 0)
            rsiz = jcast('int', 0)
            i = jcast('int', ql)
            while (i <= qr):
                id = jcast('int', Code02_MatrixKth1.qid[i])
                satisfy = jcast('int', Code02_MatrixKth1.query(Code02_MatrixKth1.a[id], Code02_MatrixKth1.b[id], Code02_MatrixKth1.c[id], Code02_MatrixKth1.d[id]))
                if (satisfy >= Code02_MatrixKth1.k[id]):
                    jset(Code02_MatrixKth1.lset, (lsiz := jcast('int', (lsiz + (1)))), id)
                else:
                    Code02_MatrixKth1.k[id] = jcast('int', jcast('int', (Code02_MatrixKth1.k[id] - satisfy)))
                    jset(Code02_MatrixKth1.rset, (rsiz := jcast('int', (rsiz + (1)))), id)
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= lsiz):
                Code02_MatrixKth1.qid[jcast('int', (jcast('int', jadd(ql, i)) - 1))] = jcast('int', Code02_MatrixKth1.lset[i])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= rsiz):
                Code02_MatrixKth1.qid[jcast('int', (jcast('int', jadd(jcast('int', jadd(ql, lsiz)), i)) - 1))] = jcast('int', Code02_MatrixKth1.rset[i])
                i = jcast('int', (i + 1))
            i = jcast('int', vl)
            while (i <= mid):
                Code02_MatrixKth1.add(Code02_MatrixKth1.xyv[i][0], Code02_MatrixKth1.xyv[i][1], jcast('int', (-1)))
                i = jcast('int', (i + 1))
            Code02_MatrixKth1.compute(ql, jcast('int', (jcast('int', jadd(ql, lsiz)) - 1)), vl, mid)
            Code02_MatrixKth1.compute(jcast('int', jadd(ql, lsiz)), qr, jcast('int', jadd(mid, 1)), vr)

    @staticmethod
    def main(args):
        in_ = Code02_MatrixKth1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_MatrixKth1.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_MatrixKth1.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_MatrixKth1.n):
            j = jcast('int', 1)
            while (j <= Code02_MatrixKth1.n):
                jset(Code02_MatrixKth1.xyv[((_java_obj_3 := Code02_MatrixKth1), (_java_key_4 := 'cntv'), (_java_old_5 := jget(_java_obj_3, _java_key_4)), jset(_java_obj_3, _java_key_4, jcast('int', (_java_old_5 + (1)))))[3]], 0, i)
                jset(Code02_MatrixKth1.xyv[Code02_MatrixKth1.cntv], 1, j)
                jset(Code02_MatrixKth1.xyv[Code02_MatrixKth1.cntv], 2, jcall(in_, 'nextInt'))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_MatrixKth1.q):
            Code02_MatrixKth1.qid[i] = jcast('int', i)
            jset(Code02_MatrixKth1.a, i, jcall(in_, 'nextInt'))
            jset(Code02_MatrixKth1.b, i, jcall(in_, 'nextInt'))
            jset(Code02_MatrixKth1.c, i, jcall(in_, 'nextInt'))
            jset(Code02_MatrixKth1.d, i, jcall(in_, 'nextInt'))
            jset(Code02_MatrixKth1.k, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_MatrixKth1.xyv, 1, jcast('int', jadd(Code02_MatrixKth1.cntv, 1)), (lambda a, b: jcast('int', (a[2] - b[2]))))
        Code02_MatrixKth1.compute(1, Code02_MatrixKth1.q, 1, Code02_MatrixKth1.cntv)
        i = jcast('int', 1)
        while (i <= Code02_MatrixKth1.q):
            jcall(out, 'println', Code02_MatrixKth1.ans[i])
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
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_MatrixKth1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_MatrixKth1.MAXN = jcast('int', 501)
Code02_MatrixKth1.MAXQ = jcast('int', 1000001)
Code02_MatrixKth1.n = jcast('int', 0)
Code02_MatrixKth1.q = jcast('int', 0)
Code02_MatrixKth1.xyv = jarray('int', [jcast('int', (Code02_MatrixKth1.MAXN * Code02_MatrixKth1.MAXN)), 3])
Code02_MatrixKth1.cntv = jcast('int', 0)
Code02_MatrixKth1.qid = jarray('int', [Code02_MatrixKth1.MAXQ])
Code02_MatrixKth1.a = jarray('int', [Code02_MatrixKth1.MAXQ])
Code02_MatrixKth1.b = jarray('int', [Code02_MatrixKth1.MAXQ])
Code02_MatrixKth1.c = jarray('int', [Code02_MatrixKth1.MAXQ])
Code02_MatrixKth1.d = jarray('int', [Code02_MatrixKth1.MAXQ])
Code02_MatrixKth1.k = jarray('int', [Code02_MatrixKth1.MAXQ])
Code02_MatrixKth1.tree = jarray('int', [Code02_MatrixKth1.MAXN, Code02_MatrixKth1.MAXN])
Code02_MatrixKth1.lset = jarray('int', [Code02_MatrixKth1.MAXQ])
Code02_MatrixKth1.rset = jarray('int', [Code02_MatrixKth1.MAXQ])
Code02_MatrixKth1.ans = jarray('int', [Code02_MatrixKth1.MAXQ])

if __name__ == '__main__':
    Code02_MatrixKth1.main([])
