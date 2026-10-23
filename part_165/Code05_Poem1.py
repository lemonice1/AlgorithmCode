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

# 作诗，Python版
# 给定一个长度为n的数组arr，接下来有m条操作，每条操作格式如下
# 操作 l r : 打印arr[l..r]范围上，有多少个数出现正偶数次
# 1 <= 所有数值 <= 10^5
# 题目要求强制在线，具体规则可以打开测试链接查看
# 测试链接 : https://www.luogu.com.cn/problem/P4135
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Poem1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'c': 'c', 'm': 'm', 'arr': 'arr', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'bl': 'bl', 'br': 'br', 'freq': 'freq', 'even': 'even', 'numCnt': 'numCnt'}
    MAXN = 0
    MAXB = 0
    n = 0
    c = 0
    m = 0
    arr = None
    blen = 0
    bnum = 0
    bi = None
    bl = None
    br = None
    # freq[i][j]表示前i块中j出现的次数
    freq = None
    # even[i][j]表示从第i块到第j块，有多少个数出现正偶数次
    even = None
    # 数字词频统计
    numCnt = None
    # 返回从l块到r块，数字v的次数
    @staticmethod
    def getCnt(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        return jcast('int', jcast('int', (Code05_Poem1.freq[r][v] - Code05_Poem1.freq[jcast('int', (l - 1))][v])))

    # 某种数的之前词频是pre，现在如果词频加1
    # 返回 出现正偶数次的数字个数 的变化量
    @staticmethod
    def delta(pre):
        pre = jcast('int', pre)
        if (pre == 0):
            return jcast('int', 0)
        if (jcast('int', (pre & 1)) == 0):
            return jcast('int', jcast('int', (-1)))
        return jcast('int', 1)

    @staticmethod
    def prepare():
        Code05_Poem1.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code05_Poem1.n)))
        Code05_Poem1.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code05_Poem1.n, Code05_Poem1.blen)) - 1)), Code05_Poem1.blen)))
        i = jcast('int', 1)
        while (i <= Code05_Poem1.n):
            Code05_Poem1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code05_Poem1.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Poem1.bnum):
            Code05_Poem1.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code05_Poem1.blen)), 1)))
            jset(Code05_Poem1.br, i, jstatic('Math', 'min', jcast('int', (i * Code05_Poem1.blen)), Code05_Poem1.n))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Poem1.bnum):
            j = jcast('int', Code05_Poem1.bl[i])
            while (j <= Code05_Poem1.br[i]):
                ((_java_obj_1 := Code05_Poem1.freq[i]), (_java_key_2 := Code05_Poem1.arr[j]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
                j = jcast('int', (j + 1))
            j = jcast('int', 1)
            while (j <= Code05_Poem1.c):
                ((_java_obj_4 := Code05_Poem1.freq[i]), (_java_key_5 := j), jset(_java_obj_4, _java_key_5, jcast('int', jadd(jget(_java_obj_4, _java_key_5), Code05_Poem1.freq[jcast('int', (i - 1))][j]))))[2]
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_Poem1.bnum):
            j = jcast('int', i)
            while (j <= Code05_Poem1.bnum):
                jset(Code05_Poem1.even[i], j, Code05_Poem1.even[i][jcast('int', (j - 1))])
                k = jcast('int', Code05_Poem1.bl[j])
                while (k <= Code05_Poem1.br[j]):
                    ((_java_obj_6 := Code05_Poem1.even[i]), (_java_key_7 := j), jset(_java_obj_6, _java_key_7, jcast('int', jadd(jget(_java_obj_6, _java_key_7), Code05_Poem1.delta(Code05_Poem1.numCnt[Code05_Poem1.arr[k]])))))[2]
                    ((_java_obj_8 := Code05_Poem1.numCnt), (_java_key_9 := Code05_Poem1.arr[k]), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))), _java_old_10)[4]
                    k = jcast('int', (k + 1))
                j = jcast('int', (j + 1))
            j = jcast('int', 1)
            while (j <= Code05_Poem1.c):
                Code05_Poem1.numCnt[j] = jcast('int', 0)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        ans = jcast('int', 0)
        if (Code05_Poem1.bi[l] == Code05_Poem1.bi[r]):
            i = jcast('int', l)
            while (i <= r):
                ans = jcast('int', jcast('int', jadd(ans, Code05_Poem1.delta(Code05_Poem1.numCnt[Code05_Poem1.arr[i]]))))
                ((_java_obj_11 := Code05_Poem1.numCnt), (_java_key_12 := Code05_Poem1.arr[i]), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]
                i = jcast('int', (i + 1))
            i = jcast('int', l)
            while (i <= r):
                jset(Code05_Poem1.numCnt, Code05_Poem1.arr[i], 0)
                i = jcast('int', (i + 1))
        else:
            ans = jcast('int', Code05_Poem1.even[jcast('int', jadd(Code05_Poem1.bi[l], 1))][jcast('int', (Code05_Poem1.bi[r] - 1))])
            i = jcast('int', l)
            while (i <= Code05_Poem1.br[Code05_Poem1.bi[l]]):
                ans = jcast('int', jcast('int', jadd(ans, Code05_Poem1.delta(jcast('int', jadd(Code05_Poem1.getCnt(jcast('int', jadd(Code05_Poem1.bi[l], 1)), jcast('int', (Code05_Poem1.bi[r] - 1)), Code05_Poem1.arr[i]), Code05_Poem1.numCnt[Code05_Poem1.arr[i]]))))))
                ((_java_obj_14 := Code05_Poem1.numCnt), (_java_key_15 := Code05_Poem1.arr[i]), (_java_old_16 := jget(_java_obj_14, _java_key_15)), jset(_java_obj_14, _java_key_15, jcast('int', (_java_old_16 + (1)))), _java_old_16)[4]
                i = jcast('int', (i + 1))
            i = jcast('int', Code05_Poem1.bl[Code05_Poem1.bi[r]])
            while (i <= r):
                ans = jcast('int', jcast('int', jadd(ans, Code05_Poem1.delta(jcast('int', jadd(Code05_Poem1.getCnt(jcast('int', jadd(Code05_Poem1.bi[l], 1)), jcast('int', (Code05_Poem1.bi[r] - 1)), Code05_Poem1.arr[i]), Code05_Poem1.numCnt[Code05_Poem1.arr[i]]))))))
                ((_java_obj_17 := Code05_Poem1.numCnt), (_java_key_18 := Code05_Poem1.arr[i]), (_java_old_19 := jget(_java_obj_17, _java_key_18)), jset(_java_obj_17, _java_key_18, jcast('int', (_java_old_19 + (1)))), _java_old_19)[4]
                i = jcast('int', (i + 1))
            i = jcast('int', l)
            while (i <= Code05_Poem1.br[Code05_Poem1.bi[l]]):
                jset(Code05_Poem1.numCnt, Code05_Poem1.arr[i], 0)
                i = jcast('int', (i + 1))
            i = jcast('int', Code05_Poem1.bl[Code05_Poem1.bi[r]])
            while (i <= r):
                jset(Code05_Poem1.numCnt, Code05_Poem1.arr[i], 0)
                i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code05_Poem1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_Poem1.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_Poem1.c = jcast('int', jcall(in_, 'nextInt'))
        Code05_Poem1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_Poem1.n):
            jset(Code05_Poem1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code05_Poem1.prepare()
        i = jcast('int', 1)
        a = 0
        b = 0
        l = 0
        r = 0
        lastAns = jcast('int', 0)
        while (i <= Code05_Poem1.m):
            a = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', jadd(jcall(in_, 'nextInt'), lastAns)), Code05_Poem1.n)), 1)))
            b = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', jadd(jcall(in_, 'nextInt'), lastAns)), Code05_Poem1.n)), 1)))
            l = jcast('int', jstatic('Math', 'min', a, b))
            r = jcast('int', jstatic('Math', 'max', a, b))
            lastAns = jcast('int', Code05_Poem1.query(l, r))
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
            return jcast('int', self.buffer[((_java_obj_20 := self), (_java_key_21 := 'ptr'), (_java_old_22 := jget(_java_obj_20, _java_key_21)), jset(_java_obj_20, _java_key_21, jcast('int', (_java_old_22 + (1)))), _java_old_22)[4]])

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
            raise TypeError("No matching overload for Code05_Poem1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Poem1.MAXN = jcast('int', 100001)
Code05_Poem1.MAXB = jcast('int', 401)
Code05_Poem1.n = jcast('int', 0)
Code05_Poem1.c = jcast('int', 0)
Code05_Poem1.m = jcast('int', 0)
Code05_Poem1.arr = jarray('int', [Code05_Poem1.MAXN])
Code05_Poem1.blen = jcast('int', 0)
Code05_Poem1.bnum = jcast('int', 0)
Code05_Poem1.bi = jarray('int', [Code05_Poem1.MAXN])
Code05_Poem1.bl = jarray('int', [Code05_Poem1.MAXB])
Code05_Poem1.br = jarray('int', [Code05_Poem1.MAXB])
Code05_Poem1.freq = jarray('int', [Code05_Poem1.MAXB, Code05_Poem1.MAXN])
Code05_Poem1.even = jarray('int', [Code05_Poem1.MAXB, Code05_Poem1.MAXB])
Code05_Poem1.numCnt = jarray('int', [Code05_Poem1.MAXN])

if __name__ == '__main__':
    Code05_Poem1.main([])
