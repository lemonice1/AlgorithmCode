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

# 断罪者，删除任意编号节点，Python版
# 给定t，w，k，表示一共有t个人，死亡方式都为w，地狱阈值都为k，w和k含义稍后解释
# 每个人都给定n和m，表示这人一生有n件错事，有m次领悟
# 这个人的n件错事，给定对应的n个罪恶值，然后给定m次领悟，领悟类型如下
# 2 a   : 第a件错事的罪恶值变成0
# 3 a b : 第a件错事所在的集合中，最大罪恶值的错事，罪恶值减少b
# 如果减少后罪恶值变成负数，认为这件错事的罪恶值变为0
# 如果集合中，两件错事都是最大的罪恶值，取编号较小的错事
# 4 a b : 第a件错事所在的集合与第b件错事所在的集合合并
# 一个错事集合的罪恶值 = 这个集合中的最大罪恶值，只取一个
# 一个人的罪恶值 = 这个人所有错事集合的罪恶值累加起来
# 然后根据死亡方式w，对每个人的罪恶值做最后调整，然后打印这个人的下场
# 如果w==1，不调整
# 如果w==2，人的罪恶值 -= 错事集合的罪恶值中的最大值
# 如果w==3，人的罪恶值 += 错事集合的罪恶值中的最大值
# 如果一个人的罪恶值 == 0，打印"Gensokyo 0"
# 如果一个人的罪恶值  > k，打印"Hell "，然后打印罪恶值
# 如果一个人的罪恶值 <= k，打印"Heaven "，然后打印罪恶值
# 一共有t个人，所以最终会有t次打印
# 1 <= t <= 30
# 1 <= n <= 2 * 10^6
# 错事罪恶值可能很大，输入保证每个人的罪恶值用long类型不溢出
# 测试链接 : https://www.luogu.com.cn/problem/P4971
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Convict2:
    __java_fields__ = {'MAXN': 'MAXN', 't': 't', 'w': 'w', 'n': 'n', 'm': 'm', 'k': 'k', 'num': 'num', 'up': 'up', 'left': 'left', 'right': 'right', 'dist': 'dist', 'father': 'father'}
    MAXN = 0
    t = 0
    w = 0
    n = 0
    m = 0
    k = 0
    num = None
    # up[i]表示节点i在左偏树结构上的父亲节点
    up = None
    left = None
    right = None
    dist = None
    # father[i]表示并查集里节点i的路径信息
    father = None
    @staticmethod
    def prepare():
        Code02_Convict2.dist[0] = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= Code02_Convict2.n):
            jset(Code02_Convict2.up, i, jset(Code02_Convict2.left, i, jset(Code02_Convict2.right, i, jset(Code02_Convict2.dist, i, 0))))
            Code02_Convict2.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        jset(Code02_Convict2.father, i, (i if (Code02_Convict2.father[i] == i) else Code02_Convict2.find(Code02_Convict2.father[i])))
        return jcast('int', Code02_Convict2.father[i])

    @staticmethod
    def merge(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if ((i == 0) or (j == 0)):
            return jcast('int', jcast('int', jadd(i, j)))
        tmp = 0
        # 维护大根堆，如果值一样，编号小的节点做头
        if ((Code02_Convict2.num[i] < Code02_Convict2.num[j]) or ((Code02_Convict2.num[i] == Code02_Convict2.num[j]) and (i > j))):
            tmp = jcast('int', i)
            i = jcast('int', j)
            j = jcast('int', tmp)
        jset(Code02_Convict2.right, i, Code02_Convict2.merge(Code02_Convict2.right[i], j))
        # 设置up信息
        jset(Code02_Convict2.up, Code02_Convict2.right[i], i)
        if (Code02_Convict2.dist[Code02_Convict2.left[i]] < Code02_Convict2.dist[Code02_Convict2.right[i]]):
            tmp = jcast('int', Code02_Convict2.left[i])
            Code02_Convict2.left[i] = jcast('int', Code02_Convict2.right[i])
            Code02_Convict2.right[i] = jcast('int', tmp)
        Code02_Convict2.dist[i] = jcast('int', jcast('int', jadd(Code02_Convict2.dist[Code02_Convict2.right[i]], 1)))
        jset(Code02_Convict2.father, Code02_Convict2.left[i], jset(Code02_Convict2.father, Code02_Convict2.right[i], i))
        return jcast('int', i)

    # 节点i是所在左偏树的任意节点，删除节点i，返回整棵树的头节点编号
    @staticmethod
    def remove(i):
        i = jcast('int', i)
        h = jcast('int', Code02_Convict2.find(i))
        jset(Code02_Convict2.father, Code02_Convict2.left[i], Code02_Convict2.left[i])
        jset(Code02_Convict2.father, Code02_Convict2.right[i], Code02_Convict2.right[i])
        s = jcast('int', Code02_Convict2.merge(Code02_Convict2.left[i], Code02_Convict2.right[i]))
        f = jcast('int', Code02_Convict2.up[i])
        Code02_Convict2.father[i] = jcast('int', s)
        Code02_Convict2.up[s] = jcast('int', f)
        if (h != i):
            Code02_Convict2.father[s] = jcast('int', h)
            if (Code02_Convict2.left[f] == i):
                Code02_Convict2.left[f] = jcast('int', s)
            else:
                Code02_Convict2.right[f] = jcast('int', s)
            d = jcast('int', Code02_Convict2.dist[s])
            tmp = 0
            while (Code02_Convict2.dist[f] > jcast('int', jadd(d, 1))):
                Code02_Convict2.dist[f] = jcast('int', jcast('int', jadd(d, 1)))
                if (Code02_Convict2.dist[Code02_Convict2.left[f]] < Code02_Convict2.dist[Code02_Convict2.right[f]]):
                    tmp = jcast('int', Code02_Convict2.left[f])
                    Code02_Convict2.left[f] = jcast('int', Code02_Convict2.right[f])
                    Code02_Convict2.right[f] = jcast('int', tmp)
                f = jcast('int', Code02_Convict2.up[f])
                d = jcast('int', (d + 1))
        jset(Code02_Convict2.up, i, jset(Code02_Convict2.left, i, jset(Code02_Convict2.right, i, jset(Code02_Convict2.dist, i, 0))))
        return jcast('int', Code02_Convict2.father[s])

    @staticmethod
    def reduce(i, v):
        i = jcast('int', i)
        v = jcast('long', v)
        h = jcast('int', Code02_Convict2.remove(i))
        jset(Code02_Convict2.num, i, jstatic('Math', 'max', jcast('long', (Code02_Convict2.num[i] - v)), 0))
        jset(Code02_Convict2.father, h, jset(Code02_Convict2.father, i, Code02_Convict2.merge(h, i)))

    @staticmethod
    def compute():
        ans = jcast('long', 0)
        max = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code02_Convict2.n):
            if (Code02_Convict2.father[i] == i):
                ans = jcast('long', jcast('long', jadd(ans, Code02_Convict2.num[i])))
                max = jcast('long', jstatic('Math', 'max', max, Code02_Convict2.num[i]))
            i = jcast('int', (i + 1))
        if (Code02_Convict2.w == 2):
            ans = jcast('long', jcast('long', (ans - max)))
        else:
            if (Code02_Convict2.w == 3):
                ans = jcast('long', jcast('long', jadd(ans, max)))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code02_Convict2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = Code02_Convict2.FastWriter(jget(System, 'out'), _java_ctor=1)
        Code02_Convict2.t = jcast('int', jcall(in_, 'readInt'))
        Code02_Convict2.w = jcast('int', jcall(in_, 'readInt'))
        Code02_Convict2.k = jcast('long', jcall(in_, 'readLong'))
        i = jcast('int', 1)
        while (i <= Code02_Convict2.t):
            Code02_Convict2.n = jcast('int', jcall(in_, 'readInt'))
            Code02_Convict2.m = jcast('int', jcall(in_, 'readInt'))
            Code02_Convict2.prepare()
            j = jcast('int', 1)
            while (j <= Code02_Convict2.n):
                jset(Code02_Convict2.num, j, jcall(in_, 'readLong'))
                j = jcast('int', (j + 1))
            j = jcast('int', 1)
            op = 0
            a = 0
            b = 0
            while (j <= Code02_Convict2.m):
                op = jcast('int', jcall(in_, 'readInt'))
                a = jcast('int', jcall(in_, 'readInt'))
                if (op == 2):
                    Code02_Convict2.reduce(a, Code02_Convict2.num[a])
                else:
                    if (op == 3):
                        b = jcast('int', jcall(in_, 'readInt'))
                        Code02_Convict2.reduce(Code02_Convict2.find(a), b)
                    else:
                        b = jcast('int', jcall(in_, 'readInt'))
                        l = jcast('int', Code02_Convict2.find(a))
                        r = jcast('int', Code02_Convict2.find(b))
                        if (l != r):
                            Code02_Convict2.merge(l, r)
                j = jcast('int', (j + 1))
            ans = jcast('long', Code02_Convict2.compute())
            if (ans == 0):
                jcall(out, '_java_write_1', 'Gensokyo ')
            else:
                if (ans > Code02_Convict2.k):
                    jcall(out, '_java_write_1', 'Hell ')
                else:
                    jcall(out, '_java_write_1', 'Heaven ')
            jcall(out, 'println', ans)
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
            raise TypeError("No matching overload for Code02_Convict2.FastReader.FastReader")


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
            if (self.ptr == Code02_Convict2.FastWriter.BUF_SIZE):
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
            if (jcast('int', jadd(self.ptr, 21)) >= Code02_Convict2.FastWriter.BUF_SIZE):
                self.innerflush()
            if (x < 0):
                self._java_write_0(jcast('byte', jchar('-')))
                x = jcast('long', jcast('long', (-x)))
            d = jcast('int', Code02_Convict2.FastWriter.countDigits(x))
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
            self.buf = jarray('byte', [Code02_Convict2.FastWriter.BUF_SIZE])
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
            raise TypeError("No matching overload for Code02_Convict2.FastWriter.FastWriter")

        def write(self, *args):
            _java_choice = jselect(args, [['byte'], ['String'], ['long']], [False, False, False])
            if _java_choice == 0:
                return self._java_write_0(*args)
            if _java_choice == 1:
                return self._java_write_1(*args)
            if _java_choice == 2:
                return self._java_write_2(*args)
            raise TypeError("No matching overload for Code02_Convict2.FastWriter.write")

        def writeln(self, *args):
            _java_choice = jselect(args, [['long'], []], [False, False])
            if _java_choice == 0:
                return self._java_writeln_0(*args)
            if _java_choice == 1:
                return self._java_writeln_1(*args)
            raise TypeError("No matching overload for Code02_Convict2.FastWriter.writeln")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


def _java_lambda_9(c, self):
    jset(self.buf, ((_java_obj_10 := self), (_java_key_11 := 'ptr'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4], jcast('byte', c))
    if (self.ptr == Code02_Convict2.FastWriter.BUF_SIZE):
        self.innerflush()

Code02_Convict2.MAXN = jcast('int', 2000001)
Code02_Convict2.t = jcast('int', 0)
Code02_Convict2.w = jcast('int', 0)
Code02_Convict2.n = jcast('int', 0)
Code02_Convict2.m = jcast('int', 0)
Code02_Convict2.k = jcast('long', 0)
Code02_Convict2.num = jarray('long', [Code02_Convict2.MAXN])
Code02_Convict2.up = jarray('int', [Code02_Convict2.MAXN])
Code02_Convict2.left = jarray('int', [Code02_Convict2.MAXN])
Code02_Convict2.right = jarray('int', [Code02_Convict2.MAXN])
Code02_Convict2.dist = jarray('int', [Code02_Convict2.MAXN])
Code02_Convict2.father = jarray('int', [Code02_Convict2.MAXN])
Code02_Convict2.FastWriter.BUF_SIZE = jcast('int', jcast('int', (1 << (13 & 31))))

if __name__ == '__main__':
    Code02_Convict2.main([])
