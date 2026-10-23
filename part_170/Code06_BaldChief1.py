# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 秃子酋长，Python版
# 给定一个长度为n的数组arr，一共有m条查询，格式如下
# 查询 l r : 打印arr[l..r]范围上，如果所有数排序后，
# 相邻的数在原序列中的位置的差的绝对值之和
# 注意arr很特殊，1~n这些数字在arr中都只出现1次
# 1 <= n、m <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P8078
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 对应实现可参考 Code06_BaldChief2.py
# 两个版本保留相同的算法逻辑
class Code06_BaldChief1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'arr': 'arr', 'query': 'query', 'pos': 'pos', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'bl': 'bl', 'last': 'last', 'next': 'next', 'sum': 'sum', 'ans': 'ans'}
    MAXN = 0
    n = 0
    m = 0
    arr = None
    query = None
    pos = None
    blen = 0
    bnum = 0
    bi = None
    bl = None
    last = None
    next = None
    sum = 0
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code06_BaldChief1.bi[a[0]] != Code06_BaldChief1.bi[b[0]]):
                return jcast('int', jcast('int', (Code06_BaldChief1.bi[a[0]] - Code06_BaldChief1.bi[b[0]])))
            return jcast('int', jcast('int', (b[1] - a[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def del_(num):
        num = jcast('int', num)
        less = jcast('int', Code06_BaldChief1.last[num])
        more = jcast('int', Code06_BaldChief1.next[num])
        if (less != 0):
            Code06_BaldChief1.sum = jcast('long', jcast('long', (Code06_BaldChief1.sum - jstatic('Math', 'abs', jcast('int', (Code06_BaldChief1.pos[num] - Code06_BaldChief1.pos[less]))))))
        if (more != jcast('int', jadd(Code06_BaldChief1.n, 1))):
            Code06_BaldChief1.sum = jcast('long', jcast('long', (Code06_BaldChief1.sum - jstatic('Math', 'abs', jcast('int', (Code06_BaldChief1.pos[more] - Code06_BaldChief1.pos[num]))))))
        if ((less != 0) and (more != jcast('int', jadd(Code06_BaldChief1.n, 1)))):
            Code06_BaldChief1.sum = jcast('long', jcast('long', jadd(Code06_BaldChief1.sum, jstatic('Math', 'abs', jcast('int', (Code06_BaldChief1.pos[more] - Code06_BaldChief1.pos[less]))))))
        Code06_BaldChief1.next[less] = jcast('int', more)
        Code06_BaldChief1.last[more] = jcast('int', less)

    # 加数字的顺序，就是删数字顺序的回滚，才能这么方便的更新
    @staticmethod
    def add(num):
        num = jcast('int', num)
        jset(Code06_BaldChief1.next, Code06_BaldChief1.last[num], num)
        jset(Code06_BaldChief1.last, Code06_BaldChief1.next[num], num)

    @staticmethod
    def compute():
        v = jcast('int', 1)
        while (v <= Code06_BaldChief1.n):
            Code06_BaldChief1.last[v] = jcast('int', jcast('int', (v - 1)))
            Code06_BaldChief1.next[v] = jcast('int', jcast('int', jadd(v, 1)))
            v = jcast('int', (v + 1))
        Code06_BaldChief1.next[0] = jcast('int', 1)
        Code06_BaldChief1.last[jcast('int', jadd(Code06_BaldChief1.n, 1))] = jcast('int', Code06_BaldChief1.n)
        v = jcast('int', 2)
        while (v <= Code06_BaldChief1.n):
            Code06_BaldChief1.sum = jcast('long', jcast('long', jadd(Code06_BaldChief1.sum, jstatic('Math', 'abs', jcast('int', (Code06_BaldChief1.pos[v] - Code06_BaldChief1.pos[jcast('int', (v - 1))]))))))
            v = jcast('int', (v + 1))
        winl = jcast('int', 1)
        winr = jcast('int', Code06_BaldChief1.n)
        block = jcast('int', 1)
        qi = jcast('int', 1)
        while ((block <= Code06_BaldChief1.bnum) and (qi <= Code06_BaldChief1.m)):
            while (winl < Code06_BaldChief1.bl[block]):
                Code06_BaldChief1.del_(Code06_BaldChief1.arr[((_java_old_1 := winl), (winl := jcast('int', (winl + (1)))), _java_old_1)[2]])
            beforeJob = jcast('long', Code06_BaldChief1.sum)
            while ((qi <= Code06_BaldChief1.m) and (Code06_BaldChief1.bi[Code06_BaldChief1.query[qi][0]] == block)):
                jobl = jcast('int', Code06_BaldChief1.query[qi][0])
                jobr = jcast('int', Code06_BaldChief1.query[qi][1])
                id = jcast('int', Code06_BaldChief1.query[qi][2])
                while (winr > jobr):
                    Code06_BaldChief1.del_(Code06_BaldChief1.arr[((_java_old_2 := winr), (winr := jcast('int', (winr + (-1)))), _java_old_2)[2]])
                backup = jcast('long', Code06_BaldChief1.sum)
                while (winl < jobl):
                    Code06_BaldChief1.del_(Code06_BaldChief1.arr[((_java_old_3 := winl), (winl := jcast('int', (winl + (1)))), _java_old_3)[2]])
                Code06_BaldChief1.ans[id] = jcast('long', Code06_BaldChief1.sum)
                Code06_BaldChief1.sum = jcast('long', backup)
                while (winl > Code06_BaldChief1.bl[block]):
                    Code06_BaldChief1.add(Code06_BaldChief1.arr[(winl := jcast('int', (winl + (-1))))])
                qi = jcast('int', (qi + 1))
            while (winr < Code06_BaldChief1.n):
                Code06_BaldChief1.add(Code06_BaldChief1.arr[(winr := jcast('int', (winr + (1))))])
            Code06_BaldChief1.sum = jcast('long', beforeJob)
            block = jcast('int', (block + 1))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code06_BaldChief1.n):
            jset(Code06_BaldChief1.pos, Code06_BaldChief1.arr[i], i)
            i = jcast('int', (i + 1))
        Code06_BaldChief1.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code06_BaldChief1.n)))
        Code06_BaldChief1.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code06_BaldChief1.n, Code06_BaldChief1.blen)) - 1)), Code06_BaldChief1.blen)))
        i = jcast('int', 1)
        while (i <= Code06_BaldChief1.n):
            Code06_BaldChief1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code06_BaldChief1.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_BaldChief1.bnum):
            Code06_BaldChief1.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code06_BaldChief1.blen)), 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code06_BaldChief1.query, 1, jcast('int', jadd(Code06_BaldChief1.m, 1)), Code06_BaldChief1.QueryCmp())

    @staticmethod
    def main(args):
        in_ = Code06_BaldChief1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_BaldChief1.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_BaldChief1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_BaldChief1.n):
            jset(Code06_BaldChief1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_BaldChief1.m):
            jset(Code06_BaldChief1.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code06_BaldChief1.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code06_BaldChief1.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code06_BaldChief1.prepare()
        Code06_BaldChief1.compute()
        i = jcast('int', 1)
        while (i <= Code06_BaldChief1.m):
            jcall(out, 'println', Code06_BaldChief1.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_4 := self), (_java_key_5 := 'ptr'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]])

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
            raise TypeError("No matching overload for Code06_BaldChief1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_BaldChief1.MAXN = jcast('int', 500001)
Code06_BaldChief1.n = jcast('int', 0)
Code06_BaldChief1.m = jcast('int', 0)
Code06_BaldChief1.arr = jarray('int', [Code06_BaldChief1.MAXN])
Code06_BaldChief1.query = jarray('int', [Code06_BaldChief1.MAXN, 3])
Code06_BaldChief1.pos = jarray('int', [Code06_BaldChief1.MAXN])
Code06_BaldChief1.blen = jcast('int', 0)
Code06_BaldChief1.bnum = jcast('int', 0)
Code06_BaldChief1.bi = jarray('int', [Code06_BaldChief1.MAXN])
Code06_BaldChief1.bl = jarray('int', [Code06_BaldChief1.MAXN])
Code06_BaldChief1.last = jarray('int', [jcast('int', jadd(Code06_BaldChief1.MAXN, 1))])
Code06_BaldChief1.next = jarray('int', [jcast('int', jadd(Code06_BaldChief1.MAXN, 1))])
Code06_BaldChief1.sum = jcast('long', 0)
Code06_BaldChief1.ans = jarray('long', [Code06_BaldChief1.MAXN])

if __name__ == '__main__':
    Code06_BaldChief1.main([])
