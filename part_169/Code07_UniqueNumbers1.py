# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 统计出现1次的数，Python版
# 给定一个长度为n的数组arr，下标0~n-1，一共有m条操作，格式如下
# 操作 1 pos val : 把arr[pos]的值设置成val
# 操作 2 l r     : 查询arr[l..r]范围上，有多少种数出现了1次
# 0 <= n、m、arr[i] <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/SP30906
# 测试链接 : https://www.spoj.com/problems/ADAUNIQ/
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 对应实现可参考 Code07_UniqueNumbers2.py
# 两个版本保留相同的算法逻辑
class Code07_UniqueNumbers1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'arr': 'arr', 'bi': 'bi', 'query': 'query', 'update': 'update', 'cntq': 'cntq', 'cntu': 'cntu', 'cnt': 'cnt', 'curCnt': 'curCnt', 'ans': 'ans'}
    MAXN = 0
    n = 0
    m = 0
    arr = None
    bi = None
    query = None
    update = None
    cntq = 0
    cntu = 0
    # 每种数字的词频统计
    cnt = None
    # curCnt代表出现次数1次的数有几种
    curCnt = 0
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code07_UniqueNumbers1.bi[a[0]] != Code07_UniqueNumbers1.bi[b[0]]):
                return jcast('int', jcast('int', (Code07_UniqueNumbers1.bi[a[0]] - Code07_UniqueNumbers1.bi[b[0]])))
            if (Code07_UniqueNumbers1.bi[a[1]] != Code07_UniqueNumbers1.bi[b[1]]):
                return jcast('int', jcast('int', (Code07_UniqueNumbers1.bi[a[1]] - Code07_UniqueNumbers1.bi[b[1]])))
            return jcast('int', jcast('int', (a[2] - b[2])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def del_(num):
        num = jcast('int', num)
        if (Code07_UniqueNumbers1.cnt[num] == 1):
            Code07_UniqueNumbers1.curCnt = jcast('int', (Code07_UniqueNumbers1.curCnt - 1))
        if (Code07_UniqueNumbers1.cnt[num] == 2):
            Code07_UniqueNumbers1.curCnt = jcast('int', (Code07_UniqueNumbers1.curCnt + 1))
        Code07_UniqueNumbers1.cnt[num] = jcast('int', (Code07_UniqueNumbers1.cnt[num] - 1))

    @staticmethod
    def add(num):
        num = jcast('int', num)
        if (Code07_UniqueNumbers1.cnt[num] == 0):
            Code07_UniqueNumbers1.curCnt = jcast('int', (Code07_UniqueNumbers1.curCnt + 1))
        if (Code07_UniqueNumbers1.cnt[num] == 1):
            Code07_UniqueNumbers1.curCnt = jcast('int', (Code07_UniqueNumbers1.curCnt - 1))
        Code07_UniqueNumbers1.cnt[num] = jcast('int', (Code07_UniqueNumbers1.cnt[num] + 1))

    @staticmethod
    def moveTime(jobl, jobr, tim):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        tim = jcast('int', tim)
        pos = jcast('int', Code07_UniqueNumbers1.update[tim][0])
        val = jcast('int', Code07_UniqueNumbers1.update[tim][1])
        if ((jobl <= pos) and (pos <= jobr)):
            Code07_UniqueNumbers1.del_(Code07_UniqueNumbers1.arr[pos])
            Code07_UniqueNumbers1.add(val)
        tmp = jcast('int', Code07_UniqueNumbers1.arr[pos])
        Code07_UniqueNumbers1.arr[pos] = jcast('int', val)
        jset(Code07_UniqueNumbers1.update[tim], 1, tmp)

    @staticmethod
    def compute():
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        wint = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code07_UniqueNumbers1.cntq):
            jobl = jcast('int', Code07_UniqueNumbers1.query[i][0])
            jobr = jcast('int', Code07_UniqueNumbers1.query[i][1])
            jobt = jcast('int', Code07_UniqueNumbers1.query[i][2])
            id = jcast('int', Code07_UniqueNumbers1.query[i][3])
            while (winl > jobl):
                Code07_UniqueNumbers1.add(Code07_UniqueNumbers1.arr[(winl := jcast('int', (winl + (-1))))])
            while (winr < jobr):
                Code07_UniqueNumbers1.add(Code07_UniqueNumbers1.arr[(winr := jcast('int', (winr + (1))))])
            while (winl < jobl):
                Code07_UniqueNumbers1.del_(Code07_UniqueNumbers1.arr[((_java_old_1 := winl), (winl := jcast('int', (winl + (1)))), _java_old_1)[2]])
            while (winr > jobr):
                Code07_UniqueNumbers1.del_(Code07_UniqueNumbers1.arr[((_java_old_2 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_2)[2]])
            while (wint < jobt):
                Code07_UniqueNumbers1.moveTime(jobl, jobr, (wint := jcast('int', (wint + (1)))))
            while (wint > jobt):
                Code07_UniqueNumbers1.moveTime(jobl, jobr, ((_java_old_3 := wint), (wint := jcast('int', (wint + (-1)))), _java_old_3)[2])
            Code07_UniqueNumbers1.ans[id] = jcast('int', Code07_UniqueNumbers1.curCnt)
            i = jcast('int', (i + 1))

    @staticmethod
    def prepare():
        blen = jcast('int', jstatic('Math', 'max', 1, jcast('int', jstatic('Math', 'pow', Code07_UniqueNumbers1.n, jdiv(2.0, 3)))))
        i = jcast('int', 1)
        while (i <= Code07_UniqueNumbers1.n):
            Code07_UniqueNumbers1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code07_UniqueNumbers1.query, 1, jcast('int', jadd(Code07_UniqueNumbers1.cntq, 1)), Code07_UniqueNumbers1.QueryCmp())

    @staticmethod
    def main(args):
        in_ = Code07_UniqueNumbers1.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_UniqueNumbers1.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_UniqueNumbers1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_UniqueNumbers1.n):
            jset(Code07_UniqueNumbers1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        l = 0
        r = 0
        pos = 0
        val = 0
        while (i <= Code07_UniqueNumbers1.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                pos = jcast('int', jcall(in_, 'nextInt'))
                val = jcast('int', jcall(in_, 'nextInt'))
                Code07_UniqueNumbers1.cntu = jcast('int', (Code07_UniqueNumbers1.cntu + 1))
                jset(Code07_UniqueNumbers1.update[Code07_UniqueNumbers1.cntu], 0, jcast('int', jadd(pos, 1)))
                jset(Code07_UniqueNumbers1.update[Code07_UniqueNumbers1.cntu], 1, val)
            else:
                l = jcast('int', jcall(in_, 'nextInt'))
                r = jcast('int', jcall(in_, 'nextInt'))
                Code07_UniqueNumbers1.cntq = jcast('int', (Code07_UniqueNumbers1.cntq + 1))
                jset(Code07_UniqueNumbers1.query[Code07_UniqueNumbers1.cntq], 0, jcast('int', jadd(l, 1)))
                jset(Code07_UniqueNumbers1.query[Code07_UniqueNumbers1.cntq], 1, jcast('int', jadd(r, 1)))
                jset(Code07_UniqueNumbers1.query[Code07_UniqueNumbers1.cntq], 2, Code07_UniqueNumbers1.cntu)
                jset(Code07_UniqueNumbers1.query[Code07_UniqueNumbers1.cntq], 3, Code07_UniqueNumbers1.cntq)
            i = jcast('int', (i + 1))
        Code07_UniqueNumbers1.prepare()
        Code07_UniqueNumbers1.compute()
        i = jcast('int', 1)
        while (i <= Code07_UniqueNumbers1.cntq):
            jcall(out, 'println', Code07_UniqueNumbers1.ans[i])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'BUFFER_SIZE': 'BUFFER_SIZE', 'in': 'in_', 'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len'}
        # BUFFER_SIZE：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.in_ = jget(System, 'in')
            self.buffer = jarray('byte', [self.BUFFER_SIZE])
            self.ptr = jcast('int', jset(self, 'len', 0))

        def hasNextByte(self):
            if (self.ptr < self.len):
                return jcast('boolean', True)
            self.ptr = jcast('int', 0)
            self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
            return jcast('boolean', (self.len > 0))

        def readByte(self):
            if (not self.hasNextByte()):
                return jcast('byte', jcast('int', (-1)))
            return jcast('byte', self.buffer[((_java_obj_4 := self), (_java_key_5 := 'ptr'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]])

        def nextChar(self):
            c = 0
            while True:
                c = jcast('byte', self.readByte())
                if (c == jcast('int', (-1))):
                    return jcast('char', 0)
                if not ((c <= jchar(' '))):
                    break
            ans = jcast('char', 0)
            while (c > jchar(' ')):
                ans = jcast('char', jcast('char', c))
                c = jcast('byte', self.readByte())
            return jcast('char', ans)

        def nextInt(self):
            num = jcast('int', 0)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                num = jcast('int', jcast('int', jadd(jcast('int', (num * 10)), jcast('int', (b - jchar('0'))))))
                b = jcast('byte', self.readByte())
            return jcast('int', (jcast('int', (-num)) if minus else num))

        def isWhitespace(self, b):
            b = jcast('byte', b)
            return jcast('boolean', ((((b == jchar(' ')) or (b == jchar('\n'))) or (b == jchar('\r'))) or (b == jchar('\t'))))

        def __init__(self, *args, _java_ctor=None):
            self.BUFFER_SIZE = jcast('int', jcast('int', (1 << (16 & 31))))
            self.in_ = None
            self.buffer = None
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code07_UniqueNumbers1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_UniqueNumbers1.MAXN = jcast('int', 200001)
Code07_UniqueNumbers1.n = jcast('int', 0)
Code07_UniqueNumbers1.m = jcast('int', 0)
Code07_UniqueNumbers1.arr = jarray('int', [Code07_UniqueNumbers1.MAXN])
Code07_UniqueNumbers1.bi = jarray('int', [Code07_UniqueNumbers1.MAXN])
Code07_UniqueNumbers1.query = jarray('int', [Code07_UniqueNumbers1.MAXN, 4])
Code07_UniqueNumbers1.update = jarray('int', [Code07_UniqueNumbers1.MAXN, 2])
Code07_UniqueNumbers1.cntq = jcast('int', 0)
Code07_UniqueNumbers1.cntu = jcast('int', 0)
Code07_UniqueNumbers1.cnt = jarray('int', [Code07_UniqueNumbers1.MAXN])
Code07_UniqueNumbers1.curCnt = jcast('int', 0)
Code07_UniqueNumbers1.ans = jarray('int', [Code07_UniqueNumbers1.MAXN])

if __name__ == '__main__':
    Code07_UniqueNumbers1.main([])
