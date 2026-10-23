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

# 蒲公英，Python版
# 给定一个长度为n的数组arr，接下来有m条操作，每条操作格式如下
# 操作 l r : 打印arr[l..r]范围上的众数，如果有多个众数，打印值最小的
# 1 <= n <= 4 * 10^4
# 1 <= m <= 5 * 10^4
# 1 <= 数组中的值 <= 10^9
# 题目要求强制在线，具体规则可以打开测试链接查看
# 测试链接 : https://www.luogu.com.cn/problem/P4168
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Violet1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 's': 's', 'arr': 'arr', 'sortv': 'sortv', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'bl': 'bl', 'br': 'br', 'freq': 'freq', 'mode': 'mode', 'numCnt': 'numCnt'}
    MAXN = 0
    MAXB = 0
    n = 0
    m = 0
    s = 0
    arr = None
    # 数字做离散化
    sortv = None
    blen = 0
    bnum = 0
    bi = None
    bl = None
    br = None
    # freq[i][j]表示前i块中j出现的次数
    freq = None
    # mode[i][j]表示从i块到j块中的众数(最小)
    mode = None
    # 数字的词频统计
    numCnt = None
    @staticmethod
    def lower(num):
        num = jcast('int', num)
        l = jcast('int', 1)
        r = jcast('int', Code03_Violet1.s)
        m = 0
        ans = jcast('int', 0)
        while (l <= r):
            m = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code03_Violet1.sortv[m] >= num):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    @staticmethod
    def getCnt(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        return jcast('int', jcast('int', (Code03_Violet1.freq[r][v] - Code03_Violet1.freq[jcast('int', (l - 1))][v])))

    @staticmethod
    def prepare():
        # 建块
        Code03_Violet1.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code03_Violet1.n)))
        Code03_Violet1.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code03_Violet1.n, Code03_Violet1.blen)) - 1)), Code03_Violet1.blen)))
        i = jcast('int', 1)
        while (i <= Code03_Violet1.n):
            Code03_Violet1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code03_Violet1.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_Violet1.bnum):
            Code03_Violet1.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code03_Violet1.blen)), 1)))
            jset(Code03_Violet1.br, i, jstatic('Math', 'min', jcast('int', (i * Code03_Violet1.blen)), Code03_Violet1.n))
            i = jcast('int', (i + 1))
        # 离散化
        i = jcast('int', 1)
        while (i <= Code03_Violet1.n):
            Code03_Violet1.sortv[i] = jcast('int', Code03_Violet1.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code03_Violet1.sortv, 1, jcast('int', jadd(Code03_Violet1.n, 1)))
        Code03_Violet1.s = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code03_Violet1.n):
            if (Code03_Violet1.sortv[Code03_Violet1.s] != Code03_Violet1.sortv[i]):
                jset(Code03_Violet1.sortv, ((_java_obj_1 := Code03_Violet1), (_java_key_2 := 's'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_Violet1.sortv[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_Violet1.n):
            jset(Code03_Violet1.arr, i, Code03_Violet1.lower(Code03_Violet1.arr[i]))
            i = jcast('int', (i + 1))
        # 填好freq
        i = jcast('int', 1)
        while (i <= Code03_Violet1.bnum):
            j = jcast('int', Code03_Violet1.bl[i])
            while (j <= Code03_Violet1.br[i]):
                ((_java_obj_4 := Code03_Violet1.freq[i]), (_java_key_5 := Code03_Violet1.arr[j]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]
                j = jcast('int', (j + 1))
            j = jcast('int', 1)
            while (j <= Code03_Violet1.s):
                ((_java_obj_7 := Code03_Violet1.freq[i]), (_java_key_8 := j), jset(_java_obj_7, _java_key_8, jcast('int', jadd(jget(_java_obj_7, _java_key_8), Code03_Violet1.freq[jcast('int', (i - 1))][j]))))[2]
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        # 填好mode
        i = jcast('int', 1)
        while (i <= Code03_Violet1.bnum):
            j = jcast('int', i)
            while (j <= Code03_Violet1.bnum):
                most = jcast('int', Code03_Violet1.mode[i][jcast('int', (j - 1))])
                mostCnt = jcast('int', Code03_Violet1.getCnt(i, j, most))
                k = jcast('int', Code03_Violet1.bl[j])
                while (k <= Code03_Violet1.br[j]):
                    cur = jcast('int', Code03_Violet1.arr[k])
                    curCnt = jcast('int', Code03_Violet1.getCnt(i, j, cur))
                    if ((curCnt > mostCnt) or ((curCnt == mostCnt) and (cur < most))):
                        most = jcast('int', cur)
                        mostCnt = jcast('int', curCnt)
                    k = jcast('int', (k + 1))
                jset(Code03_Violet1.mode[i], j, most)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        most = jcast('int', 0)
        if (Code03_Violet1.bi[l] == Code03_Violet1.bi[r]):
            i = jcast('int', l)
            while (i <= r):
                ((_java_obj_9 := Code03_Violet1.numCnt), (_java_key_10 := Code03_Violet1.arr[i]), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))), _java_old_11)[4]
                i = jcast('int', (i + 1))
            i = jcast('int', l)
            while (i <= r):
                if ((Code03_Violet1.numCnt[Code03_Violet1.arr[i]] > Code03_Violet1.numCnt[most]) or ((Code03_Violet1.numCnt[Code03_Violet1.arr[i]] == Code03_Violet1.numCnt[most]) and (Code03_Violet1.arr[i] < most))):
                    most = jcast('int', Code03_Violet1.arr[i])
                i = jcast('int', (i + 1))
            i = jcast('int', l)
            while (i <= r):
                jset(Code03_Violet1.numCnt, Code03_Violet1.arr[i], 0)
                i = jcast('int', (i + 1))
        else:
            i = jcast('int', l)
            while (i <= Code03_Violet1.br[Code03_Violet1.bi[l]]):
                ((_java_obj_12 := Code03_Violet1.numCnt), (_java_key_13 := Code03_Violet1.arr[i]), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))), _java_old_14)[4]
                i = jcast('int', (i + 1))
            i = jcast('int', Code03_Violet1.bl[Code03_Violet1.bi[r]])
            while (i <= r):
                ((_java_obj_15 := Code03_Violet1.numCnt), (_java_key_16 := Code03_Violet1.arr[i]), (_java_old_17 := jget(_java_obj_15, _java_key_16)), jset(_java_obj_15, _java_key_16, jcast('int', (_java_old_17 + (1)))), _java_old_17)[4]
                i = jcast('int', (i + 1))
            most = jcast('int', Code03_Violet1.mode[jcast('int', jadd(Code03_Violet1.bi[l], 1))][jcast('int', (Code03_Violet1.bi[r] - 1))])
            mostCnt = jcast('int', jcast('int', jadd(Code03_Violet1.getCnt(jcast('int', jadd(Code03_Violet1.bi[l], 1)), jcast('int', (Code03_Violet1.bi[r] - 1)), most), Code03_Violet1.numCnt[most])))
            i = jcast('int', l)
            while (i <= Code03_Violet1.br[Code03_Violet1.bi[l]]):
                cur = jcast('int', Code03_Violet1.arr[i])
                curCnt = jcast('int', jcast('int', jadd(Code03_Violet1.getCnt(jcast('int', jadd(Code03_Violet1.bi[l], 1)), jcast('int', (Code03_Violet1.bi[r] - 1)), cur), Code03_Violet1.numCnt[cur])))
                if ((curCnt > mostCnt) or ((curCnt == mostCnt) and (cur < most))):
                    most = jcast('int', cur)
                    mostCnt = jcast('int', curCnt)
                i = jcast('int', (i + 1))
            i = jcast('int', Code03_Violet1.bl[Code03_Violet1.bi[r]])
            while (i <= r):
                cur = jcast('int', Code03_Violet1.arr[i])
                curCnt = jcast('int', jcast('int', jadd(Code03_Violet1.getCnt(jcast('int', jadd(Code03_Violet1.bi[l], 1)), jcast('int', (Code03_Violet1.bi[r] - 1)), cur), Code03_Violet1.numCnt[cur])))
                if ((curCnt > mostCnt) or ((curCnt == mostCnt) and (cur < most))):
                    most = jcast('int', cur)
                    mostCnt = jcast('int', curCnt)
                i = jcast('int', (i + 1))
            i = jcast('int', l)
            while (i <= Code03_Violet1.br[Code03_Violet1.bi[l]]):
                jset(Code03_Violet1.numCnt, Code03_Violet1.arr[i], 0)
                i = jcast('int', (i + 1))
            i = jcast('int', Code03_Violet1.bl[Code03_Violet1.bi[r]])
            while (i <= r):
                jset(Code03_Violet1.numCnt, Code03_Violet1.arr[i], 0)
                i = jcast('int', (i + 1))
        return jcast('int', Code03_Violet1.sortv[most])

    @staticmethod
    def main(args):
        in_ = Code03_Violet1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_Violet1.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_Violet1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_Violet1.n):
            jset(Code03_Violet1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code03_Violet1.prepare()
        i = jcast('int', 1)
        a = 0
        b = 0
        l = 0
        r = 0
        lastAns = jcast('int', 0)
        while (i <= Code03_Violet1.m):
            a = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', (jcast('int', jadd(jcall(in_, 'nextInt'), lastAns)) - 1)), Code03_Violet1.n)), 1)))
            b = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', (jcast('int', jadd(jcall(in_, 'nextInt'), lastAns)) - 1)), Code03_Violet1.n)), 1)))
            l = jcast('int', jstatic('Math', 'min', a, b))
            r = jcast('int', jstatic('Math', 'max', a, b))
            lastAns = jcast('int', Code03_Violet1.query(l, r))
            jcall(out, 'println', lastAns)
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
            return jcast('int', self.buffer[((_java_obj_18 := self), (_java_key_19 := 'ptr'), (_java_old_20 := jget(_java_obj_18, _java_key_19)), jset(_java_obj_18, _java_key_19, jcast('int', (_java_old_20 + (1)))), _java_old_20)[4]])

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
            raise TypeError("No matching overload for Code03_Violet1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Violet1.MAXN = jcast('int', 40001)
Code03_Violet1.MAXB = jcast('int', 201)
Code03_Violet1.n = jcast('int', 0)
Code03_Violet1.m = jcast('int', 0)
Code03_Violet1.s = jcast('int', 0)
Code03_Violet1.arr = jarray('int', [Code03_Violet1.MAXN])
Code03_Violet1.sortv = jarray('int', [Code03_Violet1.MAXN])
Code03_Violet1.blen = jcast('int', 0)
Code03_Violet1.bnum = jcast('int', 0)
Code03_Violet1.bi = jarray('int', [Code03_Violet1.MAXN])
Code03_Violet1.bl = jarray('int', [Code03_Violet1.MAXB])
Code03_Violet1.br = jarray('int', [Code03_Violet1.MAXB])
Code03_Violet1.freq = jarray('int', [Code03_Violet1.MAXB, Code03_Violet1.MAXN])
Code03_Violet1.mode = jarray('int', [Code03_Violet1.MAXB, Code03_Violet1.MAXB])
Code03_Violet1.numCnt = jarray('int', [Code03_Violet1.MAXN])

if __name__ == '__main__':
    Code03_Violet1.main([])
