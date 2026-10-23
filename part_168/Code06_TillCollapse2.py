# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最少划分，Python版
# 给定一个长度为n的数组arr，考虑如下问题的解
# 数组arr划分成若干段子数组，保证每段不同数字的种类 <= k，返回至少划分成几段
# 打印k = 1, 2, 3..n时，所有的答案
# 1 <= arr[i] <= n <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF786C
# 测试链接 : https://codeforces.com/problemset/problem/786/C
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_TillCollapse2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'blen': 'blen', 'arr': 'arr', 'vis': 'vis', 'ans': 'ans'}
    MAXN = 0
    n = 0
    blen = 0
    arr = None
    vis = None
    ans = None
    @staticmethod
    def query(limit):
        limit = jcast('int', limit)
        kind = jcast('int', 0)
        cnt = jcast('int', 0)
        start = jcast('int', 1)
        i = jcast('int', 1)
        while (i <= Code06_TillCollapse2.n):
            if (not Code06_TillCollapse2.vis[Code06_TillCollapse2.arr[i]]):
                kind = jcast('int', (kind + 1))
                if (kind > limit):
                    cnt = jcast('int', (cnt + 1))
                    j = jcast('int', start)
                    while (j < i):
                        jset(Code06_TillCollapse2.vis, Code06_TillCollapse2.arr[j], False)
                        j = jcast('int', (j + 1))
                    start = jcast('int', i)
                    kind = jcast('int', 1)
                jset(Code06_TillCollapse2.vis, Code06_TillCollapse2.arr[i], True)
            i = jcast('int', (i + 1))
        if (kind > 0):
            cnt = jcast('int', (cnt + 1))
            j = jcast('int', start)
            while (j <= Code06_TillCollapse2.n):
                jset(Code06_TillCollapse2.vis, Code06_TillCollapse2.arr[j], False)
                j = jcast('int', (j + 1))
        return jcast('int', cnt)

    @staticmethod
    def jump(l, r, curAns):
        l = jcast('int', l)
        r = jcast('int', r)
        curAns = jcast('int', curAns)
        find = jcast('int', l)
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            check = jcast('int', Code06_TillCollapse2.query(mid))
            if (check < curAns):
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                if (check > curAns):
                    l = jcast('int', jcast('int', jadd(mid, 1)))
                else:
                    find = jcast('int', mid)
                    l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', jcast('int', jadd(find, 1)))

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code06_TillCollapse2.blen):
            jset(Code06_TillCollapse2.ans, i, Code06_TillCollapse2.query(i))
            i = jcast('int', (i + 1))
        i = jcast('int', jcast('int', jadd(Code06_TillCollapse2.blen, 1)))
        while (i <= Code06_TillCollapse2.n):
            jset(Code06_TillCollapse2.ans, i, Code06_TillCollapse2.query(i))
            i = jcast('int', Code06_TillCollapse2.jump(i, Code06_TillCollapse2.n, Code06_TillCollapse2.ans[i]))

    @staticmethod
    def prepare():
        log2n = jcast('int', 0)
        while (jcast('int', (1 << (log2n & 31))) <= jcast('int', (Code06_TillCollapse2.n >> (1 & 31)))):
            log2n = jcast('int', (log2n + 1))
        Code06_TillCollapse2.blen = jcast('int', jstatic('Math', 'max', 1, jcast('int', jstatic('Math', 'sqrt', jcast('int', (Code06_TillCollapse2.n * log2n))))))
        jstatic('Arrays', 'fill', Code06_TillCollapse2.ans, 1, jcast('int', jadd(Code06_TillCollapse2.n, 1)), jcast('int', (-1)))

    @staticmethod
    def main(args):
        in_ = Code06_TillCollapse2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jget(System, 'out'))
        Code06_TillCollapse2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_TillCollapse2.n):
            jset(Code06_TillCollapse2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code06_TillCollapse2.prepare()
        Code06_TillCollapse2.compute()
        i = jcast('int', 1)
        while (i <= Code06_TillCollapse2.n):
            if (Code06_TillCollapse2.ans[i] == jcast('int', (-1))):
                Code06_TillCollapse2.ans[i] = jcast('int', Code06_TillCollapse2.ans[jcast('int', (i - 1))])
            jcall(out, 'print', jadd(Code06_TillCollapse2.ans[i], ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println')
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
            raise TypeError("No matching overload for Code06_TillCollapse2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_TillCollapse2.MAXN = jcast('int', 100001)
Code06_TillCollapse2.n = jcast('int', 0)
Code06_TillCollapse2.blen = jcast('int', 0)
Code06_TillCollapse2.arr = jarray('int', [Code06_TillCollapse2.MAXN])
Code06_TillCollapse2.vis = jarray('boolean', [Code06_TillCollapse2.MAXN])
Code06_TillCollapse2.ans = jarray('int', [Code06_TillCollapse2.MAXN])

if __name__ == '__main__':
    Code06_TillCollapse2.main([])
