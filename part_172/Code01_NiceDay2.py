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

# 美好的每一天，Python版
# 给定一个长度为n的字符串str，其中都是小写字母
# 如果一个子串重新排列字符之后能成为回文串，那么该子串叫做达标子串
# 接下来有m条查询，格式为 l r : 打印str[l..r]范围上有多少达标子串
# 1 <= n、m <= 6 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P3604
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_NiceDay2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'n': 'n', 'm': 'm', 'arr': 'arr', 'query': 'query', 'bi': 'bi', 'cnt': 'cnt', 'curAns': 'curAns', 'ans': 'ans'}
    MAXN = 0
    MAXV = 0
    n = 0
    m = 0
    arr = None
    query = None
    bi = None
    cnt = None
    curAns = 0
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code01_NiceDay2.bi[a[0]] != Code01_NiceDay2.bi[b[0]]):
                return jcast('int', jcast('int', (Code01_NiceDay2.bi[a[0]] - Code01_NiceDay2.bi[b[0]])))
            if (jcast('int', (Code01_NiceDay2.bi[a[0]] & 1)) == 1):
                return jcast('int', jcast('int', (a[1] - b[1])))
            else:
                return jcast('int', jcast('int', (b[1] - a[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def add(s):
        s = jcast('int', s)
        Code01_NiceDay2.curAns = jcast('long', jcast('long', jadd(Code01_NiceDay2.curAns, Code01_NiceDay2.cnt[s])))
        Code01_NiceDay2.cnt[s] = jcast('int', (Code01_NiceDay2.cnt[s] + 1))
        i = jcast('int', 0)
        while (i < 26):
            Code01_NiceDay2.curAns = jcast('long', jcast('long', jadd(Code01_NiceDay2.curAns, Code01_NiceDay2.cnt[jcast('int', (s ^ jcast('int', (1 << (i & 31)))))])))
            i = jcast('int', (i + 1))

    @staticmethod
    def del_(s):
        s = jcast('int', s)
        Code01_NiceDay2.cnt[s] = jcast('int', (Code01_NiceDay2.cnt[s] - 1))
        Code01_NiceDay2.curAns = jcast('long', jcast('long', (Code01_NiceDay2.curAns - Code01_NiceDay2.cnt[s])))
        i = jcast('int', 0)
        while (i < 26):
            Code01_NiceDay2.curAns = jcast('long', jcast('long', (Code01_NiceDay2.curAns - Code01_NiceDay2.cnt[jcast('int', (s ^ jcast('int', (1 << (i & 31)))))])))
            i = jcast('int', (i + 1))

    @staticmethod
    def compute():
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code01_NiceDay2.m):
            jobl = jcast('int', Code01_NiceDay2.query[i][0])
            jobr = jcast('int', Code01_NiceDay2.query[i][1])
            id = jcast('int', Code01_NiceDay2.query[i][2])
            while (winl > jobl):
                Code01_NiceDay2.add(Code01_NiceDay2.arr[(winl := jcast('int', (winl + (-1))))])
            while (winr < jobr):
                Code01_NiceDay2.add(Code01_NiceDay2.arr[(winr := jcast('int', (winr + (1))))])
            while (winl < jobl):
                Code01_NiceDay2.del_(Code01_NiceDay2.arr[((_java_old_1 := winl), (winl := jcast('int', (winl + (1)))), _java_old_1)[2]])
            while (winr > jobr):
                Code01_NiceDay2.del_(Code01_NiceDay2.arr[((_java_old_2 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_2)[2]])
            Code01_NiceDay2.ans[id] = jcast('long', Code01_NiceDay2.curAns)
            i = jcast('int', (i + 1))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code01_NiceDay2.n):
            Code01_NiceDay2.arr[i] = jcast('int', jcast('int', (Code01_NiceDay2.arr[i] ^ Code01_NiceDay2.arr[jcast('int', (i - 1))])))
            i = jcast('int', (i + 1))
        i = jcast('int', Code01_NiceDay2.n)
        while (i >= 0):
            Code01_NiceDay2.arr[jcast('int', jadd(i, 1))] = jcast('int', Code01_NiceDay2.arr[i])
            i = jcast('int', (i - 1))
        Code01_NiceDay2.n = jcast('int', (Code01_NiceDay2.n + 1))
        blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code01_NiceDay2.n)))
        i = jcast('int', 1)
        while (i <= Code01_NiceDay2.n):
            Code01_NiceDay2.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_NiceDay2.m):
            ((_java_obj_3 := Code01_NiceDay2.query[i]), (_java_key_4 := 1), (_java_old_5 := jget(_java_obj_3, _java_key_4)), jset(_java_obj_3, _java_key_4, jcast('int', (_java_old_5 + (1)))), _java_old_5)[4]
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code01_NiceDay2.query, 1, jcast('int', jadd(Code01_NiceDay2.m, 1)), Code01_NiceDay2.QueryCmp())

    @staticmethod
    def main(args):
        in_ = Code01_NiceDay2.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_NiceDay2.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_NiceDay2.m = jcast('int', jcall(in_, 'nextInt'))
        c = jchar(0)
        i = jcast('int', 1)
        while (i <= Code01_NiceDay2.n):
            c = jcast('char', jcall(in_, 'nextLowerCase'))
            Code01_NiceDay2.arr[i] = jcast('int', jcast('int', (1 << (jcast('int', (c - jchar('a'))) & 31))))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_NiceDay2.m):
            jset(Code01_NiceDay2.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code01_NiceDay2.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code01_NiceDay2.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code01_NiceDay2.prepare()
        Code01_NiceDay2.compute()
        i = jcast('int', 1)
        while (i <= Code01_NiceDay2.m):
            jcall(out, 'println', Code01_NiceDay2.ans[i])
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
            return jcast('byte', self.buffer[((_java_obj_6 := self), (_java_key_7 := 'ptr'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))), _java_old_8)[4]])

        def nextLowerCase(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if ((c >= jchar('a')) and (c <= jchar('z'))):
                    return jcast('char', jcast('char', c))

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
            self.BUFFER_SIZE = jcast('int', jcast('int', (1 << (16 & 31))))
            self.in_ = None
            self.buffer = None
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_NiceDay2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_NiceDay2.MAXN = jcast('int', 60002)
Code01_NiceDay2.MAXV = jcast('int', jcast('int', (1 << (26 & 31))))
Code01_NiceDay2.n = jcast('int', 0)
Code01_NiceDay2.m = jcast('int', 0)
Code01_NiceDay2.arr = jarray('int', [Code01_NiceDay2.MAXN])
Code01_NiceDay2.query = jarray('int', [Code01_NiceDay2.MAXN, 3])
Code01_NiceDay2.bi = jarray('int', [Code01_NiceDay2.MAXN])
Code01_NiceDay2.cnt = jarray('int', [Code01_NiceDay2.MAXV])
Code01_NiceDay2.curAns = jcast('long', 0)
Code01_NiceDay2.ans = jarray('long', [Code01_NiceDay2.MAXN])

if __name__ == '__main__':
    Code01_NiceDay2.main([])
