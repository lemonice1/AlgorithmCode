# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 简单的询问，Python版
# 给定一个长度为n的数组arr，下标从1到n
# 函数get(l, r, x) = arr[l..r]范围上，数组x出现的次数
# 接下来有q条查询，格式如下
# 查询 l1 r1 l2 r2 : 每种x都算，打印 get(l1, r1, x) * get(l2, r2, x) 的累加和
# 1 <= n、q <= 5 * 10^4
# 1 <= arr[i] <= n
# 测试链接 : https://www.luogu.com.cn/problem/P5268
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_SimpleQuery1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'q': 'q', 'cntq': 'cntq', 'arr': 'arr', 'query': 'query', 'bi': 'bi', 'cnt1': 'cnt1', 'cnt2': 'cnt2', 'curAns': 'curAns', 'ans': 'ans'}
    MAXN = 0
    n = 0
    q = 0
    cntq = 0
    arr = None
    # 查询任务，siz1、siz2、op、id
    query = None
    bi = None
    # cnt1 : arr[1..siz1]范围内每种数字出现的次数
    # cnt2 : arr[1..siz2]范围内每种数字出现的次数
    cnt1 = None
    cnt2 = None
    curAns = 0
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code02_SimpleQuery1.bi[a[0]] != Code02_SimpleQuery1.bi[b[0]]):
                return jcast('int', jcast('int', (Code02_SimpleQuery1.bi[a[0]] - Code02_SimpleQuery1.bi[b[0]])))
            if (jcast('int', (Code02_SimpleQuery1.bi[a[0]] & 1)) == 1):
                return jcast('int', jcast('int', (a[1] - b[1])))
            else:
                return jcast('int', jcast('int', (b[1] - a[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def addQuery(siz1, siz2, op, id):
        siz1 = jcast('int', siz1)
        siz2 = jcast('int', siz2)
        op = jcast('int', op)
        id = jcast('int', id)
        jset(Code02_SimpleQuery1.query[((_java_obj_1 := Code02_SimpleQuery1), (_java_key_2 := 'cntq'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]], 0, siz1)
        jset(Code02_SimpleQuery1.query[Code02_SimpleQuery1.cntq], 1, siz2)
        jset(Code02_SimpleQuery1.query[Code02_SimpleQuery1.cntq], 2, op)
        jset(Code02_SimpleQuery1.query[Code02_SimpleQuery1.cntq], 3, id)

    # win1和win2不代表一段区间，而是代表两个独立区域各自去覆盖arr
    # win1 = 0，win2 = 0，表示两个覆盖区域一开始都没有数字
    # job1和job2也不代表区间，而是代表两个区域各自要覆盖多大
    @staticmethod
    def compute():
        win1 = jcast('int', 0)
        win2 = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code02_SimpleQuery1.cntq):
            job1 = jcast('int', Code02_SimpleQuery1.query[i][0])
            job2 = jcast('int', Code02_SimpleQuery1.query[i][1])
            op = jcast('int', Code02_SimpleQuery1.query[i][2])
            id = jcast('int', Code02_SimpleQuery1.query[i][3])
            while (win1 < job1):
                win1 = jcast('int', (win1 + 1))
                ((_java_obj_4 := Code02_SimpleQuery1.cnt1), (_java_key_5 := Code02_SimpleQuery1.arr[win1]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]
                Code02_SimpleQuery1.curAns = jcast('long', jcast('long', jadd(Code02_SimpleQuery1.curAns, Code02_SimpleQuery1.cnt2[Code02_SimpleQuery1.arr[win1]])))
            while (win1 > job1):
                ((_java_obj_7 := Code02_SimpleQuery1.cnt1), (_java_key_8 := Code02_SimpleQuery1.arr[win1]), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]
                Code02_SimpleQuery1.curAns = jcast('long', jcast('long', (Code02_SimpleQuery1.curAns - Code02_SimpleQuery1.cnt2[Code02_SimpleQuery1.arr[win1]])))
                win1 = jcast('int', (win1 - 1))
            while (win2 < job2):
                win2 = jcast('int', (win2 + 1))
                ((_java_obj_10 := Code02_SimpleQuery1.cnt2), (_java_key_11 := Code02_SimpleQuery1.arr[win2]), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]
                Code02_SimpleQuery1.curAns = jcast('long', jcast('long', jadd(Code02_SimpleQuery1.curAns, Code02_SimpleQuery1.cnt1[Code02_SimpleQuery1.arr[win2]])))
            while (win2 > job2):
                ((_java_obj_13 := Code02_SimpleQuery1.cnt2), (_java_key_14 := Code02_SimpleQuery1.arr[win2]), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (-1)))), _java_old_15)[4]
                Code02_SimpleQuery1.curAns = jcast('long', jcast('long', (Code02_SimpleQuery1.curAns - Code02_SimpleQuery1.cnt1[Code02_SimpleQuery1.arr[win2]])))
                win2 = jcast('int', (win2 - 1))
            Code02_SimpleQuery1.ans[id] = jcast('long', jcast('long', jadd(Code02_SimpleQuery1.ans[id], jcast('long', (Code02_SimpleQuery1.curAns * op)))))
            i = jcast('int', (i + 1))

    @staticmethod
    def prepare():
        blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code02_SimpleQuery1.n)))
        i = jcast('int', 1)
        while (i <= Code02_SimpleQuery1.n):
            Code02_SimpleQuery1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_SimpleQuery1.cntq):
            if (Code02_SimpleQuery1.query[i][0] > Code02_SimpleQuery1.query[i][1]):
                tmp = jcast('int', Code02_SimpleQuery1.query[i][0])
                jset(Code02_SimpleQuery1.query[i], 0, Code02_SimpleQuery1.query[i][1])
                jset(Code02_SimpleQuery1.query[i], 1, tmp)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_SimpleQuery1.query, 1, jcast('int', jadd(Code02_SimpleQuery1.cntq, 1)), Code02_SimpleQuery1.QueryCmp())

    @staticmethod
    def main(args):
        in_ = Code02_SimpleQuery1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_SimpleQuery1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_SimpleQuery1.n):
            jset(Code02_SimpleQuery1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code02_SimpleQuery1.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        l1 = 0
        r1 = 0
        l2 = 0
        r2 = 0
        while (i <= Code02_SimpleQuery1.q):
            l1 = jcast('int', jcall(in_, 'nextInt'))
            r1 = jcast('int', jcall(in_, 'nextInt'))
            l2 = jcast('int', jcall(in_, 'nextInt'))
            r2 = jcast('int', jcall(in_, 'nextInt'))
            Code02_SimpleQuery1.addQuery(r1, r2, 1, i)
            Code02_SimpleQuery1.addQuery(r1, jcast('int', (l2 - 1)), jcast('int', (-1)), i)
            Code02_SimpleQuery1.addQuery(jcast('int', (l1 - 1)), r2, jcast('int', (-1)), i)
            Code02_SimpleQuery1.addQuery(jcast('int', (l1 - 1)), jcast('int', (l2 - 1)), 1, i)
            i = jcast('int', (i + 1))
        Code02_SimpleQuery1.prepare()
        Code02_SimpleQuery1.compute()
        i = jcast('int', 1)
        while (i <= Code02_SimpleQuery1.q):
            jcall(out, 'println', Code02_SimpleQuery1.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_16 := self), (_java_key_17 := 'ptr'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))), _java_old_18)[4]])

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
            raise TypeError("No matching overload for Code02_SimpleQuery1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_SimpleQuery1.MAXN = jcast('int', 50001)
Code02_SimpleQuery1.n = jcast('int', 0)
Code02_SimpleQuery1.q = jcast('int', 0)
Code02_SimpleQuery1.cntq = jcast('int', 0)
Code02_SimpleQuery1.arr = jarray('int', [Code02_SimpleQuery1.MAXN])
Code02_SimpleQuery1.query = jarray('int', [jcast('int', (Code02_SimpleQuery1.MAXN << (2 & 31))), 4])
Code02_SimpleQuery1.bi = jarray('int', [Code02_SimpleQuery1.MAXN])
Code02_SimpleQuery1.cnt1 = jarray('int', [Code02_SimpleQuery1.MAXN])
Code02_SimpleQuery1.cnt2 = jarray('int', [Code02_SimpleQuery1.MAXN])
Code02_SimpleQuery1.curAns = jcast('long', 0)
Code02_SimpleQuery1.ans = jarray('long', [Code02_SimpleQuery1.MAXN])

if __name__ == '__main__':
    Code02_SimpleQuery1.main([])
