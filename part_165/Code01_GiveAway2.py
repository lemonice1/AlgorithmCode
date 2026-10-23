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

# Give Away，Python版
# 给定一个长度为n的数组arr，接下来有m条操作，每条操作是如下两种类型中的一种
# 操作 0 a b c : 打印arr[a..b]范围上>=c的数字个数
# 操作 1 a b   : 把arr[a]的值改成b
# 1 <= n <= 5 * 10^5
# 1 <= m <= 10^5
# 1 <= 数组中的值 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/SP18185
# 测试链接 : https://www.spoj.com/problems/GIVEAWAY
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_GiveAway2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'arr': 'arr', 'sortv': 'sortv', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'bl': 'bl', 'br': 'br'}
    MAXN = 0
    MAXB = 0
    n = 0
    m = 0
    arr = None
    sortv = None
    blen = 0
    bnum = 0
    bi = None
    bl = None
    br = None
    @staticmethod
    def build():
        Code01_GiveAway2.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code01_GiveAway2.n)))
        Code01_GiveAway2.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code01_GiveAway2.n, Code01_GiveAway2.blen)) - 1)), Code01_GiveAway2.blen)))
        i = jcast('int', 1)
        while (i <= Code01_GiveAway2.n):
            Code01_GiveAway2.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code01_GiveAway2.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_GiveAway2.bnum):
            Code01_GiveAway2.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code01_GiveAway2.blen)), 1)))
            jset(Code01_GiveAway2.br, i, jstatic('Math', 'min', jcast('int', (i * Code01_GiveAway2.blen)), Code01_GiveAway2.n))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_GiveAway2.n):
            Code01_GiveAway2.sortv[i] = jcast('int', Code01_GiveAway2.arr[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_GiveAway2.bnum):
            jstatic('Arrays', 'sort', Code01_GiveAway2.sortv, Code01_GiveAway2.bl[i], jcast('int', jadd(Code01_GiveAway2.br[i], 1)))
            i = jcast('int', (i + 1))

    @staticmethod
    def getCnt(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        l = jcast('int', Code01_GiveAway2.bl[i])
        r = jcast('int', Code01_GiveAway2.br[i])
        m = 0
        ans = jcast('int', 0)
        while (l <= r):
            m = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code01_GiveAway2.sortv[m] >= v):
                ans = jcast('int', jcast('int', jadd(ans, jcast('int', jadd(jcast('int', (r - m)), 1)))))
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    @staticmethod
    def query(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        ans = jcast('int', 0)
        if (Code01_GiveAway2.bi[l] == Code01_GiveAway2.bi[r]):
            i = jcast('int', l)
            while (i <= r):
                if (Code01_GiveAway2.arr[i] >= v):
                    ans = jcast('int', (ans + 1))
                i = jcast('int', (i + 1))
        else:
            i = jcast('int', l)
            while (i <= Code01_GiveAway2.br[Code01_GiveAway2.bi[l]]):
                if (Code01_GiveAway2.arr[i] >= v):
                    ans = jcast('int', (ans + 1))
                i = jcast('int', (i + 1))
            i = jcast('int', Code01_GiveAway2.bl[Code01_GiveAway2.bi[r]])
            while (i <= r):
                if (Code01_GiveAway2.arr[i] >= v):
                    ans = jcast('int', (ans + 1))
                i = jcast('int', (i + 1))
            i = jcast('int', jcast('int', jadd(Code01_GiveAway2.bi[l], 1)))
            while (i <= jcast('int', (Code01_GiveAway2.bi[r] - 1))):
                ans = jcast('int', jcast('int', jadd(ans, Code01_GiveAway2.getCnt(i, v))))
                i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def update(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        l = jcast('int', Code01_GiveAway2.bl[Code01_GiveAway2.bi[i]])
        r = jcast('int', Code01_GiveAway2.br[Code01_GiveAway2.bi[i]])
        Code01_GiveAway2.arr[i] = jcast('int', v)
        j = jcast('int', l)
        while (j <= r):
            Code01_GiveAway2.sortv[j] = jcast('int', Code01_GiveAway2.arr[j])
            j = jcast('int', (j + 1))
        jstatic('Arrays', 'sort', Code01_GiveAway2.sortv, l, jcast('int', jadd(r, 1)))

    @staticmethod
    def main(args):
        in_ = Code01_GiveAway2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_GiveAway2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_GiveAway2.n):
            jset(Code01_GiveAway2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code01_GiveAway2.build()
        Code01_GiveAway2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        op = 0
        a = 0
        b = 0
        c = 0
        while (i <= Code01_GiveAway2.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            a = jcast('int', jcall(in_, 'nextInt'))
            b = jcast('int', jcall(in_, 'nextInt'))
            if (op == 0):
                c = jcast('int', jcall(in_, 'nextInt'))
                jcall(out, 'println', Code01_GiveAway2.query(a, b, c))
            else:
                Code01_GiveAway2.update(a, b)
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
            self.buffer = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_GiveAway2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_GiveAway2.MAXN = jcast('int', 500001)
Code01_GiveAway2.MAXB = jcast('int', 1001)
Code01_GiveAway2.n = jcast('int', 0)
Code01_GiveAway2.m = jcast('int', 0)
Code01_GiveAway2.arr = jarray('int', [Code01_GiveAway2.MAXN])
Code01_GiveAway2.sortv = jarray('int', [Code01_GiveAway2.MAXN])
Code01_GiveAway2.blen = jcast('int', 0)
Code01_GiveAway2.bnum = jcast('int', 0)
Code01_GiveAway2.bi = jarray('int', [Code01_GiveAway2.MAXN])
Code01_GiveAway2.bl = jarray('int', [Code01_GiveAway2.MAXB])
Code01_GiveAway2.br = jarray('int', [Code01_GiveAway2.MAXB])

if __name__ == '__main__':
    Code01_GiveAway2.main([])
