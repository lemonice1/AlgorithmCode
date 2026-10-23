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

# 可持久化平衡树，FHQ-Treap实现，不用词频压缩，Python版
# 认为一开始是0版本的树，为空树，实现如下操作，操作一共发生n次
# v 1 x : 基于v版本的树，增加一个x，生成新版本的树
# v 2 x : 基于v版本的树，删除一个x，生成新版本的树
# v 3 x : 基于v版本的树，查询x的排名，生成新版本的树状况=v版本状况
# v 4 x : 基于v版本的树，查询数据中排名为x的数，生成新版本的树状况=v版本状况
# v 5 x : 基于v版本的树，查询x的前驱，生成新版本的树状况=v版本状况
# v 6 x : 基于v版本的树，查询x的后继，生成新版本的树状况=v版本状况
# 不管什么操作，都基于某个v版本，操作完成后得到新版本的树，但v版本不会变化
# 如果x的前驱不存在，返回-2^31 + 1，如果x的后继不存在，返回+2^31 - 1
# 1 <= n <= 5 * 10^5
# -10^9 <= x <= +10^9
# 测试链接 : https://www.luogu.com.cn/problem/P3835
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_PersistentFHQTreap2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'cnt': 'cnt', 'head': 'head', 'key': 'key', 'left': 'left', 'right': 'right', 'size': 'size', 'priority': 'priority'}
    MAXN = 0
    MAXM = 0
    cnt = 0
    head = None
    key = None
    left = None
    right = None
    size = None
    priority = None
    @staticmethod
    def copy(i):
        i = jcast('int', i)
        jset(Code05_PersistentFHQTreap2.key, ((_java_obj_1 := Code05_PersistentFHQTreap2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_PersistentFHQTreap2.key[i])
        Code05_PersistentFHQTreap2.left[Code05_PersistentFHQTreap2.cnt] = jcast('int', Code05_PersistentFHQTreap2.left[i])
        Code05_PersistentFHQTreap2.right[Code05_PersistentFHQTreap2.cnt] = jcast('int', Code05_PersistentFHQTreap2.right[i])
        Code05_PersistentFHQTreap2.size[Code05_PersistentFHQTreap2.cnt] = jcast('int', Code05_PersistentFHQTreap2.size[i])
        Code05_PersistentFHQTreap2.priority[Code05_PersistentFHQTreap2.cnt] = jcast('double', Code05_PersistentFHQTreap2.priority[i])
        return jcast('int', Code05_PersistentFHQTreap2.cnt)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code05_PersistentFHQTreap2.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code05_PersistentFHQTreap2.size[Code05_PersistentFHQTreap2.left[i]], Code05_PersistentFHQTreap2.size[Code05_PersistentFHQTreap2.right[i]])), 1)))

    @staticmethod
    def split(l, r, i, num):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            jset(Code05_PersistentFHQTreap2.right, l, jset(Code05_PersistentFHQTreap2.left, r, 0))
        else:
            i = jcast('int', Code05_PersistentFHQTreap2.copy(i))
            if (Code05_PersistentFHQTreap2.key[i] <= num):
                Code05_PersistentFHQTreap2.right[l] = jcast('int', i)
                Code05_PersistentFHQTreap2.split(i, r, Code05_PersistentFHQTreap2.right[i], num)
            else:
                Code05_PersistentFHQTreap2.left[r] = jcast('int', i)
                Code05_PersistentFHQTreap2.split(l, i, Code05_PersistentFHQTreap2.left[i], num)
            Code05_PersistentFHQTreap2.up(i)

    @staticmethod
    def merge(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if ((l == 0) or (r == 0)):
            return jcast('int', jcast('int', jadd(l, r)))
        if (Code05_PersistentFHQTreap2.priority[l] >= Code05_PersistentFHQTreap2.priority[r]):
            l = jcast('int', Code05_PersistentFHQTreap2.copy(l))
            jset(Code05_PersistentFHQTreap2.right, l, Code05_PersistentFHQTreap2.merge(Code05_PersistentFHQTreap2.right[l], r))
            Code05_PersistentFHQTreap2.up(l)
            return jcast('int', l)
        else:
            r = jcast('int', Code05_PersistentFHQTreap2.copy(r))
            jset(Code05_PersistentFHQTreap2.left, r, Code05_PersistentFHQTreap2.merge(l, Code05_PersistentFHQTreap2.left[r]))
            Code05_PersistentFHQTreap2.up(r)
            return jcast('int', r)

    # v : 新生成的版本编号
    # i : 基于的历史版本，树的头节点编号
    # num : 加入的数字
    @staticmethod
    def add(v, i, num):
        v = jcast('int', v)
        i = jcast('int', i)
        num = jcast('int', num)
        Code05_PersistentFHQTreap2.split(0, 0, i, num)
        l = jcast('int', Code05_PersistentFHQTreap2.right[0])
        r = jcast('int', Code05_PersistentFHQTreap2.left[0])
        # 后续可能基于0版本，去生成新版本的树，所以一定要清空，保证0版本始终是空树
        jset(Code05_PersistentFHQTreap2.left, 0, jset(Code05_PersistentFHQTreap2.right, 0, 0))
        jset(Code05_PersistentFHQTreap2.key, ((_java_obj_4 := Code05_PersistentFHQTreap2), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], num)
        Code05_PersistentFHQTreap2.size[Code05_PersistentFHQTreap2.cnt] = jcast('int', 1)
        jset(Code05_PersistentFHQTreap2.priority, Code05_PersistentFHQTreap2.cnt, jstatic('Math', 'random'))
        jset(Code05_PersistentFHQTreap2.head, v, Code05_PersistentFHQTreap2.merge(Code05_PersistentFHQTreap2.merge(l, Code05_PersistentFHQTreap2.cnt), r))

    # v : 新生成的版本编号
    # i : 基于的历史版本，树的头节点编号
    # num : 加入的数字
    @staticmethod
    def remove(v, i, num):
        v = jcast('int', v)
        i = jcast('int', i)
        num = jcast('int', num)
        Code05_PersistentFHQTreap2.split(0, 0, i, num)
        lm = jcast('int', Code05_PersistentFHQTreap2.right[0])
        r = jcast('int', Code05_PersistentFHQTreap2.left[0])
        Code05_PersistentFHQTreap2.split(0, 0, lm, jcast('int', (num - 1)))
        l = jcast('int', Code05_PersistentFHQTreap2.right[0])
        m = jcast('int', Code05_PersistentFHQTreap2.left[0])
        # 后续可能基于0版本，去生成新版本的树，所以一定要清空，保证0版本始终是空树
        jset(Code05_PersistentFHQTreap2.left, 0, jset(Code05_PersistentFHQTreap2.right, 0, 0))
        jset(Code05_PersistentFHQTreap2.head, v, Code05_PersistentFHQTreap2.merge(Code05_PersistentFHQTreap2.merge(l, Code05_PersistentFHQTreap2.merge(Code05_PersistentFHQTreap2.left[m], Code05_PersistentFHQTreap2.right[m])), r))

    @staticmethod
    def small(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', 0)
        if (Code05_PersistentFHQTreap2.key[i] >= num):
            return jcast('int', Code05_PersistentFHQTreap2.small(Code05_PersistentFHQTreap2.left[i], num))
        else:
            return jcast('int', jcast('int', jadd(jcast('int', jadd(Code05_PersistentFHQTreap2.size[Code05_PersistentFHQTreap2.left[i]], 1)), Code05_PersistentFHQTreap2.small(Code05_PersistentFHQTreap2.right[i], num))))

    @staticmethod
    def index(i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        if (Code05_PersistentFHQTreap2.size[Code05_PersistentFHQTreap2.left[i]] >= x):
            return jcast('int', Code05_PersistentFHQTreap2.index(Code05_PersistentFHQTreap2.left[i], x))
        else:
            if (jcast('int', jadd(Code05_PersistentFHQTreap2.size[Code05_PersistentFHQTreap2.left[i]], 1)) < x):
                return jcast('int', Code05_PersistentFHQTreap2.index(Code05_PersistentFHQTreap2.right[i], jcast('int', (jcast('int', (x - Code05_PersistentFHQTreap2.size[Code05_PersistentFHQTreap2.left[i]])) - 1))))
            else:
                return jcast('int', Code05_PersistentFHQTreap2.key[i])

    @staticmethod
    def pre(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', jcast('int', jadd(jget(Integer, 'MIN_VALUE'), 1)))
        if (Code05_PersistentFHQTreap2.key[i] >= num):
            return jcast('int', Code05_PersistentFHQTreap2.pre(Code05_PersistentFHQTreap2.left[i], num))
        else:
            return jcast('int', jstatic('Math', 'max', Code05_PersistentFHQTreap2.key[i], Code05_PersistentFHQTreap2.pre(Code05_PersistentFHQTreap2.right[i], num)))

    @staticmethod
    def post(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', jget(Integer, 'MAX_VALUE'))
        if (Code05_PersistentFHQTreap2.key[i] <= num):
            return jcast('int', Code05_PersistentFHQTreap2.post(Code05_PersistentFHQTreap2.right[i], num))
        else:
            return jcast('int', jstatic('Math', 'min', Code05_PersistentFHQTreap2.key[i], Code05_PersistentFHQTreap2.post(Code05_PersistentFHQTreap2.left[i], num)))

    @staticmethod
    def main(args):
        in_ = Code05_PersistentFHQTreap2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = Code05_PersistentFHQTreap2.FastWriter(jget(System, 'out'), _java_ctor=1)
        n = jcast('int', jcall(in_, 'readInt'))
        i = jcast('int', 1)
        version = 0
        op = 0
        x = 0
        while (i <= n):
            version = jcast('int', jcall(in_, 'readInt'))
            op = jcast('int', jcall(in_, 'readInt'))
            x = jcast('int', jcall(in_, 'readInt'))
            if (op == 1):
                Code05_PersistentFHQTreap2.add(i, Code05_PersistentFHQTreap2.head[version], x)
            else:
                if (op == 2):
                    Code05_PersistentFHQTreap2.remove(i, Code05_PersistentFHQTreap2.head[version], x)
                else:
                    Code05_PersistentFHQTreap2.head[i] = jcast('int', Code05_PersistentFHQTreap2.head[version])
                    if (op == 3):
                        jcall(out, 'println', jcast('int', jadd(Code05_PersistentFHQTreap2.small(Code05_PersistentFHQTreap2.head[i], x), 1)))
                    else:
                        if (op == 4):
                            jcall(out, 'println', Code05_PersistentFHQTreap2.index(Code05_PersistentFHQTreap2.head[i], x))
                        else:
                            if (op == 5):
                                jcall(out, 'println', Code05_PersistentFHQTreap2.pre(Code05_PersistentFHQTreap2.head[i], x))
                            else:
                                jcall(out, 'println', Code05_PersistentFHQTreap2.post(Code05_PersistentFHQTreap2.head[i], x))
            i = jcast('int', (i + 1))
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
                except Exception as _java_exception_7:
                    if jinstanceof(_java_exception_7, 'IOException'):
                        e = _java_exception_7
                        raise jnew('InputMismatchException')
                    else:
                        raise
                if (self.lenbuf <= 0):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', self.inbuf[((_java_obj_8 := self), (_java_key_9 := 'ptrbuf'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))), _java_old_10)[4]])

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
            raise TypeError("No matching overload for Code05_PersistentFHQTreap2.FastReader.FastReader")


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
            except Exception as _java_exception_11:
                if jinstanceof(_java_exception_11, 'FileNotFoundException'):
                    e = _java_exception_11
                    raise jnew('RuntimeException', 'FastWriter')
                else:
                    raise

        def _java_write_0(self, b):
            b = jcast('byte', b)
            jset(self.buf, ((_java_obj_12 := self), (_java_key_13 := 'ptr'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))), _java_old_14)[4], b)
            if (self.ptr == Code05_PersistentFHQTreap2.FastWriter.BUF_SIZE):
                self.innerflush()
            return self

        def _java_write_1(self, s):
            jcall(jcall(s, 'chars'), 'forEach', (lambda c: _java_lambda_15(c, self)))
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
            if (jcast('int', jadd(self.ptr, 21)) >= Code05_PersistentFHQTreap2.FastWriter.BUF_SIZE):
                self.innerflush()
            if (x < 0):
                self._java_write_0(jcast('byte', jchar('-')))
                x = jcast('long', jcast('long', (-x)))
            d = jcast('int', Code05_PersistentFHQTreap2.FastWriter.countDigits(x))
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
            except Exception as _java_exception_19:
                if jinstanceof(_java_exception_19, 'IOException'):
                    e = _java_exception_19
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
            except Exception as _java_exception_20:
                if jinstanceof(_java_exception_20, 'IOException'):
                    e = _java_exception_20
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
            except Exception as _java_exception_21:
                if jinstanceof(_java_exception_21, 'Exception'):
                    e = _java_exception_21
                    None
                else:
                    raise

        def __init__(self, *args, _java_ctor=None):
            self.buf = jarray('byte', [Code05_PersistentFHQTreap2.FastWriter.BUF_SIZE])
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
            raise TypeError("No matching overload for Code05_PersistentFHQTreap2.FastWriter.FastWriter")

        def write(self, *args):
            _java_choice = jselect(args, [['byte'], ['String'], ['long']], [False, False, False])
            if _java_choice == 0:
                return self._java_write_0(*args)
            if _java_choice == 1:
                return self._java_write_1(*args)
            if _java_choice == 2:
                return self._java_write_2(*args)
            raise TypeError("No matching overload for Code05_PersistentFHQTreap2.FastWriter.write")

        def writeln(self, *args):
            _java_choice = jselect(args, [['long'], []], [False, False])
            if _java_choice == 0:
                return self._java_writeln_0(*args)
            if _java_choice == 1:
                return self._java_writeln_1(*args)
            raise TypeError("No matching overload for Code05_PersistentFHQTreap2.FastWriter.writeln")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


def _java_lambda_15(c, self):
    jset(self.buf, ((_java_obj_16 := self), (_java_key_17 := 'ptr'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))), _java_old_18)[4], jcast('byte', c))
    if (self.ptr == Code05_PersistentFHQTreap2.FastWriter.BUF_SIZE):
        self.innerflush()

Code05_PersistentFHQTreap2.MAXN = jcast('int', 500001)
Code05_PersistentFHQTreap2.MAXM = jcast('int', jcast('int', (Code05_PersistentFHQTreap2.MAXN * 50)))
Code05_PersistentFHQTreap2.cnt = jcast('int', 0)
Code05_PersistentFHQTreap2.head = jarray('int', [Code05_PersistentFHQTreap2.MAXN])
Code05_PersistentFHQTreap2.key = jarray('int', [Code05_PersistentFHQTreap2.MAXM])
Code05_PersistentFHQTreap2.left = jarray('int', [Code05_PersistentFHQTreap2.MAXM])
Code05_PersistentFHQTreap2.right = jarray('int', [Code05_PersistentFHQTreap2.MAXM])
Code05_PersistentFHQTreap2.size = jarray('int', [Code05_PersistentFHQTreap2.MAXM])
Code05_PersistentFHQTreap2.priority = jarray('double', [Code05_PersistentFHQTreap2.MAXM])
Code05_PersistentFHQTreap2.FastWriter.BUF_SIZE = jcast('int', jcast('int', (1 << (13 & 31))))

if __name__ == '__main__':
    Code05_PersistentFHQTreap2.main([])
