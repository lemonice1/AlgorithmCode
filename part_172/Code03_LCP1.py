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

# 区间lcp达标对，Python版
# 给定一个长度为n的字符串str，还有一个参数k
# 位置a开头和位置b开头的字符串，如果最长公共前缀的长度 >= k，那么(a, b)构成lcp达标对
# 构成lcp达标对，必须是不同的位置，并且(a, b)和(b, a)只算一个达标对，不要重复统计
# 接下来有m条查询，格式为 l r : str[l..r]范围上，可以任选开头位置，打印lcp达标对的数量
# 1 <= n、k <= 3 * 10^6       1 <= m <= 10^5
# 1 <= n * n * m <= 10^15    字符集为 f z o u t s y
# 测试链接 : https://www.luogu.com.cn/problem/P5112
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_LCP1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'k': 'k', 'len': 'len', 'cntq': 'cntq', 'cntv': 'cntv', 'str': 'str', 'query': 'query', 'base': 'base', 'basePower': 'basePower', 'hashValue': 'hashValue', 'val': 'val', 'sorted': 'sorted', 'arr': 'arr', 'bi': 'bi', 'cnt': 'cnt', 'curAns': 'curAns', 'ans': 'ans'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    k = 0
    len = 0
    cntq = 0
    cntv = 0
    str = None
    query = None
    # 字符串哈希
    base = 0
    basePower = None
    hashValue = None
    # 哈希值离散化，用哈希值替代字符串，再用排名替代哈希值
    val = None
    sorted = None
    arr = None
    bi = None
    cnt = None
    curAns = 0
    ans = None
    @staticmethod
    def kth(num):
        num = jcast('long', num)
        left = jcast('int', 1)
        right = jcast('int', Code03_LCP1.cntv)
        mid = 0
        ret = jcast('int', 0)
        while (left <= right):
            mid = jcast('int', jcast('int', (jcast('int', jadd(left, right)) >> (1 & 31))))
            if (Code03_LCP1.sorted[mid] <= num):
                ret = jcast('int', mid)
                left = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ret)

    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code03_LCP1.bi[a[0]] != Code03_LCP1.bi[b[0]]):
                return jcast('int', jcast('int', (Code03_LCP1.bi[a[0]] - Code03_LCP1.bi[b[0]])))
            if (jcast('int', (Code03_LCP1.bi[a[0]] & 1)) == 1):
                return jcast('int', jcast('int', (a[1] - b[1])))
            else:
                return jcast('int', jcast('int', (b[1] - a[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def add(x):
        x = jcast('int', x)
        Code03_LCP1.curAns = jcast('long', jcast('long', jadd(Code03_LCP1.curAns, Code03_LCP1.cnt[x])))
        Code03_LCP1.cnt[x] = jcast('int', (Code03_LCP1.cnt[x] + 1))

    @staticmethod
    def del_(x):
        x = jcast('int', x)
        Code03_LCP1.cnt[x] = jcast('int', (Code03_LCP1.cnt[x] - 1))
        Code03_LCP1.curAns = jcast('long', jcast('long', (Code03_LCP1.curAns - Code03_LCP1.cnt[x])))

    @staticmethod
    def compute():
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code03_LCP1.cntq):
            jobl = jcast('int', Code03_LCP1.query[i][0])
            jobr = jcast('int', Code03_LCP1.query[i][1])
            id = jcast('int', Code03_LCP1.query[i][2])
            while (winl > jobl):
                Code03_LCP1.add(Code03_LCP1.arr[(winl := jcast('int', (winl + (-1))))])
            while (winr < jobr):
                Code03_LCP1.add(Code03_LCP1.arr[(winr := jcast('int', (winr + (1))))])
            while (winl < jobl):
                Code03_LCP1.del_(Code03_LCP1.arr[((_java_old_1 := winl), (winl := jcast('int', (winl + (1)))), _java_old_1)[2]])
            while (winr > jobr):
                Code03_LCP1.del_(Code03_LCP1.arr[((_java_old_2 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_2)[2]])
            Code03_LCP1.ans[id] = jcast('long', Code03_LCP1.curAns)
            i = jcast('int', (i + 1))

    @staticmethod
    def prepare():
        Code03_LCP1.basePower[0] = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= Code03_LCP1.n):
            Code03_LCP1.basePower[i] = jcast('long', jcast('long', (Code03_LCP1.basePower[jcast('int', (i - 1))] * Code03_LCP1.base)))
            Code03_LCP1.hashValue[i] = jcast('long', jcast('long', jadd(jcast('long', (Code03_LCP1.hashValue[jcast('int', (i - 1))] * Code03_LCP1.base)), jcast('int', jadd(jcast('int', (Code03_LCP1.str[i] - jchar('a'))), 1)))))
            i = jcast('int', (i + 1))
        l = jcast('int', 1)
        r = jcast('int', Code03_LCP1.k)
        while (r <= Code03_LCP1.n):
            Code03_LCP1.val[l] = jcast('long', jcast('long', (Code03_LCP1.hashValue[r] - jcast('long', (Code03_LCP1.hashValue[jcast('int', (l - 1))] * Code03_LCP1.basePower[jcast('int', jadd(jcast('int', (r - l)), 1))])))))
            l = jcast('int', (l + 1))
            r = jcast('int', (r + 1))
        i = jcast('int', 1)
        while (i <= Code03_LCP1.len):
            Code03_LCP1.sorted[i] = jcast('long', Code03_LCP1.val[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code03_LCP1.sorted, 1, jcast('int', jadd(Code03_LCP1.len, 1)))
        Code03_LCP1.cntv = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code03_LCP1.len):
            if (Code03_LCP1.sorted[Code03_LCP1.cntv] != Code03_LCP1.sorted[i]):
                jset(Code03_LCP1.sorted, ((_java_obj_3 := Code03_LCP1), (_java_key_4 := 'cntv'), (_java_old_5 := jget(_java_obj_3, _java_key_4)), jset(_java_obj_3, _java_key_4, jcast('int', (_java_old_5 + (1)))))[3], Code03_LCP1.sorted[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_LCP1.len):
            jset(Code03_LCP1.arr, i, Code03_LCP1.kth(Code03_LCP1.val[i]))
            i = jcast('int', (i + 1))
        # 优化块长
        blen = jcast('int', jstatic('Math', 'max', 1, jcast('int', jdiv(jcast('double', Code03_LCP1.n), jstatic('Math', 'sqrt', Code03_LCP1.m)))))
        i = jcast('int', 1)
        while (i <= Code03_LCP1.n):
            Code03_LCP1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code03_LCP1.query, 1, jcast('int', jadd(Code03_LCP1.cntq, 1)), Code03_LCP1.QueryCmp())

    @staticmethod
    def main(args):
        in_ = Code03_LCP1.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_LCP1.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_LCP1.m = jcast('int', jcall(in_, 'nextInt'))
        Code03_LCP1.k = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_LCP1.n):
            jset(Code03_LCP1.str, i, jcall(in_, 'nextLowerCase'))
            i = jcast('int', (i + 1))
        # 有效开头的个数，剩下的开头舍弃
        Code03_LCP1.len = jcast('int', jcast('int', jadd(jcast('int', (Code03_LCP1.n - Code03_LCP1.k)), 1)))
        Code03_LCP1.cntq = jcast('int', 0)
        i = jcast('int', 1)
        l = 0
        r = 0
        while (i <= Code03_LCP1.m):
            l = jcast('int', jcall(in_, 'nextInt'))
            r = jcast('int', jcall(in_, 'nextInt'))
            # 过滤查询并调整查询参数
            if (l <= Code03_LCP1.len):
                jset(Code03_LCP1.query[((_java_obj_6 := Code03_LCP1), (_java_key_7 := 'cntq'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))))[3]], 0, l)
                jset(Code03_LCP1.query[Code03_LCP1.cntq], 1, jstatic('Math', 'min', r, Code03_LCP1.len))
                jset(Code03_LCP1.query[Code03_LCP1.cntq], 2, i)
            i = jcast('int', (i + 1))
        Code03_LCP1.prepare()
        Code03_LCP1.compute()
        i = jcast('int', 1)
        while (i <= Code03_LCP1.m):
            jcall(out, 'println', Code03_LCP1.ans[i])
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
            return jcast('byte', self.buffer[((_java_obj_9 := self), (_java_key_10 := 'ptr'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))), _java_old_11)[4]])

        def nextLowerCase(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if ((c >= jchar('a')) and (c <= jchar('z'))):
                    return jcast('char', jcast('char', c))

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
            raise TypeError("No matching overload for Code03_LCP1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_LCP1.MAXN = jcast('int', 3000001)
Code03_LCP1.MAXM = jcast('int', 100001)
Code03_LCP1.n = jcast('int', 0)
Code03_LCP1.m = jcast('int', 0)
Code03_LCP1.k = jcast('int', 0)
Code03_LCP1.len = jcast('int', 0)
Code03_LCP1.cntq = jcast('int', 0)
Code03_LCP1.cntv = jcast('int', 0)
Code03_LCP1.str = jarray('char', [Code03_LCP1.MAXN])
Code03_LCP1.query = jarray('int', [Code03_LCP1.MAXM, 3])
Code03_LCP1.base = jcast('int', 499)
Code03_LCP1.basePower = jarray('long', [Code03_LCP1.MAXN])
Code03_LCP1.hashValue = jarray('long', [Code03_LCP1.MAXN])
Code03_LCP1.val = jarray('long', [Code03_LCP1.MAXN])
Code03_LCP1.sorted = jarray('long', [Code03_LCP1.MAXN])
Code03_LCP1.arr = jarray('int', [Code03_LCP1.MAXN])
Code03_LCP1.bi = jarray('int', [Code03_LCP1.MAXN])
Code03_LCP1.cnt = jarray('int', [Code03_LCP1.MAXN])
Code03_LCP1.curAns = jcast('long', 0)
Code03_LCP1.ans = jarray('long', [Code03_LCP1.MAXM])

if __name__ == '__main__':
    Code03_LCP1.main([])
