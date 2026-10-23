# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 由乃打扑克，Python版
# 给定一个长度为n的数组arr，接下来有m条操作，操作类型如下
# 操作 1 l r v : 查询arr[l..r]范围上，第v小的数
# 操作 2 l r v : arr[l..r]范围上每个数加v，v可能是负数
# 1 <= n、m <= 10^5
# -2 * 10^4 <= 数组中的值 <= +2 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P5356
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_Poker2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'arr': 'arr', 'sortv': 'sortv', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'bl': 'bl', 'br': 'br', 'lazy': 'lazy'}
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
    lazy = None
    @staticmethod
    def innerAdd(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        i = jcast('int', l)
        while (i <= r):
            Code01_Poker2.arr[i] = jcast('int', jcast('int', jadd(Code01_Poker2.arr[i], v)))
            i = jcast('int', (i + 1))
        i = jcast('int', Code01_Poker2.bl[Code01_Poker2.bi[l]])
        while (i <= Code01_Poker2.br[Code01_Poker2.bi[l]]):
            Code01_Poker2.sortv[i] = jcast('int', Code01_Poker2.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code01_Poker2.sortv, Code01_Poker2.bl[Code01_Poker2.bi[l]], jcast('int', jadd(Code01_Poker2.br[Code01_Poker2.bi[l]], 1)))

    @staticmethod
    def add(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        if (Code01_Poker2.bi[l] == Code01_Poker2.bi[r]):
            Code01_Poker2.innerAdd(l, r, v)
        else:
            Code01_Poker2.innerAdd(l, Code01_Poker2.br[Code01_Poker2.bi[l]], v)
            Code01_Poker2.innerAdd(Code01_Poker2.bl[Code01_Poker2.bi[r]], r, v)
            i = jcast('int', jcast('int', jadd(Code01_Poker2.bi[l], 1)))
            while (i <= jcast('int', (Code01_Poker2.bi[r] - 1))):
                Code01_Poker2.lazy[i] = jcast('int', jcast('int', jadd(Code01_Poker2.lazy[i], v)))
                i = jcast('int', (i + 1))

    @staticmethod
    def getMin(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        lb = jcast('int', Code01_Poker2.bi[l])
        rb = jcast('int', Code01_Poker2.bi[r])
        ans = jcast('int', 10000000)
        if (lb == rb):
            i = jcast('int', l)
            while (i <= r):
                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(Code01_Poker2.arr[i], Code01_Poker2.lazy[lb]))))
                i = jcast('int', (i + 1))
        else:
            i = jcast('int', l)
            while (i <= Code01_Poker2.br[lb]):
                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(Code01_Poker2.arr[i], Code01_Poker2.lazy[lb]))))
                i = jcast('int', (i + 1))
            i = jcast('int', Code01_Poker2.bl[rb])
            while (i <= r):
                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(Code01_Poker2.arr[i], Code01_Poker2.lazy[rb]))))
                i = jcast('int', (i + 1))
            i = jcast('int', jcast('int', jadd(lb, 1)))
            while (i <= jcast('int', (rb - 1))):
                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(Code01_Poker2.sortv[Code01_Poker2.bl[i]], Code01_Poker2.lazy[i]))))
                i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def getMax(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        lb = jcast('int', Code01_Poker2.bi[l])
        rb = jcast('int', Code01_Poker2.bi[r])
        ans = jcast('int', jcast('int', (-10000000)))
        if (lb == rb):
            i = jcast('int', l)
            while (i <= r):
                ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(Code01_Poker2.arr[i], Code01_Poker2.lazy[lb]))))
                i = jcast('int', (i + 1))
        else:
            i = jcast('int', l)
            while (i <= Code01_Poker2.br[lb]):
                ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(Code01_Poker2.arr[i], Code01_Poker2.lazy[lb]))))
                i = jcast('int', (i + 1))
            i = jcast('int', Code01_Poker2.bl[rb])
            while (i <= r):
                ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(Code01_Poker2.arr[i], Code01_Poker2.lazy[rb]))))
                i = jcast('int', (i + 1))
            i = jcast('int', jcast('int', jadd(lb, 1)))
            while (i <= jcast('int', (rb - 1))):
                ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(Code01_Poker2.sortv[Code01_Poker2.br[i]], Code01_Poker2.lazy[i]))))
                i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 返回第i块内<= v的数字个数
    @staticmethod
    def blockCnt(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        v = jcast('int', jcast('int', (v - Code01_Poker2.lazy[i])))
        l = jcast('int', Code01_Poker2.bl[i])
        r = jcast('int', Code01_Poker2.br[i])
        if (Code01_Poker2.sortv[l] > v):
            return jcast('int', 0)
        if (Code01_Poker2.sortv[r] <= v):
            return jcast('int', jcast('int', jadd(jcast('int', (r - l)), 1)))
        m = 0
        find = jcast('int', l)
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code01_Poker2.sortv[m] <= v):
                find = jcast('int', m)
                l = jcast('int', jcast('int', jadd(m, 1)))
            else:
                r = jcast('int', jcast('int', (m - 1)))
        return jcast('int', jcast('int', jadd(jcast('int', (find - Code01_Poker2.bl[i])), 1)))

    # 返回arr[l..r]范围上<= v的数字个数
    @staticmethod
    def getCnt(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        lb = jcast('int', Code01_Poker2.bi[l])
        rb = jcast('int', Code01_Poker2.bi[r])
        ans = jcast('int', 0)
        if (lb == rb):
            i = jcast('int', l)
            while (i <= r):
                if (jcast('int', jadd(Code01_Poker2.arr[i], Code01_Poker2.lazy[lb])) <= v):
                    ans = jcast('int', (ans + 1))
                i = jcast('int', (i + 1))
        else:
            i = jcast('int', l)
            while (i <= Code01_Poker2.br[lb]):
                if (jcast('int', jadd(Code01_Poker2.arr[i], Code01_Poker2.lazy[lb])) <= v):
                    ans = jcast('int', (ans + 1))
                i = jcast('int', (i + 1))
            i = jcast('int', Code01_Poker2.bl[rb])
            while (i <= r):
                if (jcast('int', jadd(Code01_Poker2.arr[i], Code01_Poker2.lazy[rb])) <= v):
                    ans = jcast('int', (ans + 1))
                i = jcast('int', (i + 1))
            i = jcast('int', jcast('int', jadd(lb, 1)))
            while (i <= jcast('int', (rb - 1))):
                ans = jcast('int', jcast('int', jadd(ans, Code01_Poker2.blockCnt(i, v))))
                i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def query(l, r, k):
        l = jcast('int', l)
        r = jcast('int', r)
        k = jcast('int', k)
        if ((k < 1) or (k > jcast('int', jadd(jcast('int', (r - l)), 1)))):
            return jcast('int', jcast('int', (-1)))
        minv = jcast('int', Code01_Poker2.getMin(l, r))
        maxv = jcast('int', Code01_Poker2.getMax(l, r))
        midv = 0
        ans = jcast('int', jcast('int', (-1)))
        while (minv <= maxv):
            midv = jcast('int', jcast('int', jadd(minv, jcast('int', jdiv(jcast('int', (maxv - minv)), 2)))))
            if (Code01_Poker2.getCnt(l, r, midv) >= k):
                ans = jcast('int', midv)
                maxv = jcast('int', jcast('int', (midv - 1)))
            else:
                minv = jcast('int', jcast('int', jadd(midv, 1)))
        return jcast('int', ans)

    # 注意调整块长
    @staticmethod
    def prepare():
        Code01_Poker2.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', jcast('int', jdiv(Code01_Poker2.n, 2)))))
        Code01_Poker2.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code01_Poker2.n, Code01_Poker2.blen)) - 1)), Code01_Poker2.blen)))
        i = jcast('int', 1)
        while (i <= Code01_Poker2.n):
            Code01_Poker2.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code01_Poker2.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_Poker2.bnum):
            Code01_Poker2.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code01_Poker2.blen)), 1)))
            jset(Code01_Poker2.br, i, jstatic('Math', 'min', jcast('int', (i * Code01_Poker2.blen)), Code01_Poker2.n))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_Poker2.n):
            Code01_Poker2.sortv[i] = jcast('int', Code01_Poker2.arr[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_Poker2.bnum):
            jstatic('Arrays', 'sort', Code01_Poker2.sortv, Code01_Poker2.bl[i], jcast('int', jadd(Code01_Poker2.br[i], 1)))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code01_Poker2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_Poker2.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_Poker2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_Poker2.n):
            jset(Code01_Poker2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code01_Poker2.prepare()
        i = jcast('int', 1)
        op = 0
        l = 0
        r = 0
        v = 0
        while (i <= Code01_Poker2.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            l = jcast('int', jcall(in_, 'nextInt'))
            r = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                jcall(out, 'println', Code01_Poker2.query(l, r, v))
            else:
                Code01_Poker2.add(l, r, v)
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
            raise TypeError("No matching overload for Code01_Poker2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_Poker2.MAXN = jcast('int', 100001)
Code01_Poker2.MAXB = jcast('int', 1001)
Code01_Poker2.n = jcast('int', 0)
Code01_Poker2.m = jcast('int', 0)
Code01_Poker2.arr = jarray('int', [Code01_Poker2.MAXN])
Code01_Poker2.sortv = jarray('int', [Code01_Poker2.MAXN])
Code01_Poker2.blen = jcast('int', 0)
Code01_Poker2.bnum = jcast('int', 0)
Code01_Poker2.bi = jarray('int', [Code01_Poker2.MAXN])
Code01_Poker2.bl = jarray('int', [Code01_Poker2.MAXB])
Code01_Poker2.br = jarray('int', [Code01_Poker2.MAXB])
Code01_Poker2.lazy = jarray('int', [Code01_Poker2.MAXB])

if __name__ == '__main__':
    Code01_Poker2.main([])
