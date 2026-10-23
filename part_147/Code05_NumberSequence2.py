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

# 数字序列，Python版
# 给定一个长度为n的数组A，要求构造出一个长度为n的递增数组B
# 希望 |A[1] - B[1]| + |A[2] - B[2]| + ... + |A[n] - B[n]| 最小
# 打印这个最小值，然后打印数组B，如果有多个方案，只打印其中的一个
# 1 <= n <= 10^6
# 0 <= A[i] <= 2^32 - 1
# 测试链接 : https://www.luogu.com.cn/problem/P4331
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_NumberSequence2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'arr': 'arr', 'left': 'left', 'right': 'right', 'dist': 'dist', 'father': 'father', 'from': 'from_', 'to': 'to', 'size': 'size', 'stack': 'stack', 'ans': 'ans'}
    MAXN = 0
    n = 0
    arr = None
    # 左偏树需要
    left = None
    right = None
    dist = None
    # 并查集向上的路径
    father = None
    # 集合表达区域的左下标
    from_ = None
    # 集合表达区域的右下标
    to = None
    # 集合里有几个数字
    size = None
    # 单调栈
    stack = None
    # 构造的数组
    ans = None
    @staticmethod
    def prepare():
        Code05_NumberSequence2.dist[0] = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= Code05_NumberSequence2.n):
            jset(Code05_NumberSequence2.left, i, jset(Code05_NumberSequence2.right, i, jset(Code05_NumberSequence2.dist, i, 0)))
            jset(Code05_NumberSequence2.father, i, jset(Code05_NumberSequence2.from_, i, jset(Code05_NumberSequence2.to, i, i)))
            Code05_NumberSequence2.size[i] = jcast('int', 1)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        jset(Code05_NumberSequence2.father, i, (i if (Code05_NumberSequence2.father[i] == i) else Code05_NumberSequence2.find(Code05_NumberSequence2.father[i])))
        return jcast('int', Code05_NumberSequence2.father[i])

    @staticmethod
    def merge(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if ((i == 0) or (j == 0)):
            return jcast('int', jcast('int', jadd(i, j)))
        tmp = 0
        # 维护大根堆
        if (Code05_NumberSequence2.arr[i] < Code05_NumberSequence2.arr[j]):
            tmp = jcast('int', i)
            i = jcast('int', j)
            j = jcast('int', tmp)
        jset(Code05_NumberSequence2.right, i, Code05_NumberSequence2.merge(Code05_NumberSequence2.right[i], j))
        if (Code05_NumberSequence2.dist[Code05_NumberSequence2.left[i]] < Code05_NumberSequence2.dist[Code05_NumberSequence2.right[i]]):
            tmp = jcast('int', Code05_NumberSequence2.left[i])
            Code05_NumberSequence2.left[i] = jcast('int', Code05_NumberSequence2.right[i])
            Code05_NumberSequence2.right[i] = jcast('int', tmp)
        Code05_NumberSequence2.dist[i] = jcast('int', jcast('int', jadd(Code05_NumberSequence2.dist[Code05_NumberSequence2.right[i]], 1)))
        jset(Code05_NumberSequence2.father, Code05_NumberSequence2.left[i], jset(Code05_NumberSequence2.father, Code05_NumberSequence2.right[i], i))
        return jcast('int', i)

    @staticmethod
    def pop(i):
        i = jcast('int', i)
        jset(Code05_NumberSequence2.father, Code05_NumberSequence2.left[i], Code05_NumberSequence2.left[i])
        jset(Code05_NumberSequence2.father, Code05_NumberSequence2.right[i], Code05_NumberSequence2.right[i])
        jset(Code05_NumberSequence2.father, i, Code05_NumberSequence2.merge(Code05_NumberSequence2.left[i], Code05_NumberSequence2.right[i]))
        jset(Code05_NumberSequence2.left, i, jset(Code05_NumberSequence2.right, i, jset(Code05_NumberSequence2.dist, i, 0)))
        return jcast('int', Code05_NumberSequence2.father[i])

    @staticmethod
    def compute():
        stackSize = jcast('int', 0)
        i = jcast('int', 1)
        pre = 0
        cur = 0
        s = 0
        while (i <= Code05_NumberSequence2.n):
            try:
                while (stackSize > 0):
                    try:
                        pre = jcast('int', Code05_NumberSequence2.find(Code05_NumberSequence2.stack[stackSize]))
                        cur = jcast('int', Code05_NumberSequence2.find(i))
                        if (Code05_NumberSequence2.arr[pre] <= Code05_NumberSequence2.arr[cur]):
                            raise JBreak(None)
                        s = jcast('int', jcast('int', jadd(Code05_NumberSequence2.size[pre], Code05_NumberSequence2.size[cur])))
                        cur = jcast('int', Code05_NumberSequence2.merge(pre, cur))
                        # 大根堆只保留到上中位数
                        while (s > jcast('int', jdiv(jcast('int', jadd(jcast('int', jadd(jcast('int', (i - Code05_NumberSequence2.from_[pre])), 1)), 1)), 2))):
                            cur = jcast('int', Code05_NumberSequence2.pop(cur))
                            s = jcast('int', (s - 1))
                        Code05_NumberSequence2.from_[cur] = jcast('int', Code05_NumberSequence2.from_[pre])
                        Code05_NumberSequence2.to[cur] = jcast('int', i)
                        Code05_NumberSequence2.size[cur] = jcast('int', s)
                        stackSize = jcast('int', (stackSize - 1))
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                jset(Code05_NumberSequence2.stack, (stackSize := jcast('int', (stackSize + (1)))), i)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        sum = jcast('long', 0)
        i = jcast('int', 1)
        cur = 0
        while (i <= stackSize):
            cur = jcast('int', Code05_NumberSequence2.find(Code05_NumberSequence2.stack[i]))
            j = jcast('int', Code05_NumberSequence2.from_[cur])
            while (j <= Code05_NumberSequence2.to[cur]):
                Code05_NumberSequence2.ans[j] = jcast('long', Code05_NumberSequence2.arr[cur])
                sum = jcast('long', jcast('long', jadd(sum, jstatic('Math', 'abs', jcast('long', (Code05_NumberSequence2.ans[j] - Code05_NumberSequence2.arr[j]))))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('long', sum)

    @staticmethod
    def main(args):
        in_ = Code05_NumberSequence2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = Code05_NumberSequence2.FastWriter(jget(System, 'out'), _java_ctor=1)
        Code05_NumberSequence2.n = jcast('int', jcall(in_, 'readInt'))
        Code05_NumberSequence2.prepare()
        i = jcast('int', 1)
        while (i <= Code05_NumberSequence2.n):
            jset(Code05_NumberSequence2.arr, i, jcast('long', (jcall(in_, 'readLong') - i)))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code05_NumberSequence2.compute())
        i = jcast('int', 1)
        while (i <= Code05_NumberSequence2.n):
            jcall(out, '_java_write_2', jcast('long', jadd(Code05_NumberSequence2.ans[i], i)))
            jcall(out, '_java_write_1', ' ')
            i = jcast('int', (i + 1))
        jcall(out, '_java_writeln_1')
        jcall(out, 'flush')
        jcall(out, 'close')

    # 快读
    class FastReader:
        __java_fields__ = {'is': 'is_', 'inbuf': 'inbuf', 'lenbuf': 'lenbuf', 'ptrbuf': 'ptrbuf'}
        # is_：实例字段，在构造函数中初始化。
        # inbuf：实例字段，在构造函数中初始化。
        # lenbuf：实例字段，在构造函数中初始化。
        # ptrbuf：实例字段，在构造函数中初始化。
        def _java_init_0(self, is_):
            self.is_ = is_

        def readByte(self):
            if (self.lenbuf == jcast('int', (-1))):
                raise jnew('InputMismatchException')
            if (self.ptrbuf >= self.lenbuf):
                self.ptrbuf = jcast('int', 0)
                try:
                    self.lenbuf = jcast('int', jcall(self.is_, 'read', self.inbuf))
                except (JBreak, JContinue):
                    raise
                except Exception as _java_exception_3:
                    if jinstanceof(_java_exception_3, 'IOException'):
                        e = _java_exception_3
                        raise jnew('InputMismatchException')
                    else:
                        raise
                if (self.lenbuf <= 0):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', self.inbuf[((_java_obj_4 := self), (_java_key_5 := 'ptrbuf'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]])

        def readInt(self):
            return jcast('int', jcast('int', self.readLong()))

        def readLong(self):
            num = jcast('long', 0)
            b = 0
            minus = jcast('boolean', False)
            while (((b := self.readByte()) != jcast('int', (-1))) and (not (((b >= jchar('0')) and (b <= jchar('9'))) or (b == jchar('-'))))):
                None
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('int', self.readByte())
            while True:
                if ((b >= jchar('0')) and (b <= jchar('9'))):
                    num = jcast('long', jcast('long', jadd(jcast('long', (num * 10)), jcast('int', (b - jchar('0'))))))
                else:
                    return jcast('long', (jcast('long', (-num)) if minus else num))
                b = jcast('int', self.readByte())

        def __init__(self, *args, _java_ctor=None):
            self.is_ = None
            self.inbuf = jarray('byte', [1024])
            self.lenbuf = jcast('int', 0)
            self.ptrbuf = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_NumberSequence2.FastReader.FastReader")


    # 快写
    class FastWriter:
        __java_fields__ = {'BUF_SIZE': 'BUF_SIZE', 'buf': 'buf', 'out': 'out', 'writer': 'writer', 'ptr': 'ptr'}
        BUF_SIZE = 0
        # buf：实例字段，在构造函数中初始化。
        # out：实例字段，在构造函数中初始化。
        # writer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        def _java_init_0(self, writer):
            self.writer = jnew('BufferedWriter', writer)
            self.out = jnew('ByteArrayOutputStream')

        def _java_init_1(self, os):
            self.out = os

        def _java_init_2(self, path):
            try:
                self.out = jnew('FileOutputStream', path)
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_7:
                if jinstanceof(_java_exception_7, 'FileNotFoundException'):
                    e = _java_exception_7
                    raise jnew('RuntimeException', 'FastWriter')
                else:
                    raise

        def _java_write_0(self, b):
            b = jcast('byte', b)
            jset(self.buf, ((_java_obj_8 := self), (_java_key_9 := 'ptr'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))), _java_old_10)[4], b)
            if (self.ptr == Code05_NumberSequence2.FastWriter.BUF_SIZE):
                self.innerflush()
            return self

        def _java_write_1(self, s):
            jcall(jcall(s, 'chars'), 'forEach', (lambda c: _java_lambda_11(c, self)))
            return self

        @staticmethod
        def countDigits(l):
            l = jcast('long', l)
            if (l >= 1000000000000000000):
                return jcast('int', 19)
            if (l >= 100000000000000000):
                return jcast('int', 18)
            if (l >= 10000000000000000):
                return jcast('int', 17)
            if (l >= 1000000000000000):
                return jcast('int', 16)
            if (l >= 100000000000000):
                return jcast('int', 15)
            if (l >= 10000000000000):
                return jcast('int', 14)
            if (l >= 1000000000000):
                return jcast('int', 13)
            if (l >= 100000000000):
                return jcast('int', 12)
            if (l >= 10000000000):
                return jcast('int', 11)
            if (l >= 1000000000):
                return jcast('int', 10)
            if (l >= 100000000):
                return jcast('int', 9)
            if (l >= 10000000):
                return jcast('int', 8)
            if (l >= 1000000):
                return jcast('int', 7)
            if (l >= 100000):
                return jcast('int', 6)
            if (l >= 10000):
                return jcast('int', 5)
            if (l >= 1000):
                return jcast('int', 4)
            if (l >= 100):
                return jcast('int', 3)
            if (l >= 10):
                return jcast('int', 2)
            return jcast('int', 1)

        def _java_write_2(self, x):
            x = jcast('long', x)
            if (x == jget(Long, 'MIN_VALUE')):
                return self._java_write_1(jadd('', x))
            if (jcast('int', jadd(self.ptr, 21)) >= Code05_NumberSequence2.FastWriter.BUF_SIZE):
                self.innerflush()
            if (x < 0):
                self._java_write_0(jcast('byte', jchar('-')))
                x = jcast('long', jcast('long', (-x)))
            d = jcast('int', Code05_NumberSequence2.FastWriter.countDigits(x))
            i = jcast('int', jcast('int', (jcast('int', jadd(self.ptr, d)) - 1)))
            while (i >= self.ptr):
                self.buf[i] = jcast('byte', jcast('byte', jcast('long', jadd(jchar('0'), jcast('long', jmod(x, 10))))))
                x = jcast('long', jcast('long', jdiv(x, 10)))
                i = jcast('int', (i - 1))
            self.ptr = jcast('int', jcast('int', jadd(self.ptr, d)))
            return self

        def _java_writeln_0(self, x):
            x = jcast('long', x)
            return jcall(self._java_write_2(x), '_java_writeln_1')

        def _java_writeln_1(self):
            return self._java_write_0(jcast('byte', jchar('\n')))

        def innerflush(self):
            try:
                jcall(self.out, 'write', self.buf, 0, self.ptr)
                self.ptr = jcast('int', 0)
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_15:
                if jinstanceof(_java_exception_15, 'IOException'):
                    e = _java_exception_15
                    raise jnew('RuntimeException', 'innerflush')
                else:
                    raise

        def flush(self):
            self.innerflush()
            try:
                if (self.writer != None):
                    jcall(self.writer, 'write', jcall(jcast('ByteArrayOutputStream', self.out), 'toString'))
                    self.out = jnew('ByteArrayOutputStream')
                    jcall(self.writer, 'flush')
                else:
                    jcall(self.out, 'flush')
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_16:
                if jinstanceof(_java_exception_16, 'IOException'):
                    e = _java_exception_16
                    raise jnew('RuntimeException', 'flush')
                else:
                    raise

        def println(self, x):
            x = jcast('long', x)
            return self._java_writeln_0(x)

        def close(self):
            self.flush()
            try:
                jcall(self.out, 'close')
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_17:
                if jinstanceof(_java_exception_17, 'Exception'):
                    e = _java_exception_17
                    None
                else:
                    raise

        def __init__(self, *args, _java_ctor=None):
            self.buf = jarray('byte', [Code05_NumberSequence2.FastWriter.BUF_SIZE])
            self.out = None
            self.writer = None
            self.ptr = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['Writer'], ['OutputStream'], ['String']], [False, False, False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            if _java_choice == 1:
                return self._java_init_1(*args)
            if _java_choice == 2:
                return self._java_init_2(*args)
            raise TypeError("No matching overload for Code05_NumberSequence2.FastWriter.FastWriter")

        def write(self, *args):
            _java_choice = jselect(args, [['byte'], ['String'], ['long']], [False, False, False])
            if _java_choice == 0:
                return self._java_write_0(*args)
            if _java_choice == 1:
                return self._java_write_1(*args)
            if _java_choice == 2:
                return self._java_write_2(*args)
            raise TypeError("No matching overload for Code05_NumberSequence2.FastWriter.write")

        def writeln(self, *args):
            _java_choice = jselect(args, [['long'], []], [False, False])
            if _java_choice == 0:
                return self._java_writeln_0(*args)
            if _java_choice == 1:
                return self._java_writeln_1(*args)
            raise TypeError("No matching overload for Code05_NumberSequence2.FastWriter.writeln")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


def _java_lambda_11(c, self):
    jset(self.buf, ((_java_obj_12 := self), (_java_key_13 := 'ptr'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))), _java_old_14)[4], jcast('byte', c))
    if (self.ptr == Code05_NumberSequence2.FastWriter.BUF_SIZE):
        self.innerflush()

Code05_NumberSequence2.MAXN = jcast('int', 1000001)
Code05_NumberSequence2.n = jcast('int', 0)
Code05_NumberSequence2.arr = jarray('long', [Code05_NumberSequence2.MAXN])
Code05_NumberSequence2.left = jarray('int', [Code05_NumberSequence2.MAXN])
Code05_NumberSequence2.right = jarray('int', [Code05_NumberSequence2.MAXN])
Code05_NumberSequence2.dist = jarray('int', [Code05_NumberSequence2.MAXN])
Code05_NumberSequence2.father = jarray('int', [Code05_NumberSequence2.MAXN])
Code05_NumberSequence2.from_ = jarray('int', [Code05_NumberSequence2.MAXN])
Code05_NumberSequence2.to = jarray('int', [Code05_NumberSequence2.MAXN])
Code05_NumberSequence2.size = jarray('int', [Code05_NumberSequence2.MAXN])
Code05_NumberSequence2.stack = jarray('int', [Code05_NumberSequence2.MAXN])
Code05_NumberSequence2.ans = jarray('long', [Code05_NumberSequence2.MAXN])
Code05_NumberSequence2.FastWriter.BUF_SIZE = jcast('int', jcast('int', (1 << (13 & 31))))

if __name__ == '__main__':
    Code05_NumberSequence2.main([])
