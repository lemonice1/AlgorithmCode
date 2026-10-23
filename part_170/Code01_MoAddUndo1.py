# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 只增回滚莫队入门题，Python版
# 给定一个长度为n的数组arr，下面定义重要度的概念
# 如果一段范围上，数字x出现c次，那么这个数字的重要度为x * c
# 范围上的最大重要度，就是该范围上，每种数字的重要度，取最大值
# 一共有m条查询，格式 l r : 打印arr[l..r]范围上的最大重要度
# 1 <= n、m <= 10^5
# 1 <= arr[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/AT_joisc2014_c
# 测试链接 : https://atcoder.jp/contests/joisc2014/tasks/joisc2014_c
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_MoAddUndo1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'arr': 'arr', 'query': 'query', 'sorted': 'sorted', 'cntv': 'cntv', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'br': 'br', 'cnt': 'cnt', 'curAns': 'curAns', 'ans': 'ans'}
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
    # 词频表
    cnt = None
    # 当前窗口的最大重要度
    curAns = 0
    # 收集所有答案
    ans = None
    # 只增回滚莫队经典排序
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code01_MoAddUndo1.bi[a[0]] != Code01_MoAddUndo1.bi[b[0]]):
                return jcast('int', jcast('int', (Code01_MoAddUndo1.bi[a[0]] - Code01_MoAddUndo1.bi[b[0]])))
            return jcast('int', jcast('int', (a[1] - b[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code01_MoAddUndo1.cntv)
        mid = 0
        ret = jcast('int', 0)
        while (left <= right):
            mid = jcast('int', jcast('int', (jcast('int', jadd(left, right)) >> (1 & 31))))
            if (Code01_MoAddUndo1.sorted[mid] <= num):
                ret = jcast('int', mid)
                left = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ret)

    # 暴力遍历arr[l..r]得到答案
    @staticmethod
    def force(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        ret = jcast('long', 0)
        i = jcast('int', l)
        while (i <= r):
            ((_java_obj_1 := Code01_MoAddUndo1.cnt), (_java_key_2 := Code01_MoAddUndo1.arr[i]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
            i = jcast('int', (i + 1))
        i = jcast('int', l)
        while (i <= r):
            ret = jcast('long', jstatic('Math', 'max', ret, jcast('long', (jcast('long', Code01_MoAddUndo1.cnt[Code01_MoAddUndo1.arr[i]]) * Code01_MoAddUndo1.sorted[Code01_MoAddUndo1.arr[i]]))))
            i = jcast('int', (i + 1))
        i = jcast('int', l)
        while (i <= r):
            ((_java_obj_4 := Code01_MoAddUndo1.cnt), (_java_key_5 := Code01_MoAddUndo1.arr[i]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))), _java_old_6)[4]
            i = jcast('int', (i + 1))
        return jcast('long', ret)

    # 窗口增加num，词频和答案都更新
    @staticmethod
    def add(num):
        num = jcast('int', num)
        Code01_MoAddUndo1.cnt[num] = jcast('int', (Code01_MoAddUndo1.cnt[num] + 1))
        Code01_MoAddUndo1.curAns = jcast('long', jstatic('Math', 'max', Code01_MoAddUndo1.curAns, jcast('long', (jcast('long', Code01_MoAddUndo1.cnt[num]) * Code01_MoAddUndo1.sorted[num]))))

    # 窗口减少num，词频更新、答案不更新
    @staticmethod
    def del_(num):
        num = jcast('int', num)
        Code01_MoAddUndo1.cnt[num] = jcast('int', (Code01_MoAddUndo1.cnt[num] - 1))

    @staticmethod
    def compute():
        block = jcast('int', 1)
        qi = jcast('int', 1)
        while ((block <= Code01_MoAddUndo1.bnum) and (qi <= Code01_MoAddUndo1.m)):
            Code01_MoAddUndo1.curAns = jcast('long', 0)
            jstatic('Arrays', 'fill', Code01_MoAddUndo1.cnt, 1, jcast('int', jadd(Code01_MoAddUndo1.cntv, 1)), 0)
            winl = jcast('int', jcast('int', jadd(Code01_MoAddUndo1.br[block], 1)))
            winr = jcast('int', Code01_MoAddUndo1.br[block])
            while ((qi <= Code01_MoAddUndo1.m) and (Code01_MoAddUndo1.bi[Code01_MoAddUndo1.query[qi][0]] == block)):
                jobl = jcast('int', Code01_MoAddUndo1.query[qi][0])
                jobr = jcast('int', Code01_MoAddUndo1.query[qi][1])
                id = jcast('int', Code01_MoAddUndo1.query[qi][2])
                if (jobr <= Code01_MoAddUndo1.br[block]):
                    jset(Code01_MoAddUndo1.ans, id, Code01_MoAddUndo1.force(jobl, jobr))
                else:
                    while (winr < jobr):
                        Code01_MoAddUndo1.add(Code01_MoAddUndo1.arr[(winr := jcast('int', (winr + (1))))])
                    backup = jcast('long', Code01_MoAddUndo1.curAns)
                    while (winl > jobl):
                        Code01_MoAddUndo1.add(Code01_MoAddUndo1.arr[(winl := jcast('int', (winl + (-1))))])
                    Code01_MoAddUndo1.ans[id] = jcast('long', Code01_MoAddUndo1.curAns)
                    Code01_MoAddUndo1.curAns = jcast('long', backup)
                    while (winl <= Code01_MoAddUndo1.br[block]):
                        Code01_MoAddUndo1.del_(Code01_MoAddUndo1.arr[((_java_old_7 := winl), (winl := jcast('int', (winl + (1)))), _java_old_7)[2]])
                qi = jcast('int', (qi + 1))
            block = jcast('int', (block + 1))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code01_MoAddUndo1.n):
            Code01_MoAddUndo1.sorted[i] = jcast('int', Code01_MoAddUndo1.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code01_MoAddUndo1.sorted, 1, jcast('int', jadd(Code01_MoAddUndo1.n, 1)))
        Code01_MoAddUndo1.cntv = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code01_MoAddUndo1.n):
            if (Code01_MoAddUndo1.sorted[Code01_MoAddUndo1.cntv] != Code01_MoAddUndo1.sorted[i]):
                jset(Code01_MoAddUndo1.sorted, ((_java_obj_8 := Code01_MoAddUndo1), (_java_key_9 := 'cntv'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3], Code01_MoAddUndo1.sorted[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_MoAddUndo1.n):
            jset(Code01_MoAddUndo1.arr, i, Code01_MoAddUndo1.kth(Code01_MoAddUndo1.arr[i]))
            i = jcast('int', (i + 1))
        Code01_MoAddUndo1.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code01_MoAddUndo1.n)))
        Code01_MoAddUndo1.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code01_MoAddUndo1.n, Code01_MoAddUndo1.blen)) - 1)), Code01_MoAddUndo1.blen)))
        i = jcast('int', 1)
        while (i <= Code01_MoAddUndo1.n):
            Code01_MoAddUndo1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code01_MoAddUndo1.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_MoAddUndo1.bnum):
            jset(Code01_MoAddUndo1.br, i, jstatic('Math', 'min', jcast('int', (i * Code01_MoAddUndo1.blen)), Code01_MoAddUndo1.n))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code01_MoAddUndo1.query, 1, jcast('int', jadd(Code01_MoAddUndo1.m, 1)), Code01_MoAddUndo1.QueryCmp())

    @staticmethod
    def main(args):
        in_ = Code01_MoAddUndo1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_MoAddUndo1.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_MoAddUndo1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_MoAddUndo1.n):
            jset(Code01_MoAddUndo1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_MoAddUndo1.m):
            jset(Code01_MoAddUndo1.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code01_MoAddUndo1.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code01_MoAddUndo1.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code01_MoAddUndo1.prepare()
        Code01_MoAddUndo1.compute()
        i = jcast('int', 1)
        while (i <= Code01_MoAddUndo1.m):
            jcall(out, 'println', Code01_MoAddUndo1.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_11 := self), (_java_key_12 := 'ptr'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]])

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
            raise TypeError("No matching overload for Code01_MoAddUndo1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_MoAddUndo1.MAXN = jcast('int', 100001)
Code01_MoAddUndo1.MAXB = jcast('int', 401)
Code01_MoAddUndo1.n = jcast('int', 0)
Code01_MoAddUndo1.m = jcast('int', 0)
Code01_MoAddUndo1.arr = jarray('int', [Code01_MoAddUndo1.MAXN])
Code01_MoAddUndo1.query = jarray('int', [Code01_MoAddUndo1.MAXN, 3])
Code01_MoAddUndo1.sorted = jarray('int', [Code01_MoAddUndo1.MAXN])
Code01_MoAddUndo1.cntv = jcast('int', 0)
Code01_MoAddUndo1.blen = jcast('int', 0)
Code01_MoAddUndo1.bnum = jcast('int', 0)
Code01_MoAddUndo1.bi = jarray('int', [Code01_MoAddUndo1.MAXN])
Code01_MoAddUndo1.br = jarray('int', [Code01_MoAddUndo1.MAXB])
Code01_MoAddUndo1.cnt = jarray('int', [Code01_MoAddUndo1.MAXN])
Code01_MoAddUndo1.curAns = jcast('long', 0)
Code01_MoAddUndo1.ans = jarray('long', [Code01_MoAddUndo1.MAXN])

if __name__ == '__main__':
    Code01_MoAddUndo1.main([])
