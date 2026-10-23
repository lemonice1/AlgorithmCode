# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 五彩斑斓的世界，Python版
# 给定一个长度为n的数组arr，一共有m条操作，每条操作类型如下
# 操作 1 l r x : arr[l..r]范围上，所有大于x的数减去x
# 操作 2 l r x : arr[l..r]范围上，查询x出现的次数
# 1 <= n <= 10^6
# 1 <= m <= 5 * 10^5
# 0 <= arr[i]、x <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4117
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 对应实现可参考 Code03_ColorfulWorld2.py
# 两个版本保留相同的算法逻辑
class Code03_ColorfulWorld1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXV': 'MAXV', 'n': 'n', 'm': 'm', 'blen': 'blen', 'bnum': 'bnum', 'arr': 'arr', 'op': 'op', 'ql': 'ql', 'qr': 'qr', 'qx': 'qx', 'maxv': 'maxv', 'lazy': 'lazy', 'fa': 'fa', 'pre0': 'pre0', 'cntv': 'cntv', 'ans': 'ans'}
    MAXN = 0
    MAXM = 0
    MAXV = 0
    n = 0
    m = 0
    blen = 0
    bnum = 0
    arr = None
    op = None
    ql = None
    qr = None
    qx = None
    # maxv代表一个序列块中的最大值
    # lazy代表一个序列块中，所有数字需要统计减去多少
    # fa代表值域并查集
    # pre0代表数组前缀上0的词频统计
    # cntv代表一个序列块中每种值的词频统计
    maxv = 0
    lazy = 0
    fa = None
    pre0 = None
    cntv = None
    # 查询的答案
    ans = None
    # 查询x值变成了什么
    @staticmethod
    def find(x):
        x = jcast('int', x)
        if (x != Code03_ColorfulWorld1.fa[x]):
            jset(Code03_ColorfulWorld1.fa, x, Code03_ColorfulWorld1.find(Code03_ColorfulWorld1.fa[x]))
        return jcast('int', Code03_ColorfulWorld1.fa[x])

    # 所有x值变成y值
    @staticmethod
    def change(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code03_ColorfulWorld1.fa[x] = jcast('int', y)

    # 修改保留在值域并查集，把修改写入arr[l..r]
    @staticmethod
    def down(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', l)
        while (i <= r):
            jset(Code03_ColorfulWorld1.arr, i, Code03_ColorfulWorld1.find(Code03_ColorfulWorld1.arr[i]))
            i = jcast('int', (i + 1))

    @staticmethod
    def update(qi, l, r):
        qi = jcast('int', qi)
        l = jcast('int', l)
        r = jcast('int', r)
        jobl = jcast('int', Code03_ColorfulWorld1.ql[qi])
        jobr = jcast('int', Code03_ColorfulWorld1.qr[qi])
        jobx = jcast('int', Code03_ColorfulWorld1.qx[qi])
        if (((jobx >= jcast('int', (Code03_ColorfulWorld1.maxv - Code03_ColorfulWorld1.lazy))) or (jobl > r)) or (jobr < l)):
            return
        if ((jobl <= l) and (r <= jobr)):
            if (jcast('int', (jobx << (1 & 31))) <= jcast('int', (Code03_ColorfulWorld1.maxv - Code03_ColorfulWorld1.lazy))):
                v = jcast('int', jcast('int', jadd(Code03_ColorfulWorld1.lazy, 1)))
                while (v <= jcast('int', jadd(Code03_ColorfulWorld1.lazy, jobx))):
                    Code03_ColorfulWorld1.cntv[jcast('int', jadd(v, jobx))] = jcast('int', jcast('int', jadd(Code03_ColorfulWorld1.cntv[jcast('int', jadd(v, jobx))], Code03_ColorfulWorld1.cntv[v])))
                    Code03_ColorfulWorld1.cntv[v] = jcast('int', 0)
                    Code03_ColorfulWorld1.change(v, jcast('int', jadd(v, jobx)))
                    v = jcast('int', (v + 1))
                Code03_ColorfulWorld1.lazy = jcast('int', jcast('int', jadd(Code03_ColorfulWorld1.lazy, jobx)))
            else:
                v = jcast('int', jcast('int', jadd(jcast('int', jadd(Code03_ColorfulWorld1.lazy, jobx)), 1)))
                while (v <= Code03_ColorfulWorld1.maxv):
                    Code03_ColorfulWorld1.cntv[jcast('int', (v - jobx))] = jcast('int', jcast('int', jadd(Code03_ColorfulWorld1.cntv[jcast('int', (v - jobx))], Code03_ColorfulWorld1.cntv[v])))
                    Code03_ColorfulWorld1.cntv[v] = jcast('int', 0)
                    Code03_ColorfulWorld1.change(v, jcast('int', (v - jobx)))
                    v = jcast('int', (v + 1))
                v = jcast('int', Code03_ColorfulWorld1.maxv)
                while (v >= 0):
                    try:
                        if (Code03_ColorfulWorld1.cntv[v] != 0):
                            Code03_ColorfulWorld1.maxv = jcast('int', v)
                            raise JBreak(None)
                    except JContinue as _java_control_1:
                        if _java_control_1.label not in (None,):
                            raise
                    except JBreak as _java_control_1:
                        if _java_control_1.label not in (None,):
                            raise
                        break
                    v = jcast('int', (v - 1))
        else:
            Code03_ColorfulWorld1.down(l, r)
            i = jcast('int', jstatic('Math', 'max', l, jobl))
            while (i <= jstatic('Math', 'min', r, jobr)):
                if (jcast('int', (Code03_ColorfulWorld1.arr[i] - Code03_ColorfulWorld1.lazy)) > jobx):
                    ((_java_obj_2 := Code03_ColorfulWorld1.cntv), (_java_key_3 := Code03_ColorfulWorld1.arr[i]), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (-1)))), _java_old_4)[4]
                    Code03_ColorfulWorld1.arr[i] = jcast('int', jcast('int', (Code03_ColorfulWorld1.arr[i] - jobx)))
                    ((_java_obj_5 := Code03_ColorfulWorld1.cntv), (_java_key_6 := Code03_ColorfulWorld1.arr[i]), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))), _java_old_7)[4]
                i = jcast('int', (i + 1))
            v = jcast('int', Code03_ColorfulWorld1.maxv)
            while (v >= 0):
                try:
                    if (Code03_ColorfulWorld1.cntv[v] != 0):
                        Code03_ColorfulWorld1.maxv = jcast('int', v)
                        raise JBreak(None)
                except JContinue as _java_control_8:
                    if _java_control_8.label not in (None,):
                        raise
                except JBreak as _java_control_8:
                    if _java_control_8.label not in (None,):
                        raise
                    break
                v = jcast('int', (v - 1))

    @staticmethod
    def query(qi, l, r):
        qi = jcast('int', qi)
        l = jcast('int', l)
        r = jcast('int', r)
        jobl = jcast('int', Code03_ColorfulWorld1.ql[qi])
        jobr = jcast('int', Code03_ColorfulWorld1.qr[qi])
        jobx = jcast('int', Code03_ColorfulWorld1.qx[qi])
        if ((((jobx == 0) or (jobx > jcast('int', (Code03_ColorfulWorld1.maxv - Code03_ColorfulWorld1.lazy)))) or (jobl > r)) or (jobr < l)):
            return
        if ((jobl <= l) and (r <= jobr)):
            Code03_ColorfulWorld1.ans[qi] = jcast('int', jcast('int', jadd(Code03_ColorfulWorld1.ans[qi], Code03_ColorfulWorld1.cntv[jcast('int', jadd(jobx, Code03_ColorfulWorld1.lazy))])))
        else:
            Code03_ColorfulWorld1.down(l, r)
            i = jcast('int', jstatic('Math', 'max', l, jobl))
            while (i <= jstatic('Math', 'min', r, jobr)):
                if (jcast('int', (Code03_ColorfulWorld1.arr[i] - Code03_ColorfulWorld1.lazy)) == jobx):
                    Code03_ColorfulWorld1.ans[qi] = jcast('int', (Code03_ColorfulWorld1.ans[qi] + 1))
                i = jcast('int', (i + 1))

    @staticmethod
    def compute(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        jstatic('Arrays', 'fill', Code03_ColorfulWorld1.cntv, 0)
        Code03_ColorfulWorld1.maxv = jcast('int', jset(Code03_ColorfulWorld1, 'lazy', 0))
        i = jcast('int', l)
        while (i <= r):
            Code03_ColorfulWorld1.maxv = jcast('int', jstatic('Math', 'max', Code03_ColorfulWorld1.maxv, Code03_ColorfulWorld1.arr[i]))
            ((_java_obj_9 := Code03_ColorfulWorld1.cntv), (_java_key_10 := Code03_ColorfulWorld1.arr[i]), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))), _java_old_11)[4]
            i = jcast('int', (i + 1))
        v = jcast('int', 0)
        while (v <= Code03_ColorfulWorld1.maxv):
            Code03_ColorfulWorld1.fa[v] = jcast('int', v)
            v = jcast('int', (v + 1))
        i = jcast('int', 1)
        while (i <= Code03_ColorfulWorld1.m):
            if (Code03_ColorfulWorld1.op[i] == 1):
                Code03_ColorfulWorld1.update(i, l, r)
            else:
                Code03_ColorfulWorld1.query(i, l, r)
            i = jcast('int', (i + 1))

    @staticmethod
    def prepare():
        Code03_ColorfulWorld1.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code03_ColorfulWorld1.n)))
        Code03_ColorfulWorld1.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code03_ColorfulWorld1.n, Code03_ColorfulWorld1.blen)) - 1)), Code03_ColorfulWorld1.blen)))
        i = jcast('int', 1)
        while (i <= Code03_ColorfulWorld1.n):
            Code03_ColorfulWorld1.pre0[i] = jcast('int', jcast('int', jadd(Code03_ColorfulWorld1.pre0[jcast('int', (i - 1))], (1 if (Code03_ColorfulWorld1.arr[i] == 0) else 0))))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_ColorfulWorld1.m):
            if ((Code03_ColorfulWorld1.op[i] == 2) and (Code03_ColorfulWorld1.qx[i] == 0)):
                Code03_ColorfulWorld1.ans[i] = jcast('int', jcast('int', (Code03_ColorfulWorld1.pre0[Code03_ColorfulWorld1.qr[i]] - Code03_ColorfulWorld1.pre0[jcast('int', (Code03_ColorfulWorld1.ql[i] - 1))])))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code03_ColorfulWorld1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_ColorfulWorld1.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_ColorfulWorld1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_ColorfulWorld1.n):
            jset(Code03_ColorfulWorld1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_ColorfulWorld1.m):
            jset(Code03_ColorfulWorld1.op, i, jcall(in_, 'nextInt'))
            jset(Code03_ColorfulWorld1.ql, i, jcall(in_, 'nextInt'))
            jset(Code03_ColorfulWorld1.qr, i, jcall(in_, 'nextInt'))
            jset(Code03_ColorfulWorld1.qx, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code03_ColorfulWorld1.prepare()
        i = jcast('int', 1)
        l = 0
        r = 0
        while (i <= Code03_ColorfulWorld1.bnum):
            l = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code03_ColorfulWorld1.blen)), 1)))
            r = jcast('int', jstatic('Math', 'min', jcast('int', (i * Code03_ColorfulWorld1.blen)), Code03_ColorfulWorld1.n))
            Code03_ColorfulWorld1.compute(l, r)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_ColorfulWorld1.m):
            if (Code03_ColorfulWorld1.op[i] == 2):
                jcall(out, 'println', Code03_ColorfulWorld1.ans[i])
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
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code03_ColorfulWorld1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_ColorfulWorld1.MAXN = jcast('int', 1000001)
Code03_ColorfulWorld1.MAXM = jcast('int', 500001)
Code03_ColorfulWorld1.MAXV = jcast('int', 100002)
Code03_ColorfulWorld1.n = jcast('int', 0)
Code03_ColorfulWorld1.m = jcast('int', 0)
Code03_ColorfulWorld1.blen = jcast('int', 0)
Code03_ColorfulWorld1.bnum = jcast('int', 0)
Code03_ColorfulWorld1.arr = jarray('int', [Code03_ColorfulWorld1.MAXN])
Code03_ColorfulWorld1.op = jarray('int', [Code03_ColorfulWorld1.MAXM])
Code03_ColorfulWorld1.ql = jarray('int', [Code03_ColorfulWorld1.MAXM])
Code03_ColorfulWorld1.qr = jarray('int', [Code03_ColorfulWorld1.MAXM])
Code03_ColorfulWorld1.qx = jarray('int', [Code03_ColorfulWorld1.MAXM])
Code03_ColorfulWorld1.maxv = jcast('int', 0)
Code03_ColorfulWorld1.lazy = jcast('int', 0)
Code03_ColorfulWorld1.fa = jarray('int', [Code03_ColorfulWorld1.MAXV])
Code03_ColorfulWorld1.pre0 = jarray('int', [Code03_ColorfulWorld1.MAXN])
Code03_ColorfulWorld1.cntv = jarray('int', [Code03_ColorfulWorld1.MAXV])
Code03_ColorfulWorld1.ans = jarray('int', [Code03_ColorfulWorld1.MAXM])

if __name__ == '__main__':
    Code03_ColorfulWorld1.main([])
