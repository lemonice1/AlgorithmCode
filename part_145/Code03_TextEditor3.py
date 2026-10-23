# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 文本编辑器，优化数组扩容与输入输出的 Python 版本
# 一开始文本为空，光标在文本开头，也就是1位置，请实现如下6种操作
# Move k     : 将光标移动到第k个字符之后，操作保证光标不会到非法位置
# Insert n s : 在光标处插入长度为n的字符串s，光标位置不变
# Delete n   : 删除光标后的n个字符，光标位置不变，操作保证有足够字符
# Get n      : 输出光标后的n个字符，光标位置不变，操作保证有足够字符
# Prev       : 光标前移一个字符，操作保证光标不会到非法位置
# Next       : 光标后移一个字符，操作保证光标不会到非法位置
# Insert操作时，字符串s中ASCII码在[32,126]范围上的字符一定有n个，其他字符请过滤掉
# 测试链接 : https://www.luogu.com.cn/problem/P4008
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本版本自行维护数组扩容与输入输出，重点在于减少额外开销
# 讲解172，讲解块状链表时，本题又讲了一遍，分块的方法，更有学习意义
class Code03_TextEditor3:
    __java_fields__ = {'is': 'is_', 'inbuf': 'inbuf', 'str': 'str', 'lenbuf': 'lenbuf', 'ptrbuf': 'ptrbuf', 'b': 'b', 'out': 'out', 'key': 'key', 'lc': 'lc', 'rc': 'rc', 'sz': 'sz', 'priority': 'priority', 'head': 'head', 'no': 'no'}
    is_ = None
    inbuf = None
    str = None
    lenbuf = 0
    ptrbuf = 0
    b = 0
    out = None
    key = None
    lc = None
    rc = None
    sz = None
    priority = None
    head = 0
    no = 0
    @staticmethod
    def create(k):
        k = jcast('byte', k)
        if (((_java_obj_1 := Code03_TextEditor3), (_java_key_2 := 'no'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3] == jget(Code03_TextEditor3.key, 'length')):
            Code03_TextEditor3.key = jstatic('Arrays', 'copyOf', Code03_TextEditor3.key, jcast('int', (Code03_TextEditor3.no << (1 & 31))))
            Code03_TextEditor3.lc = jstatic('Arrays', 'copyOf', Code03_TextEditor3.lc, jcast('int', (Code03_TextEditor3.no << (1 & 31))))
            Code03_TextEditor3.rc = jstatic('Arrays', 'copyOf', Code03_TextEditor3.rc, jcast('int', (Code03_TextEditor3.no << (1 & 31))))
            Code03_TextEditor3.sz = jstatic('Arrays', 'copyOf', Code03_TextEditor3.sz, jcast('int', (Code03_TextEditor3.no << (1 & 31))))
            Code03_TextEditor3.priority = jstatic('Arrays', 'copyOf', Code03_TextEditor3.priority, jcast('int', (Code03_TextEditor3.no << (1 & 31))))
        Code03_TextEditor3.key[Code03_TextEditor3.no] = jcast('byte', k)
        Code03_TextEditor3.sz[Code03_TextEditor3.no] = jcast('int', 1)
        jset(Code03_TextEditor3.priority, Code03_TextEditor3.no, jstatic('Math', 'random'))
        return jcast('int', Code03_TextEditor3.no)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code03_TextEditor3.sz[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code03_TextEditor3.sz[Code03_TextEditor3.lc[i]], Code03_TextEditor3.sz[Code03_TextEditor3.rc[i]])), 1)))

    @staticmethod
    def split(l, r, i, rk):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rk = jcast('int', rk)
        if (i == 0):
            jset(Code03_TextEditor3.rc, l, jset(Code03_TextEditor3.lc, r, 0))
            return
        if (jcast('int', jadd(Code03_TextEditor3.sz[Code03_TextEditor3.lc[i]], 1)) <= rk):
            Code03_TextEditor3.rc[l] = jcast('int', i)
            Code03_TextEditor3.split(i, r, Code03_TextEditor3.rc[i], jcast('int', (jcast('int', (rk - Code03_TextEditor3.sz[Code03_TextEditor3.lc[i]])) - 1)))
        else:
            Code03_TextEditor3.lc[r] = jcast('int', i)
            Code03_TextEditor3.split(l, i, Code03_TextEditor3.lc[i], rk)
        Code03_TextEditor3.up(i)

    @staticmethod
    def merge(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if ((l == 0) or (r == 0)):
            return jcast('int', jcast('int', jadd(l, r)))
        if (Code03_TextEditor3.priority[l] >= Code03_TextEditor3.priority[r]):
            jset(Code03_TextEditor3.rc, l, Code03_TextEditor3.merge(Code03_TextEditor3.rc[l], r))
            Code03_TextEditor3.up(l)
            return jcast('int', l)
        else:
            jset(Code03_TextEditor3.lc, r, Code03_TextEditor3.merge(l, Code03_TextEditor3.lc[r]))
            Code03_TextEditor3.up(r)
            return jcast('int', r)

    @staticmethod
    def inorder(i):
        i = jcast('int', i)
        if (i == 0):
            return
        Code03_TextEditor3.inorder(Code03_TextEditor3.lc[i])
        jcall(Code03_TextEditor3.out, '_java_write_0', Code03_TextEditor3.key[i])
        Code03_TextEditor3.inorder(Code03_TextEditor3.rc[i])

    @staticmethod
    def main(args):
        Code03_TextEditor3.key = jarray('byte', [1])
        Code03_TextEditor3.lc = jarray('int', [1])
        Code03_TextEditor3.rc = jarray('int', [1])
        Code03_TextEditor3.sz = jarray('int', [1])
        Code03_TextEditor3.priority = jarray('double', [1])
        i = jcast('int', 0)
        n = 0
        l = 0
        r = 0
        lx = 0
        mx = 0
        rx = 0
        c = 0
        op = jcast('int', Code03_TextEditor3.nextInt())
        while (((_java_old_4 := op), (op := jcast('int', (op + (-1)))), _java_old_4)[2] > 0):
            try:
                _java_switch_6 = Code03_TextEditor3.next()
                _java_case_7 = 5
                if _java_switch_6 == (jchar('M')):
                    _java_case_7 = 0
                elif _java_switch_6 == (jchar('I')):
                    _java_case_7 = 1
                elif _java_switch_6 == (jchar('D')):
                    _java_case_7 = 2
                elif _java_switch_6 == (jchar('G')):
                    _java_case_7 = 3
                elif _java_switch_6 == (jchar('P')):
                    _java_case_7 = 4
                try:
                    if _java_case_7 <= 0:
                        i = jcast('int', Code03_TextEditor3.nextInt())
                        raise JBreak(None)
                    if _java_case_7 <= 1:
                        Code03_TextEditor3.split(0, 0, Code03_TextEditor3.head, i)
                        l = jcast('int', Code03_TextEditor3.rc[0])
                        r = jcast('int', Code03_TextEditor3.lc[0])
                        n = jcast('int', Code03_TextEditor3.nextInt())
                        while (n > 0):
                            try:
                                c = jcast('byte', Code03_TextEditor3.readByte())
                                if (c < 32):
                                    raise JContinue(None)
                                l = jcast('int', Code03_TextEditor3.merge(l, Code03_TextEditor3.create(c)))
                                n = jcast('int', (n - 1))
                            except JContinue as _java_control_9:
                                if _java_control_9.label not in (None,):
                                    raise
                            except JBreak as _java_control_9:
                                if _java_control_9.label not in (None,):
                                    raise
                                break
                        Code03_TextEditor3.head = jcast('int', Code03_TextEditor3.merge(l, r))
                        raise JBreak(None)
                    if _java_case_7 <= 2:
                        n = jcast('int', Code03_TextEditor3.nextInt())
                        l = jcast('int', jcast('int', jadd(i, 1)))
                        r = jcast('int', jcast('int', jadd(i, n)))
                        Code03_TextEditor3.split(0, 0, Code03_TextEditor3.head, i)
                        lx = jcast('int', Code03_TextEditor3.rc[0])
                        mx = jcast('int', Code03_TextEditor3.lc[0])
                        Code03_TextEditor3.split(0, 0, mx, n)
                        mx = jcast('int', Code03_TextEditor3.rc[0])
                        rx = jcast('int', Code03_TextEditor3.lc[0])
                        Code03_TextEditor3.head = jcast('int', Code03_TextEditor3.merge(lx, rx))
                        raise JBreak(None)
                    if _java_case_7 <= 3:
                        n = jcast('int', Code03_TextEditor3.nextInt())
                        l = jcast('int', jcast('int', jadd(i, 1)))
                        r = jcast('int', jcast('int', jadd(i, n)))
                        Code03_TextEditor3.split(0, 0, Code03_TextEditor3.head, i)
                        lx = jcast('int', Code03_TextEditor3.rc[0])
                        mx = jcast('int', Code03_TextEditor3.lc[0])
                        Code03_TextEditor3.split(0, 0, mx, n)
                        mx = jcast('int', Code03_TextEditor3.rc[0])
                        rx = jcast('int', Code03_TextEditor3.lc[0])
                        Code03_TextEditor3.inorder(mx)
                        jcall(Code03_TextEditor3.out, 'writeln')
                        Code03_TextEditor3.head = jcast('int', Code03_TextEditor3.merge(Code03_TextEditor3.merge(lx, mx), rx))
                        raise JBreak(None)
                    if _java_case_7 <= 4:
                        i = jcast('int', (i - 1))
                        raise JBreak(None)
                    if _java_case_7 <= 5:
                        i = jcast('int', (i + 1))
                        raise JBreak(None)
                except JBreak as _java_break_8:
                    if _java_break_8.label not in (None,):
                        raise
            except JContinue as _java_control_5:
                if _java_control_5.label not in (None,):
                    raise
            except JBreak as _java_control_5:
                if _java_control_5.label not in (None,):
                    raise
                break
        jcall(Code03_TextEditor3.out, 'flush')

    @staticmethod
    def readByte():
        if (Code03_TextEditor3.ptrbuf == Code03_TextEditor3.lenbuf):
            Code03_TextEditor3.ptrbuf = jcast('int', 0)
            try:
                Code03_TextEditor3.lenbuf = jcast('int', jcall(Code03_TextEditor3.is_, 'read', Code03_TextEditor3.inbuf))
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_10:
                if jinstanceof(_java_exception_10, 'Exception'):
                    e = _java_exception_10
                    None
                else:
                    raise
            if (Code03_TextEditor3.lenbuf <= 0):
                return jcast('byte', jcast('int', (-1)))
        return jcast('byte', Code03_TextEditor3.inbuf[((_java_obj_11 := Code03_TextEditor3), (_java_key_12 := 'ptrbuf'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]])

    @staticmethod
    def next():
        while (jset(Code03_TextEditor3, 'b', Code03_TextEditor3.readByte()) < 33):
            None
        i = jcast('int', 0)
        while (Code03_TextEditor3.b > 32):
            jset(Code03_TextEditor3.str, ((_java_old_14 := i), (i := jcast('int', (i + (1)))), _java_old_14)[2], jcast('char', Code03_TextEditor3.b))
            Code03_TextEditor3.b = jcast('int', Code03_TextEditor3.readByte())
        return jcast('char', Code03_TextEditor3.str[0])

    @staticmethod
    def nextInt():
        while (jset(Code03_TextEditor3, 'b', Code03_TextEditor3.readByte()) < 33):
            None
        num = jcast('int', jcast('int', (Code03_TextEditor3.b - jchar('0'))))
        while (jset(Code03_TextEditor3, 'b', Code03_TextEditor3.readByte()) > 32):
            num = jcast('int', jcast('int', jadd(jcast('int', (num * 10)), jcast('int', (Code03_TextEditor3.b - jchar('0'))))))
        return jcast('int', num)

    class FastWriter:
        __java_fields__ = {'out': 'out', 'tr': 'tr', 'BUF_SIZE': 'BUF_SIZE', 'buf': 'buf'}
        # out：实例字段，在构造函数中初始化。
        # tr：实例字段，在构造函数中初始化。
        # BUF_SIZE：实例字段，在构造函数中初始化。
        # buf：实例字段，在构造函数中初始化。
        def _java_countDigits_0(self, v):
            v = jcast('int', v)
            return jcast('int', ((((10 if (v >= 1000000000) else 9) if (v >= 100000000) else 8) if (v >= 10000000) else (7 if (v >= 1000000) else 6)) if (v >= 100000) else ((5 if (v >= 10000) else 4) if (v >= 1000) else (3 if (v >= 100) else (2 if (v >= 10) else 1)))))

        def _java_countDigits_1(self, v):
            v = jcast('long', v)
            return jcast('int', (jcast('int', jadd(10, self._java_countDigits_0(jcast('int', jcast('long', jdiv(v, 10000000000)))))) if (v >= 10000000000) else (10 if (v >= 1000000000) else self._java_countDigits_0(jcast('int', v)))))

        def _java_write_0(self, b):
            b = jcast('byte', b)
            jset(self.buf, ((_java_obj_15 := self), (_java_key_16 := 'tr'), (_java_old_17 := jget(_java_obj_15, _java_key_16)), jset(_java_obj_15, _java_key_16, jcast('int', (_java_old_17 + (1)))), _java_old_17)[4], b)
            if (self.tr == self.BUF_SIZE):
                self.innerflush()
            return self

        def _java_write_1(self, c):
            c = jcast('char', c)
            return self._java_write_0(jcast('byte', c))

        def _java_write_2(self, x):
            x = jcast('int', x)
            if (x == jget(Integer, 'MIN_VALUE')):
                return self._java_write_3(jcast('long', x))
            if (jcast('int', jadd(self.tr, 12)) >= self.BUF_SIZE):
                self.innerflush()
            if (x < 0):
                self._java_write_0(jcast('byte', jchar('-')))
                x = jcast('int', jcast('int', (-x)))
            d = jcast('int', self._java_countDigits_0(x))
            i = jcast('int', jcast('int', (jcast('int', jadd(self.tr, d)) - 1)))
            while (i >= self.tr):
                self.buf[i] = jcast('byte', jcast('byte', jcast('int', jadd(jchar('0'), jcast('int', jmod(x, 10))))))
                x = jcast('int', jcast('int', jdiv(x, 10)))
                i = jcast('int', (i - 1))
            self.tr = jcast('int', jcast('int', jadd(self.tr, d)))
            return self

        def _java_write_3(self, x):
            x = jcast('long', x)
            if (x == jget(Long, 'MIN_VALUE')):
                return self._java_write_5(jadd('', x))
            if (jcast('int', jadd(self.tr, 21)) >= self.BUF_SIZE):
                self.innerflush()
            if (x < 0):
                self._java_write_0(jcast('byte', jchar('-')))
                x = jcast('long', jcast('long', (-x)))
            d = jcast('int', self._java_countDigits_1(x))
            i = jcast('int', jcast('int', (jcast('int', jadd(self.tr, d)) - 1)))
            while (i >= self.tr):
                self.buf[i] = jcast('byte', jcast('byte', jcast('long', jadd(jchar('0'), jcast('long', jmod(x, 10))))))
                x = jcast('long', jcast('long', jdiv(x, 10)))
                i = jcast('int', (i - 1))
            self.tr = jcast('int', jcast('int', jadd(self.tr, d)))
            return self

        def _java_write_4(self, x, precision):
            x = jcast('double', x)
            precision = jcast('int', precision)
            if (x < 0):
                self._java_write_1(jchar('-'))
                x = jcast('double', (-x))
            x = jcast('double', jadd(x, jdiv(jstatic('Math', 'pow', 10, jcast('int', (-precision))), 2)))
            jcall(self._java_write_3(jcast('long', x)), '_java_write_5', '.')
            x = jcast('double', (x - jcast('long', x)))
            i = jcast('int', 0)
            while (i < precision):
                x = jcast('double', (x * 10))
                self._java_write_1(jcast('char', jcast('int', jadd(jchar('0'), jcast('int', x)))))
                x = jcast('double', (x - jcast('int', x)))
                i = jcast('int', (i + 1))
            return self

        def _java_write_5(self, s):
            i = jcast('int', 0)
            while (i < jcall(s, 'length')):
                jset(self.buf, ((_java_obj_18 := self), (_java_key_19 := 'tr'), (_java_old_20 := jget(_java_obj_18, _java_key_19)), jset(_java_obj_18, _java_key_19, jcast('int', (_java_old_20 + (1)))), _java_old_20)[4], jcast('byte', jcall(s, 'charAt', i)))
                if (self.tr == self.BUF_SIZE):
                    self.innerflush()
                i = jcast('int', (i + 1))
            return self

        def _java_print_0(self, c):
            c = jcast('char', c)
            self._java_write_1(c)

        def _java_print_1(self, s):
            self._java_write_5(s)

        def _java_print_2(self, x):
            x = jcast('int', x)
            self._java_write_2(x)

        def _java_print_3(self, x):
            x = jcast('long', x)
            self._java_write_3(x)

        def _java_print_4(self, x, precision):
            x = jcast('double', x)
            precision = jcast('int', precision)
            self._java_write_4(x, precision)

        def writeln(self):
            self._java_write_0(jcast('byte', jchar('\n')))

        def _java_println_0(self, c):
            c = jcast('char', c)
            jcall(self._java_write_1(c), 'writeln')

        def _java_println_1(self, x):
            x = jcast('int', x)
            jcall(self._java_write_2(x), 'writeln')

        def _java_println_2(self, x):
            x = jcast('long', x)
            jcall(self._java_write_3(x), 'writeln')

        def _java_println_3(self, x, precision):
            x = jcast('double', x)
            precision = jcast('int', precision)
            jcall(self._java_write_4(x, precision), 'writeln')

        def _java_println_4(self, s):
            jcall(self._java_write_5(s), 'writeln')

        def innerflush(self):
            try:
                jcall(self.out, 'write', self.buf, 0, self.tr)
                self.tr = jcast('int', 0)
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_21:
                if jinstanceof(_java_exception_21, 'Exception'):
                    e = _java_exception_21
                    None
                else:
                    raise

        def flush(self):
            self.innerflush()
            try:
                jcall(self.out, 'flush')
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_22:
                if jinstanceof(_java_exception_22, 'Exception'):
                    e = _java_exception_22
                    None
                else:
                    raise

        def __init__(self, *args, _java_ctor=None):
            self.out = jget(System, 'out')
            self.tr = jcast('int', 0)
            self.BUF_SIZE = jcast('int', 8192)
            self.buf = jarray('byte', [self.BUF_SIZE])
            if args:
                raise TypeError('This class has a no-argument constructor')

        def countDigits(self, *args):
            _java_choice = jselect(args, [['int'], ['long']], [False, False])
            if _java_choice == 0:
                return self._java_countDigits_0(*args)
            if _java_choice == 1:
                return self._java_countDigits_1(*args)
            raise TypeError("No matching overload for Code03_TextEditor3.FastWriter.countDigits")

        def write(self, *args):
            _java_choice = jselect(args, [['byte'], ['char'], ['int'], ['long'], ['double', 'int'], ['String']], [False, False, False, False, False, False])
            if _java_choice == 0:
                return self._java_write_0(*args)
            if _java_choice == 1:
                return self._java_write_1(*args)
            if _java_choice == 2:
                return self._java_write_2(*args)
            if _java_choice == 3:
                return self._java_write_3(*args)
            if _java_choice == 4:
                return self._java_write_4(*args)
            if _java_choice == 5:
                return self._java_write_5(*args)
            raise TypeError("No matching overload for Code03_TextEditor3.FastWriter.write")

        def print(self, *args):
            _java_choice = jselect(args, [['char'], ['String'], ['int'], ['long'], ['double', 'int']], [False, False, False, False, False])
            if _java_choice == 0:
                return self._java_print_0(*args)
            if _java_choice == 1:
                return self._java_print_1(*args)
            if _java_choice == 2:
                return self._java_print_2(*args)
            if _java_choice == 3:
                return self._java_print_3(*args)
            if _java_choice == 4:
                return self._java_print_4(*args)
            raise TypeError("No matching overload for Code03_TextEditor3.FastWriter.print")

        def println(self, *args):
            _java_choice = jselect(args, [['char'], ['int'], ['long'], ['double', 'int'], ['String']], [False, False, False, False, False])
            if _java_choice == 0:
                return self._java_println_0(*args)
            if _java_choice == 1:
                return self._java_println_1(*args)
            if _java_choice == 2:
                return self._java_println_2(*args)
            if _java_choice == 3:
                return self._java_println_3(*args)
            if _java_choice == 4:
                return self._java_println_4(*args)
            raise TypeError("No matching overload for Code03_TextEditor3.FastWriter.println")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_TextEditor3.is_ = jget(System, 'in')
Code03_TextEditor3.inbuf = jarray('byte', [1024])
Code03_TextEditor3.str = jarray('char', [16])
Code03_TextEditor3.lenbuf = jcast('int', 0)
Code03_TextEditor3.ptrbuf = jcast('int', 0)
Code03_TextEditor3.b = jcast('int', 0)
Code03_TextEditor3.out = Code03_TextEditor3.FastWriter()
Code03_TextEditor3.key = None
Code03_TextEditor3.lc = None
Code03_TextEditor3.rc = None
Code03_TextEditor3.sz = None
Code03_TextEditor3.priority = None
Code03_TextEditor3.head = jcast('int', 0)
Code03_TextEditor3.no = jcast('int', 0)

if __name__ == '__main__':
    Code03_TextEditor3.main([])
