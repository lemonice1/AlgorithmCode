# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 相同数的最远距离，Python版
# 给定一个长度为n的数组arr，一共有m条查询，格式如下
# 查询 l r : 打印arr[l..r]范围上，相同的数的最远间隔距离
# 序列中两个元素的间隔距离指的是两个元素下标差的绝对值
# 1 <= n、m <= 2 * 10^5
# 1 <= arr[i] <= 2 * 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P5906
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_SameNumberMaxDist2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'arr': 'arr', 'query': 'query', 'sorted': 'sorted', 'cntv': 'cntv', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'br': 'br', 'first': 'first', 'mostRight': 'mostRight', 'maxDist': 'maxDist', 'ans': 'ans'}
    MAXN = 0
    MAXB = 0
    n = 0
    m = 0
    arr = None
    query = None
    sorted = None
    cntv = 0
    blen = 0
    bnum = 0
    bi = None
    br = None
    # first[x]表示只考虑窗口右扩阶段，数字x首次出现的位置
    first = None
    # mostRight[x]表示窗口中数字x最右出现的位置
    mostRight = None
    # 答案信息，相同的数的最远间隔距离
    maxDist = 0
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code03_SameNumberMaxDist2.bi[a[0]] != Code03_SameNumberMaxDist2.bi[b[0]]):
                return jcast('int', jcast('int', (Code03_SameNumberMaxDist2.bi[a[0]] - Code03_SameNumberMaxDist2.bi[b[0]])))
            return jcast('int', jcast('int', (a[1] - b[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code03_SameNumberMaxDist2.cntv)
        mid = 0
        ret = jcast('int', 0)
        while (left <= right):
            mid = jcast('int', jcast('int', (jcast('int', jadd(left, right)) >> (1 & 31))))
            if (Code03_SameNumberMaxDist2.sorted[mid] <= num):
                ret = jcast('int', mid)
                left = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ret)

    @staticmethod
    def force(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        ret = jcast('int', 0)
        i = jcast('int', l)
        while (i <= r):
            if (Code03_SameNumberMaxDist2.first[Code03_SameNumberMaxDist2.arr[i]] == 0):
                jset(Code03_SameNumberMaxDist2.first, Code03_SameNumberMaxDist2.arr[i], i)
            else:
                ret = jcast('int', jstatic('Math', 'max', ret, jcast('int', (i - Code03_SameNumberMaxDist2.first[Code03_SameNumberMaxDist2.arr[i]]))))
            i = jcast('int', (i + 1))
        i = jcast('int', l)
        while (i <= r):
            jset(Code03_SameNumberMaxDist2.first, Code03_SameNumberMaxDist2.arr[i], 0)
            i = jcast('int', (i + 1))
        return jcast('int', ret)

    @staticmethod
    def addRight(idx):
        idx = jcast('int', idx)
        num = jcast('int', Code03_SameNumberMaxDist2.arr[idx])
        Code03_SameNumberMaxDist2.mostRight[num] = jcast('int', idx)
        if (Code03_SameNumberMaxDist2.first[num] == 0):
            Code03_SameNumberMaxDist2.first[num] = jcast('int', idx)
        Code03_SameNumberMaxDist2.maxDist = jcast('int', jstatic('Math', 'max', Code03_SameNumberMaxDist2.maxDist, jcast('int', (idx - Code03_SameNumberMaxDist2.first[num]))))

    @staticmethod
    def addLeft(idx):
        idx = jcast('int', idx)
        num = jcast('int', Code03_SameNumberMaxDist2.arr[idx])
        if (Code03_SameNumberMaxDist2.mostRight[num] == 0):
            Code03_SameNumberMaxDist2.mostRight[num] = jcast('int', idx)
        else:
            Code03_SameNumberMaxDist2.maxDist = jcast('int', jstatic('Math', 'max', Code03_SameNumberMaxDist2.maxDist, jcast('int', (Code03_SameNumberMaxDist2.mostRight[num] - idx))))

    @staticmethod
    def delLeft(idx):
        idx = jcast('int', idx)
        num = jcast('int', Code03_SameNumberMaxDist2.arr[idx])
        if (Code03_SameNumberMaxDist2.mostRight[num] == idx):
            Code03_SameNumberMaxDist2.mostRight[num] = jcast('int', 0)

    @staticmethod
    def compute():
        block = jcast('int', 1)
        qi = jcast('int', 1)
        while ((block <= Code03_SameNumberMaxDist2.bnum) and (qi <= Code03_SameNumberMaxDist2.m)):
            Code03_SameNumberMaxDist2.maxDist = jcast('int', 0)
            jstatic('Arrays', 'fill', Code03_SameNumberMaxDist2.first, 1, jcast('int', jadd(Code03_SameNumberMaxDist2.cntv, 1)), 0)
            jstatic('Arrays', 'fill', Code03_SameNumberMaxDist2.mostRight, 1, jcast('int', jadd(Code03_SameNumberMaxDist2.cntv, 1)), 0)
            winl = jcast('int', jcast('int', jadd(Code03_SameNumberMaxDist2.br[block], 1)))
            winr = jcast('int', Code03_SameNumberMaxDist2.br[block])
            while ((qi <= Code03_SameNumberMaxDist2.m) and (Code03_SameNumberMaxDist2.bi[Code03_SameNumberMaxDist2.query[qi][0]] == block)):
                jobl = jcast('int', Code03_SameNumberMaxDist2.query[qi][0])
                jobr = jcast('int', Code03_SameNumberMaxDist2.query[qi][1])
                id = jcast('int', Code03_SameNumberMaxDist2.query[qi][2])
                if (jobr <= Code03_SameNumberMaxDist2.br[block]):
                    jset(Code03_SameNumberMaxDist2.ans, id, Code03_SameNumberMaxDist2.force(jobl, jobr))
                else:
                    while (winr < jobr):
                        Code03_SameNumberMaxDist2.addRight((winr := jcast('int', (winr + (1)))))
                    backup = jcast('int', Code03_SameNumberMaxDist2.maxDist)
                    while (winl > jobl):
                        Code03_SameNumberMaxDist2.addLeft((winl := jcast('int', (winl + (-1)))))
                    Code03_SameNumberMaxDist2.ans[id] = jcast('int', Code03_SameNumberMaxDist2.maxDist)
                    Code03_SameNumberMaxDist2.maxDist = jcast('int', backup)
                    while (winl <= Code03_SameNumberMaxDist2.br[block]):
                        Code03_SameNumberMaxDist2.delLeft(((_java_old_1 := winl), (winl := jcast('int', (winl + (1)))), _java_old_1)[2])
                qi = jcast('int', (qi + 1))
            block = jcast('int', (block + 1))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code03_SameNumberMaxDist2.n):
            Code03_SameNumberMaxDist2.sorted[i] = jcast('int', Code03_SameNumberMaxDist2.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code03_SameNumberMaxDist2.sorted, 1, jcast('int', jadd(Code03_SameNumberMaxDist2.n, 1)))
        Code03_SameNumberMaxDist2.cntv = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code03_SameNumberMaxDist2.n):
            if (Code03_SameNumberMaxDist2.sorted[Code03_SameNumberMaxDist2.cntv] != Code03_SameNumberMaxDist2.sorted[i]):
                jset(Code03_SameNumberMaxDist2.sorted, ((_java_obj_2 := Code03_SameNumberMaxDist2), (_java_key_3 := 'cntv'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))))[3], Code03_SameNumberMaxDist2.sorted[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_SameNumberMaxDist2.n):
            jset(Code03_SameNumberMaxDist2.arr, i, Code03_SameNumberMaxDist2.kth(Code03_SameNumberMaxDist2.arr[i]))
            i = jcast('int', (i + 1))
        Code03_SameNumberMaxDist2.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code03_SameNumberMaxDist2.n)))
        Code03_SameNumberMaxDist2.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code03_SameNumberMaxDist2.n, Code03_SameNumberMaxDist2.blen)) - 1)), Code03_SameNumberMaxDist2.blen)))
        i = jcast('int', 1)
        while (i <= Code03_SameNumberMaxDist2.n):
            Code03_SameNumberMaxDist2.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code03_SameNumberMaxDist2.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_SameNumberMaxDist2.bnum):
            jset(Code03_SameNumberMaxDist2.br, i, jstatic('Math', 'min', jcast('int', (i * Code03_SameNumberMaxDist2.blen)), Code03_SameNumberMaxDist2.n))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code03_SameNumberMaxDist2.query, 1, jcast('int', jadd(Code03_SameNumberMaxDist2.m, 1)), Code03_SameNumberMaxDist2.QueryCmp())

    @staticmethod
    def main(args):
        in_ = Code03_SameNumberMaxDist2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_SameNumberMaxDist2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_SameNumberMaxDist2.n):
            jset(Code03_SameNumberMaxDist2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code03_SameNumberMaxDist2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_SameNumberMaxDist2.m):
            jset(Code03_SameNumberMaxDist2.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code03_SameNumberMaxDist2.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code03_SameNumberMaxDist2.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code03_SameNumberMaxDist2.prepare()
        Code03_SameNumberMaxDist2.compute()
        i = jcast('int', 1)
        while (i <= Code03_SameNumberMaxDist2.m):
            jcall(out, 'println', Code03_SameNumberMaxDist2.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_5 := self), (_java_key_6 := 'ptr'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))), _java_old_7)[4]])

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
            raise TypeError("No matching overload for Code03_SameNumberMaxDist2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_SameNumberMaxDist2.MAXN = jcast('int', 200001)
Code03_SameNumberMaxDist2.MAXB = jcast('int', 501)
Code03_SameNumberMaxDist2.n = jcast('int', 0)
Code03_SameNumberMaxDist2.m = jcast('int', 0)
Code03_SameNumberMaxDist2.arr = jarray('int', [Code03_SameNumberMaxDist2.MAXN])
Code03_SameNumberMaxDist2.query = jarray('int', [Code03_SameNumberMaxDist2.MAXN, 3])
Code03_SameNumberMaxDist2.sorted = jarray('int', [Code03_SameNumberMaxDist2.MAXN])
Code03_SameNumberMaxDist2.cntv = jcast('int', 0)
Code03_SameNumberMaxDist2.blen = jcast('int', 0)
Code03_SameNumberMaxDist2.bnum = jcast('int', 0)
Code03_SameNumberMaxDist2.bi = jarray('int', [Code03_SameNumberMaxDist2.MAXN])
Code03_SameNumberMaxDist2.br = jarray('int', [Code03_SameNumberMaxDist2.MAXB])
Code03_SameNumberMaxDist2.first = jarray('int', [Code03_SameNumberMaxDist2.MAXN])
Code03_SameNumberMaxDist2.mostRight = jarray('int', [Code03_SameNumberMaxDist2.MAXN])
Code03_SameNumberMaxDist2.maxDist = jcast('int', 0)
Code03_SameNumberMaxDist2.ans = jarray('int', [Code03_SameNumberMaxDist2.MAXN])

if __name__ == '__main__':
    Code03_SameNumberMaxDist2.main([])
