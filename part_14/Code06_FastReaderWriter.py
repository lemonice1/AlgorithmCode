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

# 本文件课上没有讲
# FastReader 和 FastWriter 保留分块输入输出接口，底层调用 Python 字节流
# 如何使用可以参考main函数
class Code06_FastReaderWriter:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        reader = Code06_FastReaderWriter.FastReader(jget(System, 'in'), _java_ctor=0)
        writer = Code06_FastReaderWriter.FastWriter(jget(System, 'out'), _java_ctor=1)
        jprint('输入一个字符：', newline=True)
        # reader会读到字符的ASCII码
        cha = jcast('int', jcall(reader, 'readByte'))
        jprint('输入一个int类型的数字：', newline=True)
        # reader会读到该数字
        num1 = jcast('int', jcall(reader, 'readInt'))
        jprint('输入一个long类型的数字：', newline=True)
        # reader会读到该数字
        num2 = jcast('long', jcall(reader, 'readLong'))
        jprint('打印结果:', newline=True)
        jcall(writer, 'println', cha)
        jcall(writer, 'println', num1)
        jcall(writer, 'println', num2)
        # close方法包含flush，会把结果刷出去
        jcall(writer, 'close')

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
                except Exception as _java_exception_1:
                    if jinstanceof(_java_exception_1, 'IOException'):
                        e = _java_exception_1
                        raise jnew('InputMismatchException')
                    else:
                        raise
                if (self.lenbuf <= 0):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', self.inbuf[((_java_obj_2 := self), (_java_key_3 := 'ptrbuf'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))), _java_old_4)[4]])

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
            raise TypeError("No matching overload for Code06_FastReaderWriter.FastReader.FastReader")


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
            except Exception as _java_exception_5:
                if jinstanceof(_java_exception_5, 'FileNotFoundException'):
                    e = _java_exception_5
                    raise jnew('RuntimeException', 'FastWriter')
                else:
                    raise

        def _java_write_0(self, b):
            b = jcast('byte', b)
            jset(self.buf, ((_java_obj_6 := self), (_java_key_7 := 'ptr'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))), _java_old_8)[4], b)
            if (self.ptr == Code06_FastReaderWriter.FastWriter.BUF_SIZE):
                self.innerflush()
            return self

        def _java_write_1(self, s):
            jcall(jcall(s, 'chars'), 'forEach', (lambda c: _java_lambda_9(c, self)))
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
            if (jcast('int', jadd(self.ptr, 21)) >= Code06_FastReaderWriter.FastWriter.BUF_SIZE):
                self.innerflush()
            if (x < 0):
                self._java_write_0(jcast('byte', jchar('-')))
                x = jcast('long', jcast('long', (-x)))
            d = jcast('int', Code06_FastReaderWriter.FastWriter.countDigits(x))
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
            except Exception as _java_exception_13:
                if jinstanceof(_java_exception_13, 'IOException'):
                    e = _java_exception_13
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
            except Exception as _java_exception_14:
                if jinstanceof(_java_exception_14, 'IOException'):
                    e = _java_exception_14
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
            except Exception as _java_exception_15:
                if jinstanceof(_java_exception_15, 'Exception'):
                    e = _java_exception_15
                    None
                else:
                    raise

        def __init__(self, *args, _java_ctor=None):
            self.buf = jarray('byte', [Code06_FastReaderWriter.FastWriter.BUF_SIZE])
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
            raise TypeError("No matching overload for Code06_FastReaderWriter.FastWriter.FastWriter")

        def write(self, *args):
            _java_choice = jselect(args, [['byte'], ['String'], ['long']], [False, False, False])
            if _java_choice == 0:
                return self._java_write_0(*args)
            if _java_choice == 1:
                return self._java_write_1(*args)
            if _java_choice == 2:
                return self._java_write_2(*args)
            raise TypeError("No matching overload for Code06_FastReaderWriter.FastWriter.write")

        def writeln(self, *args):
            _java_choice = jselect(args, [['long'], []], [False, False])
            if _java_choice == 0:
                return self._java_writeln_0(*args)
            if _java_choice == 1:
                return self._java_writeln_1(*args)
            raise TypeError("No matching overload for Code06_FastReaderWriter.FastWriter.writeln")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


def _java_lambda_9(c, self):
    jset(self.buf, ((_java_obj_10 := self), (_java_key_11 := 'ptr'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4], jcast('byte', c))
    if (self.ptr == Code06_FastReaderWriter.FastWriter.BUF_SIZE):
        self.innerflush()

Code06_FastReaderWriter.FastWriter.BUF_SIZE = jcast('int', jcast('int', (1 << (13 & 31))))

if __name__ == '__main__':
    Code06_FastReaderWriter.main([])
