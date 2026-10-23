# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 由乃的玉米田，Python版
# 给定一个长度为n的数组arr，接下来有m条查询，查询格式如下
# 查询 1 l r x : 打印arr[l..r]范围上能否选出两个数，减的结果为x
# 查询 2 l r x : 打印arr[l..r]范围上能否选出两个数，加的结果为x
# 查询 3 l r x : 打印arr[l..r]范围上能否选出两个数，乘的结果为x
# 查询 4 l r x : 打印arr[l..r]范围上能否选出两个数，除的结果为x，并且没有余数
# 选出的这两个数可以是同一个位置的数，答案如果为是，打印 "yuno"，否则打印 "yumi"
# 1 <= 所有数据 <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P5355
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code08_YnoiCornfield2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'blen': 'blen', 'arr': 'arr', 'bi': 'bi', 'query': 'query', 'cntq': 'cntq', 'headq': 'headq', 'nextq': 'nextq', 'ql': 'ql', 'qr': 'qr', 'qid': 'qid', 'cnts': 'cnts', 'cnt': 'cnt', 'bitSet1': 'bitSet1', 'bitSet2': 'bitSet2', 'pre': 'pre', 'dp': 'dp', 'ans': 'ans'}
    class BitSet:
        __java_fields__ = {'len': 'len', 'status': 'status'}
        # len：实例字段，在构造函数中初始化。
        # status：实例字段，在构造函数中初始化。
        def _java_init_0(self, siz):
            siz = jcast('int', siz)
            self.len = jcast('int', jcast('int', (jcast('int', jadd(siz, 63)) >> (6 & 31))))
            self.status = jarray('long', [self.len])

        def setOne(self, bit):
            bit = jcast('int', bit)
            self.status[jcast('int', (bit >> (6 & 31)))] = jcast('long', jcast('long', (self.status[jcast('int', (bit >> (6 & 31)))] | jcast('long', (1 << (jcast('int', (bit & 63)) & 63))))))

        def setZero(self, bit):
            bit = jcast('int', bit)
            self.status[jcast('int', (bit >> (6 & 31)))] = jcast('long', jcast('long', (self.status[jcast('int', (bit >> (6 & 31)))] & jcast('long', (~jcast('long', (1 << (jcast('int', (bit & 63)) & 63))))))))

        def getStatus(self, bit):
            bit = jcast('int', bit)
            return jcast('boolean', (jcast('long', (jcast('long', (self.status[jcast('int', (bit >> (6 & 31)))] >> (jcast('int', (bit & 63)) & 63))) & 1)) != 0))

        # 检查 自己 & other右移k位 是否有1存在
        def andOtherMoveRight(self, other, move):
            move = jcast('int', move)
            ws = jcast('int', jcast('int', (move >> (6 & 31))))
            bs = jcast('int', jcast('int', (move & 63)))
            i = jcast('int', 0)
            while (i < self.len):
                try:
                    src = jcast('int', jcast('int', jadd(i, ws)))
                    if (src >= self.len):
                        raise JBreak(None)
                    shifted = jcast('long', jcast('long', jushr(jget(other, 'status')[src], bs, 64)))
                    if ((bs != 0) and (jcast('int', jadd(src, 1)) < self.len)):
                        shifted = jcast('long', jcast('long', (shifted | jcast('long', (jget(other, 'status')[jcast('int', jadd(src, 1))] << (jcast('int', (64 - bs)) & 63))))))
                    if (jcast('long', (self.status[i] & shifted)) != 0):
                        return jcast('boolean', True)
                except JContinue as _java_control_1:
                    if _java_control_1.label not in (None,):
                        raise
                except JBreak as _java_control_1:
                    if _java_control_1.label not in (None,):
                        raise
                    break
                i = jcast('int', (i + 1))
            return jcast('boolean', False)

        def __init__(self, *args, _java_ctor=None):
            self.len = jcast('int', 0)
            self.status = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code08_YnoiCornfield2.BitSet.BitSet")


    MAXN = 0
    MAXV = 0
    MAXB = 0
    n = 0
    m = 0
    blen = 0
    arr = None
    bi = None
    # 普通查询，l、r、x、op、id
    query = None
    cntq = 0
    # 特别查询，x的问题列表 : l、r、id
    headq = None
    nextq = None
    ql = None
    qr = None
    qid = None
    cnts = 0
    # 数字出现的词频
    cnt = None
    bitSet1 = None
    bitSet2 = None
    # 特别查询的dp过程
    pre = None
    dp = None
    ans = None
    @staticmethod
    def addSpecial(x, l, r, id):
        x = jcast('int', x)
        l = jcast('int', l)
        r = jcast('int', r)
        id = jcast('int', id)
        jset(Code08_YnoiCornfield2.nextq, ((_java_obj_2 := Code08_YnoiCornfield2), (_java_key_3 := 'cnts'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))))[3], Code08_YnoiCornfield2.headq[x])
        Code08_YnoiCornfield2.headq[x] = jcast('int', Code08_YnoiCornfield2.cnts)
        Code08_YnoiCornfield2.ql[Code08_YnoiCornfield2.cnts] = jcast('int', l)
        Code08_YnoiCornfield2.qr[Code08_YnoiCornfield2.cnts] = jcast('int', r)
        Code08_YnoiCornfield2.qid[Code08_YnoiCornfield2.cnts] = jcast('int', id)

    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code08_YnoiCornfield2.bi[a[0]] != Code08_YnoiCornfield2.bi[b[0]]):
                return jcast('int', jcast('int', (Code08_YnoiCornfield2.bi[a[0]] - Code08_YnoiCornfield2.bi[b[0]])))
            if (jcast('int', (Code08_YnoiCornfield2.bi[a[0]] & 1)) == 1):
                return jcast('int', jcast('int', (a[1] - b[1])))
            else:
                return jcast('int', jcast('int', (b[1] - a[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def add(x):
        x = jcast('int', x)
        Code08_YnoiCornfield2.cnt[x] = jcast('int', (Code08_YnoiCornfield2.cnt[x] + 1))
        if (Code08_YnoiCornfield2.cnt[x] == 1):
            jcall(Code08_YnoiCornfield2.bitSet1, 'setOne', x)
            jcall(Code08_YnoiCornfield2.bitSet2, 'setOne', jcast('int', (Code08_YnoiCornfield2.MAXV - x)))

    @staticmethod
    def del_(x):
        x = jcast('int', x)
        Code08_YnoiCornfield2.cnt[x] = jcast('int', (Code08_YnoiCornfield2.cnt[x] - 1))
        if (Code08_YnoiCornfield2.cnt[x] == 0):
            jcall(Code08_YnoiCornfield2.bitSet1, 'setZero', x)
            jcall(Code08_YnoiCornfield2.bitSet2, 'setZero', jcast('int', (Code08_YnoiCornfield2.MAXV - x)))

    @staticmethod
    def calc(op, x):
        op = jcast('int', op)
        x = jcast('int', x)
        if (op == 1):
            return jcast('boolean', jcall(Code08_YnoiCornfield2.bitSet1, 'andOtherMoveRight', Code08_YnoiCornfield2.bitSet1, x))
        else:
            if (op == 2):
                return jcast('boolean', jcall(Code08_YnoiCornfield2.bitSet1, 'andOtherMoveRight', Code08_YnoiCornfield2.bitSet2, jcast('int', (Code08_YnoiCornfield2.MAXV - x))))
            else:
                if (op == 3):
                    f = jcast('int', 1)
                    while (jcast('int', (f * f)) <= x):
                        if (((jcast('int', jmod(x, f)) == 0) and jcall(Code08_YnoiCornfield2.bitSet1, 'getStatus', f)) and jcall(Code08_YnoiCornfield2.bitSet1, 'getStatus', jcast('int', jdiv(x, f)))):
                            return jcast('boolean', True)
                        f = jcast('int', (f + 1))
                    return jcast('boolean', False)
                else:
                    if (x >= 1):
                        i = jcast('int', 1)
                        while (jcast('int', (i * x)) <= Code08_YnoiCornfield2.MAXV):
                            if (jcall(Code08_YnoiCornfield2.bitSet1, 'getStatus', i) and jcall(Code08_YnoiCornfield2.bitSet1, 'getStatus', jcast('int', (i * x)))):
                                return jcast('boolean', True)
                            i = jcast('int', (i + 1))
                    return jcast('boolean', False)

    @staticmethod
    def compute():
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code08_YnoiCornfield2.cntq):
            jobl = jcast('int', Code08_YnoiCornfield2.query[i][0])
            jobr = jcast('int', Code08_YnoiCornfield2.query[i][1])
            jobx = jcast('int', Code08_YnoiCornfield2.query[i][2])
            op = jcast('int', Code08_YnoiCornfield2.query[i][3])
            id = jcast('int', Code08_YnoiCornfield2.query[i][4])
            while (winl > jobl):
                Code08_YnoiCornfield2.add(Code08_YnoiCornfield2.arr[(winl := jcast('int', (winl + (-1))))])
            while (winr < jobr):
                Code08_YnoiCornfield2.add(Code08_YnoiCornfield2.arr[(winr := jcast('int', (winr + (1))))])
            while (winl < jobl):
                Code08_YnoiCornfield2.del_(Code08_YnoiCornfield2.arr[((_java_old_5 := winl), (winl := jcast('int', (winl + (1)))), _java_old_5)[2]])
            while (winr > jobr):
                Code08_YnoiCornfield2.del_(Code08_YnoiCornfield2.arr[((_java_old_6 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_6)[2]])
            jset(Code08_YnoiCornfield2.ans, id, Code08_YnoiCornfield2.calc(op, jobx))
            i = jcast('int', (i + 1))

    @staticmethod
    def special():
        x = jcast('int', 1)
        while (x < Code08_YnoiCornfield2.blen):
            if (Code08_YnoiCornfield2.headq[x] != 0):
                jstatic('Arrays', 'fill', Code08_YnoiCornfield2.pre, 0)
                jstatic('Arrays', 'fill', Code08_YnoiCornfield2.dp, 0)
                i = jcast('int', 1)
                while (i <= Code08_YnoiCornfield2.n):
                    v = jcast('int', Code08_YnoiCornfield2.arr[i])
                    Code08_YnoiCornfield2.pre[v] = jcast('int', i)
                    Code08_YnoiCornfield2.dp[i] = jcast('int', Code08_YnoiCornfield2.dp[jcast('int', (i - 1))])
                    if (jcast('int', (v * x)) <= Code08_YnoiCornfield2.MAXV):
                        jset(Code08_YnoiCornfield2.dp, i, jstatic('Math', 'max', Code08_YnoiCornfield2.dp[i], Code08_YnoiCornfield2.pre[jcast('int', (v * x))]))
                    if (jcast('int', jmod(v, x)) == 0):
                        jset(Code08_YnoiCornfield2.dp, i, jstatic('Math', 'max', Code08_YnoiCornfield2.dp[i], Code08_YnoiCornfield2.pre[jcast('int', jdiv(v, x))]))
                    i = jcast('int', (i + 1))
                q = jcast('int', Code08_YnoiCornfield2.headq[x])
                while (q > 0):
                    l = jcast('int', Code08_YnoiCornfield2.ql[q])
                    r = jcast('int', Code08_YnoiCornfield2.qr[q])
                    id = jcast('int', Code08_YnoiCornfield2.qid[q])
                    Code08_YnoiCornfield2.ans[id] = jcast('boolean', (l <= Code08_YnoiCornfield2.dp[r]))
                    q = jcast('int', Code08_YnoiCornfield2.nextq[q])
            x = jcast('int', (x + 1))

    @staticmethod
    def main(args):
        in_ = Code08_YnoiCornfield2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code08_YnoiCornfield2.n = jcast('int', jcall(in_, 'nextInt'))
        Code08_YnoiCornfield2.m = jcast('int', jcall(in_, 'nextInt'))
        Code08_YnoiCornfield2.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code08_YnoiCornfield2.MAXV)))
        i = jcast('int', 1)
        while (i <= Code08_YnoiCornfield2.n):
            Code08_YnoiCornfield2.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code08_YnoiCornfield2.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code08_YnoiCornfield2.n):
            jset(Code08_YnoiCornfield2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        l = 0
        r = 0
        x = 0
        while (i <= Code08_YnoiCornfield2.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            l = jcast('int', jcall(in_, 'nextInt'))
            r = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            if ((op == 4) and (x < Code08_YnoiCornfield2.blen)):
                Code08_YnoiCornfield2.addSpecial(x, l, r, i)
            else:
                jset(Code08_YnoiCornfield2.query[((_java_obj_7 := Code08_YnoiCornfield2), (_java_key_8 := 'cntq'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]], 0, l)
                jset(Code08_YnoiCornfield2.query[Code08_YnoiCornfield2.cntq], 1, r)
                jset(Code08_YnoiCornfield2.query[Code08_YnoiCornfield2.cntq], 2, x)
                jset(Code08_YnoiCornfield2.query[Code08_YnoiCornfield2.cntq], 3, op)
                jset(Code08_YnoiCornfield2.query[Code08_YnoiCornfield2.cntq], 4, i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code08_YnoiCornfield2.query, 1, jcast('int', jadd(Code08_YnoiCornfield2.cntq, 1)), Code08_YnoiCornfield2.QueryCmp())
        Code08_YnoiCornfield2.compute()
        Code08_YnoiCornfield2.special()
        i = jcast('int', 1)
        while (i <= Code08_YnoiCornfield2.m):
            if Code08_YnoiCornfield2.ans[i]:
                jcall(out, 'println', 'yuno')
            else:
                jcall(out, 'println', 'yumi')
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
            return jcast('int', self.buffer[((_java_obj_10 := self), (_java_key_11 := 'ptr'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]])

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
            raise TypeError("No matching overload for Code08_YnoiCornfield2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code08_YnoiCornfield2.MAXN = jcast('int', 100001)
Code08_YnoiCornfield2.MAXV = jcast('int', 100000)
Code08_YnoiCornfield2.MAXB = jcast('int', 401)
Code08_YnoiCornfield2.n = jcast('int', 0)
Code08_YnoiCornfield2.m = jcast('int', 0)
Code08_YnoiCornfield2.blen = jcast('int', 0)
Code08_YnoiCornfield2.arr = jarray('int', [Code08_YnoiCornfield2.MAXN])
Code08_YnoiCornfield2.bi = jarray('int', [Code08_YnoiCornfield2.MAXN])
Code08_YnoiCornfield2.query = jarray('int', [Code08_YnoiCornfield2.MAXN, 5])
Code08_YnoiCornfield2.cntq = jcast('int', 0)
Code08_YnoiCornfield2.headq = jarray('int', [Code08_YnoiCornfield2.MAXB])
Code08_YnoiCornfield2.nextq = jarray('int', [Code08_YnoiCornfield2.MAXN])
Code08_YnoiCornfield2.ql = jarray('int', [Code08_YnoiCornfield2.MAXN])
Code08_YnoiCornfield2.qr = jarray('int', [Code08_YnoiCornfield2.MAXN])
Code08_YnoiCornfield2.qid = jarray('int', [Code08_YnoiCornfield2.MAXN])
Code08_YnoiCornfield2.cnts = jcast('int', 0)
Code08_YnoiCornfield2.cnt = jarray('int', [Code08_YnoiCornfield2.MAXN])
Code08_YnoiCornfield2.bitSet1 = Code08_YnoiCornfield2.BitSet(Code08_YnoiCornfield2.MAXN, _java_ctor=0)
Code08_YnoiCornfield2.bitSet2 = Code08_YnoiCornfield2.BitSet(Code08_YnoiCornfield2.MAXN, _java_ctor=0)
Code08_YnoiCornfield2.pre = jarray('int', [Code08_YnoiCornfield2.MAXN])
Code08_YnoiCornfield2.dp = jarray('int', [Code08_YnoiCornfield2.MAXN])
Code08_YnoiCornfield2.ans = jarray('boolean', [Code08_YnoiCornfield2.MAXN])

if __name__ == '__main__':
    Code08_YnoiCornfield2.main([])
