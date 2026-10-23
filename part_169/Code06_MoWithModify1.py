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

# 带修莫队入门题，Python版
# 给定一个长度为n的数组arr，一共有m条操作，操作格式如下
# 操作 Q l r     : 打印arr[l..r]范围上有几种不同的数
# 操作 R pos val : 把arr[pos]的值设置成val
# 1 <= n、m <= 2 * 10^5
# 1 <= arr[i]、val <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P1903
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_MoWithModify1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'n': 'n', 'm': 'm', 'arr': 'arr', 'bi': 'bi', 'query': 'query', 'update': 'update', 'cntq': 'cntq', 'cntu': 'cntu', 'cnt': 'cnt', 'kind': 'kind', 'ans': 'ans'}
    MAXN = 0
    MAXV = 0
    n = 0
    m = 0
    arr = None
    bi = None
    # 每条查询 : jobl、jobr、jobt、id
    query = None
    # 每条修改 : pos、val
    update = None
    cntq = 0
    cntu = 0
    cnt = None
    kind = 0
    ans = None
    # 带修莫队的任务排序
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code06_MoWithModify1.bi[a[0]] != Code06_MoWithModify1.bi[b[0]]):
                return jcast('int', jcast('int', (Code06_MoWithModify1.bi[a[0]] - Code06_MoWithModify1.bi[b[0]])))
            if (Code06_MoWithModify1.bi[a[1]] != Code06_MoWithModify1.bi[b[1]]):
                return jcast('int', jcast('int', (Code06_MoWithModify1.bi[a[1]] - Code06_MoWithModify1.bi[b[1]])))
            return jcast('int', jcast('int', (a[2] - b[2])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def del_(num):
        num = jcast('int', num)
        if (((_java_obj_1 := Code06_MoWithModify1.cnt), (_java_key_2 := num), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))))[3] == 0):
            Code06_MoWithModify1.kind = jcast('int', (Code06_MoWithModify1.kind - 1))

    @staticmethod
    def add(num):
        num = jcast('int', num)
        if (((_java_obj_4 := Code06_MoWithModify1.cnt), (_java_key_5 := num), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3] == 1):
            Code06_MoWithModify1.kind = jcast('int', (Code06_MoWithModify1.kind + 1))

    # jobl..jobr 数组范围
    # tim : 生效或者撤销的修改时间点
    @staticmethod
    def moveTime(jobl, jobr, tim):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        tim = jcast('int', tim)
        pos = jcast('int', Code06_MoWithModify1.update[tim][0])
        val = jcast('int', Code06_MoWithModify1.update[tim][1])
        if ((jobl <= pos) and (pos <= jobr)):
            Code06_MoWithModify1.del_(Code06_MoWithModify1.arr[pos])
            Code06_MoWithModify1.add(val)
        # 不管生效还是撤销，数据只要在arr和update之间交换即可
        tmp = jcast('int', Code06_MoWithModify1.arr[pos])
        Code06_MoWithModify1.arr[pos] = jcast('int', val)
        jset(Code06_MoWithModify1.update[tim], 1, tmp)

    @staticmethod
    def compute():
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        wint = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code06_MoWithModify1.cntq):
            jobl = jcast('int', Code06_MoWithModify1.query[i][0])
            jobr = jcast('int', Code06_MoWithModify1.query[i][1])
            jobt = jcast('int', Code06_MoWithModify1.query[i][2])
            id = jcast('int', Code06_MoWithModify1.query[i][3])
            while (winl > jobl):
                Code06_MoWithModify1.add(Code06_MoWithModify1.arr[(winl := jcast('int', (winl + (-1))))])
            while (winr < jobr):
                Code06_MoWithModify1.add(Code06_MoWithModify1.arr[(winr := jcast('int', (winr + (1))))])
            while (winl < jobl):
                Code06_MoWithModify1.del_(Code06_MoWithModify1.arr[((_java_old_7 := winl), (winl := jcast('int', (winl + (1)))), _java_old_7)[2]])
            while (winr > jobr):
                Code06_MoWithModify1.del_(Code06_MoWithModify1.arr[((_java_old_8 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_8)[2]])
            while (wint < jobt):
                Code06_MoWithModify1.moveTime(jobl, jobr, (wint := jcast('int', (wint + (1)))))
            while (wint > jobt):
                Code06_MoWithModify1.moveTime(jobl, jobr, ((_java_old_9 := wint), (wint := jcast('int', (wint + (-1)))), _java_old_9)[2])
            Code06_MoWithModify1.ans[id] = jcast('int', Code06_MoWithModify1.kind)
            i = jcast('int', (i + 1))

    @staticmethod
    def prepare():
        blen = jcast('int', jstatic('Math', 'max', 1, jcast('int', jstatic('Math', 'pow', Code06_MoWithModify1.n, jdiv(2.0, 3)))))
        i = jcast('int', 1)
        while (i <= Code06_MoWithModify1.n):
            Code06_MoWithModify1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code06_MoWithModify1.query, 1, jcast('int', jadd(Code06_MoWithModify1.cntq, 1)), Code06_MoWithModify1.QueryCmp())

    @staticmethod
    def main(args):
        in_ = Code06_MoWithModify1.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_MoWithModify1.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_MoWithModify1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_MoWithModify1.n):
            jset(Code06_MoWithModify1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        op = jchar(0)
        l = 0
        r = 0
        pos = 0
        val = 0
        i = jcast('int', 1)
        while (i <= Code06_MoWithModify1.m):
            op = jcast('char', jcall(in_, 'nextChar'))
            if (op == jchar('Q')):
                l = jcast('int', jcall(in_, 'nextInt'))
                r = jcast('int', jcall(in_, 'nextInt'))
                Code06_MoWithModify1.cntq = jcast('int', (Code06_MoWithModify1.cntq + 1))
                jset(Code06_MoWithModify1.query[Code06_MoWithModify1.cntq], 0, l)
                jset(Code06_MoWithModify1.query[Code06_MoWithModify1.cntq], 1, r)
                jset(Code06_MoWithModify1.query[Code06_MoWithModify1.cntq], 2, Code06_MoWithModify1.cntu)
                jset(Code06_MoWithModify1.query[Code06_MoWithModify1.cntq], 3, Code06_MoWithModify1.cntq)
            else:
                pos = jcast('int', jcall(in_, 'nextInt'))
                val = jcast('int', jcall(in_, 'nextInt'))
                Code06_MoWithModify1.cntu = jcast('int', (Code06_MoWithModify1.cntu + 1))
                jset(Code06_MoWithModify1.update[Code06_MoWithModify1.cntu], 0, pos)
                jset(Code06_MoWithModify1.update[Code06_MoWithModify1.cntu], 1, val)
            i = jcast('int', (i + 1))
        Code06_MoWithModify1.prepare()
        Code06_MoWithModify1.compute()
        i = jcast('int', 1)
        while (i <= Code06_MoWithModify1.cntq):
            jcall(out, 'println', Code06_MoWithModify1.ans[i])
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
            return jcast('byte', self.buffer[((_java_obj_10 := self), (_java_key_11 := 'ptr'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]])

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
            raise TypeError("No matching overload for Code06_MoWithModify1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_MoWithModify1.MAXN = jcast('int', 200001)
Code06_MoWithModify1.MAXV = jcast('int', 1000001)
Code06_MoWithModify1.n = jcast('int', 0)
Code06_MoWithModify1.m = jcast('int', 0)
Code06_MoWithModify1.arr = jarray('int', [Code06_MoWithModify1.MAXN])
Code06_MoWithModify1.bi = jarray('int', [Code06_MoWithModify1.MAXN])
Code06_MoWithModify1.query = jarray('int', [Code06_MoWithModify1.MAXN, 4])
Code06_MoWithModify1.update = jarray('int', [Code06_MoWithModify1.MAXN, 2])
Code06_MoWithModify1.cntq = jcast('int', 0)
Code06_MoWithModify1.cntu = jcast('int', 0)
Code06_MoWithModify1.cnt = jarray('int', [Code06_MoWithModify1.MAXV])
Code06_MoWithModify1.kind = jcast('int', 0)
Code06_MoWithModify1.ans = jarray('int', [Code06_MoWithModify1.MAXN])

if __name__ == '__main__':
    Code06_MoWithModify1.main([])
